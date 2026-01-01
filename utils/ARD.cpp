// void setup() {
//   Serial.begin(9600);
//   pinMode(13, OUTPUT);
// }

// void loop() {
//   if (Serial.available() > 0) {
//     int data = Serial.read();

//     // T1 - T15 (ค่า 1-15)
//     if (data >= 1 && data <= 15) {
//       // ทำงานสำหรับ T (เช่น T15 คือ data == 15)
//       // Serial.print("Detected T: ");
//       // Serial.println(data);
//     } 
//     // F1 - F15 (ค่า 16-30)
//     else if (data >= 16 && data <= 30) {
//       // ทำงานสำหรับ F (เช่น F1 คือ data == 16)
//       // Serial.print("Detected F: ");
//       // Serial.println(data - 15); // ถ้าอยากรู้ว่าเป็น F ลำดับที่เท่าไหร่ก็ลบ 15 ออก
//     }
//   }
// }