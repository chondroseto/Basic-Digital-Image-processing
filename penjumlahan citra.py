# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:32:12 2018

@author: chondroseto
"""

import cv2

img1 = cv2.imread('images/k1-200px.jpg')
img2 = cv2.imread('images/k3-200px.jpg')

print 'Nilai Citra Asli 1',img1
print 'Nilai Citra Asli 2',img2
cv2.imshow('Citra Asli 1',img1)
cv2.imshow('Citra Asli 2',img2)

img = img1+img2

print 'Nilai Hasil Penjumlahan',img
cv2.imshow('Hasil penjumlahan',img)
cv2.waitKey(0)