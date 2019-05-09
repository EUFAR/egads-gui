from PyQt5 import QtCore, QtWidgets, QtGui


class PushButtonRight (QtWidgets.QToolButton):
    rightClick = QtCore.pyqtSignal()

    def __init__(self, string):
        QtWidgets.QToolButton.__init__(self, string)

    def mousePressEvent(self, event):
        QtWidgets.QToolButton.mousePressEvent(self, event)
        if event.button() == QtCore.Qt.RightButton:
            self.rightClick.emit()


class ListWidgetRight (QtWidgets.QListWidget):
    rightClick = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QListWidget.__init__(self, parent=None)

    def mousePressEvent(self, event):
        QtWidgets.QListWidget.mousePressEvent(self, event)
        if event.button() == QtCore.Qt.RightButton:
            self.rightClick.emit()


class VerticalLabel(QtWidgets.QLabel):

    def __init__(self, *args):
        QtWidgets.QLabel.__init__(self, *args)

    def paintEvent(self, event):
        QtWidgets.QLabel.paintEvent(self, event)
        painter = QtGui.QPainter(self)
        painter.translate(0, self.height()-1)
        painter.rotate(-90)
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        QtWidgets.QLabel.render(self, painter)
        painter.end()

    def minimumSizeHint(self):
        size = QtWidgets.QLabel.minimumSizeHint(self)
        return QtCore.QSize(size.height(), size.width())

    def sizeHint(self):
        size = QtWidgets.QLabel.sizeHint(self)
        return QtCore.QSize(size.height(), size.width())
