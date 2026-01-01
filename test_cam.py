import cv2
import time

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

last = time.time()
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("err")
        break

    count += 1
    if time.time() - last >= 1:
        print("FPS =", count)
        count = 0
        last = time.time()

    # *** COMMENT OUT imshow ***
    cv2.imshow("cam", frame)
    if cv2.waitKey(1) == ord('q'):
       break
