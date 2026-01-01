from . import define

class ModeManager:
    # ค่าคงที่สำหรับโหมดต่างๆ
    NORMAL = 1
    LOG = 2
    SETTING = 3
    CAPTURE = 4

    def __init__(self):
        # จุดสำคัญ! ต้องมีการประกาศตัวแปรนี้ตรงนี้
        self.current_mode = self.NORMAL

    def _refresh_screen(self, msg):
        """ฟังก์ชันช่วยเคลียร์จอ + วาด Header + วาดข้อความแจ้งเตือน"""
        define.clear_screen()
        print(define.msg_header) 
        print(f"\n{msg}\n")     

    def check_input(self, key):
        # ป้องกันกรณีลืม init (กันเหนียว)
        if not hasattr(self, 'current_mode'):
            self.current_mode = self.NORMAL

        if key == ord('1') and self.current_mode != self.NORMAL:
            self.current_mode = self.NORMAL
            self._refresh_screen(f"Mode Switched to: {define.T_GREEN}NORMAL MODE{define.T_RS}")

        elif key == ord('2') and self.current_mode != self.LOG:
            self.current_mode = self.LOG
            self._refresh_screen(f"Mode Switched to: {define.T_YELLOW}LOG MODE (Real-time){define.T_RS}")

        elif key == ord('3') and self.current_mode != self.SETTING:
            self.current_mode = self.SETTING
            self._refresh_screen(f"Mode Switched to: {define.T_CYAN}SETTING MODE (Demo){define.T_RS}")
            
        elif key == ord('4') and self.current_mode != self.CAPTURE:
            self.current_mode = self.CAPTURE
            self._refresh_screen(f"Mode Switched to: {define.T_MAGENTA}CAPTURE MODE{define.T_RS}")

        return self.current_mode

    def get_name(self):
        # ป้องกันกรณีลืม init (กันเหนียว)
        if not hasattr(self, 'current_mode'):
            self.current_mode = self.NORMAL
            
        if self.current_mode == self.NORMAL: return "NORMAL"
        if self.current_mode == self.LOG: return "LOG"
        if self.current_mode == self.SETTING: return "SETTING"
        if self.current_mode == self.CAPTURE: return "CAPTURE"
        return "UNKNOWN"