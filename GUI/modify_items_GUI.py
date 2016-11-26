# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_items_GUI.ui'
#
# Created: Sat Nov 26 19:39:41 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from src.modify_items import *

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

class Ui_ModifyItems(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName(_fromUtf8("Dialog5"))
        Dialog5.resize(305, 175)
        self.label = QtGui.QLabel(Dialog5)
        self.label.setGeometry(QtCore.QRect(10, 25, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog5)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 41, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_1 = QtGui.QLineEdit(Dialog5)
        self.lineEdit_1.setGeometry(QtCore.QRect(60, 30, 151, 27))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog5)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 80, 151, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_1 = QtGui.QPushButton(Dialog5)
        self.pushButton_1.setGeometry(QtCore.QRect(130, 130, 71, 26))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(Dialog5)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 30, 71, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog5)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 80, 71, 26))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi5(Dialog5)
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL("clicked()"), self.modify_local)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.lineEdit_1.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi5(self, Dialog5):
        Dialog5.setWindowTitle(_translate("Dialog5", "Modify Items", None))
        self.label.setText(_translate("Dialog5", "Name", None))
        self.label_2.setText(_translate("Dialog5", "Price", None))
        self.pushButton_1.setText(_translate("Dialog5", "OK", None))
        self.pushButton_2.setText(_translate("Dialog5", "Clear", None))
        self.pushButton_3.setText(_translate("Dialog5", "Clear", None))

    def clear_text(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()

    def modify_setValues(self, id):
        self.id_local = id

    def modify_local(self):
        msg = QtGui.QMessageBox()
        message = dbase_modify_results_gui(self.id_local, self.lineEdit_1.text(), self.lineEdit_2.text())
        QtGui.QMessageBox.setIcon(msg, QtGui.QMessageBox().Information)
        QtGui.QMessageBox.about(msg, 'Info', message)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog5 = QtGui.QDialog()
    ui = Ui_ModifyItems()
    ui.setupUi(Dialog5)
    Dialog5.show()
    sys.exit(app.exec_())

