# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:59:10 2018

@author: chondroseto
"""

import cv2
import numpy as np

img_rgb = cv2.imread('images/b1-200px.jpg')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/templateb1.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(res>= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,255,255),1)
    
cv2.imshow('template',template)
cv2.imshow('Hasil',img_rgb)
cv2.waitKey(0)
