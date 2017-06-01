import numpy as np
import cv2

cap = cv2.VideoCapture(1)
mog = cv2.createBackgroundSubtractorMOG2()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray_prev = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mask = mog.apply(image=gray_prev)

    cv2.imshow('frame',mask)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
