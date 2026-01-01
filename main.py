import cv2
import time
import os
from modules import define
from modules import draw
from modules.modes import ModeManager
from modules.detect import ObjectDetector
from modules.getphoto import PhotoCollector
from modules.serials import SerialHandler
from modules.getlog import LogMonitor

class SmartCamApp:
    def __init__(self):
        # ไม่ต้อง print header ตรงนี้แล้ว เพราะเดี๋ยวโดน detector ลบทิ้ง
        # define.clear_screen() <--- ลบออก
        # print(define.msg_header) <--- ลบออก

        self.setup_camera()
        self.serial = SerialHandler()
        self.modes = ModeManager()
        self.detector = ObjectDetector(serial_handler=self.serial) 
        self.collector = PhotoCollector()
        self.logger = LogMonitor(self.serial)
        
        self.running = True

    def setup_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.cap = cv2.VideoCapture(1)
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, define.DISP_WID)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, define.DISP_HEI)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    def run(self):
        if not self.cap.isOpened():
            print(define.msg_err_01)
            return
            
        if self.detector.model is None:
             print("Error: Could not load YOLO model.")
             return

        cv2.namedWindow("PROGRAM", cv2.WINDOW_NORMAL)

        # --- แก้ตรงนี้ครับ! ---
        # หลังจากโหลดทุกอย่างเสร็จแล้ว ให้เคลียร์จอแล้วโชว์ Guide ค้างไว้เลย
        define.clear_screen()
        print(define.msg_header)
        # -------------------

        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                print(define.msg_err_02)
                break

            key = cv2.waitKey(1) & 0xFF
            current_mode = self.modes.check_input(key)
            
            final_frame = frame
            obj_name = "N/A"

            if current_mode == ModeManager.CAPTURE:
                final_frame = self.collector.process(frame, key)
                
            else:
                final_frame, obj_name = self.detector.process(frame)
                
                if current_mode == ModeManager.LOG:
                    final_frame = self.logger.process(final_frame, obj_name)
                else:
                    final_frame = draw.draw_line(final_frame)
                    final_frame = draw.draw_reg(final_frame, obj_name)

            cv2.putText(final_frame, f"MODE: {self.modes.get_name()}", (10, 470), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, define.ORANGE, 2)
            
            cv2.imshow("PROGRAM", final_frame)

            if key == ord('x') or key == ord('q'):
                self.running = False

        self.cleanup()

    def cleanup(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print("\n")
        print(define.msg_exit)
        time.sleep(2)
        define.clear_screen()

if __name__ == "__main__":
    app = SmartCamApp()
    app.run()