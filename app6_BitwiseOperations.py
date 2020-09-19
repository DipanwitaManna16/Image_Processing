import numpy as np
import cv2

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

cv2.imshow("image" , final)
cv2.waitKey(0)