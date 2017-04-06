# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:09:17 2017

@author: USER
"""

from PyQt4.QtGui import *
import sys 
import StudentTable

class XDialog(QDialog, StudentTable.Ui_MyDialog):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
        
        self.btnSave.clicked.connect(self.saveData)
        self.btnCancel.clicked.connect(self.clearData)
        
    def saveData(self):
        with open("data.csv","a",encoding="utf-8") as f:
            s="%s,%s,%s\n" % (self.Editname.text(),self.EditNumber.text(),self.EditMajor.text())
            f.write(s)
        QMessageBox.information(self,"저장","성공적으로 저장")
        
    def clearData(self):
        self.Editname.clear()
        self.EditNumber.clear()
        self.EditMajor.clear()
        
app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()
