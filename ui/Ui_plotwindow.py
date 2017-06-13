# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_window_3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName("plotWindow")
        plotWindow.resize(1105, 659)
        plotWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/plot_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        plotWindow.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(plotWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pw_toolbar_fr = QtWidgets.QVBoxLayout()
        self.pw_toolbar_fr.setObjectName("pw_toolbar_fr")
        self.verticalLayout_4.addLayout(self.pw_toolbar_fr)
        self.tabWidget = QtWidgets.QTabWidget(plotWindow)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    top: -1px;\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"    \n"
"QTabWidget::tab-bar {\n"
"    left: 0px;\n"
"}\n"
"    \n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border-top: 1px solid rgb(180,180,180);\n"
"    border-left: 1px solid rgb(180,180,180);\n"
"    border-right: 1px solid rgb(180,180,180);\n"
"    border-top-right-radius: 5px;\n"
"    border-top-left-radius: 5px;\n"
"    padding: 2px 10px 2px 10px;\n"
"    margin-right: 2px;\n"
"}\n"
"    \n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(210,210,210);\n"
"}\n"
"    \n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"    \n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pw_label_1 = QtWidgets.QLabel(self.tab)
        self.pw_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_1.setFont(font)
        self.pw_label_1.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.pw_label_1.setObjectName("pw_label_1")
        self.horizontalLayout_6.addWidget(self.pw_label_1)
        spacerItem3 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
        self.pw_single_rd = QtWidgets.QRadioButton(self.tab)
        self.pw_single_rd.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_single_rd.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_single_rd.setFont(font)
        self.pw_single_rd.setStyleSheet("QRadioButton {\n"
"    spacing: 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(icons/radiobox_icon_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(icons/radiobox_icon_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(icons/radiobox_icon_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(icons/radiobox_icon_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(icons/radiobox_icon_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    image: url(icons/radiobox_icon_checked.png);\n"
"}")
        self.pw_single_rd.setObjectName("pw_single_rd")
        self.horizontalLayout_18.addWidget(self.pw_single_rd)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem5)
        self.pw_multiple_rd = QtWidgets.QRadioButton(self.tab)
        self.pw_multiple_rd.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_multiple_rd.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_multiple_rd.setFont(font)
        self.pw_multiple_rd.setStyleSheet("QRadioButton {\n"
"    spacing: 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(icons/radiobox_icon_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(icons/radiobox_icon_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(icons/radiobox_icon_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(icons/radiobox_icon_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(icons/radiobox_icon_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    image: url(icons/radiobox_icon_checked.png);\n"
"}")
        self.pw_multiple_rd.setObjectName("pw_multiple_rd")
        self.horizontalLayout_18.addWidget(self.pw_multiple_rd)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.pw_info_bt1 = QtWidgets.QToolButton(self.tab)
        self.pw_info_bt1.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt1.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_info_bt1.setIcon(icon)
        self.pw_info_bt1.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt1.setObjectName("pw_info_bt1")
        self.horizontalLayout_18.addWidget(self.pw_info_bt1)
        spacerItem7 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.pw_graphType_sa = QtWidgets.QScrollArea(self.tab)
        self.pw_graphType_sa.setMinimumSize(QtCore.QSize(390, 0))
        self.pw_graphType_sa.setMaximumSize(QtCore.QSize(390, 16777215))
        self.pw_graphType_sa.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.pw_graphType_sa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pw_graphType_sa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pw_graphType_sa.setWidgetResizable(True)
        self.pw_graphType_sa.setObjectName("pw_graphType_sa")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 390, 435))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pw_graphType_la = QtWidgets.QVBoxLayout()
        self.pw_graphType_la.setObjectName("pw_graphType_la")
        self.gridLayout_4.addLayout(self.pw_graphType_la, 0, 0, 1, 1)
        self.pw_graphType_sa.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.pw_graphType_sa)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pw_plot_fr = QtWidgets.QVBoxLayout()
        self.pw_plot_fr.setObjectName("pw_plot_fr")
        self.horizontalLayout.addLayout(self.pw_plot_fr)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem9, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem11, 2, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pw_plotOption_fr = QtWidgets.QScrollArea(self.tab_2)
        self.pw_plotOption_fr.setMinimumSize(QtCore.QSize(480, 0))
        self.pw_plotOption_fr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pw_plotOption_fr.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.pw_plotOption_fr.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pw_plotOption_fr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pw_plotOption_fr.setWidgetResizable(True)
        self.pw_plotOption_fr.setObjectName("pw_plotOption_fr")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1019, 481))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pw_graphOptions_la = QtWidgets.QVBoxLayout()
        self.pw_graphOptions_la.setObjectName("pw_graphOptions_la")
        self.gridLayout_5.addLayout(self.pw_graphOptions_la, 0, 0, 1, 1)
        self.pw_plotOption_fr.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_2.addWidget(self.pw_plotOption_fr)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem14)
        self.pw_update_bt_1 = QtWidgets.QToolButton(self.tab_2)
        self.pw_update_bt_1.setMinimumSize(QtCore.QSize(80, 27))
        self.pw_update_bt_1.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_update_bt_1.setFont(font)
        self.pw_update_bt_1.setStyleSheet("QToolButton {\n"
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
        self.pw_update_bt_1.setObjectName("pw_update_bt_1")
        self.horizontalLayout_24.addWidget(self.pw_update_bt_1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_24)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem16, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem17, 1, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_10.addItem(spacerItem18, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem19, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pw_lineOption_fr_2 = QtWidgets.QScrollArea(self.tab_4)
        self.pw_lineOption_fr_2.setMinimumSize(QtCore.QSize(540, 0))
        self.pw_lineOption_fr_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pw_lineOption_fr_2.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.pw_lineOption_fr_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pw_lineOption_fr_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pw_lineOption_fr_2.setWidgetResizable(True)
        self.pw_lineOption_fr_2.setObjectName("pw_lineOption_fr_2")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1019, 481))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pw_plotOptions_la = QtWidgets.QVBoxLayout()
        self.pw_plotOptions_la.setObjectName("pw_plotOptions_la")
        self.gridLayout_9.addLayout(self.pw_plotOptions_la, 0, 0, 1, 1)
        self.pw_lineOption_fr_2.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_9.addWidget(self.pw_lineOption_fr_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        spacerItem20 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem20)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem21)
        self.pw_update_bt_2 = QtWidgets.QToolButton(self.tab_4)
        self.pw_update_bt_2.setMinimumSize(QtCore.QSize(80, 27))
        self.pw_update_bt_2.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_update_bt_2.setFont(font)
        self.pw_update_bt_2.setStyleSheet("QToolButton {\n"
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
        self.pw_update_bt_2.setObjectName("pw_update_bt_2")
        self.horizontalLayout_25.addWidget(self.pw_update_bt_2)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem22)
        self.verticalLayout_5.addLayout(self.horizontalLayout_25)
        self.gridLayout_10.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_10.addItem(spacerItem23, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pw_saveOptions_lb_1 = QtWidgets.QLabel(self.tab_3)
        self.pw_saveOptions_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_1.setFont(font)
        self.pw_saveOptions_lb_1.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.pw_saveOptions_lb_1.setObjectName("pw_saveOptions_lb_1")
        self.horizontalLayout_3.addWidget(self.pw_saveOptions_lb_1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem24)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem25)
        self.pw_saveOptions_lb_2 = QtWidgets.QLabel(self.tab_3)
        self.pw_saveOptions_lb_2.setMinimumSize(QtCore.QSize(60, 27))
        self.pw_saveOptions_lb_2.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_2.setFont(font)
        self.pw_saveOptions_lb_2.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.pw_saveOptions_lb_2.setObjectName("pw_saveOptions_lb_2")
        self.horizontalLayout_4.addWidget(self.pw_saveOptions_lb_2)
        self.pw_saveOptions_ln_1 = QtWidgets.QLineEdit(self.tab_3)
        self.pw_saveOptions_ln_1.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ln_1.setFont(font)
        self.pw_saveOptions_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.pw_saveOptions_ln_1.setObjectName("pw_saveOptions_ln_1")
        self.horizontalLayout_4.addWidget(self.pw_saveOptions_ln_1)
        self.pw_saveOptions_cb_1 = QtWidgets.QComboBox(self.tab_3)
        self.pw_saveOptions_cb_1.setMinimumSize(QtCore.QSize(130, 27))
        self.pw_saveOptions_cb_1.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_cb_1.setFont(font)
        self.pw_saveOptions_cb_1.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: black;\n"
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
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
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
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: transparent;\n"
"    selection-color: blue;\n"
"    border: 0px, solid black;\n"
"}")
        self.pw_saveOptions_cb_1.setObjectName("pw_saveOptions_cb_1")
        self.pw_saveOptions_cb_1.addItem("")
        self.pw_saveOptions_cb_1.addItem("")
        self.horizontalLayout_4.addWidget(self.pw_saveOptions_cb_1)
        self.pw_info_bt2 = QtWidgets.QToolButton(self.tab_3)
        self.pw_info_bt2.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt2.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_info_bt2.setIcon(icon)
        self.pw_info_bt2.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt2.setObjectName("pw_info_bt2")
        self.horizontalLayout_4.addWidget(self.pw_info_bt2)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem26)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem27)
        self.pw_saveOptions_lb_3 = QtWidgets.QLabel(self.tab_3)
        self.pw_saveOptions_lb_3.setMinimumSize(QtCore.QSize(60, 27))
        self.pw_saveOptions_lb_3.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_3.setFont(font)
        self.pw_saveOptions_lb_3.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.pw_saveOptions_lb_3.setObjectName("pw_saveOptions_lb_3")
        self.horizontalLayout_5.addWidget(self.pw_saveOptions_lb_3)
        self.pw_saveOptions_ln_2 = QtWidgets.QLineEdit(self.tab_3)
        self.pw_saveOptions_ln_2.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_2.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ln_2.setFont(font)
        self.pw_saveOptions_ln_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.pw_saveOptions_ln_2.setObjectName("pw_saveOptions_ln_2")
        self.horizontalLayout_5.addWidget(self.pw_saveOptions_ln_2)
        self.pw_saveOptions_cb_2 = QtWidgets.QComboBox(self.tab_3)
        self.pw_saveOptions_cb_2.setMinimumSize(QtCore.QSize(130, 27))
        self.pw_saveOptions_cb_2.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_cb_2.setFont(font)
        self.pw_saveOptions_cb_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: black;\n"
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
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
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
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: transparent;\n"
"    selection-color: blue;\n"
"    border: 0px, solid black;\n"
"}")
        self.pw_saveOptions_cb_2.setObjectName("pw_saveOptions_cb_2")
        self.pw_saveOptions_cb_2.addItem("")
        self.pw_saveOptions_cb_2.addItem("")
        self.horizontalLayout_5.addWidget(self.pw_saveOptions_cb_2)
        self.pw_info_bt3 = QtWidgets.QToolButton(self.tab_3)
        self.pw_info_bt3.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt3.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_info_bt3.setIcon(icon)
        self.pw_info_bt3.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt3.setObjectName("pw_info_bt3")
        self.horizontalLayout_5.addWidget(self.pw_info_bt3)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem28)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem29)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pw_saveOptions_lb_4 = QtWidgets.QLabel(self.tab_3)
        self.pw_saveOptions_lb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_4.setFont(font)
        self.pw_saveOptions_lb_4.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.pw_saveOptions_lb_4.setObjectName("pw_saveOptions_lb_4")
        self.horizontalLayout_7.addWidget(self.pw_saveOptions_lb_4)
        self.pw_saveOptions_ln_3 = QtWidgets.QLineEdit(self.tab_3)
        self.pw_saveOptions_ln_3.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_3.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ln_3.setFont(font)
        self.pw_saveOptions_ln_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.pw_saveOptions_ln_3.setObjectName("pw_saveOptions_ln_3")
        self.horizontalLayout_7.addWidget(self.pw_saveOptions_ln_3)
        self.pw_info_bt4 = QtWidgets.QToolButton(self.tab_3)
        self.pw_info_bt4.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt4.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_info_bt4.setIcon(icon)
        self.pw_info_bt4.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt4.setObjectName("pw_info_bt4")
        self.horizontalLayout_7.addWidget(self.pw_info_bt4)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem30)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem31 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem31)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pw_saveOptions_lb_5 = QtWidgets.QLabel(self.tab_3)
        self.pw_saveOptions_lb_5.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_5.setFont(font)
        self.pw_saveOptions_lb_5.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.pw_saveOptions_lb_5.setObjectName("pw_saveOptions_lb_5")
        self.horizontalLayout_8.addWidget(self.pw_saveOptions_lb_5)
        self.pw_saveOptions_ck_1 = QtWidgets.QCheckBox(self.tab_3)
        self.pw_saveOptions_ck_1.setMinimumSize(QtCore.QSize(25, 20))
        self.pw_saveOptions_ck_1.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ck_1.setFont(font)
        self.pw_saveOptions_ck_1.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(icons/checkbox_icon_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(icons/checkbox_icon_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(icons/checkbox_icon_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(icons/checkbox_icon_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(icons/checkbox_icon_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    image: url(icons/checkbox_icon_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:hover {\n"
"    image: url(icons/checkbox_icon_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:pressed {\n"
"    image: url(icons/checkbox_icon_checked.png);\n"
"}")
        self.pw_saveOptions_ck_1.setText("")
        self.pw_saveOptions_ck_1.setObjectName("pw_saveOptions_ck_1")
        self.horizontalLayout_8.addWidget(self.pw_saveOptions_ck_1)
        self.pw_info_bt5 = QtWidgets.QToolButton(self.tab_3)
        self.pw_info_bt5.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt5.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_info_bt5.setIcon(icon)
        self.pw_info_bt5.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt5.setObjectName("pw_info_bt5")
        self.horizontalLayout_8.addWidget(self.pw_info_bt5)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem32)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem33)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem34, 1, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem35, 1, 2, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem36, 0, 1, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem37, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(plotWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        _translate = QtCore.QCoreApplication.translate
        plotWindow.setWindowTitle(_translate("plotWindow", "Data Plot"))
        self.pw_label_1.setText(_translate("plotWindow", "Please choose the type of graphs"))
        self.pw_single_rd.setText(_translate("plotWindow", "Single plot"))
        self.pw_multiple_rd.setText(_translate("plotWindow", "Multiple plots"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("plotWindow", "Plot window"))
        self.pw_update_bt_1.setText(_translate("plotWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("plotWindow", "Figure options"))
        self.pw_update_bt_2.setText(_translate("plotWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("plotWindow", "Plot options"))
        self.pw_saveOptions_lb_1.setText(_translate("plotWindow", "Figure dimensions:"))
        self.pw_saveOptions_lb_2.setText(_translate("plotWindow", "height:"))
        self.pw_saveOptions_cb_1.setItemText(0, _translate("plotWindow", "Centimeters"))
        self.pw_saveOptions_cb_1.setItemText(1, _translate("plotWindow", "Inches"))
        self.pw_saveOptions_lb_3.setText(_translate("plotWindow", "width:"))
        self.pw_saveOptions_cb_2.setItemText(0, _translate("plotWindow", "Centimeters"))
        self.pw_saveOptions_cb_2.setItemText(1, _translate("plotWindow", "Inches"))
        self.pw_saveOptions_lb_4.setText(_translate("plotWindow", "Figure resolution:"))
        self.pw_saveOptions_lb_5.setText(_translate("plotWindow", "Transparent background ?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("plotWindow", "Save options"))

