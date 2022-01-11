import cv2
from imutils.perspective import four_point_transform
import math
import numpy as np
from matplotlib import pyplot as plt

def drawArea(points):
    global clone
    cv2.line(clone, points[0], points[1], (155, 155, 155), 20)
    cv2.line(clone, points[1], points[2], (155, 155, 155), 20)
    cv2.line(clone, points[2], points[3], (155, 155, 155), 20)
    cv2.line(clone, points[3], points[0], (155, 155, 155), 20)
    cv2.circle(clone, points[0], 20, (0, 255, 0), 20)
    cv2.circle(clone, points[1], 20, (0, 255, 0), 20)
    cv2.circle(clone, points[2], 20, (0, 255, 0), 20)
    cv2.circle(clone, points[3], 20, (0, 255, 0), 20)

#==========================================================
opened_pic_file = "IMG_7510.jpg"
img = cv2.imread(opened_pic_file)
clone = img.copy()

fourPoints = [(736,541), (179,3429), (1545, 3687), (2026, 840)]
drawArea(fourPoints)

imgResize = cv2.resize(clone, (320, 240), interpolation=cv2.INTER_AREA)

# The origin figure transform
srcTransform = four_point_transform(img, np.array(fourPoints))
srcTransformCopy = srcTransform.copy()
srcTransformResize = cv2.resize(srcTransformCopy, (320, 240), interpolation=cv2.INTER_AREA)

# ROI
fourPoints = [(145,826), (137,967), (1119, 908), (1108, 790)]
ROI = four_point_transform(srcTransform, np.array(fourPoints))

# ROI 影像處理
ROIGray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
#cv2.imshow('ROI', ROIGray)

thr = cv2.threshold(ROIGray, int(255/3), 255, cv2.THRESH_BINARY_INV)[1]
#cv2.imshow('thr', thr)

kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(thr, kernel, iterations = 3)
#cv2.imshow('dilate', dilate)

erode = cv2.erode(dilate, kernel, iterations = 2)
#cv2.imshow('erode', erode)

threshold = cv2.threshold(erode, int(255/3), 255, cv2.THRESH_BINARY_INV)[1]
#cv2.imshow('threshold', threshold)

# 原始ROI太窄小，使用numpy insert 插入空白元素以擴增矩陣
extend = np.ones((threshold.shape[0], 1), np.uint8)*255
threshold = np.insert(threshold, 0, values=extend, axis=1)
threshold = np.insert(threshold, threshold.shape[1], values=extend, axis=1)

extend = np.ones((50,  threshold.shape[1]), np.uint8)*255
threshold = np.insert(threshold, 0, values=extend, axis=0)
threshold = np.insert(threshold, threshold.shape[0], values=extend, axis=0)
#cv2.imshow("Extend", threshold)

#cv2.imwrite("test6.jpg", threshold)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# ROI => OCR 文字辨識
from PIL import Image
import pytesseract
from pytesseract import Output

d = pytesseract.image_to_data(threshold, output_type=Output.DICT)
print(d.keys())
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(threshold, (x, y), (x + w, y + h), (166, 18, 166), 2)
#cv2.imshow('Final', threshold)

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Miller.Huang\Anaconda3\Library\bin\tesseract.exe"
text = pytesseract.image_to_string(threshold)
print(text)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

# 繪圖設置
fig=plt.figure(figsize=(8,8))
ax1=fig.add_subplot(321)
ax1.imshow(imgResize)
ax1.set_title("source image")
ax1.set_xticks([])
ax1.set_yticks([])

ax2=fig.add_subplot(322)
ax2.imshow(srcTransformResize)
ax2.set_title("transformed image")
ax2.set_xticks([])
ax2.set_yticks([])

ax3=fig.add_subplot(312)
ax3.imshow(ROI)
ax3.set_title("transformed ROI")
ax3.set_xticks([])
ax3.set_yticks([])

ax4=fig.add_subplot(313)
ax4.imshow(threshold)
ax4.set_title("OCR Object")
ax4.set_xticks([])
ax4.set_yticks([])
plt.show()