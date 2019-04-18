# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:54:31 2018

@author: chondroseto
"""

import cv2

img = cv2.imread('images/r2-200px.jpg')

cv2.imshow('Citra Asli', img)
print 'Nilai Citra asli',img

num_rows, num_cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2,num_rows/2),30 ,1)
img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols,num_rows))

print 'Nilai Hasil Rotasi Citra', img_rotation
cv2.imshow('Hasil Rotasi',img_rotation)
cv2.waitKey()