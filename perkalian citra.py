# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:37:29 2018

@author: chondroseto
"""

import cv2

img1 = cv2.imread('images/k1-200px.jpg')

print 'Nilai Citra Asli 1',img1
cv2.imshow('Citra Asli 1',img1)

img = img1*3

print 'Nilai Hasil Perkalian',img
cv2.imshow('Hasil Perkalian',img)
cv2.waitKey(0)