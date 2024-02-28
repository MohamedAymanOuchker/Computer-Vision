#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:59:10 2024

@author: aymanouchker
"""

import cv2 as cv
import numpy as np

#imshow reconnait l espace BGR

def nothing(x):
    print(x)

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('H','image', 0, 179, nothing) # NOTHING affiche  l intensite de la couleur 
cv.createTrackbar('S','image', 255, 255, nothing)
cv.createTrackbar('V','image', 255, 255, nothing)

img_hsv = np.zeros((250,500,3),np.uint8)

while True:
    h = cv.getTrackbarPos('H','image')
    s = cv.getTrackbarPos('S', 'image')
    v = cv.getTrackbarPos('V', 'image')
    
    img[:] = (h,s,v)
    img_bgr = cv.cvtColor(img,cv.COLOR_HSV2BGR)

    cv.imshow('image',img_bgr)
    
    k = cv.waitKey(1) 
    if k == 27:
        break

cv.destroyAllWindows()