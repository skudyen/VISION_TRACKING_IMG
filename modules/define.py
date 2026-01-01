import cv2
import os

# --- COLORS (B, G, R) ---
GREEN = (100, 235, 52)
BLUE = (255, 10, 10)
RED = (0, 0, 255)
ORANGE = (0, 165, 255)
YELLOW = (0, 255, 255)
# --- TERMINAL COLORS ---
T_GREEN = "\033[32m"
T_BLUE = "\033[34m"
T_RED = "\033[31m"
T_ORANGE = "\033[38;5;208m"
T_RS = "\033[0m"
T_MAGENTA = "\033[35m"
T_CYAN = "\033[36m"
T_YELLOW = "\033[33m"

# --- HELPER FUNCTIONS ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

def rainbow(text):
    colors = ["\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m"]
    result = ""
    for i, char in enumerate(text):
        if char != " ":
            result += colors[i % len(colors)] + char
        else:
            result += char
    return result + "\033[0m"

# --- TEXT MESSAGES ---
msg_header = (
    f"======  {rainbow('Welcome to Program')} ]=======\n"
    f"{T_GREEN}Program has start running ...{T_RS} \n"
    "_________________________________________________\n\n"
    "[ GUIDE ]\n"
    f"  {T_GREEN}+ If you need to close program press{T_RS} [x] {T_GREEN}button.{T_RS}\n"
    f"\n  [ INTERFACE GUIDE ]\n"
    f"     {T_ORANGE}DETECTION{T_RS} : \"Shows {T_GREEN}True{T_RS} when an object is detected, and {T_RED}False{T_RS} when not.\" \n"
    f"     {T_ORANGE}NAME{T_RS}      : \"Shows the object name.\" \n"
    f"     {T_ORANGE}MATCH{T_RS}     : \"Shows how closely it matches, in percentage (%).\" \n"
    f"     {T_ORANGE}BBP{T_RS}       : \"Shows pixels size of object that found.\" \n"
    f"  ( BBP : Bounding Box Pixel ) \n"
    "_________________________________________________\n\n"
    f"  {T_GREEN}+ CHANGE PROGRAM MODES{T_RS} \n"
    f"    Type {T_MAGENTA}Number{T_RS} in terminal than press enter to change mode.\n"
    f"     [1] : Normal Mode \n"
    f"     [2] : Log Mode \n"
    f"     [3] : Setting {rainbow('COMING SOON ...')} \n"
    f"     [4] : Capture Mode (For Training Data)"
)

msg_err_01 = ("CANNOT OPEN CAMERA")
msg_err_02 = ("CANNOT RECEIVE FRAME")
msg_exit = f"{T_RED}Exit ... {T_RS}"

# --- CONFIG ---
MODEL_PATH = "models/best.pt" 
CONF_FILTER = 65
ARDUINO_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# --- DISPLAY ---
DISP_WID = 640
DISP_HEI = 480
RT_TOPC = (200, 100)
RT_UNDC = (450, 350)
THICKNESS = 2