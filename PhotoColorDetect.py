import cv2 as cv
from util import get_limits

image = cv.imread('apple-virus1.jpg')

yellow = [0, 255, 255]
green = [0, 255, 0]

if image is None:
    print("Failed to read image file")
    exit()

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

yellowLowerLimit, yellowUpperLimit = get_limits(color=yellow)
greenLowerLimit, greenUpperLimit = get_limits(color=green)

yellowMask = cv.inRange(hsv, yellowLowerLimit, yellowUpperLimit)
greenMask = cv.inRange(hsv, greenLowerLimit, greenUpperLimit)

yellowPixels = cv.countNonZero(yellowMask)
greenPixels = cv.countNonZero(greenMask)

yellowAndGreenPixels = cv.countNonZero(yellowMask | greenMask)

print(greenPixels)
print(yellowPixels)


yellowToGreenRatio = yellowPixels / greenPixels

print("Yellow to green pixel ratio:", yellowToGreenRatio)

cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()