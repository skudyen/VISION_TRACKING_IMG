import serial
import time
from . import define

class SerialHandler:
    def __init__(self):
        self.ser = None
        self.last_sent = 2
        
        self.mapping = {}
        for i in range(1, 16):
            self.mapping[f"T{i}"] = i 
            self.mapping[f"F{i}"] = i + 15 

        try:
            self.ser = serial.Serial(define.ARDUINO_PORT, define.BAUD_RATE, timeout=1)
            print(f"{define.T_GREEN}Arduino Connected at {define.ARDUINO_PORT}{define.T_RS}")
        except Exception as e:
            print(f"{define.T_RED}Arduino Not Found ({e}){define.T_RS}")

    def send_signal(self, detected_name):
        """รับชื่อวัตถุเข้ามา แปลงเป็นเลข แล้วส่งออก Serial"""
        if self.ser is None:
            return

        if detected_name in self.mapping:
            value_to_send = self.mapping[detected_name]
            
            try:
                self.ser.write(bytes([value_to_send]))
                #print(f"Sent Serial: {detected_name} -> {value_to_send}")
                
            except Exception as e:
                print(f"Serial Write Error: {e}")