import cv2
import numpy as np

img = cv2.imread("Images\WhatsApp Image 2020-09-06 at 10.46.51 AM.jpeg")

print(type(img))
print(img.shape)

#----------------------------gray_image---------------------
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#---------------------------Resize the image-----------------
#img_resize = cv2.resize(img,(256,256))

#---------------------------Flip the image-------------------
# 1->vertical |  0-> horizontal |  -1->combined effect
#img_flip = cv2.flip(img , -1)

#--------------------------Cropping---------------------------
#img_crop = img[100:300 , 200:500]

#------------------------Saving an image----------------------
#cv2.imwrite('fruits_small.png',img_crop)

#-----------------------BlackImage---------------------------
img1 = np.zeros((512,512,3))

#----------------------Creating a Rectangle------------------
cv2.rectangle(img1 , pt1=(100,100), pt2=(200,300), color=(255,0,0) , thickness=3)
#----------------------Creating a Circle----------------------
cv2.circle(img1 , center=(200,400) , radius=50 , color=(0,0,255), thickness=-1)
#------------------------Line----------------------------------
cv2.line(img1 ,pt1=(0,0) , pt2=(512,512) , thickness=2 , color=(0,255,0))
#-----------------------FontText-------------------------------
cv2.putText(img1 , text='Hi', org=(400,400) ,fontScale=4 , color=(0,255,255) ,
        thickness=2 , lineType=cv2.LINE_AA , fontFace=cv2.FONT_ITALIC)



cv2.imshow("window",img1)
cv2.waitKey(0)
