#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 08:58:45 2024

@author: aymanouchker
"""

import cv2
import numpy as np

img = np.zeros([512, 512, 3], np.uint8) # create image

img = cv2.line(img, (0, 0), (255, 255), (147, 96, 46), 3) # draw line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 3) # draw arrow
img = cv2.rectangle(img, (384, 0), (510, 511), (0, 0, 255), -1) # draw rectangle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1) # draw circle

font = cv2.FONT_HERSHEY_SIMPLEX # type of font
img = cv2.putText(img, "OpenCV", (10, 300), font, 4, (0, 255, 255), 3, cv2.LINE_AA) # write a text

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
