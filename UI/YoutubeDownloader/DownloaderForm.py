# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloader.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(568, 469)
        Form.setStyleSheet("* {\n"
"    background-color: rgb(85, 87, 83);\n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    font: 18pt \"Ubuntu\";\n"
"    border : 2px solid rgb(211, 215, 207);\n"
"    border-radius : 15px;    \n"
"    height : 50px;\n"
"}\n"
"QPushButton{\n"
"    border-radius: 15px;\n"
"    height : 55px;\n"
"    background-color: rgb(238, 238, 236);\n"
"    color: rgb(46, 52, 54);\n"
"    font : 18pt;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    border-radius: 15px;\n"
"    height : 55px;\n"
"    background-color: rgb(204, 0, 0);\n"
"    color: rgb(238, 238, 236);\n"
"    font : 18pt;\n"
"}\n"
"QPushButton:hover:pressed{\n"
"    border-radius: 15px;\n"
"    height : 55px;\n"
"    background-color: rgb(255, 0, 0);\n"
"    border : 5px solid rgba(0,0,0,0);\n"
"    color: rgb(238, 238, 236);\n"
"    font : 18pt;\n"
"}\n"
"QListWidget{\n"
"    color: rgb(46, 52, 54);\n"
"    font : 18pt;\n"
"}\n"
"QListWidget::item:selected{\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: rgb(204, 0, 0);\n"
"    font : 18pt;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tbxUrl = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.tbxUrl.setText("")
        self.tbxUrl.setObjectName("tbxUrl")
        self.verticalLayout.addWidget(self.tbxUrl)
        self.btnSearch = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSearch.setObjectName("btnSearch")
        self.verticalLayout.addWidget(self.btnSearch)
        self.tblRes = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.tblRes.setObjectName("tblRes")
        self.verticalLayout.addWidget(self.tblRes)
        self.btnDownload = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDownload.setObjectName("btnDownload")
        self.verticalLayout.addWidget(self.btnDownload)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "YouTube Downloader"))
        self.tbxUrl.setPlaceholderText(_translate("Form", "https://www.youtube.com/"))
        self.btnSearch.setText(_translate("Form", "Search"))
        self.btnDownload.setText(_translate("Form", "Download"))
