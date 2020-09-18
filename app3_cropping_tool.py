import cv2
import numpy as np

img = cv2.imread("Images\WhatsApp Image 2020-09-06 at 10.46.50 AM.jpeg")

flag=False
ix=-1
iy=-1

def crop(event , x, y , flags , params):

    global flag , ix ,iy

    if event==1:
        flag=True
        ix=x
        iy=y

    elif event==4:
        fx=x
        fy=y
        flag=True
        
        cv2.rectangle(img , pt1=(ix,iy) , pt2=(x,y) , color=(0,0,255) , thickness=1)

        cropped = img[iy:fy , ix:fx]

        cv2.imwrite("croppend_img.png" , cropped)
        cv2.imshow("new_window" , cropped)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", crop)

while True:

    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF ==ord('x'):     #pressing x in keyboard
        break

cv2.destroyAllWindows()  #destroy all the windows