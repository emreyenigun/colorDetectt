import cv2 as cv
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
  
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
  
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
   
    lowerLimit, upperLimit = get_limits(color=yellow)
    
    mask = cv.inRange(hsv, lowerLimit, upperLimit)
    
    mask2 = Image.fromarray(mask)

    bbox = mask2.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (255,0,0), thickness=2) 

    print(bbox)

    cv.imshow("cam", frame) 
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()