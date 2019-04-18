# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 06:26:08 2018

@author: chondroseto
"""
import cv2

image = cv2.imread("images/k1-200px.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print "Citra Sebelum di invert"
print image

invert = 255-image

print " "
print "Citra setelah di invert"
print invert

cv2.imshow("Sebelum", image)
cv2.imshow("Hasil", invert)
cv2.waitKey()

