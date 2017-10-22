import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    # we are using HSV for color range purpose , here hue is color value
    # it consist of all colors
    # saturation => intensity of that color
    # value => light
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # TO HSV format

    lower = np.array([90,90,50])
    upper = np.array([120,255,255])

    mask = cv2.inRange(hsv, lower , upper) # acc to main obect
    # mask is that portion of hsv frame which is under lower and upper range
    res = cv2.bitwise_and(frame , frame , mask=mask)
    # if mask in range(lower-upper) we get 1(WHITE) o/w 0(Black)
    # basically we are filtering import object

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release() #to release webcam
