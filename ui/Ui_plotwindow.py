# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_window_3.ui'
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

class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName(_fromUtf8("plotWindow"))
        plotWindow.resize(1105, 659)
        plotWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/plot_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        plotWindow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pw_toolbar_fr = QtGui.QVBoxLayout()
        self.pw_toolbar_fr.setObjectName(_fromUtf8("pw_toolbar_fr"))
        self.verticalLayout_4.addLayout(self.pw_toolbar_fr)
        self.tabWidget = QtGui.QTabWidget(plotWindow)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
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
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pw_label_1 = QtGui.QLabel(self.tab)
        self.pw_label_1.setMinimumSize(QtCore.QSize(260, 27))
        self.pw_label_1.setMaximumSize(QtCore.QSize(260, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_label_1.setFont(font)
        self.pw_label_1.setObjectName(_fromUtf8("pw_label_1"))
        self.horizontalLayout_6.addWidget(self.pw_label_1)
        spacerItem = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.pw_single_rd = QtGui.QRadioButton(self.tab)
        self.pw_single_rd.setMinimumSize(QtCore.QSize(120, 27))
        self.pw_single_rd.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_single_rd.setFont(font)
        self.pw_single_rd.setObjectName(_fromUtf8("pw_single_rd"))
        self.pw_single_rd.setStyleSheet(_fromUtf8("QRadioButton {\n"
        "    spacing: 5px;\n"
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
        "}"))
        self.horizontalLayout_18.addWidget(self.pw_single_rd)
        self.pw_multiple_rd = QtGui.QRadioButton(self.tab)
        self.pw_multiple_rd.setMinimumSize(QtCore.QSize(140, 27))
        self.pw_multiple_rd.setMaximumSize(QtCore.QSize(140, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_multiple_rd.setFont(font)
        self.pw_multiple_rd.setObjectName(_fromUtf8("pw_multiple_rd"))
        self.pw_multiple_rd.setStyleSheet(_fromUtf8("QRadioButton {\n"
        "    spacing: 5px;\n"
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
        "}"))
        self.horizontalLayout_18.addWidget(self.pw_multiple_rd)
        self.pw_info_bt1 = QtGui.QToolButton(self.tab)
        self.pw_info_bt1.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt1.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt1.setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
"\n"
"QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"\n"
"QToolButton:flat {border: none;}"))
        self.pw_info_bt1.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_info_bt1.setIcon(icon)
        self.pw_info_bt1.setIconSize(QtCore.QSize(27, 27))
        self.pw_info_bt1.setAutoRaise(True)
        self.pw_info_bt1.setObjectName(_fromUtf8("pw_info_bt1"))
        self.horizontalLayout_18.addWidget(self.pw_info_bt1)
        spacerItem2 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pw_graphType_sa = QtGui.QScrollArea(self.tab)
        self.pw_graphType_sa.setMinimumSize(QtCore.QSize(390, 0))
        self.pw_graphType_sa.setMaximumSize(QtCore.QSize(390, 16777215))
        self.pw_graphType_sa.setStyleSheet(_fromUtf8("QScrollArea {background: transparent;}\n"
"\n"
"QScrollArea > QWidget > QWidget {background: transparent;}"))
        self.pw_graphType_sa.setFrameShape(QtGui.QFrame.NoFrame)
        self.pw_graphType_sa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pw_graphType_sa.setWidgetResizable(True)
        self.pw_graphType_sa.setObjectName(_fromUtf8("pw_graphType_sa"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 390, 482))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pw_graphType_la = QtGui.QVBoxLayout()
        self.pw_graphType_la.setObjectName(_fromUtf8("pw_graphType_la"))
        self.gridLayout_4.addLayout(self.pw_graphType_la, 0, 0, 1, 1)
        self.pw_graphType_sa.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.pw_graphType_sa)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.pw_plot_fr = QtGui.QVBoxLayout()
        self.pw_plot_fr.setObjectName(_fromUtf8("pw_plot_fr"))
        self.horizontalLayout.addLayout(self.pw_plot_fr)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pw_plotOption_fr = QtGui.QScrollArea(self.tab_2)
        self.pw_plotOption_fr.setMinimumSize(QtCore.QSize(480, 0))
        self.pw_plotOption_fr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pw_plotOption_fr.setStyleSheet(_fromUtf8("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }"))
        self.pw_plotOption_fr.setFrameShape(QtGui.QFrame.NoFrame)
        self.pw_plotOption_fr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pw_plotOption_fr.setWidgetResizable(True)
        self.pw_plotOption_fr.setObjectName(_fromUtf8("pw_plotOption_fr"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1061, 527))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pw_graphOptions_la = QtGui.QVBoxLayout()
        self.pw_graphOptions_la.setObjectName(_fromUtf8("pw_graphOptions_la"))
        self.gridLayout_5.addLayout(self.pw_graphOptions_la, 0, 0, 1, 1)
        self.pw_plotOption_fr.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_2.addWidget(self.pw_plotOption_fr)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem5)
        self.pw_update_bt_1 = QtGui.QToolButton(self.tab_2)
        self.pw_update_bt_1.setMinimumSize(QtCore.QSize(80, 27))
        self.pw_update_bt_1.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_update_bt_1.setFont(font)
        self.pw_update_bt_1.setObjectName(_fromUtf8("pw_update_bt_1"))
        self.horizontalLayout_24.addWidget(self.pw_update_bt_1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_24)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.pw_lineOption_fr_2 = QtGui.QScrollArea(self.tab_4)
        self.pw_lineOption_fr_2.setMinimumSize(QtCore.QSize(540, 0))
        self.pw_lineOption_fr_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pw_lineOption_fr_2.setStyleSheet(_fromUtf8("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }"))
        self.pw_lineOption_fr_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.pw_lineOption_fr_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pw_lineOption_fr_2.setWidgetResizable(True)
        self.pw_lineOption_fr_2.setObjectName(_fromUtf8("pw_lineOption_fr_2"))
        self.scrollAreaWidgetContents_5 = QtGui.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1061, 527))
        self.scrollAreaWidgetContents_5.setObjectName(_fromUtf8("scrollAreaWidgetContents_5"))
        self.gridLayout_9 = QtGui.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.pw_plotOptions_la = QtGui.QVBoxLayout()
        self.pw_plotOptions_la.setObjectName(_fromUtf8("pw_plotOptions_la"))
        self.gridLayout_9.addLayout(self.pw_plotOptions_la, 0, 0, 1, 1)
        self.pw_lineOption_fr_2.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_9.addWidget(self.pw_lineOption_fr_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        spacerItem7 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem8)
        self.pw_update_bt_2 = QtGui.QToolButton(self.tab_4)
        self.pw_update_bt_2.setMinimumSize(QtCore.QSize(80, 27))
        self.pw_update_bt_2.setMaximumSize(QtCore.QSize(80, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_update_bt_2.setFont(font)
        self.pw_update_bt_2.setObjectName(_fromUtf8("pw_update_bt_2"))
        self.horizontalLayout_25.addWidget(self.pw_update_bt_2)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_25)
        self.gridLayout_10.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pw_saveOptions_lb_1 = QtGui.QLabel(self.tab_3)
        self.pw_saveOptions_lb_1.setMinimumSize(QtCore.QSize(150, 27))
        self.pw_saveOptions_lb_1.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_1.setFont(font)
        self.pw_saveOptions_lb_1.setObjectName(_fromUtf8("pw_saveOptions_lb_1"))
        self.horizontalLayout_3.addWidget(self.pw_saveOptions_lb_1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem11 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.pw_saveOptions_lb_2 = QtGui.QLabel(self.tab_3)
        self.pw_saveOptions_lb_2.setMinimumSize(QtCore.QSize(70, 27))
        self.pw_saveOptions_lb_2.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_2.setFont(font)
        self.pw_saveOptions_lb_2.setObjectName(_fromUtf8("pw_saveOptions_lb_2"))
        self.horizontalLayout_4.addWidget(self.pw_saveOptions_lb_2)
        self.pw_saveOptions_ln_1 = QtGui.QLineEdit(self.tab_3)
        self.pw_saveOptions_ln_1.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_1.setMaximumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_1.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_saveOptions_ln_1.setObjectName(_fromUtf8("pw_saveOptions_ln_1"))
        self.horizontalLayout_4.addWidget(self.pw_saveOptions_ln_1)
        self.pw_saveOptions_cb_1 = QtGui.QComboBox(self.tab_3)
        self.pw_saveOptions_cb_1.setMinimumSize(QtCore.QSize(130, 27))
        self.pw_saveOptions_cb_1.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_cb_1.setFont(font)
        self.pw_saveOptions_cb_1.setStyleSheet(_fromUtf8("QComboBox {\n"
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
        self.pw_saveOptions_cb_1.setObjectName(_fromUtf8("pw_saveOptions_cb_1"))
        self.pw_saveOptions_cb_1.addItem(_fromUtf8(""))
        self.pw_saveOptions_cb_1.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.pw_saveOptions_cb_1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem13 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.pw_saveOptions_lb_3 = QtGui.QLabel(self.tab_3)
        self.pw_saveOptions_lb_3.setMinimumSize(QtCore.QSize(70, 27))
        self.pw_saveOptions_lb_3.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_3.setFont(font)
        self.pw_saveOptions_lb_3.setObjectName(_fromUtf8("pw_saveOptions_lb_3"))
        self.horizontalLayout_5.addWidget(self.pw_saveOptions_lb_3)
        self.pw_saveOptions_ln_2 = QtGui.QLineEdit(self.tab_3)
        self.pw_saveOptions_ln_2.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_2.setMaximumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_2.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_saveOptions_ln_2.setObjectName(_fromUtf8("pw_saveOptions_ln_2"))
        self.horizontalLayout_5.addWidget(self.pw_saveOptions_ln_2)
        self.pw_saveOptions_cb_2 = QtGui.QComboBox(self.tab_3)
        self.pw_saveOptions_cb_2.setMinimumSize(QtCore.QSize(130, 27))
        self.pw_saveOptions_cb_2.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_cb_2.setFont(font)
        self.pw_saveOptions_cb_2.setStyleSheet(_fromUtf8("QComboBox {\n"
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
        self.pw_saveOptions_cb_2.setObjectName(_fromUtf8("pw_saveOptions_cb_2"))
        self.pw_saveOptions_cb_2.addItem(_fromUtf8(""))
        self.pw_saveOptions_cb_2.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.pw_saveOptions_cb_2)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem15 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem15)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pw_saveOptions_lb_4 = QtGui.QLabel(self.tab_3)
        self.pw_saveOptions_lb_4.setMinimumSize(QtCore.QSize(150, 27))
        self.pw_saveOptions_lb_4.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_4.setFont(font)
        self.pw_saveOptions_lb_4.setObjectName(_fromUtf8("pw_saveOptions_lb_4"))
        self.horizontalLayout_7.addWidget(self.pw_saveOptions_lb_4)
        self.pw_saveOptions_ln_3 = QtGui.QLineEdit(self.tab_3)
        self.pw_saveOptions_ln_3.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_3.setMaximumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_3.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}"))
        self.pw_saveOptions_ln_3.setObjectName(_fromUtf8("pw_saveOptions_ln_3"))
        self.horizontalLayout_7.addWidget(self.pw_saveOptions_ln_3)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem17 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem17)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pw_saveOptions_lb_5 = QtGui.QLabel(self.tab_3)
        self.pw_saveOptions_lb_5.setMinimumSize(QtCore.QSize(210, 27))
        self.pw_saveOptions_lb_5.setMaximumSize(QtCore.QSize(210, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_5.setFont(font)
        self.pw_saveOptions_lb_5.setObjectName(_fromUtf8("pw_saveOptions_lb_5"))
        self.horizontalLayout_8.addWidget(self.pw_saveOptions_lb_5)
        self.pw_saveOptions_ck_1 = QtGui.QCheckBox(self.tab_3)
        self.pw_saveOptions_ck_1.setMinimumSize(QtCore.QSize(25, 20))
        self.pw_saveOptions_ck_1.setMaximumSize(QtCore.QSize(25, 20))
        self.pw_saveOptions_ck_1.setText(_fromUtf8(""))
        self.pw_saveOptions_ck_1.setObjectName(_fromUtf8("pw_saveOptions_ck_1"))
        self.pw_saveOptions_ck_1.setStyleSheet(_fromUtf8("QCheckBox {\n"
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
        "}"))
        self.horizontalLayout_8.addWidget(self.pw_saveOptions_ck_1)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem19)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(plotWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(_translate("plotWindow", "Data Plot", None))
        self.pw_label_1.setText(_translate("plotWindow", "Please choose the type of graphs", None))
        self.pw_single_rd.setText(_translate("plotWindow", "Single plot", None))
        self.pw_multiple_rd.setText(_translate("plotWindow", "Multiple plots", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("plotWindow", "Plot window", None))
        self.pw_update_bt_1.setText(_translate("plotWindow", "Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("plotWindow", "Figure options", None))
        self.pw_update_bt_2.setText(_translate("plotWindow", "Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("plotWindow", "Plot options", None))
        self.pw_saveOptions_lb_1.setText(_translate("plotWindow", "Figure dimensions:", None))
        self.pw_saveOptions_lb_2.setText(_translate("plotWindow", "height:", None))
        self.pw_saveOptions_cb_1.setItemText(0, _translate("plotWindow", "Centimeters", None))
        self.pw_saveOptions_cb_1.setItemText(1, _translate("plotWindow", "Inches", None))
        self.pw_saveOptions_lb_3.setText(_translate("plotWindow", "width:", None))
        self.pw_saveOptions_cb_2.setItemText(0, _translate("plotWindow", "Centimeters", None))
        self.pw_saveOptions_cb_2.setItemText(1, _translate("plotWindow", "Inches", None))
        self.pw_saveOptions_lb_4.setText(_translate("plotWindow", "Figure resolution:", None))
        self.pw_saveOptions_lb_5.setText(_translate("plotWindow", "Transparent background ?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("plotWindow", "Save options", None))

