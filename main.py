import cv2
import define
import draw
import detect 

capt = define.init_camera()
model = detect.init_model()

if not capt.isOpened():
    print(define.msg_err_01)
    exit()

if model is None:
    print("Error: Could not load YOLO model.")
    exit()

print(define.msg_start)

cv2.namedWindow("PROGRAM", cv2.WINDOW_NORMAL)
cv2.resizeWindow("PROGRAM", 960, 540)

while True:
    ret, frame = capt.read()

    if not ret:
        print(define.msg_err_02)
        break
    frame, obj_name = detect.detect_process(frame, model)

    frame = draw.draw_line(frame)

    frame = draw.draw_reg(frame, obj_name)

    cv2.imshow("PROGRAM", frame)

    if cv2.waitKey(1) & 0xFF == define.button:
        break

print(define.msg_exit)

capt.release()
cv2.destroyAllWindows()