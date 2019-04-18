# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:47:44 2018

@author: chondroseto
"""
import cv2
import numpy as np

img = cv2.imread('images/k1-200px.jpg')

print img

H,W = img.shape[:2]
grey = np.zeros((H,W), np.uint8)

for i in range (H):
    for j in range(W):
        grey[i,j] = np.clip(0.299 * img[i,j,0] + 0.587 * img[i,j,1] + 0.114 * img[i,j,2], 0, 255)

print ""
print "Grayscale :"
print grey


cv2.imshow("RGB", img)
cv2.imshow("Grayscale", grey)
cv2.waitKey()