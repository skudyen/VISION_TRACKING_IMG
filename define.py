import cv2
import math

# DEFINE POSITION and DISPLAY
DISP_WID = 1920
DISP_HEI = 1080

# DEFINE CAMERA
capt = cv2.VideoCapture(0)
set_wid = capt.set(cv2.CAP_PROP_FRAME_HEIGHT, DISP_WID)
set_hei = capt.set(cv2.CAP_PROP_FRAME_WIDTH, DISP_HEI)

# DEFINE COLORS and THICKNESS
NEON_GREEN = (100, 235, 52)
BLUE = (54, 137, 214)
RED = (224, 31, 31)

# MESSAGE TEXT
msg_start = (
    "====== 🦛[ Welcome to Program ]🦛 =======\n"
    "Program has start running ... \n"
    "_________________________________________________\n\n"
    "[📚 GUIDE 📚]\n"
    "  + If you need to close program press [x] button.\n"
    "_________________________________________________\n\n"
)

# DEFINE BUTTON
button = ord('x')