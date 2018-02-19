import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_face_gray = gray_frame[y:y+h, x:x+w]
        roi_face_color = frame[y:y+h, x:x+w]
        eyes = eye_classifier.detectMultiScale(roi_face_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()