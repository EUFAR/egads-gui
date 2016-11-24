# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logwindow.ui'
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

class Ui_Changelog(object):
    def setupUi(self, Changelog):
        Changelog.setObjectName(_fromUtf8("Changelog"))
        Changelog.resize(600, 450)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/SourceSansPro-Regular.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Changelog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/changelog_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Changelog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Changelog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.log_txBrower = QtGui.QTextBrowser(Changelog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/SourceSansPro-Regular.ttf"))
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.log_txBrower.setFont(font)
        self.log_txBrower.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log_txBrower.setObjectName(_fromUtf8("log_txBrower"))
        self.gridLayout.addWidget(self.log_txBrower, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lg_okButton = QtGui.QPushButton(Changelog)
        self.lg_okButton.setMinimumSize(QtCore.QSize(50, 27))
        self.lg_okButton.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/SourceSansPro-Regular.ttf"))
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lg_okButton.setFont(font)
        self.lg_okButton.setObjectName(_fromUtf8("lg_okButton"))
        self.horizontalLayout.addWidget(self.lg_okButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Changelog)
        QtCore.QMetaObject.connectSlotsByName(Changelog)

    def retranslateUi(self, Changelog):
        Changelog.setWindowTitle(_translate("Changelog", "Changelog", None))
        self.log_txBrower.setDocumentTitle(_translate("Changelog", "Changelog", None))
        self.lg_okButton.setText(_translate("Changelog", "Ok", None))

