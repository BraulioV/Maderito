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

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

cap0 = cv2.VideoCapture(1)

t_minus = cv2.cvtColor(cap0.read()[1], cv2.COLOR_BGR2GRAY)
t_0 = cv2.cvtColor(cap0.read()[1], cv2.COLOR_BGR2GRAY)
t_plus = cv2.cvtColor(cap0.read()[1], cv2.COLOR_BGR2GRAY)

while(True):
    # Our operations on the frame come here
    diff_img = diffImg(t_minus,t_0,t_plus)
    # show the difference
    cv2.imshow('Mapa de profundidad', diff_img)
    # update images
    t_minus = t_0
    t_0 = t_plus
    t_plus  = cv2.cvtColor(cap0.read()[1], cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap0.release()
cv2.destroyAllWindows()
