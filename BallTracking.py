import numpy as np
import cv2
import math
"""
1.實做color ball tracking
算出物體的長寬,面積大小(單位是公分)
可以球為例
"""

cv2.namedWindow('image')
def nothing(x):
    pass

def ballArea(x, y, r):
    # 1 pix ~= 0.026458333 cm
    alpha = 0.026458333
    x = alpha*x
    y = alpha*y
    r = alpha*r
    return round(2*math.pi*(r**2), 1)

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    if frame is not None:
        # == Resize frame, then convert to HSV & filter it
        frame = cv2.resize(frame, (320, 200), interpolation=cv2.INTER_AREA)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        img_median = cv2.medianBlur(img, 5)
        cv2.imshow('image', img_median)

        lower_red = np.array([22, 111, 119])
        upper_red = np.array([75, 251, 255])

        # == Set the mask
        mask = cv2.inRange(img_median, lower_red, upper_red)
        cv2.imshow('Mask', mask)

        # == Get the contours (such like an object (tuple))
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour_list = []

        # == Get a specific area, then store in a list
        maxPixel = 300
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > maxPixel:  # if the area greater maxPixel then store the ndarray
                contour_list.append(contour)

        # == get bounding for each contour object, then plot the bounding
        for contourMember in contour_list:
            x, y, w, h = cv2.boundingRect(contourMember)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # plot the center point
            midx = int((x + x + w) / 2)
            midy = int((y + y + h) / 2)
            cv2.circle(frame, (midx, midy), 2, (0, 255, 255), 2)

            objectArea = ballArea(midx, midy, (x+w)/2)
            text = "Area: " + str(objectArea) + " cm^2"
            cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (219, 168, 0), 1, cv2.LINE_AA)

        cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()