# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:39:39 2018

@author: chondroseto
"""

import cv2

img1 = cv2.imread('images/k1-200px.jpg')

print 'Nilai Citra Asli 1',img1
cv2.imshow('Citra Asli 1',img1)

img = img1/2

print 'Nilai Hasil Pembagian',img
cv2.imshow('Hasil pembagian',img)
cv2.waitKey(0)