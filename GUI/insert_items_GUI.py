# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_items_GUI.ui'
#
# Created: Sat Nov 26 10:50:01 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from src.insert_items import insert_items_gui
import re
import sys

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

class Ui_InsertItems(object):

    def setupUi(self, Dialog4):
        Dialog4.setObjectName(_fromUtf8("Dialog4"))
        Dialog4.resize(251, 201)
        self.pushButton_1 = QtGui.QPushButton(Dialog4)
        self.pushButton_1.setGeometry(QtCore.QRect(53, 145, 80, 31))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(Dialog4)
        self.pushButton_2.setGeometry(QtCore.QRect(145, 145, 80, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_1 = QtGui.QLineEdit(Dialog4)
        self.lineEdit_1.setGeometry(QtCore.QRect(110, 30, 113, 27))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog4)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 65, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Dialog4)
        self.label.setGeometry(QtCore.QRect(10, 35, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog4)
        self.label_2.setGeometry(QtCore.QRect(15, 70, 41, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog4)
        self.label_3.setGeometry(QtCore.QRect(15, 105, 66, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog4)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 100, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.retranslateUi4(Dialog4)
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL("clicked()"), self.clear_text)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.show_message)
        QtCore.QMetaObject.connectSlotsByName(Dialog4)


    def retranslateUi4(self, Dialog4):
        Dialog4.setWindowTitle(_translate("Dialog4", "Dialog4", None))
        self.label.setText(_translate("Dialog4", "  Item Name", None))
        self.label_2.setText(_translate("Dialog4", "Price", None))
        self.label_3.setText(_translate("Dialog4", "Quantity", None))
        self.pushButton_1.setText(_translate("Dialog4", "Clear", None))
        self.pushButton_2.setText(_translate("Dialog4", "Add", None))

    def show_message(self):
        msg = QtGui.QMessageBox()
        try:
            int(self.lineEdit_3.text())
            insert_items_gui(self.lineEdit_1.text(), self.lineEdit_2.text())
            QtGui.QMessageBox.setIcon(msg, QtGui.QMessageBox().Information)
            QtGui.QMessageBox.about(msg, 'Info', 'Insert Successful')
            self.clear_text()
        except Exception:
            QtGui.QMessageBox.setIcon(msg, QtGui.QMessageBox().Critical)
            QtGui.QMessageBox.about(msg, 'Error', 'Input can only be a number')
            self.lineEdit_3.clear()


    def clear_text(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog4 = QtGui.QDialog()
    ui = Ui_InsertItems()
    ui.setupUi(Dialog4)
    Dialog4.show()
    sys.exit(app.exec_())

