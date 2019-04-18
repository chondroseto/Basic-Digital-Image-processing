# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:28:21 2018

@author: chondroseto
"""

import cv2

img = cv2.imread('images/g2-200px.jpg')

cv2.imshow('Citra Asli',img)
print'Nilai sebelum refleksi',img

reflection = cv2.flip(img,0,1)

print 'nilai hasil refleksi',reflection
cv2.imshow('hasil refleksi citra',reflection)
cv2.waitKey()