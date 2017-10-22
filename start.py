import numpy as np
import matplotlib as plt
import cv2

img = cv2.imread('watch.jpg',0) # 0 for grayscale(B/W) 1 for color
# IMREAD_UNCHANGED (-1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()