import numpy as np
import cv2 
import define

def draw_reg(frame, text = None):
    cv2.rectangle(frame,
                define.RT_TOPC,
                define.RT_UNDC,
                define.GREEN,
                define.THICKNESS)
    if text:
        x, y = define.RT_TOPC 
        
        cv2.putText(frame, f"TARGET: {text}", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, define.GREEN, 2)
    else:
        x, y = define.RT_TOPC
        cv2.putText(frame, "Searching...", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 2)
    
    return frame

def draw_line(frame):
    x1, y1 = define.RT_TOPC
    x2, y2 = define.RT_UNDC

    center_x = (x1 + x2)//2
    center_y = (y1 + y2)//2

    size = 20

    cv2.line(
        frame,
        (center_x - size, center_y),
        (center_x + size, center_y),
        define.RED,
        define.THICKNESS
    )

    cv2.line(
        frame,
        (center_x, center_y - size),
        (center_x, center_y + size),
        define.RED,
        define.THICKNESS
    )

    return frame