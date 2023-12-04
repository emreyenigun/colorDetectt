import cv2 as cv
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])  
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  

   
    if hue >= 20 and hue <= 60:
        lowerLimit = np.array([hue - 5, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 5, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([0, 0, 0], dtype=np.uint8)
        upperLimit = np.array([0, 0, 0], dtype=np.uint8)

    return lowerLimit, upperLimit


cv.waitKey(0)