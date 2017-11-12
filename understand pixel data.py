import numpy as np
import cv2

img = cv2.imread('logo.png',1) # 1 for color

print(img)
print('img[0][0] ==>',img[0][0])
print('TyPE img ==> ',type(img))
print('Length img ==> ',len(img))
print('length of img[0][0] ie.channel ==>',len(img[0][0]))
print('Shape img ==> ' ,img.shape)



