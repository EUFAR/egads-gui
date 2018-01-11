# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process_window_3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_processingWindow(object):
    def setupUi(self, processingWindow):
        processingWindow.setObjectName("processingWindow")
        processingWindow.resize(700, 565)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(processingWindow.sizePolicy().hasHeightForWidth())
        processingWindow.setSizePolicy(sizePolicy)
        processingWindow.setMinimumSize(QtCore.QSize(700, 565))
        processingWindow.setMaximumSize(QtCore.QSize(700, 565))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        processingWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        processingWindow.setWindowIcon(icon)
        processingWindow.setStyleSheet("")
        self.gridLayout_11 = QtWidgets.QGridLayout(processingWindow)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(processingWindow)
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
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_13.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.aw_label_1 = QtWidgets.QLabel(self.tab_4)
        self.aw_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_1.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_1.setFont(font)
        self.aw_label_1.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.aw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aw_label_1.setWordWrap(True)
        self.aw_label_1.setObjectName("aw_label_1")
        self.verticalLayout_2.addWidget(self.aw_label_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.aw_label_2 = QtWidgets.QLabel(self.tab_4)
        self.aw_label_2.setEnabled(True)
        self.aw_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_2.setFont(font)
        self.aw_label_2.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.aw_label_2.setObjectName("aw_label_2")
        self.gridLayout_2.addWidget(self.aw_label_2, 0, 0, 1, 1)
        self.aw_combobox_1 = QtWidgets.QComboBox(self.tab_4)
        self.aw_combobox_1.setMinimumSize(QtCore.QSize(200, 27))
        self.aw_combobox_1.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_combobox_1.setFont(font)
        self.aw_combobox_1.setStyleSheet("QComboBox {\n"
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
        self.aw_combobox_1.setFrame(False)
        self.aw_combobox_1.setObjectName("aw_combobox_1")
        self.gridLayout_2.addWidget(self.aw_combobox_1, 0, 1, 1, 1)
        self.aw_label_3 = QtWidgets.QLabel(self.tab_4)
        self.aw_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_3.setFont(font)
        self.aw_label_3.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.aw_label_3.setObjectName("aw_label_3")
        self.gridLayout_2.addWidget(self.aw_label_3, 1, 0, 1, 1)
        self.aw_combobox_2 = QtWidgets.QComboBox(self.tab_4)
        self.aw_combobox_2.setEnabled(False)
        self.aw_combobox_2.setMinimumSize(QtCore.QSize(200, 27))
        self.aw_combobox_2.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_combobox_2.setFont(font)
        self.aw_combobox_2.setStyleSheet("QComboBox {\n"
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
        self.aw_combobox_2.setFrame(False)
        self.aw_combobox_2.setObjectName("aw_combobox_2")
        self.gridLayout_2.addWidget(self.aw_combobox_2, 1, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.line_2 = QtWidgets.QFrame(self.tab_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.aw_label_4 = QtWidgets.QLabel(self.tab_4)
        self.aw_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_4.setFont(font)
        self.aw_label_4.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.aw_label_4.setObjectName("aw_label_4")
        self.gridLayout_12.addWidget(self.aw_label_4, 0, 0, 1, 1)
        self.aw_textbrowser_1 = QtWidgets.QTextBrowser(self.tab_4)
        self.aw_textbrowser_1.setMinimumSize(QtCore.QSize(500, 100))
        self.aw_textbrowser_1.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_textbrowser_1.setFont(font)
        self.aw_textbrowser_1.setStyleSheet("QTextBrowser {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QTextBrowser:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.aw_textbrowser_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aw_textbrowser_1.setObjectName("aw_textbrowser_1")
        self.gridLayout_12.addWidget(self.aw_textbrowser_1, 0, 1, 1, 1)
        self.aw_label_5 = QtWidgets.QLabel(self.tab_4)
        self.aw_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_5.setFont(font)
        self.aw_label_5.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.aw_label_5.setObjectName("aw_label_5")
        self.gridLayout_12.addWidget(self.aw_label_5, 1, 0, 1, 1)
        self.aw_textbrowser_2 = QtWidgets.QTextBrowser(self.tab_4)
        self.aw_textbrowser_2.setMinimumSize(QtCore.QSize(500, 100))
        self.aw_textbrowser_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_textbrowser_2.setFont(font)
        self.aw_textbrowser_2.setStyleSheet("QTextBrowser {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QTextBrowser:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.aw_textbrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aw_textbrowser_2.setObjectName("aw_textbrowser_2")
        self.gridLayout_12.addWidget(self.aw_textbrowser_2, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_12)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.gridLayout_13.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem7, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem9, 1, 2, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.aw_label_6 = QtWidgets.QLabel(self.tab_5)
        self.aw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_6.setFont(font)
        self.aw_label_6.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.aw_label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aw_label_6.setWordWrap(True)
        self.aw_label_6.setObjectName("aw_label_6")
        self.horizontalLayout_12.addWidget(self.aw_label_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        spacerItem10 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem10)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.scrollArea_4.setFont(font)
        self.scrollArea_4.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 616, 335))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.input_layout_2 = QtWidgets.QGridLayout()
        self.input_layout_2.setObjectName("input_layout_2")
        self.gridLayout_8.addLayout(self.input_layout_2, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 181, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem11, 1, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_9.addWidget(self.scrollArea_4)
        self.gridLayout_7.addLayout(self.verticalLayout_9, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem12, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.aw_label_7 = QtWidgets.QLabel(self.tab_6)
        self.aw_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_7.setFont(font)
        self.aw_label_7.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.aw_label_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aw_label_7.setWordWrap(True)
        self.aw_label_7.setObjectName("aw_label_7")
        self.horizontalLayout_13.addWidget(self.aw_label_7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        spacerItem13 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem13)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_6)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.scrollArea_5.setFont(font)
        self.scrollArea_5.setAutoFillBackground(False)
        self.scrollArea_5.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.scrollArea_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 616, 335))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.output_layout_2 = QtWidgets.QGridLayout()
        self.output_layout_2.setObjectName("output_layout_2")
        self.gridLayout_10.addLayout(self.output_layout_2, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 181, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem14, 1, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_10.addWidget(self.scrollArea_5)
        self.gridLayout_9.addLayout(self.verticalLayout_10, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem15, 1, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem16, 1, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem17, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout_11.addWidget(self.tabWidget)
        spacerItem18 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem18)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem19)
        self.aw_cancelButton = QtWidgets.QToolButton(processingWindow)
        self.aw_cancelButton.setMinimumSize(QtCore.QSize(100, 27))
        self.aw_cancelButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_cancelButton.setFont(font)
        self.aw_cancelButton.setStyleSheet("QToolButton {\n"
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
        self.aw_cancelButton.setObjectName("aw_cancelButton")
        self.horizontalLayout.addWidget(self.aw_cancelButton)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem20)
        self.aw_okButton = QtWidgets.QToolButton(processingWindow)
        self.aw_okButton.setEnabled(False)
        self.aw_okButton.setMinimumSize(QtCore.QSize(180, 27))
        self.aw_okButton.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_okButton.setFont(font)
        self.aw_okButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: black;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.aw_okButton.setObjectName("aw_okButton")
        self.horizontalLayout.addWidget(self.aw_okButton)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem21)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.gridLayout_11.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.retranslateUi(processingWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(processingWindow)

    def retranslateUi(self, processingWindow):
        _translate = QtCore.QCoreApplication.translate
        processingWindow.setWindowTitle(_translate("processingWindow", "Processing"))
        self.aw_label_1.setText(_translate("processingWindow", "<html><head/><body><p align=\"justify\">Please choose a category and an algorithm to begin the processing. Once it has been done, please proceed with the next step: Input(s).</p></body></html>"))
        self.aw_label_2.setText(_translate("processingWindow", "Category:"))
        self.aw_label_3.setText(_translate("processingWindow", "Algorithm:"))
        self.aw_label_4.setText(_translate("processingWindow", "Purpose:"))
        self.aw_textbrowser_1.setHtml(_translate("processingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'FreeSans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro\'; font-size:12pt;\"><br /></p></body></html>"))
        self.aw_label_5.setText(_translate("processingWindow", "Description:"))
        self.aw_textbrowser_2.setHtml(_translate("processingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'FreeSans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro\'; font-size:12pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("processingWindow", "Choose an algorithm"))
        self.aw_label_6.setText(_translate("processingWindow", "<html><head/><body><p align=\"justify\">Please enter a variable name for the input(s). Once it has been done, please proceed with the next step: Output(s).</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("processingWindow", "Input(s)"))
        self.aw_label_7.setText(_translate("processingWindow", "<html><head/><body><p align=\"justify\">Please select the output(s). Once it has been done, please click on save to launch the processing.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("processingWindow", "Output(s)"))
        self.aw_cancelButton.setText(_translate("processingWindow", "Cancel"))
        self.aw_okButton.setText(_translate("processingWindow", "Launch processing"))

