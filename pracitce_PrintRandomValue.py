# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice_PrintRandomValue.ui'
#
# Created: Mon Apr 03 10:17:31 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
        MainWindow.resize(748, 415)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        #%%
        #Talbe_1
        self.Table_1 = QtGui.QTableWidget(self.centralwidget)
        self.Table_1.setGeometry(QtCore.QRect(20, 80, 341, 231))
        self.Table_1.setObjectName(_fromUtf8("Table_1"))
        self.Table_1.setColumnCount(3)
    
#        self.Table_1.setRowCount(1)
        #Talbe_1(rows)
#        item = QtGui.QTableWidgetItem()
#        self.Table_1.setVerticalHeaderItem(0, item)
    
        #Table_1(3 columns)
        item = QtGui.QTableWidgetItem()
        self.Table_1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Table_1.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.Table_1.setHorizontalHeaderItem(2, item)
        #%%
        #Table_2
        self.Table_2 = QtGui.QTableWidget(self.centralwidget)
        self.Table_2.setGeometry(QtCore.QRect(380, 80, 341, 231))
        self.Table_2.setObjectName(_fromUtf8("Table_2"))
        self.Table_2.setColumnCount(3)
#        self.Table_2.setRowCount(1)
        #Table_2(10 rows)
#        item = QtGui.QTableWidgetItem()
#        self.Table_2.setVerticalHeaderItem(0, item)
        #Table_2(3 columns)
        item = QtGui.QTableWidgetItem()
        self.Table_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Table_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.Table_2.setHorizontalHeaderItem(2, item)
        #%%
        #label
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 321, 41))
        self.label.setStyleSheet(_fromUtf8("font: 75 36pt \"210 멋진어느날 R\";"))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        #추가 
        for i in range(1,11):
            self.insertValue(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 함수
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        #%%
        #table_1
#        item = self.Table_1.verticalHeaderItem(0)
#        item.setText(_translate("MainWindow", "1", None))
        item = self.Table_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "최대 폭", None))
        item = self.Table_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "평균 폭", None))
        item = self.Table_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "길이", None)) 
        
        #%%
        #table_2
#        item = self.Table_2.verticalHeaderItem(0)
#        item.setText(_translate("MainWindow", "1", None))    
        item = self.Table_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "이미지", None))
        item = self.Table_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "상태", None))
        item = self.Table_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "비교", None))

        #%%
        self.label.setText(_translate("MainWindow", "PRINT Random Value", None))

#%% value 추가 함수(행 추가)
    def insertValue(self,MainWindowm):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        #table_1 행추가
        rowPosition = self.Table_1.rowCount()
        self.Table_1.insertRow(rowPosition)
        x=random.randint(1,100)
        y=random.randint(100,200)
        z=random.randint(200,300)
        self.Table_1.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(x)))
        self.Table_1.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(y)))
        self.Table_1.setItem(rowPosition , 2, QtGui.QTableWidgetItem(str(z)))
        
        #table_2 행추가
        rowPosition = self.Table_2.rowCount()
        self.Table_2.insertRow(rowPosition)
        a=random.randint(1,100)
        b=random.randint(100,200)
        c=random.randint(200,300)
        self.Table_2.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(a)))
        self.Table_2.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(b)))
        self.Table_2.setItem(rowPosition , 2, QtGui.QTableWidgetItem(str(c)))
        
  #%%      
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

