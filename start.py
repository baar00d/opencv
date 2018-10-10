import numpy as np
import matplotlib as plt
import cv2

img = cv2.imread('watch.jpg',0) # 0 for grayscale(B/W) 1 for color
# IMREAD_UNCHANGED (-1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
