# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListView_demo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 367)
        MainWindow.setStyleSheet("*{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QListWidget{\n"
"    color : rgb(255,255,255);\n"
"    font-size : 18px;\n"
"}\n"
"QListWidget::item:selected{\n"
"    background: rgb(239, 41, 41);\n"
"    color : black;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    width : 120px;\n"
"    height: 30px;\n"
"    border-radius : 8px; \n"
"    font-size : 18px;\n"
"}\n"
"QPushButton#btnExit{\n"
"    background-color: rgb(204, 0, 0);\n"
"    width : 120px;\n"
"    height: 30px;\n"
"    border-radius : 8px; \n"
"    font-size : 18px;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"  border: 2px solid rgb(46, 52, 54);\n"
"    color :rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"    font-size : 18px;\n"
"    color : white;\n"
"}\n"
"QLineEdit{\n"
"    font-size : 18px;\n"
"    color : white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 326))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnRemove = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout.addWidget(self.btnRemove)
        self.btnEdit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEdit.setObjectName("btnEdit")
        self.verticalLayout.addWidget(self.btnEdit)
        self.btnUp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnUp.setObjectName("btnUp")
        self.verticalLayout.addWidget(self.btnUp)
        self.btnDown = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnDown.setObjectName("btnDown")
        self.verticalLayout.addWidget(self.btnDown)
        self.btnSort = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSort.setObjectName("btnSort")
        self.verticalLayout.addWidget(self.btnSort)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btnExit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.btnExit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnRemove.setText(_translate("MainWindow", "Remove"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnUp.setText(_translate("MainWindow", "Up"))
        self.btnDown.setText(_translate("MainWindow", "Down"))
        self.btnSort.setText(_translate("MainWindow", "Sort"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.btnExit.setShortcut(_translate("MainWindow", "Ctrl+Esc"))
