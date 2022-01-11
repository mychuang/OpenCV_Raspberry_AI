import cv2
import numpy as np

import cv2
from imutils.perspective import four_point_transform
import math
import numpy as np
from matplotlib import pyplot as plt

def OCR(ROI):
    # ROI 影像處理
    ROIGray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('ROI', ROIGray)

    equa = cv2.equalizeHist(ROIGray)
    #cv2.imshow('enhance', equa)

    thr = cv2.threshold(equa, int(255 / 3), 255, cv2.THRESH_BINARY_INV)[1]
    #cv2.imshow('thr', thr)

    kernel = np.ones((3, 3), np.uint8)
    erode = cv2.erode(thr, kernel, iterations=1)
    #cv2.imshow('erode', erode)

    dilate = cv2.dilate(erode, kernel, iterations=1)
    #cv2.imshow('dilate', dilate)

    threshold = cv2.threshold(erode, int(255 / 3), 255, cv2.THRESH_BINARY_INV)[1]
    # cv2.imshow('threshold', threshold)

    # 原始ROI太窄小，使用numpy insert 插入空白元素以擴增矩陣
    extend = np.ones((threshold.shape[0], 1), np.uint8) * 255
    threshold = np.insert(threshold, 0, values=extend, axis=1)
    threshold = np.insert(threshold, threshold.shape[1], values=extend, axis=1)

    extend = np.ones((50, threshold.shape[1]), np.uint8) * 255
    threshold = np.insert(threshold, 0, values=extend, axis=0)
    threshold = np.insert(threshold, threshold.shape[0], values=extend, axis=0)
    cv2.namedWindow('ExtendOCR', cv2.WINDOW_NORMAL)
    cv2.imshow("ExtendOCR", threshold)

    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Miller.Huang\Anaconda3\Library\bin\tesseract.exe"
    text = pytesseract.image_to_string(threshold, lang="chi_tra")
    print(text)

def click_event(event, x, y, flags, param):
    global select_point_num
    global clone
    global star_points

    if event == cv2.EVENT_LBUTTONDOWN and select_point_num < 4:
        print(x, y, select_point_num)
        select_point_num = select_point_num + 1
        point = (x, y)
        star_points.append(point)

    if event == cv2.EVENT_RBUTTONDOWN and select_point_num == 4:
        srcTransform = four_point_transform(clone, np.array(star_points))
        #cv2.imshow("clone", srcTransform)
        OCR(srcTransform)


cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.setMouseCallback("original", click_event)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
select_point_num = 0
star_points = []
while True:
    # 获取每一帧
    ret, img = cap.read()
    clone = img.copy()
    if ret==True:
        # 顯示圖片
        if(len(star_points)>0):
            for i in range(len(star_points)):
                cv2.circle(img, star_points[i], 2, (0, 255, 0), 2)
        if (len(star_points) == 4):
            cv2.line(img, star_points[0], star_points[1], (155, 155, 155), 5)
            cv2.line(img, star_points[1], star_points[2], (155, 155, 155), 5)
            cv2.line(img, star_points[2], star_points[3], (155, 155, 155), 5)
            cv2.line(img, star_points[3], star_points[0], (155, 155, 155), 5)
            cv2.putText(img, "Click right for OCR", star_points[1], cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        cv2.imshow('original', img)

    k = cv2.waitKey(1)  # & 0xFF
    if k == ord('q'):
        break
# 关闭窗口
cap.release()
cv2.destroyAllWindows()

