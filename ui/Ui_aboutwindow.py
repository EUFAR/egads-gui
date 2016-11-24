# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutwindow.ui'
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

class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName(_fromUtf8("aboutWindow"))
        aboutWindow.resize(452, 220)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutWindow.sizePolicy().hasHeightForWidth())
        aboutWindow.setSizePolicy(sizePolicy)
        aboutWindow.setMinimumSize(QtCore.QSize(450, 220))
        aboutWindow.setMaximumSize(QtCore.QSize(452, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/SourceSansPro-Regular.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        aboutWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/about_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutWindow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(aboutWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.aw_label_2 = QtGui.QLabel(aboutWindow)
        self.aw_label_2.setMinimumSize(QtCore.QSize(55, 55))
        self.aw_label_2.setMaximumSize(QtCore.QSize(55, 55))
        self.aw_label_2.setText(_fromUtf8(""))
        self.aw_label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/about_icon.png")))
        self.aw_label_2.setScaledContents(True)
        self.aw_label_2.setObjectName(_fromUtf8("aw_label_2"))
        self.verticalLayout.addWidget(self.aw_label_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.aw_label_1 = QtGui.QLabel(aboutWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aw_label_1.sizePolicy().hasHeightForWidth())
        self.aw_label_1.setSizePolicy(sizePolicy)
        self.aw_label_1.setMinimumSize(QtCore.QSize(341, 170))
        self.aw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/SourceSansPro-Regular.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_1.setFont(font)
        self.aw_label_1.setFrameShape(QtGui.QFrame.NoFrame)
        self.aw_label_1.setFrameShadow(QtGui.QFrame.Plain)
        self.aw_label_1.setLineWidth(1)
        self.aw_label_1.setMidLineWidth(0)
        self.aw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.aw_label_1.setScaledContents(False)
        self.aw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aw_label_1.setWordWrap(True)
        self.aw_label_1.setObjectName(_fromUtf8("aw_label_1"))
        self.horizontalLayout.addWidget(self.aw_label_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.aw_okButton = QtGui.QPushButton(aboutWindow)
        self.aw_okButton.setMinimumSize(QtCore.QSize(50, 27))
        self.aw_okButton.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/SourceSansPro-Regular.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.aw_okButton.setFont(font)
        self.aw_okButton.setObjectName(_fromUtf8("aw_okButton"))
        self.horizontalLayout_2.addWidget(self.aw_okButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        aboutWindow.setWindowTitle(_translate("aboutWindow", "About EGADS", None))
        self.aw_label_1.setText(_translate("aboutWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.aw_okButton.setText(_translate("aboutWindow", "OK", None))

