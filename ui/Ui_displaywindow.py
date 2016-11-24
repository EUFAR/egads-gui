# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_displayWindow(object):
    def setupUi(self, displayWindow):
        displayWindow.setObjectName(_fromUtf8("displayWindow"))
        displayWindow.resize(600, 320)
        displayWindow.setMinimumSize(QtCore.QSize(600, 320))
        displayWindow.setMaximumSize(QtCore.QSize(600, 320))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        displayWindow.setFont(font)
        self.gridLayout = QtGui.QGridLayout(displayWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.dw_label_1 = QtGui.QLabel(displayWindow)
        self.dw_label_1.setMinimumSize(QtCore.QSize(80, 27))
        self.dw_label_1.setMaximumSize(QtCore.QSize(80, 27))
        self.dw_label_1.setObjectName(_fromUtf8("dw_label_1"))
        self.horizontalLayout_2.addWidget(self.dw_label_1)
        self.dw_line_1 = QtGui.QLineEdit(displayWindow)
        self.dw_line_1.setMinimumSize(QtCore.QSize(400, 27))
        self.dw_line_1.setMaximumSize(QtCore.QSize(400, 27))
        self.dw_line_1.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
""))
        self.dw_line_1.setFrame(False)
        self.dw_line_1.setReadOnly(True)
        self.dw_line_1.setObjectName(_fromUtf8("dw_line_1"))
        self.horizontalLayout_2.addWidget(self.dw_line_1)
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.dw_label_2 = QtGui.QLabel(displayWindow)
        self.dw_label_2.setMinimumSize(QtCore.QSize(80, 27))
        self.dw_label_2.setMaximumSize(QtCore.QSize(80, 27))
        self.dw_label_2.setObjectName(_fromUtf8("dw_label_2"))
        self.horizontalLayout_3.addWidget(self.dw_label_2)
        self.dw_line_2 = QtGui.QLineEdit(displayWindow)
        self.dw_line_2.setMinimumSize(QtCore.QSize(400, 27))
        self.dw_line_2.setMaximumSize(QtCore.QSize(400, 27))
        self.dw_line_2.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
""))
        self.dw_line_2.setFrame(False)
        self.dw_line_2.setReadOnly(True)
        self.dw_line_2.setObjectName(_fromUtf8("dw_line_2"))
        self.horizontalLayout_3.addWidget(self.dw_line_2)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.dw_table = QtGui.QTableWidget(displayWindow)
        self.dw_table.setMinimumSize(QtCore.QSize(580, 170))
        self.dw_table.setMaximumSize(QtCore.QSize(580, 170))
        self.dw_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.dw_table.setGridStyle(QtCore.Qt.SolidLine)
        self.dw_table.setObjectName(_fromUtf8("dw_table"))
        self.dw_table.setColumnCount(0)
        self.dw_table.setRowCount(0)
        self.verticalLayout.addWidget(self.dw_table)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dw_okButton = QtGui.QToolButton(displayWindow)
        self.dw_okButton.setEnabled(True)
        self.dw_okButton.setMinimumSize(QtCore.QSize(100, 27))
        self.dw_okButton.setMaximumSize(QtCore.QSize(100, 27))
        self.dw_okButton.setObjectName(_fromUtf8("dw_okButton"))
        self.horizontalLayout.addWidget(self.dw_okButton)
        spacerItem4 = QtGui.QSpacerItem(398, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(displayWindow)
        QtCore.QMetaObject.connectSlotsByName(displayWindow)

    def retranslateUi(self, displayWindow):
        displayWindow.setWindowTitle(_translate("displayWindow", "Display Data", None))
        self.dw_label_1.setText(_translate("displayWindow", "Variable:", None))
        self.dw_label_2.setText(_translate("displayWindow", "Units:", None))
        self.dw_okButton.setText(_translate("displayWindow", "OK", None))

