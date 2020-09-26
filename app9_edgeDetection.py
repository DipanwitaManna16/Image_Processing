import cv2
import numpy as np

img = cv2.imread('Images\sudoko512.png')

vertical = cv2.Sobel(img , -1, 1, 0)
horizontal = cv2.Sobel(img , -1 , 0 ,1)
both = cv2.Sobel(img , -1,1,1)
#both = cv2.Sobel(vertical , 0.8 , horizontal , 0.2 , 0)


cv2.imshow('window',img)
cv2.imshow('vertical',vertical)
cv2.imshow('horozontal',horizontal)
cv2.imshow('Both',both)
cv2.waitKey(0)