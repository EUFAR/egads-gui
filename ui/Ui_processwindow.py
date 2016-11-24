# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process_window.ui'
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

class Ui_processingWindow(object):
    def setupUi(self, processingWindow):
        processingWindow.setObjectName(_fromUtf8("processingWindow"))
        processingWindow.resize(700, 450)
        processingWindow.setMinimumSize(QtCore.QSize(700, 450))
        processingWindow.setMaximumSize(QtCore.QSize(700, 450))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        processingWindow.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(processingWindow)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(processingWindow)
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
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.al_label_1 = QtGui.QLabel(self.tab)
        self.al_label_1.setMinimumSize(QtCore.QSize(630, 27))
        self.al_label_1.setMaximumSize(QtCore.QSize(800, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_label_1.setFont(font)
        self.al_label_1.setWordWrap(True)
        self.al_label_1.setObjectName(_fromUtf8("al_label_1"))
        self.verticalLayout_5.addWidget(self.al_label_1)
        spacerItem = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.al_label_2 = QtGui.QLabel(self.tab)
        self.al_label_2.setEnabled(True)
        self.al_label_2.setMinimumSize(QtCore.QSize(90, 27))
        self.al_label_2.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_label_2.setFont(font)
        self.al_label_2.setObjectName(_fromUtf8("al_label_2"))
        self.horizontalLayout_4.addWidget(self.al_label_2)
        self.al_combobox_1 = QtGui.QComboBox(self.tab)
        self.al_combobox_1.setMinimumSize(QtCore.QSize(160, 27))
        self.al_combobox_1.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_combobox_1.setFont(font)
        self.al_combobox_1.setStyleSheet(_fromUtf8("QComboBox {\n"
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
"    padding: 4px 1px 4px 1px;\n"
"}"))
        self.al_combobox_1.setFrame(False)
        self.al_combobox_1.setObjectName(_fromUtf8("al_combobox_1"))
        self.horizontalLayout_4.addWidget(self.al_combobox_1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.al_label_3 = QtGui.QLabel(self.tab)
        self.al_label_3.setMinimumSize(QtCore.QSize(90, 27))
        self.al_label_3.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_label_3.setFont(font)
        self.al_label_3.setObjectName(_fromUtf8("al_label_3"))
        self.horizontalLayout_5.addWidget(self.al_label_3)
        self.al_combobox_2 = QtGui.QComboBox(self.tab)
        self.al_combobox_2.setEnabled(False)
        self.al_combobox_2.setMinimumSize(QtCore.QSize(200, 27))
        self.al_combobox_2.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_combobox_2.setFont(font)
        self.al_combobox_2.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.al_combobox_2.setFrame(False)
        self.al_combobox_2.setObjectName(_fromUtf8("al_combobox_2"))
        self.horizontalLayout_5.addWidget(self.al_combobox_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.al_label_6 = QtGui.QLabel(self.tab)
        self.al_label_6.setMinimumSize(QtCore.QSize(100, 27))
        self.al_label_6.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_label_6.setFont(font)
        self.al_label_6.setObjectName(_fromUtf8("al_label_6"))
        self.verticalLayout.addWidget(self.al_label_6)
        spacerItem4 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.al_textBrowser_1 = QtGui.QTextBrowser(self.tab)
        self.al_textBrowser_1.setMinimumSize(QtCore.QSize(500, 60))
        self.al_textBrowser_1.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_textBrowser_1.setFont(font)
        self.al_textBrowser_1.setFrameShape(QtGui.QFrame.NoFrame)
        self.al_textBrowser_1.setObjectName(_fromUtf8("al_textBrowser_1"))
        self.horizontalLayout_3.addWidget(self.al_textBrowser_1)
        spacerItem5 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.al_label_7 = QtGui.QLabel(self.tab)
        self.al_label_7.setMinimumSize(QtCore.QSize(100, 27))
        self.al_label_7.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_label_7.setFont(font)
        self.al_label_7.setObjectName(_fromUtf8("al_label_7"))
        self.verticalLayout_6.addWidget(self.al_label_7)
        spacerItem6 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.al_textBrowser_2 = QtGui.QTextBrowser(self.tab)
        self.al_textBrowser_2.setMinimumSize(QtCore.QSize(500, 100))
        self.al_textBrowser_2.setMaximumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_textBrowser_2.setFont(font)
        self.al_textBrowser_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.al_textBrowser_2.setObjectName(_fromUtf8("al_textBrowser_2"))
        self.horizontalLayout_9.addWidget(self.al_textBrowser_2)
        spacerItem7 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        spacerItem8 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.al_label_4 = QtGui.QLabel(self.tab_2)
        self.al_label_4.setMinimumSize(QtCore.QSize(610, 27))
        self.al_label_4.setMaximumSize(QtCore.QSize(610, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_label_4.setFont(font)
        self.al_label_4.setWordWrap(True)
        self.al_label_4.setObjectName(_fromUtf8("al_label_4"))
        self.horizontalLayout_2.addWidget(self.al_label_4)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem10)
        self.scrollArea_3 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_3.setStyleSheet(_fromUtf8("QScrollArea { background: transparent; }\n"
        "\n"
        "QScrollArea > QWidget > QWidget { background: transparent; }\n"
        ))
        self.scrollArea_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 658, 256))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.input_layout = QtGui.QVBoxLayout()
        self.input_layout.setObjectName(_fromUtf8("input_layout"))
        self.gridLayout_6.addLayout(self.input_layout, 0, 0, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 181, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem11, 1, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.al_label_5 = QtGui.QLabel(self.tab_3)
        self.al_label_5.setMinimumSize(QtCore.QSize(610, 27))
        self.al_label_5.setMaximumSize(QtCore.QSize(610, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.al_label_5.setFont(font)
        self.al_label_5.setWordWrap(True)
        self.al_label_5.setObjectName(_fromUtf8("al_label_5"))
        self.horizontalLayout_6.addWidget(self.al_label_5)
        spacerItem12 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem13)
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_3)
        self.scrollArea_2.setAutoFillBackground(False)
        self.scrollArea_2.setStyleSheet(_fromUtf8("QScrollArea { background: transparent; }\n"
        "\n"
        "QScrollArea > QWidget > QWidget { background: transparent; }\n"
        ))
        self.scrollArea_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 658, 256))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.output_layout = QtGui.QVBoxLayout()
        self.output_layout.setObjectName(_fromUtf8("output_layout"))
        self.gridLayout_5.addLayout(self.output_layout, 0, 0, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(20, 181, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem14, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        spacerItem15 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem15)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem16 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.al_cancelButton = QtGui.QToolButton(processingWindow)
        self.al_cancelButton.setMinimumSize(QtCore.QSize(100, 27))
        self.al_cancelButton.setMaximumSize(QtCore.QSize(100, 27))
        self.al_cancelButton.setObjectName(_fromUtf8("al_cancelButton"))
        self.horizontalLayout.addWidget(self.al_cancelButton)
        spacerItem17 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.al_okButton = QtGui.QToolButton(processingWindow)
        self.al_okButton.setEnabled(False)
        self.al_okButton.setMinimumSize(QtCore.QSize(100, 27))
        self.al_okButton.setMaximumSize(QtCore.QSize(100, 27))
        self.al_okButton.setObjectName(_fromUtf8("al_okButton"))
        self.horizontalLayout.addWidget(self.al_okButton)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem18)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(processingWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(processingWindow)

    def retranslateUi(self, processingWindow):
        processingWindow.setWindowTitle(_translate("processingWindow", "Algorithms", None))
        self.al_label_1.setText(_translate("processingWindow", "<html><head/><body><p align=\"justify\">Please choose a category and an algorithm to begin the processing. Once it has been done, please proceed with the next step: Input(s).</p></body></html>", None))
        self.al_label_2.setText(_translate("processingWindow", "Category:", None))
        self.al_label_3.setText(_translate("processingWindow", "Algorithm:", None))
        self.al_label_6.setText(_translate("processingWindow", "Purpose:", None))
        self.al_textBrowser_1.setHtml(_translate("processingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'fonts/SourceSansPro-Regular.ttf\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.al_label_7.setText(_translate("processingWindow", "Description:", None))
        self.al_textBrowser_2.setHtml(_translate("processingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'fonts/SourceSansPro-Regular.ttf\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("processingWindow", "Choose an algorithm", None))
        self.al_label_4.setText(_translate("processingWindow", "<html><head/><body><p align=\"justify\">Please select the input(s). Once it has been done, please proceed with the next step: Output(s).</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("processingWindow", "Input(s)", None))
        self.al_label_5.setText(_translate("processingWindow", "<html><head/><body><p align=\"justify\">Please enter a variable name for the output(s). Once it has been done, please click on save to launch the processing.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("processingWindow", "Output(s)", None))
        self.al_cancelButton.setText(_translate("processingWindow", "Cancel", None))
        self.al_okButton.setText(_translate("processingWindow", "Save", None))

