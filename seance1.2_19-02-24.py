#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:02:57 2024

@author: aymanouchker
"""

import cv2

cap = cv2.VideoCapture(0) # open laptop camera
fourcc = cv2.VideoWriter_fourcc(*'XVID') # use any fourcc type to improve quality
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480), isColor=False) # video settings

print(cap.isOpened()) # check if the camera is opened
while(cap.isOpened()): # while loop to read all frames
    ret, frame = cap.read() # read all frames if ret is True
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # get the frame width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # get the frame height
        
        out.write(frame) # save your video
        
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('frame', gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()