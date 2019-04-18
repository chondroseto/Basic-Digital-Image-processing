import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/r3-200px.jpg')

gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(gray,'gray')
plt.title('input')
plt.show()

ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imwrite("images/output.jpg",thresh)
plt.imshow(thresh,'gray')
plt.title('output')
plt.show