# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child.ui'
#
# Created: Thu Nov 24 19:57:42 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3 as lite
from src.view_bills import dbase_results_gui

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

class Ui_Dialog11(object):

    def dbase_results(self):
        customer_name = self.cname_edit.text()
        allSQLRows = dbase_results_gui(str(customer_name))
        # this code is moved to view_bills.py for abstraction in gui.
        # connection_db = lite.connect("/home/chakri/SQLite/smarket_db.sqlite")
        # csr = connection_db.cursor()
        # allSQLRows = csr.execute('''select invoice_items.invoice_id, invoice_items.item_id, items.item_name, invoice_items.quantity, items.item_price,
        #                                 (invoice_items.quantity * items.item_price) as Price from customer join items join invoice_items join invoice
        #                                  on invoice.invoice_number = invoice_items.invoice_id and invoice.customer_id = customer.id and
        #                                  items.item_id = invoice_items.item_id and customer.name= ?
        #                                  ''', (str(customer_name),)).fetchall()

        self.tableWidget.setRowCount(len(allSQLRows))  ##set number of rows
        self.tableWidget.setColumnCount(6)  ## set number of columns
        for x in range(0, len(allSQLRows)):
            r = allSQLRows[x]
            for col in range(0, 6):
                self.tableWidget.setItem(x, col, QtGui.QTableWidgetItem(str(r[col])))

    def clear_text(self):
        self.cname_edit.clear()
        self.tableWidget.clearContents()

    def setupUi(self, Dialog1):
        Dialog1.setObjectName(_fromUtf8("Dialog1"))
        Dialog1.resize(650, 389)
        self.tableWidget = QtGui.QTableWidget(Dialog1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 620, 241))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.search_button = QtGui.QPushButton(Dialog1)
        self.search_button.setGeometry(QtCore.QRect(330, 30, 81, 26))
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.cname_edit = QtGui.QLineEdit(Dialog1)
        self.cname_edit.setGeometry(QtCore.QRect(200, 30, 113, 27))
        self.cname_edit.setText(_fromUtf8(""))
        self.cname_edit.setObjectName(_fromUtf8("cname_edit"))
        self.exit_button = QtGui.QPushButton(Dialog1)
        self.exit_button.setGeometry(QtCore.QRect(540, 340, 91, 26))
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.clear_button = QtGui.QPushButton(Dialog1)
        self.clear_button.setGeometry(QtCore.QRect(420, 30, 91, 26))
        self.clear_button.setObjectName(_fromUtf8("clear_button"))


        self.retranslateUi1(Dialog1)
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL("clicked()"), Dialog1.accept)
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL("clicked()"), self.clear_text)
        QtCore.QObject.connect(self.search_button, QtCore.SIGNAL("clicked()"), self.dbase_results)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi1(self, Dialog1):
        Dialog1.setWindowTitle(_translate("Dialog1", "Dialog1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog1", "Invoice", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog1", "ItemID", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog1", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog1", "Quantity", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog1", "Price", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog1", "Total", None))
        self.search_button.setText(_translate("Dialog1", "Search", None))
        self.exit_button.setText(_translate("Dialog1", "Exit", None))
        self.clear_button.setText(_translate("Dialog1", "Clear", None))
        self.dbase_results()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog1 = QtGui.QDialog()
    ui = Ui_Dialog11()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())

