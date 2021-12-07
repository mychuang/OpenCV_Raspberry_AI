"""
2.歐洲散步題目
TownCentreXVID.mp4是歐洲人在街道散步,
上課有用 bitwise_and, bitwise_or, bitwise_xor 示範去背的部分,
以此概念來圈出畫面非黑色的物體.
   sudo code
1. Open vedio, convert to gray
2. Preprocess the frame
3. Track the moving object, then get mask
4. Plot the result
"""
import cv2
import numpy as np
# == create show window
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
width  = 320 #640
height = 240 #480

def laplacian(f):
    temp = cv2.Laplacian(f, cv2.CV_32F) + 128
    g = np.uint8(np.clip(temp, 0,255))
    return g

capture = cv2.VideoCapture("../data/TownCentreXVID.mp4")
MOG2 = cv2.createBackgroundSubtractorMOG2()
while(1):
    ret, frame = capture.read()
    if frame is not None:
        frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
        #cv2.imshow("Frame", frame)

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        medFrame = cv2.medianBlur(grayFrame, 5)
        lMedFrame = laplacian(medFrame)
        #cv2.imshow("LaplacianMedian", lMedFrame)

        mog2_img = MOG2.apply(lMedFrame)
        cv2.imshow("MOG2", mog2_img)
        Circle = cv2.cvtColor(mog2_img, cv2.COLOR_GRAY2BGR)

        # b100 & b101 = b100
        bitwiseAnd = cv2.bitwise_and(frame, Circle)
        mask = cv2.cvtColor(bitwiseAnd, cv2.COLOR_BGR2GRAY)
        cv2.imshow("AND", mask)

        # ==== Plot the contours ====
        contours, hierarchy = cv2.findContours(mask,
                                               cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)
        contour_list = []
        maxPixel = 50
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > maxPixel:  # if the area greater maxPixel then store the ndarray
                contour_list.append(contour)

        # == get bounding for each contour object, then plot the bounding
        for contourMember in contour_list:
            x, y, w, h = cv2.boundingRect(contourMember)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('frame', frame)

    else:
        print("Can't find Video")
        break

    keyboard = cv2.waitKey(30)
    if keyboard == ord('q') or keyboard == 27:
        break
capture.release()
cv2.destroyAllWindows()