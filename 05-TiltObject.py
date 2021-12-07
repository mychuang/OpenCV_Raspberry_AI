import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
from pprint import pprint

def vector(x1, y1, x2, y2):
    u = x2-x1
    v = y2-y1
    return (u, v)

def vectorTheta(u0, v0, u1, v1):
    innerProduct = u0*u1 + v0*v1
    L1 = math.sqrt(u0**2 + v0**2)
    L2 = math.sqrt(u1**2 + v1**2)
    theta = math.acos(innerProduct/(L1*L2))
    return theta

# (1) read original data
image = cv2.imread('img2.png')
clone=image.copy()
plt.subplot(221), plt.imshow(image)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# (2) Convert to Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(222), plt.imshow(gray)
plt.title('Gray'), plt.xticks([]), plt.yticks([])

# (3) Gaussion Blur
blurred = cv2.GaussianBlur(gray, (9, 9), 0)
plt.subplot(223), plt.imshow(blurred)
plt.title('Blur'), plt.xticks([]), plt.yticks([])

# (4) Binnary: use canny method
binaryIMG = cv2.Canny(blurred, int(255/3), 255)
plt.subplot(224), plt.imshow(binaryIMG)
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.show()

# (5) get Contours and calculate the rotation angle
contours, hierarchy = cv2.findContours(binaryIMG.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
index = 0
sourceROI = []
angleList = []
thetaList = []

#cv2.namedWindow('clone',cv2.WINDOW_NORMAL)
for cnt in contours:
    index = index + 1
    M = cv2.moments(cnt)

    if M['m00'] > 0:  #零階矩相當於面積 (像素強度總和)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(clone, (cx, cy), 3, (1, 227, 254), -1)
        print("contour: ", index, "at: ", cx, cy)
        print("area: ", M['m00'], " arcLength: ", round(cv2.arcLength(cnt, True),1))

        # 邊界矩形
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(clone, (x,y), (x+w, y+h), (0,255,0), 2)
        (u0, v0) = vector(x, y, x+w, y)

        # 取出物件
        ROI = image[y-5:y+h+5, x-5:x+w+5]
        sourceROI.append(ROI)

        # 橢圓擬合
        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(clone, ellipse, (0, 255, 255), 2)

        # 最小外接圆
        (x0, y0), radius = cv2.minEnclosingCircle(cnt)
        cv2.circle(clone, (int(x0), int(y0)), int(radius), (255, 255, 255), 2)

        # 旋轉邊界最小矩形 (we will use this to rotate)
        rotrect = cv2.minAreaRect(cnt)
        box = np.int0(cv2.boxPoints(rotrect))  # –> int0會省略小數點後方的數字
        cv2.drawContours(clone, [box], -1, (255, 0, 255), 2)
        (u1, v1) = vector(box[0][0], box[0][1], box[3][0], box[3][1])

        # get angle from rotated rectangle
        angle = rotrect[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        angleList.append(angle)
        print("Angle: ", round(angle, 1), "deg")

        # get angle by inner product
        theta = vectorTheta(u0, v0, u1, v1)
        thetaList.append(theta*180/math.pi)
        print("theta: ", round(theta*180/math.pi, 1), "deg")
        print("----------------------------------------------------")

        # draw arraw line
        (px, py) = (cx+30*math.cos(-angle*math.pi/180), cy+30*math.sin(-angle*math.pi/180))
        #print(round(px,1), round(py,1))
        cv2.arrowedLine(clone, (cx, cy), (int(px), int(py)), (0, 0, 255), 2, cv2.LINE_8, tipLength=0.3)

        # print msg in original image
        cv2.putText(clone,"#%d" %index, (cx-20, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

#cv2.imshow('clone',clone)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# (6) get the objects
for i in range(index):
    plt.subplot(2,3,i+1)
    plt.imshow(cv2.resize(sourceROI[i], (320, 240), interpolation=cv2.INTER_AREA))
    plt.title("#%d" %(i+1))
    plt.xticks([])
    plt.yticks([])
image2 = cv2.resize(clone, (320, 240), interpolation=cv2.INTER_AREA)
plt.subplot(2,3,6), plt.imshow(image2)
plt.title("source image"), plt.xticks([]), plt.yticks([])
plt.show()

# (7) plotting the tilting objects
for i in range(index):
    plt.subplot(3, 5, i+1)
    plt.imshow(cv2.resize(sourceROI[i], (320, 240), interpolation=cv2.INTER_AREA))
    plt.title("origin #%d" % (i + 1))
    plt.xticks([])
    plt.yticks([])
for i in range(index):
    (h, w) = sourceROI[i].shape[:2]
    center = (w // 2, h // 2)
    rotateMat = cv2.getRotationMatrix2D(center, angleList[i], 1.0)
    print(angleList[i])
    rotateImg = cv2.warpAffine(sourceROI[i], rotateMat, (w, h),
                   flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    # plotting
    plt.subplot(3, 5, 5+ i + 1)
    plt.imshow(cv2.resize(rotateImg, (320, 240), interpolation=cv2.INTER_AREA))
    plt.title("tilt_01 #%d" % (i + 1))
    plt.xticks([])
    plt.yticks([])
for i in range(index):
    (h, w) = sourceROI[i].shape[:2]
    center = (w // 2, h // 2)
    rotateMat = cv2.getRotationMatrix2D(center, thetaList[i], 1.0)
    print(thetaList[i])
    rotateImg2 = cv2.warpAffine(sourceROI[i], rotateMat, (w, h),
                   flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    # plotting
    plt.subplot(3, 5, 10+ i + 1)
    plt.imshow(cv2.resize(rotateImg2, (320, 240), interpolation=cv2.INTER_AREA))
    plt.title("tilt_02 #%d" % (i + 1))
    plt.xticks([])
    plt.yticks([])

plt.show()
