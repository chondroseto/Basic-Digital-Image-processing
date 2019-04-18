# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 06:31:17 2018

@author: chondroseto
"""
import numpy as np
import cv2

def adjust_gamma(image, gamma):
    invGamma= 1.0 / gamma
    
    table = np.array([((i/255.0)** invGamma)*255 for i in np.arange(0, 256)]).astype("uint8")
    
    return cv2.LUT(image, table)

original = cv2.imread("images/k1-200px.jpg")
img = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

for gamma in np.arange(0.0, 3.6, 0.5):
    if gamma ==1:
        continue
    gamma = gamma if gamma > 0 else 0.1
    adjusted = adjust_gamma(img, gamma=gamma)
    cv2.putText(adjusted,"g={}".format(gamma),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("images", np.hstack([img, adjusted]))
    cv2.waitKey(0)
cv2.waitKey()