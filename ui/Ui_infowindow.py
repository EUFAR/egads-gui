# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infowindow.ui'
#
# Created: Fri Feb 13 13:26:29 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_infoWindow(object):
    def setupUi(self, infoWindow):
        infoWindow.setObjectName(_fromUtf8("infoWindow"))
        infoWindow.resize(450, 50)
        infoWindow.setMinimumSize(QtCore.QSize(450, 50))
        infoWindow.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        infoWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infoWindow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(infoWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.iw_label_2 = QtGui.QLabel(infoWindow)
        self.iw_label_2.setMinimumSize(QtCore.QSize(55, 55))
        self.iw_label_2.setMaximumSize(QtCore.QSize(55, 55))
        self.iw_label_2.setText(_fromUtf8(""))
        self.iw_label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")))
        self.iw_label_2.setScaledContents(True)
        self.iw_label_2.setObjectName(_fromUtf8("iw_label_2"))
        self.verticalLayout.addWidget(self.iw_label_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.iw_label_1 = QtGui.QLabel(infoWindow)
        self.iw_label_1.setMinimumSize(QtCore.QSize(341, 27))
        self.iw_label_1.setMaximumSize(QtCore.QSize(341, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.iw_label_1.setFont(font)
        self.iw_label_1.setFrameShape(QtGui.QFrame.NoFrame)
        self.iw_label_1.setFrameShadow(QtGui.QFrame.Plain)
        self.iw_label_1.setLineWidth(0)
        self.iw_label_1.setMidLineWidth(0)
        self.iw_label_1.setText(_fromUtf8(""))
        self.iw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.iw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.iw_label_1.setWordWrap(True)
        self.iw_label_1.setObjectName(_fromUtf8("iw_label_1"))
        self.horizontalLayout.addWidget(self.iw_label_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.iw_okButton = QtGui.QPushButton(infoWindow)
        self.iw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.iw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.iw_okButton.setFont(font)
        self.iw_okButton.setObjectName(_fromUtf8("iw_okButton"))
        self.horizontalLayout_2.addWidget(self.iw_okButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(infoWindow)
        QtCore.QMetaObject.connectSlotsByName(infoWindow)

    def retranslateUi(self, infoWindow):
        infoWindow.setWindowTitle(_translate("infoWindow", "Information", None))
        self.iw_okButton.setText(_translate("infoWindow", "OK", None))

