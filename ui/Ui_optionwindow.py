# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionWindow(object):
    def setupUi(self, optionWindow):
        optionWindow.setObjectName("optionWindow")
        optionWindow.resize(722, 234)
        optionWindow.setMinimumSize(QtCore.QSize(0, 0))
        optionWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        optionWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        optionWindow.setWindowIcon(icon)
        optionWindow.setWindowOpacity(1.0)
        optionWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(optionWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(optionWindow)
        self.label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.combobox_1 = QtWidgets.QComboBox(optionWindow)
        self.combobox_1.setMinimumSize(QtCore.QSize(100, 27))
        self.combobox_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.combobox_1.setFont(font)
        self.combobox_1.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.combobox_1.setObjectName("combobox_1")
        self.combobox_1.addItem("")
        self.combobox_1.addItem("")
        self.combobox_1.addItem("")
        self.combobox_1.addItem("")
        self.combobox_1.addItem("")
        self.horizontalLayout_7.addWidget(self.combobox_1)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.info_button_1 = QtWidgets.QToolButton(optionWindow)
        self.info_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button_1.setIcon(icon1)
        self.info_button_1.setIconSize(QtCore.QSize(23, 23))
        self.info_button_1.setAutoRaise(False)
        self.info_button_1.setObjectName("info_button_1")
        self.horizontalLayout_7.addWidget(self.info_button_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(optionWindow)
        self.label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_1 = QtWidgets.QLineEdit(optionWindow)
        self.line_1.setMinimumSize(QtCore.QSize(400, 27))
        self.line_1.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.line_1.setFont(font)
        self.line_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.line_1.setObjectName("line_1")
        self.horizontalLayout.addWidget(self.line_1)
        self.open_button_1 = QtWidgets.QToolButton(optionWindow)
        self.open_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.open_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.open_button_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_button_1.setIcon(icon2)
        self.open_button_1.setIconSize(QtCore.QSize(23, 23))
        self.open_button_1.setAutoRaise(False)
        self.open_button_1.setObjectName("open_button_1")
        self.horizontalLayout.addWidget(self.open_button_1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.info_button_2 = QtWidgets.QToolButton(optionWindow)
        self.info_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_2.setText("")
        self.info_button_2.setIcon(icon1)
        self.info_button_2.setIconSize(QtCore.QSize(23, 23))
        self.info_button_2.setAutoRaise(False)
        self.info_button_2.setObjectName("info_button_2")
        self.horizontalLayout.addWidget(self.info_button_2)
        spacerItem3 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.line = QtWidgets.QFrame(optionWindow)
        self.line.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem5 = QtWidgets.QSpacerItem(14, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkbox_1 = QtWidgets.QCheckBox(optionWindow)
        self.checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.checkbox_1.setFont(font)
        self.checkbox_1.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.checkbox_1.setObjectName("checkbox_1")
        self.horizontalLayout_6.addWidget(self.checkbox_1)
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.check_button = QtWidgets.QToolButton(optionWindow)
        self.check_button.setMinimumSize(QtCore.QSize(110, 27))
        self.check_button.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.check_button.setFont(font)
        self.check_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
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
        self.check_button.setObjectName("check_button")
        self.horizontalLayout_6.addWidget(self.check_button)
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.ow_infoButton_7 = QtWidgets.QToolButton(optionWindow)
        self.ow_infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_infoButton_7.setText("")
        self.ow_infoButton_7.setIcon(icon1)
        self.ow_infoButton_7.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_7.setAutoRaise(False)
        self.ow_infoButton_7.setObjectName("ow_infoButton_7")
        self.horizontalLayout_6.addWidget(self.ow_infoButton_7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(138, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.ok_button = QtWidgets.QToolButton(optionWindow)
        self.ok_button.setMinimumSize(QtCore.QSize(100, 27))
        self.ok_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ok_button.setFont(font)
        self.ok_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
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
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.cancel_button = QtWidgets.QToolButton(optionWindow)
        self.cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
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
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(optionWindow)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        optionWindow.setWindowTitle(_translate("optionWindow", "Options"))
        self.label_1.setText(_translate("optionWindow", "Logging level:"))
        self.combobox_1.setItemText(0, _translate("optionWindow", "DEBUG"))
        self.combobox_1.setItemText(1, _translate("optionWindow", "INFO"))
        self.combobox_1.setItemText(2, _translate("optionWindow", "WARNING"))
        self.combobox_1.setItemText(3, _translate("optionWindow", "CRITICAL"))
        self.combobox_1.setItemText(4, _translate("optionWindow", "ERROR"))
        self.label_2.setText(_translate("optionWindow", "Path of the logging file:"))
        self.checkbox_1.setText(_translate("optionWindow", "Check EGADS GUI updates on GitHub at startup"))
        self.check_button.setText(_translate("optionWindow", "Check now"))
        self.ok_button.setText(_translate("optionWindow", "Ok"))
        self.cancel_button.setText(_translate("optionWindow", "Cancel"))

