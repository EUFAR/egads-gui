Due to the lack of right click event for the QToolButton, it is necessary to subclass QToolButtons in the Ui_mainwindow.py with a modified QToolButton. As it is not possible to subclass using QT Creator, it is necessary to do it manually.


The following line has to be added to the beginning of the file:
from functions.gui_elements import PushButtonRight

The following lines:
self.gm_button_1 = QtWidgets.QToolButton(self.tab)
self.gm_button_2 = QtWidgets.QToolButton(self.tab)
self.gm_button_3 = QtWidgets.QToolButton(self.tab)
self.gm_button_4 = QtWidgets.QToolButton(self.tab)
self.gm_button_5 = QtWidgets.QToolButton(self.tab)
self.gm_button_6 = QtWidgets.QToolButton(self.tab)
self.va_button_1 = QtWidgets.QToolButton(self.tab_2)
self.va_button_2 = QtWidgets.QToolButton(self.tab_2)
self.va_button_3 = QtWidgets.QToolButton(self.tab_2)
self.va_button_4 = QtWidgets.QToolButton(self.tab_2)
self.new_button_1 = QtWidgets.QToolButton(self.tab_3)
self.new_button_2 = QtWidgets.QToolButton(self.tab_3)
self.new_button_3 = QtWidgets.QToolButton(self.tab_3)
self.new_button_4 = QtWidgets.QToolButton(self.tab_3)

have to be replaced by:
self.gm_button_1 = PushButtonRight(self.tab)
self.gm_button_2 = PushButtonRight(self.tab)
self.gm_button_3 = PushButtonRight(self.tab)
self.gm_button_4 = PushButtonRight(self.tab)
self.gm_button_5 = PushButtonRight(self.tab)
self.gm_button_6 = PushButtonRight(self.tab)
self.va_button_1 = PushButtonRight(self.tab_2)
self.va_button_2 = PushButtonRight(self.tab_2)
self.va_button_3 = PushButtonRight(self.tab_2)
self.va_button_4 = PushButtonRight(self.tab_2)
self.new_button_1 = PushButtonRight(self.tab_3)
self.new_button_2 = PushButtonRight(self.tab_3)
self.new_button_3 = PushButtonRight(self.tab_3)
self.new_button_4 = PushButtonRight(self.tab_3)
