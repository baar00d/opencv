import numpy as np
import cv2

bw = cv2.imread('detect_blob.png', 0) # 0 for B/W image
height,width = bw.shape[0:2]
cv2.imshow('original BW', bw)

binary = np.zeros([height,width,1],'uint8') # empty matrix, unint for 8 bit image,
# 3-dimension array ,
# First two Dimens. are location of pixel
# 3rd dimension contains value between (0,255), 1==> single channel, 3==> three channel B,G,R

thresh = 80 # in 8 bit image maximum value is 266

#### slow method ################

for row in range(0,height):
    for col in range(0,width):
        if bw[row][col]>thresh:
            binary[row][col]=255 # 255 for complete WHITE

cv2.imshow('Slow Binary', binary)

##################################

ret,thresh = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("CV Threshold",thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
