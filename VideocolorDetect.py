import cv2 as cv
from util import get_limits

yellow = [0, 255, 255]
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

totalPixels = 0
yellowPixels = 0
nonYellowPixels = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv.inRange(hsv, lowerLimit, upperLimit)

    totalPixels += mask.shape[0] * mask.shape[1]

    yellowPixels += cv.countNonZero(mask)

    nonYellowPixels = totalPixels - yellowPixels

    #percentage of yellow pixelsq
    yellowPixelPercantage = (yellowPixels / totalPixels) * 100

    print("Yellow pixel percentage:", yellowPixelPercantage)

    cv.imshow("cam", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()