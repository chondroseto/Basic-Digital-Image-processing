# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:47:00 2018

@author: chondroseto
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

import math 
#from IPython.display import display, image
def hysteresis(img, threshold, maxVal):
    heigth,width = img.shape
    bi_img = np.zeros((height,width),dtype = np.uint8)
    for x in xrange(height):
        for y in xrange(width):
            if img.item(x,y) > threshold:
                bi_img.itemset((x,y),maxVal)
            
    return bi_img

def smoothing(w,s):
    filt = np.zeros((w,w))
    center = (w/2) + 1
    
    for row in xrange(w):
        if (row+1)<center:
            x = center - (row +1)
        if (row + 1) > center:
            x = ((row+1) - center)
        if center == (row +1):
            x=0
        for column in xrange(w):
            if (column+ 1)<center:
                y = center - (column+1)
            if (column+1)>center:
                y =((column +1 ) - center)
            if center == (column + 1):
                y=0
            exp = math.exp((-1*(math.pow(x,2)+math.pow(y,2)))/(2*pow(s,2)))
            filt[row, column] = (1/(s*math.sqrt(2*math.pi)))*exp
            total = 0
            for x2 in xrange(x):
                for y2 in xrange(w):
                    total = total + filt[x2,y2]
            x2 = 0
            y2 = 0
            for x2 in xrange(w):
                filt[x2,y2]= filt[x2,y2]/total
            return filt
def maxsupress(img):
    sobX=np.zeros((3,3),dtype = np.float32)
    sobX[0,0] = 1
    sobX[0,1] = 0
    sobX[0,2] = -1
    sobX[1,0] = 2
    sobX[1,1] = 0
    sobX[1,2] = -2
    sobX[2,0] = 1
    sobX[2,1] = 0
    sobX[2,2] = 1
    imgX = cv2.filter2D(img,-1,sobX)
    sobY = np.zeros((3,3), dtype = np.float32)
    sobY[0,0] = 1
    sobY[0,1] = 1
    sobY[0,2] = 1
    sobY[1,0] = 1
    sobY[1,1] = 1
    sobY[1,2] = 1
    sobY[2,0] = 1
    sobY[2,1] = 1
    sobY[2,2] = 1
    imgY = cv2.filter2D(img,-1,sobY)
    
    height,width = imgX.shape
    
    ans = np.zeros((height,width),dtype=np.float32)
    
    ans2 = np.zeros((height, width), dtype=np.float32)
    for x in xrange(height):
        for y in xrange(width):
            temp = math.sqrt(imgX.item(x,y)**2+ imgY.item(x,y)**2)
            ans.itemset((x,y), temp)
    for x1 in xrange(height):
        for y1 in xrange(width):
            
            temp = np.arctan2(imgY.item(x1,y1),imgX.item(x1,y1))
            temp = math.degrees(temp)
            if(temp<0):
                temp = temp*-1
                temp = 180 - temp
                
            ans2.itemset((x1,y1),temp)
        return ans, ans2
    
def directFinder(direct):
    height,width = direct.shape
    for x in xrange(height):
        for y in xrange(width):
            temp = direct.item(x,y)
            if ((temp>= 0 and temp <22.5)or (temp >=157.5 and temp <= 180)):
                direct.itemset((x,y),0)
            if (temp>=22.5 and temp <67.5):
                direct.itemset((x,y),45)
            if (temp>=67.5 and temp <112.5):
                direct.itemset((x,y),90)
            if (temp>= 112.5 and temp < 157.5):
                direct.itemset((x,y),135)
    return direct
def nonmax(grad,direct):
    height,width = grad.shape
    ret = grad
    
    for x in xrange(height):
        for y in xrange(width):
            if (direct.item(x,y)==0):
                if y!=0 and y != (width-1):
                    temp1 = grad.item(x,y-1)
                    tempr = grad.item(x,y+1)
                    if((grad.item(x,y)<temp1) or (grad.item(x,y)<tempr)):
                        ret.itemset((x,y),0)
                if y==0 or y ==(width -1):
                    if y == 0:
                        tempr = grad.item(x,y+1)
                        if (grad.item(x,y)<tempr):
                            ret.itemset((x,y),0)
                            if y == (width-1):
                                temp1 = grad.item(x,y-1)
                                if (grad.item(x,y)<temp1):
                                    ret.itemset((x,y),0)
            if (direct.item(x,y)==45):
                if y!= 0 and y!=(width-1) and x!= 0 and x != (height-1):
                    temp1 = grad.item(x+1,y-1)
                    tempr = grad.item(x-1,y+1)
                    if ((grad.item(x,y)<temp1)or (grad.item(x,y)<tempr)):
                        ret.itemset((x,y),0)
                    elif y== 0 or x == (height - 1):
                        tempr = grad.item(x-1,y+1)
                        if tempr > grad.item(x,y):
                            ret.itemset((x,y),0)
                        else:
                            temp1 = grad.item(x+1,y-1)
                            if temp1>grad.item(x,y):
                                ret.itemset((x,y),0)
                    if (direct.item(x,y)==90):
                        if x != 0 and x != (height - 1):
                            temp1 = grad.item(x+1,y)
                            tempr = grad.item(x-1,y)
                            if ((grad.item(x,y)<temp1) or (grad.item(x,y)<tempr)):
                                ret.itemset((x,y),0)
                            if x == 0 or x == (height -1):
                                if x == 0:
                                   temp1 = grad.item(x+1,y)
                                   if (grad.item(x,y)<temp1):
                                       ret.itemset((x,y),0)
                                if x==(height -1):
                                    tempr = grad,item(x-1,y)
                                    if (grad.item(x,y)<tempr):
                                        ret.itemset((x,y),0)
                                if (direct.item(x,y)== 135):
                                    if y!= 0 and y != (width - 1) and x != 0 and x != (height - 1):
                                        temp1 = grad.item(x-1,y-1)
                                        tempr = grad.item(x+1,y+1)
                                        if ((grad.item(x,y)<temp1) or grad.item(x,y)<tempr):
                                            ret.itemset((x,y),0)
                                    elif x== 0 or y == 0:
                                        tempr = grad.item(x+1,y+1)
                                        if(grad.item(x,y)<tempr):
                                            ret.itemset((x,y),0)
                                    else:
                                        temp1 = grad.item(x-1,y-1)
                                        if (grad.item(x,y)<temp1):
                                            ret.itemset((x,y),0)
    return ret

img = cv2.imread("alif.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

height, width = imgGray.shape

img2 = np.zeros((height,width),dtype = np.float32)

for x in xrange(height):
    for y in xrange(width):
        img2.itemset((x,y),imgGray.item(x,y))

filt = smoothing(5,1)

img3 = cv2.filter2D(img2,-1,filt)

grad, direct = maxsupress(img3)

direct = directFinder(direct)

height,width = direct.shape

img4 = nonmax(grad,direct)

img5 = hysteresis(img4,150,255)

plt.figure(figsize=(18,6))
plt.subplot(1,3,1)
plt.imshow(img5,'gray')
plt.title('canny edge detection')
plt.axis("off")
plt.show()

                                          
                                
            
                                
                        
                    
        
    
    