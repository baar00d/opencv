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

    #cv2.imshow('frame', frame)
    cv2.imshow('res', res)

    median = cv2.medianBlur(res,15 )
    cv2.imshow('median ', median)

    gauss = cv2.GaussianBlur(res , (15,15) ,0)
    cv2.imshow('gaussian blur', gauss)

    kernel = np.ones((15,15),np.float32)/225        # 15 X 15 = 225
    smooth = cv2.filter2D(res, -1, kernel)
    cv2.imshow('smooth',smooth)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()