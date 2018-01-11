# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'algorithm_creation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_creationWindow(object):
    def setupUi(self, creationWindow):
        creationWindow.setObjectName("creationWindow")
        creationWindow.resize(1000, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(creationWindow.sizePolicy().hasHeightForWidth())
        creationWindow.setSizePolicy(sizePolicy)
        creationWindow.setMinimumSize(QtCore.QSize(1000, 700))
        creationWindow.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        creationWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/create_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        creationWindow.setWindowIcon(icon)
        creationWindow.setStyleSheet("")
        self.gridLayout_11 = QtWidgets.QGridLayout(creationWindow)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(creationWindow)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
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
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; \n"
"}\n"
"\n"
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
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(210,210,210);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px; \n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    background-color: rgb(240,240,240);\n"
"}\n"
"\n"
"QTabBar QToolButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(icons/right_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(icons/left_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cw_label_1 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_1.setFont(font)
        self.cw_label_1.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_1.setObjectName("cw_label_1")
        self.horizontalLayout_2.addWidget(self.cw_label_1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cw_add_1 = QtWidgets.QToolButton(self.tab_1)
        self.cw_add_1.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_add_1.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_add_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/plus_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_add_1.setIcon(icon1)
        self.cw_add_1.setIconSize(QtCore.QSize(23, 23))
        self.cw_add_1.setObjectName("cw_add_1")
        self.horizontalLayout_2.addWidget(self.cw_add_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cw_info_1 = QtWidgets.QToolButton(self.tab_1)
        self.cw_info_1.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_1.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_info_1.setIcon(icon2)
        self.cw_info_1.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_1.setObjectName("cw_info_1")
        self.horizontalLayout_2.addWidget(self.cw_info_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.cw_scrollarea_1 = QtWidgets.QScrollArea(self.tab_1)
        self.cw_scrollarea_1.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.cw_scrollarea_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cw_scrollarea_1.setWidgetResizable(True)
        self.cw_scrollarea_1.setObjectName("cw_scrollarea_1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 916, 494))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cw_input_vl = QtWidgets.QVBoxLayout()
        self.cw_input_vl.setObjectName("cw_input_vl")
        self.gridLayout_7.addLayout(self.cw_input_vl, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 1, 0, 1, 1)
        self.cw_scrollarea_1.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.cw_scrollarea_1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem8, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cw_label_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_2.setFont(font)
        self.cw_label_2.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_2.setObjectName("cw_label_2")
        self.horizontalLayout_3.addWidget(self.cw_label_2)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.cw_add_2 = QtWidgets.QToolButton(self.tab_2)
        self.cw_add_2.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_add_2.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_add_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_add_2.setIcon(icon1)
        self.cw_add_2.setIconSize(QtCore.QSize(23, 23))
        self.cw_add_2.setObjectName("cw_add_2")
        self.horizontalLayout_3.addWidget(self.cw_add_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.cw_info_2 = QtWidgets.QToolButton(self.tab_2)
        self.cw_info_2.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_2.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_2.setIcon(icon2)
        self.cw_info_2.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_2.setObjectName("cw_info_2")
        self.horizontalLayout_3.addWidget(self.cw_info_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem13)
        self.cw_scrollarea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.cw_scrollarea_2.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.cw_scrollarea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cw_scrollarea_2.setWidgetResizable(True)
        self.cw_scrollarea_2.setObjectName("cw_scrollarea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 916, 494))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cw_output_vl = QtWidgets.QVBoxLayout()
        self.cw_output_vl.setObjectName("cw_output_vl")
        self.gridLayout_6.addLayout(self.cw_output_vl, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem14, 1, 0, 1, 1)
        self.cw_scrollarea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.cw_scrollarea_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem16 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem16, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem17, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cw_label_3 = QtWidgets.QLabel(self.tab_3)
        self.cw_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_3.setFont(font)
        self.cw_label_3.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}QLabel:{\n"
"    color: black;\n"
"}")
        self.cw_label_3.setObjectName("cw_label_3")
        self.gridLayout_3.addWidget(self.cw_label_3, 0, 0, 1, 1)
        self.cw_line_1 = QtWidgets.QLineEdit(self.tab_3)
        self.cw_line_1.setEnabled(True)
        self.cw_line_1.setMinimumSize(QtCore.QSize(150, 27))
        self.cw_line_1.setMaximumSize(QtCore.QSize(150, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cw_line_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_line_1.setFont(font)
        self.cw_line_1.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
"\n"
"QLineEdit:disabled {background-color: rgb(200,200,200);}")
        self.cw_line_1.setText("")
        self.cw_line_1.setFrame(False)
        self.cw_line_1.setObjectName("cw_line_1")
        self.gridLayout_3.addWidget(self.cw_line_1, 0, 1, 1, 1)
        self.cw_info_3 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_3.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_3.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_3.setIcon(icon2)
        self.cw_info_3.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_3.setObjectName("cw_info_3")
        self.gridLayout_3.addWidget(self.cw_info_3, 0, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem18, 0, 3, 1, 1)
        self.cw_label_5 = QtWidgets.QLabel(self.tab_3)
        self.cw_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_5.setFont(font)
        self.cw_label_5.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_5.setObjectName("cw_label_5")
        self.gridLayout_3.addWidget(self.cw_label_5, 0, 4, 1, 1)
        self.cw_line_3 = QtWidgets.QLineEdit(self.tab_3)
        self.cw_line_3.setEnabled(True)
        self.cw_line_3.setMinimumSize(QtCore.QSize(150, 27))
        self.cw_line_3.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cw_line_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_line_3.setFont(font)
        self.cw_line_3.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
"\n"
"QLineEdit:disabled {background-color: rgb(200,200,200);}")
        self.cw_line_3.setText("")
        self.cw_line_3.setFrame(False)
        self.cw_line_3.setObjectName("cw_line_3")
        self.gridLayout_3.addWidget(self.cw_line_3, 0, 5, 1, 1)
        self.cw_info_5 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_5.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_5.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_5.setIcon(icon2)
        self.cw_info_5.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_5.setObjectName("cw_info_5")
        self.gridLayout_3.addWidget(self.cw_info_5, 0, 6, 1, 1)
        self.cw_label_4 = QtWidgets.QLabel(self.tab_3)
        self.cw_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_4.setFont(font)
        self.cw_label_4.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_4.setObjectName("cw_label_4")
        self.gridLayout_3.addWidget(self.cw_label_4, 1, 0, 1, 1)
        self.cw_line_2 = QtWidgets.QLineEdit(self.tab_3)
        self.cw_line_2.setEnabled(True)
        self.cw_line_2.setMinimumSize(QtCore.QSize(150, 27))
        self.cw_line_2.setMaximumSize(QtCore.QSize(150, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cw_line_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_line_2.setFont(font)
        self.cw_line_2.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
"\n"
"QLineEdit:disabled {background-color: rgb(200,200,200);}")
        self.cw_line_2.setText("")
        self.cw_line_2.setFrame(False)
        self.cw_line_2.setObjectName("cw_line_2")
        self.gridLayout_3.addWidget(self.cw_line_2, 1, 1, 1, 1)
        self.cw_info_4 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_4.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_4.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_4.setIcon(icon2)
        self.cw_info_4.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_4.setObjectName("cw_info_4")
        self.gridLayout_3.addWidget(self.cw_info_4, 1, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 1, 3, 1, 1)
        self.cw_label_6 = QtWidgets.QLabel(self.tab_3)
        self.cw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_6.setFont(font)
        self.cw_label_6.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_6.setObjectName("cw_label_6")
        self.gridLayout_3.addWidget(self.cw_label_6, 1, 4, 1, 1)
        self.cw_line_4 = QtWidgets.QLineEdit(self.tab_3)
        self.cw_line_4.setEnabled(True)
        self.cw_line_4.setMinimumSize(QtCore.QSize(150, 27))
        self.cw_line_4.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cw_line_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_line_4.setFont(font)
        self.cw_line_4.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
"\n"
"QLineEdit:disabled {background-color: rgb(200,200,200);}")
        self.cw_line_4.setText("")
        self.cw_line_4.setFrame(False)
        self.cw_line_4.setObjectName("cw_line_4")
        self.gridLayout_3.addWidget(self.cw_line_4, 1, 5, 1, 1)
        self.cw_info_6 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_6.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_6.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_6.setIcon(icon2)
        self.cw_info_6.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_6.setObjectName("cw_info_6")
        self.gridLayout_3.addWidget(self.cw_info_6, 1, 6, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cw_info_7 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_7.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_7.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_7.setIcon(icon2)
        self.cw_info_7.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_7.setObjectName("cw_info_7")
        self.gridLayout_4.addWidget(self.cw_info_7, 0, 2, 1, 1)
        self.cw_plain_2 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.cw_plain_2.setEnabled(True)
        self.cw_plain_2.setMinimumSize(QtCore.QSize(400, 50))
        self.cw_plain_2.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cw_plain_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_plain_2.setFont(font)
        self.cw_plain_2.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QPlainTextEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.cw_plain_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cw_plain_2.setPlainText("")
        self.cw_plain_2.setObjectName("cw_plain_2")
        self.gridLayout_4.addWidget(self.cw_plain_2, 0, 1, 1, 1)
        self.cw_plain_1 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.cw_plain_1.setEnabled(True)
        self.cw_plain_1.setMinimumSize(QtCore.QSize(400, 50))
        self.cw_plain_1.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cw_plain_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_plain_1.setFont(font)
        self.cw_plain_1.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QPlainTextEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.cw_plain_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cw_plain_1.setPlainText("")
        self.cw_plain_1.setObjectName("cw_plain_1")
        self.gridLayout_4.addWidget(self.cw_plain_1, 1, 1, 1, 1)
        self.cw_info_8 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_8.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_8.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_8.setIcon(icon2)
        self.cw_info_8.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_8.setObjectName("cw_info_8")
        self.gridLayout_4.addWidget(self.cw_info_8, 1, 2, 1, 1)
        self.cw_label_8 = QtWidgets.QLabel(self.tab_3)
        self.cw_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_8.setFont(font)
        self.cw_label_8.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_8.setObjectName("cw_label_8")
        self.gridLayout_4.addWidget(self.cw_label_8, 0, 0, 1, 1)
        self.cw_label_7 = QtWidgets.QLabel(self.tab_3)
        self.cw_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_7.setFont(font)
        self.cw_label_7.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_7.setObjectName("cw_label_7")
        self.gridLayout_4.addWidget(self.cw_label_7, 1, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cw_label_9 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_9.setFont(font)
        self.cw_label_9.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_9.setObjectName("cw_label_9")
        self.horizontalLayout_4.addWidget(self.cw_label_9)
        self.cw_combobox_1 = QtWidgets.QComboBox(self.tab_3)
        self.cw_combobox_1.setMinimumSize(QtCore.QSize(150, 27))
        self.cw_combobox_1.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_combobox_1.setFont(font)
        self.cw_combobox_1.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.cw_combobox_1.setFrame(False)
        self.cw_combobox_1.setObjectName("cw_combobox_1")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.cw_combobox_1.addItem("")
        self.horizontalLayout_4.addWidget(self.cw_combobox_1)
        self.cw_add_3 = QtWidgets.QToolButton(self.tab_3)
        self.cw_add_3.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_add_3.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_add_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_add_3.setIcon(icon3)
        self.cw_add_3.setIconSize(QtCore.QSize(23, 23))
        self.cw_add_3.setObjectName("cw_add_3")
        self.horizontalLayout_4.addWidget(self.cw_add_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem20)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 100))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e5e5e5, stop: 1 #b2b2b2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e5e5e5, stop: 1 #b2b2b2);\n"
"    color: black;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #F0F0F0, stop: 1 #dddddd);\n"
"    border: 1px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"}\n"
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
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_5.addWidget(self.listWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cw_info_9 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_9.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_9.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_9.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_9.setIcon(icon2)
        self.cw_info_9.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_9.setObjectName("cw_info_9")
        self.verticalLayout_4.addWidget(self.cw_info_9)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem21)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem22)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cw_label_10 = QtWidgets.QLabel(self.tab_3)
        self.cw_label_10.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_10.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_10.setFont(font)
        self.cw_label_10.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.cw_label_10.setObjectName("cw_label_10")
        self.verticalLayout_6.addWidget(self.cw_label_10)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem23)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.cw_plain_4 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.cw_plain_4.setEnabled(True)
        self.cw_plain_4.setMinimumSize(QtCore.QSize(300, 100))
        self.cw_plain_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cw_plain_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_plain_4.setFont(font)
        self.cw_plain_4.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QPlainTextEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.cw_plain_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cw_plain_4.setPlainText("")
        self.cw_plain_4.setObjectName("cw_plain_4")
        self.horizontalLayout_6.addWidget(self.cw_plain_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cw_info_10 = QtWidgets.QToolButton(self.tab_3)
        self.cw_info_10.setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_10.setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_10.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cw_info_10.setIcon(icon2)
        self.cw_info_10.setIconSize(QtCore.QSize(23, 23))
        self.cw_info_10.setObjectName("cw_info_10")
        self.verticalLayout_5.addWidget(self.cw_info_10)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem24)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem25)
        self.gridLayout_5.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem26, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_11.addWidget(self.tabWidget)
        spacerItem27 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem27)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem28 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem28)
        self.cw_cancelButton = QtWidgets.QToolButton(creationWindow)
        self.cw_cancelButton.setMinimumSize(QtCore.QSize(100, 27))
        self.cw_cancelButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_cancelButton.setFont(font)
        self.cw_cancelButton.setStyleSheet("QToolButton {\n"
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
        self.cw_cancelButton.setObjectName("cw_cancelButton")
        self.horizontalLayout.addWidget(self.cw_cancelButton)
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem29)
        self.cw_okButton = QtWidgets.QToolButton(creationWindow)
        self.cw_okButton.setEnabled(True)
        self.cw_okButton.setMinimumSize(QtCore.QSize(100, 27))
        self.cw_okButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_okButton.setFont(font)
        self.cw_okButton.setStyleSheet("QToolButton {\n"
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
        self.cw_okButton.setObjectName("cw_okButton")
        self.horizontalLayout.addWidget(self.cw_okButton)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem30)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.gridLayout_11.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.retranslateUi(creationWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(creationWindow)

    def retranslateUi(self, creationWindow):
        _translate = QtCore.QCoreApplication.translate
        creationWindow.setWindowTitle(_translate("creationWindow", "Algorithm creation"))
        self.cw_label_1.setText(_translate("creationWindow", "Click on the \'+\' button to add a new input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("creationWindow", "Input(s)"))
        self.cw_label_2.setText(_translate("creationWindow", "Click on the \'+\' button to add a new output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("creationWindow", "Output(s)"))
        self.cw_label_3.setText(_translate("creationWindow", "Algorithm name:"))
        self.cw_label_5.setText(_translate("creationWindow", "Algorithm sources:"))
        self.cw_label_4.setText(_translate("creationWindow", "Algorithm author(s):"))
        self.cw_label_6.setText(_translate("creationWindow", "Algorithm references:"))
        self.cw_label_8.setText(_translate("creationWindow", "Algorithm purpose:"))
        self.cw_label_7.setText(_translate("creationWindow", "Algorithm description:"))
        self.cw_label_9.setText(_translate("creationWindow", "Algorithm category:"))
        self.cw_combobox_1.setItemText(0, _translate("creationWindow", "Make a choice..."))
        self.cw_combobox_1.setItemText(1, _translate("creationWindow", "Other..."))
        self.cw_combobox_1.setItemText(2, _translate("creationWindow", "Comparisons"))
        self.cw_combobox_1.setItemText(3, _translate("creationWindow", "Corrections"))
        self.cw_combobox_1.setItemText(4, _translate("creationWindow", "Mathematics"))
        self.cw_combobox_1.setItemText(5, _translate("creationWindow", "Microphysics"))
        self.cw_combobox_1.setItemText(6, _translate("creationWindow", "Radiation"))
        self.cw_combobox_1.setItemText(7, _translate("creationWindow", "Thermodynamics"))
        self.cw_combobox_1.setItemText(8, _translate("creationWindow", "Transforms"))
        self.cw_label_10.setText(_translate("creationWindow", "Algorithm:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("creationWindow", "Algorithm"))
        self.cw_cancelButton.setText(_translate("creationWindow", "Cancel"))
        self.cw_okButton.setText(_translate("creationWindow", "Save"))

