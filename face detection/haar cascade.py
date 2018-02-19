'''

Tuning Cascade Classifiers

ourClassifier.detectMultiScale(input image, Scale Factor , Min Neighbors)

Scale Factor Specifies how much we reduce the image size each time we scale.
E.g. in face detection we typically use 1.3. This means we reduce the image by 30% each time it’s scaled.
Smaller values, like 1.05 will take longer to compute, but will increase the rate of detection.

Min Neighbors Specifies the number of neighbors each potential window should have in order to consider it a positive detection.
Typically set between 3-6. It acts as sensitivity setting, low values will sometimes detect multiples faces over a single face.
High values will ensure less false positives, but you may miss some faces.

'''

import numpy as np
import cv2

image = cv2.imread('images/front_face.png')

height, width = image.shape[:2]
#image = cv2.resize(img, (width / 3, height / 3), interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## create classifier
face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
## classifier return ROI
## contain top-left bottom-right
faces = face_classifier.detectMultiScale(gray,1.3,5) ## store array of faces

if faces is (): # empty/NO face
    print "NO Face Found"

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2) ## draw rectangle over face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y + h, x:x + w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh),(0,255,0), 2)

cv2.imshow('Face', image)

cv2.waitKey(0)
cv2.destroyAllWindows()