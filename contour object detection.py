import numpy as np
import cv2

img = cv2.imread('detect_blob.png' ,1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# now we will create a binary image
thresh  = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
cv2.imshow('binary', thresh)

# NOTE: contours takes binary image input
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

# contours returns => list of individual contours
# each contour is a list of points which describes parameter of object

img2 = img.copy()
index = -1 # index => index of contour we want to draw ,-1 for all contours
thickness = 4
color = (255, 0 ,255) # pink

# contours are drawn over an image , here img2

cv2.drawContours(img2, contours, index, color, thickness) # overlapping contours and img2
cv2.imshow("Contours",img2 )


cv2.waitKey(0)
cv2.destroyAllWindows()