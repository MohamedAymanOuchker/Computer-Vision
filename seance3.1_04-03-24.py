#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:24:39 2024

@author: aymanouchker
"""

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

 #balayage de la video frame par frame
 
while(1):
  _, frame=cap.read()
  #elle retourne le frame et est ce qu on l a detecte
  hsv= cv.cvtColor (frame, cv.COLOR_BGR2HSV)
  #definir la plage de la couleur
  lower_blue = np.array([36, 25, 25])
  upper_blue = np.array([70, 255, 255])
  #isoler la couleur souhaitee
  mask = cv.inRange(hsv, lower_blue, upper_blue) #image,min,max il convertit la couleur en 255 ou 0
  res=cv.bitwise_and(frame,frame,mask=mask) #and avec image originale
  cv.imshow('frame',frame)
  cv.imshow('mask',mask)
  cv.imshow('res',res)
  k=cv.waitKey(5) & 0xFF
 
  if  k == 27 :
      break

cap.release()
cv.destroyAllWindows()