# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_displayWindow(object):
    def setupUi(self, displayWindow):
        displayWindow.setObjectName("displayWindow")
        displayWindow.resize(600, 320)
        displayWindow.setMinimumSize(QtCore.QSize(600, 320))
        displayWindow.setMaximumSize(QtCore.QSize(16777215, 600))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        displayWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/data_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        displayWindow.setWindowIcon(icon)
        displayWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(displayWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dw_label_1 = QtWidgets.QLabel(displayWindow)
        self.dw_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.dw_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_label_1.setFont(font)
        self.dw_label_1.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.dw_label_1.setObjectName("dw_label_1")
        self.gridLayout.addWidget(self.dw_label_1, 0, 0, 1, 1)
        self.dw_line_1 = QtWidgets.QLineEdit(displayWindow)
        self.dw_line_1.setEnabled(False)
        self.dw_line_1.setMinimumSize(QtCore.QSize(400, 27))
        self.dw_line_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_line_1.setFont(font)
        self.dw_line_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: black;\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.dw_line_1.setFrame(False)
        self.dw_line_1.setReadOnly(True)
        self.dw_line_1.setObjectName("dw_line_1")
        self.gridLayout.addWidget(self.dw_line_1, 0, 1, 1, 1)
        self.dw_label_2 = QtWidgets.QLabel(displayWindow)
        self.dw_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.dw_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_label_2.setFont(font)
        self.dw_label_2.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.dw_label_2.setObjectName("dw_label_2")
        self.gridLayout.addWidget(self.dw_label_2, 1, 0, 1, 1)
        self.dw_line_2 = QtWidgets.QLineEdit(displayWindow)
        self.dw_line_2.setEnabled(False)
        self.dw_line_2.setMinimumSize(QtCore.QSize(400, 27))
        self.dw_line_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_line_2.setFont(font)
        self.dw_line_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: black;\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.dw_line_2.setFrame(False)
        self.dw_line_2.setReadOnly(True)
        self.dw_line_2.setObjectName("dw_line_2")
        self.gridLayout.addWidget(self.dw_line_2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.dw_table = QtWidgets.QTableWidget(displayWindow)
        self.dw_table.setMinimumSize(QtCore.QSize(580, 170))
        self.dw_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_table.setFont(font)
        self.dw_table.setStyleSheet("background-color: rgb(240,240,240);")
        self.dw_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dw_table.setGridStyle(QtCore.Qt.SolidLine)
        self.dw_table.setObjectName("dw_table")
        self.dw_table.setColumnCount(0)
        self.dw_table.setRowCount(0)
        self.verticalLayout.addWidget(self.dw_table)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.dw_okButton = QtWidgets.QToolButton(displayWindow)
        self.dw_okButton.setEnabled(True)
        self.dw_okButton.setMinimumSize(QtCore.QSize(100, 27))
        self.dw_okButton.setMaximumSize(QtCore.QSize(100, 27))
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
        self.horizontalLayout.addWidget(self.dw_okButton)
        spacerItem3 = QtWidgets.QSpacerItem(398, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(displayWindow)
        QtCore.QMetaObject.connectSlotsByName(displayWindow)

    def retranslateUi(self, displayWindow):
        _translate = QtCore.QCoreApplication.translate
        displayWindow.setWindowTitle(_translate("displayWindow", "Display Data"))
        self.dw_label_1.setText(_translate("displayWindow", "Variable:"))
        self.dw_label_2.setText(_translate("displayWindow", "Units:"))
        self.dw_okButton.setText(_translate("displayWindow", "Ok"))

