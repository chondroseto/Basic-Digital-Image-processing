# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 18:48:39 2018

@author: chondroseto
"""

from cv2 import *
import cv2

if __name__ == '__main__':
    source = cv2.imread("images/r3-200px.jpg",cv2.IMREAD_GRAYSCALE)
    final = source[:]
    for y in range(len(source)):
        for x in range(y):
            final[y,x] = source[y,x]
            
    members = [source[0,0]]*9
    for y in range(1,len(source)-1):
        for x in range(1,y-1):
            members[0] = source[y-1,x-1]
            members[1] = source[y,x-1]
            members[2] = source[y+1,x-1]
            members[3] = source[y-1,x]
            members[4] = source[y,x]
            members[5] = source[y+1,x]
            members[6] = source[y-1,x+1]
            members[7] = source[y,x+1]
            members[8] = source[y+1,x+1]
            
            members.sort()
            final[y,x] = members[4]
            
            cv2.namedWindow('Source_Picture', cv2.WINDOW_AUTOSIZE)
            cv2.namedWindow('Final_Picture',cv2.WINDOW_AUTOSIZE)
            cv2.imshow('Source_Picture',source)
            cv2.imshow('Final_Picture', final)
            print ("source", source)
            print ("final",final)
            cv2.waitKey()
    