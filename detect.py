import cv2
import math
from ultralytics import YOLO
import define

def init_model():
    print(f"Loading YOLO model from: {define.MODEL_PATH}")
    try:
        model = YOLO(define.MODEL_PATH)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def detect_process(frame, model):
    detected_name = ""
    
    results = model(frame, stream=True, verbose=False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            conf = math.ceil((box.conf[0] * 100)) / 100

            cls = int(box.cls[0])
            current_name = model.names[cls] 
            
            detected_name = current_name 

            cv2.rectangle(frame, (x1, y1), (x2, y2), define.BLUE, define.THICKNESS)
            cv2.putText(frame, f"{current_name} {conf}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, define.BLUE, 2)


    return frame, detected_name