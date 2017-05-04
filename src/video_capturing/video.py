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
cap1 = cv2.VideoCapture(2)
ffdetector = cv2.xfeatures2d.SURF_create()

while(True):
    # Capture frame-by-frame
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()

    # Our operations on the frame come here
    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    keypoints0 = ffdetector.detect(image=gray0, mask=None)
    keypoints1 = ffdetector.detect(image=gray1, mask=None)

    result1 = np.zeros(gray0.shape, np.int8)
    result2 = np.zeros(gray1.shape, np.int8)

    result1 = cv2.drawKeypoints(gray0, keypoints0, result1)
    result2 = cv2.drawKeypoints(gray1, keypoints1, result2)

    # Display the resulting frame
    cv2.imshow('Camera 0',result1)
    cv2.imshow('Camera 1',result2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# cap0.release()
cap1.release()
cv2.destroyAllWindows()
