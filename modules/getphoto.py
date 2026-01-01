import cv2
import os
import numpy as np
from . import define

class PhotoCollector:
    def __init__(self, folder="photo"):
        self.save_folder = folder
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

    def _get_next_filename(self):
        i = 1
        while True:
            filename = f"{self.save_folder}/Capture{i:02d}.jpg"
            if not os.path.exists(filename):
                return filename
            i += 1

    def process(self, frame, key):
        b, g, r = cv2.split(frame)
        gray_enhanced = np.maximum(np.maximum(r, g), b)
        display_frame = cv2.cvtColor(gray_enhanced, cv2.COLOR_GRAY2BGR)
        
        h, w, _ = display_frame.shape
        
        cv2.putText(display_frame, "MODE [4]: PHOTO COLLECTION", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, define.GREEN, 2)
        
        cx, cy = w // 2, h // 2
        size = 100
        cv2.rectangle(display_frame, (cx - size, cy - size), (cx + size, cy + size), define.GREEN, 2)

        if key == ord('c'):
            filename = self._get_next_filename()
            cv2.imwrite(filename, gray_enhanced)
            print(f"{define.T_GREEN}Saved: {filename}{define.T_RS}")
            
            cv2.rectangle(display_frame, (0, 0), (w, h), (255, 255, 255), -1)
            cv2.putText(display_frame, "SAVED!", (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        return display_frame