import time
import cv2
from . import define

class LogMonitor:
    def __init__(self, serial_handler):
        self.serial = serial_handler
        self.prev_time = time.time()
        self.frame_count = 0
        self.current_fps = 0

    def process(self, frame, detected_name):
        self.frame_count += 1
        current_time = time.time()
        elapsed = current_time - self.prev_time
        
        if elapsed >= 1.0: 
            self.current_fps = self.frame_count / elapsed
            self.frame_count = 0
            self.prev_time = current_time

        serial_value = "None"
        if self.serial and detected_name in self.serial.mapping:
            byte_val = self.serial.mapping[detected_name]
            serial_value = f"{byte_val} (0x{byte_val:02X})"

        log_msg = (
            f"\r{define.T_YELLOW}[LOG MODE]{define.T_RS} "
            f"FPS: {define.T_GREEN}{self.current_fps:.2f}{define.T_RS} | "
            f"OBJ: {define.T_CYAN}{detected_name:<5}{define.T_RS} | "
            f"SERIAL SEND: {define.T_MAGENTA}{serial_value}{define.T_RS}      " 
        )
        print(log_msg, end="", flush=True)

        cv2.putText(frame, "LOG MODE ACTIVATED (Check Terminal)", (10, 430), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, define.YELLOW, 2)

        return frame