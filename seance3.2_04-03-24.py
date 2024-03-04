#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:26:18 2024

@author: aymanouchker
"""

import cv2 as cv
import numpy as np

# Initialize the webcam capture
webcam = cv.VideoCapture(0)
while True:
    # Read a frame from the webcam
    _, imageFrame = webcam.read()

    # Convert the BGR image to the HSV color space
    hsv = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)

    # Define color ranges for red, green, and blue in the HSV color space
    lower_red = np.array([136, 87, 111],np.uint8)
    upper_red = np.array([180, 255, 255],np.uint8)
    lower_green = np.array([25, 52, 72],np.uint8)
    upper_green = np.array([102, 255, 255],np.uint8)
    lower_blue = np.array([94, 80, 2],np.uint8)
    upper_blue = np.array([120, 255, 255],np.uint8)

    # Create masks for red, green, and blue colors
    red_mask = cv.inRange(hsv, lower_red, upper_red)
    green_mask = cv.inRange(hsv, lower_green, upper_green)
    blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
   
    kernel = np.ones((5, 5), "uint8")
    red_mask = cv.dilate(red_mask, kernel)
    green_mask = cv.dilate(green_mask, kernel)
    blue_mask = cv.dilate(blue_mask, kernel)
   
    contours,hierarchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
   
    for pic, contour in enumerate (contours) :
        area = cv.contourArea(contour)
        if(area>300):
            x,y,w,h = cv.boundingRect(contour)
            imageFrame=cv.rectangle(imageFrame, (x,y),(x+w,y+h),(0,0,255),2)
            cv.putText(imageFrame, "red",(x,y),cv.FONT_HERSHEY_SIMPLEX, 1.0,(0,0,255))    
       
    contours,hierarchy = cv.findContours(green_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
   
    for pic, contour in enumerate (contours) :
        area = cv.contourArea(contour)
        if(area>300):
            x,y,w,h=cv.boundingRect(contour)
            imageFrame=cv.rectangle(imageFrame,(x,y),(x+w,y+h),(0,255,0),2)
            cv.putText(imageFrame, "green",(x,y),cv.FONT_HERSHEY_SIMPLEX, 1.0,(0,255,0))    
   
    contours,hierarchy = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
   
    for pic, contour in enumerate (contours) :
        area = cv.contourArea(contour)
        if(area>300):
            x,y,w,h=cv.boundingRect(contour)
            imageFrame=cv.rectangle(imageFrame,(x,y),(x+w,y+h),(255,0,0),2)
            cv.putText(imageFrame,"blue",(x,y), cv.FONT_HERSHEY_SIMPLEX, 1.0,(255,0,0))    
   
    # Show the resulting frame
    cv.imshow('frame', imageFrame)

    # Exit the loop if the 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()