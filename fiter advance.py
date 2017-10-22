import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower = np.array([90,90,50])
    upper = np.array([120,255,255])

    mask = cv2.inRange(hsv, lower , upper)
    res = cv2.bitwise_and(frame , frame , mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask , kernel ,iterations=1)  # removes differnt value in the region of slider.Reduces noise
    dilation = cv2.dilate(mask, kernel ,iterations=1) # opposite of erosion

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    # False positive => noise in the background
    # False negatice => noise in main object
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # removes False positive
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # removes False neg
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
