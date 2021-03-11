# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 350)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("*{\n"
"background-color :rgb(85, 87, 83);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color : rgb(238, 238, 236);\n"
"    background-color : rgb(136, 138, 133);\n"
"}\n"
"\n"
"QPushButton{\n"
"    color : rgb(238, 238, 236);\n"
"    background-color : rgb(136, 138, 133);\n"
"}\n"
"\n"
"QTableWidget{\n"
"    color : rgb(238, 238, 236);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 1, 621, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblProducts = QtWidgets.QTableWidget(self.layoutWidget)
        self.tblProducts.setAutoFillBackground(False)
        self.tblProducts.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.tblProducts.setObjectName("tblProducts")
        self.tblProducts.setColumnCount(0)
        self.tblProducts.setRowCount(0)
        self.horizontalLayout.addWidget(self.tblProducts)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tbxName = QtWidgets.QLineEdit(self.layoutWidget)
        self.tbxName.setStyleSheet("")
        self.tbxName.setObjectName("tbxName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tbxName)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tbxPrice = QtWidgets.QLineEdit(self.layoutWidget)
        self.tbxPrice.setStyleSheet("")
        self.tbxPrice.setObjectName("tbxPrice")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tbxPrice)
        self.verticalLayout.addLayout(self.formLayout)
        self.btnSave = QtWidgets.QPushButton(self.layoutWidget)
        self.btnSave.setStyleSheet("")
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout.addWidget(self.btnSave)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnSave.setShortcut(_translate("MainWindow", "Ctrl+Return"))
