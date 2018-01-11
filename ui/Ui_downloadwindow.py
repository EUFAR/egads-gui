# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadupdatewindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_downloadWindow(object):
    def setupUi(self, downloadWindow):
        downloadWindow.setObjectName("downloadWindow")
        downloadWindow.resize(500, 230)
        downloadWindow.setMinimumSize(QtCore.QSize(500, 230))
        downloadWindow.setMaximumSize(QtCore.QSize(500, 230))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        downloadWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        downloadWindow.setWindowIcon(icon)
        downloadWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.widget = QtWidgets.QWidget(downloadWindow)
        self.widget.setGeometry(QtCore.QRect(11, 11, 478, 208))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dw_label_2 = QtWidgets.QLabel(self.widget)
        self.dw_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.dw_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.dw_label_2.setText("")
        self.dw_label_2.setPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"))
        self.dw_label_2.setScaledContents(True)
        self.dw_label_2.setObjectName("dw_label_2")
        self.verticalLayout.addWidget(self.dw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dw_label_1 = QtWidgets.QLabel(self.widget)
        self.dw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.dw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_label_1.setFont(font)
        self.dw_label_1.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.dw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dw_label_1.setLineWidth(0)
        self.dw_label_1.setMidLineWidth(0)
        self.dw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.dw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.dw_label_1.setWordWrap(True)
        self.dw_label_1.setObjectName("dw_label_1")
        self.verticalLayout_2.addWidget(self.dw_label_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.dw_downloadButton = QtWidgets.QToolButton(self.widget)
        self.dw_downloadButton.setMinimumSize(QtCore.QSize(160, 27))
        self.dw_downloadButton.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_downloadButton.setFont(font)
        self.dw_downloadButton.setStyleSheet("QToolButton {\n"
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
        self.dw_downloadButton.setObjectName("dw_downloadButton")
        self.horizontalLayout.addWidget(self.dw_downloadButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.dw_downloadButton_2 = QtWidgets.QToolButton(self.widget)
        self.dw_downloadButton_2.setMinimumSize(QtCore.QSize(140, 27))
        self.dw_downloadButton_2.setMaximumSize(QtCore.QSize(140, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_downloadButton_2.setFont(font)
        self.dw_downloadButton_2.setStyleSheet("QToolButton {\n"
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
        self.dw_downloadButton_2.setObjectName("dw_downloadButton_2")
        self.horizontalLayout.addWidget(self.dw_downloadButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.dw_okButton = QtWidgets.QToolButton(self.widget)
        self.dw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.dw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_okButton.setFont(font)
        self.dw_okButton.setStyleSheet("QToolButton {\n"
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
        self.dw_okButton.setObjectName("dw_okButton")
        self.horizontalLayout_2.addWidget(self.dw_okButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(downloadWindow)
        QtCore.QMetaObject.connectSlotsByName(downloadWindow)

    def retranslateUi(self, downloadWindow):
        _translate = QtCore.QCoreApplication.translate
        downloadWindow.setWindowTitle(_translate("downloadWindow", "Information"))
        self.dw_label_1.setText(_translate("downloadWindow", "<html><head/><body><p>A new version of the EGADS GUI is available on GitHub. Click on <span style=\" font-weight:600;\">Download update</span> to download it, or click on <span style=\" font-weight:600;\">Visit GitHub</span> to have a look at the EGADS GUI repository on GitHub.</p></body></html>"))
        self.dw_downloadButton.setText(_translate("downloadWindow", "Download update"))
        self.dw_downloadButton_2.setText(_translate("downloadWindow", "Visit GitHub"))
        self.dw_okButton.setText(_translate("downloadWindow", "Ok"))

