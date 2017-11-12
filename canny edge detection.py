import numpy as np
import cv2

img = cv2.imread("tomatoes.jpg",1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convers to HSV
# HSV is channel image
# hsv[:,:,0] => hue channel , hue values of all pixels
# hsv[:,:,1] => saturation channel
# hsv[:,:,2] => Value channel

thresh  = 25
# hue values 0-25 is around red and at very high level 250-255
res,thresh = cv2.threshold(hsv[:,:,0], thresh, 255, cv2.THRESH_BINARY_INV)
# NOTE: its THRESH_BINARY_INV which includes values which are less LESS than threshold value
# if hue value 0-25(red region) make it compelete white
cv2.imshow('Thresh',thresh)

# We see tomatoes blobbed together => no edges
# contours will see this as one object

# Canny Edge technique
edges = cv2.Canny(img,100,70)
# threshold values of edges between 100,70
cv2.imshow("Canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()