# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 18:42:49 2018

@author: chondroseto
"""

import numpy as np
import cv2

img = cv2.imread("images/r3-200px.jpg",cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)
print "processing..."

myIMG = cv2.blur(img,(3,3))

cv2.namedWindow('Processed Image', cv2.WINDOW_NORMAL)
cv2.imshow('Processed Image', myIMG)
cv2.waitKey(0)
print "Done!"
