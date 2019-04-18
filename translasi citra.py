# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:37:00 2018

@author: chondroseto
"""
import cv2
import numpy as np

img = cv2.imread('images/r3-200px.jpg')

cv2.imshow('Citra Asli', img)
print'Nilai sebelum Translasi', img

num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([[1,0,70],[0,1,60]])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols,num_rows))

print 'Nilai Hasil Translasi', img_translation
cv2.imshow('Hasil Translasi', img_translation)
cv2.waitKey()
