from . import define

class ModeManager:
    NORMAL = 1
    LOG = 2
    SETTING = 3
    CAPTURE = 4

    def __init__(self):
        self.current_mode = self.NORMAL

    def check_input(self, key):
        if key == ord('1') and self.current_mode != self.NORMAL:
            self.current_mode = self.NORMAL
            define.clear_screen() # เคลียร์จอทีนึงตอนกลับมาโหมดปกติ
            print(f"Mode Switched to: {define.T_GREEN}NORMAL MODE{define.T_RS}")

        elif key == ord('2') and self.current_mode != self.LOG:
            self.current_mode = self.LOG
            define.clear_screen() 
            print(f"Mode Switched to: {define.T_YELLOW}LOG MODE (Real-time){define.T_RS}")

        elif key == ord('3') and self.current_mode != self.SETTING:
            self.current_mode = self.SETTING
            print(f"Mode Switched to: {define.T_CYAN}SETTING MODE (Demo){define.T_RS}")
            
        elif key == ord('4') and self.current_mode != self.CAPTURE:
            self.current_mode = self.CAPTURE
            print(f"Mode Switched to: {define.T_MAGENTA}CAPTURE MODE{define.T_RS}")

        return self.current_mode

    def get_name(self):
        if self.current_mode == self.NORMAL: return "NORMAL"
        if self.current_mode == self.LOG: return "LOG"
        if self.current_mode == self.SETTING: return "SETTING"
        if self.current_mode == self.CAPTURE: return "CAPTURE"
        return "UNKNOWN"