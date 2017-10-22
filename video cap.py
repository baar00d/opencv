import cv2
import numpy as np

cap = cv2.VideoCapture(0)                           # caputure vid using default cam(0)

while True:
    _, frame = cap.read()                         # Frame 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Frame 2

    cv2.imshow('Frame',frame)                       # Display Frame 1
    cv2.imshow('Gray Frame',gray)                   # Display Frame 2

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()  # to release webcam
