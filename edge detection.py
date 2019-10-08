import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    # we are using HSV for color range purpose , here hue is color value
    # it consist of all colors
    # saturation => intensity of that color
    # value => light
    cv2.resize(frame, fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # TO HSV format


    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release() #to release webcam
