import numpy as np
import cv2
import serial

def track_object(p0):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    diff = p0 - p1
    if diff[0,0,0] > 10:
        print("girando hacia la izquierda")
    elif diff[0,0,0] < -10:
        print("girando hacia la derecha")
    else:
        print("quieto")

    # Select good points
    if (p1 != None and p0 != None) : 
        good_new = p1[st==1]
        good_old = p0[st==1]

    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    
    img = cv2.add(frame,mask)

    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        return 1

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)
    
def detect_object():
    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    return p0
    

cap = cv2.VideoCapture(1)
ser = serial.Serial('dev/ttyACM0', 9600)

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 500,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))


# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

p0 = detect_object()

while(1):
    state = ser.read()

    # the robot is not moving
    if state != 'm':
        track_object(p0)
    else:
        if state == 's':
            p0 = detect_object()
    

cv2.destroyAllWindows()
cap.release()
