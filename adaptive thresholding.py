## limits of simple thresholding : when there's uneven lighting in image.

import numpy as np
import cv2

img = cv2.imread('sudoku.png',0) # 0 for black and white
cv2.imshow('original',img)

ret,thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow('Basic Binary',thresh_basic)

thresh_adapt = cv2.adaptiveThreshold(img, 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
cv2.imshow('Adaptive Threshold',thresh_adapt)

## image as input,

## maximum pixel value of 255 

## cv2.ADAPTIVE_THRESH_GAUSSIAN, 

## cv2.THRESH_BINARY,

## followed by the neighborhood parameter indicating how far or
## what the localization of where the adaptive thresholding will act over.
## This is a value which we can put as 115 and

## then a value of 1,
## which is a mean subtraction from the end result.

cv2.waitKey(0)
cv2.destroyAllWindows()
