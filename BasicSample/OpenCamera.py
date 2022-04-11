import numpy as np
import cv2

cap = cv2.VideoCapture(0)

countMax = 20
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        count = count + 1
        # 降 frame Rate
        if(count == countMax):
            frame = cv2.resize(frame, (320, 240))
            cv2.imshow('frame', frame)
            count = 0
    else:
        break

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()