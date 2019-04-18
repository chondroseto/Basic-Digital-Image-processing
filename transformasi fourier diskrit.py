# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 08:57:08 2018

@author: chondroseto
"""

import sys
import cv2 as cv
import numpy as np

def main(argv):
    filename = argv[0] if len(argv) > 0 else "images/g2-200px.jpg"
    I = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    if I is None:
        print ('error opening image')
        return -1
    
    rows, cols = I.shape
    m = cv.getOptimalDFTSize( rows )
    n = cv.getOptimalDFTSize( cols )
    padded = cv.copyMakeBorder(I, 0, m - rows, 0, n - cols,cv.BORDER_CONSTANT, value=[0,0,0])
    
    planes = [np.float32(padded), np.zeros(padded.shape,np.float32)]
    complexI = cv.merge(planes)
    cv.dft(complexI,complexI)
    
    cv.split(complexI,planes)
    cv.magnitude(planes[0],planes[1],planes[0])
    magI = planes[0]
    
    matOfOnes = np.ones(magI.shape, dtype = magI.dtype)
    cv.add(matOfOnes, magI,magI)
    cv.log(magI,magI)
    magI_rows,magI_cols = magI.shape
    magI = magI[0:(magI_rows & -2), 0:(magI_cols & -2)]
    cx = int(magI_rows/2)
    cy = int(magI_cols/2)
    q0 = magI[0:cx, 0:cy]
    
    q1 = magI[cx:cx+cx, 0:cy]
    q2 = magI[0:cx, cy:cy+cy]
    q3 = magI[cx:cx+cx, cy:cy+cy]
    tmp = np.copy(q0)
    
    magI[0:cx, 0:cy] = q3
    magI[cx:cx + cx, cy:cy+cy] = tmp
    tmp = np.copy(q1)
    
    magI[cx:cx+cx, 0:cy] = q2
    magI[0:cx, cy:cy + cy] = tmp
    
    cv.normalize(magI,magI,0,1,cv.NORM_MINMAX)
    
    cv.imshow("input image",I)
    print('nilai pixel gambar Grayscale :')
    print('')
    print I
    print('')
    cv.imshow("spectrum magnitude", magI)
    print('Nilai spectrum magnitude :')
    print('')
    print magI
    cv.waitKey()
    
main(sys.argv[1:])
