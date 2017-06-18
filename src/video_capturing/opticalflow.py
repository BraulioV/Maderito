import numpy as np
import cv2
import serial
from time import sleep

SLEEP_TIME = 2
cap = cv2.VideoCapture(0)
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)


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

n_frame, old_state = 0, b's'

# Create a mask image for drawing purposes
# ret, old_frame = cap.read()
# mask = np.zeros_like(old_frame)

def clear_buffer():
    ser.reset_output_buffer()
    ser.reset_input_buffer()


def track_object(p0, old_gray, mask, n_frame):
    
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    good, move, direccion = True, False, 'q'

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    if n_frame == 9:
        if err.mean() > 3.5: 
            good = False


    if good: 
    # Select good points
        good_new = p1[st==1]
        good_old = p0[st==1]

        diff = good_new - good_old
        norm = np.sum(diff)
        if diff[0,0] > 10:
            print("girando hacia la DERECHA")
            direccion = 'r'
            move = True
        elif diff[0,0] < -10:
            print("girando hacia la IZQUIERDA")
            
            direccion = 'l'
            move = True
        else:
            direccion = 'q'
            print("QUIETO")
            move = False

        # draw the tracks
        for i,(new,old) in enumerate(zip(good_new,good_old)):
            a,b = new.ravel()
            # c,d = old.ravel()
            # mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
            frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
        
        img = cv2.add(frame,mask)

        cv2.imshow('frame', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            return 1

        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)

    
    return good, move, direccion
    
    
def detect_object(cam):
    # Take first frame and find corners in it
    cam.release()
    cap = cv2.VideoCapture(0)
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    mask = np.zeros_like(old_frame)
    return p0, old_gray, mask, cap


p0, old_gray, mask, cap = detect_object(cap)
clear_buffer()
old_state = b's'
direccion = 'q';
# move = False

while(1):
    print("----------------------------------------------------------")
    ser.write(direccion.encode())
    state = ser.read()

    print("estado = ", old_state)
    print("nuevo estado =", state)
    if state == b'm' and old_state == b's':
        # started to move
        sleep(SLEEP_TIME)

    elif state == b'm' and old_state == b'm':
        sleep(SLEEP_TIME)
        direccion = 'q'

    elif old_state == b'm' and state == b's':
        direccion = 'q'
        print("Voy a detectar objetos")
        p0, old_gray, mask, cap = detect_object(cap)
        clear_buffer()
        # ser.write(direccion.encode())
        # while ser.read() != b'f':
        #     print("entro a la espera")

    # the robot is not moving
    elif old_state == b's' and state == b's':    
        print("Voy a calcular la foto")
        good, move, direccion = track_object(p0, old_gray, mask, n_frame)
        n_frame = (1 + n_frame) % 10

        

    old_state = state 


cv2.destroyAllWindows()
cap.release()
