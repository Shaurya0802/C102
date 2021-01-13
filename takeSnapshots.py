import cv2
import time
import sys

def takeSnapshot():
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("newpic.jpg", frame)
        result = False

    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
takeSnapshot()
sys.exit()