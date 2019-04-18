"""
Created on Mon Mar 05 17:56:32 2018

@author: chondroseto
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt 

def perataanHistogram(A):
    nilai_bin = 255
    A = A+1
    [frekuensi,value] = np.histogram(A,bins=nilai_bin)
    cumulatif_histogram = frekuensi.cumsum()
    [baris,kolom] = A.shape 
    probabilty_frekuensi = np.round((cumulatif_histogram/float(A.size))*nilai_bin)
    B = np.empty(A.shape)
    for i in range(0,baris):
        for j in range(0,kolom):
            B[i,j] = probabilty_frekuensi[A[i,j]-1]
    return B

I = cv2.imread('images/k2-200px.jpg')
gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
hasil = perataanHistogram(gray)
plt.hist(hasil.ravel(),256,[0,256])
plt.figure('perataan histogram')

cv2.imshow('gray',gray)
cv2.imshow('perataan',hasil)
plt.show()
