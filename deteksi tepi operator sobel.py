# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:47:02 2018

@author: chondroseto
"""

import numpy as np
import cv2

def sobel_filter(im):
    im = im.astype(np.float)
    
    kh = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype = np.float)
    kv = np.array([[1,2,1],[0,0,0],[-1,-2,-1]],dtype = np.float)
    
    gx = cv2.filter2D(im,-1,kh)
    gy = cv2.filter2D(im,-1,kv)
    
    g = np.sqrt(abs(gx)**2) + abs(gy)**2
    
    return g

slika = cv2.imread("alif.jpg",0)
cv2.imshow("Citra Grayscale",slika)
cv2.waitKey(0)
cv2.destroyAllWindows()

sobelSlika = sobel_filter(slika)

cv2.imwrite("images/baru.jpg",sobelSlika)

img = cv2.imread("images/g1-200px.jpg")
cv2.imshow("Citra filter sobel",img)
cv2.waitKey(0)
cv2.destroyAllWindows()    

print "asli :"
print slika

