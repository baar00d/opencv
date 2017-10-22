import cv2
import numpy as np

cap = cv2.VideoCapture(0)                           # caputure vid using default cam(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')           # codec
out = cv2.VideoWriter_fourcc('output.avi', fourcc , 20.0 , (640,480)) #output

while True:
    ret, frame = cap.read()                         # Frame 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Frame 2

    out.write(frame)                                # writing Frame 1

    cv2.imshow('Frame',frame)                       # Display Frame 1
    cv2.imshow('gray',gray)                         # Display Frame 2

    if cv2.waitKey(1) & 0xFF == ord('q'):           # press q to quit
        break

cap.release()
cv2.destroyAllWindows()