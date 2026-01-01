import numpy as np
import cv2 
from . import define

def draw_reg(frame, obj_name="N/A"):
    cv2.rectangle(frame,
                define.RT_TOPC,
                define.RT_UNDC,
                define.GREEN,
                define.THICKNESS)

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

def draw_msg(frame, status, obj_name, conf, pixel_size):
    text_x, text_y = 10, 30
    cv2.putText(frame,
                f"DETECTION : [ {status} ]",
                (text_x, text_y),
                cv2.FONT_HERSHEY_DUPLEX,
                0.7,
                define.RED,
                define.THICKNESS)
    cv2.putText(frame,
                f"NAME : [ {obj_name} ]",
                (text_x, text_y + 20),
                cv2.FONT_HERSHEY_DUPLEX,
                0.7,
                define.RED,
                define.THICKNESS)
    cv2.putText(frame,
                f"MATCH : [ {conf} %]",
                (text_x, text_y + 40),
                cv2.FONT_HERSHEY_DUPLEX,
                0.7,
                define.RED,
                define.THICKNESS)
    cv2.putText(frame,
                f"BOUNDING BOX PIXEL : [{pixel_size}]",
                (text_x, text_y + 60),
                cv2.FONT_HERSHEY_DUPLEX,
                0.7,
                define.RED,
                define.THICKNESS)
    return frame