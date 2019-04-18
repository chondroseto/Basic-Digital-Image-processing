# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:53:21 2018

@author: chondroseto
"""
import cv2
import numpy as np

I = cv2.imread('images/g1-200px.jpg')
grey = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

print "Pixels sebelum ditambah brigthness :"
print grey

value = -100

cerah = np.where((255 - grey) < value,255,grey+value)

cerah[cerah < 0] = 0

print ""
print "Pixels setelah ditambah brightness :"
print cerah

cv2.imshow("Grey", grey)
cv2.imshow("hasil", cerah)
cv2.imwrite("Hasil_Kecerahan.jpg",cerah)
cv2.waitKey()
