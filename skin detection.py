import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v),axis =1)
cv2.imshow('split HSV',hsv_split)
cv2.resizeWindow("split HSV",900,900)

cv2.waitKey()
cv2.destroyAllWindows()

