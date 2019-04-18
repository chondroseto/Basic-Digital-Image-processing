# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:39:23 2018

@author: chondroseto
"""
import cv2
import numpy as np

img = cv2.imread("images/b1-200px.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print "Gambar Asli"
print img

min = np.amin(img)
max = np.amax(img)

print 'min =',min
print 'max =',max

H,W = img.shape[:2]
array_kontras = np.zeros((H,W), np.uint8)

for i in range (H):
    for j in range(W):
        pixel = img[i,j]
        pixel = (pixel-min)*255/(max-min)
        array_kontras[i,j]=pixel
        
print "Array Kontras"
print array_kontras

cv2.imshow("Sebelum", img)
cv2.imshow("Sesudah", array_kontras)
cv2.waitKey()
