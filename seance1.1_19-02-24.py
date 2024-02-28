#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 08:58:08 2024

@author: aymanouchker
"""

import cv2

img = cv2.imread('img1.png', 1)

cv2.imshow('image', img)

k = cv2.waitKey(0) & 0xFF

if k == 27: # esc in keyboard
    cv2.destroyAllWindows() # close the window
    
elif k == ord('s'): # if order is s save the image
    cv2.imwrite('img1_gray.png', img) # write image 
    cv2.destroyAllWindows() # close the window

cv2.imshow('image', img)

cv2.waitKey(5000)
cv2.destroyAllWindows()