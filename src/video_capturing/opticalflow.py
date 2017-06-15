import numpy as np
import cv2
import serial

cap = cv2.VideoCapture(0)
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=0)

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 50,
                       qualityLevel = 0.1,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.0001))

# Create some random colors
color = np.random.randint(0,255,(100,3))

n_frame = 0

# Create a mask image for drawing purposes
ret, old_frame = cap.read()
mask = np.zeros_like(old_frame)

def track_object(p0, old_gray, mask, n_frame):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    good = True

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    if n_frame == 9:
        print(err.mean())
        if err.mean() > 5: 
            good = False

    diff = p0 - p1
    if diff[0,0,0] > 10:
        print("girando hacia la izquierda")
        ser.write('l'.encode())
    elif diff[0,0,0] < -10:
        print("girando hacia la derecha")
        ser.write('r'.encode())
    else:
        print("quieto")
        ser.write('q'.encode())

    if good: 
    # Select good points
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

        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)

    # Now update the previous frame and previous points
    return good 
    
    
def detect_object():
    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    return p0, old_gray


p0, old_gray = detect_object()

while(1):
    state = ser.read()
    # state = 's'
    # the robot is not moving
    print("estado = ", state)
    if state != 'm':
        good = track_object(p0, old_gray, mask, n_frame)
        n_frame = (1 + n_frame) % 10
        if not good:
            p0, old_gray = detect_object()

    if state == 's':    
        p0, old_gray = detect_object()
    

cv2.destroyAllWindows()
cap.release()
