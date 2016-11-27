# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created: Thu Nov 24 15:00:13 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from modify_items_GUI import Ui_ModifyItems
from view_bills_GUI import Ui_Dialog11
from view_items_GUI import Ui_ViewItems
from insert_items_GUI import Ui_InsertItems
from billing_GUI import Ui_Billing

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


class Ui_Dialog(object):
    def view_bill_local(self):
        self.welcomeWindow = QtGui.QDialog()
        self.ui1 = Ui_Dialog11()
        self.ui1.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

    def view_items_local(self):
        self.item_window = QtGui.QDialog()
        self.ui2 = Ui_ViewItems()
        self.ui2.setupUi(self.item_window)
        self.item_window.show()

    def insert_items_local(self):
        self.insert_window = QtGui.QDialog()
        self.ui3 = Ui_InsertItems()
        self.ui3.setupUi(self.insert_window)
        self.insert_window.show()

    def modify_items_local(self):
        self.modify_window = QtGui.QDialog()
        self.ui4 = Ui_ModifyItems()
        self.ui4.setupUi(self.modify_window)
        self.modify_window.show()

    def billing_items_local(self):
        self.billing_window = QtGui.QDialog()
        self.ui5 = Ui_Billing()
        self.ui5.setupUi6(self.billing_window)
        self.billing_window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(426, 296)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 381, 191))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton1 = QtGui.QPushButton(self.tab)
        self.pushButton1.setGeometry(QtCore.QRect(20, 10, 96, 26))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 10, 96, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 10, 111, 26))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 71, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 10, 96, 26))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 10, 131, 26))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        #Here Comes the code for button event handling
        QtCore.QObject.connect(self.pushButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.view_items_local)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.insert_items_local)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.modify_items_local)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.billing_items_local)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.view_bill_local)
        #QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), view_bills)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton1.setText(_translate("Dialog", "View Items", None))
        self.pushButton_2.setText(_translate("Dialog", "Insert Items", None))
        self.pushButton_3.setText(_translate("Dialog", "Modify Items", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Inventory", None))
        self.pushButton.setText(_translate("Dialog", "Billing", None))
        self.pushButton_4.setText(_translate("Dialog", "View Bills", None))
        self.pushButton_5.setText(_translate("Dialog", "Customer Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Billing", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

