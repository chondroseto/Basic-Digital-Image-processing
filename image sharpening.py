# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 12:01:53 2018

@author: chondroseto
"""

import cv2
import numpy as np

I = cv2.imread('images/k1-200px.jpg')
img = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

print "hasil sebelum sharpening"
print img

laplacian = np.array([[0,-1,0], [-1,5,-1],[0,-1,0]])

im = cv2.filter2D(img,-1,laplacian)

print "hasil sesudah sharpening :"
print im

cv2.imshow('sebelum',img)
cv2.imshow('hasil',im)
cv2.waitKey()
