#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myblog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import json
import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    store_list = []
    server='http://172.96.193.223/sblog/'
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.edit_search = QtWidgets.QLineEdit(self.groupBox)
        self.edit_search.setObjectName("edit_search")

        
        self.btn_flush = QtWidgets.QPushButton(self.groupBox)
        self.btn_flush.setObjectName("btn_flush")
        self.horizontalLayout_3.addWidget(self.btn_flush)
        self.horizontalLayout_3.addWidget(self.edit_search)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_file = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_file.setObjectName("edit_file")
        self.horizontalLayout.addWidget(self.edit_file)
        self.btn_save = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #self.splitter.setStretchFactor(1, 2)
        self.listWidget.itemClicked.connect(self.titleclick)
        self.btn_clear.clicked.connect(self.btn_clead_click)
        self.btn_save.clicked.connect(self.save)
        self.btn_flush.clicked.connect(self.showall)
        self.edit_search.textChanged.connect(self.search)
        self.edit_search.setPlaceholderText('搜索')



        self.showall()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showall(self):
        self.edit_search.clear()
        r=requests.get(self.server+'getlist.php')

        json_array = r.json()
        self.store_list.clear()
        self.listWidget.clear()        

        for item in json_array:
            store_details = {'title':None, 'file':None}
            store_details['title'] = item[0]
            store_details['file'] = item[1]
            self.listWidget.addItem(item[0])
            self.store_list.append(store_details)

        self.statusbar.showMessage('找到'+str(self.listWidget.count())+'篇笔记')


    def search(self,str):
        self.store_list.clear()
        self.listWidget.clear()
        if str=='':
            self.showall()
        else:

            r=requests.get(self.server+'getsearch.php?k='+str)

            json_array = r.json()
            for item in json_array:
                    store_details = {'title':None, 'file':None}
                    store_details['title'] = item[0]
                    store_details['file'] = item[1]
                    self.listWidget.addItem(item[0])
                    self.store_list.append(store_details)

    def btn_clead_click(self):
        #self.textEdit.setMarkdown(self.textEdit.toPlainText())
        self.textEdit.clear()
        from datetime import date
        self.edit_file.setText(date.today().strftime('%Y-%m-%d-')+'.md')
        
    def save(self):
        file=str(self.edit_file.text())
        with open(self.edit_file.text(), 'w') as yourFile:
            yourFile.write(self.textEdit.toPlainText())
        files = {'file': open(file, 'rb')}
        values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
        r = requests.post(self.server+'upload.php', files=files, data=values)

        self.statusbar.showMessage(r.text+' 返回玛：'+str(r.status_code))

    def titleclick(self,item):
        file=self.store_list[self.listWidget.currentRow()]['file']
        content=requests.get(self.server+'_posts/'+file)
        content.encoding = "utf-8"
        #self.textEdit.setMarkdown(content.text)
        self.textEdit.setText(content.text)
        self.edit_file.setText(file)


    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的笔记"))
        self.groupBox.setTitle(_translate("MainWindow", "标题"))
        self.groupBox_2.setTitle(_translate("MainWindow", "内容"))
        self.btn_save.setText(_translate("MainWindow", "保存"))
        self.btn_flush.setText(_translate("MainWindow", "全部笔记"))
        self.btn_clear.setText(_translate("MainWindow", "清空"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
