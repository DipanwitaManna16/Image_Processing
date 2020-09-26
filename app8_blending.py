import cv2
import numpy as np

#blending used in watermark

img1 = cv2.imread("Images\WhatsApp Image 2020-09-06 at 10.43.37 AM.jpeg")
img2 = cv2.imread("Images\WhatsApp Image 2020-09-06 at 10.46.50 AM.jpeg")

result = cv2.addWeighted(img1 , 0.5 , img2, 0.5, 0)

cv2.imshow("result",result)
cv2.waitKey(0)