# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:47:05 2018

@author: chondroseto
"""

import cv2

faceCascade = cv2.CascadeClassifier("images/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("images/haarcascade_eye.xml")

image = cv2.imread('images/selfie.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)

print("Found {0} faces!".format(len(faces)))

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(255,0,0),2)
    
    eyes = eyeCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,flags = cv2.CASCADE_SCALE_IMAGE)
    
    for (ex,ey,ew,eh) in eyes :
        cv2.rectangle(image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
cv2.imshow("Faces found",image)
cv2.waitKey(0)