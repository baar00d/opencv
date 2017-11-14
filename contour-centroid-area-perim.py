import cv2
import numpy as np

img = cv2.imread('lion.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i =4
cv2.drawContours(img,contours,i,(0,255,0),3) # Contour(s) u want 2 draw, -1 for all contr.

print 'area= ',cv2.contourArea(contours[i])
print 'perimeter= ',cv2.arcLength(contours[i],True)

M = cv2.moments(contours[i])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print 'centroid=', cx, ',', cy
cv2.circle(img,(cx,cy),5,(255,0,0),3)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

