# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:23:43 2018

@author: chondroseto
"""

import cv2
import numpy as np

im_in = cv2.imread("images/r3-200px.jpg",cv2.IMREAD_GRAYSCALE)

th, im_th = cv2.threshold(im_in,220,255,cv2.THRESH_BINARY_INV)

im_floodfill = im_th.copy()

h,w = im_th.shape[:2]
mask = np.zeros((h+2,w+2),np.uint8)

cv2.floodFill(im_floodfill,mask,(0,0),255)

im_floodfill_inv = cv2.bitwise_not(im_floodfill)

im_out = im_th | im_floodfill_inv

cv2.imshow("thresholded image",im_th)
cv2.imshow("thresholded image",im_floodfill)
cv2.imshow("thresholded image",im_floodfill_inv)
cv2.imshow("foreground",im_out)
cv2.waitKey(0)