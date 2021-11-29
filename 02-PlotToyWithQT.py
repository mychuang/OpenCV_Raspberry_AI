#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:58:31 2021

@author: miller
"""

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

import sys # for exiting
import cv2
import numpy as np

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Plotting Toy")

# ui setting
label = QLabel()
btnLine = QPushButton("Line")
btnCircle = QPushButton("Cirle")
btnSquar = QPushButton("Square")
btnClean = QPushButton("Clean")

hLayout = QHBoxLayout()
hLayout.addWidget(btnLine)
hLayout.addWidget(btnCircle)
hLayout.addWidget(btnSquar)
hLayout.addWidget(btnClean)

vLayout = QVBoxLayout()

vLayout.addWidget(label)
vLayout.addLayout(hLayout)

# setting slot function
def defaultMap():
    global img
    img = np.zeros([400, 500, 3], dtype='uint8')

def getQPixmap():
    h, w, ch = img.shape
    bytesPerLine = ch * w
    qImg = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(qImg)
    return pixmap

def plotLine():
    cv2.line(img, (50,50), (150,150), (255, 0, 0), 2, cv2.LINE_AA, 0)
    pixmap = getQPixmap()
    label.setPixmap(pixmap)
    btnLine.setEnabled(False)

def plotSquare():
    cv2.rectangle(img, (300,50), (400,200), (0, 255, 0), 1, cv2.LINE_AA)
    pixmap = getQPixmap()
    label.setPixmap(pixmap)
    btnSquar.setEnabled(False)

def plotCircle():
    cv2.circle(img, (300, 300), 50, (0, 0, 255), -1)
    pixmap = getQPixmap()
    label.setPixmap(pixmap)
    btnCircle.setEnabled(False)

def plotClean():
    global img
    defaultMap()
    pixmap = getQPixmap()
    label.setPixmap(pixmap)
    btnLine.setEnabled(True)
    btnCircle.setEnabled(True)
    btnSquar.setEnabled(True)

# setting black map
img = np.zeros([400, 500, 3], dtype='uint8')
pixmap = getQPixmap()
label.setPixmap(pixmap)

# setting connect
btnLine.clicked.connect(plotLine)
btnSquar.clicked.connect(plotSquare)
btnClean.clicked.connect(plotClean)
btnCircle.clicked.connect(plotCircle)

#%% exec
window.setLayout(vLayout)
window.show()
app.exec_()






