import numpy as np
import cv2

img = cv2.imread("Images\WhatsApp Image 2020-09-06 at 10.46.51 AM.jpeg")

mask = np.ones(img.shape , np.uint8) * 100

result = cv2.add(img , mask)    #addition-brightening
result1 = cv2.subtract(img , mask)    #subtraction-darkening

final = np.hstack((result1 , img , result))      #horizontly stacking

cv2.imshow("image" , final)
cv2.waitKey(0)