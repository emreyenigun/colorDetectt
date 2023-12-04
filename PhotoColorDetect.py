import cv2 as cv
from util import get_limits

image = cv.imread('MosaicLettuce.jpg')

yellow = [0, 255, 255]

if image is None:
    print("Failed to read image file")
    exit()

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

lowerLimit, upperLimit = get_limits(color=yellow)

mask = cv.inRange(hsv, lowerLimit, upperLimit)

totalPixels = mask.shape[0] * mask.shape[1]

yellowPixels = cv.countNonZero(mask)

nonYellowPixels = totalPixels - yellowPixels

yellowPixelPercentage = (yellowPixels / totalPixels) * 100

print("Yellow pixel percentage:", yellowPixelPercentage)

cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()