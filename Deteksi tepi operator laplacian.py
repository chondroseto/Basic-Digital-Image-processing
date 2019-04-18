# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:49:12 2018

@author: chondroseto
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img0 = cv2.imread('alif.jpg',cv2.IMREAD_GRAYSCALE)

#gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img0,(3,3),0)


laplacian = cv2.Laplacian(img,cv2.CV_64F)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(img,cmap = 'gray')
plt.title('Gray'), plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(img,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]),plt.yticks([])
plt.show()

print "asli :"
print img0

print "hasil :"
print laplacian

cv2.imwrite("tes.jpg",laplacian)
