import cv2
import numpy as np

#img = cv2.imread("Images\WhatsApp Image 2020-09-06 at 10.46.51 AM.jpeg")

img = np.zeros((512,512,3))

#-----------------------------Basics Events-----------------
'''
def draw(event, x ,y , flags , params):   #x any y are the co-ordinates

    if event==0:
        print("Mouse moved ")
    elif event==1:
        print("Mouse down clicked")
    elif event==4:
        print("Mouse up clicked") '''

#----------------------------To darw a circle------------------
'''
def draw(event, x, y, flags, params ):

    if event==1:
        cv2.circle(img , center=(x,y) , radius=40 , color=(0,0,255), thickness=1)  '''

#---------------------Draw the image with Dragging----------------
flag=False
ix=-1
iy=-1

def draw(event , x, y ,flags ,params):

    global ix,iy , flag

    if event==1:
        ix=x
        iy=y

    elif event==0:

        if flag==True:
            cv2.rectangle(img , pt1=(ix,ix), pt2=(x,y) ,color=(0,255,0),thickness=-1)
    elif event==4:

        if flag==False:
            cv2.rectangle(img , pt1=(ix,ix), pt2=(x,y) ,color=(0,255,0),thickness=-1)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window" , draw)

while True:

    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF ==ord('x'):  #pressing x in keyboard
        break


cv2.destroyAllWindows()  #destroy all the windows