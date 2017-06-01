import numpy as np
import cv2

cap0 = cv2.VideoCapture(1)
cap1 = cv2.VideoCapture(2)
# disparity range is tuned for 'aloe' image pair
window_size = 3
min_disp = 16
num_disp = 112-min_disp

stereo = cv2.StereoSGBM_create(numDisparities = num_disp,
            blockSize = 16, minDisparity=min_disp)

while(True):
    # Capture frame-by-frame
    ret0, imgL = cap0.read()
    ret1, imgR = cap1.read()

    print('computing disparity...')
    disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    # print('generating 3d point cloud...',)
    # h, w = imgL.shape[:2]
    # f = 0.8*w                          # guess for focal length
    # Q = np.float32([[1, 0, 0, -0.5*w],
    #                 [0,-1, 0,  0.5*h], # turn points 180 deg around x-axis,
    #                 [0, 0, 0,     -f], # so that y-axis looks up
    #                 [0, 0, 1,      0]])
    # points = cv2.reprojectImageTo3D(disp, Q)
    # colors = cv2.cvtColor(imgL, cv2.COLOR_BGR2RGB)
    # mask = disp > disp.min()
    # out_points = points[mask]
    # out_colors = colors[mask]
    # out_fn = 'out.ply'
    # write_ply('out.ply', out_points, out_colors)
    # print('%s saved' % 'out.ply')
    # threshold = cv2.threshold(disp, 0.6, 1.0, cv2.THRESH_BINARY)[1]

    cv2.imshow('left', imgL)
    cv2.imshow('disparity', (disp-min_disp)/num_disp)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap0.release()
cv2.destroyAllWindows()
