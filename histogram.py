# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 17:51:26 2018

@author: chondroseto
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('images/k2-200px.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Grayscale',img)
plt.hist(img.ravel(),256,[0,256]);