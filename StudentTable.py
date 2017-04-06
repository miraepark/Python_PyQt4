# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentTable.ui'
#
# Created: Thu Mar 09 13:55:02 2017
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

class Ui_MyDialog(object):
    def setupUi(self, MyDialog):
        MyDialog.setObjectName(_fromUtf8("MyDialog"))
        MyDialog.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(MyDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 91, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbname = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbname.setAlignment(QtCore.Qt.AlignCenter)
        self.lbname.setObjectName(_fromUtf8("lbname"))
        self.verticalLayout.addWidget(self.lbname)
        self.lbnumber = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbnumber.setAlignment(QtCore.Qt.AlignCenter)
        self.lbnumber.setObjectName(_fromUtf8("lbnumber"))
        self.verticalLayout.addWidget(self.lbnumber)
        self.lbmajor = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbmajor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbmajor.setObjectName(_fromUtf8("lbmajor"))
        self.verticalLayout.addWidget(self.lbmajor)
        self.verticalLayoutWidget_2 = QtGui.QWidget(MyDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(129, 69, 231, 111))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Editname = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Editname.setObjectName(_fromUtf8("Editname"))
        self.verticalLayout_2.addWidget(self.Editname)
        self.EditNumber = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.EditNumber.setObjectName(_fromUtf8("EditNumber"))
        self.verticalLayout_2.addWidget(self.EditNumber)
        self.EditMajor = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.EditMajor.setObjectName(_fromUtf8("EditMajor"))
        self.verticalLayout_2.addWidget(self.EditMajor)
        self.horizontalLayoutWidget = QtGui.QWidget(MyDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 220, 331, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnSave = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnCancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)

        self.retranslateUi(MyDialog)
        QtCore.QMetaObject.connectSlotsByName(MyDialog)

    def retranslateUi(self, MyDialog):
        MyDialog.setWindowTitle(_translate("MyDialog", "학생 테이블", None))
        self.lbname.setText(_translate("MyDialog", "이름", None))
        self.lbnumber.setText(_translate("MyDialog", "학번", None))
        self.lbmajor.setText(_translate("MyDialog", "학과", None))
        self.btnSave.setText(_translate("MyDialog", "저장", None))
        self.btnCancel.setText(_translate("MyDialog", "취소", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MyDialog = QtGui.QDialog()
    ui = Ui_MyDialog()
    ui.setupUi(MyDialog)
    MyDialog.show()
    sys.exit(app.exec_())

