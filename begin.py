import numpy as np
import cv2

img = cv2.imread('logo.png')
cv2.namedWindow('Image',cv2.WINDOW_NORMAL) # creating named window
cv2.imshow('Image',img)

cv2.waitKey(0) # wait untill user interact with env.

cv2.imwrite('output.jpg',img)
