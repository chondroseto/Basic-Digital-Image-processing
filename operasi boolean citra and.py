# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:41:17 2018

@author: chondroseto
"""

import cv2

img1 = cv2.imread('images/k1-200px.jpg',0)
img2 = cv2.imread('images/k3-200px.jpg',0)
th,t1=cv2.threshold(img1,125,255,cv2.THRESH_BINARY)
th,t2=cv2.threshold(img2,125,255,cv2.THRESH_BINARY)

print 'Nilai Citra Asli 1',t1
print 'Nilai Citra Asli 1',t2
cv2.imshow('Citra Asli 1',t1)
cv2.imshow('Citra Asli 1',t2)

img = cv2.bitwise_and(t1,t2)

cv2.imshow('img',img)
print 'Hasil AND',img
cv2.waitKey(0)