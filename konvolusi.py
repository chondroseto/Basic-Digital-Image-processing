# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 18:26:06 2018

@author: chondroseto
"""

import cv2
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

imgc = cv2.imread('images/g2-200px.jpg')
img = cv2.cvtColor(imgc,cv2.COLOR_BGR2GRAY)
w_k = np.array([[0,0,0],[0,1,0],[0,0,0],],dtype='float')

w_k = np.rot90(w_k, 2)

print(img.shape,w_k.shape)
f = signal.convolve2d(img, w_k, 'valid')

plt.subplot(121),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(122),plt.imshow(f,'gray'),plt.title('filter')
print("pixel asli",img)
print("pixel filter",f)
plt.show()
