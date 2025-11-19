import cv2

# เปิดกล้องตัวที่ 0
cap = cv2.VideoCapture(0)

# ใช้ MJPG เพื่อให้ C920 ส่ง 1080p ได้
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

# ตั้งค่าความละเอียดที่ต้องการเช็ค
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# อ่านเฟรมแรกเพื่อตรวจสอบขนาด
ret, frame = cap.read()

if not ret:
    print("❌ ไม่สามารถอ่านภาพจากกล้องได้")
    cap.release()
    exit()

h, w, _ = frame.shape

print("\n========== CAMERA CHECK ==========")
print(f"Frame Resolution (Actual): {w} x {h}")
print("==================================\n")


print("\n========== CAMERA CHECK ==========")
print(f"Frame Resolution (Actual): {w} x {h}")
print("==================================\n")

# แสดงภาพให้เห็นจริง
cv2.imshow("CHECK SIZE", frame)

# แสดงภาพให้เห็นจริง
cv2.imshow("CHECK SIZE", frame)

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
