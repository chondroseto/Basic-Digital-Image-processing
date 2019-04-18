# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 11:50:03 2018

@author: chondroseto
"""

import cv2
import numpy as np

I = cv2.imread('images/g1-200px.jpg')
img = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

print "Hasil sebelum Smoothing :"
print img

mean = np.array([[0.111,0.111,0.111],[0.111,0.111,0.111],[0.111,0.111,0.111]])

im = cv2.filter2D(img, -1 , mean)

print "hasil sesudah smoothing :"
print im

cv2.imshow('sebelum',img)
cv2.imshow('hasil',im)
cv2.waitKey()