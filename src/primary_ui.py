import sys
from PyQt4.QtCore import *
from PyQt4.QtCore import QObject
from PyQt4.QtGui import *
from view_details import view_items
from view_bills import view_bills


def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("View Items")
   b1.move(50,20)
   # b1.clicked.connect(view_items) # for python 3
   QObject.connect(b1,SIGNAL("clicked()"), view_items)

   b2 = QPushButton(win)
   b2.setText("View Bills")
   b2.move(50,50)
   # b2.clicked.connect(view_bills) # for python 3
   QObject.connect(b2, SIGNAL("clicked()"), view_bills)
   win.setGeometry(100,100,200,100)
   win.setWindowTitle("S market")
   win.show()
   sys.exit(app.exec_())


def b1_clicked():
   print "Button 1 clicked"

def b2_clicked():
   print "Button 2 clicked"

if __name__ == '__main__':
   window()