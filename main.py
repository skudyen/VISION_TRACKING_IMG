import cv2
import define
import math


if not define.capt.isOpened():
    print("Cannot open camera")
    exit()

print(define.msg_start)

while True:
    ret, frame = define.capt.read()

    if not ret:
        print("ไม่สามารถรับภาพจากกล้องได้ (Can't receive frame)")
        break
    
    cv2.rectangle(frame, (50, 10), (200, 50), define.NEON_GREEN, 2)
    cv2.imshow("PROGRAM", frame)
    if cv2.waitKey(1) == define.button :
        break

print("Bye Bye !!!")

define.capt.release()
cv2.destroyAllWindows()
