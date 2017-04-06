# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created: Thu Mar 09 10:32:31 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtGui
from PyQt4 import uic
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot

class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("hello.ui", self)
        self.ui.show()
        self.HelloBtn.clicked.connect(self.slot_1)
        self.ReInputBtn.clicked.connect(self.slot_2)
 
    def slot_1(self,Dialog):
        self.ui.label.setText("HELLO")
           
        
    def slot_2(self,Dialog):
        self.ui.label.setText("INPUT AGAIN")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec_())

