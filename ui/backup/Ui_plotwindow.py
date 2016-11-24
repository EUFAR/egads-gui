# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_window_2.ui'
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

class Ui_PlotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName(_fromUtf8("plotWindow"))
        plotWindow.resize(1100, 650)
        plotWindow.setMinimumSize(QtCore.QSize(1100, 650))
        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBar = QtGui.QToolBar()
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.verticalLayout.addWidget(self.toolBar)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.tabWidget = QtGui.QTabWidget(plotWindow)
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane { \n"
        "    border: 1px solid rgb(180,180,180);\n"
        "    border-bottom-left-radius: 5px;\n"
        "    border-bottom-right-radius: 5px;\n"
        "    border-top-right-radius: 5px;\n"
        "   top: -1px;\n"
        "   background-color: rgb(230,230,230);\n"
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
        "     border-top-left-radius: 5px;\n"
        "    padding: 2px 10px 2px 10px;\n"
        "    margin-right: 2px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "    background-color: rgb(210,210,210);\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "    background-color: rgb(230,230,230);\n"
        "}\n"
        "\n"
        "QTabBar::tab:!selected {\n"
        "    margin-top: 4px; \n"
        "}"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pw_label_1 = QtGui.QLabel(self.tab)
        self.pw_label_1.setMinimumSize(QtCore.QSize(300, 27))
        self.pw_label_1.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_1.setFont(font)
        self.pw_label_1.setObjectName(_fromUtf8("pw_label_1"))
        self.horizontalLayout.addWidget(self.pw_label_1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pw_xvariable_rl = QtGui.QComboBox(self.tab)
        self.pw_xvariable_rl.setFont(font)
        self.pw_xvariable_rl.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_xvariable_rl.setMaximumSize(QtCore.QSize(250, 27))
        self.pw_xvariable_rl.setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
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
        "    image: url(images/arrow_down.png);\n"
        "    width: 18px;\n"
        "    height: 18px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow:on {\n"
        "    top: 1px;\n"
        "    left: 1px;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    background-color: rgb(240,240,240);\n"
        "    selection-color: blue;\n"
        "   padding: 1px 4px 1px 1px 1px\n"
        "}"))
        self.pw_xvariable_rl.setObjectName(_fromUtf8("pw_xvariable_rl"))
        self.horizontalLayout_2.addWidget(self.pw_xvariable_rl)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pw_label_2 = QtGui.QLabel(self.tab)
        self.pw_label_2.setMinimumSize(QtCore.QSize(310, 60))
        self.pw_label_2.setMaximumSize(QtCore.QSize(310, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_2.setFont(font)
        self.pw_label_2.setWordWrap(True)
        self.pw_label_2.setObjectName(_fromUtf8("pw_label_2"))
        self.horizontalLayout_3.addWidget(self.pw_label_2)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pw_yvariable_rl = QtGui.QComboBox(self.tab)
        self.pw_yvariable_rl.setFont(font)
        self.pw_yvariable_rl.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_yvariable_rl.setMaximumSize(QtCore.QSize(250, 27))
        self.pw_yvariable_rl.setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
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
        "    image: url(images/arrow_down.png);\n"
        "    width: 18px;\n"
        "    height: 18px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow:on {\n"
        "    top: 1px;\n"
        "    left: 1px;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    background-color: rgb(240,240,240);\n"
        "    selection-color: blue;\n"
        "   padding: 1px 4px 1px 1px 1px\n"
        "}"))
        self.pw_yvariable_rl.setObjectName(_fromUtf8("pw_yvariable_rl"))
        self.horizontalLayout_4.addWidget(self.pw_yvariable_rl)
        self.pw_addbutton = QtGui.QToolButton(self.tab)
        self.pw_addbutton.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_addbutton.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_addbutton.setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_addbutton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/plus_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_addbutton.setIcon(icon)
        self.pw_addbutton.setIconSize(QtCore.QSize(27, 27))
        self.pw_addbutton.setAutoRaise(True)
        self.pw_addbutton.setObjectName(_fromUtf8("pw_addbutton"))
        self.horizontalLayout_4.addWidget(self.pw_addbutton)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem50 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem50)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.pw_label_11 = QtGui.QLabel(self.tab)
        self.pw_label_11.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_label_11.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_11.setFont(font)
        self.pw_label_11.setText("List of plotted variables:")
        self.pw_label_11.setObjectName(_fromUtf8("pw_label_11"))
        self.pw_label_11.hide()
        self.horizontalLayout_15.addWidget(self.pw_label_11)
        spacerItem51 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem51)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.scrollArea2 = QtGui.QScrollArea(self.tab)

        self.scrollArea2.setStyleSheet(_fromUtf8("QScrollArea { background: transparent; }\n"
        "\n"
        "QScrollArea > QWidget > QWidget { background: transparent; }\n"
        ))
        
        self.scrollArea2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea2.setMinimumSize(QtCore.QSize(300, 270))
        self.scrollArea2.setMaximumSize(QtCore.QSize(300, 270))
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName(_fromUtf8("scrollArea2"))
        self.scrollAreaWidgetContents2 = QtGui.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(QtCore.QRect(0, 0, 300, 270))
        self.scrollAreaWidgetContents2.setObjectName(_fromUtf8("scrollAreaWidgetContents2"))
        self.gridLayout_10 = QtGui.QGridLayout(self.scrollAreaWidgetContents2)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem40 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_10.addItem(spacerItem40, 1, 0, 1, 1)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents2)
        self.horizontalLayout_5.addWidget(self.scrollArea2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_6.addWidget(self.line)
        self.pw_plot_fr = QtGui.QVBoxLayout()
        self.pw_plot_fr.setObjectName(_fromUtf8("pw_plot_fr"))
        self.horizontalLayout_6.addLayout(self.pw_plot_fr)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.pw_label_3 = QtGui.QLabel(self.tab_2)
        self.pw_label_3.setMinimumSize(QtCore.QSize(150, 27))
        self.pw_label_3.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_3.setFont(font)
        self.pw_label_3.setObjectName(_fromUtf8("pw_label_3"))
        self.horizontalLayout_13.addWidget(self.pw_label_3)
        spacerItem9 = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem10 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem10)
        self.pw_label_4 = QtGui.QLabel(self.tab_2)
        self.pw_label_4.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_label_4.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_4.setFont(font)
        self.pw_label_4.setObjectName(_fromUtf8("pw_label_4"))
        self.horizontalLayout_14.addWidget(self.pw_label_4)
        self.pw_title_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_title_ln.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_title_ln.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_title_ln.setFont(font)
        self.pw_title_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_title_ln.setObjectName(_fromUtf8("pw_title_ln"))
        self.horizontalLayout_14.addWidget(self.pw_title_ln)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_button_0 = QtGui.QToolButton()
        self.pw_button_0.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_button_0.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_button_0.setText(_fromUtf8(""))
        self.pw_button_0.setIcon(icon)
        self.pw_button_0.setIconSize(QtCore.QSize(27, 27))
        self.pw_button_0.setPopupMode(QtGui.QToolButton.InstantPopup)  
        self.pw_button_0.setAutoRaise(True)
        self.pw_button_0.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                 stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "QToolButton:flat {\n"
        "    border: none; /* no border for a flat push button */\n"
        "}"))
        self.pw_button_0.setObjectName("pw_button_0")
        self.horizontalLayout_14.addWidget(self.pw_button_0)
        spacerItem11 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem12)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pw_label_5 = QtGui.QLabel(self.tab_2)
        self.pw_label_5.setMinimumSize(QtCore.QSize(150, 27))
        self.pw_label_5.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_5.setFont(font)
        self.pw_label_5.setObjectName(_fromUtf8("pw_label_5"))
        self.horizontalLayout_7.addWidget(self.pw_label_5)
        spacerItem13 = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem14 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.pw_label_6 = QtGui.QLabel(self.tab_2)
        self.pw_label_6.setMinimumSize(QtCore.QSize(190, 27))
        self.pw_label_6.setMaximumSize(QtCore.QSize(190, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_6.setFont(font)
        self.pw_label_6.setObjectName(_fromUtf8("pw_label_6"))
        self.horizontalLayout_8.addWidget(self.pw_label_6)
        self.pw_xmin_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_xmin_ln.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_xmin_ln.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_xmin_ln.setFont(font)
        self.pw_xmin_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_xmin_ln.setObjectName(_fromUtf8("pw_xmin_ln"))
        self.horizontalLayout_8.addWidget(self.pw_xmin_ln)
        self.pw_xmax_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_xmax_ln.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_xmax_ln.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_xmax_ln.setFont(font)
        self.pw_xmax_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_xmax_ln.setObjectName(_fromUtf8("pw_xmax_ln"))
        self.horizontalLayout_8.addWidget(self.pw_xmax_ln)
        self.pw_xtick_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_xtick_ln.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_xtick_ln.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_xtick_ln.setFont(font)
        self.pw_xtick_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_xtick_ln.setObjectName(_fromUtf8("pw_xtick_ln"))
        self.horizontalLayout_8.addWidget(self.pw_xtick_ln)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_button_1 = QtGui.QToolButton()
        self.pw_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_button_1.setText(_fromUtf8(""))
        self.pw_button_1.setIcon(icon)
        self.pw_button_1.setIconSize(QtCore.QSize(27, 27))
        self.pw_button_1.setPopupMode(QtGui.QToolButton.InstantPopup)  
        self.pw_button_1.setAutoRaise(True)
        self.pw_button_1.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                 stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "QToolButton:flat {\n"
        "    border: none; /* no border for a flat push button */\n"
        "}"))
        self.pw_button_1.setObjectName("pw_button_1")
        self.horizontalLayout_8.addWidget(self.pw_button_1)
        spacerItem15 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem16 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.pw_label_7 = QtGui.QLabel(self.tab_2)
        self.pw_label_7.setMinimumSize(QtCore.QSize(190, 27))
        self.pw_label_7.setMaximumSize(QtCore.QSize(190, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_7.setFont(font)
        self.pw_label_7.setObjectName(_fromUtf8("pw_label_7"))
        self.horizontalLayout_9.addWidget(self.pw_label_7)
        self.pw_ymin_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_ymin_ln.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_ymin_ln.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_ymin_ln.setFont(font)
        self.pw_ymin_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_ymin_ln.setObjectName(_fromUtf8("pw_ymin_ln"))
        self.horizontalLayout_9.addWidget(self.pw_ymin_ln)
        self.pw_ymax_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_ymax_ln.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_ymax_ln.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_ymax_ln.setFont(font)
        self.pw_ymax_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_ymax_ln.setObjectName(_fromUtf8("pw_ymax_ln"))
        self.horizontalLayout_9.addWidget(self.pw_ymax_ln)
        self.pw_ytick_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_ytick_ln.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_ytick_ln.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_ytick_ln.setFont(font)
        self.pw_ytick_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_ytick_ln.setObjectName(_fromUtf8("pw_ytick_ln"))
        self.horizontalLayout_9.addWidget(self.pw_ytick_ln)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_button_2 = QtGui.QToolButton()
        self.pw_button_2.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_button_2.setText(_fromUtf8(""))
        self.pw_button_2.setIcon(icon)
        self.pw_button_2.setIconSize(QtCore.QSize(27, 27))
        self.pw_button_2.setPopupMode(QtGui.QToolButton.InstantPopup)  
        self.pw_button_2.setAutoRaise(True)
        self.pw_button_2.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                 stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "QToolButton:flat {\n"
        "    border: none; /* no border for a flat push button */\n"
        "}"))
        self.pw_button_2.setObjectName("pw_button_2")
        self.horizontalLayout_9.addWidget(self.pw_button_2)
        spacerItem17 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem18 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.pw_label_8 = QtGui.QLabel(self.tab_2)
        self.pw_label_8.setMinimumSize(QtCore.QSize(70, 27))
        self.pw_label_8.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_8.setFont(font)
        self.pw_label_8.setObjectName(_fromUtf8("pw_label_8"))
        self.horizontalLayout_10.addWidget(self.pw_label_8)
        self.pw_xlabel_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_xlabel_ln.setMinimumSize(QtCore.QSize(262, 27))
        self.pw_xlabel_ln.setMaximumSize(QtCore.QSize(262, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_xlabel_ln.setFont(font)
        self.pw_xlabel_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_xlabel_ln.setObjectName(_fromUtf8("pw_xlabel_ln"))
        self.horizontalLayout_10.addWidget(self.pw_xlabel_ln)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_button_3 = QtGui.QToolButton()
        self.pw_button_3.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_button_3.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_button_3.setText(_fromUtf8(""))
        self.pw_button_3.setIcon(icon)
        self.pw_button_3.setIconSize(QtCore.QSize(27, 27))
        self.pw_button_3.setPopupMode(QtGui.QToolButton.InstantPopup)  
        self.pw_button_3.setAutoRaise(True)
        self.pw_button_3.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                 stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "QToolButton:flat {\n"
        "    border: none; /* no border for a flat push button */\n"
        "}"))
        self.pw_button_3.setObjectName("pw_button_3")
        self.horizontalLayout_10.addWidget(self.pw_button_3)
        spacerItem19 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem19)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem20 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem20)
        self.pw_label_9 = QtGui.QLabel(self.tab_2)
        self.pw_label_9.setMinimumSize(QtCore.QSize(70, 27))
        self.pw_label_9.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_9.setFont(font)
        self.pw_label_9.setObjectName(_fromUtf8("pw_label_9"))
        self.horizontalLayout_11.addWidget(self.pw_label_9)
        self.pw_ylabel_ln = QtGui.QLineEdit(self.tab_2)
        self.pw_ylabel_ln.setMinimumSize(QtCore.QSize(262, 27))
        self.pw_ylabel_ln.setMaximumSize(QtCore.QSize(262, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_ylabel_ln.setFont(font)
        self.pw_ylabel_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_ylabel_ln.setObjectName(_fromUtf8("pw_ylabel_ln"))
        self.horizontalLayout_11.addWidget(self.pw_ylabel_ln)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_button_4 = QtGui.QToolButton()
        self.pw_button_4.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_button_4.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_button_4.setText(_fromUtf8(""))
        self.pw_button_4.setIcon(icon)
        self.pw_button_4.setIconSize(QtCore.QSize(27, 27))
        self.pw_button_4.setPopupMode(QtGui.QToolButton.InstantPopup)  
        self.pw_button_4.setAutoRaise(True)
        self.pw_button_4.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                 stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "QToolButton:flat {\n"
        "    border: none; /* no border for a flat push button */\n"
        "}"))
        self.pw_button_4.setObjectName("pw_button_4")
        self.horizontalLayout_11.addWidget(self.pw_button_4)
        spacerItem21 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem21)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem22 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem22)
        self.pw_label_10 = QtGui.QLabel(self.tab_2)
        self.pw_label_10.setMinimumSize(QtCore.QSize(110, 27))
        self.pw_label_10.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_10.setFont(font)
        self.pw_label_10.setObjectName(_fromUtf8("pw_label_10"))
        self.horizontalLayout_12.addWidget(self.pw_label_10)
        self.pw_grid_ck = QtGui.QCheckBox(self.tab_2)
        self.pw_grid_ck.setMinimumSize(QtCore.QSize(20, 20))
        self.pw_grid_ck.setMaximumSize(QtCore.QSize(20, 20))
        self.pw_grid_ck.setText(_fromUtf8(""))
        self.pw_grid_ck.setObjectName(_fromUtf8("pw_grid_ck"))
        self.horizontalLayout_12.addWidget(self.pw_grid_ck)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_button_5 = QtGui.QToolButton()
        self.pw_button_5.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_button_5.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_button_5.setText(_fromUtf8(""))
        self.pw_button_5.setIcon(icon)
        self.pw_button_5.setIconSize(QtCore.QSize(27, 27))
        self.pw_button_5.setPopupMode(QtGui.QToolButton.InstantPopup)  
        self.pw_button_5.setAutoRaise(True)
        self.pw_button_5.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                 stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "QToolButton:flat {\n"
        "    border: none; /* no border for a flat push button */\n"
        "}"))
        self.pw_button_5.setObjectName("pw_button_5")
        self.horizontalLayout_12.addWidget(self.pw_button_5)
        spacerItem23 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem23)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        spacerItem24 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem24)
        self.horizontalLayout_23.addLayout(self.verticalLayout_5)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_23.addWidget(self.line_2)
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setStyleSheet(_fromUtf8("QScrollArea { background: transparent; }\n"
        "\n"
        "QScrollArea > QWidget > QWidget { background: transparent; }\n"
        ))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setMinimumSize(QtCore.QSize(580, 510))
        self.scrollArea.setMaximumSize(QtCore.QSize(580, 510))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 540, 510))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem40 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem40)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_23.addWidget(self.scrollArea)
        
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        spacerItem41 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem41)
        self.toolButton = QtGui.QToolButton(self.tab_2)
        self.toolButton.setFont(font)
        self.toolButton.setMinimumSize(QtCore.QSize(80, 27))
        self.toolButton.setMaximumSize(QtCore.QSize(80, 27))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_24.addWidget(self.toolButton)
        spacerItem42 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem42)
        
        
        self.verticalLayout_8.addLayout(self.horizontalLayout_24)
        self.gridLayout_4.addLayout(self.verticalLayout_8, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.actionSave_as = QtGui.QAction(plotWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save_as_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon1)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionSave_as.setEnabled(False)
        self.actionClose = QtGui.QAction(plotWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/exit_icon_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionZoom = QtGui.QAction(plotWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/zoom_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon4)
        self.actionZoom.setObjectName(_fromUtf8("actionZoom"))
        self.actionZoom.setEnabled(False)
        self.actionPan = QtGui.QAction(plotWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pan_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon5)
        self.actionPan.setObjectName(_fromUtf8("actionPan"))
        self.actionPan.setEnabled(False)
        self.actionOrigin = QtGui.QAction(plotWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/origin_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOrigin.setIcon(icon6)
        self.actionOrigin.setObjectName(_fromUtf8("actionOrigin"))
        self.actionOrigin.setEnabled(False)
        self.actionClear = QtGui.QAction(plotWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon6)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionClear.setEnabled(False)
        self.actionSeparator1 = QtGui.QAction(plotWindow)
        self.actionSeparator1.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icons/separator_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSeparator1.setIcon(icon7)
        self.actionSeparator1.setObjectName(_fromUtf8("actionSeparator1"))
        self.actionSeparator2 = QtGui.QAction(plotWindow)
        self.actionSeparator2.setEnabled(False)
        self.actionSeparator2.setIcon(icon7)
        self.actionSeparator2.setObjectName(_fromUtf8("actionSeparator2"))
        self.actionSeparator3 = QtGui.QAction(plotWindow)
        self.actionSeparator3.setEnabled(False)
        self.actionSeparator3.setIcon(icon7)
        self.actionSeparator3.setObjectName(_fromUtf8("actionSeparator3"))
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionSeparator1)
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionZoom)
        self.toolBar.addAction(self.actionSeparator2)
        self.toolBar.addAction(self.actionOrigin)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addAction(self.actionSeparator3)
        self.toolBar.addAction(self.actionClose)
        self.toolBar.setIconSize(QtCore.QSize(36, 36))

        self.retranslateUi(plotWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(_translate("plotWindow", "Data Plot", None))
        self.pw_label_1.setText(_translate("plotWindow", "Please choose a variable for the X axis", None))
        self.pw_label_2.setText(_translate("plotWindow", "Please choose one variable in the following list for the Y axis and click on the '+' button to add it to the plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("plotWindow", "Plot window", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("plotWindow", "Plot options", None))
        self.toolBar.setWindowTitle(_translate("plotWindow", "toolBar", None))
        self.actionSave_as.setText(_translate("plotWindow", "Save as...", None))
        self.actionSave_as.setToolTip(_translate("plotWindow", "Save to a graphic file", None))
        self.actionClose.setText(_translate("plotWindow", "Close...", None))
        self.actionClose.setToolTip(_translate("plotWindow", "Close the plot window", None))
        self.actionZoom.setText(_translate("plotWindow", "Zoom", None))
        self.actionZoom.setToolTip(_translate("plotWindow", "Zoom to rectangle", None))
        self.actionPan.setText(_translate("plotWindow", "Pan", None))
        self.actionPan.setToolTip(_translate("plotWindow", "Pan axes", None))
        self.actionOrigin.setText(_translate("plotWindow", "Origin", None))
        self.actionOrigin.setToolTip(_translate("plotWindow", "Reset to original view", None))
        self.actionClear.setText(_translate("plotWindow", "Clear", None))
        self.actionClear.setToolTip(_translate("plotWindow", "Clear the view", None))
        self.pw_label_3.setText(_translate("plotWindow", "Figure options", None))
        self.pw_label_4.setText(_translate("plotWindow", "Figure title:", None))
        self.pw_label_5.setText(_translate("plotWindow", "Axis options", None))
        self.pw_label_6.setText(_translate("plotWindow", "X min / max / tick step:", None))
        self.pw_label_7.setText(_translate("plotWindow", "Y min / max / tick step:", None))
        self.pw_label_8.setText(_translate("plotWindow", "X label:", None))
        self.pw_label_9.setText(_translate("plotWindow", "Y label:", None))
        self.pw_label_10.setText(_translate("plotWindow", "Display grid ?", None))
        self.toolButton.setText(_translate("PlotWindow", "Update", None))
