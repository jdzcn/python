#!/usr/bin/python3

import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def initializeModel(model):
   model.setTable('product')
   model.setEditStrategy(QSqlTableModel.OnFieldChange)
   model.select()
   #model.setHeaderData(0, Qt.Horizontal, "id")
   #model.setHeaderData(1, Qt.Horizontal, "name")
   #model.setHeaderData(2, Qt.Horizontal, "price")

def createView(title, model):
   view = QTableView()
   view.setModel(model)
   view.setColumnWidth(0, 50)
   view.setColumnWidth(1, 300)
   view.setWindowTitle(title)
   return view

def addrow():
   print (model.rowCount())
   ret = model.insertRows(model.rowCount(), 1)
   print (ret)

def findrow(i):
   delrow = i.row()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('product.db')
   model = QSqlTableModel()
   delrow = -1
   initializeModel(model)

   view1 = createView("Table Model (View 1)", model)
   view1.clicked.connect(findrow)

   dlg = QWidget()
   layout = QVBoxLayout()
   layout.addWidget(view1)

   button = QPushButton("Add a row")
   button.clicked.connect(addrow)
   layout.addWidget(button)

   btn1 = QPushButton("del a row")
   btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
   layout.addWidget(btn1)

   dlg.setLayout(layout)
   dlg.setWindowTitle("Database Demo")
   dlg.setGeometry(200, 200,1000, 600)
   #dlg.setFixedSize(900, 600)
   dlg.setFont(QFont('fonts-wqy-microhei', 12))
   dlg.show()
   sys.exit(app.exec_())
