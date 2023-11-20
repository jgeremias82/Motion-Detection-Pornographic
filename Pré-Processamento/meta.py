import cv2
import numpy as np
from numpy import *
import os.path

def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[...,0] = ang*(180/np.pi/2)
    hsv[...,1] = 255
    hsv[...,2] = np.minimum(v*4, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr

img1 = cv2.imread("./teste1.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (256,256))

img2 = cv2.imread("./teste2.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (256,256))

flow = cv2.calcOpticalFlowFarneback(img1,img2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
img_out = draw_hsv(flow)

img_out_name = "./teste3.jpg";
cv2.imwrite(img_out_name,img_out)

