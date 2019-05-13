# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:20:15 2019

@author: Simhadri G
"""

import numpy as np
import cv2

# start video capture
cap = cv2.VideoCapture(0)

# save the background
ret, background = cap.read()
cv2.imshow("background",background)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([70, 40, 70])
    upper_blue = np.array([110, 250, 250])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((7,7),np.uint8)
    
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    invert = cv2.bitwise_not(closing)
    
    cv2.imshow("invert",invert)
    
    res1 = cv2.bitwise_and(background, background, mask=closing)
    res = cv2.bitwise_and(frame, frame, mask=invert)
    
    result = res+res1
    
    cv2.imshow("result",result)
    
    
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    cv2.imshow("res1",res1)

    # Display the resulting frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()