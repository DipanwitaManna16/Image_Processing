import numpy as np
import cv2

#---------------Converting the image into Black&White---------------
#Binary Image
#Shape Detection

img = cv2.imread("Images\WhatsApp Image 2020-09-06 at 10.46.51 AM.jpeg" , 0)  # direct grey image
ret , thresh1 = cv2.threshold(img , 127 , 255 , cv2.THRESH_BINARY)
ret1 , thresh2 = cv2.threshold(img , 127 , 255 , cv2.THRESH_BINARY_INV)
ret2 , thresh3 = cv2.threshold(img , 127 , 255 , cv2.THRESH_TRUNC)
ret3 , thresh4 = cv2.threshold(img , 127 , 255 , cv2.THRESH_TOZERO)
ret4 , thresh5 = cv2.threshold(img , 127 , 255 , cv2.THRESH_TOZERO_INV)

final = np.hstack((  thresh4 , thresh5))

cv2.imshow("image" , final)
cv2.waitKey(0)
