# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Changelog(object):
    def setupUi(self, Changelog):
        Changelog.setObjectName("Changelog")
        Changelog.resize(600, 450)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Changelog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/changelog_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Changelog.setWindowIcon(icon)
        Changelog.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Changelog)
        self.gridLayout.setObjectName("gridLayout")
        self.log_txBrower = QtWidgets.QTextBrowser(Changelog)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.log_txBrower.setFont(font)
        self.log_txBrower.setStyleSheet("QTextBrowser {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background: white;\n"
"    color: black;\n"
"}")
        self.log_txBrower.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log_txBrower.setObjectName("log_txBrower")
        self.gridLayout.addWidget(self.log_txBrower, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lg_okButton = QtWidgets.QToolButton(Changelog)
        self.lg_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.lg_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lg_okButton.setFont(font)
        self.lg_okButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: black;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
"}")
        self.lg_okButton.setObjectName("lg_okButton")
        self.horizontalLayout.addWidget(self.lg_okButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Changelog)
        QtCore.QMetaObject.connectSlotsByName(Changelog)

    def retranslateUi(self, Changelog):
        _translate = QtCore.QCoreApplication.translate
        Changelog.setWindowTitle(_translate("Changelog", "Changelog"))
        self.log_txBrower.setDocumentTitle(_translate("Changelog", "Changelog"))
        self.lg_okButton.setText(_translate("Changelog", "Ok"))

