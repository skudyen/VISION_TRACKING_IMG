import numpy as np
import cv2 
import define

def draw_reg(frame):
    cv2.rectangle(frame,
                define.RT_TOPC,
                define.RT_UNDC,
                define.GREEN,
                define.THICKNESS)
    return frame

def draw_line(frame):
    cv2.line(frame,
             (0, 20), 
             (300, 20), 
             define.BLUE, 
             define.THICKNESS)
    cv2.line(frame, (451, 230), (500, 230), define.BLUE, define.THICKNESS)
    return frame