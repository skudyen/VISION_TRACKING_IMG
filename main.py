import cv2
import define
import draw

capt = define.init_camera()

if not capt.isOpened():
    print(define.msg_err_01)
    exit()

print(define.msg_start)

while True:
    ret, frame = capt.read()
    
    if not ret:
        print(define.msg_err_02)
        break
    
    frame = draw.draw_line(frame)
    frame = draw.draw_reg(frame)
    cv2.imshow("PROGRAM", frame)
    if cv2.waitKey(1) == define.button:
        break

print(define.msg_exit)

capt.release()
cv2.destroyAllWindows()
