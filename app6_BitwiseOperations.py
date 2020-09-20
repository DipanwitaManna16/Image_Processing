import numpy as np
import cv2

#-----------Basic Bitwise Operations(MASKING)-------------

'''
first = np.zeros((512,512) , np.uint8)
cv2.circle(first , (200,200) , 100, (255,255,255) , -1)

second = np.zeros((512,512),np.uint8)
cv2.circle(second , (200,200) , 100, (255,255,255) , -1)

#Bitwise Operations

imgOr = cv2.bitwise_or(first,second)
imgAnd = cv2.bitwise_and(first , second)
imgXor = cv2.bitwise_xor(first , second)
imgNot = cv2.bitwise_not(first , second)

final = np.hstack((first , second , imgXor))
'''

#---------------Bitwise Operations on an image-------------------------

img = cv2.imread('Images\WhatsApp Image 2020-09-06 at 10.46.51 AM.jpeg')


first = np.zeros((512,512,3), np.uint8)
cv2.circle(first , (200,200), 100, (255,255,255) , -1)

#imgAnd = cv2.bitwise_and(img ,first)
#imgAnd = cv2.bitwise_or(img ,first)
#imgXor = cv2.bitwise_xor(img ,first)
imgNot = cv2.bitwise_not(img ,first)

final = np.hstack((img , imgNot))

cv2.imshow("image" , final)
cv2.waitKey(0)