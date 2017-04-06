# -*- coding: utf-8 -*-
"""
display-PIL-image-in-pyqt4/Display.PIL.Image.in.PyQt4.py
"""
import sys
from PyQt4.QtGui import *
import cv2

class App(QDialog):
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        window = QGridLayout()
        path = "D:\cv py\savingtest2.jpg"
        
        im = cv2.imread(path, 1)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        height, width = im.shape[:2]
        bytesPerLine = 3 * width # gray : 1*width
        image = QImage(im, width, height, bytesPerLine, QImage.Format_RGB888) # gray : QImage.Format_Indexed8 
        
        pix = QPixmap.fromImage(image)
        lbl = QLabel()
        lbl.setPixmap(pix)
        window.addWidget(lbl,0,0)

        self.setLayout(window)

Application = QApplication(sys.argv)
app = App()
app.show()
Application.exec_()

