# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_netcdf.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functions.gui_elements import PushButtonRight

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 544)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/egads_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 431))
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
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gm_filename_lb = QtWidgets.QLabel(self.tab)
        self.gm_filename_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_filename_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_filename_lb.setFont(font)
        self.gm_filename_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_filename_lb.setObjectName("gm_filename_lb")
        self.horizontalLayout.addWidget(self.gm_filename_lb)
        self.gm_filename_ln = QtWidgets.QLabel(self.tab)
        self.gm_filename_ln.setMinimumSize(QtCore.QSize(500, 27))
        self.gm_filename_ln.setMaximumSize(QtCore.QSize(500, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_filename_ln.setFont(font)
        self.gm_filename_ln.setText("")
        self.gm_filename_ln.setObjectName("gm_filename_ln")
        self.horizontalLayout.addWidget(self.gm_filename_ln)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gm_dateCreation_lb = QtWidgets.QLabel(self.tab)
        self.gm_dateCreation_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_dateCreation_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_dateCreation_lb.setFont(font)
        self.gm_dateCreation_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_dateCreation_lb.setObjectName("gm_dateCreation_lb")
        self.horizontalLayout.addWidget(self.gm_dateCreation_lb)
        self.gm_dateCreation_ln = QtWidgets.QLabel(self.tab)
        self.gm_dateCreation_ln.setMinimumSize(QtCore.QSize(150, 27))
        self.gm_dateCreation_ln.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_dateCreation_ln.setFont(font)
        self.gm_dateCreation_ln.setText("")
        self.gm_dateCreation_ln.setObjectName("gm_dateCreation_ln")
        self.horizontalLayout.addWidget(self.gm_dateCreation_ln)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(25)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gm_project_lb = QtWidgets.QLabel(self.tab)
        self.gm_project_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_project_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_project_lb.setFont(font)
        self.gm_project_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_project_lb.setObjectName("gm_project_lb")
        self.gridLayout_2.addWidget(self.gm_project_lb, 3, 0, 1, 1)
        self.gm_project_ln = QtWidgets.QLineEdit(self.tab)
        self.gm_project_ln.setEnabled(False)
        self.gm_project_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.gm_project_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.gm_project_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gm_project_ln.setFont(font)
        self.gm_project_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.gm_project_ln.setText("")
        self.gm_project_ln.setFrame(False)
        self.gm_project_ln.setObjectName("gm_project_ln")
        self.gridLayout_2.addWidget(self.gm_project_ln, 3, 1, 1, 1)
        self.gm_button_4 = PushButtonRight(self.tab)
        self.gm_button_4.setMinimumSize(QtCore.QSize(27, 27))
        self.gm_button_4.setMaximumSize(QtCore.QSize(27, 27))
        self.gm_button_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.gm_button_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gm_button_4.setIcon(icon1)
        self.gm_button_4.setIconSize(QtCore.QSize(23, 23))
        self.gm_button_4.setObjectName("gm_button_4")
        self.gridLayout_2.addWidget(self.gm_button_4, 3, 2, 1, 1)
        self.gm_title_lb = QtWidgets.QLabel(self.tab)
        self.gm_title_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_title_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_title_lb.setFont(font)
        self.gm_title_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_title_lb.setObjectName("gm_title_lb")
        self.gridLayout_2.addWidget(self.gm_title_lb, 0, 0, 1, 1)
        self.gm_institution_lb = QtWidgets.QLabel(self.tab)
        self.gm_institution_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_institution_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_institution_lb.setFont(font)
        self.gm_institution_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_institution_lb.setObjectName("gm_institution_lb")
        self.gridLayout_2.addWidget(self.gm_institution_lb, 1, 0, 1, 1)
        self.gm_title_ln = QtWidgets.QLineEdit(self.tab)
        self.gm_title_ln.setEnabled(False)
        self.gm_title_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.gm_title_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.gm_title_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gm_title_ln.setFont(font)
        self.gm_title_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.gm_title_ln.setText("")
        self.gm_title_ln.setFrame(False)
        self.gm_title_ln.setObjectName("gm_title_ln")
        self.gridLayout_2.addWidget(self.gm_title_ln, 0, 1, 1, 1)
        self.gm_button_1 = PushButtonRight(self.tab)
        self.gm_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.gm_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.gm_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.gm_button_1.setText("")
        self.gm_button_1.setIcon(icon1)
        self.gm_button_1.setIconSize(QtCore.QSize(23, 23))
        self.gm_button_1.setObjectName("gm_button_1")
        self.gridLayout_2.addWidget(self.gm_button_1, 0, 2, 1, 1)
        self.gm_source_lb = QtWidgets.QLabel(self.tab)
        self.gm_source_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_source_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_source_lb.setFont(font)
        self.gm_source_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_source_lb.setObjectName("gm_source_lb")
        self.gridLayout_2.addWidget(self.gm_source_lb, 2, 0, 1, 1)
        self.gm_source_ln = QtWidgets.QLineEdit(self.tab)
        self.gm_source_ln.setEnabled(False)
        self.gm_source_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.gm_source_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.gm_source_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gm_source_ln.setFont(font)
        self.gm_source_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.gm_source_ln.setText("")
        self.gm_source_ln.setFrame(False)
        self.gm_source_ln.setObjectName("gm_source_ln")
        self.gridLayout_2.addWidget(self.gm_source_ln, 2, 1, 1, 1)
        self.gm_button_3 = PushButtonRight(self.tab)
        self.gm_button_3.setMinimumSize(QtCore.QSize(27, 27))
        self.gm_button_3.setMaximumSize(QtCore.QSize(27, 27))
        self.gm_button_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.gm_button_3.setText("")
        self.gm_button_3.setIcon(icon1)
        self.gm_button_3.setIconSize(QtCore.QSize(23, 23))
        self.gm_button_3.setObjectName("gm_button_3")
        self.gridLayout_2.addWidget(self.gm_button_3, 2, 2, 1, 1)
        self.gm_button_2 = PushButtonRight(self.tab)
        self.gm_button_2.setMinimumSize(QtCore.QSize(27, 27))
        self.gm_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.gm_button_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.gm_button_2.setText("")
        self.gm_button_2.setIcon(icon1)
        self.gm_button_2.setIconSize(QtCore.QSize(23, 23))
        self.gm_button_2.setObjectName("gm_button_2")
        self.gridLayout_2.addWidget(self.gm_button_2, 1, 2, 1, 1)
        self.gm_institution_ln = QtWidgets.QLineEdit(self.tab)
        self.gm_institution_ln.setEnabled(False)
        self.gm_institution_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.gm_institution_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.gm_institution_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gm_institution_ln.setFont(font)
        self.gm_institution_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.gm_institution_ln.setText("")
        self.gm_institution_ln.setFrame(False)
        self.gm_institution_ln.setObjectName("gm_institution_ln")
        self.gridLayout_2.addWidget(self.gm_institution_ln, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gm_history_lb = QtWidgets.QLabel(self.tab)
        self.gm_history_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_history_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_history_lb.setFont(font)
        self.gm_history_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_history_lb.setObjectName("gm_history_lb")
        self.verticalLayout.addWidget(self.gm_history_lb)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gm_history_ln = QtWidgets.QPlainTextEdit(self.tab)
        self.gm_history_ln.setEnabled(False)
        self.gm_history_ln.setMinimumSize(QtCore.QSize(400, 150))
        self.gm_history_ln.setMaximumSize(QtCore.QSize(16777215, 150))
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
        self.gm_history_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gm_history_ln.setFont(font)
        self.gm_history_ln.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QPlainTextEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.gm_history_ln.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gm_history_ln.setPlainText("")
        self.gm_history_ln.setObjectName("gm_history_ln")
        self.horizontalLayout_2.addWidget(self.gm_history_ln)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gm_button_5 = PushButtonRight(self.tab)
        self.gm_button_5.setMinimumSize(QtCore.QSize(27, 27))
        self.gm_button_5.setMaximumSize(QtCore.QSize(27, 27))
        self.gm_button_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.gm_button_5.setText("")
        self.gm_button_5.setIcon(icon1)
        self.gm_button_5.setIconSize(QtCore.QSize(23, 23))
        self.gm_button_5.setObjectName("gm_button_5")
        self.verticalLayout_2.addWidget(self.gm_button_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gm_history_lb_2 = QtWidgets.QLabel(self.tab)
        self.gm_history_lb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.gm_history_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.gm_history_lb_2.setFont(font)
        self.gm_history_lb_2.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_history_lb_2.setObjectName("gm_history_lb_2")
        self.verticalLayout_9.addWidget(self.gm_history_lb_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.gm_history_ln_2 = QtWidgets.QPlainTextEdit(self.tab)
        self.gm_history_ln_2.setEnabled(False)
        self.gm_history_ln_2.setMinimumSize(QtCore.QSize(400, 150))
        self.gm_history_ln_2.setMaximumSize(QtCore.QSize(16777215, 150))
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
        self.gm_history_ln_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gm_history_ln_2.setFont(font)
        self.gm_history_ln_2.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QPlainTextEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.gm_history_ln_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gm_history_ln_2.setPlainText("")
        self.gm_history_ln_2.setObjectName("gm_history_ln_2")
        self.horizontalLayout_6.addWidget(self.gm_history_ln_2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gm_button_6 = PushButtonRight(self.tab)
        self.gm_button_6.setMinimumSize(QtCore.QSize(27, 27))
        self.gm_button_6.setMaximumSize(QtCore.QSize(27, 27))
        self.gm_button_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.gm_button_6.setText("")
        self.gm_button_6.setIcon(icon1)
        self.gm_button_6.setIconSize(QtCore.QSize(23, 23))
        self.gm_button_6.setObjectName("gm_button_6")
        self.verticalLayout_10.addWidget(self.gm_button_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem11)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_11.addItem(spacerItem13)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gm_compatibility_lb = QtWidgets.QLabel(self.tab)
        self.gm_compatibility_lb.setEnabled(False)
        self.gm_compatibility_lb.setMinimumSize(QtCore.QSize(23, 23))
        self.gm_compatibility_lb.setMaximumSize(QtCore.QSize(23, 23))
        self.gm_compatibility_lb.setText("")
        self.gm_compatibility_lb.setPixmap(QtGui.QPixmap("icons/none_icon.png"))
        self.gm_compatibility_lb.setScaledContents(True)
        self.gm_compatibility_lb.setObjectName("gm_compatibility_lb")
        self.horizontalLayout_9.addWidget(self.gm_compatibility_lb)
        self.gm_details_lb = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gm_details_lb.sizePolicy().hasHeightForWidth())
        self.gm_details_lb.setSizePolicy(sizePolicy)
        self.gm_details_lb.setMinimumSize(QtCore.QSize(941, 35))
        self.gm_details_lb.setMaximumSize(QtCore.QSize(941, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(8)
        self.gm_details_lb.setFont(font)
        self.gm_details_lb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gm_details_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.gm_details_lb.setText("")
        self.gm_details_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gm_details_lb.setWordWrap(True)
        self.gm_details_lb.setObjectName("gm_details_lb")
        self.horizontalLayout_9.addWidget(self.gm_details_lb)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.gm_button_7 = QtWidgets.QToolButton(self.tab)
        self.gm_button_7.setEnabled(False)
        self.gm_button_7.setMinimumSize(QtCore.QSize(27, 27))
        self.gm_button_7.setMaximumSize(QtCore.QSize(27, 27))
        self.gm_button_7.setStyleSheet("QToolButton {\n"
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
        self.gm_button_7.setIcon(icon2)
        self.gm_button_7.setIconSize(QtCore.QSize(23, 23))
        self.gm_button_7.setObjectName("gm_button_7")
        self.horizontalLayout_9.addWidget(self.gm_button_7)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.gridLayout_4.addLayout(self.verticalLayout_11, 1, 1, 2, 1)
        spacerItem16 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem16, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem17, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setMinimumSize(QtCore.QSize(400, 328))
        self.listWidget.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: black;\n"
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
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.va_varName_lb = QtWidgets.QLabel(self.tab_2)
        self.va_varName_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.va_varName_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_varName_lb.setFont(font)
        self.va_varName_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.va_varName_lb.setObjectName("va_varName_lb")
        self.gridLayout_3.addWidget(self.va_varName_lb, 0, 0, 1, 1)
        self.va_varName_ln = QtWidgets.QLineEdit(self.tab_2)
        self.va_varName_ln.setEnabled(False)
        self.va_varName_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.va_varName_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.va_varName_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_varName_ln.setFont(font)
        self.va_varName_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.va_varName_ln.setText("")
        self.va_varName_ln.setFrame(False)
        self.va_varName_ln.setObjectName("va_varName_ln")
        self.gridLayout_3.addWidget(self.va_varName_ln, 0, 1, 1, 1)
        self.va_button_1 = PushButtonRight(self.tab_2)
        self.va_button_1.setEnabled(False)
        self.va_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.va_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.va_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.va_button_1.setText("")
        self.va_button_1.setIcon(icon1)
        self.va_button_1.setIconSize(QtCore.QSize(23, 23))
        self.va_button_1.setObjectName("va_button_1")
        self.gridLayout_3.addWidget(self.va_button_1, 0, 2, 1, 1)
        self.va_longName_lb = QtWidgets.QLabel(self.tab_2)
        self.va_longName_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.va_longName_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_longName_lb.setFont(font)
        self.va_longName_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.va_longName_lb.setObjectName("va_longName_lb")
        self.gridLayout_3.addWidget(self.va_longName_lb, 1, 0, 1, 1)
        self.va_longName_ln = QtWidgets.QLineEdit(self.tab_2)
        self.va_longName_ln.setEnabled(False)
        self.va_longName_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.va_longName_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.va_longName_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_longName_ln.setFont(font)
        self.va_longName_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.va_longName_ln.setText("")
        self.va_longName_ln.setFrame(False)
        self.va_longName_ln.setObjectName("va_longName_ln")
        self.gridLayout_3.addWidget(self.va_longName_ln, 1, 1, 1, 1)
        self.va_button_2 = PushButtonRight(self.tab_2)
        self.va_button_2.setEnabled(False)
        self.va_button_2.setMinimumSize(QtCore.QSize(27, 27))
        self.va_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.va_button_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.va_button_2.setText("")
        self.va_button_2.setIcon(icon1)
        self.va_button_2.setIconSize(QtCore.QSize(23, 23))
        self.va_button_2.setObjectName("va_button_2")
        self.gridLayout_3.addWidget(self.va_button_2, 1, 2, 1, 1)
        self.va_category_lb = QtWidgets.QLabel(self.tab_2)
        self.va_category_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.va_category_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_category_lb.setFont(font)
        self.va_category_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.va_category_lb.setObjectName("va_category_lb")
        self.gridLayout_3.addWidget(self.va_category_lb, 2, 0, 1, 1)
        self.va_category_ln = QtWidgets.QLineEdit(self.tab_2)
        self.va_category_ln.setEnabled(False)
        self.va_category_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.va_category_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.va_category_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_category_ln.setFont(font)
        self.va_category_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.va_category_ln.setText("")
        self.va_category_ln.setFrame(False)
        self.va_category_ln.setObjectName("va_category_ln")
        self.gridLayout_3.addWidget(self.va_category_ln, 2, 1, 1, 1)
        self.va_button_3 = PushButtonRight(self.tab_2)
        self.va_button_3.setEnabled(False)
        self.va_button_3.setMinimumSize(QtCore.QSize(27, 27))
        self.va_button_3.setMaximumSize(QtCore.QSize(27, 27))
        self.va_button_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.va_button_3.setText("")
        self.va_button_3.setIcon(icon1)
        self.va_button_3.setIconSize(QtCore.QSize(23, 23))
        self.va_button_3.setObjectName("va_button_3")
        self.gridLayout_3.addWidget(self.va_button_3, 2, 2, 1, 1)
        self.va_units_lb = QtWidgets.QLabel(self.tab_2)
        self.va_units_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.va_units_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_units_lb.setFont(font)
        self.va_units_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.va_units_lb.setObjectName("va_units_lb")
        self.gridLayout_3.addWidget(self.va_units_lb, 3, 0, 1, 1)
        self.va_units_ln = QtWidgets.QLineEdit(self.tab_2)
        self.va_units_ln.setEnabled(False)
        self.va_units_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.va_units_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.va_units_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_units_ln.setFont(font)
        self.va_units_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.va_units_ln.setText("")
        self.va_units_ln.setFrame(False)
        self.va_units_ln.setObjectName("va_units_ln")
        self.gridLayout_3.addWidget(self.va_units_ln, 3, 1, 1, 1)
        self.va_button_4 = PushButtonRight(self.tab_2)
        self.va_button_4.setEnabled(False)
        self.va_button_4.setMinimumSize(QtCore.QSize(27, 27))
        self.va_button_4.setMaximumSize(QtCore.QSize(27, 27))
        self.va_button_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.va_button_4.setText("")
        self.va_button_4.setIcon(icon1)
        self.va_button_4.setIconSize(QtCore.QSize(23, 23))
        self.va_button_4.setObjectName("va_button_4")
        self.gridLayout_3.addWidget(self.va_button_4, 3, 2, 1, 1)
        self.va_fillValue_lb = QtWidgets.QLabel(self.tab_2)
        self.va_fillValue_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.va_fillValue_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_fillValue_lb.setFont(font)
        self.va_fillValue_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.va_fillValue_lb.setObjectName("va_fillValue_lb")
        self.gridLayout_3.addWidget(self.va_fillValue_lb, 4, 0, 1, 1)
        self.va_fillValue_ln = QtWidgets.QLabel(self.tab_2)
        self.va_fillValue_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.va_fillValue_ln.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_fillValue_ln.setFont(font)
        self.va_fillValue_ln.setText("")
        self.va_fillValue_ln.setObjectName("va_fillValue_ln")
        self.gridLayout_3.addWidget(self.va_fillValue_ln, 4, 1, 1, 1)
        self.va_dimensions_lb = QtWidgets.QLabel(self.tab_2)
        self.va_dimensions_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.va_dimensions_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_dimensions_lb.setFont(font)
        self.va_dimensions_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.va_dimensions_lb.setObjectName("va_dimensions_lb")
        self.gridLayout_3.addWidget(self.va_dimensions_lb, 5, 0, 1, 1)
        self.va_dimensions_ln = QtWidgets.QLabel(self.tab_2)
        self.va_dimensions_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.va_dimensions_ln.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_dimensions_ln.setFont(font)
        self.va_dimensions_ln.setText("")
        self.va_dimensions_ln.setObjectName("va_dimensions_ln")
        self.gridLayout_3.addWidget(self.va_dimensions_ln, 5, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.va_egadsProcessor_lb = QtWidgets.QLabel(self.tab_2)
        self.va_egadsProcessor_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.va_egadsProcessor_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_egadsProcessor_lb.setFont(font)
        self.va_egadsProcessor_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.va_egadsProcessor_lb.setObjectName("va_egadsProcessor_lb")
        self.verticalLayout_4.addWidget(self.va_egadsProcessor_lb)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem18)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 6, 0, 1, 1)
        self.va_egadsProcessor_ln = QtWidgets.QPlainTextEdit(self.tab_2)
        self.va_egadsProcessor_ln.setEnabled(False)
        self.va_egadsProcessor_ln.setMinimumSize(QtCore.QSize(400, 100))
        self.va_egadsProcessor_ln.setMaximumSize(QtCore.QSize(16777215, 100))
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
        self.va_egadsProcessor_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.va_egadsProcessor_ln.setFont(font)
        self.va_egadsProcessor_ln.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QPlainTextEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.va_egadsProcessor_ln.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.va_egadsProcessor_ln.setPlainText("")
        self.va_egadsProcessor_ln.setObjectName("va_egadsProcessor_ln")
        self.gridLayout_3.addWidget(self.va_egadsProcessor_ln, 6, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        spacerItem19 = QtWidgets.QSpacerItem(28, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem19)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 1, 2, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem20, 2, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem21, 3, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem22, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem23, 1, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem24, 1, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.new_listwidget = QtWidgets.QListWidget(self.tab_3)
        self.new_listwidget.setMinimumSize(QtCore.QSize(400, 328))
        self.new_listwidget.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_listwidget.setFont(font)
        self.new_listwidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: black;\n"
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
"}")
        self.new_listwidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.new_listwidget.setObjectName("new_listwidget")
        self.horizontalLayout_5.addWidget(self.new_listwidget)
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.new_varName_lb = QtWidgets.QLabel(self.tab_3)
        self.new_varName_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.new_varName_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_varName_lb.setFont(font)
        self.new_varName_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.new_varName_lb.setObjectName("new_varName_lb")
        self.gridLayout_6.addWidget(self.new_varName_lb, 0, 0, 1, 1)
        self.new_varName_ln = QtWidgets.QLineEdit(self.tab_3)
        self.new_varName_ln.setEnabled(False)
        self.new_varName_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.new_varName_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.new_varName_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_varName_ln.setFont(font)
        self.new_varName_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.new_varName_ln.setText("")
        self.new_varName_ln.setFrame(False)
        self.new_varName_ln.setObjectName("new_varName_ln")
        self.gridLayout_6.addWidget(self.new_varName_ln, 0, 1, 1, 1)
        self.new_button_1 = PushButtonRight(self.tab_3)
        self.new_button_1.setEnabled(False)
        self.new_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.new_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.new_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.new_button_1.setText("")
        self.new_button_1.setIcon(icon1)
        self.new_button_1.setIconSize(QtCore.QSize(23, 23))
        self.new_button_1.setObjectName("new_button_1")
        self.gridLayout_6.addWidget(self.new_button_1, 0, 2, 1, 1)
        self.new_longName_lb = QtWidgets.QLabel(self.tab_3)
        self.new_longName_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.new_longName_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_longName_lb.setFont(font)
        self.new_longName_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.new_longName_lb.setObjectName("new_longName_lb")
        self.gridLayout_6.addWidget(self.new_longName_lb, 1, 0, 1, 1)
        self.new_longName_ln = QtWidgets.QLineEdit(self.tab_3)
        self.new_longName_ln.setEnabled(False)
        self.new_longName_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.new_longName_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.new_longName_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_longName_ln.setFont(font)
        self.new_longName_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.new_longName_ln.setText("")
        self.new_longName_ln.setFrame(False)
        self.new_longName_ln.setObjectName("new_longName_ln")
        self.gridLayout_6.addWidget(self.new_longName_ln, 1, 1, 1, 1)
        self.new_button_2 = PushButtonRight(self.tab_3)
        self.new_button_2.setEnabled(False)
        self.new_button_2.setMinimumSize(QtCore.QSize(27, 27))
        self.new_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.new_button_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.new_button_2.setText("")
        self.new_button_2.setIcon(icon1)
        self.new_button_2.setIconSize(QtCore.QSize(23, 23))
        self.new_button_2.setObjectName("new_button_2")
        self.gridLayout_6.addWidget(self.new_button_2, 1, 2, 1, 1)
        self.new_category_lb = QtWidgets.QLabel(self.tab_3)
        self.new_category_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.new_category_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_category_lb.setFont(font)
        self.new_category_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.new_category_lb.setObjectName("new_category_lb")
        self.gridLayout_6.addWidget(self.new_category_lb, 2, 0, 1, 1)
        self.new_category_ln = QtWidgets.QLineEdit(self.tab_3)
        self.new_category_ln.setEnabled(False)
        self.new_category_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.new_category_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.new_category_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_category_ln.setFont(font)
        self.new_category_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.new_category_ln.setText("")
        self.new_category_ln.setFrame(False)
        self.new_category_ln.setObjectName("new_category_ln")
        self.gridLayout_6.addWidget(self.new_category_ln, 2, 1, 1, 1)
        self.new_button_3 = PushButtonRight(self.tab_3)
        self.new_button_3.setEnabled(False)
        self.new_button_3.setMinimumSize(QtCore.QSize(27, 27))
        self.new_button_3.setMaximumSize(QtCore.QSize(27, 27))
        self.new_button_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.new_button_3.setText("")
        self.new_button_3.setIcon(icon1)
        self.new_button_3.setIconSize(QtCore.QSize(23, 23))
        self.new_button_3.setObjectName("new_button_3")
        self.gridLayout_6.addWidget(self.new_button_3, 2, 2, 1, 1)
        self.new_units_lb = QtWidgets.QLabel(self.tab_3)
        self.new_units_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.new_units_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_units_lb.setFont(font)
        self.new_units_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.new_units_lb.setObjectName("new_units_lb")
        self.gridLayout_6.addWidget(self.new_units_lb, 3, 0, 1, 1)
        self.new_units_ln = QtWidgets.QLineEdit(self.tab_3)
        self.new_units_ln.setEnabled(False)
        self.new_units_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.new_units_ln.setMaximumSize(QtCore.QSize(16777215, 27))
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
        self.new_units_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_units_ln.setFont(font)
        self.new_units_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}")
        self.new_units_ln.setText("")
        self.new_units_ln.setFrame(False)
        self.new_units_ln.setObjectName("new_units_ln")
        self.gridLayout_6.addWidget(self.new_units_ln, 3, 1, 1, 1)
        self.new_button_4 = PushButtonRight(self.tab_3)
        self.new_button_4.setEnabled(False)
        self.new_button_4.setMinimumSize(QtCore.QSize(27, 27))
        self.new_button_4.setMaximumSize(QtCore.QSize(27, 27))
        self.new_button_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.new_button_4.setText("")
        self.new_button_4.setIcon(icon1)
        self.new_button_4.setIconSize(QtCore.QSize(23, 23))
        self.new_button_4.setObjectName("new_button_4")
        self.gridLayout_6.addWidget(self.new_button_4, 3, 2, 1, 1)
        self.new_fillValue_lb = QtWidgets.QLabel(self.tab_3)
        self.new_fillValue_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.new_fillValue_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_fillValue_lb.setFont(font)
        self.new_fillValue_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.new_fillValue_lb.setObjectName("new_fillValue_lb")
        self.gridLayout_6.addWidget(self.new_fillValue_lb, 4, 0, 1, 1)
        self.new_fillValue_ln = QtWidgets.QLabel(self.tab_3)
        self.new_fillValue_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.new_fillValue_ln.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_fillValue_ln.setFont(font)
        self.new_fillValue_ln.setText("")
        self.new_fillValue_ln.setObjectName("new_fillValue_ln")
        self.gridLayout_6.addWidget(self.new_fillValue_ln, 4, 1, 1, 1)
        self.new_dimensions_lb = QtWidgets.QLabel(self.tab_3)
        self.new_dimensions_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.new_dimensions_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_dimensions_lb.setFont(font)
        self.new_dimensions_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.new_dimensions_lb.setObjectName("new_dimensions_lb")
        self.gridLayout_6.addWidget(self.new_dimensions_lb, 5, 0, 1, 1)
        self.new_dimensions_ln = QtWidgets.QLabel(self.tab_3)
        self.new_dimensions_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.new_dimensions_ln.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_dimensions_ln.setFont(font)
        self.new_dimensions_ln.setText("")
        self.new_dimensions_ln.setObjectName("new_dimensions_ln")
        self.gridLayout_6.addWidget(self.new_dimensions_ln, 5, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.new_egadsProcessor_lb = QtWidgets.QLabel(self.tab_3)
        self.new_egadsProcessor_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.new_egadsProcessor_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_egadsProcessor_lb.setFont(font)
        self.new_egadsProcessor_lb.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.new_egadsProcessor_lb.setObjectName("new_egadsProcessor_lb")
        self.verticalLayout_6.addWidget(self.new_egadsProcessor_lb)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem25)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 6, 0, 1, 1)
        self.new_egadsProcessor_ln = QtWidgets.QPlainTextEdit(self.tab_3)
        self.new_egadsProcessor_ln.setEnabled(False)
        self.new_egadsProcessor_ln.setMinimumSize(QtCore.QSize(400, 100))
        self.new_egadsProcessor_ln.setMaximumSize(QtCore.QSize(16777215, 100))
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
        self.new_egadsProcessor_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.new_egadsProcessor_ln.setFont(font)
        self.new_egadsProcessor_ln.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}\n"
"    \n"
"QPlainTextEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.new_egadsProcessor_ln.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.new_egadsProcessor_ln.setPlainText("")
        self.new_egadsProcessor_ln.setObjectName("new_egadsProcessor_ln")
        self.gridLayout_6.addWidget(self.new_egadsProcessor_ln, 6, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_6)
        spacerItem26 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem26)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.gridLayout_7.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem27, 2, 1, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem28, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1190, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuProcessings = QtWidgets.QMenu(self.menuBar)
        self.menuProcessings.setObjectName("menuProcessings")
        self.menuEmbedded_algorithms = QtWidgets.QMenu(self.menuProcessings)
        self.menuEmbedded_algorithms.setObjectName("menuEmbedded_algorithms")
        self.menuUser_defined_algorithms = QtWidgets.QMenu(self.menuProcessings)
        self.menuUser_defined_algorithms.setObjectName("menuUser_defined_algorithms")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.toolBar.setFont(font)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(28, 28))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpenBar = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenBar.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOpenBar.setFont(font)
        self.actionOpenBar.setObjectName("actionOpenBar")
        self.actionSaveBar = QtWidgets.QAction(MainWindow)
        self.actionSaveBar.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/save_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveBar.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSaveBar.setFont(font)
        self.actionSaveBar.setObjectName("actionSaveBar")
        self.actionCloseBar = QtWidgets.QAction(MainWindow)
        self.actionCloseBar.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/off_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseBar.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionCloseBar.setFont(font)
        self.actionCloseBar.setObjectName("actionCloseBar")
        self.actionAlgorithmsBar = QtWidgets.QAction(MainWindow)
        self.actionAlgorithmsBar.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/new_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlgorithmsBar.setIcon(icon6)
        self.actionAlgorithmsBar.setObjectName("actionAlgorithmsBar")
        self.actionCreatealgorithmBar = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/create_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreatealgorithmBar.setIcon(icon7)
        self.actionCreatealgorithmBar.setObjectName("actionCreatealgorithmBar")
        self.actionCreateVariableBar = QtWidgets.QAction(MainWindow)
        self.actionCreateVariableBar.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/new_var_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreateVariableBar.setIcon(icon8)
        self.actionCreateVariableBar.setObjectName("actionCreateVariableBar")
        self.actionMigrateVariableBar = QtWidgets.QAction(MainWindow)
        self.actionMigrateVariableBar.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/migrate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMigrateVariableBar.setIcon(icon9)
        self.actionMigrateVariableBar.setObjectName("actionMigrateVariableBar")
        self.actionDeleteVariableBar = QtWidgets.QAction(MainWindow)
        self.actionDeleteVariableBar.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteVariableBar.setIcon(icon10)
        self.actionDeleteVariableBar.setObjectName("actionDeleteVariableBar")
        self.actionGlobalAttributesBar = QtWidgets.QAction(MainWindow)
        self.actionGlobalAttributesBar.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/glo_metadata_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGlobalAttributesBar.setIcon(icon11)
        self.actionGlobalAttributesBar.setObjectName("actionGlobalAttributesBar")
        self.actionVariableAttributesBar = QtWidgets.QAction(MainWindow)
        self.actionVariableAttributesBar.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/var_metadata_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVariableAttributesBar.setIcon(icon12)
        self.actionVariableAttributesBar.setObjectName("actionVariableAttributesBar")
        self.actionPlotBar = QtWidgets.QAction(MainWindow)
        self.actionPlotBar.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/plot_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlotBar.setIcon(icon13)
        self.actionPlotBar.setObjectName("actionPlotBar")
        self.actionBatch_processing = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/batch_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBatch_processing.setIcon(icon14)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionBatch_processing.setFont(font)
        self.actionBatch_processing.setObjectName("actionBatch_processing")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon15)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/help_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_EGADS = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/about_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_EGADS.setIcon(icon17)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionAbout_EGADS.setFont(font)
        self.actionAbout_EGADS.setObjectName("actionAbout_EGADS")
        self.actionChangelog = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/changelog_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangelog.setIcon(icon18)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionChangelog.setFont(font)
        self.actionChangelog.setObjectName("actionChangelog")
        self.actionSeparator = QtWidgets.QAction(MainWindow)
        self.actionSeparator.setEnabled(False)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSeparator.setIcon(icon19)
        self.actionSeparator.setObjectName("actionSeparator")
        self.actionSeparator2 = QtWidgets.QAction(MainWindow)
        self.actionSeparator2.setEnabled(False)
        self.actionSeparator2.setIcon(icon19)
        self.actionSeparator2.setVisible(True)
        self.actionSeparator2.setIconVisibleInMenu(True)
        self.actionSeparator2.setObjectName("actionSeparator2")
        self.actionSeparator3 = QtWidgets.QAction(MainWindow)
        self.actionSeparator3.setEnabled(False)
        self.actionSeparator3.setIcon(icon19)
        self.actionSeparator3.setObjectName("actionSeparator3")
        self.actionSeparator4 = QtWidgets.QAction(MainWindow)
        self.actionSeparator4.setEnabled(False)
        self.actionSeparator4.setIcon(icon19)
        self.actionSeparator4.setObjectName("actionSeparator4")
        self.actionSaveAsBar = QtWidgets.QAction(MainWindow)
        self.actionSaveAsBar.setEnabled(False)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/save_as_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAsBar.setIcon(icon20)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSaveAsBar.setFont(font)
        self.actionSaveAsBar.setObjectName("actionSaveAsBar")
        self.actionDisplayBar = QtWidgets.QAction(MainWindow)
        self.actionDisplayBar.setEnabled(False)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icons/data_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisplayBar.setIcon(icon21)
        self.actionDisplayBar.setObjectName("actionDisplayBar")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon22)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOptions.setFont(font)
        self.actionOptions.setObjectName("actionOptions")
        self.menuFile.addAction(self.actionOpenBar)
        self.menuFile.addAction(self.actionSaveBar)
        self.menuFile.addAction(self.actionSaveAsBar)
        self.menuFile.addAction(self.actionCloseBar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionBatch_processing)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuProcessings.addAction(self.menuEmbedded_algorithms.menuAction())
        self.menuProcessings.addAction(self.menuUser_defined_algorithms.menuAction())
        self.menuAbout.addAction(self.actionOptions)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout_EGADS)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionChangelog)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuProcessings.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionOpenBar)
        self.toolBar.addAction(self.actionSaveBar)
        self.toolBar.addAction(self.actionSaveAsBar)
        self.toolBar.addAction(self.actionCloseBar)
        self.toolBar.addAction(self.actionSeparator)
        self.toolBar.addAction(self.actionGlobalAttributesBar)
        self.toolBar.addAction(self.actionVariableAttributesBar)
        self.toolBar.addAction(self.actionSeparator3)
        self.toolBar.addAction(self.actionCreateVariableBar)
        self.toolBar.addAction(self.actionMigrateVariableBar)
        self.toolBar.addAction(self.actionDeleteVariableBar)
        self.toolBar.addAction(self.actionSeparator4)
        self.toolBar.addAction(self.actionAlgorithmsBar)
        self.toolBar.addAction(self.actionCreatealgorithmBar)
        self.toolBar.addAction(self.actionSeparator2)
        self.toolBar.addAction(self.actionDisplayBar)
        self.toolBar.addAction(self.actionPlotBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EGADS"))
        self.gm_filename_lb.setText(_translate("MainWindow", "Filename:"))
        self.gm_dateCreation_lb.setText(_translate("MainWindow", "Date of creation:"))
        self.gm_project_lb.setText(_translate("MainWindow", "Project:"))
        self.gm_title_lb.setText(_translate("MainWindow", "Title:"))
        self.gm_institution_lb.setText(_translate("MainWindow", "Institution:"))
        self.gm_source_lb.setText(_translate("MainWindow", "Source:"))
        self.gm_history_lb.setText(_translate("MainWindow", "History:"))
        self.gm_history_lb_2.setText(_translate("MainWindow", "<html><head/><body><p>Special<br>comments:</p></body></html>"))
        self.gm_button_7.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Global Metadata"))
        self.va_varName_lb.setText(_translate("MainWindow", "Variable name:"))
        self.va_longName_lb.setText(_translate("MainWindow", "Long name:"))
        self.va_category_lb.setText(_translate("MainWindow", "Category:"))
        self.va_units_lb.setText(_translate("MainWindow", "Units:"))
        self.va_fillValue_lb.setText(_translate("MainWindow", "Fill value:"))
        self.va_dimensions_lb.setText(_translate("MainWindow", "Dimensions:"))
        self.va_egadsProcessor_lb.setText(_translate("MainWindow", "EGADS processor:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Variables"))
        self.new_varName_lb.setText(_translate("MainWindow", "Variable name:"))
        self.new_longName_lb.setText(_translate("MainWindow", "Long name:"))
        self.new_category_lb.setText(_translate("MainWindow", "Category:"))
        self.new_units_lb.setText(_translate("MainWindow", "Units:"))
        self.new_fillValue_lb.setText(_translate("MainWindow", "Fill value:"))
        self.new_dimensions_lb.setText(_translate("MainWindow", "Dimensions:"))
        self.new_egadsProcessor_lb.setText(_translate("MainWindow", "EGADS processor:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "New Variables"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuProcessings.setTitle(_translate("MainWindow", "Processing"))
        self.menuEmbedded_algorithms.setTitle(_translate("MainWindow", "Embedded algorithms"))
        self.menuUser_defined_algorithms.setTitle(_translate("MainWindow", "User-defined algorithms"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpenBar.setText(_translate("MainWindow", "Open..."))
        self.actionOpenBar.setToolTip(_translate("MainWindow", "Open a file"))
        self.actionSaveBar.setText(_translate("MainWindow", "Save..."))
        self.actionSaveBar.setToolTip(_translate("MainWindow", "Save the current file"))
        self.actionCloseBar.setText(_translate("MainWindow", "Close..."))
        self.actionCloseBar.setToolTip(_translate("MainWindow", "Close the current file"))
        self.actionAlgorithmsBar.setText(_translate("MainWindow", "Algorithms"))
        self.actionAlgorithmsBar.setToolTip(_translate("MainWindow", "Launch a process"))
        self.actionCreatealgorithmBar.setText(_translate("MainWindow", "Create Algorithm"))
        self.actionCreatealgorithmBar.setToolTip(_translate("MainWindow", "Create a new algorithm"))
        self.actionCreateVariableBar.setText(_translate("MainWindow", "Create Variable"))
        self.actionCreateVariableBar.setToolTip(_translate("MainWindow", "Create a new simple variable"))
        self.actionMigrateVariableBar.setText(_translate("MainWindow", "Migrate Variable"))
        self.actionMigrateVariableBar.setToolTip(_translate("MainWindow", "Migrate the selected variable to the main workspace"))
        self.actionDeleteVariableBar.setText(_translate("MainWindow", "Delete Variable"))
        self.actionDeleteVariableBar.setToolTip(_translate("MainWindow", "Delete the selected variable"))
        self.actionGlobalAttributesBar.setText(_translate("MainWindow", "Global Attributes"))
        self.actionGlobalAttributesBar.setToolTip(_translate("MainWindow", "Add or modify global attributes"))
        self.actionVariableAttributesBar.setText(_translate("MainWindow", "Variable Attributes"))
        self.actionVariableAttributesBar.setToolTip(_translate("MainWindow", "Add or modify the selected variable attributes"))
        self.actionPlotBar.setText(_translate("MainWindow", "Plot"))
        self.actionPlotBar.setToolTip(_translate("MainWindow", "Display a graph of the selected variable"))
        self.actionBatch_processing.setText(_translate("MainWindow", "Batch processing..."))
        self.actionExit.setText(_translate("MainWindow", "Exit..."))
        self.actionHelp.setText(_translate("MainWindow", "Help..."))
        self.actionAbout_EGADS.setText(_translate("MainWindow", "About EGADS..."))
        self.actionChangelog.setText(_translate("MainWindow", "Changelog..."))
        self.actionSeparator.setText(_translate("MainWindow", "separator"))
        self.actionSeparator2.setText(_translate("MainWindow", "separator2"))
        self.actionSeparator3.setText(_translate("MainWindow", "separator3"))
        self.actionSeparator4.setText(_translate("MainWindow", "separator4"))
        self.actionSaveAsBar.setText(_translate("MainWindow", "Save as..."))
        self.actionSaveAsBar.setToolTip(_translate("MainWindow", "Save to a new file"))
        self.actionDisplayBar.setText(_translate("MainWindow", "Display"))
        self.actionDisplayBar.setToolTip(_translate("MainWindow", "Display the selected variable"))
        self.actionOptions.setText(_translate("MainWindow", "Options..."))
        self.actionOptions.setToolTip(_translate("MainWindow", "EGADS GUI options"))

