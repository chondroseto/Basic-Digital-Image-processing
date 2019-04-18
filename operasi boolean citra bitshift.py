# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:03:03 2018

@author: chondroseto
"""

import cv2

img1 = cv2.imread('images/k1-200px.jpg',0)

print 'Nilai Citra Asli 1',img1
cv2.imshow('Citra Asli 1',img1)

imga = img1*(2*3)
imgb = img1/(2*3)

print 'Nilai hasil bitshift kanan',imga
print 'Nilai hasil bitshift kiri',imgb
cv2.imshow('Hasil bitshift kanan',imga)
cv2.imshow('Hasil bitshift kiri',imgb)
cv2.waitKey(0)