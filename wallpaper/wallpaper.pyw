#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wallpaper.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import os
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(80, 260, 256, 192))
        self.listWidget.setIconSize(QtCore.QSize(300, 300))
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.listWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer_setwp)

        self.act_dir = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_dir.setIcon(icon)
        self.act_dir.setObjectName("act_dir")

        self.act_timer = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("timer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_timer.setIcon(icon1)
        self.act_timer.setObjectName("act_timer")



        self.act_exit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon2)
        self.act_exit.setObjectName("act_exit")
        self.act_exit.setEnabled(False)


        self.toolBar.addAction(self.act_dir)
        self.toolBar.addAction(self.act_timer)
        self.toolBar.addAction(self.act_exit)

        self.toolBar.actionTriggered[QtWidgets.QAction].connect(self.toolbtnpressed)

        self.listWidget.itemDoubleClicked.connect(self.setwp)
        self.mydir='/home/sb/wallpaper'

        self.showdir(self.mydir)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wallpaper"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.act_dir.setText(_translate("MainWindow", "目录"))
        self.act_dir.setToolTip(_translate("MainWindow", "选取目录"))
        self.act_timer.setText(_translate("MainWindow", "定时开始"))
        self.act_timer.setToolTip(_translate("MainWindow", "定时更换壁纸"))
        self.act_exit.setText(_translate("MainWindow", "退出定时"))
        self.act_exit.setToolTip(_translate("MainWindow", "关闭程序"))        

    def timer_setwp(self):
        max=self.listWidget.count()-1
        item=self.listWidget.item(random.randint(0,max))
        os.system('feh --bg-fill '+self.mydir+'/'+item.text())

    def setwp(self,item):
        self.statusbar.showMessage(self.mydir+'/'+item.text())
        os.system('feh --bg-fill '+self.mydir+'/'+item.text())

    def showdir(self,str):
        self.listWidget.clear()
        for file in os.listdir(str):
            icon = QtGui.QIcon(os.path.join(str, file))
            item = QtWidgets.QListWidgetItem(icon, file)
            self.listWidget.addItem(item)
        self.statusbar.showMessage('当前目录：'+self.mydir)

    def toolbtnpressed(self,a):
        if a.text()=='目录':
            seldir = QtWidgets.QFileDialog.getExistingDirectory(None, '选择图片目录')
            if seldir!='':
                self.mydir=seldir
                self.showdir(seldir)
        if a.text()=='退出定时':        
            	self.timer.stop()
            	self.act_exit.setEnabled(False)
            	self.act_timer.setEnabled(True)
        if a.text()=='定时开始':
            i, okPressed = QtWidgets.QInputDialog.getInt(None, "Please enter time","millisecond :", 1000, 1000, 600000, 1000)
            if okPressed:
                self.timer.start(i)
                self.act_exit.setEnabled(True)
                self.act_timer.setEnabled(False)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())