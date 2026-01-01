import cv2
import math
import numpy as np
from ultralytics import YOLO
import time
from . import define
from . import draw

class ObjectDetector:
    def __init__(self, serial_handler=None):
        self.serial = serial_handler
        
        print(f"{define.T_ORANGE}Loading YOLO model from: {define.MODEL_PATH}")
        time.sleep(1)
        define.clear_screen()
        time.sleep(1)
        
        try:
            self.model = YOLO(define.MODEL_PATH)
            print(define.rainbow(f"Model loaded successfully!"))
            time.sleep(1)
            define.clear_screen()
            time.sleep(1)       
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def _get_color(self, img_patch):
        """ฟังก์ชันช่วยแยกสี (เบาเครื่องมาก)"""

        if img_patch.size == 0: return "N/A", (128, 128, 128)

        avg_b = np.mean(img_patch[:, :, 0])
        avg_g = np.mean(img_patch[:, :, 1])
        avg_r = np.mean(img_patch[:, :, 2])

        if avg_b > 180 and avg_g > 180 and avg_r > 180:
            return "WHITE", (255, 255, 255) 

        elif avg_r > avg_b and avg_r > avg_g:
            return "RED", (0, 0, 255)
        

        elif avg_b > avg_r and avg_b > avg_g:
            return "BLUE", (255, 0, 0)

        return "UNKNOWN", (128, 128, 128)

    def process(self, frame):
        if self.model is None:
            return frame, "N/A"

        b, g, r = cv2.split(frame)
        gray_enhanced = np.maximum(np.maximum(r, g), b)
        display_frame = cv2.cvtColor(gray_enhanced, cv2.COLOR_GRAY2BGR)

        detected_name = "N/A"
        conf_value = "N/A"
        detection_status = "False"
        pixel_size_value = "N/A"

        x_start, y_start = define.RT_TOPC
        x_end, y_end = define.RT_UNDC
        ROI_FRAME = display_frame[y_start:y_end, x_start:x_end]

        results = self.model(ROI_FRAME, stream=True, verbose=False, imgsz=256)

        best_conf = 0

        for r in results:
            boxes = r.boxes
            for box in boxes:
                conf = math.ceil(box.conf[0] * 100)
                if conf < define.CONF_FILTER:
                    continue 
                
                detection_status = "True"

                if conf > best_conf:
                    best_conf = conf
                    conf_value = f"{conf:.2f}"
                    
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    box_width = x2 - x1
                    box_height = y2 - y1
                    pixel_size_value = f"{box_width}x{box_height}"

                    cls = int(box.cls[0])
                    detected_name = self.model.names[cls] 

                    if self.serial:
                        self.serial.send_signal(detected_name)

                    original_x1 = x1 + x_start
                    original_y1 = y1 + y_start
                    original_x2 = x2 + x_start
                    original_y2 = y2 + y_start

                    check_x = original_x2 + 5
                    check_y = (original_y1 + original_y2) // 2
                    
                    paper_color = "N/A"
                    ui_color = (128, 128, 128)
                    
                    try:
                        patch = frame[check_y-1:check_y+2, check_x-1:check_x+2]
                        paper_color, ui_color = self._get_color(patch)
                    except:
                        pass 

                    cv2.rectangle(display_frame, (original_x1, original_y1), (original_x2, original_y2), define.BLUE, define.THICKNESS)

                    cv2.putText(display_frame, f"{detected_name} {conf:.2f}%", (original_x1, original_y2 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, define.BLUE, 2)
                    
                    cv2.rectangle(display_frame, (check_x-2, check_y-2), (check_x+2, check_y+2), ui_color, -1) # -1 คือระบายทึบ

                    cv2.putText(display_frame, f"COLOR: {paper_color}", (check_x + 10, check_y + 5), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, ui_color, 2)

        display_frame = draw.draw_msg(display_frame, detection_status, detected_name, conf_value, pixel_size_value)
        return display_frame, detected_name