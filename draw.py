import cv2 as cv
import numpy as np

#width, height, number of collor channels
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("blank", blank)

#paint the image
# blank[200:400, 200:400] = 0, 255, 0
# cv.imshow("Blue", blank)

#draw a border

#start, end corrdinates, rgb border color, 
# cv.rectangle(blank, (0,0), (250, 250), (0,250,0), thickness=cv.FILLED)
# cv.imshow('border', blank)

#draw a circle
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 50, (0,0,255), thickness=-1)
# cv.imshow("circle", blank)

#draw a line
# cv.line(blank, (100,100), (250, 250), (255,255,255), thickness=3)
# cv.imshow("line", blank)

#write text on image
cv.putText(blank, "Hello World", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("text", blank)   
cv.waitKey(0)


