# -*- coding: utf-8 -*-

import copy
import logging
import numpy
import ntpath
import platform
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_plotwindow import Ui_plotWindow
from functions.gui_functions import clear_layout
import matplotlib
from babel import units
matplotlib.use('Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
        
        
class PlotWindow(QtWidgets.QDialog, Ui_plotWindow):
    def __init__(self, list_of_variables, list_of_new_variables):
        logging.debug('gui - plot_window_functions.py - PlotWindow - __init__')
        QtWidgets.QDialog.__init__(self, parent=None)
        self.setupUi(self)
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
        self.setup_toolbar()
        self.list_of_variables_and_attributes = dict(list_of_variables, **list_of_new_variables)
        self.figure = plt.figure(figsize=(20, 20), facecolor='white')
        self.canvas = FigureCanvas(self.figure)
        self.pw_plot_fr.addWidget(self.canvas)
        self.navigation_toolbar = NavigationToolbar(self.canvas, self)
        self.navigation_toolbar.hide()
        self.pw_single_rd.clicked.connect(lambda: self.plot_type())
        self.pw_multiple_rd.clicked.connect(lambda: self.plot_type())
        self.pw_update_bt_2.clicked.connect(lambda: self.update_plot_options())
        self.pw_update_bt_1.clicked.connect(lambda: self.update_figure_options())
        self.plot_type_str = ""
        self.pw_graphType_la.setAlignment(QtCore.Qt.AlignTop)
        self.actionClose.triggered.connect(lambda: self.close_window())
        self.actionSave_as.triggered.connect(lambda: self.plot_save())
        self.actionPan.triggered.connect(lambda: self.plot_pan())
        self.actionZoom.triggered.connect(lambda: self.plot_zoom())
        self.actionOrigin.triggered.connect(lambda: self.plot_home())
        self.actionClear.triggered.connect(lambda: self.plot_clear())
        self.list_label = []
        self.list_button = []
        self.list_horLayout = []
        self.pw_figureOptions_vl_1 = []
        self.pw_figureOptions_gl_1 = []
        self.pw_figureOptions_gl_2 = []
        self.pw_figureOptions_gl_3 = []
        self.pw_figureOptions_gl_4 = []
        self.pw_figureOptions_hl_1 = []
        self.pw_figureOptions_hl_2 = []
        self.pw_figureOptions_hl_3 = []
        self.pw_figureOptions_hl_4 = []
        self.pw_figureOptions_hl_5 = []
        self.pw_figureOptions_hl_12 = []
        self.pw_figureOptions_lb_1 = []
        self.pw_figureOptions_lb_2 = []
        self.pw_figureOptions_lb_3 = []
        self.pw_figureOptions_lb_4 = []
        self.pw_figureOptions_lb_5 = []
        self.pw_figureOptions_lb_6 = []
        self.pw_figureOptions_lb_7 = []
        self.pw_figureOptions_lb_8 = []
        self.pw_figureOptions_lb_9 = []
        self.pw_figureOptions_lb_10 = []
        self.pw_figureOptions_lb_11 = []
        self.pw_figureOptions_lb_12 = []
        self.pw_figureOptions_lb_13 = []
        self.pw_figureOptions_lb_14 = []
        self.pw_figureOptions_lb_15 = []
        self.pw_figureOptions_lb_16 = []
        self.pw_figureOptions_lb_17 = []
        self.pw_figureOptions_lb_18 = []
        self.pw_figureOptions_lb_19 = []
        self.pw_figureOptions_lb_20 = []
        self.pw_figureOptions_lb_21 = []
        self.pw_figureOptions_lb_22 = []
        self.pw_figureOptions_lb_23 = []
        self.pw_figureOptions_lb_24 = []
        self.pw_figureOptions_lb_25 = []
        self.pw_figureOptions_lb_26 = []
        self.pw_figureOptions_lb_27 = []
        self.pw_figureOptions_lb_28 = []
        self.pw_figureOptions_lb_29 = []
        self.pw_figureOptions_lb_30 = []
        self.pw_figureOptions_ln_1 = []
        self.pw_figureOptions_ln_2 = []
        self.pw_figureOptions_ln_3 = []
        self.pw_figureOptions_ln_4 = []
        self.pw_figureOptions_ln_5 = []
        self.pw_figureOptions_ln_6 = []
        self.pw_figureOptions_ln_7 = []
        self.pw_figureOptions_ln_8 = []
        self.pw_figureOptions_ln_9 = []
        self.pw_figureOptions_ln_10 = []
        self.pw_figureOptions_cb_1 = []
        self.pw_figureOptions_cb_2 = []
        self.pw_figureOptions_cb_3 = []
        self.pw_figureOptions_cb_4 = []
        self.pw_figureOptions_cb_5 = []
        self.pw_figureOptions_cb_6 = []
        self.pw_figureOptions_cb_7 = []
        self.pw_figureOptions_cb_8 = []
        self.pw_figureOptions_cb_9 = []
        self.pw_figureOptions_cb_10 = []
        self.pw_figureOptions_bt_1 = []
        self.pw_figureOptions_bt_2 = []
        self.pw_figureOptions_bt_6 = []
        self.pw_figureOptions_bt_7 = []
        self.pw_figureOptions_bt_8 = []
        self.pw_figureOptions_bt_9 = []
        self.pw_figureOptions_ck_1 = []
        self.pw_figureOptions_ck_2 = []
        self.pw_figureOptions_li_1 = []
        self.pw_figureOptions_sl_1 = []
        self.pw_figureOptions_sl_2 = []
        self.pw_figureOptions_sl_3 = []
        self.pw_figureOptions_sl_4 = []
        self.pw_figureOptions_sl_5 = []
        self.option_num = 0
        self.pw_plotOptions_vl_1 = []
        self.pw_plotOptions_hl_1 = []
        self.pw_plotOptions_hl_2 = []
        self.pw_plotOptions_hl_3 = []
        self.pw_plotOptions_hl_4 = []
        self.pw_plotOptions_hl_5 = []
        self.pw_plotOptions_hl_6 = []
        self.pw_plotOptions_hl_7 = []
        self.pw_plotOptions_hl_8 = []
        self.pw_plotOptions_hl_9 = []
        self.pw_plotOptions_lb_1 = []
        self.pw_plotOptions_lb_2 = []
        self.pw_plotOptions_lb_3 = []
        self.pw_plotOptions_lb_4 = []
        self.pw_plotOptions_lb_5 = []
        self.pw_plotOptions_lb_6 = []
        self.pw_plotOptions_lb_7 = []
        self.pw_plotOptions_lb_8 = []
        self.pw_plotOptions_lb_9 = []
        self.pw_plotOptions_bg_1 = []
        self.pw_plotOptions_rb_1 = []
        self.pw_plotOptions_rb_2 = []
        self.pw_plotOptions_cb_1 = []
        self.pw_plotOptions_cb_2 = []
        self.pw_plotOptions_ln_1 = []
        self.pw_plotOptions_ln_2 = []
        self.pw_plotOptions_ln_3 = []
        self.pw_plotOptions_ln_4 = []
        self.pw_plotOptions_ck_1 = []
        self.pw_plotOptions_ck_2 = []
        self.pw_plotOptions_bt_1 = []
        self.pw_plotOptions_bt_2 = []
        self.pw_plotOptions_bt_3 = []
        self.pw_plotOptions_bt_4 = []
        self.pw_plotOptions_bt_5 = []
        self.pw_plotOptions_bt_6 = []
        self.pw_plotOptions_li_1 = []
        self.option_num2 = 0
        self.new_legend_entries = []
        if platform.system() == 'Linux':
            self.font_list = ([str(f.name) for f in matplotlib.font_manager.fontManager.ttflist] + 
                              [str(f.name) for f in matplotlib.font_manager.fontManager.afmlist])
        elif platform.system() == 'Windows':
            self.font_list = [font_manager.FontProperties(fname=fname).get_name() for fname in font_manager.win32InstalledFonts()]
        else:
            raise Exception('The program couldnt determined which os is intalled')
            logging.exception('gui - plot_window_functions.py - PlotWindow - __init__: an exception occured - the '
                              + 'program couldnt determined which os is intalled')
        for index, item in enumerate(self.font_list):
            self.font_list[index] = str(item)
        self.default_font = font_manager.FontProperties(family=[str(matplotlib.rcParams['font.family'][0])]).get_name()
        if self.default_font not in self.font_list:
            self.font_list.append(self.default_font)
        self.font_list = sorted(set(self.font_list))
        
        self.line_styles = [
                            "Dashed",
                            "Dash-dot",
                            "Dotted",
                            "Solid"
                            ]
        self.line_styles_dict = {
                            "Dashed":"--",
                            "Dash-dot":"-.",
                            "Dotted":":",
                            "Solid":"-"
                            }
        self.marker_styles = [
                              "Circle",
                              "Diamond",
                              "Hegagon",
                              "Pentagon",
                              "Plus",
                              "Point",
                              "Square",
                              "Star",
                              "Triangle",
                              "X"
                              ]
        self.marker_styles_dict = {
                              "Circle":"o",
                              "Diamond":"d",
                              "Hegagon":"h",
                              "Pentagon":"p",
                              "Plus":"+",
                              "Point":".",
                              "Square":"s",
                              "Star":"*",
                              "Triangle":"^",
                              "X":"x"
                              }
        
        self.colors = [
                       "HEX Color",
                       "RGB Color",
                       "Black",
                       "Blue",
                       "Cyan",
                       "Green",
                       "Magenta",
                       "Red",
                       "Yellow",
                       "White"
                       ]
        
        self.colors_grid = [
                       "Black",
                       "Blue",
                       "Cyan",
                       "Green",
                       "Magenta",
                       "Red",
                       "Yellow",
                       "White"
                       ]
        
        self.colors_dict = {
                       "Black":"k",
                       "Blue":"b",
                       "Cyan":"c",
                       "Green":"g",
                       "Magenta":"m",
                       "Red":"r",
                       "Yellow":"y",
                       "White":"w"
                       }
        
        self.variable_num = 0
        logging.info('gui - plot_window_functions.py - PlotWindow - ready')

    
    def close_window(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - close_window')
        self.close()
    
    
    def setup_toolbar(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - setup_toolbar')
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.toolBar = QtWidgets.QToolBar()
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setFont(font)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(28, 28))
        self.actionSave_as = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/save_as_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon1)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.setEnabled(False)
        self.actionClose = QtWidgets.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName("actionClose")
        self.actionZoom = QtWidgets.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon4)
        self.actionZoom.setObjectName("actionZoom")
        self.actionZoom.setEnabled(False)
        self.actionPan = QtWidgets.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/pan_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon5)
        self.actionPan.setObjectName("actionPan")
        self.actionPan.setEnabled(False)
        self.actionOrigin = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/origin_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOrigin.setIcon(icon6)
        self.actionOrigin.setObjectName("actionOrigin")
        self.actionOrigin.setEnabled(False)
        self.actionClear = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon6)
        self.actionClear.setObjectName("actionClear")
        self.actionClear.setEnabled(False)
        self.actionSeparator1 = QtWidgets.QAction(self)
        self.actionSeparator1.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSeparator1.setIcon(icon7)
        self.actionSeparator1.setObjectName("actionSeparator1")
        self.actionSeparator2 = QtWidgets.QAction(self)
        self.actionSeparator2.setEnabled(False)
        self.actionSeparator2.setIcon(icon7)
        self.actionSeparator2.setObjectName("actionSeparator2")
        self.actionSeparator3 = QtWidgets.QAction(self)
        self.actionSeparator3.setEnabled(False)
        self.actionSeparator3.setIcon(icon7)
        self.actionSeparator3.setObjectName("actionSeparator3")
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionSeparator1)
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionZoom)
        self.toolBar.addAction(self.actionSeparator2)
        self.toolBar.addAction(self.actionOrigin)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addAction(self.actionSeparator3)
        self.toolBar.addAction(self.actionClose)
        self.pw_toolbar_fr.addWidget(self.toolBar)
        self.toolBar.setWindowTitle("toolBar")
        self.actionSave_as.setText("Save as...")
        self.actionSave_as.setToolTip("Save to a graphic file")
        self.actionClose.setText("Close...")
        self.actionClose.setToolTip("Close the plot window")
        self.actionZoom.setText("Zoom")
        self.actionZoom.setToolTip("Zoom to rectangle")
        self.actionPan.setText("Pan")
        self.actionPan.setToolTip("Pan axes")
        self.actionOrigin.setText("Origin")
        self.actionOrigin.setToolTip("Reset to original view")
        self.actionClear.setText("Clear")
        self.actionClear.setToolTip("Clear the view")
    
    
    def plot_pan(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_pan: actionPan.objectName() '
                      + str(self.actionPan.objectName()))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon)
        self.actionZoom.setObjectName("actionZoom")
        if "activated" in self.actionPan.objectName():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/pan_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPan.setIcon(icon)
            self.actionPan.setObjectName("actionPan")
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/pan_icon_activated.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPan.setIcon(icon)
            self.actionPan.setObjectName("activated_actionPan")
        self.navigation_toolbar.pan()
        
        
    def plot_zoom(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_zoom : actionZoom.objectName() '
                      + str(self.actionZoom.objectName()))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/pan_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon)
        self.actionPan.setObjectName("actionPan")
        if "activated" in self.actionZoom.objectName():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionZoom.setIcon(icon)
            self.actionZoom.setObjectName("actionZoom")
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/zoom_icon_activated.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionZoom.setIcon(icon)
            self.actionZoom.setObjectName("activated_actionZoom")
        self.navigation_toolbar.zoom()
        
        
    def plot_home(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_home')
        self.navigation_toolbar.home()
    
    
    def plot_save(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_save')
        save_file_name, save_file_ext = self.get_file_name()
        if not save_file_name:
            return
        out_file_name, out_file_ext = ntpath.splitext(ntpath.basename(save_file_name))
        if not out_file_ext:
            if save_file_ext == "EPS Files (*.eps)":
                save_file_name = save_file_name + ".eps"
            elif save_file_ext == "JPEG Files (*.jpg *.jpeg *.jpe)":
                save_file_name = save_file_name + ".jpg"
            elif save_file_ext == "PDF Files (*.pdf)":
                save_file_name = save_file_name + ".pdf"
            elif save_file_ext == "PNG Files (*.png *.pns)":
                save_file_name = save_file_name + ".png"
            elif save_file_ext == "TIFF Files (*.tif *.tiff)":
                save_file_name = save_file_name + ".tif"
        
        figure = plt.gcf()        
        xsize_scr, ysize_scr = figure.get_size_inches()
                
        if self.pw_saveOptions_ln_1.text() != "" and self.pw_saveOptions_ln_2.text() != "":
            ysize_fig = float(self.pw_saveOptions_ln_1.text())
            xsize_fig = float(self.pw_saveOptions_ln_2.text())
            if self.pw_saveOptions_cb_1.currentText() == "Centimeters":
                ysize_fig = ysize_fig * 0.393701
            if self.pw_saveOptions_cb_2.currentText() == "Centimeters":
                xsize_fig = xsize_fig * 0.393701
        
            figure.set_size_inches(xsize_fig, ysize_fig)
        
        fname = save_file_name
        kwargs = {
                  "orientation":None,
                  "papertype":None,
                  "format":None,
                  "bbox_inches":None,
                  "pad_inches":0.1,
                  "frameon":None
                  }
        if self.pw_saveOptions_ln_3.text() != "":
            try:
                kwargs["dpi"] = int(str(self.pw_saveOptions_ln_3.text()))
            except ValueError:
                kwargs["dpi"] = 100
        else:
            kwargs["dpi"] = 100
        if self.pw_saveOptions_ck_1.isChecked() == True:
            kwargs["transparent"] = True
        else:
            kwargs["transparent"] = False
        plt.savefig(fname, **kwargs)
        
        figure.set_size_inches(xsize_scr, ysize_scr)
        self.canvas.draw()
    
    
    def plot_type(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_type : sender().objectName() '
                      + str(self.sender().objectName()))
        if self.sender().objectName() == "pw_single_rd":
            if self.plot_type_str == "" or self.plot_type_str == "multiple":
                clear_layout(self, self.pw_graphType_la)
                self.plot_clear()
                self.plot_type_str = "single"
                self.setup_type_single()
                self.populate_comboboxes(self.pw_xvariable_rl)
                self.populate_comboboxes(self.pw_yvariable_rl)
        elif self.sender().objectName() == "pw_multiple_rd":
            if self.plot_type_str == "" or self.plot_type_str == "single":
                clear_layout(self, self.pw_graphType_la)
                self.plot_clear()
                self.plot_type_str = "multiple"
                self.setup_type_multiple()
    
    
    def plot_clear(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_clear : plot_type_str '
                      + str(self.plot_type_str))
        if self.plot_type_str == "single":
            for i in reversed(range(0, len(self.list_horLayout))):
                self.del_variable_single(i)
            plt.clf()
            self.canvas.draw()
        elif self.plot_type_str == "multiple":
            for i in reversed(range(0, len(self.subplot_data))):
                print i
                self.del_subplot(i)
            plt.clf()
            self.canvas.draw()
            
            
    def setup_type_single(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - setup_type_single')
        self.legend_visibility = True
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/plus_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_singleHorlayout_1 = QtWidgets.QHBoxLayout()
        self.pw_singleHorlayout_1.setObjectName("pw_singleHorlayout_1")
        self.pw_singleLabel_1 = QtWidgets.QLabel()
        self.pw_singleLabel_1.setMinimumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_1.setMaximumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_1.setFont(font)
        self.pw_singleLabel_1.setText("Please choose a variable for the X axis")
        self.pw_singleLabel_1.setObjectName("pw_singleLabel_1")
        self.pw_singleLabel_1.setStyleSheet("QLabel {color: black;}")
        self.pw_singleHorlayout_1.addWidget(self.pw_singleLabel_1)
        self.pw_singleHorlayout_1.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_1)
        self.pw_singleHorlayout_2 = QtWidgets.QHBoxLayout()
        self.pw_singleHorlayout_2.setObjectName("pw_singleHorlayout_2")
        self.pw_singleHorlayout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_xvariable_rl = QtWidgets.QComboBox()
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_xvariable_rl.setItemDelegate(itemDelegate)
        self.pw_xvariable_rl.setFont(font2)
        self.pw_xvariable_rl.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_xvariable_rl.setMaximumSize(QtCore.QSize(250, 27))
        self.pw_xvariable_rl.setStyleSheet("QComboBox {\n"
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
        self.pw_xvariable_rl.setObjectName("pw_xvariable_rl")
        self.pw_singleHorlayout_2.addWidget(self.pw_xvariable_rl)
        self.pw_singleHorlayout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_2)
        self.pw_graphType_la.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.pw_singleHorlayout_3 = QtWidgets.QHBoxLayout()
        self.pw_singleHorlayout_3.setObjectName("pw_singleHorlayout_3")
        self.pw_singleLabel_2 = QtWidgets.QLabel()
        self.pw_singleLabel_2.setMinimumSize(QtCore.QSize(310, 60))
        self.pw_singleLabel_2.setMaximumSize(QtCore.QSize(310, 60))
        self.pw_singleLabel_2.setFont(font)
        self.pw_singleLabel_2.setText("Please choose one variable in the following list for the Y axis and click on the '+' button to add it to the plot")
        self.pw_singleLabel_2.setWordWrap(True)
        self.pw_singleLabel_2.setObjectName("pw_singleLabel_2")
        self.pw_singleLabel_2.setStyleSheet("QLabel {color: black;}")
        self.pw_singleHorlayout_3.addWidget(self.pw_singleLabel_2)
        self.pw_singleHorlayout_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_3)
        self.pw_singleHorlayout_4 = QtWidgets.QHBoxLayout()
        self.pw_singleHorlayout_4.setObjectName("pw_singleHorlayout_4")
        self.pw_singleHorlayout_4.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_yvariable_rl = QtWidgets.QComboBox()
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_yvariable_rl.setItemDelegate(itemDelegate)
        self.pw_yvariable_rl.setFont(font2)
        self.pw_yvariable_rl.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_yvariable_rl.setMaximumSize(QtCore.QSize(250, 27))
        self.pw_yvariable_rl.setStyleSheet("QComboBox {\n"
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
        self.pw_yvariable_rl.setObjectName("pw_yvariable_rl")
        self.pw_singleHorlayout_4.addWidget(self.pw_yvariable_rl)
        self.pw_addSingle_bt = QtWidgets.QToolButton()
        self.pw_addSingle_bt.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_addSingle_bt.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_addSingle_bt.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_addSingle_bt.setText("")
        self.pw_addSingle_bt.setIcon(icon)
        self.pw_addSingle_bt.setIconSize(QtCore.QSize(23, 23))
        self.pw_addSingle_bt.setObjectName("pw_addSingle_bt")
        self.pw_singleHorlayout_4.addWidget(self.pw_addSingle_bt)
        self.pw_singleHorlayout_4.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_4)
        self.pw_graphType_la.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.pw_singleHorlayout_5 = QtWidgets.QHBoxLayout()
        self.pw_singleHorlayout_5.setObjectName("self.pw_singleHorlayout_5")
        self.pw_singleLabel_3 = QtWidgets.QLabel()
        self.pw_singleLabel_3.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_singleLabel_3.setMaximumSize(QtCore.QSize(250, 27))
        font.setBold(True)
        font.setWeight(75)
        self.pw_singleLabel_3.setFont(font)
        self.pw_singleLabel_3.setText("List of plotted variables:")
        self.pw_singleLabel_3.setObjectName("pw_singleLabel_3")
        self.pw_singleLabel_3.setStyleSheet("QLabel {color: black;}")
        self.pw_singleLabel_3.hide()
        self.pw_singleHorlayout_5.addWidget(self.pw_singleLabel_3)
        self.pw_singleHorlayout_5.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_5)
        self.pw_singleVerlayout_1 = QtWidgets.QVBoxLayout()
        self.pw_singleVerlayout_1.setObjectName("pw_singleVerlayout_1")
        self.pw_graphType_la.addLayout(self.pw_singleVerlayout_1)
        self.pw_addSingle_bt.clicked.connect(lambda: self.plot_variable_single())
        
        
    def setup_type_multiple(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - setup_type_multiple')
        self.pw_multipleVerlayout_1 = []
        self.pw_multipleVerlayout_2 = []
        self.pw_multipleHorlayout_2 = []
        self.pw_multipleHorlayout_3 = []
        self.pw_multipleHorlayout_4 = []
        self.pw_multipleHorlayout_5 = []
        self.pw_multipleHorlayout_6 = []
        self.pw_multipleHorlayout_7 = []
        self.pw_singleLabel_1 = []
        self.pw_singleLabel_2 = []
        self.pw_singleLabel_3 = []
        self.pw_multipleYvariable_rl = []
        self.pw_multipleXvariable_rl = []
        self.pw_multipleDel_bt = []
        self.pw_multipleLine_1 = []
        self.multiple_num = 0
        self.mult_margin_left = 0.13
        self.mult_margin_right = 0.92
        self.mult_margin_bottom = 0.11
        self.mult_margin_top = 0.95
        self.mult_vert_space = 0.4
        self.mult_grid_option = []
        self.subplot_data = []
        self.legend_visibility = []
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/plus_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_multipleHorlayout_1 = QtWidgets.QHBoxLayout()
        self.pw_multipleHorlayout_1.setObjectName("pw_multipleHorlayout_1")
        self.pw_multipleLabel_1 = QtWidgets.QLabel()
        self.pw_multipleLabel_1.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_multipleLabel_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_multipleLabel_1.setFont(font)
        self.pw_multipleLabel_1.setText("Please press the '+' to add a subplot")
        self.pw_multipleLabel_1.setObjectName("pw_multipleLabel_1")
        self.pw_multipleLabel_1.setStyleSheet("QLabel {color: black;}")
        self.pw_multipleHorlayout_1.addWidget(self.pw_multipleLabel_1)
        self.pw_addMultiple_bt = QtWidgets.QToolButton()
        self.pw_addMultiple_bt.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_addMultiple_bt.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_addMultiple_bt.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_addMultiple_bt.setIcon(icon)
        self.pw_addMultiple_bt.setIconSize(QtCore.QSize(23, 23))
        self.pw_addMultiple_bt.setObjectName("pw_addMultiple_bt")
        self.pw_multipleHorlayout_1.addWidget(self.pw_addMultiple_bt)
        self.pw_multipleHorlayout_1.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_multipleHorlayout_1)
        self.pw_addMultiple_bt.clicked.connect(lambda: self.add_subplot_selection())

 
    def add_variable_single(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - add_variable_single: pw_yvariable_rl.currentText() '
                      + str(self.pw_yvariable_rl.currentText()))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.list_horLayout.append(QtWidgets.QHBoxLayout())
        self.list_horLayout[self.variable_num].setObjectName("list_horLayout_" + str(self.variable_num))
        self.list_horLayout[self.variable_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.list_label.append(QtWidgets.QLabel())
        self.list_label[self.variable_num].setFont(font)
        self.list_label[self.variable_num].setText(self.pw_yvariable_rl.currentText())
        self.list_label[self.variable_num].setToolTip(self.pw_yvariable_rl.currentText())
        self.list_label[self.variable_num].setMinimumSize(QtCore.QSize(150, 27))
        self.list_label[self.variable_num].setMaximumSize(QtCore.QSize(250, 27))
        self.list_label[self.variable_num].setObjectName("list_label_" + str(self.variable_num))
        self.list_label[self.variable_num].setStyleSheet("QLabel {color: black;}")
        self.list_horLayout[self.variable_num].addWidget(self.list_label[self.variable_num])
        self.list_button.append(QtWidgets.QToolButton())
        self.list_button[self.variable_num].setMinimumSize(QtCore.QSize(27, 27))
        self.list_button[self.variable_num].setMaximumSize(QtCore.QSize(27, 27))
        self.list_button[self.variable_num].setText("")
        self.list_button[self.variable_num].setIcon(icon)
        self.list_button[self.variable_num].setIconSize(QtCore.QSize(23, 23))
        self.list_button[self.variable_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.list_button[self.variable_num].setAutoRaise(False)
        self.list_button[self.variable_num].setObjectName("list_button_" + str(self.variable_num))
        self.list_button[self.variable_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.list_button[self.variable_num].clicked.connect(lambda: self.del_variable_single())
        self.list_horLayout[self.variable_num].addWidget(self.list_button[self.variable_num])
        self.list_horLayout[self.variable_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_singleVerlayout_1.addLayout(self.list_horLayout[self.variable_num])
        self.variable_num += 1
        
        
    def del_variable_single(self, index = None):
        if index == None:
            index = int(self.sender().objectName()[12:])
        logging.debug('gui - plot_window_functions.py - PlotWindow - del_variable_single : index '
                      + str(index) + ', list_label[index].text() ' + str(self.list_label[index].text()))
        plt.axes().lines[index].remove()
        if self.variable_num > 1:
            leg = plt.legend(prop={'family':self.default_font, 'size':'10'})
            leg.draggable()
            if not self.legend_visibility:
                plt.gca().legend().set_visibility(False)
        self.canvas.draw()
        self.list_label[index].deleteLater()
        self.list_label.pop(index)
        self.list_button[index].deleteLater()
        self.list_button.pop(index)
        self.list_horLayout[index].deleteLater()
        self.list_horLayout.pop(index)
        self.variable_num -= 1
        self.del_plot_options(index)
        if len(self.list_horLayout) > 0:
            for i in range(0, len(self.list_horLayout)):
                self.list_horLayout[i].setObjectName("list_horLayout_" + str(i))
                self.list_button[i].setObjectName("list_button_" + str(i))
                self.list_label[i].setObjectName("list_label_" + str(i))
        else:
            plt.clf()
            self.canvas.draw()
            self.actionZoom.setEnabled(False)
            self.actionPan.setEnabled(False)
            self.actionSave_as.setEnabled(False)
            self.actionOrigin.setEnabled(False)
            self.actionClear.setEnabled(False)
            self.pw_singleLabel_3.hide()
            self.pw_yvariable_rl.setCurrentIndex(0)
            self.pw_xvariable_rl.setCurrentIndex(0)
            self.del_figure_options(0)
    
    
    def del_figure_options(self, index):
        if self.pw_figureOptions_vl_1:
            logging.debug('gui - plot_window_functions.py - PlotWindow - del_figure_options : index '
                      + str(index))
            keep_first_index = None
            if len(self.pw_figureOptions_vl_1) > 1 and index == 0 and self.plot_type_str == 'multiple':
                keep_first_index = 1
                index = 1
                line_value_1 = self.pw_figureOptions_ln_1[index].text()
                line_value_2 = self.pw_figureOptions_ln_2[index].text()
                line_value_3 = self.pw_figureOptions_ln_3[index].text()
                line_value_4 = self.pw_figureOptions_ln_4[index].text()
                line_value_5 = self.pw_figureOptions_ln_5[index].text()
                line_value_6 = self.pw_figureOptions_ln_6[index].text()
                line_value_7 = self.pw_figureOptions_ln_7[index].text()
                line_value_8 = self.pw_figureOptions_ln_8[index].text()
                line_value_9 = self.pw_figureOptions_ln_9[index].text()
                line_value_10 = self.pw_figureOptions_ln_10[index].text()
                combo_value_1 = self.pw_figureOptions_cb_1[index].currentIndex()
                combo_value_2 = self.pw_figureOptions_cb_2[index].currentIndex()
                combo_value_3 = self.pw_figureOptions_cb_3[index].currentIndex()
                combo_value_4 = self.pw_figureOptions_cb_4[index].currentIndex()
                combo_value_5 = self.pw_figureOptions_cb_5[index].currentIndex()
                combo_value_6 = self.pw_figureOptions_cb_6[index].currentIndex()
                combo_value_7 = self.pw_figureOptions_cb_7[index].currentIndex()
                combo_value_8 = self.pw_figureOptions_cb_8[index].currentIndex()
                combo_value_9 = self.pw_figureOptions_cb_9[index].currentIndex()
                combo_value_10 = self.pw_figureOptions_cb_10[index].currentIndex()
                check_value_1 = self.pw_figureOptions_ck_1[index].isChecked()
                check_value_2 = self.pw_figureOptions_ck_2[index].isChecked()
            if index < 1:
                self.pw_figureOptions_hl_5[index].deleteLater()
                self.pw_figureOptions_hl_5.pop(index)
                self.pw_figureOptions_gl_4[index].deleteLater()
                self.pw_figureOptions_gl_4.pop(index)
                self.pw_figureOptions_lb_20[index].deleteLater()
                self.pw_figureOptions_lb_20.pop(index)
                self.pw_figureOptions_lb_21[index].deleteLater()
                self.pw_figureOptions_lb_21.pop(index)
                self.pw_figureOptions_lb_22[index].deleteLater()
                self.pw_figureOptions_lb_22.pop(index)
                self.pw_figureOptions_lb_23[index].deleteLater()
                self.pw_figureOptions_lb_23.pop(index)
                self.pw_figureOptions_lb_24[index].deleteLater()
                self.pw_figureOptions_lb_24.pop(index)
                self.pw_figureOptions_lb_25[index].deleteLater()
                self.pw_figureOptions_lb_25.pop(index)
                self.pw_figureOptions_lb_26[index].deleteLater()
                self.pw_figureOptions_lb_26.pop(index)
                self.pw_figureOptions_lb_27[index].deleteLater()
                self.pw_figureOptions_lb_27.pop(index)
                self.pw_figureOptions_lb_28[index].deleteLater()
                self.pw_figureOptions_lb_28.pop(index)
                self.pw_figureOptions_bt_8[index].deleteLater()
                self.pw_figureOptions_bt_8.pop(index)
                self.pw_figureOptions_sl_1[index].deleteLater()
                self.pw_figureOptions_sl_1.pop(index)
                self.pw_figureOptions_sl_2[index].deleteLater()
                self.pw_figureOptions_sl_2.pop(index)
                self.pw_figureOptions_sl_3[index].deleteLater()
                self.pw_figureOptions_sl_3.pop(index)
                self.pw_figureOptions_sl_4[index].deleteLater()
                self.pw_figureOptions_sl_4.pop(index)
            self.pw_figureOptions_vl_1[index].deleteLater()
            self.pw_figureOptions_vl_1.pop(index)
            self.pw_figureOptions_gl_1[index].deleteLater()
            self.pw_figureOptions_gl_1.pop(index)
            self.pw_figureOptions_gl_2[index].deleteLater()
            self.pw_figureOptions_gl_2.pop(index)
            self.pw_figureOptions_gl_3[index].deleteLater()
            self.pw_figureOptions_gl_3.pop(index)
            self.pw_figureOptions_hl_1[index].deleteLater()
            self.pw_figureOptions_hl_1.pop(index)
            self.pw_figureOptions_hl_2[index].deleteLater()
            self.pw_figureOptions_hl_2.pop(index)
            self.pw_figureOptions_hl_3[index].deleteLater()
            self.pw_figureOptions_hl_3.pop(index)
            self.pw_figureOptions_hl_4[index].deleteLater()
            self.pw_figureOptions_hl_4.pop(index)
            self.pw_figureOptions_lb_1[index].deleteLater()
            self.pw_figureOptions_lb_1.pop(index)
            self.pw_figureOptions_lb_2[index].deleteLater()
            self.pw_figureOptions_lb_2.pop(index)
            self.pw_figureOptions_lb_3[index].deleteLater()
            self.pw_figureOptions_lb_3.pop(index)
            self.pw_figureOptions_lb_4[index].deleteLater()
            self.pw_figureOptions_lb_4.pop(index)
            self.pw_figureOptions_lb_5[index].deleteLater()
            self.pw_figureOptions_lb_5.pop(index)
            self.pw_figureOptions_lb_6[index].deleteLater()
            self.pw_figureOptions_lb_6.pop(index)
            self.pw_figureOptions_lb_7[index].deleteLater()
            self.pw_figureOptions_lb_7.pop(index)
            self.pw_figureOptions_lb_8[index].deleteLater()
            self.pw_figureOptions_lb_8.pop(index)
            self.pw_figureOptions_lb_9[index].deleteLater()
            self.pw_figureOptions_lb_9.pop(index)
            self.pw_figureOptions_lb_10[index].deleteLater()
            self.pw_figureOptions_lb_10.pop(index)
            self.pw_figureOptions_lb_11[index].deleteLater()
            self.pw_figureOptions_lb_11.pop(index)
            self.pw_figureOptions_lb_12[index].deleteLater()
            self.pw_figureOptions_lb_12.pop(index)
            self.pw_figureOptions_lb_13[index].deleteLater()
            self.pw_figureOptions_lb_13.pop(index)
            self.pw_figureOptions_lb_14[index].deleteLater()
            self.pw_figureOptions_lb_14.pop(index)
            self.pw_figureOptions_lb_15[index].deleteLater()
            self.pw_figureOptions_lb_15.pop(index)
            self.pw_figureOptions_lb_16[index].deleteLater()
            self.pw_figureOptions_lb_16.pop(index)
            self.pw_figureOptions_lb_17[index].deleteLater()
            self.pw_figureOptions_lb_17.pop(index)
            self.pw_figureOptions_lb_18[index].deleteLater()
            self.pw_figureOptions_lb_18.pop(index)
            self.pw_figureOptions_lb_19[index].deleteLater()
            self.pw_figureOptions_lb_19.pop(index)
            self.pw_figureOptions_ln_1[index].deleteLater()
            self.pw_figureOptions_ln_1.pop(index)
            self.pw_figureOptions_ln_2[index].deleteLater()
            self.pw_figureOptions_ln_2.pop(index)
            self.pw_figureOptions_ln_3[index].deleteLater()
            self.pw_figureOptions_ln_3.pop(index)
            self.pw_figureOptions_ln_4[index].deleteLater()
            self.pw_figureOptions_ln_4.pop(index)
            self.pw_figureOptions_ln_5[index].deleteLater()
            self.pw_figureOptions_ln_5.pop(index)
            self.pw_figureOptions_ln_6[index].deleteLater()
            self.pw_figureOptions_ln_6.pop(index)
            self.pw_figureOptions_ln_7[index].deleteLater()
            self.pw_figureOptions_ln_7.pop(index)
            self.pw_figureOptions_ln_8[index].deleteLater()
            self.pw_figureOptions_ln_8.pop(index)
            self.pw_figureOptions_ln_9[index].deleteLater()
            self.pw_figureOptions_ln_9.pop(index)
            self.pw_figureOptions_ln_10[index].deleteLater()
            self.pw_figureOptions_ln_10.pop(index)
            self.pw_figureOptions_cb_1[index].deleteLater()
            self.pw_figureOptions_cb_1.pop(index)
            self.pw_figureOptions_cb_2[index].deleteLater()
            self.pw_figureOptions_cb_2.pop(index)
            self.pw_figureOptions_cb_3[index].deleteLater()
            self.pw_figureOptions_cb_3.pop(index)
            self.pw_figureOptions_cb_4[index].deleteLater()
            self.pw_figureOptions_cb_4.pop(index)
            self.pw_figureOptions_cb_5[index].deleteLater()
            self.pw_figureOptions_cb_5.pop(index)
            self.pw_figureOptions_cb_6[index].deleteLater()
            self.pw_figureOptions_cb_6.pop(index)
            self.pw_figureOptions_cb_7[index].deleteLater()
            self.pw_figureOptions_cb_7.pop(index)
            self.pw_figureOptions_cb_8[index].deleteLater()
            self.pw_figureOptions_cb_8.pop(index)
            self.pw_figureOptions_cb_9[index].deleteLater()
            self.pw_figureOptions_cb_9.pop(index)
            self.pw_figureOptions_cb_10[index].deleteLater()
            self.pw_figureOptions_cb_10.pop(index)
            self.pw_figureOptions_bt_1[index].deleteLater()
            self.pw_figureOptions_bt_1.pop(index)
            self.pw_figureOptions_bt_2[index].deleteLater()
            self.pw_figureOptions_bt_2.pop(index)
            self.pw_figureOptions_bt_6[index].deleteLater()
            self.pw_figureOptions_bt_6.pop(index)
            self.pw_figureOptions_bt_7[index].deleteLater()
            self.pw_figureOptions_bt_7.pop(index)
            self.pw_figureOptions_ck_1[index].deleteLater()
            self.pw_figureOptions_ck_1.pop(index)
            self.pw_figureOptions_ck_2[index].deleteLater()
            self.pw_figureOptions_ck_2.pop(index)
            self.pw_figureOptions_li_1[index].deleteLater()
            self.pw_figureOptions_li_1.pop(index)
            if self.plot_type_str == "multiple":
                if index < 1:
                    self.pw_figureOptions_hl_12[index].deleteLater()
                    self.pw_figureOptions_hl_12.pop(index)
                    self.pw_figureOptions_sl_5[index].deleteLater()
                    self.pw_figureOptions_sl_5.pop(index)
                    self.pw_figureOptions_lb_29[index].deleteLater()
                    self.pw_figureOptions_lb_29.pop(index)
                    self.pw_figureOptions_lb_30[index].deleteLater()
                    self.pw_figureOptions_lb_30.pop(index)
                    self.pw_figureOptions_bt_9[index].deleteLater()
                    self.pw_figureOptions_bt_9.pop(index)
                for i in range(0, self.option_num - 1):
                    xlim_up = self.subplot_plot[i].axes.get_xlim()[1]
                    xlim_dn = self.subplot_plot[i].axes.get_xlim()[0]
                    ylim_up = self.subplot_plot[i].axes.get_ylim()[1]
                    ylim_dn = self.subplot_plot[i].axes.get_ylim()[0]
                    xstep = self.subplot_plot[i].axes.get_xticks()[1] - self.subplot_plot[i].axes.get_xticks()[0]
                    ystep = self.subplot_plot[i].axes.get_yticks()[1] - self.subplot_plot[i].axes.get_yticks()[0]
                    self.pw_figureOptions_ln_4[i].setText(str(xlim_dn))
                    self.pw_figureOptions_ln_4[i].setCursorPosition(0)
                    self.pw_figureOptions_ln_5[i].setText(str(xlim_up))
                    self.pw_figureOptions_ln_5[i].setCursorPosition(0)
                    self.pw_figureOptions_ln_6[i].setText(str(xstep))
                    self.pw_figureOptions_ln_6[i].setCursorPosition(0)
                    self.pw_figureOptions_ln_7[i].setText(str(ylim_dn))
                    self.pw_figureOptions_ln_7[i].setCursorPosition(0)
                    self.pw_figureOptions_ln_8[i].setText(str(ylim_up))
                    self.pw_figureOptions_ln_8[i].setCursorPosition(0)
                    self.pw_figureOptions_ln_9[i].setText(str(ystep))
                    self.pw_figureOptions_ln_9[i].setCursorPosition(0)
            self.option_num -= 1
            if keep_first_index == 1:
                self.pw_figureOptions_ck_1[0].setChecked(check_value_1)
                self.pw_figureOptions_ck_2[0].setChecked(check_value_2)
                self.pw_figureOptions_ln_1[0].setText(line_value_1)
                self.pw_figureOptions_ln_2[0].setText(line_value_2)
                self.pw_figureOptions_ln_3[0].setText(line_value_3)
                self.pw_figureOptions_ln_4[0].setText(line_value_4)
                self.pw_figureOptions_ln_5[0].setText(line_value_5)
                self.pw_figureOptions_ln_6[0].setText(line_value_6)
                self.pw_figureOptions_ln_7[0].setText(line_value_7)
                self.pw_figureOptions_ln_8[0].setText(line_value_8)
                self.pw_figureOptions_ln_9[0].setText(line_value_9)
                self.pw_figureOptions_ln_10[0].setText(line_value_10)
                self.pw_figureOptions_cb_1[0].setCurrentIndex(combo_value_1)
                self.pw_figureOptions_cb_2[0].setCurrentIndex(combo_value_2)
                self.pw_figureOptions_cb_3[0].setCurrentIndex(combo_value_3)
                self.pw_figureOptions_cb_4[0].setCurrentIndex(combo_value_4)
                self.pw_figureOptions_cb_5[0].setCurrentIndex(combo_value_5)
                self.pw_figureOptions_cb_6[0].setCurrentIndex(combo_value_6)
                self.pw_figureOptions_cb_7[0].setCurrentIndex(combo_value_7)
                self.pw_figureOptions_cb_8[0].setCurrentIndex(combo_value_8)
                self.pw_figureOptions_cb_9[0].setCurrentIndex(combo_value_9)
                self.pw_figureOptions_cb_10[0].setCurrentIndex(combo_value_10)
            self.update_figure_options()
    
    
    def del_plot_options(self, index):
        if self.pw_plotOptions_vl_1:
            logging.debug('gui - plot_window_functions.py - PlotWindow - del_plot_options : index '
                      + str(index))
            self.pw_plotOptions_vl_1[index].deleteLater()
            self.pw_plotOptions_vl_1.pop(index)
            self.pw_plotOptions_hl_1[index].deleteLater()
            self.pw_plotOptions_hl_1.pop(index)
            self.pw_plotOptions_hl_2[index].deleteLater()
            self.pw_plotOptions_hl_2.pop(index)
            self.pw_plotOptions_hl_3[index].deleteLater()
            self.pw_plotOptions_hl_3.pop(index)
            self.pw_plotOptions_hl_4[index].deleteLater()
            self.pw_plotOptions_hl_4.pop(index)
            self.pw_plotOptions_hl_5[index].deleteLater()
            self.pw_plotOptions_hl_5.pop(index)
            self.pw_plotOptions_hl_6[index].deleteLater()
            self.pw_plotOptions_hl_6.pop(index)
            self.pw_plotOptions_hl_7[index].deleteLater()
            self.pw_plotOptions_hl_7.pop(index)
            self.pw_plotOptions_hl_8[index].deleteLater()
            self.pw_plotOptions_hl_8.pop(index)
            self.pw_plotOptions_hl_9[index].deleteLater()
            self.pw_plotOptions_hl_9.pop(index)
            self.pw_plotOptions_lb_1[index].deleteLater()
            self.pw_plotOptions_lb_1.pop(index)
            self.pw_plotOptions_lb_2[index].deleteLater()
            self.pw_plotOptions_lb_2.pop(index)
            self.pw_plotOptions_lb_3[index].deleteLater()
            self.pw_plotOptions_lb_3.pop(index)
            self.pw_plotOptions_lb_4[index].deleteLater()
            self.pw_plotOptions_lb_4.pop(index)
            self.pw_plotOptions_lb_5[index].deleteLater()
            self.pw_plotOptions_lb_5.pop(index)
            self.pw_plotOptions_lb_6[index].deleteLater()
            self.pw_plotOptions_lb_6.pop(index)
            self.pw_plotOptions_lb_7[index].deleteLater()
            self.pw_plotOptions_lb_7.pop(index)
            self.pw_plotOptions_lb_8[index].deleteLater()
            self.pw_plotOptions_lb_8.pop(index)
            self.pw_plotOptions_lb_9[index].deleteLater()
            self.pw_plotOptions_lb_9.pop(index)
            self.pw_plotOptions_rb_1[index].deleteLater()
            self.pw_plotOptions_rb_1.pop(index)
            self.pw_plotOptions_rb_2[index].deleteLater()
            self.pw_plotOptions_rb_2.pop(index)
            self.pw_plotOptions_cb_1[index].deleteLater()
            self.pw_plotOptions_cb_1.pop(index)
            self.pw_plotOptions_cb_2[index].deleteLater()
            self.pw_plotOptions_cb_2.pop(index)
            self.pw_plotOptions_bt_1[index].deleteLater()
            self.pw_plotOptions_bt_1.pop(index)
            self.pw_plotOptions_bt_2[index].deleteLater()
            self.pw_plotOptions_bt_2.pop(index)
            self.pw_plotOptions_bt_3[index].deleteLater()
            self.pw_plotOptions_bt_3.pop(index)
            self.pw_plotOptions_bt_4[index].deleteLater()
            self.pw_plotOptions_bt_4.pop(index)
            self.pw_plotOptions_bt_5[index].deleteLater()
            self.pw_plotOptions_bt_5.pop(index)
            self.pw_plotOptions_bt_6[index].deleteLater()
            self.pw_plotOptions_bt_6.pop(index)
            self.pw_plotOptions_ln_1[index].deleteLater()
            self.pw_plotOptions_ln_1.pop(index)
            self.pw_plotOptions_ln_2[index].deleteLater()
            self.pw_plotOptions_ln_2.pop(index)
            self.pw_plotOptions_ln_3[index].deleteLater()
            self.pw_plotOptions_ln_3.pop(index)
            self.pw_plotOptions_ln_4[index].deleteLater()
            self.pw_plotOptions_ln_4.pop(index)
            self.pw_plotOptions_ck_1[index].deleteLater()
            self.pw_plotOptions_ck_1.pop(index)
            self.pw_plotOptions_ck_2[index].deleteLater()
            self.pw_plotOptions_ck_2.pop(index)
            self.pw_plotOptions_li_1[index].deleteLater()
            self.pw_plotOptions_li_1.pop(index)
            self.option_num2 -=1
            self.update_plot_options()
        
    
    def add_subplot_selection(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - add_subplot_selection : multiple_num '
                      + str(self.multiple_num))
        if self.multiple_num > 0:
            if (self.pw_multipleXvariable_rl[self.multiple_num - 1].currentText() == 'Make a choice...' or
            self.pw_multipleYvariable_rl[self.multiple_num - 1].currentText() == 'Make a choice...'):
                return
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font.setBold(True)
        font.setWeight(75)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_multipleVerlayout_2.append(QtWidgets.QVBoxLayout())
        self.pw_multipleVerlayout_2[self.multiple_num].setObjectName("pw_multipleVerlayout_2_" + str(self.multiple_num))
        self.pw_multipleVerlayout_2[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.pw_multipleVerlayout_1.append(QtWidgets.QVBoxLayout())
        self.pw_multipleVerlayout_1[self.multiple_num].setObjectName("pw_multipleVerlayout_1_" + str(self.multiple_num))
        self.pw_multipleHorlayout_2.append(QtWidgets.QHBoxLayout())
        self.pw_multipleHorlayout_2[self.multiple_num].setObjectName("pw_multipleHorlayout_2_" + str(self.multiple_num))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_2[self.multiple_num])
        self.pw_singleLabel_1.append(QtWidgets.QLabel())
        self.pw_singleLabel_1[self.multiple_num].setMinimumSize(QtCore.QSize(150, 27))
        self.pw_singleLabel_1[self.multiple_num].setMaximumSize(QtCore.QSize(150, 27))
        self.pw_singleLabel_1[self.multiple_num].setFont(font)
        self.pw_singleLabel_1[self.multiple_num].setText("Subplot " + str(self.multiple_num + 1))
        self.pw_singleLabel_1[self.multiple_num].setObjectName("pw_singleLabel_1_" + str(self.multiple_num))
        self.pw_singleLabel_1[self.multiple_num].setStyleSheet("QLabel {color: black;}")
        self.pw_multipleHorlayout_2[self.multiple_num].addWidget(self.pw_singleLabel_1[self.multiple_num])
        self.pw_multipleHorlayout_2[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_3.append(QtWidgets.QHBoxLayout())
        self.pw_multipleHorlayout_3[self.multiple_num].setObjectName("pw_multipleHorlayout_3_" + str(self.multiple_num))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_3[self.multiple_num])
        self.pw_singleLabel_2.append(QtWidgets.QLabel())
        self.pw_singleLabel_2[self.multiple_num].setMinimumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_2[self.multiple_num].setMaximumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_2[self.multiple_num].setFont(font2)
        self.pw_singleLabel_2[self.multiple_num].setText("Please choose a variable for the X axis")
        self.pw_singleLabel_2[self.multiple_num].setObjectName("pw_singleLabel_2_" + str(self.multiple_num))
        self.pw_singleLabel_2[self.multiple_num].setStyleSheet("QLabel {color: black;}")
        self.pw_multipleHorlayout_3[self.multiple_num].addWidget(self.pw_singleLabel_2[self.multiple_num])
        self.pw_multipleHorlayout_3[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_4.append(QtWidgets.QHBoxLayout())
        self.pw_multipleHorlayout_4[self.multiple_num].setObjectName("pw_multipleHorlayout_4_" + str(self.multiple_num))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_4[self.multiple_num])
        self.pw_multipleHorlayout_4[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleXvariable_rl.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_multipleXvariable_rl[self.multiple_num].setItemDelegate(itemDelegate)
        self.pw_multipleXvariable_rl[self.multiple_num].setFont(font3)
        self.pw_multipleXvariable_rl[self.multiple_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_multipleXvariable_rl[self.multiple_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_multipleXvariable_rl[self.multiple_num].setStyleSheet("QComboBox {\n"
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
        self.pw_multipleXvariable_rl[self.multiple_num].setObjectName("pw_multipleXvariable_rl_" + str(self.multiple_num))
        self.pw_multipleHorlayout_4[self.multiple_num].addWidget(self.pw_multipleXvariable_rl[self.multiple_num])
        self.pw_multipleHorlayout_4[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_5.append(QtWidgets.QHBoxLayout())
        self.pw_multipleHorlayout_5[self.multiple_num].setObjectName("pw_multipleHorlayout_5_" + str(self.multiple_num))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_5[self.multiple_num])
        self.pw_singleLabel_3.append(QtWidgets.QLabel())
        self.pw_singleLabel_3[self.multiple_num].setMinimumSize(QtCore.QSize(310, 27))
        self.pw_singleLabel_3[self.multiple_num].setMaximumSize(QtCore.QSize(310, 27))
        self.pw_singleLabel_3[self.multiple_num].setFont(font2)
        self.pw_singleLabel_3[self.multiple_num].setText("Please choose a variable for the Y axis")
        self.pw_singleLabel_3[self.multiple_num].setObjectName("pw_singleLabel_3_" + str(self.multiple_num))
        self.pw_singleLabel_3[self.multiple_num].setWordWrap(True)
        self.pw_singleLabel_3[self.multiple_num].setStyleSheet("QLabel {color: black;}")
        self.pw_multipleHorlayout_5[self.multiple_num].addWidget(self.pw_singleLabel_3[self.multiple_num])
        self.pw_multipleHorlayout_5[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_6.append(QtWidgets.QHBoxLayout())
        self.pw_multipleHorlayout_6[self.multiple_num].setObjectName("pw_multipleHorlayout_6_" + str(self.multiple_num))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_6[self.multiple_num])
        self.pw_multipleHorlayout_6[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleYvariable_rl.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_multipleYvariable_rl[self.multiple_num].setItemDelegate(itemDelegate)
        self.pw_multipleYvariable_rl[self.multiple_num].setFont(font3)
        self.pw_multipleYvariable_rl[self.multiple_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_multipleYvariable_rl[self.multiple_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_multipleYvariable_rl[self.multiple_num].setStyleSheet("QComboBox {\n"
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
        self.pw_multipleYvariable_rl[self.multiple_num].setObjectName("pw_multipleYvariable_rl_" + str(self.multiple_num))
        self.pw_multipleHorlayout_6[self.multiple_num].addWidget(self.pw_multipleYvariable_rl[self.multiple_num])
        self.pw_multipleHorlayout_6[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_7.append(QtWidgets.QHBoxLayout())
        self.pw_multipleHorlayout_7[self.multiple_num].setObjectName("pw_multipleHorlayout_7_" + str(self.multiple_num))
        self.pw_multipleDel_bt.append(QtWidgets.QToolButton())
        self.pw_multipleDel_bt[self.multiple_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_multipleDel_bt[self.multiple_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_multipleDel_bt[self.multiple_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_multipleDel_bt[self.multiple_num].setText("")
        self.pw_multipleDel_bt[self.multiple_num].setIcon(icon)
        self.pw_multipleDel_bt[self.multiple_num].setIconSize(QtCore.QSize(23, 23))
        self.pw_multipleDel_bt[self.multiple_num].setAutoRaise(False)
        self.pw_multipleDel_bt[self.multiple_num].setObjectName("pw_multipleDel_bt_" + str(self.multiple_num))
        self.pw_multipleHorlayout_7[self.multiple_num].addWidget(self.pw_multipleDel_bt[self.multiple_num])
        self.pw_multipleLine_1.append(QtWidgets.QFrame())
        self.pw_multipleLine_1[self.multiple_num].setFrameShape(QtWidgets.QFrame.VLine)
        self.pw_multipleLine_1[self.multiple_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pw_multipleLine_1[self.multiple_num].setObjectName("pw_multipleLine_1_" + str(self.multiple_num))
        self.pw_multipleHorlayout_7[self.multiple_num].addWidget(self.pw_multipleLine_1[self.multiple_num])
        self.pw_multipleHorlayout_7[self.multiple_num].addLayout(self.pw_multipleVerlayout_1[self.multiple_num])
        self.pw_multipleHorlayout_7[self.multiple_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_multipleVerlayout_2[self.multiple_num].addLayout(self.pw_multipleHorlayout_7[self.multiple_num])
        self.pw_graphType_la.addLayout(self.pw_multipleVerlayout_2[self.multiple_num])
        self.populate_comboboxes(self.pw_multipleXvariable_rl[self.multiple_num])
        self.populate_comboboxes(self.pw_multipleYvariable_rl[self.multiple_num])
        self.pw_multipleXvariable_rl[self.multiple_num].activated.connect(lambda: self.add_subplot_plot())
        self.pw_multipleYvariable_rl[self.multiple_num].activated.connect(lambda: self.add_subplot_plot())
        self.pw_multipleDel_bt[self.multiple_num].clicked.connect(lambda: self.del_subplot())
        self.subplot_data.append([])
        self.multiple_num += 1
        
    
    def plot_variable_single(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_variable_single : pw_xvariable_rl.currentText() '
                      + str(self.pw_xvariable_rl.currentText()) + ', pw_yvariable_rl.currentText() '
                      + str(self.pw_yvariable_rl.currentText()))
        if self.pw_xvariable_rl.currentText() != "Make a choice..." and self.pw_yvariable_rl.currentText() != "Make a choice...":
            self.actionZoom.setEnabled(True)
            self.actionPan.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.actionOrigin.setEnabled(True)
            self.actionClear.setEnabled(True)
            self.pw_singleLabel_3.show()
            self.add_variable_single()
            xnan = ""
            ynan = ""
            sublist = self.list_of_variables_and_attributes[str(self.pw_xvariable_rl.currentText())]
            xvalue = copy.deepcopy(sublist[3].value)
            try:
                xunits = copy.deepcopy(sublist[1]["units"])
            except KeyError:
                logging.exception('gui - plot_window_functions.py - PlotWindow - plot_variable_single : x no units')
                xunits = 'no units'
            try:
                xnan = sublist[1]["_FillValue"]
            except KeyError:
                logging.exception('gui - plot_window_functions.py - PlotWindow - plot_variable_single : x no _FillValue')
                pass
            sublist = self.list_of_variables_and_attributes[str(self.pw_yvariable_rl.currentText())]
            yvalue = copy.deepcopy(sublist[3].value)
            yname = str(self.pw_yvariable_rl.currentText())
            try:
                yunits = copy.deepcopy(sublist[1]["units"])
            except KeyError:
                logging.exception('gui - plot_window_functions.py - PlotWindow - plot_variable_single : y no units')
                yunits = 'no units'
            try:
                ynan = sublist[1]["_FillValue"]
            except KeyError:
                logging.error('gui - plot_window_functions.py - PlotWindow - plot_variable_single : y no _FillValue')
                pass
            for index, xitem in enumerate(xvalue):
                if xitem == xnan:
                    xvalue[index] = numpy.nan
            for index, yitem in enumerate(yvalue):
                if yitem == ynan:
                    yvalue[index] = numpy.nan
            plt.plot(xvalue, yvalue, label = yname)
            plt.ylabel(yunits)
            plt.xlabel(xunits)
            leg = plt.legend(prop={'family':self.default_font, 'size':'10'})
            leg.draggable()
            if self.variable_num == 1:
                plt.ylim([plt.axes().get_yticks()[0], plt.axes().get_yticks()[-1]])
                plt.xlim([plt.axes().get_xticks()[0], plt.axes().get_xticks()[-1]])
                plt.subplots_adjust(left=0.13, right=0.92, bottom=0.11, top=0.95)
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.gca().get_xaxis().tick_bottom()
            plt.gca().get_yaxis().tick_left()
            plt.gca().set_axisbelow(True)
            if not self.legend_visibility:
                plt.gca().legend().set_visibility(False)
            self.canvas.draw()
            if self.option_num == 0:
                self.figure_options()
            self.plot_options()
    
        
    def add_subplot_plot(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - add_subplot_plot : sender().objectName() '
                      + str(self.sender().objectName()))
        index = int(self.sender().objectName()[24:])
        if "X" in self.sender().objectName():
            xcombobox = self.sender()
            ycombobox = self.findChild(QtWidgets.QComboBox, "pw_multipleYvariable_rl_" + str(index))
        elif "Y" in self.sender().objectName():
            xcombobox = self.findChild(QtWidgets.QComboBox, "pw_multipleXvariable_rl_" + str(index))
            ycombobox = self.sender()
        logging.debug('gui - plot_window_functions.py - PlotWindow - add_subplot_plot : xcombobox.currentText() '
                      + str(xcombobox.currentText()) + ', ycombobox.currentText() ' + xcombobox.currentText())
        if ycombobox.currentText() != "Make a choice..." and xcombobox.currentText() != "Make a choice...":
            self.actionZoom.setEnabled(True)
            self.actionPan.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.actionOrigin.setEnabled(True)
            self.actionClear.setEnabled(True)
            xnan = ""
            ynan = ""
            self.mult_grid_option.append(False)
            self.legend_visibility.append(True)
            sublist = self.list_of_variables_and_attributes[str(xcombobox.currentText())]
            xvalue = copy.deepcopy(sublist[3].value)
            xunits = copy.deepcopy(sublist[1]["units"])
            xname = copy.deepcopy(sublist[1]["var_name"])
            try:
                xnan = sublist[1]["_FillValue"]
            except KeyError:
                logging.exception('gui - plot_window_functions.py - PlotWindow - add_subplot_plot : x no _FillValue')
                pass
            sublist = self.list_of_variables_and_attributes[str(ycombobox.currentText())]
            yvalue = copy.deepcopy(sublist[3].value)
            yunits = copy.deepcopy(sublist[1]["units"])
            yname = copy.deepcopy(sublist[1]["var_name"])
            try:
                ynan = sublist[1]["_FillValue"]
            except KeyError:
                logging.exception('gui - plot_window_functions.py - PlotWindow - add_subplot_plot : y no _FillValue')
                pass
            for xindex, xitem in enumerate(xvalue):
                if xitem == xnan:
                    xvalue[xindex] = numpy.nan
            for yindex, yitem in enumerate(yvalue):
                if yitem == ynan:
                    yvalue[yindex] = numpy.nan
            self.subplot_data[index] = [xvalue, yvalue, xunits, yunits, xname, yname]
            plt.clf()
            self.subplot_plot = []
            tmp = []
            for item in self.subplot_data:
                if item:
                    tmp.append(item)
            for index, item in enumerate(tmp):
                if item:
                    self.subplot_plot.append(self.figure.add_subplot(len(tmp), 1, index + 1))
                    self.subplot_plot[index].plot(item[0], item[1], label = item[5])
                    self.subplot_plot[index].set_ylabel(item[3])
                    self.subplot_plot[index].set_xlabel(item[2])
                    self.subplot_plot[index].set_ylim([self.subplot_plot[index].axes.get_yticks()[0],
                                                       self.subplot_plot[index].axes.get_yticks()[-1]])
                    self.subplot_plot[index].set_xlim([self.subplot_plot[index].axes.get_xticks()[0],
                                                       self.subplot_plot[index].axes.get_xticks()[-1]])
                    self.subplot_plot[index].spines['top'].set_visible(False)
                    self.subplot_plot[index].spines['right'].set_visible(False)
                    self.subplot_plot[index].get_xaxis().tick_bottom()
                    self.subplot_plot[index].get_yaxis().tick_left()
                    self.subplot_plot[index].set_axisbelow(True)
                    leg = self.subplot_plot[index].legend(prop={'family':self.default_font, 'size':'10'})
                    leg.draggable()
                    if not isinstance(self.mult_grid_option[index], bool):
                        self.subplot_plot[index].grid(b=True, **self.mult_grid_option[index])
                    if not self.legend_visibility[index]:
                        self.subplot_plot[index].legend().set_visible(False)
            self.figure.tight_layout()
            plt.subplots_adjust(left=self.mult_margin_left,
                                right=self.mult_margin_right,
                                bottom=self.mult_margin_bottom,
                                top=self.mult_margin_top,
                                hspace=self.mult_vert_space)
            self.canvas.draw()
            self.figure_options()
            self.plot_options()
            self.update_figure_options()
            self.update_plot_options()
    
    
    def del_subplot(self, index=None):
        if index == None:
            index = int(self.sender().objectName()[18:])
        logging.debug('gui - plot_window_functions.py - PlotWindow - del_subplot invoked: index '
                      + str(index))
        x_string = self.pw_multipleXvariable_rl[index].currentText()
        y_string = self.pw_multipleYvariable_rl[index].currentText()
        self.pw_multipleVerlayout_1[index].deleteLater()
        self.pw_multipleVerlayout_1.pop(index)
        self.pw_multipleVerlayout_2[index].deleteLater()
        self.pw_multipleVerlayout_2.pop(index)
        self.pw_multipleHorlayout_2[index].deleteLater()
        self.pw_multipleHorlayout_2.pop(index)
        self.pw_multipleHorlayout_3[index].deleteLater()
        self.pw_multipleHorlayout_3.pop(index)
        self.pw_multipleHorlayout_4[index].deleteLater()
        self.pw_multipleHorlayout_4.pop(index)
        self.pw_multipleHorlayout_5[index].deleteLater()
        self.pw_multipleHorlayout_5.pop(index)
        self.pw_multipleHorlayout_6[index].deleteLater()
        self.pw_multipleHorlayout_6.pop(index)
        self.pw_multipleHorlayout_7[index].deleteLater()
        self.pw_multipleHorlayout_7.pop(index)
        self.pw_singleLabel_1[index].deleteLater()
        self.pw_singleLabel_1.pop(index)
        self.pw_singleLabel_2[index].deleteLater()
        self.pw_singleLabel_2.pop(index)
        self.pw_singleLabel_3[index].deleteLater()
        self.pw_singleLabel_3.pop(index)
        self.pw_multipleYvariable_rl[index].deleteLater()
        self.pw_multipleYvariable_rl.pop(index)
        self.pw_multipleXvariable_rl[index].deleteLater()
        self.pw_multipleXvariable_rl.pop(index)
        self.pw_multipleDel_bt[index].deleteLater()
        self.pw_multipleDel_bt.pop(index)
        self.pw_multipleLine_1[index].deleteLater()
        self.pw_multipleLine_1.pop(index)
        self.subplot_data.pop(index)
        plt.clf()
        self.subplot_plot = []
        tmp = []
        for item in self.subplot_data:
            if item:
                tmp.append(item)
        for i, item in enumerate(tmp):
            if item:
                self.subplot_plot.append(self.figure.add_subplot(len(tmp), 1, i + 1))
                self.subplot_plot[i].plot(item[0], item[1], label = item[5])
                self.subplot_plot[i].set_ylabel(item[3])
                self.subplot_plot[i].set_xlabel(item[2])
                self.subplot_plot[i].spines['top'].set_visible(False)
                self.subplot_plot[i].spines['right'].set_visible(False)
        if self.subplot_data:
            if len(self.subplot_data) > 1:
                self.figure.tight_layout()
            self.canvas.draw()
        self.multiple_num -= 1
        if x_string != 'Make a choice...' and y_string != 'Make a choice...':
            self.del_figure_options(index)
            self.del_plot_options(index)
        if len(self.pw_multipleVerlayout_1) > 0:
            for i in range(0, len(self.pw_multipleVerlayout_1)):
                self.pw_singleLabel_1[i].setText("Subplot " + str(i + 1))
                self.pw_multipleVerlayout_2[i].setObjectName("pw_multipleVerlayout_2_" + str(i))
                self.pw_multipleVerlayout_1[i].setObjectName("pw_multipleVerlayout_1_" + str(i))
                self.pw_multipleHorlayout_2[i].setObjectName("pw_multipleHorlayout_2_" + str(i))
                self.pw_singleLabel_1[i].setObjectName("pw_singleLabel_1_" + str(i))
                self.pw_multipleHorlayout_3[i].setObjectName("pw_multipleHorlayout_3_" + str(i))
                self.pw_singleLabel_2[i].setObjectName("pw_singleLabel_2_" + str(i))
                self.pw_multipleHorlayout_4[i].setObjectName("pw_multipleHorlayout_4_" + str(i))
                self.pw_multipleXvariable_rl[i].setObjectName("pw_multipleXvariable_rl_" + str(i))
                self.pw_multipleHorlayout_5[i].setObjectName("pw_multipleHorlayout_5_" + str(i))
                self.pw_singleLabel_3[i].setObjectName("pw_singleLabel_3_" + str(i))
                self.pw_multipleHorlayout_6[i].setObjectName("pw_multipleHorlayout_6_" + str(i))
                self.pw_multipleYvariable_rl[i].setObjectName("pw_multipleYvariable_rl_" + str(i))
                self.pw_multipleHorlayout_7[i].setObjectName("pw_multipleHorlayout_7_" + str(i))
                self.pw_multipleDel_bt[i].setObjectName("pw_multipleDel_bt_" + str(i))
                self.pw_multipleLine_1[i].setObjectName("pw_multipleLine_1_" + str(i))
        else:
            plt.clf()
            self.canvas.draw()
            self.actionZoom.setEnabled(False)
            self.actionPan.setEnabled(False)
            self.actionSave_as.setEnabled(False)
            self.actionOrigin.setEnabled(False)
            self.actionClear.setEnabled(False)
        
        
    def figure_options(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - figure_options : plot_type_str '
                      + str(self.plot_type_str) + ', option_num ' + str(self.option_num))
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_figureOptions_vl_1.append(QtWidgets.QVBoxLayout())
        self.pw_figureOptions_vl_1[self.option_num].setObjectName("pw_figureOptions_vl_1_" + str(self.option_num))
        self.pw_figureOptions_hl_1.append(QtWidgets.QHBoxLayout())
        self.pw_figureOptions_hl_1[self.option_num].setObjectName("pw_figureOptions_hl_1_" + str(self.option_num))
        self.pw_figureOptions_lb_1.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_1[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_1[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_1[self.option_num].setFont(font2)
        if self.plot_type_str == "single":
            self.pw_figureOptions_lb_1[self.option_num].setText("Figure options:")
        else:
            self.pw_figureOptions_lb_1[self.option_num].setText("Subplot " + str(self.option_num + 1) + ": Figure options")
        self.pw_figureOptions_lb_1[self.option_num].setObjectName("pw_figureOptions_lb_1_" + str(self.option_num))
        self.pw_figureOptions_lb_1[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_hl_1[self.option_num].addWidget(self.pw_figureOptions_lb_1[self.option_num])
        self.pw_figureOptions_hl_1[self.option_num].addItem(QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_1[self.option_num])
        self.pw_figureOptions_hl_2.append(QtWidgets.QHBoxLayout())
        self.pw_figureOptions_hl_2[self.option_num].setObjectName("pw_figureOptions_hl_2_" + str(self.option_num))
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_gl_1.append(QtWidgets.QGridLayout())
        self.pw_figureOptions_gl_1[self.option_num].setObjectName("pw_figureOptions_gl_1_" + str(self.option_num))
        self.pw_figureOptions_hl_2[self.option_num].addLayout(self.pw_figureOptions_gl_1[self.option_num])
        self.pw_figureOptions_lb_2.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_2[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_2[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_2[self.option_num].setFont(font)
        self.pw_figureOptions_lb_2[self.option_num].setText("Figure title:")
        self.pw_figureOptions_lb_2[self.option_num].setObjectName("pw_figureOptions_lb_2_" + str(self.option_num))
        self.pw_figureOptions_lb_2[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_2[self.option_num], 0, 0, 1, 1)
        self.pw_figureOptions_ln_1.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_1[self.option_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_1[self.option_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_1[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_1[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_1[self.option_num].setObjectName("pw_lineEdit_1_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_ln_1[self.option_num], 0, 1, 1, 1)
        self.pw_figureOptions_gl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 2, 1, 1)
        self.pw_figureOptions_lb_3.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_3[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_3[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_3[self.option_num].setFont(font)
        self.pw_figureOptions_lb_3[self.option_num].setText("Font:")
        self.pw_figureOptions_lb_3[self.option_num].setObjectName("pw_figureOptions_lb_3_" + str(self.option_num))
        self.pw_figureOptions_lb_3[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_3[self.option_num], 0, 3, 1, 1)
        self.pw_figureOptions_cb_1.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_1[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_1[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_1[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_1[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_1[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_1[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_1[self.option_num].setObjectName("pw_figureOptions_cb_1_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_cb_1[self.option_num], 0, 4, 1, 1)
        self.pw_figureOptions_gl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 5, 1, 1)
        self.pw_figureOptions_lb_4.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_4[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_4[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_4[self.option_num].setFont(font)
        self.pw_figureOptions_lb_4[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_4[self.option_num].setObjectName("pw_figureOptions_lb_4_" + str(self.option_num))
        self.pw_figureOptions_lb_4[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_4[self.option_num], 0, 6, 1, 1)
        self.pw_figureOptions_cb_2.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_2[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_2[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_2[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_2[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_2[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_2[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_2[self.option_num].setObjectName("pw_figureOptions_cb_2_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_cb_2[self.option_num], 0, 7, 1, 1)
        self.pw_figureOptions_gl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 8, 1, 1)
        self.pw_figureOptions_lb_5.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_5[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_5[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_5[self.option_num].setFont(font)
        self.pw_figureOptions_lb_5[self.option_num].setText("X axis label:")
        self.pw_figureOptions_lb_5[self.option_num].setObjectName("pw_figureOptions_lb_5_" + str(self.option_num))
        self.pw_figureOptions_lb_5[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_5[self.option_num], 1, 0, 1, 1)
        self.pw_figureOptions_ln_2.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_2[self.option_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_2[self.option_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_2[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_2[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_2[self.option_num].setObjectName("pw_lineEdit_2_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_ln_2[self.option_num], 1, 1, 1, 1)
        self.pw_figureOptions_gl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
        self.pw_figureOptions_lb_6.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_6[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_6[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_6[self.option_num].setFont(font)
        self.pw_figureOptions_lb_6[self.option_num].setText("Font:")
        self.pw_figureOptions_lb_6[self.option_num].setObjectName("pw_figureOptions_lb_6_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_6[self.option_num], 1, 3, 1, 1)
        self.pw_figureOptions_cb_3.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_3[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_3[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_3[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_3[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_3[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_3[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_3[self.option_num].setObjectName("pw_figureOptions_cb_3_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_cb_3[self.option_num], 1, 4, 1, 1)
        self.pw_figureOptions_gl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 5, 1, 1)
        self.pw_figureOptions_lb_7.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_7[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_7[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_7[self.option_num].setFont(font)
        self.pw_figureOptions_lb_7[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_7[self.option_num].setObjectName("pw_figureOptions_lb_7_" + str(self.option_num))
        self.pw_figureOptions_lb_7[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_7[self.option_num], 1, 6, 1, 1)
        self.pw_figureOptions_cb_4.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_4[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_4[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_4[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_4[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_4[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_4[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_4[self.option_num].setObjectName("pw_figureOptions_cb_4_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_cb_4[self.option_num], 1, 7, 1, 1)
        self.pw_figureOptions_lb_8.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_8[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_8[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_8[self.option_num].setFont(font)
        self.pw_figureOptions_lb_8[self.option_num].setText("Y axis label:")
        self.pw_figureOptions_lb_8[self.option_num].setObjectName("pw_figureOptions_lb_8_" + str(self.option_num))
        self.pw_figureOptions_lb_8[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_8[self.option_num], 2, 0, 1, 1)
        self.pw_figureOptions_ln_3.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_3[self.option_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_3[self.option_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_3[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_3[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_3[self.option_num].setObjectName("pw_lineEdit_3_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_ln_3[self.option_num], 2, 1, 1, 1)
        self.pw_figureOptions_gl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 2, 2, 1, 1)
        self.pw_figureOptions_lb_9.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_9[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_9[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_9[self.option_num].setFont(font)
        self.pw_figureOptions_lb_9[self.option_num].setText("Font:")
        self.pw_figureOptions_lb_9[self.option_num].setObjectName("pw_figureOptions_lb_9_" + str(self.option_num))
        self.pw_figureOptions_lb_9[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_9[self.option_num], 2, 3, 1, 1)
        self.pw_figureOptions_cb_5.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_5[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_5[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_5[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_5[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_5[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_5[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_5[self.option_num].setObjectName("pw_figureOptions_cb_5_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_cb_5[self.option_num], 2, 4, 1, 1)
        self.pw_figureOptions_gl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 2, 5, 1, 1)
        self.pw_figureOptions_lb_10.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_10[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_10[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_10[self.option_num].setFont(font)
        self.pw_figureOptions_lb_10[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_10[self.option_num].setObjectName("pw_figureOptions_lb_10_" + str(self.option_num))
        self.pw_figureOptions_lb_10[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_lb_10[self.option_num], 2, 6, 1, 1)
        self.pw_figureOptions_cb_6.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_6[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_6[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_6[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_6[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_6[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_6[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_6[self.option_num].setObjectName("pw_figureOptions_cb_6_" + str(self.option_num))
        self.pw_figureOptions_gl_1[self.option_num].addWidget(self.pw_figureOptions_cb_6[self.option_num], 2, 7, 1, 1)
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_1.append(QtWidgets.QToolButton())
        self.pw_figureOptions_bt_1[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_1[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_1[self.option_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_figureOptions_bt_1[self.option_num].setText("")
        self.pw_figureOptions_bt_1[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_1[self.option_num].setIconSize(QtCore.QSize(23, 23))
        self.pw_figureOptions_bt_1[self.option_num].setAutoRaise(False)
        self.pw_figureOptions_bt_1[self.option_num].setObjectName("pw_figureOptions_bt_1_" + str(self.option_num))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_bt_1[self.option_num])
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_2[self.option_num])
        self.pw_figureOptions_hl_3.append(QtWidgets.QHBoxLayout())
        self.pw_figureOptions_hl_3[self.option_num].setObjectName("pw_figureOptions_hl_3_" + str(self.option_num))
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_gl_2.append(QtWidgets.QGridLayout())
        self.pw_figureOptions_gl_2[self.option_num].setObjectName("pw_figureOptions_gl_2_" + str(self.option_num))
        self.pw_figureOptions_hl_3[self.option_num].addLayout(self.pw_figureOptions_gl_2[self.option_num])
        self.pw_figureOptions_lb_11.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_11[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_11[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_11[self.option_num].setFont(font)
        self.pw_figureOptions_lb_11[self.option_num].setText("X min / max / tick step:")
        self.pw_figureOptions_lb_11[self.option_num].setObjectName("pw_figureOptions_lb_11_" + str(self.option_num))
        self.pw_figureOptions_lb_11[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_lb_11[self.option_num], 0, 0, 1, 1)
        self.pw_figureOptions_ln_4.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_4[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_4[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_4[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_4[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_4[self.option_num].setObjectName("pw_figureOptions_ln_4_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_ln_4[self.option_num], 0, 1, 1, 1)
        self.pw_figureOptions_ln_5.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_5[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_5[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_5[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_5[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_5[self.option_num].setObjectName("pw_figureOptions_ln_5_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_ln_5[self.option_num], 0, 2, 1, 1)
        self.pw_figureOptions_ln_6.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_6[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_6[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_6[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_6[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_6[self.option_num].setObjectName("pw_figureOptions_ln_6_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_ln_6[self.option_num], 0, 3, 1, 1)
        self.pw_figureOptions_gl_2[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 4, 1, 1)
        self.pw_figureOptions_lb_12.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_12[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_12[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_12[self.option_num].setFont(font)
        self.pw_figureOptions_lb_12[self.option_num].setText("Format:")
        self.pw_figureOptions_lb_12[self.option_num].setObjectName("pw_figureOptions_lb_12_" + str(self.option_num))
        self.pw_figureOptions_lb_12[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_lb_12[self.option_num], 0, 5, 1, 1)
        self.pw_figureOptions_cb_7.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_7[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_7[self.option_num].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_7[self.option_num].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_7[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_7[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_7[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_7[self.option_num].setObjectName("pw_figureOptions_cb_7_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_cb_7[self.option_num], 0, 6, 1, 1)
        self.pw_figureOptions_lb_13.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_13[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_13[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_13[self.option_num].setFont(font)
        self.pw_figureOptions_lb_13[self.option_num].setText("Y min / max / tick step:")
        self.pw_figureOptions_lb_13[self.option_num].setObjectName("pw_figureOptions_lb_13_" + str(self.option_num))
        self.pw_figureOptions_lb_13[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_lb_13[self.option_num], 1, 0, 1, 1)
        self.pw_figureOptions_ln_7.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_7[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_7[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_7[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_7[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_7[self.option_num].setObjectName("pw_figureOptions_ln_7_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_ln_7[self.option_num], 1, 1, 1, 1)
        self.pw_figureOptions_ln_8.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_8[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_8[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_8[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_8[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_8[self.option_num].setObjectName("pw_figureOptions_ln_8_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_ln_8[self.option_num], 1, 2, 1, 1)
        self.pw_figureOptions_ln_9.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_9[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_9[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_9[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_9[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_figureOptions_ln_9[self.option_num].setObjectName("pw_figureOptions_ln_9_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_ln_9[self.option_num], 1, 3, 1, 1)
        self.pw_figureOptions_gl_2[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 4, 1, 1)
        self.pw_figureOptions_lb_14.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_14[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_14[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_14[self.option_num].setFont(font)
        self.pw_figureOptions_lb_14[self.option_num].setText("Format:")
        self.pw_figureOptions_lb_14[self.option_num].setObjectName("pw_figureOptions_lb_14_" + str(self.option_num))
        self.pw_figureOptions_lb_14[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_lb_14[self.option_num], 1, 5, 1, 1)
        self.pw_figureOptions_cb_8.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_8[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_8[self.option_num].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_8[self.option_num].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_8[self.option_num].setFont(font)
        self.pw_figureOptions_cb_8[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_8[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_8[self.option_num].setObjectName("pw_figureOptions_cb_8_" + str(self.option_num))
        self.pw_figureOptions_gl_2[self.option_num].addWidget(self.pw_figureOptions_cb_8[self.option_num], 1, 6, 1, 1)
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_2.append(QtWidgets.QToolButton())
        self.pw_figureOptions_bt_2[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_2[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_2[self.option_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_figureOptions_bt_2[self.option_num].setText("")
        self.pw_figureOptions_bt_2[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_2[self.option_num].setIconSize(QtCore.QSize(23, 23))
        self.pw_figureOptions_bt_2[self.option_num].setAutoRaise(False)
        self.pw_figureOptions_bt_2[self.option_num].setObjectName("pw_figureOptions_bt_2_" + str(self.option_num))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_bt_2[self.option_num])
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_3[self.option_num])
        self.pw_figureOptions_hl_4.append(QtWidgets.QHBoxLayout())
        self.pw_figureOptions_hl_4[self.option_num].setObjectName("pw_figureOptions_hl_4_" + str(self.option_num))
        self.pw_figureOptions_hl_4[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_gl_3.append(QtWidgets.QGridLayout())
        self.pw_figureOptions_gl_3[self.option_num].setObjectName("pw_figureOptions_gl_3_" + str(self.option_num))
        self.pw_figureOptions_hl_4[self.option_num].addLayout(self.pw_figureOptions_gl_3[self.option_num])
        self.pw_figureOptions_lb_15.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_15[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_15[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_15[self.option_num].setFont(font)
        self.pw_figureOptions_lb_15[self.option_num].setText("Display grid ?")
        self.pw_figureOptions_lb_15[self.option_num].setObjectName("pw_figureOptions_lb_15_" + str(self.option_num))
        self.pw_figureOptions_lb_15[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_lb_15[self.option_num], 0, 0, 1, 1)
        self.pw_figureOptions_ck_1.append(QtWidgets.QCheckBox())
        self.pw_figureOptions_ck_1[self.option_num].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_1[self.option_num].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_1[self.option_num].setText("")
        self.pw_figureOptions_ck_1[self.option_num].setObjectName("pw_figureOptions_ck_1_" + str(self.option_num))
        self.pw_figureOptions_ck_1[self.option_num].setStyleSheet("QCheckBox {\n"
        "    spacing: 5px;\n"
        "    color: black;\n"
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
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_ck_1[self.option_num], 0, 1, 1, 1)
        self.pw_figureOptions_gl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 2, 1, 1)
        self.pw_figureOptions_lb_16.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_16[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_16[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_16[self.option_num].setFont(font)
        self.pw_figureOptions_lb_16[self.option_num].setText("Style:")
        self.pw_figureOptions_lb_16[self.option_num].setObjectName("pw_figureOptions_lb_16_" + str(self.option_num))
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_lb_16[self.option_num], 0, 3, 1, 1)
        self.pw_figureOptions_cb_9.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_9[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_9[self.option_num].setEnabled(False)
        self.pw_figureOptions_cb_9[self.option_num].setMinimumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_9[self.option_num].setMaximumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_9[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_9[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_9[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_9[self.option_num].setObjectName("pw_figureOptions_cb_9_" + str(self.option_num))
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_cb_9[self.option_num], 0, 4, 1, 1)
        self.pw_figureOptions_gl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 5, 1, 1)
        self.pw_figureOptions_lb_17.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_17[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_17[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_17[self.option_num].setFont(font)
        self.pw_figureOptions_lb_17[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_17[self.option_num].setObjectName("pw_figureOptions_lb_17_" + str(self.option_num))
        self.pw_figureOptions_lb_17[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_lb_17[self.option_num], 0, 6, 1, 1)
        self.pw_figureOptions_ln_10.append(QtWidgets.QLineEdit())
        self.pw_figureOptions_ln_10[self.option_num].setEnabled(False)
        self.pw_figureOptions_ln_10[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_ln_10[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_ln_10[self.option_num].setFont(font3)
        self.pw_figureOptions_ln_10[self.option_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}")
        self.pw_figureOptions_ln_10[self.option_num].setObjectName("pw_figureOptions_ln_10_" + str(self.option_num))
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_ln_10[self.option_num], 0, 7, 1, 1)
        self.pw_figureOptions_gl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 8, 1, 1)
        self.pw_figureOptions_lb_19.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_19[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_19[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_19[self.option_num].setFont(font)
        self.pw_figureOptions_lb_19[self.option_num].setText("Color:")
        self.pw_figureOptions_lb_19[self.option_num].setObjectName("pw_figureOptions_lb_19_" + str(self.option_num))
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_lb_19[self.option_num], 0, 9, 1, 1)
        self.pw_figureOptions_cb_10.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_figureOptions_cb_10[self.option_num].setItemDelegate(itemDelegate)
        self.pw_figureOptions_cb_10[self.option_num].setEnabled(False)
        self.pw_figureOptions_cb_10[self.option_num].setMinimumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_10[self.option_num].setMaximumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_10[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_10[self.option_num].setStyleSheet("QComboBox {\n"
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
        self.pw_figureOptions_cb_10[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_10[self.option_num].setObjectName("pw_figureOptions_cb_10_" + str(self.option_num))
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_cb_10[self.option_num], 0, 10, 1, 1)
        self.pw_figureOptions_gl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 11, 1, 1)
        self.pw_figureOptions_bt_6.append(QtWidgets.QToolButton())
        self.pw_figureOptions_bt_6[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_6[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_6[self.option_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_figureOptions_bt_6[self.option_num].setText("")
        self.pw_figureOptions_bt_6[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_6[self.option_num].setIconSize(QtCore.QSize(23, 23))
        self.pw_figureOptions_bt_6[self.option_num].setAutoRaise(False)
        self.pw_figureOptions_bt_6[self.option_num].setObjectName("pw_figureOptions_bt_6_" + str(self.option_num))
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_bt_6[self.option_num], 0, 12, 1, 1)
        self.pw_figureOptions_lb_18.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_18[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_18[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_18[self.option_num].setFont(font)
        self.pw_figureOptions_lb_18[self.option_num].setText("Display Legend ?")
        self.pw_figureOptions_lb_18[self.option_num].setObjectName("pw_figureOptions_lb_18_" + str(self.option_num))
        self.pw_figureOptions_lb_18[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_lb_18[self.option_num], 1, 0, 1, 1)
        self.pw_figureOptions_ck_2.append(QtWidgets.QCheckBox())
        self.pw_figureOptions_ck_2[self.option_num].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_2[self.option_num].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_2[self.option_num].setText("")
        self.pw_figureOptions_ck_2[self.option_num].setChecked(True)
        self.pw_figureOptions_ck_2[self.option_num].setObjectName("pw_figureOptions_ck_2_" + str(self.option_num))
        self.pw_figureOptions_ck_2[self.option_num].setStyleSheet("QCheckBox {\n"
        "    spacing: 5px;\n"
        "    color: black;\n"
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
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_ck_2[self.option_num], 1, 1, 1, 1)
        self.pw_figureOptions_gl_3[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
        self.pw_figureOptions_bt_7.append(QtWidgets.QToolButton())
        self.pw_figureOptions_bt_7[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_7[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_7[self.option_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_figureOptions_bt_7[self.option_num].setText("")
        self.pw_figureOptions_bt_7[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_7[self.option_num].setIconSize(QtCore.QSize(23, 23))
        self.pw_figureOptions_bt_7[self.option_num].setAutoRaise(False)
        self.pw_figureOptions_bt_7[self.option_num].setObjectName("pw_figureOptions_bt_7_" + str(self.option_num))
        self.pw_figureOptions_gl_3[self.option_num].addWidget(self.pw_figureOptions_bt_7[self.option_num], 1, 3, 1, 1)
        self.pw_figureOptions_gl_3[self.option_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 4, 1, 1)
        self.pw_figureOptions_hl_4[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_4[self.option_num])
        if self.option_num < 1:
            self.figure_options_sliders()
        self.pw_figureOptions_vl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.pw_figureOptions_li_1.append(QtWidgets.QFrame())
        self.pw_figureOptions_li_1[self.option_num].setFrameShape(QtWidgets.QFrame.HLine)
        self.pw_figureOptions_li_1[self.option_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pw_figureOptions_li_1[self.option_num].setObjectName("pw_figureOptions_li_1_" + str(self.option_num))
        self.pw_figureOptions_vl_1[self.option_num].addWidget(self.pw_figureOptions_li_1[self.option_num])
        self.pw_figureOptions_vl_1[self.option_num].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.pw_graphOptions_la.addLayout(self.pw_figureOptions_vl_1[self.option_num])
        self.pw_graphOptions_la.setAlignment(QtCore.Qt.AlignTop)
        self.populate_comboboxes_regular(self.pw_figureOptions_cb_1[self.option_num], self.font_list)
        self.populate_comboboxes_regular(self.pw_figureOptions_cb_3[self.option_num], self.font_list)
        self.populate_comboboxes_regular(self.pw_figureOptions_cb_5[self.option_num], self.font_list)
        temp = range(1,49,1)
        for index, item in enumerate(temp):
            temp[index] = str(item)
        self.populate_comboboxes_regular(self.pw_figureOptions_cb_2[self.option_num], temp)
        self.populate_comboboxes_regular(self.pw_figureOptions_cb_4[self.option_num], temp)
        self.populate_comboboxes_regular(self.pw_figureOptions_cb_6[self.option_num], temp)
        self.pw_figureOptions_cb_1[self.option_num].setCurrentIndex(self.pw_figureOptions_cb_1[self.option_num].findText(self.default_font))
        self.pw_figureOptions_cb_3[self.option_num].setCurrentIndex(self.pw_figureOptions_cb_3[self.option_num].findText(self.default_font))
        self.pw_figureOptions_cb_5[self.option_num].setCurrentIndex(self.pw_figureOptions_cb_5[self.option_num].findText(self.default_font))
        self.pw_figureOptions_cb_2[self.option_num].setCurrentIndex(11)
        self.pw_figureOptions_cb_4[self.option_num].setCurrentIndex(11)
        self.pw_figureOptions_cb_6[self.option_num].setCurrentIndex(11)
        self.pw_figureOptions_ck_1[self.option_num].stateChanged.connect(lambda: self.activate_grid_options())
        if self.plot_type_str == "multiple":
            xlabel = self.subplot_plot[self.option_num].axes.xaxis.get_label_text()
            ylabel = self.subplot_plot[self.option_num].axes.yaxis.get_label_text()
        elif self.plot_type_str == "single":
            xlabel = plt.axes().xaxis.get_label_text()
            ylabel = plt.axes().yaxis.get_label_text()
        self.pw_figureOptions_ln_2[self.option_num].setText(xlabel)
        self.pw_figureOptions_ln_2[self.option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_3[self.option_num].setText(ylabel)
        self.pw_figureOptions_ln_3[self.option_num].setCursorPosition(0)
        if self.option_num < 1:
            self.pw_figureOptions_sl_1[self.option_num].valueChanged.connect(lambda: self.update_slider_value())
            self.pw_figureOptions_sl_2[self.option_num].valueChanged.connect(lambda: self.update_slider_value())
            self.pw_figureOptions_sl_3[self.option_num].valueChanged.connect(lambda: self.update_slider_value())
            self.pw_figureOptions_sl_4[self.option_num].valueChanged.connect(lambda: self.update_slider_value())
            if self.plot_type_str == "multiple":
                self.pw_figureOptions_sl_5[self.option_num].valueChanged.connect(lambda: self.update_slider_value())
                self.pw_figureOptions_sl_5[self.option_num].setValue(40)
                self.pw_figureOptions_sl_5[self.option_num].setSliderPosition(40)
            self.pw_figureOptions_sl_1[self.option_num].setSliderPosition(13)
            self.pw_figureOptions_sl_2[self.option_num].setSliderPosition(8)
            self.pw_figureOptions_sl_3[self.option_num].setSliderPosition(5)
            self.pw_figureOptions_sl_4[self.option_num].setSliderPosition(11)
            self.pw_figureOptions_sl_1[self.option_num].setValue(13)
            self.pw_figureOptions_sl_2[self.option_num].setValue(8)
            self.pw_figureOptions_sl_3[self.option_num].setValue(5)
            self.pw_figureOptions_sl_4[self.option_num].setValue(11)

        if self.plot_type_str == "single":
            xlim_up = plt.axes().get_xlim()[1]
            xlim_dn = plt.axes().get_xlim()[0]
            ylim_up = plt.axes().get_ylim()[1]
            ylim_dn = plt.axes().get_ylim()[0]
            xstep = plt.axes().get_xticks()[1] - plt.axes().get_xticks()[0]
            ystep = plt.axes().get_yticks()[1] - plt.axes().get_yticks()[0]
            self.pw_figureOptions_ln_4[self.option_num].setText(str(xlim_dn))
            self.pw_figureOptions_ln_4[self.option_num].setCursorPosition(0)
            self.pw_figureOptions_ln_5[self.option_num].setText(str(xlim_up))
            self.pw_figureOptions_ln_5[self.option_num].setCursorPosition(0)
            self.pw_figureOptions_ln_6[self.option_num].setText(str(xstep))
            self.pw_figureOptions_ln_6[self.option_num].setCursorPosition(0)
            self.pw_figureOptions_ln_7[self.option_num].setText(str(ylim_dn))
            self.pw_figureOptions_ln_7[self.option_num].setCursorPosition(0)
            self.pw_figureOptions_ln_8[self.option_num].setText(str(ylim_up))
            self.pw_figureOptions_ln_8[self.option_num].setCursorPosition(0)
            self.pw_figureOptions_ln_9[self.option_num].setText(str(ystep))
            self.pw_figureOptions_ln_9[self.option_num].setCursorPosition(0)

        self.option_num +=1
        if self.plot_type_str == "multiple":
            for i in range(0, self.option_num):
                xlim_up = self.subplot_plot[i].axes.get_xlim()[1]
                xlim_dn = self.subplot_plot[i].axes.get_xlim()[0]
                ylim_up = self.subplot_plot[i].axes.get_ylim()[1]
                ylim_dn = self.subplot_plot[i].axes.get_ylim()[0]
                xstep = self.subplot_plot[i].axes.get_xticks()[1] - self.subplot_plot[i].axes.get_xticks()[0]
                ystep = self.subplot_plot[i].axes.get_yticks()[1] - self.subplot_plot[i].axes.get_yticks()[0]
                self.pw_figureOptions_ln_4[i].setText(str(xlim_dn))
                self.pw_figureOptions_ln_4[i].setCursorPosition(0)
                self.pw_figureOptions_ln_5[i].setText(str(xlim_up))
                self.pw_figureOptions_ln_5[i].setCursorPosition(0)
                self.pw_figureOptions_ln_6[i].setText(str(xstep))
                self.pw_figureOptions_ln_6[i].setCursorPosition(0)
                self.pw_figureOptions_ln_7[i].setText(str(ylim_dn))
                self.pw_figureOptions_ln_7[i].setCursorPosition(0)
                self.pw_figureOptions_ln_8[i].setText(str(ylim_up))
                self.pw_figureOptions_ln_8[i].setCursorPosition(0)
                self.pw_figureOptions_ln_9[i].setText(str(ystep))
                self.pw_figureOptions_ln_9[i].setCursorPosition(0)
    
    
    def figure_options_sliders(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - figure_options_sliders : plot_type_str '
                      + str(self.plot_type_str) + ', option_num ' + str(self.option_num))
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_figureOptions_hl_5.append(QtWidgets.QHBoxLayout())
        self.pw_figureOptions_hl_5[self.option_num].setObjectName("pw_figureOptions_hl_4_" + str(self.option_num))
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_20.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_20[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_20[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_20[self.option_num].setFont(font)
        self.pw_figureOptions_lb_20[self.option_num].setText("Set figure margins:")
        self.pw_figureOptions_lb_20[self.option_num].setObjectName("pw_figureOptions_lb_20_" + str(self.option_num))
        self.pw_figureOptions_lb_20[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_lb_20[self.option_num])
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_gl_4.append(QtWidgets.QGridLayout())
        self.pw_figureOptions_gl_4[self.option_num].setObjectName("pw_figureOptions_gl_4_" + str(self.option_num))
        self.pw_figureOptions_hl_5[self.option_num].addLayout(self.pw_figureOptions_gl_4[self.option_num])
        self.pw_figureOptions_lb_21.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_21[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_21[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_21[self.option_num].setFont(font)
        self.pw_figureOptions_lb_21[self.option_num].setText("Left:")
        self.pw_figureOptions_lb_21[self.option_num].setObjectName("pw_figureOptions_lb_21_" + str(self.option_num))
        self.pw_figureOptions_lb_21[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_21[self.option_num], 0, 0, 1, 1)
        self.pw_figureOptions_sl_1.append(QtWidgets.QSlider())
        self.pw_figureOptions_sl_1[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_1[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_1[self.option_num].setMinimum(0)
        self.pw_figureOptions_sl_1[self.option_num].setMaximum(40)
        self.pw_figureOptions_sl_1[self.option_num].setSingleStep(1)
        self.pw_figureOptions_sl_1[self.option_num].setPageStep(1)
        self.pw_figureOptions_sl_1[self.option_num].setOrientation(QtCore.Qt.Horizontal)
        self.pw_figureOptions_sl_1[self.option_num].setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_figureOptions_sl_1[self.option_num].setTickInterval(4)
        self.pw_figureOptions_sl_1[self.option_num].setObjectName("pw_figureOptions_sl_1_" + str(self.option_num))
        self.pw_figureOptions_sl_1[self.option_num].setStyleSheet("QSlider::groove:horizontal {\n"
        "border: 1px solid #999999;\n"
        "height: 1px;\n"
        "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "border: 1px solid #5c5c5c;\n"
        "width: 10px;\n"
        "margin: -5px 0;\n"
        "border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: rgb(0,0,200);\n"
        "}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_sl_1[self.option_num], 0, 1, 1, 1)
        self.pw_figureOptions_lb_22.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_22[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_22[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_22[self.option_num].setFont(font)
        self.pw_figureOptions_lb_22[self.option_num].setObjectName("pw_figureOptions_sl_1_" + str(self.option_num) + "lb_" + str(self.option_num))
        self.pw_figureOptions_lb_22[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_22[self.option_num], 0, 2, 1, 1)
        self.pw_figureOptions_gl_4[self.option_num].addItem(QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 3, 1, 1)
        self.pw_figureOptions_lb_23.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_23[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_23[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_23[self.option_num].setFont(font)
        self.pw_figureOptions_lb_23[self.option_num].setText("Right:")
        self.pw_figureOptions_lb_23[self.option_num].setObjectName("pw_figureOptions_lb_23_" + str(self.option_num))
        self.pw_figureOptions_lb_23[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_23[self.option_num], 0, 4, 1, 1)
        self.pw_figureOptions_sl_2.append(QtWidgets.QSlider())
        self.pw_figureOptions_sl_2[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_2[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_2[self.option_num].setMinimum(0)
        self.pw_figureOptions_sl_2[self.option_num].setMaximum(40)
        self.pw_figureOptions_sl_2[self.option_num].setSingleStep(1)
        self.pw_figureOptions_sl_2[self.option_num].setPageStep(1)
        self.pw_figureOptions_sl_2[self.option_num].setProperty("value", 0)
        self.pw_figureOptions_sl_2[self.option_num].setSliderPosition(0)
        self.pw_figureOptions_sl_2[self.option_num].setOrientation(QtCore.Qt.Horizontal)
        self.pw_figureOptions_sl_2[self.option_num].setInvertedAppearance(True)
        self.pw_figureOptions_sl_2[self.option_num].setInvertedControls(False)
        self.pw_figureOptions_sl_2[self.option_num].setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_figureOptions_sl_2[self.option_num].setTickInterval(4)
        self.pw_figureOptions_sl_2[self.option_num].setObjectName("pw_figureOptions_sl_2_" + str(self.option_num))
        self.pw_figureOptions_sl_2[self.option_num].setStyleSheet("QSlider::groove:horizontal {\n"
        "border: 1px solid #999999;\n"
        "height: 1px;\n"
        "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "border: 1px solid #5c5c5c;\n"
        "width: 10px;\n"
        "margin: -5px 0;\n"
        "border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "background: rgb(0,0,200);\n"
        "}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_sl_2[self.option_num], 0, 5, 1, 1)
        self.pw_figureOptions_lb_24.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_24[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_24[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_24[self.option_num].setFont(font)
        self.pw_figureOptions_lb_24[self.option_num].setObjectName("pw_figureOptions_sl_2_" + str(self.option_num) + "lb_" + str(self.option_num))
        self.pw_figureOptions_lb_24[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_24[self.option_num], 0, 6, 1, 1)
        self.pw_figureOptions_lb_25.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_25[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_25[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_25[self.option_num].setFont(font)
        self.pw_figureOptions_lb_25[self.option_num].setText("Top:")
        self.pw_figureOptions_lb_25[self.option_num].setObjectName("pw_figureOptions_lb_25_" + str(self.option_num))
        self.pw_figureOptions_lb_25[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_25[self.option_num], 1, 0, 1, 1)
        self.pw_figureOptions_sl_3.append(QtWidgets.QSlider())
        self.pw_figureOptions_sl_3[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_3[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_3[self.option_num].setMinimum(0)
        self.pw_figureOptions_sl_3[self.option_num].setMaximum(40)
        self.pw_figureOptions_sl_3[self.option_num].setSingleStep(1)
        self.pw_figureOptions_sl_3[self.option_num].setPageStep(1)
        self.pw_figureOptions_sl_3[self.option_num].setOrientation(QtCore.Qt.Horizontal)
        self.pw_figureOptions_sl_3[self.option_num].setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_figureOptions_sl_3[self.option_num].setTickInterval(4)
        self.pw_figureOptions_sl_3[self.option_num].setObjectName("pw_figureOptions_sl_3_" + str(self.option_num))
        self.pw_figureOptions_sl_3[self.option_num].setStyleSheet("QSlider::groove:horizontal {\n"
        "border: 1px solid #999999;\n"
        "height: 1px;\n"
        "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "border: 1px solid #5c5c5c;\n"
        "width: 10px;\n"
        "margin: -5px 0;\n"
        "border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: rgb(0,0,200);\n"
        "}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_sl_3[self.option_num], 1, 1, 1, 1)
        self.pw_figureOptions_lb_26.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_26[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_26[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_26[self.option_num].setFont(font)
        self.pw_figureOptions_lb_26[self.option_num].setObjectName("pw_figureOptions_sl_3_" + str(self.option_num) + "lb_" + str(self.option_num))
        self.pw_figureOptions_lb_26[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_26[self.option_num], 1, 2, 1, 1)
        self.pw_figureOptions_gl_4[self.option_num].addItem(QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 3, 1, 1)
        self.pw_figureOptions_lb_27.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_27[self.option_num].setMinimumSize(QtCore.QSize(0, 27))
        self.pw_figureOptions_lb_27[self.option_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_figureOptions_lb_27[self.option_num].setFont(font)
        self.pw_figureOptions_lb_27[self.option_num].setText("Bottom:")
        self.pw_figureOptions_lb_27[self.option_num].setObjectName("pw_figureOptions_lb_27_" + str(self.option_num))
        self.pw_figureOptions_lb_27[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_27[self.option_num], 1, 4, 1, 1)
        self.pw_figureOptions_sl_4.append(QtWidgets.QSlider())
        self.pw_figureOptions_sl_4[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_4[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_figureOptions_sl_4[self.option_num].setMinimum(0)
        self.pw_figureOptions_sl_4[self.option_num].setMaximum(40)
        self.pw_figureOptions_sl_4[self.option_num].setSingleStep(1)
        self.pw_figureOptions_sl_4[self.option_num].setPageStep(1)
        self.pw_figureOptions_sl_4[self.option_num].setProperty("value", 0)
        self.pw_figureOptions_sl_4[self.option_num].setSliderPosition(0)
        self.pw_figureOptions_sl_4[self.option_num].setOrientation(QtCore.Qt.Horizontal)
        self.pw_figureOptions_sl_4[self.option_num].setInvertedAppearance(True)
        self.pw_figureOptions_sl_4[self.option_num].setInvertedControls(False)
        self.pw_figureOptions_sl_4[self.option_num].setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_figureOptions_sl_4[self.option_num].setTickInterval(4)
        self.pw_figureOptions_sl_4[self.option_num].setObjectName("pw_figureOptions_sl_4_" + str(self.option_num))
        self.pw_figureOptions_sl_4[self.option_num].setStyleSheet("QSlider::groove:horizontal {\n"
        "border: 1px solid #999999;\n"
        "height: 1px;\n"
        "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "border: 1px solid #5c5c5c;\n"
        "width: 10px;\n"
        "margin: -5px 0;\n"
        "border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "background: rgb(0,0,200);\n"
        "}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_sl_4[self.option_num], 1, 5, 1, 1)
        self.pw_figureOptions_lb_28.append(QtWidgets.QLabel())
        self.pw_figureOptions_lb_28[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_28[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_28[self.option_num].setFont(font)
        self.pw_figureOptions_lb_28[self.option_num].setObjectName("pw_figureOptions_sl_4_" + str(self.option_num) + "lb_" + str(self.option_num))
        self.pw_figureOptions_lb_28[self.option_num].setStyleSheet("QLabel {color: black;}")
        self.pw_figureOptions_gl_4[self.option_num].addWidget(self.pw_figureOptions_lb_28[self.option_num], 1, 6, 1, 1)
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_8.append(QtWidgets.QToolButton())
        self.pw_figureOptions_bt_8[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_8[self.option_num].setMaximumSize(QtCore.QSize(27, 24))
        self.pw_figureOptions_bt_8[self.option_num].setStyleSheet("QToolButton {\n"
        "border: 1px solid transparent;\n"
        "background-color: transparent;\n"
        "width: 27px;\n"
        "height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "border: none;\n"
        "}")
        self.pw_figureOptions_bt_8[self.option_num].setText("")
        self.pw_figureOptions_bt_8[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_8[self.option_num].setIconSize(QtCore.QSize(23, 23))
        self.pw_figureOptions_bt_8[self.option_num].setAutoRaise(False)
        self.pw_figureOptions_bt_8[self.option_num].setObjectName("pw_figureOptions_bt_8_" + str(self.option_num))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_bt_8[self.option_num])
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_5[self.option_num])
        
        if self.plot_type_str == "multiple":
            self.pw_figureOptions_hl_12.append(QtWidgets.QHBoxLayout())
            self.pw_figureOptions_hl_12[self.option_num].setObjectName("pw_figureOptions_hl_12")
            self.pw_figureOptions_hl_12[self.option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
            self.pw_figureOptions_lb_29.append(QtWidgets.QLabel())
            self.pw_figureOptions_lb_29[self.option_num].setMinimumSize(QtCore.QSize(170, 27))
            self.pw_figureOptions_lb_29[self.option_num].setMaximumSize(QtCore.QSize(170, 27))
            self.pw_figureOptions_lb_29[self.option_num].setFont(font)
            self.pw_figureOptions_lb_29[self.option_num].setObjectName("pw_figureOptions_lb_29")
            self.pw_figureOptions_lb_29[self.option_num].setText("Set subplot interval:")
            self.pw_figureOptions_lb_29[self.option_num].setStyleSheet("QLabel {color: black;}")
            self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_lb_29[self.option_num])
            self.pw_figureOptions_sl_5.append(QtWidgets.QSlider())
            self.pw_figureOptions_sl_5[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
            self.pw_figureOptions_sl_5[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
            self.pw_figureOptions_sl_5[self.option_num].setStyleSheet("QSlider::groove:horizontal {\n"
            "border: 1px solid #999999;\n"
            "height: 1px;\n"
            "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
            "margin: 2px 0;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
            "border: 1px solid #5c5c5c;\n"
            "width: 10px;\n"
            "margin: -5px 0;\n"
            "border-radius: 5px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "background: rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "background: rgb(0,0,200);\n"
            "}")
            self.pw_figureOptions_sl_5[self.option_num].setMinimum(0)
            self.pw_figureOptions_sl_5[self.option_num].setMaximum(100)
            self.pw_figureOptions_sl_5[self.option_num].setSingleStep(1)
            self.pw_figureOptions_sl_5[self.option_num].setPageStep(1)
            self.pw_figureOptions_sl_5[self.option_num].setOrientation(QtCore.Qt.Horizontal)
            self.pw_figureOptions_sl_5[self.option_num].setTickPosition(QtWidgets.QSlider.TicksBelow)
            self.pw_figureOptions_sl_5[self.option_num].setTickInterval(10)
            self.pw_figureOptions_sl_5[self.option_num].setObjectName("pw_figureOptions_sl_5")
            self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_sl_5[self.option_num])
            self.pw_figureOptions_lb_30.append(QtWidgets.QLabel())
            self.pw_figureOptions_lb_30[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_30[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_30[self.option_num].setFont(font)
            self.pw_figureOptions_lb_30[self.option_num].setObjectName("pw_figureOptions_lb_30")
            self.pw_figureOptions_lb_30[self.option_num].setText("TMP")
            self.pw_figureOptions_lb_30[self.option_num].setStyleSheet("QLabel {color: black;}")
            self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_lb_30[self.option_num])
            self.pw_figureOptions_bt_9.append(QtWidgets.QToolButton())
            self.pw_figureOptions_bt_9[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
            self.pw_figureOptions_bt_9[self.option_num].setMaximumSize(QtCore.QSize(27, 24))
            self.pw_figureOptions_bt_9[self.option_num].setStyleSheet("QToolButton {\n"
            "border: 1px solid transparent;\n"
            "background-color: transparent;\n"
            "width: 27px;\n"
            "height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "border: none;\n"
            "}")
            self.pw_figureOptions_bt_9[self.option_num].setText("")
            self.pw_figureOptions_bt_9[self.option_num].setIcon(icon)
            self.pw_figureOptions_bt_9[self.option_num].setIconSize(QtCore.QSize(23, 23))
            self.pw_figureOptions_bt_9[self.option_num].setAutoRaise(False)
            self.pw_figureOptions_bt_9[self.option_num].setObjectName("pw_figureOptions_bt_9")
            self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_bt_9[self.option_num])
            self.pw_figureOptions_hl_12[self.option_num].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
            self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_12[self.option_num])

    
    def plot_options(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_options : plot_type_str '
                      + str(self.plot_type_str) + ', option_num2 ' + str(self.option_num2))
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_plotOptions_vl_1.append(QtWidgets.QVBoxLayout())
        self.pw_plotOptions_vl_1[self.option_num2].setObjectName("pw_plotOptions_vl_1_" + str(self.option_num2))
        self.pw_plotOptions_hl_1.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_1[self.option_num2].setObjectName("pw_plotOptions_hl_1_" + str(self.option_num2))
        self.pw_plotOptions_lb_1.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_1[self.option_num2].setMinimumSize(QtCore.QSize(700, 27))
        self.pw_plotOptions_lb_1[self.option_num2].setMaximumSize(QtCore.QSize(700, 27))
        self.pw_plotOptions_lb_1[self.option_num2].setFont(font2)
        if self.plot_type_str == "single":
            self.pw_plotOptions_lb_1[self.option_num2].setText("Plot options - " + self.pw_yvariable_rl.currentText() + ":")
        else:
            self.pw_plotOptions_lb_1[self.option_num2].setText("Subplot " + str(self.option_num2 + 1) + ": Plot options - " + self.pw_multipleYvariable_rl[self.option_num2].currentText())
        self.pw_plotOptions_lb_1[self.option_num2].setObjectName("pw_plotOptions_lb_1_" + str(self.option_num2))
        self.pw_plotOptions_lb_1[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_1[self.option_num2].addWidget(self.pw_plotOptions_lb_1[self.option_num2])
        self.pw_plotOptions_hl_1[self.option_num2].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_1[self.option_num2])
        self.pw_plotOptions_hl_2.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_2[self.option_num2].setObjectName("pw_plotOptions_hl_2_" + str(self.option_num2))
        self.pw_plotOptions_hl_2[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_2.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_2[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_2[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_2[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_2[self.option_num2].setText("Line style:")
        self.pw_plotOptions_lb_2[self.option_num2].setObjectName("pw_plotOptions_lb_2_" + str(self.option_num2))
        self.pw_plotOptions_lb_2[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_2[self.option_num2].addWidget(self.pw_plotOptions_lb_2[self.option_num2])
        self.pw_plotOptions_hl_3.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_3[self.option_num2].setObjectName("pw_plotOptions_hl_3_" + str(self.option_num2))
        self.pw_plotOptions_rb_1.append(QtWidgets.QRadioButton())
        self.pw_plotOptions_rb_1[self.option_num2].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_rb_1[self.option_num2].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_rb_1[self.option_num2].setFont(font)
        self.pw_plotOptions_rb_1[self.option_num2].setText("Line")
        self.pw_plotOptions_rb_1[self.option_num2].setObjectName("pw_plotOptions_rb_1_" + str(self.option_num2))
        self.pw_plotOptions_rb_1[self.option_num2].setStyleSheet("QRadioButton {\n"
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
        self.pw_plotOptions_hl_3[self.option_num2].addWidget(self.pw_plotOptions_rb_1[self.option_num2])
        self.pw_plotOptions_rb_2.append(QtWidgets.QRadioButton())
        self.pw_plotOptions_rb_2[self.option_num2].setMinimumSize(QtCore.QSize(90, 27))
        self.pw_plotOptions_rb_2[self.option_num2].setMaximumSize(QtCore.QSize(90, 27))
        self.pw_plotOptions_rb_2[self.option_num2].setFont(font)
        self.pw_plotOptions_rb_2[self.option_num2].setText("Marker")
        self.pw_plotOptions_rb_2[self.option_num2].setObjectName("pw_plotOptions_rb_2_" + str(self.option_num2))
        self.pw_plotOptions_rb_2[self.option_num2].setStyleSheet("QRadioButton {\n"
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
        self.pw_plotOptions_hl_3[self.option_num2].addWidget(self.pw_plotOptions_rb_2[self.option_num2])
        self.pw_plotOptions_bg_1.append(QtWidgets.QButtonGroup())
        self.pw_plotOptions_bg_1[self.option_num2].setObjectName("pw_plotOptions_bg_1_" + str(self.option_num2))
        self.pw_plotOptions_bg_1[self.option_num2].addButton(self.pw_plotOptions_rb_1[self.option_num2])
        self.pw_plotOptions_bg_1[self.option_num2].addButton(self.pw_plotOptions_rb_2[self.option_num2])
        self.pw_plotOptions_hl_2[self.option_num2].addLayout(self.pw_plotOptions_hl_3[self.option_num2])
        self.pw_plotOptions_cb_1.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_plotOptions_cb_1[self.option_num2].setItemDelegate(itemDelegate)
        self.pw_plotOptions_cb_1[self.option_num2].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_plotOptions_cb_1[self.option_num2].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_plotOptions_cb_1[self.option_num2].setFont(font3)
        self.pw_plotOptions_cb_1[self.option_num2].setStyleSheet("QComboBox {\n"
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
        self.pw_plotOptions_cb_1[self.option_num2].setObjectName("pw_plotOptions_cb_1_" + str(self.option_num2))
        self.pw_plotOptions_hl_2[self.option_num2].addWidget(self.pw_plotOptions_cb_1[self.option_num2])
        self.pw_plotOptions_hl_2[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_1.append(QtWidgets.QToolButton())
        self.pw_plotOptions_bt_1[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_1[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_1[self.option_num2].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_plotOptions_bt_1[self.option_num2].setText("")
        self.pw_plotOptions_bt_1[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_1[self.option_num2].setIconSize(QtCore.QSize(23, 23))
        self.pw_plotOptions_bt_1[self.option_num2].setAutoRaise(False)
        self.pw_plotOptions_bt_1[self.option_num2].setObjectName("pw_plotOptions_bt_1_" + str(self.option_num2))
        self.pw_plotOptions_hl_2[self.option_num2].addWidget(self.pw_plotOptions_bt_1[self.option_num2])
        self.pw_plotOptions_hl_2[self.option_num2].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_2[self.option_num2])
        self.pw_plotOptions_hl_4.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_4[self.option_num2].setObjectName("pw_plotOptions_hl_4_" + str(self.option_num2))
        self.pw_plotOptions_hl_4[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_3.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_3[self.option_num2].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_3[self.option_num2].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_3[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_3[self.option_num2].setText("Line / Marker color:")
        self.pw_plotOptions_lb_3[self.option_num2].setObjectName("pw_plotOptions_lb_3_" + str(self.option_num2))
        self.pw_plotOptions_lb_3[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_4[self.option_num2].addWidget(self.pw_plotOptions_lb_3[self.option_num2])
        self.pw_plotOptions_cb_2.append(QtWidgets.QComboBox())
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_plotOptions_cb_2[self.option_num2].setItemDelegate(itemDelegate)
        self.pw_plotOptions_cb_2[self.option_num2].setMinimumSize(QtCore.QSize(170, 27))
        self.pw_plotOptions_cb_2[self.option_num2].setMaximumSize(QtCore.QSize(170, 27))
        self.pw_plotOptions_cb_2[self.option_num2].setFont(font3)
        self.pw_plotOptions_cb_2[self.option_num2].setStyleSheet("QComboBox {\n"
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
        self.pw_plotOptions_cb_2[self.option_num2].setObjectName("pw_plotOptions_cb_2_" + str(self.option_num2))
        self.pw_plotOptions_hl_4[self.option_num2].addWidget(self.pw_plotOptions_cb_2[self.option_num2])
        self.pw_plotOptions_hl_5.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_5[self.option_num2].setObjectName("pw_plotOptions_hl_5_" + str(self.option_num2))
        self.pw_plotOptions_hl_5[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_8.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_8[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_8[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_8[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_8[self.option_num2].setText("RGB code:")
        self.pw_plotOptions_lb_8[self.option_num2].setObjectName("pw_plotOptions_lb_8_" + str(self.option_num2))
        self.pw_plotOptions_lb_8[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_lb_8[self.option_num2].hide()
        self.pw_plotOptions_hl_5[self.option_num2].addWidget(self.pw_plotOptions_lb_8[self.option_num2])
        self.pw_plotOptions_ln_3.append(QtWidgets.QLineEdit())
        self.pw_plotOptions_ln_3[self.option_num2].setMinimumSize(QtCore.QSize(130, 27))
        self.pw_plotOptions_ln_3[self.option_num2].setMaximumSize(QtCore.QSize(130, 27))
        self.pw_plotOptions_ln_3[self.option_num2].setFont(font3)
        self.pw_plotOptions_ln_3[self.option_num2].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_plotOptions_ln_3[self.option_num2].setObjectName("pw_plotOptions_ln_3_" + str(self.option_num2))
        self.pw_plotOptions_ln_3[self.option_num2].hide()
        self.pw_plotOptions_hl_5[self.option_num2].addWidget(self.pw_plotOptions_ln_3[self.option_num2])
        self.pw_plotOptions_hl_4[self.option_num2].addLayout(self.pw_plotOptions_hl_5[self.option_num2])
        self.pw_plotOptions_bt_2.append(QtWidgets.QToolButton())
        self.pw_plotOptions_bt_2[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_2[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_2[self.option_num2].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_plotOptions_bt_2[self.option_num2].setText("")
        self.pw_plotOptions_bt_2[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_2[self.option_num2].setIconSize(QtCore.QSize(23, 23))
        self.pw_plotOptions_bt_2[self.option_num2].setAutoRaise(False)
        self.pw_plotOptions_bt_2[self.option_num2].setObjectName("pw_plotOptions_bt_2_" + str(self.option_num2))
        self.pw_plotOptions_hl_4[self.option_num2].addWidget(self.pw_plotOptions_bt_2[self.option_num2])
        self.pw_plotOptions_hl_4[self.option_num2].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_4[self.option_num2])
        self.pw_plotOptions_hl_6.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_6[self.option_num2].setObjectName("pw_plotOptions_hl_6_" + str(self.option_num2))
        self.pw_plotOptions_hl_6[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_4.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_4[self.option_num2].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_4[self.option_num2].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_4[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_4[self.option_num2].setText("Line width / Marker size:")
        self.pw_plotOptions_lb_4[self.option_num2].setObjectName("pw_plotOptions_lb_4_" + str(self.option_num2))
        self.pw_plotOptions_lb_4[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_6[self.option_num2].addWidget(self.pw_plotOptions_lb_4[self.option_num2])
        self.pw_plotOptions_ln_1.append(QtWidgets.QLineEdit())
        self.pw_plotOptions_ln_1[self.option_num2].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_1[self.option_num2].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_1[self.option_num2].setFont(font3)
        self.pw_plotOptions_ln_1[self.option_num2].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_plotOptions_ln_1[self.option_num2].setObjectName("pw_plotOptions_ln_1_" + str(self.option_num2))
        self.pw_plotOptions_hl_6[self.option_num2].addWidget(self.pw_plotOptions_ln_1[self.option_num2])
        self.pw_plotOptions_hl_6[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_3.append(QtWidgets.QToolButton())
        self.pw_plotOptions_bt_3[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_3[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_3[self.option_num2].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_plotOptions_bt_3[self.option_num2].setText("")
        self.pw_plotOptions_bt_3[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_3[self.option_num2].setIconSize(QtCore.QSize(23, 23))
        self.pw_plotOptions_bt_3[self.option_num2].setAutoRaise(False)
        self.pw_plotOptions_bt_3[self.option_num2].setObjectName("pw_plotOptions_bt_3_" + str(self.option_num2))
        self.pw_plotOptions_hl_6[self.option_num2].addWidget(self.pw_plotOptions_bt_3[self.option_num2])
        self.pw_plotOptions_hl_6[self.option_num2].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_6[self.option_num2])
        self.pw_plotOptions_hl_7.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_7[self.option_num2].setObjectName("pw_plotOptions_hl_7_" + str(self.option_num2))
        self.pw_plotOptions_hl_7[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_5.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_5[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_5[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_5[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_5[self.option_num2].setText("Antialiased ?")
        self.pw_plotOptions_lb_5[self.option_num2].setObjectName("pw_plotOptions_lb_5_" + str(self.option_num2))
        self.pw_plotOptions_lb_5[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_7[self.option_num2].addWidget(self.pw_plotOptions_lb_5[self.option_num2])
        self.pw_plotOptions_ck_1.append(QtWidgets.QCheckBox())
        self.pw_plotOptions_ck_1[self.option_num2].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_1[self.option_num2].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_1[self.option_num2].setText("")
        self.pw_plotOptions_ck_1[self.option_num2].setObjectName("pw_plotOptions_ck_1_" + str(self.option_num2))
        self.pw_plotOptions_ck_1[self.option_num2].setStyleSheet("QCheckBox {\n"
        "    spacing: 5px;\n"
        "    color: black;\n"
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
        self.pw_plotOptions_hl_7[self.option_num2].addWidget(self.pw_plotOptions_ck_1[self.option_num2])
        self.pw_plotOptions_hl_7[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_4.append(QtWidgets.QToolButton())
        self.pw_plotOptions_bt_4[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_4[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_4[self.option_num2].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_plotOptions_bt_4[self.option_num2].setText("")
        self.pw_plotOptions_bt_4[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_4[self.option_num2].setIconSize(QtCore.QSize(23, 23))
        self.pw_plotOptions_bt_4[self.option_num2].setAutoRaise(False)
        self.pw_plotOptions_bt_4[self.option_num2].setObjectName("pw_plotOptions_bt_4_" + str(self.option_num2))
        self.pw_plotOptions_hl_7[self.option_num2].addWidget(self.pw_plotOptions_bt_4[self.option_num2])
        self.pw_plotOptions_hl_7[self.option_num2].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_7[self.option_num2])
        self.pw_plotOptions_hl_8.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_8[self.option_num2].setObjectName("pw_plotOptions_hl_8_" + str(self.option_num2))
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_6.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_6[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_6[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_6[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_6[self.option_num2].setText("Opacity ?")
        self.pw_plotOptions_lb_6[self.option_num2].setObjectName("pw_plotOptions_lb_6_" + str(self.option_num2))
        self.pw_plotOptions_lb_6[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_lb_6[self.option_num2])
        self.pw_plotOptions_ck_2.append(QtWidgets.QCheckBox())
        self.pw_plotOptions_ck_2[self.option_num2].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_2[self.option_num2].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_2[self.option_num2].setText("")
        self.pw_plotOptions_ck_2[self.option_num2].setObjectName("pw_plotOptions_ck_2_" + str(self.option_num2))
        self.pw_plotOptions_ck_2[self.option_num2].setStyleSheet("QCheckBox {\n"
        "    spacing: 5px;\n"
        "    color: black;\n"
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
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_ck_2[self.option_num2])
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_7.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_7[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_7[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_7[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_7[self.option_num2].setText("Percentage:")
        self.pw_plotOptions_lb_7[self.option_num2].setObjectName("pw_plotOptions_lb_7_" + str(self.option_num2))
        self.pw_plotOptions_lb_7[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_lb_7[self.option_num2])
        self.pw_plotOptions_ln_2.append(QtWidgets.QLineEdit())
        self.pw_plotOptions_ln_2[self.option_num2].setEnabled(False)
        self.pw_plotOptions_ln_2[self.option_num2].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_2[self.option_num2].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_2[self.option_num2].setFont(font3)
        self.pw_plotOptions_ln_2[self.option_num2].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color:  rgb(180, 180, 180);\n"
        "}")
        self.pw_plotOptions_ln_2[self.option_num2].setObjectName("pw_plotOptions_ln_2_" + str(self.option_num2))
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_ln_2[self.option_num2])
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_5.append(QtWidgets.QToolButton())
        self.pw_plotOptions_bt_5[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_5[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_5[self.option_num2].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_plotOptions_bt_5[self.option_num2].setText("")
        self.pw_plotOptions_bt_5[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_5[self.option_num2].setIconSize(QtCore.QSize(23, 23))
        self.pw_plotOptions_bt_5[self.option_num2].setAutoRaise(False)
        self.pw_plotOptions_bt_5[self.option_num2].setObjectName("pw_plotOptions_bt_5_" + str(self.option_num2))
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_bt_5[self.option_num2])
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_8[self.option_num2])
        
        self.pw_plotOptions_hl_9.append(QtWidgets.QHBoxLayout())
        self.pw_plotOptions_hl_9[self.option_num2].setObjectName("pw_plotOptions_hl_9_" + str(self.option_num2))
        self.pw_plotOptions_hl_9[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_9.append(QtWidgets.QLabel())
        self.pw_plotOptions_lb_9[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_9[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_9[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_9[self.option_num2].setText("Legend:")
        self.pw_plotOptions_lb_9[self.option_num2].setObjectName("pw_plotOptions_lb_9_" + str(self.option_num2))
        self.pw_plotOptions_lb_9[self.option_num2].setStyleSheet("QLabel {color: black;}")
        self.pw_plotOptions_hl_9[self.option_num2].addWidget(self.pw_plotOptions_lb_9[self.option_num2])
        self.pw_plotOptions_ln_4.append(QtWidgets.QLineEdit())
        self.pw_plotOptions_ln_4[self.option_num2].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_plotOptions_ln_4[self.option_num2].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_plotOptions_ln_4[self.option_num2].setFont(font3)
        self.pw_plotOptions_ln_4[self.option_num2].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.pw_plotOptions_ln_4[self.option_num2].setObjectName("pw_plotOptions_ln_4_" + str(self.option_num2))
        self.pw_plotOptions_hl_9[self.option_num2].addWidget(self.pw_plotOptions_ln_4[self.option_num2])
        self.pw_plotOptions_hl_9[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_6.append(QtWidgets.QToolButton())
        self.pw_plotOptions_bt_6[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_6[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_6[self.option_num2].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_plotOptions_bt_6[self.option_num2].setText("")
        self.pw_plotOptions_bt_6[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_6[self.option_num2].setIconSize(QtCore.QSize(23, 23))
        self.pw_plotOptions_bt_6[self.option_num2].setAutoRaise(False)
        self.pw_plotOptions_bt_6[self.option_num2].setObjectName("pw_plotOptions_bt_6_" + str(self.option_num2))
        self.pw_plotOptions_hl_9[self.option_num2].addWidget(self.pw_plotOptions_bt_6[self.option_num2])
        self.pw_plotOptions_hl_9[self.option_num2].addItem(QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_9[self.option_num2])
        self.pw_plotOptions_vl_1[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.pw_plotOptions_li_1.append(QtWidgets.QFrame())
        self.pw_plotOptions_li_1[self.option_num2].setFrameShape(QtWidgets.QFrame.HLine)
        self.pw_plotOptions_li_1[self.option_num2].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pw_plotOptions_li_1[self.option_num2].setObjectName("pw_plotOptions_li_1_" + str(self.option_num2))
        self.pw_plotOptions_vl_1[self.option_num2].addWidget(self.pw_plotOptions_li_1[self.option_num2])
        self.pw_plotOptions_vl_1[self.option_num2].addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.pw_plotOptions_la.addLayout(self.pw_plotOptions_vl_1[self.option_num2])
        self.pw_plotOptions_la.setAlignment(QtCore.Qt.AlignTop)
        self.pw_plotOptions_cb_2[self.option_num2].addItem("Make a choice...")
        self.populate_comboboxes_regular(self.pw_plotOptions_cb_2[self.option_num2], self.colors)
        self.pw_plotOptions_cb_2[self.option_num2].activated.connect(lambda: self.activate_line_color())
        self.pw_plotOptions_ck_2[self.option_num2].stateChanged.connect(lambda: self.activate_opacity_options())
        self.pw_plotOptions_rb_1[self.option_num2].clicked.connect(lambda: self.activate_line_style())
        self.pw_plotOptions_rb_2[self.option_num2].clicked.connect(lambda: self.activate_line_style())
        if self.plot_type_str == "multiple":
            try:
                line_style = self.line_styles_dict.keys()[self.line_styles_dict.values().
                                                          index(str(self.subplot_plot[self.option_num2].axes.lines[0].get_linestyle()))]
                self.pw_plotOptions_rb_1[self.option_num2].setChecked(True)
                line_styles = self.line_styles
            except ValueError:
                line_style = self.marker_styles_dict.keys()[self.marker_styles_dict.values().
                                                            index(str(self.subplot_plot[self.option_num2].axes.lines[0].get_linestyle()))]
                self.pw_plotOptions_rb_2[self.option_num2].setChecked(True)
                line_styles = self.marker_styles
            line_color = str(self.subplot_plot[self.option_num2].axes.lines[0].get_color())
            line_width = str(self.subplot_plot[self.option_num2].axes.lines[0].get_linewidth())
            line_antialiased = self.subplot_plot[self.option_num2].axes.lines[0].get_antialiased()
            if self.subplot_plot[self.option_num2].axes.lines[0].get_alpha():
                self.pw_plotOptions_ck_2[self.option_num2].setChecked(True)
            self.pw_plotOptions_ln_4[self.option_num2].setText(self.subplot_plot[self.option_num2].axes.lines[0].get_label())
        elif self.plot_type_str == "single":
            try:
                line_style = self.line_styles_dict.keys()[self.line_styles_dict.values().
                                                          index(str(plt.axes().lines[self.option_num2].
                                                                    get_linestyle()))]
                self.pw_plotOptions_rb_1[self.option_num2].setChecked(True)
                line_styles = self.line_styles
            except ValueError:
                line_style = self.marker_styles_dict.keys()[self.marker_styles_dict.values().
                                                          index(str(plt.axes().lines[self.option_num2].
                                                                    get_linestyle()))]
                self.pw_plotOptions_rb_2[self.option_num2].setChecked(True)
                line_styles = self.marker_styles
            line_color = str(plt.axes().lines[self.option_num2].get_color())
            line_width = str(plt.axes().lines[self.option_num2].get_linewidth())
            line_antialiased = plt.axes().lines[self.option_num2].get_antialiased()
            if plt.axes().lines[self.option_num2].get_alpha():
                self.pw_plotOptions_ck_2[self.option_num2].setChecked(True)
            self.pw_plotOptions_ln_4[self.option_num2].setText(plt.axes().lines[self.option_num2].get_label())
            
        self.pw_plotOptions_cb_1[self.option_num2].addItem("Make a choice...")
        self.populate_comboboxes_regular(self.pw_plotOptions_cb_1[self.option_num2], line_styles)
        self.pw_plotOptions_cb_1[self.option_num2].setCurrentIndex(self.pw_plotOptions_cb_1[self.option_num2].findText(line_style))
        if line_color in self.colors_dict.values():
            for key, value in self.colors_dict.iteritems():
                if value == line_color:
                    self.pw_plotOptions_cb_2[self.option_num2].setCurrentIndex(self.pw_plotOptions_cb_2[self.option_num2].findText(key))
                    break
        else:
            self.pw_plotOptions_cb_2[self.option_num2].setCurrentIndex(self.pw_plotOptions_cb_2[self.option_num2].findText("HEX Color"))
            self.pw_plotOptions_lb_8[self.option_num2].show()
            self.pw_plotOptions_ln_3[self.option_num2].show()
            self.pw_plotOptions_lb_8[self.option_num2].setText("HEX code:")
            self.pw_plotOptions_ln_3[self.option_num2].setText(line_color)
        self.pw_plotOptions_ln_1[self.option_num2].setText(line_width)
        self.pw_plotOptions_ck_1[self.option_num2].setChecked(line_antialiased)
        self.option_num2 +=1
        
        
    def update_figure_options(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - update_figure_options : plot_type_str '
                      + str(self.plot_type_str))
        if self.plot_type_str and self.pw_figureOptions_vl_1:
            if self.plot_type_str == "single":
                logging.debug('gui - plot_window_functions.py - PlotWindow - update_figure_options : '
                      + 'pw_figureOptions_ln_1[0].text() ' + str(self.pw_figureOptions_ln_1[0].text())
                      + ', pw_figureOptions_ln_3[0].text() ' + str(self.pw_figureOptions_ln_3[0].text())
                      + ', pw_figureOptions_ln_2[0].text() ' + str(self.pw_figureOptions_ln_2[0].text())
                      + ', pw_figureOptions_ln_6[0].text() ' + str(self.pw_figureOptions_ln_6[0].text())
                      + ', pw_figureOptions_ln_4[0].text() ' + str(self.pw_figureOptions_ln_4[0].text())
                      + ', pw_figureOptions_ln_5[0].text() ' + str(self.pw_figureOptions_ln_5[0].text())
                      + ', pw_figureOptions_ln_9[0].text() ' + str(self.pw_figureOptions_ln_9[0].text())
                      + ', pw_figureOptions_ln_7[0].text() ' + str(self.pw_figureOptions_ln_7[0].text())
                      + ', pw_figureOptions_ln_8[0].text() ' + str(self.pw_figureOptions_ln_8[0].text())
                      + ', pw_figureOptions_ln_4[0].text() ' + str(self.pw_figureOptions_ln_4[0].text())
                      + ', pw_figureOptions_ln_7[0].text() ' + str(self.pw_figureOptions_ln_7[0].text())
                      + ', pw_figureOptions_ck_1[0].isChecked() ' + str(self.pw_figureOptions_ck_1[0].isChecked())
                      + ', pw_figureOptions_cb_9[0].currentText() ' + str(self.pw_figureOptions_cb_9[0].currentText())
                      + ', pw_figureOptions_ln_10[0].text() ' + str(self.pw_figureOptions_ln_10[0].text())
                      + ', pw_figureOptions_cb_10[0].currentText() ' + str(self.pw_figureOptions_cb_10[0].currentText())
                      + ', pw_figureOptions_lb_22[0].text() ' + str(self.pw_figureOptions_lb_22[0].text())
                      + ', pw_figureOptions_lb_24[0].text() ' + str(self.pw_figureOptions_lb_24[0].text())
                      + ', pw_figureOptions_lb_26[0].text() ' + str(self.pw_figureOptions_lb_26[0].text())
                      + ', pw_figureOptions_lb_28[0].text() ' + str(self.pw_figureOptions_lb_28[0].text())
                      + ', pw_figureOptions_ck_2[0].isChecked() ' + str(self.pw_figureOptions_ck_2[0].isChecked()))
                if self.pw_figureOptions_ln_1[0].text():
                    font = {'fontname':str(self.pw_figureOptions_cb_1[0].currentText()),
                            'fontsize':int(self.pw_figureOptions_cb_2[0].currentText())}
                    plt.title(self.pw_figureOptions_ln_1[0].text(), y=1.04, **font)
                if self.pw_figureOptions_ln_3[0].text():
                    font = {'fontname':str(self.pw_figureOptions_cb_5[0].currentText()),
                            'fontsize':int(self.pw_figureOptions_cb_6[0].currentText())}       
                    plt.ylabel(self.pw_figureOptions_ln_3[0].text(), **font)
                if self.pw_figureOptions_ln_2[0].text():
                    font = {'fontname':str(self.pw_figureOptions_cb_3[0].currentText()),
                            'fontsize':int(self.pw_figureOptions_cb_4[0].currentText())}
                    plt.xlabel(self.pw_figureOptions_ln_2[0].text(), **font)
                try:
                    xstep = float(self.pw_figureOptions_ln_6[0].text())
                    xmin = float(self.pw_figureOptions_ln_4[0].text()) - xstep * 10
                    xmax = float(self.pw_figureOptions_ln_5[0].text()) + xstep * 10
                    plt.xticks(numpy.arange(xmin, xmax, xstep))
                except ValueError:
                    pass
                try:
                    ystep = float(self.pw_figureOptions_ln_9[0].text())
                    ymin = float(self.pw_figureOptions_ln_7[0].text()) - ystep * 10
                    ymax = float(self.pw_figureOptions_ln_8[0].text()) + ystep * 10
                    plt.yticks(numpy.arange(ymin, ymax, ystep))
                except ValueError:
                    pass
                try:
                    plt.xlim([float(self.pw_figureOptions_ln_4[0].text()), float(self.pw_figureOptions_ln_5[0].text())])
                except ValueError:
                    pass
                try:    
                    plt.ylim([float(self.pw_figureOptions_ln_7[0].text()), float(self.pw_figureOptions_ln_8[0].text())])
                except ValueError:
                    pass
                if self.pw_figureOptions_ck_1[0].isChecked():
                    args = {}
                    if self.pw_figureOptions_cb_9[0].currentText() != "Make a choice...":
                        args['linestyle'] = self.line_styles_dict[str(self.pw_figureOptions_cb_9[0].currentText())]
                    if self.pw_figureOptions_ln_10[0].text():
                        args['linewidth'] = float(self.pw_figureOptions_ln_10[0].text())
                    if self.pw_figureOptions_cb_10[0].currentText() != "Make a choice...":
                        args['color'] = self.colors_dict[str(self.pw_figureOptions_cb_10[0].currentText())]
                    plt.grid(b=True, **args)
                else:
                    plt.grid(b=False)
                left_margin = float(self.pw_figureOptions_lb_22[0].text()[:-1])/100
                right_margin = 1 - float(self.pw_figureOptions_lb_24[0].text()[:-1])/100
                top_margin = 1 - float(self.pw_figureOptions_lb_26[0].text()[:-1])/100
                bottom_margin = float(self.pw_figureOptions_lb_28[0].text()[:-1])/100
                plt.subplots_adjust(left=left_margin, right=right_margin, bottom=bottom_margin, top=top_margin)
                plt.gca().legend().draggable()
                if self.pw_figureOptions_ck_2[0].isChecked():
                    plt.gca().legend(prop={'family':self.default_font, 'size':'10'})
                    plt.gca().legend().set_visible(True)
                    plt.gca().legend().draggable()
                    self.legend_visibility = True
                else:
                    plt.gca().legend().set_visible(False)
                    self.legend_visibility = False
                intervall = 0.3
                     
            elif self.plot_type_str == "multiple":
                for i in range(0, len(self.pw_figureOptions_vl_1)):
                    logging.debug('gui.plot_window_functions.PlotWindow.update_figure_options invoked: '
                      + 'pw_figureOptions_ln_1[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_1[i].text())
                      + ', pw_figureOptions_ln_3[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_3[i].text())
                      + ', pw_figureOptions_ln_2[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_2[i].text())
                      + ', pw_figureOptions_ln_6[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_6[i].text())
                      + ', pw_figureOptions_ln_4[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_4[i].text())
                      + ', pw_figureOptions_ln_5[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_5[i].text())
                      + ', pw_figureOptions_ln_9[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_9[i].text())
                      + ', pw_figureOptions_ln_7[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_7[i].text())
                      + ', pw_figureOptions_ln_8[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_8[i].text())
                      + ', pw_figureOptions_ln_4[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_4[i].text())
                      + ', pw_figureOptions_ln_7[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_7[i].text())
                      + ', pw_figureOptions_ck_1[' + str(i) + '].isChecked() ' + str(self.pw_figureOptions_ck_1[i].isChecked())
                      + ', pw_figureOptions_cb_9[' + str(i) + '].currentText() ' + str(self.pw_figureOptions_cb_9[i].currentText())
                      + ', pw_figureOptions_ln_10[' + str(i) + '].text() ' + str(self.pw_figureOptions_ln_10[i].text())
                      + ', pw_figureOptions_cb_10[' + str(i) + '].currentText() ' + str(self.pw_figureOptions_cb_10[i].currentText())
                      + ', pw_figureOptions_lb_22[' + str(0) + '].text() ' + str(self.pw_figureOptions_lb_22[0].text())
                      + ', pw_figureOptions_lb_24[' + str(0) + '].text() ' + str(self.pw_figureOptions_lb_24[0].text())
                      + ', pw_figureOptions_lb_26[' + str(0) + '].text() ' + str(self.pw_figureOptions_lb_26[0].text())
                      + ', pw_figureOptions_lb_28[' + str(0) + '].text() ' + str(self.pw_figureOptions_lb_28[0].text())
                      + ', pw_figureOptions_ck_2[' + str(i) + '].isChecked() ' + str(self.pw_figureOptions_ck_2[i].isChecked()))
                    if self.pw_figureOptions_ln_1[i].text():
                        font = {'fontname':self.pw_figureOptions_cb_1[i].currentText(),
                                'fontsize':int(self.pw_figureOptions_cb_2[i].currentText())}
                        self.subplot_plot[i].set_title(self.pw_figureOptions_ln_1[i].text(), **font)
                    if self.pw_figureOptions_ln_3[i].text():
                        font = {'fontname':self.pw_figureOptions_cb_5[i].currentText(),
                                'fontsize':int(self.pw_figureOptions_cb_6[i].currentText())}
                        self.subplot_plot[i].set_ylabel(self.pw_figureOptions_ln_3[i].text(), **font)
                    if self.pw_figureOptions_ln_2[i].text():
                        font = {'fontname':self.pw_figureOptions_cb_3[i].currentText(),
                            'fontsize':int(self.pw_figureOptions_cb_4[i].currentText())}
                        self.subplot_plot[i].set_xlabel(self.pw_figureOptions_ln_2[i].text(), **font)
                    try:
                        xstep = float(self.pw_figureOptions_ln_6[i].text())
                        xmin = float(self.pw_figureOptions_ln_4[i].text()) - xstep * 10
                        xmax = float(self.pw_figureOptions_ln_5[i].text()) + xstep * 10
                        self.subplot_plot[i].set_xticks(numpy.arange(xmin, xmax, xstep))
                    except ValueError:
                        pass
                    try:
                        ystep = float(self.pw_figureOptions_ln_9[i].text())
                        ymin = float(self.pw_figureOptions_ln_7[i].text()) - ystep * 10
                        ymax = float(self.pw_figureOptions_ln_8[i].text()) + ystep * 10
                        self.subplot_plot[i].set_yticks(numpy.arange(ymin, ymax, ystep))
                    except ValueError:
                        pass
                    try:
                        self.subplot_plot[i].set_xlim([float(self.pw_figureOptions_ln_4[i].text()), 
                                                       float(self.pw_figureOptions_ln_5[i].text())])
                    except ValueError:
                        pass
                    try:    
                        self.subplot_plot[i].set_ylim([float(self.pw_figureOptions_ln_7[i].text()), 
                                                       float(self.pw_figureOptions_ln_8[i].text())])
                    except ValueError:
                        pass
                    if self.pw_figureOptions_ck_1[i].isChecked():
                        args = {}
                        if self.pw_figureOptions_cb_9[i].currentText() != "Make a choice...":
                            args['linestyle'] = self.line_styles_dict[str(self.pw_figureOptions_cb_9[i].currentText())]
                        if self.pw_figureOptions_ln_10[i].text():
                            args['linewidth'] = float(self.pw_figureOptions_ln_10[i].text())
                        if self.pw_figureOptions_cb_10[i].currentText() != "Make a choice...":
                            args['color'] = self.colors_dict[str(self.pw_figureOptions_cb_10[i].currentText())]
                        self.mult_grid_option[i] = args
                        self.subplot_plot[i].grid(b=True, **args)
                    else:
                        self.subplot_plot[i].grid(b=False)
                    if self.pw_figureOptions_ck_2[i].isChecked():
                        self.subplot_plot[i].legend(prop={'family':self.default_font, 'size':'10'})
                        self.subplot_plot[i].legend().set_visible(True)
                        self.subplot_plot[i].legend().draggable()
                        self.legend_visibility[i] = True
                    else:
                        self.subplot_plot[i].legend().set_visible(False)
                        self.legend_visibility[i] = False
                    intervall = float(self.pw_figureOptions_lb_30[0].text()[:-1])/100
                    self.mult_margin_left = float(self.pw_figureOptions_lb_22[0].text()[:-1])/100
                    self.mult_margin_right = 1 - float(self.pw_figureOptions_lb_24[0].text()[:-1])/100
                    self.mult_margin_bottom = float(self.pw_figureOptions_lb_28[0].text()[:-1])/100
                    self.mult_margin_top = 1 - float(self.pw_figureOptions_lb_26[0].text()[:-1])/100
                    self.mult_vert_space = float(self.pw_figureOptions_lb_30[0].text()[:-1])/100
            
            left_margin = float(self.pw_figureOptions_lb_22[0].text()[:-1])/100
            right_margin = 1 - float(self.pw_figureOptions_lb_24[0].text()[:-1])/100
            top_margin = 1 - float(self.pw_figureOptions_lb_26[0].text()[:-1])/100
            bottom_margin = float(self.pw_figureOptions_lb_28[0].text()[:-1])/100
            plt.subplots_adjust(left=left_margin, right=right_margin, bottom=bottom_margin, top=top_margin, hspace=intervall)    
            self.canvas.draw()
    
    
    def update_plot_options(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - update_plot_options : plot_type_str '
                      + str(self.plot_type_str))
        if self.plot_type_str and self.pw_plotOptions_vl_1:
            if self.plot_type_str == 'single':
                for i in range(self.option_num2):
                    logging.debug('gui - plot_window_functions.py - PlotWindow - update_plot_options : '
                      + 'pw_plotOptions_cb_1[' + str(i) + '].currentText() ' + str(self.pw_plotOptions_cb_1[i].currentText())
                      + ', pw_plotOptions_cb_2[' + str(i) + '].currentText() ' + str(self.pw_plotOptions_cb_2[i].currentText())
                      + ', pw_plotOptions_ln_3[' + str(i) + '].text() ' + str(self.pw_plotOptions_ln_3[i].text())
                      + ', pw_plotOptions_ln_1[' + str(i) + '].text() ' + str(self.pw_plotOptions_ln_1[i].text())
                      + ', pw_plotOptions_rb_1[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_rb_1[i].isChecked())
                      + ', pw_plotOptions_rb_2[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_rb_2[i].isChecked())
                      + ', pw_plotOptions_ck_1[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_ck_1[i].isChecked())
                      + ', pw_plotOptions_ck_2[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_ck_2[i].isChecked())
                      + ', pw_plotOptions_ln_4[' + str(i) + '].text() ' + str(self.pw_plotOptions_ln_4[i].text())
                      + ', pw_figureOptions_ck_2[0].isChecked() ' + str(self.pw_figureOptions_ck_2[0].isChecked()))
                      
                    if self.pw_plotOptions_cb_1[i].currentText() and self.pw_plotOptions_cb_1[i].currentText() != 'Make a choice...':
                        try:
                            line_style = self.line_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
                            plt.axes().lines[i].set_linestyle(line_style)
                            plt.axes().lines[i].set_marker(None)
                        except KeyError:
                            line_style = self.marker_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
                            plt.axes().lines[i].set_marker(line_style)
                            plt.axes().lines[i].set_linestyle('None')
                    if self.pw_plotOptions_cb_2[i].currentText() != 'Make a choice...' and self.pw_plotOptions_ln_3[i].text():
                        if str(self.pw_plotOptions_cb_2[i].currentText()) == 'HEX Color':
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                        elif str(self.pw_plotOptions_cb_2[i].currentText()) == 'RGB Color':
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                            line_color = line_color.replace(' ', '')
                            indexes = []
                            for index, item in enumerate(line_color):
                                if item == ',':
                                    indexes.append(index)
                            line_color = (float(float(line_color[0:indexes[0]])/255),
                                          float(float(line_color[indexes[0]+1:indexes[1]])/255),
                                          float(float(line_color[indexes[1]+1:])/255))
                        else:
                            line_color = self.colors_dict[str(self.pw_plotOptions_cb_2[i].currentText())]
                        plt.axes().lines[i].set_color(line_color)
                    if self.pw_plotOptions_ln_1[i].text():
                        line_width = float(self.pw_plotOptions_ln_1[i].text())
                        if self.pw_plotOptions_rb_1[i].isChecked():
                            plt.axes().lines[i].set_linewidth(line_width)
                        elif self.pw_plotOptions_rb_2[i].isChecked():
                            plt.axes().lines[i].set_markersize(line_width)
                    if self.pw_plotOptions_ck_1[i].isChecked():
                        plt.axes().lines[i].set_antialiased(True)
                    else:
                        plt.axes().lines[i].set_antialiased(False)
                    if self.pw_plotOptions_ck_2[i].isChecked() and self.pw_plotOptions_ln_2[i].text():
                        line_opacity = str(self.pw_plotOptions_ln_2[i].text())
                        if '%' in line_opacity:
                            line_opacity = line_opacity[:-1]
                        line_opacity = float(line_opacity)/100
                        plt.axes().lines[i].set_alpha(line_opacity)
                    else:
                        line_opacity = plt.axes().lines[i].get_alpha()
                        if line_opacity:
                            plt.axes().lines[i].get_alpha(1)
                    if self.pw_plotOptions_ln_4[i].text():
                        plt.axes().lines[i].set_label(str(self.pw_plotOptions_ln_4[i].text()))
                if self.pw_figureOptions_ck_2[0].isChecked(): 
                    plt.gca().legend().draggable()
            
            if self.plot_type_str == 'multiple':
                for i in range(self.option_num2):
                    logging.debug('gui - plot_window_functions.py - PlotWindow - update_plot_options : '
                      + 'pw_plotOptions_cb_1[' + str(i) + '].currentText() ' + str(self.pw_plotOptions_cb_1[i].currentText())
                      + ', pw_plotOptions_cb_2[' + str(i) + '].currentText() ' + str(self.pw_plotOptions_cb_2[i].currentText())
                      + ', pw_plotOptions_ln_3[' + str(i) + '].text() ' + str(self.pw_plotOptions_ln_3[i].text())
                      + ', pw_plotOptions_ln_1[' + str(i) + '].text() ' + str(self.pw_plotOptions_ln_1[i].text())
                      + ', pw_plotOptions_rb_1[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_rb_1[i].isChecked())
                      + ', pw_plotOptions_rb_2[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_rb_2[i].isChecked())
                      + ', pw_plotOptions_ck_1[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_ck_1[i].isChecked())
                      + ', pw_plotOptions_ck_2[' + str(i) + '].isChecked() ' + str(self.pw_plotOptions_ck_2[i].isChecked())
                      + ', pw_plotOptions_ln_4[' + str(i) + '].text()' + str(self.pw_plotOptions_ln_4[i].text())
                      + ', pw_figureOptions_ck_2[0].isChecked() ' + str(self.pw_figureOptions_ck_2[0].isChecked()))
                    if self.pw_plotOptions_cb_1[i].currentText() != 'Make a choice...':
                        try:
                            line_style = self.line_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]  
                            self.subplot_plot[i].axes.lines[0].set_linestyle(line_style)
                            self.subplot_plot[i].axes.lines[0].set_marker(None)
                        except KeyError:
                            line_style = self.marker_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
                            self.subplot_plot[i].axes.lines[0].set_linestyle('None')
                            self.subplot_plot[i].axes.lines[0].set_marker(line_style)
                    if self.pw_plotOptions_cb_2[i].currentText() != 'Make a choice...' and self.pw_plotOptions_ln_3[i].text():
                        if str(self.pw_plotOptions_cb_2[i].currentText()) == 'HEX Color':
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                        elif str(self.pw_plotOptions_cb_2[i].currentText()) == 'RGB Color':
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                            line_color = line_color.replace(' ', '')
                            indexes = []
                            for index, item in enumerate(line_color):
                                if item == ',':
                                    indexes.append(index)
                            line_color = (float(float(line_color[0:indexes[0]])/255),
                                          float(float(line_color[indexes[0]+1:indexes[1]])/255),
                                          float(float(line_color[indexes[1]+1:])/255))
                        else:
                            line_color = self.colors_dict[str(self.pw_plotOptions_cb_2[i].currentText())]
                        self.subplot_plot[i].axes.lines[0].set_color(line_color)
                        self.subplot_plot[i].legend(prop={'family':self.default_font, 'size':'10'})
                    if self.pw_plotOptions_ln_1[i].text():
                        line_width = float(self.pw_plotOptions_ln_1[i].text())
                        if self.pw_plotOptions_rb_1[i].isChecked():
                            self.subplot_plot[i].axes.lines[0].set_linewidth(line_width)
                        elif self.pw_plotOptions_rb_2[i].isChecked():
                            self.subplot_plot[i].axes.lines[0].set_markersize(line_width)
                    if self.pw_plotOptions_ck_1[i].isChecked():
                        self.subplot_plot[i].axes.lines[0].set_antialiased(True)
                    else:
                        self.subplot_plot[i].axes.lines[0].set_antialiased(False)
                    if self.pw_plotOptions_ck_2[i].isChecked() and self.pw_plotOptions_ln_2[i].text():
                        line_opacity = str(self.pw_plotOptions_ln_2[i].text())
                        if '%' in line_opacity:
                            line_opacity = line_opacity[:-1]
                        line_opacity = float(line_opacity)/100
                        self.subplot_plot[i].axes.lines[0].set_alpha(line_opacity)
                    else:
                        self.subplot_plot[i].axes.lines[0].set_alpha(1)
                    if self.pw_plotOptions_ln_4[i].text():
                        self.subplot_plot[i].axes.lines[0].set_label(str(self.pw_plotOptions_ln_4[i].text()))
                if self.pw_figureOptions_ck_2[0].isChecked(): 
                    leg = self.subplot_plot[i].legend(prop={'family':self.default_font, 'size':'10'})  
                    leg.draggable()
            
            self.canvas.draw()
           
    
    def activate_grid_options(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_grid_options : sender().objectName() '
                      + str(self.sender().objectName()) + ', sender().checkState() ' + str(self.sender().checkState()))
        index = int(self.sender().objectName()[22:])
        if self.sender().checkState() == 2:
            self.pw_figureOptions_cb_9[index].setEnabled(True)
            self.pw_figureOptions_cb_9[index].addItem("Make a choice...")
            self.populate_comboboxes_regular(self.pw_figureOptions_cb_9[index], self.line_styles)
            self.pw_figureOptions_cb_10[index].setEnabled(True)
            self.pw_figureOptions_cb_10[index].addItem("Make a choice...")
            self.populate_comboboxes_regular(self.pw_figureOptions_cb_10[index], self.colors_grid)
            self.pw_figureOptions_ln_10[index].setEnabled(True)
        else:
            self.pw_figureOptions_cb_9[index].setDisabled(True)
            self.pw_figureOptions_cb_9[index].clear()
            self.pw_figureOptions_cb_10[index].setDisabled(True)
            self.pw_figureOptions_cb_10[index].clear()
            self.pw_figureOptions_ln_10[index].setDisabled(True)
            self.pw_figureOptions_ln_10[index].setText("")
            
         
    def activate_opacity_options(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_opacity_options : sender().objectName() '
                      + str(self.sender().objectName()) + ', sender().checkState() ' + str(self.sender().checkState()))
        index = int(self.sender().objectName()[20:])
        if self.sender().checkState() == 2:
            self.pw_plotOptions_ln_2[index].setEnabled(True)
            self.pw_plotOptions_ln_2[index].setText("")
        else:    
            self.pw_plotOptions_ln_2[index].setDisabled(True)
            self.pw_plotOptions_ln_2[index].setText("")

    
    def activate_line_style(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_line_style : sender().objectName() '
                      + str(self.sender().objectName()) + ', sender().isChecked() ' + str(self.sender().isChecked()))
        index = int(self.sender().objectName()[20:])
        self.pw_plotOptions_cb_1[index].clear()
        if "pw_plotOptions_rb_1" in self.sender().objectName() and self.sender().isChecked() == True:
            self.pw_plotOptions_cb_1[index].addItem("Make a choice...")
            self.populate_comboboxes_regular(self.pw_plotOptions_cb_1[index], self.line_styles)
        elif "pw_plotOptions_rb_2" in self.sender().objectName() and self.sender().isChecked() == True:
            self.pw_plotOptions_cb_1[index].addItem("Make a choice...")
            self.populate_comboboxes_regular(self.pw_plotOptions_cb_1[index], self.marker_styles)
            
            
    def activate_line_color(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_line_color : sender().objectName() '
                      + str(self.sender().objectName()) + ', sender().currentText() ' + str(self.sender().currentText()))
        if self.sender().currentText() == "HEX Color" or self.sender().currentText() == "RGB Color":
            index = int(self.sender().objectName()[20:])
            self.pw_plotOptions_ln_3[index].setText("")
            self.pw_plotOptions_lb_8[index].show()
            self.pw_plotOptions_ln_3[index].show()
            self.pw_plotOptions_lb_8[index].setText(self.sender().currentText()[0:3] + " code:")
            self.pw_plotOptions_ln_3[index].setText("")
        else:
            index = int(self.sender().objectName()[20:])
            self.pw_plotOptions_lb_8[index].hide()
            self.pw_plotOptions_ln_3[index].hide()
            self.pw_plotOptions_lb_8[index].setText("")
            self.pw_plotOptions_ln_3[index].setText("TEMP")
    
    
    def update_slider_value(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - update_slider_value : sender().objectName() '
                      + str(self.sender().objectName()) + ', sender().value() ' + str(self.sender().value()))
        if self.sender().objectName() == "pw_figureOptions_sl_5":
            self.pw_figureOptions_lb_30[0].setText(str(self.sender().value()) + "%")
        else:
            label = self.findChild(QtWidgets.QLabel, str(self.sender().objectName() + "lb_" + str(self.sender().objectName()[22:])))
            label.setText(str(self.sender().value()) + "%")
            
            
    def populate_comboboxes(self, combobox):
        logging.debug('gui - plot_window_functions.py - PlotWindow - populate_comboboxes')
        combobox.addItem("Make a choice...")
        for key, _ in sorted(self.list_of_variables_and_attributes.iteritems()):
            combobox.addItem(key)
        

    def populate_comboboxes_regular(self, combobox, item_list):
        logging.debug('gui - plot_window_functions.py - PlotWindow - populate_comboboxes_regular')
        for item in item_list:
            combobox.addItem(item)

    
    def get_file_name(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        filter_types = "EPS Files (*.eps);;JPEG Files (*.jpg *.jpeg *.jpe);;PDF Files (*.pdf);;PNG Files (*.png *.pns);;TIFF Files (*.tif *.tiff)"
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, "Save File", "", filter_types)
        logging.debug('gui - plot_window_functions.py - PlotWindow - get_file_name : out_file_name '
                      + str(out_file_name) + ', out_file_ext ' + str(out_file_ext))
        return str(out_file_name), str(out_file_ext)
    
    
    def display_zoom_pan_warning(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - display_zoom_pan_warning : zoom_activated '
                      + str(self.zoom_activated) + ', pan_activated ' + str(self.pan_activated))
        entity = ''
        if self.zoom_activated:
            entity = 'Zoom'
        if self.pan_activated:
            entity = 'Pan'
        infoText = ('The ' + entity + ' function is actually active. Updating the Plot window while '
                    + 'the ' + entity + ' function is active can bring unexpected issues. Please rel'
                    + 'ease it before bringing modification to the Plot window')
        x = QtGui.QCursor.pos().x()
        y = QtGui.QCursor.pos().y()    
        x = x - 175
        y = y + 50
        self.infoWindow = MyInfo(infoText)
        self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setGeometry(x, y, 450, self.infoWindow.sizeHint().height())
        self.infoWindow.exec_()
        
        