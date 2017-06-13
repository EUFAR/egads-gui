# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'presavewindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_presaveWindow(object):
    def setupUi(self, presaveWindow):
        presaveWindow.setObjectName("presaveWindow")
        presaveWindow.resize(470, 215)
        presaveWindow.setMinimumSize(QtCore.QSize(470, 180))
        presaveWindow.setMaximumSize(QtCore.QSize(470, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        presaveWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        presaveWindow.setWindowIcon(icon)
        presaveWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(presaveWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.iw_label_2 = QtWidgets.QLabel(presaveWindow)
        self.iw_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.iw_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.iw_label_2.setText("")
        self.iw_label_2.setPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"))
        self.iw_label_2.setScaledContents(True)
        self.iw_label_2.setObjectName("iw_label_2")
        self.verticalLayout.addWidget(self.iw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.iw_label_1 = QtWidgets.QLabel(presaveWindow)
        self.iw_label_1.setMinimumSize(QtCore.QSize(341, 120))
        self.iw_label_1.setMaximumSize(QtCore.QSize(341, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.iw_label_1.setFont(font)
        self.iw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.iw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.iw_label_1.setLineWidth(0)
        self.iw_label_1.setMidLineWidth(0)
        self.iw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.iw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.iw_label_1.setWordWrap(True)
        self.iw_label_1.setObjectName("iw_label_1")
        self.horizontalLayout.addWidget(self.iw_label_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iw_nosaveButton = QtWidgets.QToolButton(presaveWindow)
        self.iw_nosaveButton.setMinimumSize(QtCore.QSize(160, 27))
        self.iw_nosaveButton.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.iw_nosaveButton.setFont(font)
        self.iw_nosaveButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.iw_nosaveButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.iw_nosaveButton.setObjectName("iw_nosaveButton")
        self.horizontalLayout_2.addWidget(self.iw_nosaveButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.iw_cancelButton = QtWidgets.QToolButton(presaveWindow)
        self.iw_cancelButton.setMinimumSize(QtCore.QSize(93, 27))
        self.iw_cancelButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.iw_cancelButton.setFont(font)
        self.iw_cancelButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.iw_cancelButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.iw_cancelButton.setObjectName("iw_cancelButton")
        self.horizontalLayout_2.addWidget(self.iw_cancelButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.iw_saveButton = QtWidgets.QToolButton(presaveWindow)
        self.iw_saveButton.setMinimumSize(QtCore.QSize(93, 27))
        self.iw_saveButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.iw_saveButton.setFont(font)
        self.iw_saveButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.iw_saveButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.iw_saveButton.setObjectName("iw_saveButton")
        self.horizontalLayout_2.addWidget(self.iw_saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(presaveWindow)
        QtCore.QMetaObject.connectSlotsByName(presaveWindow)

    def retranslateUi(self, presaveWindow):
        _translate = QtCore.QCoreApplication.translate
        presaveWindow.setWindowTitle(_translate("presaveWindow", "Close a file"))
        self.iw_label_1.setText(_translate("presaveWindow", "<html><head/><body><p align=\"justify\">The opened file has been modified. Changes will be lost if the file is not saved.<br/></p><p><span style=\" font-weight:600;\">Do you want to save your modifications ?</span></p></body></html>"))
        self.iw_nosaveButton.setText(_translate("presaveWindow", "Close without saving"))
        self.iw_cancelButton.setText(_translate("presaveWindow", "Cancel"))
        self.iw_saveButton.setText(_translate("presaveWindow", "Save"))

