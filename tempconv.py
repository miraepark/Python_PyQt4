# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:36:08 2017

@author: USER
"""

import sys
from PyQt4 import QtCore, QtGui, uic

form_class=uic.loadUiType("tempconv.ui")[0]

class MyWindowClass(QtGui.QMainWindow,form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked)
        self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)
        
    def btn_CtoFclicked(self):
        cel=float(self.editCel.text())
        fahr=cel*9/5.0+32
        self.spiFahr.setValue(int(fahr+0.5))        
        
    def btn_FtoCclicked(self):
        fahr=self.spinFahr.value()
        cel=(fahr-32)/9.0*5
        self.editCel.setText(str(cel))
        
app=QtGui.QApplication(sys.argv)
myWindow=MyWindowClass(None)
myWindow.show()
app.exec_()
        