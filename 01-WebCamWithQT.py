#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 14:20:01 2021

@author: miller

refer: 
https://reurl.cc/WXogM7 ＃About How to combine Qt & OpenCV

"""

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QKeySequence

from ui_mainwindow import  Ui_MainWindow
import cv2
import datetime

"""
 MVC structure 
 Model->  CameraManager: store & setting the camera state
 View->   Ui_MainWindow: Use Qt UI (pyuic5 to translate .ui to .py)
 Control->MainWindow   : control the UI state & connect camera by OpenCV 
"""

#%%
class CameraManager(QObject):
    frameChanged = pyqtSignal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self._capture = None
        self._interval = 60;
        self._timer = QTimer()
        self._timer.timeout.connect(self._on_timeout)

    @property 
    def capture(self):
        return self._capture

    @capture.setter
    def capture(self, c):
        self._capture = c
        self._capture.set(cv2.CAP_PROP_FRAME_WIDTH, 32)
        self._capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 48)
        
    @property
    def is_active(self):
        if(self._timer.isActive() == True and self.capture is not None):
            return True

    @pyqtSlot()
    def start(self):
        self._timer.start(self._interval)

    @pyqtSlot()
    def stop(self):
        self._timer.stop()
    
    @pyqtSlot()
    def save(self):
        ret, frame = self._capture.read()
        if ret:
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            now = datetime.datetime.now()
            title = datetime.datetime.strftime(now,'%Y%m%d%H%M%S')
            title += ".jpg"
            cv2.imwrite(title,frame)

    @pyqtSlot()
    def _on_timeout(self):
        if self._capture is None:
            return
        
        ret, frame = self._capture.read()
        if ret:
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #h, w = frame.shape[:2]
            #qImg = QImage(
            #    frame.data, w, h, QImage.Format_Grayscale8
            #)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytesPerLine = ch * w
            qImg = QImage(
                frame.data, w, h, bytesPerLine, QImage.Format_RGB888
            )
            self.frameChanged.emit(qImg)

#%%
class MainWindow(QMainWindow, QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.setWindowTitle("WebCam AP")
        self.iniUI()

        self.camera_manager = CameraManager()
        self.camera_manager.frameChanged.connect(self.on_frame_changed)

        self.camera_manager.capture = cv2.VideoCapture(0)

        self.__ui.btnCam.clicked.connect(self.camera_manager.start)
        self.__ui.btnCam.clicked.connect(self.btnUIConnect)
        self.__ui.btnClean.clicked.connect(self.camera_manager.stop)
        self.__ui.btnClean.clicked.connect(self.btnUIDisconnect)
        self.__ui.btnSave.clicked.connect(self.on_s_pressed)
        
        QShortcut(
            QKeySequence(Qt.Key_P), self, activated=self.on_p_pressed
        )
        QShortcut(
            QKeySequence(Qt.Key_S), self, activated=self.on_s_pressed
        )

    def iniUI(self):
        self.__ui.btnCam.setStyleSheet("background-color: rgb(142, 192, 245);")
        self.__ui.btnSave.setStyleSheet("background-color: rgb(46, 8, 99);")
        self.__ui.btnSave.setEnabled(False)
        self.__ui.btnClean.setStyleSheet("background-color: rgb(46, 8, 99);")
        self.__ui.btnClean.setEnabled(False)
        
    @pyqtSlot(QImage)
    def on_frame_changed(self, image):
        pixmap = QPixmap.fromImage(image)
        self.__ui.label.setPixmap(pixmap)

    @pyqtSlot()
    def on_p_pressed(self):
        if self.camera_manager.is_active:
            self.camera_manager.stop()
            
    @pyqtSlot()
    def on_s_pressed(self):
        if self.camera_manager.is_active:
            self.camera_manager.save()
            
    @pyqtSlot()
    def btnUIConnect(self):
        if self.camera_manager.is_active:
            self.__ui.btnCam.setStyleSheet("background-color: rgb(46, 8, 99);")
            self.__ui.btnCam.setEnabled(False)
            self.__ui.btnSave.setStyleSheet("background-color: rgb(142, 192, 245);")
            self.__ui.btnSave.setEnabled(True)
            self.__ui.btnClean.setStyleSheet("background-color: rgb(142, 192, 245);")
            self.__ui.btnClean.setEnabled(True)
            
    @pyqtSlot()
    def btnUIDisconnect(self):        
        self.__ui.btnCam.setStyleSheet("background-color: rgb(142, 192, 245);")
        self.__ui.btnCam.setEnabled(True)
        self.__ui.btnSave.setStyleSheet("background-color: rgb(46, 8, 99);")
        self.__ui.btnSave.setEnabled(False)
        self.__ui.btnClean.setStyleSheet("background-color: rgb(46, 8, 99);")
        self.__ui.btnClean.setEnabled(False)
            

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())