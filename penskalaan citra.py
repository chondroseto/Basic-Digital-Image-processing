# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:45:35 2018

@author: chondroseto
"""

import cv2

img = cv2.imread('images/r1-200px.jpg')

cv2.imshow('Citra Asli', img)
print 'nilai citra asli', img

num_rows, num_cols = img.shape[:2]
new_rows,new_cols = int(num_rows*2),int(num_cols*0.5)
img_scaled = cv2.resize(img,(new_rows,new_cols))

cv2.imshow('Hasil pengskalaan', img_scaled)
print 'Nilai Hasil Pengskalaan', img_scaled
cv2.waitKey()