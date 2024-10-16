import cv2 as cv
import numpy as np
img=cv.imread('more_man.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade=cv.CascadeClassifier('haar_face.xml')
if haar_cascade.empty():
    print("Error loading cascade file")
else:
    face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for (x,y,w,h) in face_rect:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    print("no of faces detected=",len(face_rect))
cv.rectangle(img,(100,100),(150,150),(0,255,0),2)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

