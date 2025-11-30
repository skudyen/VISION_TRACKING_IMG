import cv2
import math

# DEFINE COLORS and THICKNESS
GREEN = (100, 235, 52)
BLUE = (255, 10, 10)
RED = (0, 0, 255)

# MODEL PATH
MODEL_PATH = "import_model/best.pt"

# DEFINE POSITION,DISPLAY,SIZE
DISP_WID = 640
DISP_HEI = 480

RT_TOPC = (200, 100)
RT_UNDC = (450, 350)
DEF_CROS_Y = ()
DEF_CROS_P = ()

THICKNESS = 2

# DEFINE CAMERA

def init_camera():
    capt = cv2.VideoCapture(0, cv2.CAP_V4L2)
    if not capt.isOpened():
        capt = cv2.VideoCapture(1, cv2.CAP_V4L2)
    
    capt.set(cv2.CAP_PROP_FRAME_WIDTH, DISP_WID)
    capt.set(cv2.CAP_PROP_FRAME_HEIGHT, DISP_HEI)

    return capt

# capt = cv2.VideoCapture(0, cv2.CAP_V4L2)
# if not capt.isOpened():
#     capt = cv2.VideoCapture(1, cv2.CAP_V4L2)

# set_wid = capt.set(cv2.CAP_PROP_FRAME_HEIGHT, DISP_WID)
# set_hei = capt.set(cv2.CAP_PROP_FRAME_WIDTH, DISP_HEI)

# MESSAGE TEXT
msg_start = (
    "====== 🦛[ Welcome to Program ]🦛 =======\n"
    "Program has start running ... \n"
    "_________________________________________________\n\n"
    "[📚 GUIDE 📚]\n"
    "  + If you need to close program press [x] button.\n"
    "_________________________________________________\n\n"
)

msg_err_01 = ("CANNOT OPEN CAMERA")
msg_err_02 = ("CANNOT RECEIVE FRAME")
msg_err_03 = ("")

msg_exit = ("Exit ...\n\n\n Bye Bye !!!")

# DEFINE BUTTON
button = ord('x')