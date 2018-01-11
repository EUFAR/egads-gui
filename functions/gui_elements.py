# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class PushButtonRight (QtWidgets.QToolButton):
    rightClick = QtCore.pyqtSignal()

    def __init__ (self, string):
        QtWidgets.QToolButton.__init__(self, string)

    def mousePressEvent (self, event):
        QtWidgets.QToolButton.mousePressEvent(self, event)
        if event.button() == QtCore.Qt.RightButton :
            self.rightClick.emit()
