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

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()

    # Our operations on the frame come here
    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Camera 0',gray0)
    cv2.imshow('Camera 1',gray1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
