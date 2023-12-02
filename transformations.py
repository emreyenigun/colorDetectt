import cv2 as cv
import numpy as np

img = cv.imread('hero-fantasy.png')
cv.imshow("fantasy", img)

#Translation

# def translate(img, x, y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)

# translated = translate(img, 0, 600)
# cv.imshow("translated", translated)

#rotation
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
    
#     if rotPoint is None:
#         rotPoint = (height // 2, width // 2)
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, -20)
# cv.imshow("rotated", rotated)



#flipping

# flip = cv.flip(img, -1)
# cv.imshow("flip", flip)

#Cropped


cv.waitKey(0)