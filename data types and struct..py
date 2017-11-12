import numpy as np
import cv2

black = np.zeros([150,200,1] ,'uint8')
# 150px tall, 200px wide, has only one channel (only one value ie. 0 wiz 'Black')
# type unsigned integer ,idicates that range of values that allow in this matrix
# will be 0 to 255

cv2.imshow('Black',black)

#to see first pixel
print(black[0,0,:]) # we want see to all the value in that pixel

ones = np.ones([150,200,3],'uint8')
cv2.imshow('Ones',ones)
print(ones[0,0,:])

white = np.ones([150,200,3],'uint16')
white *= (2**16 -1) # to use maximum value
cv2.imshow('White',white)
print(white[0,0,:])

color = ones.copy()
color[:,:] = (255,0,0) #BGR format
cv2.imshow('BLue',color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()



