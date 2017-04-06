# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice_PrintImage.ui'
#
# Created: Mon Apr 03 16:06:20 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import cv2
import random

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(788, 399)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 10, 301, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 20pt \"210 멋진어느날 R\";\n"
"background-color: rgb(255, 255, 255);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(460, 50, 311, 291))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(20, 20, 420, 320))
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setPixmap(QtGui.QPixmap(_fromUtf8("image.jpg")))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.imageUi(MainWindow)
        self.imageScaleUi(MainWindow)
            
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "이미지 정보 출력_단위(픽셀)", None))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "가로", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "세로", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "너비", None))
    
    def imageUi(self, MainWindow):
        path = "D:\Anaconda2\Lib\site-packages\PyQt4\savingtest2.jpg"
        
        im = cv2.imread(path, 1)

        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        height, width = im.shape[:2]
        bytesPerLine = 3 * width # gray : 1*width
        image = QImage(im, width, height, bytesPerLine, QImage.Format_RGB888) # gray : QImage.Format_Indexed8 
        
        pixmap = QPixmap.fromImage(image)
        #이미지 사이즈 조정(400*300)
        pix=pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        
        self.imageLabel.setPixmap(pix)
        
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        area=height*width
        self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(height)))
        self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(width)))
        self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(str(area)))

    
    def imageScaleUi(self, MainWindow):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        
        #pixmap scaled size 
        scaledWidth=400
        scaledHeight=300
        scaledArea=scaledWidth*scaledHeight
        self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(scaledWidth)))
        self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(scaledHeight)))
        self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(str(scaledArea)))

        


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

