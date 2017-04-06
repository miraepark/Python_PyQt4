# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWindow.ui'
#
# Created: Mon Mar 13 13:46:04 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(553, 505)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 41))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"HY나무B\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtKeyword = QtGui.QLineEdit(self.centralwidget)
        self.txtKeyword.setGeometry(QtCore.QRect(90, 10, 331, 41))
        self.txtKeyword.setObjectName(_fromUtf8("txtKeyword"))
        self.btnSearch = QtGui.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(430, 10, 101, 41))
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.resultTable = QtGui.QTableWidget(self.centralwidget)
        self.resultTable.setGeometry(QtCore.QRect(40, 70, 461, 341))
        self.resultTable.setObjectName(_fromUtf8("resultTable"))
        self.resultTable.setColumnCount(2)
        self.resultTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOepn = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/USER/Pictures/open.JPG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/USER/Pictures/save.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOepn.setIcon(icon)
        self.actionOepn.setObjectName(_fromUtf8("actionOepn"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/USER/Pictures/save.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menu.addAction(self.actionOepn)
        self.menu.addAction(self.actionSave)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.actionOepn)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "키워드", None))
        self.btnSearch.setText(_translate("MainWindow", "PushButton", None))
        item = self.resultTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No", None))
        item = self.resultTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title", None))
        self.menu.setTitle(_translate("MainWindow", "파일", None))
        self.menu_2.setTitle(_translate("MainWindow", "편집", None))
        self.menu_3.setTitle(_translate("MainWindow", "도움말", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOepn.setText(_translate("MainWindow", "열기", None))
        self.actionSave.setText(_translate("MainWindow", "저장", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

