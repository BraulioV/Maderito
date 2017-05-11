#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#                       Sistemas con Microprocesadores                         #
#    Script opencv+python para leer imágenes de un eye toy con raspberry pi    #
#    Hecho por Marta Gómez y Braulio Vargas                                    #
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
################################################################################

import numpy as np
import cv2

cap0 = cv2.VideoCapture(1)
# cap1 = cv2.VideoCapture(2)
# ffdetector = cv2.xfeatures2d.SURF_create()

while(True):
    # Capture frame-by-frame
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap0.read()

    # Our operations on the frame come here
    gray_prev = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    gray_next = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray_prev, 500,  0.01, 10)

    prev_PyVR, next_PyVR = np.zeros(gray_prev.shape, dtype=np.uint8), np.zeros(gray_prev.shape, dtype=np.uint8)
    
    curr_points, status, err = cv2.calcOpticalFlowPyrLK(gray_prev, gray_next, 
                                                                                prev_PyVR, next_PyVR,  corners, (10,10), 3 , (cv2.TERM_CRITERIA_MAX_ITER|cv2.TERM_CRITERIA_EPS,20, 0.03), 0)
    # keypoints0 = ffdetector.detect(image=gray_prev, mask=None)
    # keypoints1 = ffdetector.detect(image=gray_next, mask=None)

    # result1 = np.zeros(gray_prev.shape, np.int8)
    # result2 = np.zeros(gray_next.shape, np.int8)

    # result1 = cv2.drawKeypoints(gray_prev, corners, result1)
    # result2 = cv2.drawKeypoints(gray_next, keypoints1, result2)
    # for i in corners:
        # cv2.circle(frame0, (i[0][0], i[0][1]), 10, (255, 0, 0), -1)

    # Display the resulting frame
    cv2.imshow('Camera 0',frame0)
    # cv2.imshow('Camera 1',result2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# cap0.release()
cap1.release()
cv2.destroyAllWindows()
