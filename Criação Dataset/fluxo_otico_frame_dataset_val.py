import cv2
import numpy as np
from numpy import *

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

### FRAMES NOPORNO ####


img1 = cv2.imread("./val/noporno1.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (256,256))

img2 = cv2.imread("./val/noporno1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (256,256))

flow = cv2.calcOpticalFlowFarneback(img1,img2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
img_out = draw_hsv(flow)

img_out_name = "./dataset_fluxo_val/noporno_flow1.jpg";
cv2.imwrite(img_out_name,img_out)

cont = 0;

for item in range(2,86017):


    img1_in = "./val/noporno" +  str(item - 1) + ".jpg" ;	
    img2_in = "./val/noporno" +  str(item) + ".jpg" ;

    img1 = cv2.imread(img1_in, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (256,256))

    img2 = cv2.imread(img2_in, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.resize(img2, (256,256))

    flow = cv2.calcOpticalFlowFarneback(img1,img2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    img_out = draw_hsv(flow)
    
    img_out_name = "./dataset_fluxo_val/noporno_flow" + str(item) + ".jpg";
    cv2.imwrite(img_out_name,img_out)
    
    cont = cont + 1
    if( cont == 1000):
    	cont = 0;
        print("noporno: " + str(item))

### FRAMES PORNO ###

img1 = cv2.imread("./val/porno1.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (256,256))

img2 = cv2.imread("./val/porno1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (256,256))

flow = cv2.calcOpticalFlowFarneback(img1,img2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
img_out = draw_hsv(flow)

img_out_name = "./dataset_fluxo_val/porno_flow1.jpg";
cv2.imwrite(img_out_name,img_out)


for item in range(2,193738):

    img1_in = "./val/porno" +  str(item - 1) + ".jpg" ;
    img2_in = "./val/porno" +  str(item) + ".jpg" ;

    img1 = cv2.imread(img1_in, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (256,256))

    img2 = cv2.imread(img2_in, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.resize(img2, (256,256))

    flow = cv2.calcOpticalFlowFarneback(img1,img2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    img_out = draw_hsv(flow)

    img_out_name = "./dataset_fluxo_val/porno_flow" + str(item) + ".jpg";
    cv2.imwrite(img_out_name,img_out)

    cont = cont + 1
    if( cont == 1000):
        cont = 0;
        print("porno: " + str(item))
