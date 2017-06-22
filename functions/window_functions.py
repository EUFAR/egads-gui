# -*- coding: utf-8 -*-

import copy
import logging
import egads
import numpy
import ntpath
import platform
import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_globalattributewindow import Ui_globalAttributeWindow
from ui.Ui_variableattributewindow import Ui_variableAttributeWindow
from ui.Ui_processwindow import Ui_processingWindow
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_displaywindow import Ui_displayWindow
from ui.Ui_plotwindow import Ui_plotWindow
from ui.Ui_logwindow import Ui_Changelog
from ui.Ui_aboutwindow import Ui_aboutWindow
from ui.Ui_creationwindow import Ui_creationWindow
from ui.Ui_addcategory import Ui_Addcategory
from ui.Ui_fillwindow import Ui_fillWindow
from ui.Ui_filenamewindow import Ui_Addfilename
from ui.Ui_unitwindow import Ui_unitWindow
from ui.Ui_presavewindow import Ui_presaveWindow
from functions.gui_functions import clear_layout
import matplotlib
from babel import units
matplotlib.use('Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager


class MyGlobalAttributes(QtWidgets.QDialog, Ui_globalAttributeWindow):
    def __init__(self, global_attributes, open_file_ext):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.global_attributes = global_attributes
        self.open_file_ext = open_file_ext
        self.gw_showButton.clicked.connect(self.other_attribute)
        self.gw_okButton.clicked.connect(self.close_window_save)
        self.gw_cancelButton.clicked.connect(self.close_window)
        self.gw_button_1.clicked.connect(self.add_attribute)
        self.populate_attribute()
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_del = []
        self.add_attribute_num = 0
        self.attribute_num = 0
        self.combobox_items = ["comment",
                               "date_created",
                               "geospatial_lat_min",
                               "geospatial_lat_max",
                               "geospatial_lon_min",
                               "geospatial_lon_max",
                               "geospatial_vertical_min",
                               "geospatial_vertical_max",
                               "geospatial_vertical_positive",
                               "geospatial_vertical_units",
                               "history","project",
                               "references",
                               "time_coverage_start",
                               "time_coverage_end",
                               "time_coverage_duration"]
        self.populate_combobox()
        logging.info("MyGlobalAttribute - window ready")


    def close_window(self):
        del(self.global_attributes)
        logging.info("MyGlobalAttribute - window closing")
        self.close()
        
        
    def close_window_save(self):
        try:
            logging.info("MyGlobalAttribute - saving global attributes")
            self.global_attributes["Conventions"] = str(self.gw_conventions_ln.text())
            self.global_attributes["title"] = str(self.gw_title_ln.text())
            self.global_attributes["institution"] = str(self.gw_institution_ln.text())
            self.global_attributes["source"] = str(self.gw_source_ln.text())
            try:
                for index, widget in enumerate(self.list_label):
                    try:
                        self.global_attributes[str(widget.text()[:-1])] = float(self.list_line[index].text())
                    except ValueError:
                        self.global_attributes[str(widget.text()[:-1])] = str(self.list_line[index].text())
            except AttributeError:
                pass
            for index, widget in enumerate (self.add_list_label):
                try:
                    self.global_attributes[str(widget.text()[:-1])] = float(self.add_list_line[index].text())
                except ValueError:
                    self.global_attributes[str(widget.text()[:-1])] = str(self.add_list_line[index].text())
            self.close()
        except Exception:
            logging.exception("MyGlobalAttribute - Exception")
        
    
    def add_attribute(self):
            logging.info("MyGlobalAttribute - adding attribute")
            selected_attribute =  self.gw_addAttribute_rl.currentText()
            logging.info("MyGlobalAttribute -               " + selected_attribute)
            if selected_attribute == "Make a choice...":
                return
            else:
                font = QtGui.QFont()
                font.setFamily("fonts/SourceSansPro-Regular.ttf")
                font.setPointSize(10)
                font.setKerning(True)
                font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                font2 = QtGui.QFont()
                font2.setFamily("fonts/SourceSansPro-Regular.ttf")
                font2.setPointSize(9)
                font2.setKerning(True)
                font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                if selected_attribute == "Other..." or selected_attribute == "long_name_<xx>":
                    self.add_list_label.append(QtWidgets.QLineEdit())
                    self.add_list_label[self.add_attribute_num].setFrame(False)
                    self.add_list_label[self.add_attribute_num].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                    "\n"
                    "QLineEdit:disabled {background-color: rgb(200,200,200);}")
                    self.add_list_label[self.add_attribute_num].setFont(font2)
                    
                    if selected_attribute == "long_name_<xx>":
                        self.add_list_label[self.add_attribute_num].setText("long_name_")
                else:
                    self.add_list_label.append(QtWidgets.QLabel())
                    self.add_list_label[self.add_attribute_num].setFont(font)
                    self.add_list_label[self.add_attribute_num].setToolTip(selected_attribute)
                    self.add_list_label[self.add_attribute_num].setText(selected_attribute + ':')
                    self.add_list_label[self.add_attribute_num].setStyleSheet("QLabel {color: black;}")
                self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_label[self.add_attribute_num].setObjectName("add_label_" + str(self.add_attribute_num))
                self.gridLayout_3.addWidget(self.add_list_label[self.add_attribute_num], self.add_attribute_num, 0, 1, 1)
                self.add_list_line.append(QtWidgets.QLineEdit())
                self.add_list_line[self.add_attribute_num].setEnabled(True)
                self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(400, 27))
                self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_line[self.add_attribute_num].setPalette(palette)
                self.add_list_line[self.add_attribute_num].setFrame(False)
                self.add_list_line[self.add_attribute_num].setObjectName("add_line_" + str(self.add_attribute_num))
                self.add_list_line[self.add_attribute_num].setFocus(True)
                self.add_list_line[self.add_attribute_num].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                "\n"
                "QLineEdit:disabled {background-color: rgb(200,200,200);}")
                self.add_list_line[self.add_attribute_num].setFont(font2)
                self.gridLayout_3.addWidget(self.add_list_line[self.add_attribute_num], self.add_attribute_num, 1, 1, 1)
                self.add_list_del.append(QtWidgets.QToolButton())
                self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setText("")
                self.add_list_del[self.add_attribute_num].setIcon(icon)
                self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(23, 23))
                self.add_list_del[self.add_attribute_num].setAutoRaise(True)
                self.add_list_del[self.add_attribute_num].setObjectName("add_list_del_" + str(self.add_attribute_num))
                self.add_list_del[self.add_attribute_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.gridLayout_3.addWidget(self.add_list_del[self.add_attribute_num], self.add_attribute_num, 2, 1, 1)
                self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
                self.add_attribute_num += 1
                logging.info("MyGlobalAttribute - attribute added")
    
    
    def populate_attribute(self):
        logging.info("MyGlobalAttribute - populating attributes")
        try:
            try:
                self.gw_conventions_ln.setText(self.global_attributes["Conventions"])
                self.gw_title_ln.setCursorPosition(0)
            except KeyError:
                pass
            try:
                self.gw_title_ln.setText(self.global_attributes["title"])
                self.gw_title_ln.setCursorPosition(0)
            except KeyError:
                pass
            try:
                self.gw_institution_ln.setText(self.global_attributes["institution"])
                self.gw_institution_ln.setCursorPosition(0)
            except KeyError:
                pass
            try:
                self.gw_source_ln.setText(self.global_attributes["source"])
                self.gw_source_ln.setCursorPosition(0)
            except KeyError:
                pass
        except Exception:
            logging.exception("MyGlobalAttribute - Exception")
        
        
    def other_attribute(self):
        logging.info("MyGlobalAttribute - showing other attributes")
        if self.gw_showButton.text() == "Show other attributes":
            logging.info("MyGlobalAttribute -               show")
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            for key, value in sorted(self.global_attributes.iteritems()):
                if key != "Conventions" and key != "title" and key != "institution" and key != "source" and value != "deleted":
                    font = QtGui.QFont()
                    font.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font.setPointSize(10)
                    font.setKerning(True)
                    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    font2 = QtGui.QFont()
                    font2.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font2.setPointSize(9)
                    font2.setKerning(True)
                    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.list_label.append(QtWidgets.QLabel()) 
                    self.list_label[self.attribute_num].setFont(font)
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
                    self.list_label[self.attribute_num].setText(key + ':')
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_label[self.attribute_num].setStyleSheet("QLabel {color: black;}")
                    self.gridLayout_2.addWidget(self.list_label[self.attribute_num], self.attribute_num, 0, 1, 1)
                    self.list_line.append(QtWidgets.QLineEdit())
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(400, 27))
                    self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_line[self.attribute_num].setPalette(palette)
                    self.list_line[self.attribute_num].setFrame(False)
                    self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
                    self.list_line[self.attribute_num].setText(str(value))
                    self.list_line[self.attribute_num].setCursorPosition(0)
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                    "\n"
                    "QLineEdit:disabled {background-color: rgb(200,200,200);}")
                    self.list_line[self.attribute_num].setFont(font2)
                    self.gridLayout_2.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1, 1, 1)
                    self.list_del.append(QtWidgets.QToolButton())
                    self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setText("")
                    self.list_del[self.attribute_num].setIcon(icon)
                    self.list_del[self.attribute_num].setIconSize(QtCore.QSize(23, 23))
                    self.list_del[self.attribute_num].setAutoRaise(True)
                    self.list_del[self.attribute_num].setObjectName("list_del_" + str(self.attribute_num))
                    self.list_del[self.attribute_num].setStyleSheet("QToolButton {\n"
                    "    border: 1px solid transparent;\n"
                    "    background-color: transparent;\n"
                    "    width: 27px;\n"
                    "    height: 27px;\n"
                    "}\n"
                    "\n"
                    "QToolButton:flat {\n"
                    "    border: none;\n"
                    "}")
                    self.gridLayout_2.addWidget(self.list_del[self.attribute_num], self.attribute_num, 2, 1, 1)
                    self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setEnabled(False)
                    self.attribute_num += 1   
            if self.attribute_num != 0:
                self.gw_showButton.setText("Hide other attributes")
            else:
                logging.info("MyGlobalAttribute -               no more attribute")
                self.gw_showButton.setText("Hide other attributes")
                label = QtWidgets.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName("label")
                label.setText("No more attribute")
                self.gridLayout_2.addWidget(label, 0, 0, 1, 1)
        elif self.gw_showButton.text() == "Hide other attributes":
            logging.info("MyGlobalAttribute -               hide")
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            self.clear_layout(self.gridLayout_2)
            self.gw_showButton.setText("Show other attributes")
            
            
    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):   
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QtWidgets.QLayout):
                self.clear_layout(item.layout())
            layout.removeItem(item)
            
            
    def delete_attribute(self):
        logging.info("MyGlobalAttribute - deleting attribute")
        if "add" in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            logging.info("MyGlobalAttribute -                " + self.add_list_label[index].text())
            self.add_list_label[index].deleteLater()
            self.add_list_label.pop(index)
            self.add_list_line[index].deleteLater()
            self.add_list_line.pop(index)
            self.add_list_del[index].deleteLater()
            self.add_list_del.pop(index)
            self.add_attribute_num -= 1
            if len(self.add_list_del) > 0:
                for i in range(0, len(self.add_list_del)):
                    self.add_list_line[i].setObjectName(_fromUtf8("add_line_" + str(i)))
                    self.add_list_label[i].setObjectName(_fromUtf8("add_label_" + str(i)))
                    self.add_list_del[i].setObjectName(_fromUtf8("add_list_del_" + str(i)))
        else:
            index = int(self.sender().objectName()[9:]) 
            logging.info("MyGlobalAttribute -                " + self.list_label[index].text())
            self.global_attributes[str(self.list_label[index].text()[:-1])] = "deleted"
            self.list_label[index].deleteLater()
            self.list_label.pop(index)
            self.list_line[index].deleteLater()
            self.list_line.pop(index)
            self.list_del[index].deleteLater()
            self.list_del.pop(index)
            self.attribute_num -= 1
            if len(self.list_del) > 0:
                for i in range(0, len(self.list_del)):
                    self.list_line[i].setObjectName("line_" + str(i))
                    self.list_label[i].setObjectName("label_" + str(i))
                    self.list_del[i].setObjectName("list_del_" + str(i))
            
    
    def populate_combobox(self):
        self.gw_addAttribute_rl.addItem("Make a choice...")
        self.gw_addAttribute_rl.addItem("Other...")
        for item in self.combobox_items:
            try:
                self.global_attributes[item]
                if self.global_attributes[item] == "deleted":
                    self.gw_addAttribute_rl.addItem(item)
            except KeyError:
                self.gw_addAttribute_rl.addItem(item)


class MyVariableAttributes(QtWidgets.QDialog, Ui_variableAttributeWindow):
    def __init__(self, var, variable_attributes):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.variable = var
        self.setWindowTitle('Variable attributes - ' + self.variable)
        self.attributes = variable_attributes
        self.vw_showButton.clicked.connect(self.other_attribute)
        self.vw_okButton.clicked.connect(self.close_window_save)
        self.vw_cancelButton.clicked.connect(self.close_window)
        self.vw_button_1.clicked.connect(self.add_attribute)
        self.combobox_items = ["ancillary_variables",
                               "CalibrationCoefficients",
                               "Category",
                               "Comments",
                               "Dependencies",
                               "flag_masks",
                               "flag_meaning",
                               "flag_values",
                               "InstrumentCoordinates",
                               "InstrumentLocation",
                               "long_name",
                               "long_name_<xx>",
                               "Processor",
                               "SampledRate",
                               "standard_name",
                               "valid_max",
                               "valid_min",
                               "valid_range"]
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_del = []
        self.add_attribute_num = 0
        self.populate_attribute()
        self.populate_combobox()
        logging.info("MyVariableAttribute - window ready")
        
        
    def close_window(self):
        logging.info("MyVariableAttribute - window closing")
        del(self.attributes)
        self.close()
        
        
    def close_window_save(self):
        logging.info("MyVariableAttribute - saving variable attributes")
        try:
            for index, widget in enumerate(self.list_label):
                try:
                    self.attributes[str(widget.text()[:-1])] = float(self.list_line[index].text())
                except ValueError:
                    self.attributes[str(widget.text()[:-1])] = str(self.list_line[index].text())
        except AttributeError:
            pass
        for index, widget in enumerate (self.add_list_label):
            try:
                self.attributes[str(widget.text()[:-1])] = float(self.add_list_line[index].text())
            except ValueError:
                self.attributes[str(widget.text()[:-1])] = str(self.add_list_line[index].text())
        self.close()
        
    
    def populate_attribute(self):
        logging.info("MyVariableAttribute - populating attributes")
        try:
            self.vw_units_ln.setText(str(self.attributes["units"]))
            self.vw_units_ln.setCursorPosition(0)
        except KeyError:
            pass
        try:
            self.vw_fillValue_ln.setText(str(self.attributes["_FillValue"]))
            self.vw_fillValue_ln.setCursorPosition(0)
        except KeyError:
            pass
        
  
    def other_attribute(self):
        logging.info("MyVariableAttribute - showing other attributes")
        if self.vw_showButton.text() == "Show other attributes":
            logging.info("MyVariableAttribute -               show")
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            for key, value in sorted(self.attributes.iteritems()):
                if key != "units" and key != "_FillValue" and key != "var_name" and value != "deleted":
                    if isinstance(value, list):
                        value_string = ""
                        for string in value:
                            value_string += string + ", "
                        value = value_string[:-2]
                    font = QtGui.QFont()
                    font.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font.setPointSize(10)
                    font.setKerning(True)
                    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    font2 = QtGui.QFont()
                    font2.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font2.setPointSize(9)
                    font2.setKerning(True)
                    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.list_label.append(QtWidgets.QLabel()) 
                    self.list_label[self.attribute_num].setFont(font)
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
                    self.list_label[self.attribute_num].setText(key + ':')
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_label[self.attribute_num].setStyleSheet("QLabel {color: black;}")
                    self.gridLayout_2.addWidget(self.list_label[self.attribute_num], self.attribute_num, 0, 1, 1)
                    self.list_line.append(QtWidgets.QLineEdit())
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(400, 27))
                    self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_line[self.attribute_num].setPalette(palette)
                    self.list_line[self.attribute_num].setFrame(False)
                    self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
                    self.list_line[self.attribute_num].setText(str(value))
                    self.list_line[self.attribute_num].setCursorPosition(0)
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                    "\n"
                    "QLineEdit:disabled {background-color: rgb(200,200,200);}")
                    self.list_line[self.attribute_num].setFont(font2)
                    self.gridLayout_2.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1, 1, 1)
                    self.list_del.append(QtWidgets.QToolButton())
                    self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setText("")
                    self.list_del[self.attribute_num].setIcon(icon)
                    self.list_del[self.attribute_num].setIconSize(QtCore.QSize(23, 23))
                    self.list_del[self.attribute_num].setAutoRaise(True)
                    self.list_del[self.attribute_num].setObjectName("list_del_" + str(self.attribute_num))
                    self.list_del[self.attribute_num].setStyleSheet("QToolButton {\n"
                    "    border: 1px solid transparent;\n"
                    "    background-color: transparent;\n"
                    "    width: 27px;\n"
                    "    height: 27px;\n"
                    "}\n"
                    "\n"
                    "QToolButton:flat {\n"
                    "    border: none;\n"
                    "}")
                    self.gridLayout_2.addWidget(self.list_del[self.attribute_num], self.attribute_num, 2, 1, 1)
                    self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setEnabled(False)
                    self.attribute_num += 1     
            if self.attribute_num != 0:
                self.vw_showButton.setText("Hide other attributes")
            else:
                logging.info("MyVariableAttribute -               no more attribute")
                self.vw_showButton.setText("Hide other attributes")
                label = QtGui.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName("label")
                label.setText("No more attribute")
                self.gridLayout_2.addWidget(label, 0, 0, 1, 1)
        elif self.vw_showButton.text() == "Hide other attributes":
            logging.info("MyVariableAttribute -               hide")
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            self.clear_layout(self.gridLayout_2)
            self.vw_showButton.setText("Show other attributes")
    
    
    def add_attribute(self):
        logging.info("MyVariableAttribute - adding attribute")
        selected_attribute =  self.vw_addAttribute_rl.currentText()
        logging.info("MyVariableAttribute -               " + selected_attribute)
        if selected_attribute == "Make a choice...":
            return
        else:
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font2 = QtGui.QFont()
            font2.setFamily("fonts/SourceSansPro-Regular.ttf")
            font2.setPointSize(9)
            font2.setKerning(True)
            font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if selected_attribute == "Other..." or selected_attribute == "long_name_<xx>":
                self.add_list_label.append(QtWidgets.QLineEdit())
                self.add_list_label[self.add_attribute_num].setFrame(False)
                self.add_list_label[self.add_attribute_num].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                "\n"
                "QLineEdit:disabled {background-color: rgb(200,200,200);}")
                self.add_list_label[self.add_attribute_num].setFont(font2)
                
                if selected_attribute == "long_name_<xx>":
                    self.add_list_label[self.add_attribute_num].setText("long_name_")
            else:
                self.add_list_label.append(QtWidgets.QLabel())
                self.add_list_label[self.add_attribute_num].setFont(font)
                self.add_list_label[self.add_attribute_num].setToolTip(selected_attribute)
                self.add_list_label[self.add_attribute_num].setText(selected_attribute + ':')
                self.add_list_label[self.add_attribute_num].setStyleSheet("QLabel {color: black;}")
            self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
            self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.add_list_label[self.add_attribute_num].setObjectName("add_label_" + str(self.add_attribute_num))
            self.gridLayout_3.addWidget(self.add_list_label[self.add_attribute_num], self.add_attribute_num, 0, 1, 1)
            self.add_list_line.append(QtWidgets.QLineEdit())
            self.add_list_line[self.add_attribute_num].setEnabled(True)
            self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(400, 27))
            self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.add_list_line[self.add_attribute_num].setPalette(palette)
            self.add_list_line[self.add_attribute_num].setFrame(False)
            self.add_list_line[self.add_attribute_num].setObjectName("add_line_" + str(self.add_attribute_num))
            self.add_list_line[self.add_attribute_num].setFocus(True)
            self.add_list_line[self.add_attribute_num].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
            "\n"
            "QLineEdit:disabled {background-color: rgb(200,200,200);}")
            self.add_list_line[self.add_attribute_num].setFont(font2)
            self.gridLayout_3.addWidget(self.add_list_line[self.add_attribute_num], self.add_attribute_num, 1, 1, 1)
            self.add_list_del.append(QtWidgets.QToolButton())
            self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setText("")
            self.add_list_del[self.add_attribute_num].setIcon(icon)
            self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(23, 23))
            self.add_list_del[self.add_attribute_num].setAutoRaise(True)
            self.add_list_del[self.add_attribute_num].setObjectName("add_list_del_" + str(self.add_attribute_num))
            self.add_list_del[self.add_attribute_num].setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
            self.gridLayout_3.addWidget(self.add_list_del[self.add_attribute_num], self.add_attribute_num, 2, 1, 1)
            self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
            self.add_attribute_num += 1
            logging.info("MyVariableAttribute - attribute added")
    
    
    def delete_attribute(self):
        logging.info("MyVariableAttribute - deleting attribute")
        if "add" in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            logging.info("MyVariableAttribute -               " + self.add_list_label[index].text())
            self.gridLayout_3.removeWidget(self.add_list_label[index])
            self.gridLayout_3.removeWidget(self.add_list_line[index])
            self.gridLayout_3.removeWidget(self.add_list_del[index])
            self.add_list_label[index].deleteLater()
            self.add_list_label.pop(index)
            self.add_list_line[index].deleteLater()
            self.add_list_line.pop(index)
            self.add_list_del[index].deleteLater()
            self.add_list_del.pop(index)
            self.add_attribute_num -= 1
            row_number = self.gridLayout_3.count() / 3
            if row_number > 0:
                for i in range(0, row_number):
                    self.add_list_line[i].setObjectName("add_line_" + str(i))
                    self.add_list_label[i].setObjectName("add_label_" + str(i))
                    self.add_list_del[i].setObjectName("add_list_del_" + str(i))
        else:
            index = int(self.sender().objectName()[9:])
            logging.info("MyVariableAttribute -               " + self.list_label[index].text())
            self.attributes[str(self.list_label[index].text()[:-1])] = "deleted"
            self.gridLayout_2.removeWidget(self.list_label[index])
            self.gridLayout_2.removeWidget(self.list_line[index])
            self.gridLayout_2.removeWidget(self.list_del[index])
            self.list_label[index].deleteLater()
            self.list_label.pop(index)
            self.list_line[index].deleteLater()
            self.list_line.pop(index)
            self.list_del[index].deleteLater()
            self.list_del.pop(index)
            self.attribute_num -= 1
            if len(self.list_del) > 0:
                for i in range(0, len(self.list_del)):
                    self.list_line[i].setObjectName("line_" + str(i))
                    self.list_label[i].setObjectName("label_" + str(i))
                    self.list_del[i].setObjectName("list_del_" + str(i))
        logging.info("MyVariableAttribute - attribute deleted")
        
    
    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):   
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QtWidgets.QLayout):
                self.clear_layout(item.layout())
            layout.removeItem(item)
            
            
    def populate_combobox(self):
        self.vw_addAttribute_rl.addItem("Make a choice...")
        self.vw_addAttribute_rl.addItem("Other...")
        for item in self.combobox_items:
            try:
                self.attributes[item]
                if self.attributes[item] == "deleted":
                    self.vw_addAttribute_rl.addItem(item)
            except KeyError:
                self.vw_addAttribute_rl.addItem(item)
                
                
class MyProcessing(QtWidgets.QDialog, Ui_processingWindow):
    def __init__(self, list_of_algorithms, list_of_variables_and_attributes, list_of_new_variables_and_attributes):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
        self.hide_algorithm_information()
        self.list_of_algorithms = list_of_algorithms
        self.list_of_new_variables_and_attributes = list_of_new_variables_and_attributes
        self.list_of_variables_and_attributes = dict(list_of_variables_and_attributes, **list_of_new_variables_and_attributes)
        self.algorithm = ""
        self.list_of_inputs = []
        self.list_of_outputs = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_button_input = []
        self.input_num = 0
        self.list_label_output = []
        self.list_lineedit_output = []
        self.list_button_output = []
        self.output_num = 0
        self.input_activate = 0
        self.output_activate = 0
        self.types_for_combobox = ["vector", "array","vector_optional","array_optional"]
        self.aw_okButton.clicked.connect(self.close_window_save)
        self.aw_cancelButton.clicked.connect(self.close_window)
        self.aw_combobox_1.activated.connect(lambda: self.populate_combobox_2())
        self.aw_combobox_2.activated.connect(lambda: self.prepare_layout())
        self.aw_combobox_2.activated.connect(lambda: self.load_algorithm_information())
        self.tabWidget.currentChanged.connect(lambda: self.populate_input_output())
        self.populate_combobox_1()
        logging.info("MyProcessing - window ready")

    
    def close_window(self):
        del(self.list_of_variables_and_attributes)
        del(self.list_of_new_variables_and_attributes)
        logging.info("MyProcessing - window closing")
        self.close()
    
    
    def close_window_save(self):
        logging.info("MyProcessingWindow - processing variables")
        logging.info("MyProcessingWindow - algorithm:" + self.algorithm().metadata["Processor"])
        try:
            args = []
            for index, item in enumerate(self.list_combobox_input):
                try:
                    sublist = self.list_of_variables_and_attributes[item.currentText()]
                    args.append(sublist[3])
                    if index == 0:
                        dimension_out = sublist[2]
                except AttributeError:
                    args.append(float(item.text()))
                    if index == 0:
                        dimension_out = sublist[2]
            output = self.algorithm().run(*args)
            if isinstance(output, tuple):
                for index, item in enumerate(output):
                    metadata = {
                            "var_name":"",
                            "units":"",
                            "_FillValue":"",
                            "Processor":"",
                            "long_name":"",
                            "DateProcessed":"",
                            "standard_name":"",
                            "Category":"",
                            }
                    metadata["var_name"] = str(self.list_lineedit_output[index].text())
                    metadata["units"] = output[index].metadata["units"]
                    metadata["_FillValue"] = self.list_of_variables_and_attributes[self.list_combobox_input[0].currentText()]
                    metadata["Processor"] = self.algorithm().metadata["Processor"]
                    metadata["long_name"] = output[index].metadata["long_name"]
                    metadata["standard_name"] = output[index].metadata["standard_name"]
                    metadata["DateProcessed"] = output[index].metadata["DateProcessed"]
                    metadata["Category"] = output[index].metadata["Category"]
                    dimensions = dimension_out
                    self.list_of_new_variables_and_attributes[str(self.list_lineedit_output[index].text())] = [str(self.list_lineedit_output[index].text()),
                                                                                                       metadata,
                                                                                                       dimensions,
                                                                                                       output[index]]
                self.close()
            else:
                metadata = {
                            "var_name":"",
                            "units":"",
                            "_FillValue":"",
                            "Processor":"",
                            "long_name":"",
                            "DateProcessed":"",
                            "standard_name":"",
                            "Category":"",
                            }
                metadata["var_name"] = str(self.list_lineedit_output[0].text())
                metadata["units"] = output.metadata["units"]
                metadata["_FillValue"] = self.list_of_variables_and_attributes[self.list_combobox_input[0].currentText()][1]["_FillValue"]
                metadata["Processor"] = self.algorithm().metadata["Processor"]
                metadata["long_name"] = output.metadata["long_name"]
                metadata["standard_name"] = output[index].metadata["standard_name"]
                metadata["DateProcessed"] = output.metadata["DateProcessed"]
                metadata["Category"] = output.metadata["Category"]
                dimensions = dimension_out
                self.list_of_new_variables_and_attributes[str(self.list_lineedit_output[0].text())] = [str(self.list_lineedit_output[0].text()),
                                                                                                       metadata,
                                                                                                       dimensions,
                                                                                                       output]
                self.close()
        except Exception:
            logging.exception("MyProcessingWindow - Exception")
        

    def populate_combobox_1(self):
        logging.info("MyProcessingWindow - populating combobox 1")
        self.aw_combobox_1.addItem("Make a choice...")
        folder_list = []
        for key, _ in self.list_of_algorithms.iteritems():
            folder_list.append(key.title())
        folder_list = sorted(folder_list)
        self.aw_combobox_1.addItems(folder_list)
            
    
    def populate_combobox_2(self):
        logging.info("MyProcessingWindow - populating combobox 2")
        self.output_activate = 0
        self.input_activate = 0
        self.aw_okButton.setEnabled(False)
        self.aw_combobox_2.clear()
        if self.aw_combobox_1.currentText() == "Make a choice...":
            self.aw_combobox_2.setEnabled(False)
        else:
            self.aw_combobox_2.setEnabled(True)
            self.aw_combobox_2.addItem("Make a choice...")
            
            algorithm_list = self.list_of_algorithms[str(self.aw_combobox_1.currentText()).lower()]
            self.aw_combobox_2.addItems(sorted(algorithm_list))
            
            '''for item in self.list_of_algorithms:
                if item[0] == str(self.aw_combobox_1.currentText()).lower():
                    self.aw_combobox_2.addItem(item[1])'''
    
    
    def populate_input_output(self):
        if self.aw_combobox_2.currentText() != "Make a choice..." and self.aw_combobox_2.currentText() !="" :
            if self.tabWidget.currentIndex() == 1:
                logging.info("MyProcessingWindow - populating inputs")
                if len(self.list_label_input) == 0:
                    for index, item in enumerate(self.algorithm().metadata["Inputs"]):
                        font = QtGui.QFont()
                        font.setFamily("fonts/SourceSansPro-Regular.ttf")
                        font.setPointSize(10)
                        font.setKerning(True)
                        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                        font2 = QtGui.QFont()
                        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
                        font2.setPointSize(9)
                        font2.setKerning(True)
                        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.list_label_input.append(QtWidgets.QLabel())
                        self.list_label_input[self.input_num].setFont(font)
                        self.list_label_input[self.input_num].setText(item)
                        self.list_label_input[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
                        self.list_label_input[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
                        self.list_label_input[self.input_num].setObjectName("list_label_input_" + str(self.input_num))
                        self.list_label_input[self.input_num].setStyleSheet("QLabel {color: black;}")
                        self.input_layout_2.addWidget(self.list_label_input[self.input_num], self.input_num, 0, 1, 1)
                        self.input_layout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 
                                                    self.input_num, 1 ,1 ,1)
                        if self.algorithm().metadata["InputTypes"][index] in self.types_for_combobox or self.algorithm().metadata["InputTypes"][index] == "time":
                            self.list_combobox_input.append(QtWidgets.QComboBox())
                            self.list_combobox_input[self.input_num].setEnabled(True)
                            self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                            self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                            self.list_combobox_input[self.input_num].setFrame(False)
                            self.list_combobox_input[self.input_num].setFont(font2)
                            self.list_combobox_input[self.input_num].setStyleSheet("QComboBox {\n"
                            "    border: 1px solid #acacac;\n"
                            "    border-radius: 1px;\n"
                            "    padding-left: 5px;\n"
                            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                            "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                            "    color: black;\n"
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
                            self.list_combobox_input[self.input_num].setObjectName("list_combobox_input_" + str(self.input_num))
                            self.list_combobox_input[self.input_num].addItem("Make a choice...")
                            for _, sublist in self.list_of_variables_and_attributes.items():
                                if self.algorithm().metadata["InputTypes"][index] in self.types_for_combobox:
                                    if sublist[2] != 'deleted':
                                        self.list_combobox_input[self.input_num].addItem(sublist[1]["var_name"])
                                else:
                                    if "time" in sublist[1]["var_name"]:
                                        if sublist[2] != 'deleted':
                                            self.list_combobox_input[self.input_num].addItem(sublist[1]["var_name"])
                            self.list_combobox_input[self.input_num].activated.connect(lambda: self.activate_save_button())
                            self.input_layout_2.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                        else:
                            if "coeff.[" in self.algorithm().metadata["InputTypes"][index]:
                                line_edit_num = self.algorithm().metadata["InputTypes"][index][7:-1]
                                tmp = []
                                tmp_layout = QtWidgets.QHBoxLayout()
                                if "optional" in self.algorithm().metadata["InputTypes"][index]:
                                    tmp_layout.setObjectName("optional_tmp_layout")
                                else:
                                    tmp_layout.setObjectName("tmp_layout")
                                layout_factor = {2:4,3:5,4:5,5:5}
                                try:
                                    size = (300 / int(line_edit_num)) - layout_factor[int(line_edit_num)]
                                except KeyError:
                                    size = (300 / int(line_edit_num))
                                for i in range(int(line_edit_num)):
                                    tmp.append(QtWidgets.QLineEdit())
                                    tmp[i].setEnabled(True)
                                    tmp[i].setFrame(False)
                                    tmp[i].setFont(font)
                                    tmp[i].setObjectName(_fromUtf8("multi_list_lineedit_input_" + str(i)))
                                    tmp[i].setMinimumSize(QtCore.QSize(size, 27))
                                    tmp[i].setMaximumSize(QtCore.QSize(size, 27))
                                    tmp[i].setStyleSheet("QLineEdit {\n"
                                    "    border-radius: 3px;\n"
                                    "    padding: 1px 4px 1px 4px;\n"
                                    "    background-color:  rgb(240, 240, 240);\n"
                                    "}\n")
                                    tmp[i].textChanged.connect(lambda: self.activate_save_button())
                                    tmp_layout.addWidget(tmp[i])
                                self.list_combobox_input.append(tmp_layout)
                                self.input_layout_2.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                            else:
                                self.list_combobox_input.append(QtWidgets.QLineEdit())
                                self.list_combobox_input[self.input_num].setEnabled(True)
                                self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                                self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                                self.list_combobox_input[self.input_num].setFrame(False)
                                self.list_combobox_input[self.input_num].setFont(font2)
                                self.list_combobox_input[self.input_num].setStyleSheet("QLineEdit {\n"
                                "    border-radius: 3px;\n"
                                "    padding: 1px 4px 1px 4px;\n"
                                "    background-color:  rgb(240, 240, 240);\n"
                                "}\n")
                                self.list_combobox_input[self.input_num].textChanged.connect(lambda: self.activate_save_button())
                                if "optional" in self.algorithm().metadata["InputTypes"][index]:
                                    self.list_combobox_input[self.input_num].setObjectName("optional_list_lineedit_input_" 
                                                                                           + str(self.input_num))
                                else:
                                    self.list_combobox_input[self.input_num].setObjectName("list_lineedit_input_" 
                                                                                           + str(self.input_num))
                                self.input_layout_2.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                        self.list_button_input.append(QtWidgets.QToolButton())
                        self.list_button_input[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
                        self.list_button_input[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
                        self.list_button_input[self.input_num].setText("")
                        self.list_button_input[self.input_num].setIcon(icon)
                        self.list_button_input[self.input_num].setIconSize(QtCore.QSize(23, 23))
                        self.list_button_input[self.input_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_button_input[self.input_num].setObjectName("optional_list_button_input_"
                                                                                 + str(self.input_num))
                        else:
                            self.list_button_input[self.input_num].setObjectName("list_button_input_"
                                                                                 + str(self.input_num))
                        self.input_layout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 
                                                    self.input_num, 3, 1, 1)
                        self.list_button_input[self.input_num].setStyleSheet("QToolButton {\n"
                        "    border: 1px solid transparent;\n"
                        "    background-color: transparent;\n"
                        "    width: 27px;\n"
                        "    height: 27px;\n"
                        "}\n"
                        "\n"
                        "QToolButton:flat {\n"
                        "    border: none;\n"
                        "}")
                        self.list_button_input[self.input_num].clicked.connect(lambda: self.information_button())
                        self.input_layout_2.addWidget(self.list_button_input[self.input_num], self.input_num, 4 ,1 ,1)
                        self.input_layout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 
                                                    self.input_num, 5 ,1 ,1)
                        self.input_num += 1
            if self.tabWidget.currentIndex() == 2:
                if len(self.list_label_output) == 0:
                    logging.info("MyProcessingWindow - populating outputs")
                    for item in self.algorithm().metadata["Outputs"]:
                        font = QtGui.QFont()
                        font.setFamily("fonts/SourceSansPro-Regular.ttf")
                        font.setPointSize(10)
                        font.setKerning(True)
                        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                        font2 = QtGui.QFont()
                        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
                        font2.setPointSize(9)
                        font2.setKerning(True)
                        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.list_label_output.append(QtWidgets.QLabel())
                        self.list_label_output[self.output_num].setText(item)
                        self.list_label_output[self.output_num].setFont(font)
                        self.list_label_output[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
                        self.list_label_output[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
                        self.list_label_output[self.output_num].setObjectName("list_label_output_" + str(self.output_num))
                        self.list_label_output[self.output_num].setStyleSheet("QLabel {color: black;}")
                        self.output_layout_2.addWidget(self.list_label_output[self.output_num], self.output_num, 0, 1, 1)
                        self.output_layout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 
                                                     self.output_num, 1, 1, 1)
                        self.list_lineedit_output.append(QtWidgets.QLineEdit())
                        self.list_lineedit_output[self.output_num].setEnabled(True)
                        self.list_lineedit_output[self.output_num].setFont(font2)
                        self.list_lineedit_output[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
                        self.list_lineedit_output[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
                        self.list_lineedit_output[self.output_num].setFrame(False)
                        self.list_lineedit_output[self.output_num].setStyleSheet("border-radius: 3px;"
                            + "padding: 1px 4px 1px 4px; background: rgb(240, 240, 240);")
                        self.list_lineedit_output[self.output_num].setObjectName("list_lineedit_output_" + str(self.output_num))
                        self.list_lineedit_output[self.output_num].textChanged.connect(lambda: self.activate_save_button())
                        self.output_layout_2.addWidget(self.list_lineedit_output[self.output_num], self.output_num, 2, 1, 1)
                        self.list_button_output.append(QtWidgets.QToolButton())
                        self.list_button_output[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
                        self.list_button_output[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
                        self.list_button_output[self.output_num].setText("")
                        self.list_button_output[self.output_num].setIcon(icon)
                        self.list_button_output[self.output_num].setIconSize(QtCore.QSize(23, 23))
                        self.list_button_output[self.output_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                        self.list_button_output[self.output_num].setObjectName("list_button_output_" + str(self.output_num))
                        self.output_layout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 
                                                     self.output_num, 3, 1, 1)
                        self.list_button_output[self.output_num].setStyleSheet("QToolButton {\n"
                        "    border: 1px solid transparent;\n"
                        "    background-color: transparent;\n"
                        "    width: 27px;\n"
                        "    height: 27px;\n"
                        "}\n"
                        "\n"
                        "QToolButton:flat {\n"
                        "    border: none;\n"
                        "}")
                        
                        self.list_button_output[self.output_num].clicked.connect(lambda: self.information_button())
                        self.output_layout_2.addWidget(self.list_button_output[self.output_num], self.output_num, 4, 1, 1)
                        self.output_layout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 
                                                     self.output_num, 5, 1, 1)
                        self.output_num += 1
    
    
    def prepare_layout(self):
        self.clear_layout(self.input_layout_2)
        self.clear_layout(self.output_layout_2)
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_lineedit_input = []
        self.input_num = 0
        self.list_label_output = []
        self.list_lineedit_output = []
        self.list_button_input = []
        self.list_button_output = []
        self.output_num = 0
                
                
    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):   
            item = layout.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QtGui.QLayout):
                self.clear_layout(item.layout())
            layout.removeItem(item)               
    
    
    def hide_algorithm_information(self):
        self.aw_label_4.hide()
        self.aw_label_5.hide()
        self.aw_textbrowser_1.hide()
        self.aw_textbrowser_2.hide()
        
        
    def load_algorithm_information(self):
        logging.info("MyProcessingWindow - loading algorithm information")
        self.output_activate = 0
        self.input_activate = 0
        self.aw_okButton.setEnabled(False)
        if self.aw_combobox_2.currentText() != "Make a choice...":
            self.aw_label_4.show()
            self.aw_label_5.show()
            self.aw_textbrowser_1.show()
            self.aw_textbrowser_2.show()
            self.aw_textbrowser_1.setPlainText("")
            self.aw_textbrowser_2.setPlainText("")
            try:
                self.algorithm = getattr(getattr(egads.algorithms, str(self.aw_combobox_1.currentText()).lower()), 
                                             str(self.aw_combobox_2.currentText()))
            except AttributeError:
                self.algorithm = getattr(getattr(egads.algorithms.user, str(self.aw_combobox_1.currentText()).lower()), 
                                             str(self.aw_combobox_2.currentText()))
            try:
                description_string = '<p align="justify">' + str(self.algorithm().metadata["Description"]) + '</p>'
                self.aw_textbrowser_2.setHtml(description_string)
            except KeyError:
                pass
            try:
                purpose_string = '<p align="justify">' + str(self.algorithm().metadata["Purpose"]) + '</p>'
                self.aw_textbrowser_1.setHtml(purpose_string)
            except KeyError:
                pass

    
    def activate_save_button(self):
        if self.list_combobox_input:
            activate = 1
            for widget in self.list_combobox_input:
                try:
                    if widget.currentText() == "Make a choice...":
                        activate = 0
                except AttributeError:
                    if "optional" not in widget.objectName():
                        try: 
                            if widget.text() == "":
                                activate = 0
                        except AttributeError:
                            subwidgets = (widget.itemAt(i) for i in range(widget.count()))
                            for subwidget in subwidgets:
                                if subwidget.widget().text() == "":
                                    activate = 0         
            if activate == 1:
                self.input_activate = 1
            else:
                self.input_activate = 0
        if self.list_lineedit_output:
            activate = 1
            for widget in self.list_lineedit_output:
                if widget.text() == "":
                        activate = 0
            if activate == 1:
                self.output_activate = 1
            else:
                self.output_activate = 0   
        if self.input_activate == 1 & self.output_activate == 1:
            self.aw_okButton.setEnabled(True)
        else:
            self.aw_okButton.setEnabled(False)
    
    
    def information_button(self):
        information_string =""
        if "input" in self.sender().objectName():
            if "optional" in self.sender().objectName():
                information_string = "[Optional] " + self.algorithm().metadata["InputDescription"][int(self.sender().objectName()[27:])]
            else:
                information_string = self.algorithm().metadata["InputDescription"][int(self.sender().objectName()[18:])]
        else:
            if "optional" in self.sender().objectName():
                information_string = "[Optional] " + self.algorithm().metadata["OutputDescription"][int(self.sender().objectName()[28:])]
            else:
                information_string = self.algorithm().metadata["OutputDescription"][int(self.sender().objectName()[19:])]
        self.infoWindow = MyInfo(information_string)
        self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setGeometry(QtGui.QCursor.pos().x() - 225, QtGui.QCursor.pos().y() + 50, 450, 
                                    self.infoWindow.sizeHint().height())
        self.infoWindow.exec_()

 
class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()


class MyDisplay(QtWidgets.QDialog, Ui_displayWindow):
    def __init__(self, variable):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.variable = variable
        self.dw_line_1.setText(self.variable[1]["var_name"])
        self.dw_line_2.setText(self.variable[1]["units"])
        self.dw_okButton.clicked.connect(self.closeWindow)
        self.populate_table()
        logging.info("MyDisplay - window ready")

        
    def closeWindow(self):
        logging.info("MyDisplay - window closing")
        self.close()
        
        
    def populate_table(self):
        logging.info("MyDisplay - populating table")
        col, row = 1, 1
        try:
            col = self.variable[3].value.shape[0]
            row = self.variable[3].value.shape[1]
        except IndexError:
            col = self.variable[3].value.shape[0]
        self.dw_table.setRowCount(row)
        self.dw_table.setColumnCount(col)
        if row == 1:
            for x in range(col):
                try:
                    if self.variable[3].value[x] == self.variable[1]["_FillValue"]:
                        self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem("NaN"))
                    else:
                        self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[x])))
                except KeyError:
                    try: 
                        if self.variable[3].value[x] == self.variable[1]["missing_value"]:
                            self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem("NaN"))
                        else:
                            self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[x])))
                    except KeyError:
                        self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[x])))
        else:
            for y in range(row):
                for x in range(col):
                    self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[y][x])))
        
        
class PlotWindow(QtWidgets.QDialog, Ui_plotWindow):
    def __init__(self, list_of_variables, list_of_new_variables):
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
        logging.info("PlotWindow - window ready")

    
    def close_window(self):
        self.close()
    
    
    def setup_toolbar(self):
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
        self.navigation_toolbar.home()
    
    
    def plot_save(self):
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
        self.pw_xvariable_rl.setFont(font2)
        self.pw_xvariable_rl.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_xvariable_rl.setMaximumSize(QtCore.QSize(250, 27))
        self.pw_xvariable_rl.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_yvariable_rl.setFont(font2)
        self.pw_yvariable_rl.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_yvariable_rl.setMaximumSize(QtCore.QSize(250, 27))
        self.pw_yvariable_rl.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        logging.info("PlotWindow - adding variable")
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
        logging.info("PlotWindow -                " + self.pw_yvariable_rl.currentText())
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
        logging.info("PlotWindow - variable added")
        
        
    def del_variable_single(self, index = None):
        logging.info("PlotWindow - deleting variable")
        if index == None:
            index = int(self.sender().objectName()[12:])
        logging.info("PlotWindow -               " + self.list_label[index].text())
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
        logging.info("PlotWindow - variable deleted")
    
    
    def del_figure_options(self, index):
        if self.pw_figureOptions_vl_1:
            logging.info("PlotWindow - deleting figure options")
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
            logging.info("PlotWindow - deleting plot options")
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
        self.pw_multipleXvariable_rl[self.multiple_num].setFont(font3)
        self.pw_multipleXvariable_rl[self.multiple_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_multipleXvariable_rl[self.multiple_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_multipleXvariable_rl[self.multiple_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_multipleYvariable_rl[self.multiple_num].setFont(font3)
        self.pw_multipleYvariable_rl[self.multiple_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_multipleYvariable_rl[self.multiple_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_multipleYvariable_rl[self.multiple_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        if self.pw_xvariable_rl.currentText() != "Make a choice..." and self.pw_yvariable_rl.currentText() != "Make a choice...":
            logging.info("PlotWindow -               x: " + self.pw_xvariable_rl.currentText())
            logging.info("PlotWindow -               y: " + self.pw_yvariable_rl.currentText())
            self.actionZoom.setEnabled(True)
            self.actionPan.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.actionOrigin.setEnabled(True)
            self.actionClear.setEnabled(True)
            self.pw_singleLabel_3.show()
            self.add_variable_single()
            logging.info("PlotWindow - ploting")
            xnan = ""
            ynan = ""
            sublist = self.list_of_variables_and_attributes[str(self.pw_xvariable_rl.currentText())]
            xvalue = copy.deepcopy(sublist[3].value)
            try:
                xunits = copy.deepcopy(sublist[1]["units"])
            except KeyError:
                xunits = 'no units'
            try:
                xnan = sublist[1]["_FillValue"]
            except KeyError:
                pass
            sublist = self.list_of_variables_and_attributes[str(self.pw_yvariable_rl.currentText())]
            yvalue = copy.deepcopy(sublist[3].value)
            yname = str(self.pw_yvariable_rl.currentText())
            try:
                yunits = copy.deepcopy(sublist[1]["units"])
            except KeyError:
                yunits = 'no units'
            try:
                ynan = sublist[1]["_FillValue"]
            except KeyError:
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
        index = int(self.sender().objectName()[24:])
        if "X" in self.sender().objectName():
            xcombobox = self.sender()
            ycombobox = self.findChild(QtWidgets.QComboBox, "pw_multipleYvariable_rl_" + str(index))
        elif "Y" in self.sender().objectName():
            xcombobox = self.findChild(QtWidgets.QComboBox, "pw_multipleXvariable_rl_" + str(index))
            ycombobox = self.sender()
        if ycombobox.currentText() != "Make a choice..." and xcombobox.currentText() != "Make a choice...":
            self.actionZoom.setEnabled(True)
            self.actionPan.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.actionOrigin.setEnabled(True)
            self.actionClear.setEnabled(True)
            logging.info("PlotWindow - ploting")
            xnan = ""
            ynan = ""
            self.mult_grid_option.append(False)
            self.legend_visibility.append(True)
            sublist = self.list_of_variables_and_attributes[str(xcombobox.currentText())]
            logging.info("PlotWindow -               x: " + str(xcombobox.currentText()))
            xvalue = copy.deepcopy(sublist[3].value)
            xunits = copy.deepcopy(sublist[1]["units"])
            xname = copy.deepcopy(sublist[1]["var_name"])
            try:
                xnan = sublist[1]["_FillValue"]
            except KeyError:
                pass
            sublist = self.list_of_variables_and_attributes[str(ycombobox.currentText())]
            logging.info("PlotWindow -               y: " + str(ycombobox.currentText()))
            yvalue = copy.deepcopy(sublist[3].value)
            yunits = copy.deepcopy(sublist[1]["units"])
            yname = copy.deepcopy(sublist[1]["var_name"])
            try:
                ynan = sublist[1]["_FillValue"]
            except KeyError:
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
        logging.info("PlotWindow - deletting deleted")
        if index == None:
            index = int(self.sender().objectName()[18:])
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
        logging.info("PlotWindow - variable deleted")
        
        
    def figure_options(self):
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
        self.pw_figureOptions_cb_1[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_1[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_1[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_1[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_figureOptions_cb_2[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_2[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_2[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_2[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_figureOptions_cb_3[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_3[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_3[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_3[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_figureOptions_cb_4[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_4[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_4[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_4[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_figureOptions_cb_5[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_5[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_5[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_5[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_figureOptions_cb_6[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_6[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_6[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_6[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black\n"
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
        self.pw_figureOptions_cb_7[self.option_num].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_7[self.option_num].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_7[self.option_num].setFont(font3)
        self.pw_figureOptions_cb_7[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_figureOptions_cb_8[self.option_num].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_8[self.option_num].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_8[self.option_num].setFont(font)
        self.pw_figureOptions_cb_8[self.option_num].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        "    color: black;\n"
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
        "    color: black;\n"
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
        self.pw_plotOptions_cb_1[self.option_num2].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_plotOptions_cb_1[self.option_num2].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_plotOptions_cb_1[self.option_num2].setFont(font3)
        self.pw_plotOptions_cb_1[self.option_num2].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        self.pw_plotOptions_cb_2[self.option_num2].setMinimumSize(QtCore.QSize(170, 27))
        self.pw_plotOptions_cb_2[self.option_num2].setMaximumSize(QtCore.QSize(170, 27))
        self.pw_plotOptions_cb_2[self.option_num2].setFont(font3)
        self.pw_plotOptions_cb_2[self.option_num2].setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: black;\n"
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
        if self.plot_type_str and self.pw_figureOptions_vl_1:
            if self.plot_type_str == "single":
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
        if self.plot_type_str and self.pw_plotOptions_vl_1:
            if self.plot_type_str == 'single':
                for i in range(self.option_num2):
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
        index = int(self.sender().objectName()[20:])
        if self.sender().checkState() == 2:
            self.pw_plotOptions_ln_2[index].setEnabled(True)
            self.pw_plotOptions_ln_2[index].setText("")
        else:    
            self.pw_plotOptions_ln_2[index].setDisabled(True)
            self.pw_plotOptions_ln_2[index].setText("")

    
    def activate_line_style(self):
        index = int(self.sender().objectName()[20:])
        self.pw_plotOptions_cb_1[index].clear()
        if "pw_plotOptions_rb_1" in self.sender().objectName() and self.sender().isChecked() == True:
            self.pw_plotOptions_cb_1[index].addItem("Make a choice...")
            self.populate_comboboxes_regular(self.pw_plotOptions_cb_1[index], self.line_styles)
        elif "pw_plotOptions_rb_2" in self.sender().objectName() and self.sender().isChecked() == True:
            self.pw_plotOptions_cb_1[index].addItem("Make a choice...")
            self.populate_comboboxes_regular(self.pw_plotOptions_cb_1[index], self.marker_styles)
            
            
    def activate_line_color(self):
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
        if self.sender().objectName() == "pw_figureOptions_sl_5":
            self.pw_figureOptions_lb_30[0].setText(str(self.sender().value()) + "%")
        else:
            label = self.findChild(QtWidgets.QLabel, str(self.sender().objectName() + "lb_" + str(self.sender().objectName()[22:])))
            label.setText(str(self.sender().value()) + "%")
            
            
    def populate_comboboxes(self, combobox):
        logging.info("PlotWindow - populating combobox")
        combobox.addItem("Make a choice...")
        for key, _ in sorted(self.list_of_variables_and_attributes.iteritems()):
            combobox.addItem(key)
        

    def populate_comboboxes_regular(self, combobox, item_list):
        logging.info("PlotWindow - populating combobox")
        for item in item_list:
            combobox.addItem(item)

    
    def get_file_name(self):
        file_dialog = QtWidgets.QFileDialog()
        filter_types = "EPS Files (*.eps);;JPEG Files (*.jpg *.jpeg *.jpe);;PDF Files (*.pdf);;PNG Files (*.png *.pns);;TIFF Files (*.tif *.tiff)"
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, "Save File", "", filter_types)
        return str(out_file_name), str(out_file_ext)
    
    
    def display_zoom_pan_warning(self):
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
        

        
class MyLog(QtWidgets.QDialog, Ui_Changelog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.log_txBrower.setPlainText(open("doc/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()
    
    
class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()
        
  
class MyAlgorithm(QtWidgets.QDialog, Ui_creationWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
        self.cw_okButton.clicked.connect(self.prepare_algorithm)
        self.cw_cancelButton.clicked.connect(self.closeWindow)
        self.cw_add_1.clicked.connect(self.add_input)
        self.cw_add_2.clicked.connect(self.add_output)
        self.cw_add_3.clicked.connect(lambda: self.add_category(True))
        self.listWidget.itemDoubleClicked.connect(lambda: self.remove_category(True))
        folder_list = os.walk(egads.__path__[0] + '/algorithms/user/')
        category_list = []
        for folder in folder_list:
            index = folder[0].find('user')
            if folder[0][index + 5:]:
                category_list.append(folder[0][index + 5:].title())
        category_list = ['Make a choice...', 'Other...'] + sorted(category_list)
        self.cw_combobox_1.clear()
        self.cw_combobox_1.addItems(category_list)
        self.cw_input_vl_1 = []
        self.cw_input_hl_1 = []
        self.cw_input_gd_1 = []
        self.cw_input_lb_1 = []
        self.cw_input_lb_2 = []
        self.cw_input_lb_3 = []
        self.cw_input_lb_4 = []
        self.cw_input_lb_5 = []
        self.cw_input_ln_1 = []
        self.cw_input_ln_2 = []
        self.cw_input_ln_3 = []
        self.cw_input_ln_4 = []
        self.cw_input_bt_1 = []
        self.cw_info_bt_1 = []
        self.cw_info_bt_2 = []
        self.cw_info_bt_3 = []
        self.cw_info_bt_4 = []
        self.cw_input_del_1 = []
        self.cw_input_li_1 = []
        self.input_num = 0
        self.cw_output_vl_1 = []
        self.cw_output_vl_2 = []
        self.cw_output_hl_1 = []
        self.cw_output_hl_2 = []
        self.cw_output_hl_3 = []
        self.cw_output_gd_1 = []
        self.cw_output_lb_1 = []
        self.cw_output_lb_2 = []
        self.cw_output_lb_3 = []
        self.cw_output_lb_4 = []
        self.cw_output_lb_5 = []
        self.cw_output_lb_6 = []
        self.cw_output_lb_7 = []
        self.cw_output_ln_1 = []
        self.cw_output_ln_2 = []
        self.cw_output_ln_3 = []
        self.cw_output_ln_4 = []
        self.cw_output_ln_5 = []
        self.cw_output_ln_6 = []
        self.cw_output_cb_1 = []
        self.cw_output_lw_1 = []
        self.cw_info_bt_5 = []
        self.cw_info_bt_6 = []
        self.cw_info_bt_7 = []
        self.cw_info_bt_8 = []
        self.cw_info_bt_9 = []
        self.cw_info_bt_10 = []
        self.cw_info_bt_11 = []
        self.cw_output_del_1 = []
        self.cw_output_add_1 = []
        self.cw_output_li_1 = []
        self.output_num = 0
        self.algorithm_mandatory_fields = {self.cw_line_1:self.cw_label_3,
                                           self.cw_line_2:self.cw_label_4,
                                           self.cw_plain_1:self.cw_label_7,
                                           self.cw_plain_2:self.cw_label_8,
                                           self.cw_plain_4:self.cw_label_10,
                                           self.listWidget:self.cw_label_9}
        
        
    def add_input(self):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/unit_validation_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_input_vl_1.append(QtWidgets.QVBoxLayout())
        self.cw_input_vl_1[self.input_num].setObjectName('cw_input_vl_1_' + str(self.input_num))
        self.cw_input_hl_1.append(QtWidgets.QHBoxLayout())
        self.cw_input_hl_1[self.input_num].setObjectName('cw_input_hl_1_' + str(self.input_num))
        self.cw_input_vl_1[self.input_num].addLayout(self.cw_input_hl_1[self.input_num])
        self.cw_input_del_1.append(QtWidgets.QToolButton())
        self.cw_input_del_1[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_input_del_1[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_input_del_1[self.input_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_input_del_1[self.input_num].setIcon(icon)
        self.cw_input_del_1[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_input_del_1[self.input_num].setObjectName('cw_input_del_1_' + str(self.input_num))
        self.cw_input_hl_1[self.input_num].addWidget(self.cw_input_del_1[self.input_num])
        self.cw_input_hl_1[self.input_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.cw_input_gd_1.append(QtWidgets.QGridLayout())
        self.cw_input_gd_1[self.input_num].setObjectName('cw_input_gd_1_' + str(self.input_num))
        self.cw_input_hl_1[self.input_num].addLayout(self.cw_input_gd_1[self.input_num])
        self.cw_input_lb_1.append(QtWidgets.QLabel())
        self.cw_input_lb_1[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_1[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_1[self.input_num].setFont(font)
        self.cw_input_lb_1[self.input_num].setText('Input symbols:')
        self.cw_input_lb_1[self.input_num].setObjectName('cw_input_lb_1_' + str(self.input_num))
        self.cw_input_lb_1[self.input_num].setStyleSheet("QLabel {color: black;}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_1[self.input_num], 0, 0, 1, 1)
        self.cw_input_ln_1.append(QtWidgets.QLineEdit())
        self.cw_input_ln_1[self.input_num].setEnabled(True)
        self.cw_input_ln_1[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_1[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_1[self.input_num].setFont(font)
        self.cw_input_ln_1[self.input_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_input_ln_1[self.input_num].setText('')
        self.cw_input_ln_1[self.input_num].setFrame(False)
        self.cw_input_ln_1[self.input_num].setObjectName('cw_input_ln_1_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_1[self.input_num], 0, 1, 1, 1)
        self.cw_info_bt_1.append(QtWidgets.QToolButton())
        self.cw_info_bt_1[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_1[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_1[self.input_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_1[self.input_num].setIcon(icon2)
        self.cw_info_bt_1[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_1[self.input_num].setObjectName('cw_info_bt_1_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_1[self.input_num], 0, 2, 1, 1)
        self.cw_input_gd_1[self.input_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 0, 3, 1, 1)
        self.cw_input_lb_2.append(QtWidgets.QLabel())
        self.cw_input_lb_2[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_2[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_2[self.input_num].setFont(font)
        self.cw_input_lb_2[self.input_num].setText('Input units:')
        self.cw_input_lb_2[self.input_num].setObjectName('cw_input_lb_2_' + str(self.input_num))
        self.cw_input_lb_2[self.input_num].setStyleSheet("QLabel {color: black;}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_2[self.input_num], 1, 0, 1, 1)
        self.cw_input_ln_2.append(QtWidgets.QLineEdit())
        self.cw_input_ln_2[self.input_num].setEnabled(True)
        self.cw_input_ln_2[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_2[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_2[self.input_num].setFont(font)
        self.cw_input_ln_2[self.input_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_input_ln_2[self.input_num].setText('')
        self.cw_input_ln_2[self.input_num].setFrame(False)
        self.cw_input_ln_2[self.input_num].setObjectName('cw_input_ln_2_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_2[self.input_num], 1, 1, 1, 1)
        self.cw_info_bt_2.append(QtWidgets.QToolButton())
        self.cw_info_bt_2[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_2[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_2[self.input_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_2[self.input_num].setIcon(icon2)
        self.cw_info_bt_2[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_2[self.input_num].setObjectName('cw_info_bt_2_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_2[self.input_num], 1, 2, 1, 1)
        self.cw_input_gd_1[self.input_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 3, 1, 1)
        self.cw_input_lb_3.append(QtWidgets.QLabel())
        self.cw_input_lb_3[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_3[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_3[self.input_num].setFont(font)
        self.cw_input_lb_3[self.input_num].setText('Input type:')
        self.cw_input_lb_3[self.input_num].setObjectName('cw_input_lb_3_' + str(self.input_num))
        self.cw_input_lb_3[self.input_num].setStyleSheet("QLabel {color: black;}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_3[self.input_num], 2, 0, 1, 1)
        self.cw_input_ln_3.append(QtWidgets.QLineEdit())
        self.cw_input_ln_3[self.input_num].setEnabled(True)
        self.cw_input_ln_3[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_3[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_3[self.input_num].setFont(font)
        self.cw_input_ln_3[self.input_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_input_ln_3[self.input_num].setText('')
        self.cw_input_ln_3[self.input_num].setFrame(False)
        self.cw_input_ln_3[self.input_num].setObjectName('cw_input_ln_3_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_3[self.input_num], 2, 1, 1, 1)
        self.cw_info_bt_3.append(QtWidgets.QToolButton())
        self.cw_info_bt_3[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_3[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_3[self.input_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_3[self.input_num].setIcon(icon2)
        self.cw_info_bt_3[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_3[self.input_num].setObjectName('cw_info_bt_3_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_3[self.input_num], 2, 2, 1, 1)
        self.cw_input_gd_1[self.input_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 2, 3, 1, 1)
        self.cw_input_lb_4.append(QtWidgets.QLabel())
        self.cw_input_lb_4[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_4[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_4[self.input_num].setFont(font)
        self.cw_input_lb_4[self.input_num].setText('Input description:')
        self.cw_input_lb_4[self.input_num].setObjectName('cw_input_lb_4_' + str(self.input_num))
        self.cw_input_lb_4[self.input_num].setStyleSheet("QLabel {color: black;}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_4[self.input_num], 3, 0, 1, 1)
        self.cw_input_ln_4.append(QtWidgets.QLineEdit())
        self.cw_input_ln_4[self.input_num].setEnabled(True)
        self.cw_input_ln_4[self.input_num].setMinimumSize(QtCore.QSize(500, 27))
        self.cw_input_ln_4[self.input_num].setMaximumSize(QtCore.QSize(500, 27))
        self.cw_input_ln_4[self.input_num].setFont(font)
        self.cw_input_ln_4[self.input_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_input_ln_4[self.input_num].setText('')
        self.cw_input_ln_4[self.input_num].setFrame(False)
        self.cw_input_ln_4[self.input_num].setObjectName('cw_input_ln_4_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_4[self.input_num], 3, 1, 1, 3)
        self.cw_info_bt_4.append(QtWidgets.QToolButton())
        self.cw_info_bt_4[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_4[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_4[self.input_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_4[self.input_num].setIcon(icon2)
        self.cw_info_bt_4[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_4[self.input_num].setObjectName('cw_info_bt_4_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_4[self.input_num], 3, 4, 1, 1)
        self.cw_input_hl_1[self.input_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.cw_input_vl.addLayout(self.cw_input_vl_1[self.input_num])
        self.cw_input_vl_1[self.input_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_input_li_1.append(QtWidgets.QFrame())
        self.cw_input_li_1[self.input_num].setFrameShape(QtWidgets.QFrame.HLine)
        self.cw_input_li_1[self.input_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cw_input_li_1[self.input_num].setObjectName("cw_input_li_1_" + str(self.input_num))
        self.cw_input_vl_1[self.input_num].addWidget(self.cw_input_li_1[self.input_num])
        self.cw_input_vl_1[self.input_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_input_del_1[self.input_num].clicked.connect(lambda: self.del_input())
        self.input_num += 1
        
    
    def add_output(self):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_output_vl_1.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_1[self.output_num].setObjectName('cw_output_vl_1_' + str(self.output_num))
        self.cw_output_hl_1.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_1[self.output_num].setObjectName('cw_output_hl_1_' + str(self.output_num))
        self.cw_output_vl_1[self.output_num].addLayout(self.cw_output_hl_1[self.output_num])
        self.cw_output_del_1.append(QtWidgets.QToolButton())
        self.cw_output_del_1[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_output_del_1[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_output_del_1[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_output_del_1[self.output_num].setIcon(icon)
        self.cw_output_del_1[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_output_del_1[self.output_num].setObjectName('cw_output_del_1_' + str(self.output_num))
        self.cw_output_hl_1[self.output_num].addWidget(self.cw_output_del_1[self.output_num])
        self.cw_output_hl_1[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.cw_output_vl_2.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_2[self.output_num].setObjectName('cw_output_vl_2_' + str(self.output_num))
        self.cw_output_hl_1[self.output_num].addLayout(self.cw_output_vl_2[self.output_num])
        self.cw_output_gd_1.append(QtWidgets.QGridLayout())
        self.cw_output_gd_1[self.output_num].setObjectName('cw_output_gd_1_' + str(self.output_num))
        self.cw_output_vl_2[self.output_num].addLayout(self.cw_output_gd_1[self.output_num])
        self.cw_output_lb_1.append(QtWidgets.QLabel())
        self.cw_output_lb_1[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_1[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_1[self.output_num].setFont(font)
        self.cw_output_lb_1[self.output_num].setText('Output symbols:')
        self.cw_output_lb_1[self.output_num].setObjectName('cw_output_lb_1_' + str(self.output_num))
        self.cw_output_lb_1[self.output_num].setStyleSheet("QLabel {color: black;}")
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_1[self.output_num], 0, 0, 1, 1)
        self.cw_output_ln_1.append(QtWidgets.QLineEdit())
        self.cw_output_ln_1[self.output_num].setEnabled(True)
        self.cw_output_ln_1[self.output_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_output_ln_1[self.output_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_output_ln_1[self.output_num].setFont(font)
        self.cw_output_ln_1[self.output_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_output_ln_1[self.output_num].setText('')
        self.cw_output_ln_1[self.output_num].setFrame(False)
        self.cw_output_ln_1[self.output_num].setObjectName('cw_output_ln_1_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_ln_1[self.output_num], 0, 1, 1, 1)
        self.cw_info_bt_5.append(QtWidgets.QToolButton())
        self.cw_info_bt_5[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_5[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_5[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_5[self.output_num].setIcon(icon2)
        self.cw_info_bt_5[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_5[self.output_num].setObjectName('cw_info_bt_5_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_info_bt_5[self.output_num], 0, 2, 1, 1)
        self.cw_output_gd_1[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 3, 1, 1)
        self.cw_output_lb_2.append(QtWidgets.QLabel())
        self.cw_output_lb_2[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_2[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_2[self.output_num].setFont(font)
        self.cw_output_lb_2[self.output_num].setText('Output standard name:')
        self.cw_output_lb_2[self.output_num].setObjectName('cw_output_lb_2_' + str(self.output_num))
        self.cw_output_lb_2[self.output_num].setStyleSheet("QLabel {color: black;}")
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_2[self.output_num], 0, 4, 1, 1)
        self.cw_output_ln_2.append(QtWidgets.QLineEdit())
        self.cw_output_ln_2[self.output_num].setEnabled(True)
        self.cw_output_ln_2[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
        self.cw_output_ln_2[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
        self.cw_output_ln_2[self.output_num].setFont(font)
        self.cw_output_ln_2[self.output_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_output_ln_2[self.output_num].setText('')
        self.cw_output_ln_2[self.output_num].setFrame(False)
        self.cw_output_ln_2[self.output_num].setObjectName('cw_output_ln_2_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_ln_2[self.output_num], 0, 5, 1, 1)
        self.cw_info_bt_6.append(QtWidgets.QToolButton())
        self.cw_info_bt_6[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_6[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_6[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_6[self.output_num].setIcon(icon2)
        self.cw_info_bt_6[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_6[self.output_num].setObjectName('cw_info_bt_6_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_info_bt_6[self.output_num], 0, 6, 1, 1)
        self.cw_output_lb_3.append(QtWidgets.QLabel())
        self.cw_output_lb_3[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_3[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_3[self.output_num].setFont(font)
        self.cw_output_lb_3[self.output_num].setText('Output units:')
        self.cw_output_lb_3[self.output_num].setObjectName('cw_output_lb_3_' + str(self.output_num))
        self.cw_output_lb_3[self.output_num].setStyleSheet("QLabel {color: black;}")
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_3[self.output_num], 1, 0, 1, 1)
        self.cw_output_ln_3.append(QtWidgets.QLineEdit())
        self.cw_output_ln_3[self.output_num].setEnabled(True)
        self.cw_output_ln_3[self.output_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_output_ln_3[self.output_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_output_ln_3[self.output_num].setFont(font)
        self.cw_output_ln_3[self.output_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_output_ln_3[self.output_num].setText('')
        self.cw_output_ln_3[self.output_num].setFrame(False)
        self.cw_output_ln_3[self.output_num].setObjectName('cw_output_ln_3_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_ln_3[self.output_num], 1, 1, 1, 1)
        self.cw_info_bt_7.append(QtWidgets.QToolButton())
        self.cw_info_bt_7[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_7[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_7[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_7[self.output_num].setIcon(icon2)
        self.cw_info_bt_7[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_7[self.output_num].setObjectName('cw_info_bt_7_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_info_bt_7[self.output_num], 1, 2, 1, 1)
        self.cw_output_gd_1[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 3, 1, 1)
        self.cw_output_lb_4.append(QtWidgets.QLabel())
        self.cw_output_lb_4[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_4[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_4[self.output_num].setFont(font)
        self.cw_output_lb_4[self.output_num].setText('Output long name:')
        self.cw_output_lb_4[self.output_num].setObjectName('cw_output_lb_4_' + str(self.output_num))
        self.cw_output_lb_4[self.output_num].setStyleSheet("QLabel {color: black;}")
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_4[self.output_num], 1, 4, 1, 1)
        self.cw_output_ln_4.append(QtWidgets.QLineEdit())
        self.cw_output_ln_4[self.output_num].setEnabled(True)
        self.cw_output_ln_4[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
        self.cw_output_ln_4[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
        self.cw_output_ln_4[self.output_num].setFont(font)
        self.cw_output_ln_4[self.output_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_output_ln_4[self.output_num].setText('')
        self.cw_output_ln_4[self.output_num].setFrame(False)
        self.cw_output_ln_4[self.output_num].setObjectName('cw_output_ln_4_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_ln_4[self.output_num], 1, 5, 1, 1)
        self.cw_info_bt_8.append(QtWidgets.QToolButton())
        self.cw_info_bt_8[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_8[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_8[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_8[self.output_num].setIcon(icon2)
        self.cw_info_bt_8[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_8[self.output_num].setObjectName('cw_info_bt_8_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_info_bt_8[self.output_num], 1, 6, 1, 1)
        self.cw_output_lb_7.append(QtWidgets.QLabel())
        self.cw_output_lb_7[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_7[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_7[self.output_num].setFont(font)
        self.cw_output_lb_7[self.output_num].setText('Output type:')
        self.cw_output_lb_7[self.output_num].setObjectName('cw_output_lb_7_' + str(self.output_num))
        self.cw_output_lb_7[self.output_num].setStyleSheet("QLabel {color: black;}")
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_7[self.output_num], 2, 0, 1, 1)
        self.cw_output_ln_6.append(QtWidgets.QLineEdit())
        self.cw_output_ln_6[self.output_num].setEnabled(True)
        self.cw_output_ln_6[self.output_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_output_ln_6[self.output_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_output_ln_6[self.output_num].setFont(font)
        self.cw_output_ln_6[self.output_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_output_ln_6[self.output_num].setText('')
        self.cw_output_ln_6[self.output_num].setFrame(False)
        self.cw_output_ln_6[self.output_num].setObjectName('cw_output_ln_6_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_ln_6[self.output_num], 2, 1, 1, 1)
        self.cw_info_bt_11.append(QtWidgets.QToolButton())
        self.cw_info_bt_11[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_11[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_11[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_11[self.output_num].setIcon(icon2)
        self.cw_info_bt_11[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_11[self.output_num].setObjectName('cw_info_bt_11_' + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_info_bt_11[self.output_num], 2, 2, 1, 1)
        self.cw_output_hl_2.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_2[self.output_num].setObjectName('cw_output_hl_2_' + str(self.output_num))
        self.cw_output_vl_2[self.output_num].addLayout(self.cw_output_hl_2[self.output_num])
        self.cw_output_lb_5.append(QtWidgets.QLabel())
        self.cw_output_lb_5[self.output_num].setMinimumSize(QtCore.QSize(140, 27))
        self.cw_output_lb_5[self.output_num].setMaximumSize(QtCore.QSize(170, 27))
        self.cw_output_lb_5[self.output_num].setFont(font)
        self.cw_output_lb_5[self.output_num].setText('Output description:')
        self.cw_output_lb_5[self.output_num].setObjectName('cw_output_lb_5_' + str(self.output_num))
        self.cw_output_lb_5[self.output_num].setStyleSheet("QLabel {color: black;}")
        self.cw_output_hl_2[self.output_num].addWidget(self.cw_output_lb_5[self.output_num])
        self.cw_output_ln_5.append(QtWidgets.QLineEdit())
        self.cw_output_ln_5[self.output_num].setEnabled(True)
        self.cw_output_ln_5[self.output_num].setMinimumSize(QtCore.QSize(500, 27))
        self.cw_output_ln_5[self.output_num].setMaximumSize(QtCore.QSize(500, 27))
        self.cw_output_ln_5[self.output_num].setFont(font)
        self.cw_output_ln_5[self.output_num].setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color: rgb(200,200,200);\n"
        "}")
        self.cw_output_ln_5[self.output_num].setText('')
        self.cw_output_ln_5[self.output_num].setFrame(False)
        self.cw_output_ln_5[self.output_num].setObjectName('cw_output_ln_5_' + str(self.output_num))
        self.cw_output_hl_2[self.output_num].addWidget(self.cw_output_ln_5[self.output_num])
        self.cw_info_bt_9.append(QtWidgets.QToolButton())
        self.cw_info_bt_9[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_9[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_9[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_9[self.output_num].setIcon(icon2)
        self.cw_info_bt_9[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_9[self.output_num].setObjectName('cw_info_bt_9_' + str(self.output_num))
        self.cw_output_hl_2[self.output_num].addWidget(self.cw_info_bt_9[self.output_num])
        self.cw_output_hl_2[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.cw_output_hl_3.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_3[self.output_num].setObjectName('cw_output_hl_3_' + str(self.output_num))
        self.cw_output_vl_2[self.output_num].addLayout(self.cw_output_hl_3[self.output_num])
        self.cw_output_lb_6.append(QtWidgets.QLabel())
        self.cw_output_lb_6[self.output_num].setMinimumSize(QtCore.QSize(140, 27))
        self.cw_output_lb_6[self.output_num].setMaximumSize(QtCore.QSize(170, 27))
        self.cw_output_lb_6[self.output_num].setFont(font)
        self.cw_output_lb_6[self.output_num].setText('Output category(ies):')
        self.cw_output_lb_6[self.output_num].setObjectName('cw_output_lb_6_' + str(self.output_num))
        self.cw_output_lb_6[self.output_num].setStyleSheet("QLabel {color: black;}")
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_output_lb_6[self.output_num])
        self.cw_output_cb_1.append(QtWidgets.QComboBox())
        self.cw_output_cb_1[self.output_num].setMinimumSize(QtCore.QSize(160, 27))
        self.cw_output_cb_1[self.output_num].setMaximumSize(QtCore.QSize(160, 27))
        self.cw_output_cb_1[self.output_num].setFont(font2)
        self.cw_output_cb_1[self.output_num].setStyleSheet("QComboBox {\n"
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
        "QComboBox:pressed {\n"
        "    border: 1px solid #579de5;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
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
        self.cw_output_cb_1[self.output_num].setFrame(False)
        self.cw_output_cb_1[self.output_num].setObjectName("cw_output_cb_1_" + str(self.output_num))
        self.cw_output_cb_1[self.output_num].addItem("Make a choice...")
        self.cw_output_cb_1[self.output_num].addItem("Other...")
        self.cw_output_cb_1[self.output_num].addItem("Aircraft State")
        self.cw_output_cb_1[self.output_num].addItem("Atmospheric State")
        self.cw_output_cb_1[self.output_num].addItem("Microphysics")
        self.cw_output_cb_1[self.output_num].addItem("PMS Probe")
        self.cw_output_cb_1[self.output_num].addItem("Radiation")
        self.cw_output_cb_1[self.output_num].addItem("Thermodynamics")
        self.cw_output_cb_1[self.output_num].addItem("Wind")
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_output_cb_1[self.output_num])
        self.cw_output_hl_3[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.cw_output_add_1.append(QtWidgets.QToolButton())
        self.cw_output_add_1[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_output_add_1[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_output_add_1[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_output_add_1[self.output_num].setIcon(icon3)
        self.cw_output_add_1[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_output_add_1[self.output_num].setObjectName("cw_output_add_1_" + str(self.output_num))
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_output_add_1[self.output_num])
        self.cw_output_hl_3[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.cw_output_lw_1.append(QtWidgets.QListWidget())
        self.cw_output_lw_1[self.output_num].setMinimumSize(QtCore.QSize(200, 100))
        self.cw_output_lw_1[self.output_num].setMaximumSize(QtCore.QSize(200, 100))
        self.cw_output_lw_1[self.output_num].setFont(font2)
        self.cw_output_lw_1[self.output_num].setStyleSheet("QListWidget {\n"
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
        self.cw_output_lw_1[self.output_num].setObjectName("cw_output_lw_1_" + str(self.output_num))
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_output_lw_1[self.output_num])
        self.cw_info_bt_10.append(QtWidgets.QToolButton())
        self.cw_info_bt_10[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_10[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_10[self.output_num].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.cw_info_bt_10[self.output_num].setIcon(icon2)
        self.cw_info_bt_10[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_10[self.output_num].setObjectName('cw_info_bt_10_' + str(self.output_num))
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_info_bt_10[self.output_num])
        self.cw_output_hl_3[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.cw_output_hl_1[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.cw_output_vl_1[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_output_li_1.append(QtWidgets.QFrame())
        self.cw_output_li_1[self.output_num].setFrameShape(QtWidgets.QFrame.HLine)
        self.cw_output_li_1[self.output_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cw_output_li_1[self.output_num].setObjectName("cw_output_li_1_" + str(self.output_num))
        self.cw_output_vl_1[self.output_num].addWidget(self.cw_output_li_1[self.output_num])
        self.cw_output_vl_1[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_output_vl.addLayout(self.cw_output_vl_1[self.output_num])
        self.cw_output_del_1[self.output_num].clicked.connect(lambda: self.del_output())
        self.cw_output_add_1[self.output_num].clicked.connect(lambda: self.add_category())
        self.cw_output_lw_1[self.output_num].itemDoubleClicked.connect(lambda: self.remove_category())
        self.output_num += 1
        
    
    def del_input(self, index=None):
        if index is None:
            index = int(self.sender().objectName()[15:])
        self.cw_input_vl_1[index].deleteLater()
        self.cw_input_vl_1.pop(index)
        self.cw_input_li_1[index].deleteLater()
        self.cw_input_li_1.pop(index)
        self.cw_input_hl_1[index].deleteLater()
        self.cw_input_hl_1.pop(index)
        self.cw_input_del_1[index].deleteLater()
        self.cw_input_del_1.pop(index)
        self.cw_input_gd_1[index].deleteLater()
        self.cw_input_gd_1.pop(index)
        self.cw_input_lb_1[index].deleteLater()
        self.cw_input_lb_1.pop(index)
        self.cw_input_ln_1[index].deleteLater()
        self.cw_input_ln_1.pop(index)
        self.cw_info_bt_1[index].deleteLater()
        self.cw_info_bt_1.pop(index)
        self.cw_input_lb_2[index].deleteLater()
        self.cw_input_lb_2.pop(index)
        self.cw_input_ln_2[index].deleteLater()
        self.cw_input_ln_2.pop(index)
        self.cw_info_bt_2[index].deleteLater()
        self.cw_info_bt_2.pop(index)
        self.cw_input_lb_3[index].deleteLater()
        self.cw_input_lb_3.pop(index)
        self.cw_input_ln_3[index].deleteLater()
        self.cw_input_ln_3.pop(index)
        self.cw_info_bt_3[index].deleteLater()
        self.cw_info_bt_3.pop(index)
        self.cw_input_lb_4[index].deleteLater()
        self.cw_input_lb_4.pop(index)
        self.cw_input_ln_4[index].deleteLater()
        self.cw_input_ln_4.pop(index)
        self.cw_info_bt_4[index].deleteLater()
        self.cw_info_bt_4.pop(index)
        self.input_num -= 1
        if len(self.cw_input_vl_1) > 0:
            for i in range(0, len(self.cw_input_vl_1)):
                self.cw_input_vl_1[i].setObjectName('cw_input_vl_1_' + str(i))
                self.cw_input_li_1[i].setObjectName("cw_input_li_1_" + str(i))
                self.cw_input_hl_1[i].setObjectName('cw_input_hl_1_' + str(i))
                self.cw_input_del_1[i].setObjectName('cw_input_del_1_' + str(i))
                self.cw_input_gd_1[i].setObjectName('cw_input_gd_1_' + str(i))
                self.cw_input_lb_1[i].setObjectName('cw_input_lb_1_' + str(i))
                self.cw_input_ln_1[i].setObjectName('cw_input_ln_1_' + str(i))
                self.cw_info_bt_1[i].setObjectName('cw_info_bt_1_' + str(i))
                self.cw_input_lb_2[i].setObjectName('cw_input_lb_2_' + str(i))
                self.cw_input_ln_2[i].setObjectName('cw_input_ln_2_' + str(i))
                self.cw_info_bt_2[i].setObjectName('cw_info_bt_2_' + str(i))
                self.cw_input_lb_3[i].setObjectName('cw_input_lb_3_' + str(i))
                self.cw_input_ln_3[i].setObjectName('cw_input_ln_3_' + str(i))
                self.cw_info_bt_3[i].setObjectName('cw_info_bt_3_' + str(i))
                self.cw_input_lb_4[i].setObjectName('cw_input_lb_4_' + str(i))
                self.cw_input_ln_4[i].setObjectName('cw_input_ln_4_' + str(i))
                self.cw_info_bt_4[i].setObjectName('cw_info_bt_4_' + str(i))
        
    
    def del_output(self, index=None):
        if index is None:
            index = int(self.sender().objectName()[16:])
        self.cw_output_vl_1[index].deleteLater()
        self.cw_output_vl_1.pop(index)
        self.cw_output_vl_2[index].deleteLater()
        self.cw_output_vl_2.pop(index)
        self.cw_output_hl_1[index].deleteLater()
        self.cw_output_hl_1.pop(index)
        self.cw_output_hl_2[index].deleteLater()
        self.cw_output_hl_2.pop(index)
        self.cw_output_hl_3[index].deleteLater()
        self.cw_output_hl_3.pop(index)
        self.cw_output_gd_1[index].deleteLater()
        self.cw_output_gd_1.pop(index)
        self.cw_output_lb_1[index].deleteLater()
        self.cw_output_lb_1.pop(index)
        self.cw_output_lb_2[index].deleteLater()
        self.cw_output_lb_2.pop(index)
        self.cw_output_lb_3[index].deleteLater()
        self.cw_output_lb_3.pop(index)
        self.cw_output_lb_4[index].deleteLater()
        self.cw_output_lb_4.pop(index)
        self.cw_output_lb_5[index].deleteLater()
        self.cw_output_lb_5.pop(index)
        self.cw_output_lb_6[index].deleteLater()
        self.cw_output_lb_6.pop(index)
        self.cw_output_lb_7[index].deleteLater()
        self.cw_output_lb_7.pop(index)
        self.cw_output_ln_1[index].deleteLater()
        self.cw_output_ln_1.pop(index)
        self.cw_output_ln_2[index].deleteLater()
        self.cw_output_ln_2.pop(index)
        self.cw_output_ln_3[index].deleteLater()
        self.cw_output_ln_3.pop(index)
        self.cw_output_ln_4[index].deleteLater()
        self.cw_output_ln_4.pop(index)
        self.cw_output_ln_5[index].deleteLater()
        self.cw_output_ln_5.pop(index)
        self.cw_output_ln_6[index].deleteLater()
        self.cw_output_ln_6.pop(index)
        self.cw_output_cb_1[index].deleteLater()
        self.cw_output_cb_1.pop(index)
        self.cw_output_lw_1[index].deleteLater()
        self.cw_output_lw_1.pop(index)
        self.cw_info_bt_5[index].deleteLater()
        self.cw_info_bt_5.pop(index)
        self.cw_info_bt_6[index].deleteLater()
        self.cw_info_bt_6.pop(index)
        self.cw_info_bt_7[index].deleteLater()
        self.cw_info_bt_7.pop(index)
        self.cw_info_bt_8[index].deleteLater()
        self.cw_info_bt_8.pop(index)
        self.cw_info_bt_9[index].deleteLater()
        self.cw_info_bt_9.pop(index)
        self.cw_info_bt_10[index].deleteLater()
        self.cw_info_bt_10.pop(index)
        self.cw_info_bt_11[index].deleteLater()
        self.cw_info_bt_11.pop(index)
        self.cw_output_del_1[index].deleteLater()
        self.cw_output_del_1.pop(index)
        self.cw_output_add_1[index].deleteLater()
        self.cw_output_add_1.pop(index)
        self.cw_output_li_1[index].deleteLater()
        self.cw_output_li_1.pop(index)
        self.output_num -= 1
        if len(self.cw_output_vl_1) > 0:
            for i in range(0, len(self.cw_output_vl_1)):
                self.cw_output_vl_1[i].setObjectName('cw_output_vl_1_' + str(i))
                self.cw_output_hl_1[i].setObjectName('cw_output_hl_1_' + str(i))
                self.cw_output_del_1[i].setObjectName('cw_output_del_1_' + str(i))
                self.cw_output_vl_2[i].setObjectName('cw_output_vl_2_' + str(i))
                self.cw_output_gd_1[i].setObjectName('cw_output_gd_1_' + str(i))
                self.cw_output_lb_1[i].setObjectName('cw_output_lb_1_' + str(i))
                self.cw_output_ln_1[i].setObjectName('cw_output_ln_1_' + str(i))
                self.cw_info_bt_5[i].setObjectName('cw_info_bt_5_' + str(i))
                self.cw_output_lb_2[i].setObjectName('cw_output_lb_2_' + str(i))
                self.cw_output_ln_2[i].setObjectName('cw_output_ln_2_' + str(i))
                self.cw_info_bt_6[i].setObjectName('cw_info_bt_6_' + str(i))
                self.cw_output_lb_3[i].setObjectName('cw_output_lb_3_' + str(i))
                self.cw_output_ln_3[i].setObjectName('cw_output_ln_3_' + str(i))
                self.cw_info_bt_7[i].setObjectName('cw_info_bt_7_' + str(i))
                self.cw_output_lb_4[i].setObjectName('cw_output_lb_4_' + str(i))
                self.cw_output_ln_4[i].setObjectName('cw_output_ln_4_' + str(i))
                self.cw_info_bt_8[i].setObjectName('cw_info_bt_8_' + str(i))
                self.cw_output_hl_2[i].setObjectName('cw_output_hl_2_' + str(i))
                self.cw_output_lb_5[i].setObjectName('cw_output_lb_5_' + str(i))
                self.cw_output_ln_5[i].setObjectName('cw_output_ln_5_' + str(i))
                self.cw_output_ln_6[i].setObjectName('cw_output_ln_6_' + str(i))
                self.cw_info_bt_9[i].setObjectName('cw_info_bt_9_' + str(i))
                self.cw_info_bt_10[i].setObjectName('cw_info_bt_10_' + str(i))
                self.cw_info_bt_11[i].setObjectName('cw_info_bt_11_' + str(i))
                self.cw_output_hl_3[i].setObjectName('cw_output_hl_3_' + str(i))
                self.cw_output_lb_6[i].setObjectName('cw_output_lb_6_' + str(i))
                self.cw_output_lb_7[i].setObjectName('cw_output_lb_7_' + str(i))
                self.cw_output_add_1[i].setObjectName("cw_output_add_1_" + str(i))
                self.cw_output_lw_1[i].setObjectName("cw_output_lw_1_" + str(i))
                self.cw_output_li_1[i].setObjectName("cw_output_li_1_" + str(i))
        
        
    def add_category(self, algorithm=False):
        if algorithm:
            if self.listWidget.count() > 0:
                return
        if not algorithm:
            index = int(self.sender().objectName()[16:])
            combo_widget = self.cw_output_cb_1[index]
            list_widget = self.cw_output_lw_1[index]
        else:
            combo_widget = self.cw_combobox_1
            list_widget = self.listWidget
        category = ''
        in_list = False
        if combo_widget.currentText() == 'Other...':
            x = QtGui.QCursor.pos().x()
            y = QtGui.QCursor.pos().y()
            x = x - 150
            y = y + 50
            self.categoryWindow = MyCategory()
            self.categoryWindow.setMinimumSize(QtCore.QSize(340, self.categoryWindow.sizeHint().height()))
            self.categoryWindow.setMaximumSize(QtCore.QSize(340, self.categoryWindow.sizeHint().height()))
            self.categoryWindow.setGeometry(x, y, 340, self.categoryWindow.sizeHint().height())
            if self.categoryWindow.exec_():
                category = str(self.categoryWindow.ac_line.text())
        elif combo_widget.currentText() != 'Make a choice...':
            category = str(combo_widget.currentText())
        if category:
            for i in range(0, list_widget.count()):
                if category == str(list_widget.item(i).text()):
                    in_list = True
                    break
            if not in_list:
                list_widget.addItem(category)
    
    
    def remove_category(self, algorithm=False):
        if not algorithm:
            index = int(self.sender().objectName()[15:])
            self.cw_output_lw_1[index].takeItem(self.cw_output_lw_1[index].currentRow())
        else:
            self.listWidget.takeItem(self.listWidget.currentRow())
    
    
    def prepare_algorithm(self):
        cancel = self.check_all_fields()
        if cancel == True:
            return
        self.unitWindow = MyUnit(self.validate_units())
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.unitWindow.geometry().getRect()
        self.unitWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.unitWindow.setMinimumSize(QtCore.QSize(550, self.unitWindow.sizeHint().height()))
        self.unitWindow.setMaximumSize(QtCore.QSize(550, self.unitWindow.sizeHint().height()))
        if self.unitWindow.exec_():
            self.filenameWindow = MyFilename()
            x1, y1, w1, h1 = self.geometry().getRect()
            x2, y2, w2, h2 = self.filenameWindow.geometry().getRect()
            self.filenameWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
            self.filenameWindow.setMinimumSize(QtCore.QSize(360, self.filenameWindow.sizeHint().height()))
            self.filenameWindow.setMaximumSize(QtCore.QSize(360, self.filenameWindow.sizeHint().height()))
            if self.filenameWindow.exec_():
                filename = str(self.filenameWindow.ac_line.text())
                if filename:
                    author = '__author__ = "' + str(self.cw_line_2.text()) + '"\n'
                    date = '__date__ = "$Date:: ' + self.egads_algorithm_datestring() + '#$"\n'
                    version = '__version__ = "$Revision:: 1       $"\n'
                    all = '__all__ = ["' + str(self.cw_line_1.text()) + '"]\n\n'
                    alg_imports = 'import egads.core.egads_core as egads_core\nimport egads.core.metadata as egads_metadata\n\n'
                    alg_class = 'class ' + str(self.cw_line_1.text()) + '(egads_core.EgadsAlgorithm):\n\n'
                    category = ''
                    if self.listWidget.count()> 0:
                        category = str(self.listWidget.item(0).text())
                    purpose = self.prepare_long_string(str(self.cw_plain_2.toPlainText()), 75, 16)
                    description = self.prepare_long_string(str(self.cw_plain_1.toPlainText()), 75, 16)
                    source = self.prepare_long_string(str(self.cw_line_3.text()), 75, 16)
                    reference = self.prepare_long_string(str(self.cw_line_4.text()), 75, 16)
                    alg_input = self.prepare_inputs()
                    alg_output = self.prepare_outputs()
                    alg_help = ('    """\n'
                                + '    FILE        ' + filename + '.py\n'
                                + '\n'
                                + '    VERSION     $Revision: 100 $\n'
                                + '\n'
                                + '    CATEGORY    ' + category + '\n'
                                + '\n'
                                + '    PURPOSE     ' + purpose + '\n'
                                + '\n'
                                + '    DESCRIPTION ' + description + '\n'
                                + '\n'
                                + '    INPUT       ' + alg_input
                                + '\n'
                                + '    OUTPUT      ' + alg_output
                                + '\n'
                                + '    SOURCE      ' + source + '\n'
                                + '\n'
                                + '    REFERENCES  ' + reference + '\n'
                                + '    """\n\n')
                    
                    alg_init = ('    def __init__(self, return_Egads=True):\n        '
                                + 'egads_core.EgadsAlgorithm.__init__(self, return_Egads)\n\n')
                    alg_out_metadata = self.prepare_output_metadata()
                    alg_metadata = self.prepare_algorithm_metadata()
                    alg_run = self.prepare_algorithm_run()
                    algorithm = self.prepare_algorithm_text()
                    alg_return = self.prepare_algorithm_return()
                    complete_string = (author + date + version + all + alg_imports + alg_class + alg_help
                                       + alg_init + alg_out_metadata + alg_metadata + alg_run + algorithm
                                       + alg_return)
                    try:
                        self.write_algorithm(filename, complete_string, category, str(self.cw_line_2.text()))
                        self.success = True
                    except Exception:
                        self.success = False
                    self.algorithm_filename = filename
                    self.algorithm_category = category
                    self.algorithm_name = str(self.cw_line_1.text())
                    self.close()
            
            
    def write_algorithm(self, filename, string, category, author):
        if not category:
            logging.error('Exception, there is no category for the algorithm. Impossible to save it.')
            raise Exception("ERROR: Unexpected error")
        category = category.lower()
        algorithm_path = egads.__path__[0] + '/algorithms/user/' + category
        if os.path.isdir(algorithm_path):
            with open(algorithm_path + '/__init__.py', 'r') as in_file:
                init_file = in_file.readlines()
            import_num, add_num = 0, 0
            for line in init_file:
                if '    from ' in line:
                    import_num += 1       
            if import_num == 0:
                with open(algorithm_path + '/__init__.py', 'w') as out_file:
                    for line in init_file:
                        if 'try:' in line:
                            line = line + '    from ' + filename + ' import *\n'
                        out_file.write(line)
            else:
                with open(algorithm_path + '/__init__.py', 'w') as out_file:
                    for line in init_file:
                        if '    from ' in line:
                            add_num += 1
                            if add_num == import_num:
                                line = line + '    from ' + filename + ' import *\n'
                        out_file.write(line)
            algorithm_file = open(algorithm_path + '/' + filename + '.py','w') 
            algorithm_file.write(string) 
            algorithm_file.close() 
        else:
            os.makedirs(algorithm_path)
            init_string = ('__author__ = "' + author + '"\n'
                           + '__date__ = "$Date: ' + self.egads_algorithm_datestring() + '$"\n'
                           + '__version__ = "$Revision: 100 $"\n\n'
                           + 'import logging\n\n'
                           + 'try:\n'
                           + '    from ' + filename + ' import *\n'
                           + "    logging.info('egads [user/comparisons] algorithms have been loaded')\n"
                           + 'except Exception:\n'
                           + "    logging.error('an error occured during the loading of a [user/comparisons] algorithm')\n")
            init_file = open(algorithm_path + '/__init__.py','w')
            init_file.write(init_string) 
            init_file.close() 
            
            with open(egads.__path__[0] + '/algorithms/user/' + '/__init__.py', 'r') as in_file:
                init_file = in_file.readlines()
            import_num, add_num = 0, 0
            for line in init_file:
                if 'import ' in line:
                    import_num += 1       
            with open(egads.__path__[0] + '/algorithms/user/' + '/__init__.py', 'w') as out_file:
                for line in init_file:
                    if 'import ' in line:
                        add_num += 1
                        if add_num == import_num:
                            line = line + '\nimport egads.algorithms.user.' + category
                    out_file.write(line)
            
            algorithm_file = open(algorithm_path + '/' + filename + '.py','w') 
            algorithm_file.write(string) 
            algorithm_file.close()
            
            
    def egads_algorithm_datestring(self):        
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        hour = str(datetime.datetime.now().hour)
        minute = str(datetime.datetime.now().minute)
        date_string = year + '-' + month + '-' + day + ' ' + hour + ':' + minute
        return date_string
    
    
    def prepare_long_string(self, string, length, space_num):
        new_string = ''
        i = 0
        while len(string) > length:
            if i > 0 :
                new_string += ' ' * space_num
            new_string += string[:length] + '\n'
            string = string[length:]
            i += 1
        else:
            if i > 0:
                new_string += ' ' * space_num + string
            else:
                new_string += string
        return new_string
    
    
    def prepare_inputs(self):
        input_string = ''
        input_symbols = []
        input_types = []
        input_units = []
        input_description = []
        for i in range(len(self.cw_input_vl_1)):
            input_symbols.append(str(self.cw_input_ln_1[i].text()))
            if str(self.cw_input_ln_2[i].text()):
                unit_validation = egads.EgadsData(value=[0], units=str(self.cw_input_ln_2[i].text()))
                self.units_list[str(self.cw_input_ln_1[i].text())] = [str(self.cw_input_ln_2[i].text()), unit_validation.units, 'input']
                input_units.append(str(self.cw_input_ln_2[i].text()))
            else:
                input_units.append('_')
            input_types.append(str(self.cw_input_ln_3[i].text()))
            input_description.append(str(self.cw_input_ln_4[i].text()))
        max_symbols_length = self.check_string_max_length(input_symbols)
        max_units_length = self.check_string_max_length(input_units)
        max_types_length = self.check_string_max_length(input_types)
        for i in range(len(self.cw_input_vl_1)):
            tmp_string = ' ' * 16
            tmp_string += (input_symbols[i] + ' ' * (max_symbols_length - len(input_symbols[i]) + 4)
                             + input_types[i] + ' ' * (max_types_length - len(input_types[i]) + 4)
                             + input_units[i] + ' ' * (max_units_length - len(input_units[i]) + 4)
                             + input_description[i])
            carriage_length = max_symbols_length + max_types_length + max_units_length + 28
            tmp_string = self.prepare_long_string(tmp_string, 75, carriage_length)
            input_string += tmp_string + '\n'
        return input_string[16:]
    
    
    def prepare_outputs(self):
        output_string = ''
        output_symbols = []
        output_types = []
        output_units = []
        output_description = []
        for i in range(len(self.cw_output_vl_1)):
            output_symbols.append(str(self.cw_output_ln_1[i].text()))
            if str(self.cw_output_ln_3[i].text()):
                if 'input' in str(self.cw_output_ln_3[i].text()):
                    output_units.append('_')
                else:
                    unit_validation = egads.EgadsData(value=[0], units=str(self.cw_output_ln_3[i].text()))
                    self.units_list[str(self.cw_output_ln_1[i].text())] = [str(self.cw_output_ln_3[i].text()), unit_validation.units, 'output']
                    output_units.append(str(self.cw_output_ln_3[i].text()))
            else:
                output_units.append('_')
            output_types.append(str(self.cw_output_ln_6[i].text()))
            output_description.append(str(self.cw_output_ln_5[i].text()))
        max_symbols_length = self.check_string_max_length(output_symbols)
        max_units_length = self.check_string_max_length(output_units)
        max_types_length = self.check_string_max_length(output_types)
        for i in range(len(self.cw_output_vl_1)):
            tmp_string = ' ' * 16
            tmp_string += (output_symbols[i] + ' ' * (max_symbols_length - len(output_symbols[i]) + 4)
                             + output_types[i] + ' ' * (max_types_length - len(output_types[i]) + 4)
                             + output_units[i] + ' ' * (max_units_length - len(output_units[i]) + 4)
                             + output_description[i])
            carriage_length = max_symbols_length + max_types_length + max_units_length + 28
            tmp_string = self.prepare_long_string(tmp_string, 75, carriage_length)
            output_string += tmp_string + '\n'
        return output_string[16:]
    
    
    def prepare_algorithm_metadata(self):
        input_symbols = ''
        input_units = ''
        input_types = ''
        input_description = ''
        output_symbols = ''
        output_description = ''
        for i in range(len(self.cw_input_vl_1)):
            if i == 0:
                input_symbols = '['
                input_units = '['
                input_types = '['
                input_description = '['
            input_symbols += "'" + str(self.cw_input_ln_1[i].text()) + "',"
            input_units += "'" + str(self.cw_input_ln_2[i].text()) + "',"
            input_types += "'" + str(self.cw_input_ln_3[i].text()) + "',"
            input_description += "'" + str(self.cw_input_ln_4[i].text()) + "',"
        input_symbols = input_symbols[:-1] + ']'
        input_units = input_units[:-1] + ']'
        input_types = input_types[:-1] + ']'
        input_description = input_description[:-1] + ']'
        for i in range(len(self.cw_output_vl_1)):
            if i == 0:
                output_symbols = '['
                output_description = '['
            output_symbols +=  "'" + str(self.cw_output_ln_1[i].text()) + "',"
            output_description +=  "'" + str(self.cw_output_ln_5[i].text()) + "',"
        output_symbols = output_symbols[:-1] + ']'
        output_description = output_description[:-1] + ']'
        metadata_string = ("        self.metadata = egads_metadata.AlgorithmMetadata({'Inputs':" + input_symbols + ",\n"
                       + "                                                          'InputUnits':" + input_units + ",\n"
                       + "                                                          'InputTypes':" + input_types + ",\n"
                       + "                                                          'InputDescription':" + input_description + ",\n"
                       + "                                                          'Outputs':" + output_symbols + ",\n"
                       + "                                                          'OutputDescription':" + output_description + ",\n"
                       + "                                                          'Purpose':'" + str(self.cw_plain_2.toPlainText()) + "',\n"
                       + "                                                          'Description':'" + str(self.cw_plain_1.toPlainText()) + "',\n"
                       + "                                                          'Processor':self.name,\n"
                       + "                                                          'ProcessorDate':__date__,\n"
                       + "                                                          'ProcessorVersion':__version__,\n"
                       + "                                                          'DateProcessed':self.now()},\n"
                       + "                                                          self.output_metadata)\n\n")
        return metadata_string

    
    def prepare_output_metadata(self):
        output_string = ''
        if len(self.cw_output_vl_1) > 1:
            output_string += '        self.output_metadata = []\n'
            for i in range(len(self.cw_output_vl_1)):
                units = str(self.cw_output_ln_3[i].text())
                long_name = str(self.cw_output_ln_4[i].text())
                standard_name = str(self.cw_output_ln_2[i].text())
                category = ''
                if self.cw_output_lw_1[i].count() > 0:
                    category += '['
                    for j in range(self.cw_output_lw_1[i].count()):
                        category += "'" + self.cw_output_lw_1[i].item(j).text() + "',"
                    category = category[:-1] + ']'
                output_string += ("        self.output_metadata.append(egads_metadata.VariableMetadata({"
                                  + "'units':'" + units + "',\n"
                                  + ' ' * 63 + "'long_name':'" + long_name + "',\n"
                                  + ' ' * 63 + "'standard_name':'" + standard_name + "',\n"
                                  + ' ' * 63 + "'Category':" + category + "}))\n\n")
        elif len(self.cw_output_vl_1) == 1:
            units = str(self.cw_output_ln_3[0].text())
            long_name = str(self.cw_output_ln_4[0].text())
            standard_name = str(self.cw_output_ln_2[0].text())
            category = ''
            if self.cw_output_lw_1[0].count() > 0:
                category += '['
                for j in range(self.cw_output_lw_1[0].count()):
                    category += "'" + self.cw_output_lw_1[0].item(j).text() + "',"
                category = category[:-1] + ']'
            output_string += ("        self.output_metadata = egads_metadata.VariableMetadata({"
                                  + "'units':'" + units + "',\n"
                                  + ' ' * 63 + "'long_name':'" + long_name + "',\n"
                                  + ' ' * 63 + "'standard_name':'" + standard_name + "',\n"
                                  + ' ' * 63 + "'Category':" + category + "})\n\n")
        return output_string
    
    
    def prepare_algorithm_run(self):
        run_string = ''
        input_symbols = ''
        for i in range(len(self.cw_input_vl_1)):
            input_symbols += str(self.cw_input_ln_1[i].text()) + ", "
        input_symbols = input_symbols[:-2]
        run_string += ("    def run(self, " + input_symbols + "):\n"
                       + "        return egads_core.EgadsAlgorithm.run(self, " + input_symbols + ")\n\n"
                       + "    def _algorithm(self, " + input_symbols + "):\n")
        return run_string
    
    
    def prepare_algorithm_text(self):
        algorithm_string = ''
        if self.cw_plain_4.toPlainText():
            algorithm = ' ' * 8 + str(self.cw_plain_4.toPlainText())
            algorithm_string = algorithm.replace('\n', '\n        ')
            algorithm_string += '\n'
        return algorithm_string
    
    
    def prepare_algorithm_return(self):
        return_string = ''
        if self.cw_output_vl_1:
            return_string += '        return '
            for i in range(len(self.cw_output_vl_1)):
                return_string += str(self.cw_output_ln_1[i].text()) + ', '
            return_string = return_string[:-2] + '\n\n'
        return return_string
    
    
    def check_string_max_length(self, string_list):
        max_length = 0
        for string in string_list:
            if len(string) > max_length:
                max_length = len(string)
        return max_length
    
    
    def check_all_fields(self):
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
        for label in self.findChildren(QtWidgets.QLabel):
            label.setStyleSheet('color: black;')
        algorithm_section = True
        for widget, label in self.algorithm_mandatory_fields.iteritems():
            if isinstance(widget, QtWidgets.QLineEdit):
                if not widget.text():
                    algorithm_section = False
                    label.setStyleSheet('color: rgb(200,0,0);')
                    self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200,0,0))
            elif isinstance(widget, QtWidgets.QPlainTextEdit):
                if not widget.toPlainText():
                    algorithm_section = False
                    label.setStyleSheet('color: rgb(200,0,0);')
                    self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200,0,0))
            elif isinstance(widget, QtWidgets.QListWidget):
                if widget.count() == 0:
                    algorithm_section = False
                    label.setStyleSheet('color: rgb(200,0,0);')
                    self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200,0,0))
        input_section = True
        widget_list = []
        if self.cw_input_vl_1:
            widget_list = self.tab_1.findChildren(QtWidgets.QLineEdit)
            for widget in widget_list:
                if 'cw_input_ln_2' not in widget.objectName():
                    if not widget.text():
                        input_section = False
                        label = self.tab_1.findChildren(QtWidgets.QLabel, widget.objectName()[:9] + 'lb' + widget.objectName()[11:])[0]
                        label.setStyleSheet('color: rgb(200,0,0);')
                        self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200,0,0))
        else:
            input_section = False
            self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200,0,0))
        output_section = True
        if self.cw_output_vl_1:
            widget_list = self.tab_2.findChildren(QtWidgets.QLineEdit)
            for widget in widget_list:
                if ('cw_output_ln_3' not in widget.objectName()) and ('cw_output_ln_4' not in widget.objectName()):
                    if not widget.text():
                        output_section = False
                        label = self.tab_2.findChildren(QtWidgets.QLabel, widget.objectName()[:10] + 'lb' + widget.objectName()[12:])[0]
                        label.setStyleSheet('color: rgb(200,0,0);')
                        self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200,0,0))
        else:
            output_section = False
            self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200,0,0))
        if not output_section or not input_section or not algorithm_section:
            self.fillWindow = MyFill()
            x1, y1, w1, h1 = self.geometry().getRect()
            x2, y2, w2, h2 = self.fillWindow.geometry().getRect()
            self.fillWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
            self.fillWindow.setMinimumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
            self.fillWindow.setMaximumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
            self.fillWindow.exec_()
            return self.fillWindow.cancel
        else:
            return False
    
    
    def validate_units(self):
        units_list = []
        for i in range(len(self.cw_input_vl_1)):
            if str(self.cw_input_ln_2[i].text()):
                unit_validation = egads.EgadsData(value=[0], units=str(self.cw_input_ln_2[i].text()))
                units_list.append([str(self.cw_input_ln_1[i].text()), str(self.cw_input_ln_2[i].text()), unit_validation.units, 'input'])
        for i in range(len(self.cw_output_vl_1)):
            if str(self.cw_output_ln_3[i].text()):
                if 'input' in str(self.cw_output_ln_3[i].text()):
                    pass
                else:
                    unit_validation = egads.EgadsData(value=[0], units=str(self.cw_output_ln_3[i].text()))
                    units_list.append([str(self.cw_output_ln_1[i].text()), str(self.cw_output_ln_3[i].text()), unit_validation.units, 'output'])
        return units_list
    
        
    def closeWindow(self):
        self.close()


class MyCategory(QtWidgets.QDialog, Ui_Addcategory):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept() 
        
        
class MyFilename(QtWidgets.QDialog, Ui_Addfilename):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()        
        
        
class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.fw_cancelButton.clicked.connect(self.cancelWindow)
        self.cancel = False
        self.fw_cancelButton.setFocus(True)

    def cancelWindow(self):
        self.cancel = True
        self.close()
        
        
class MyUnit(QtWidgets.QDialog, Ui_unitWindow):
    def __init__(self, units_list):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.units_list = units_list
        self.uw_label.setText(self.prepare_text())
        self.uw_cancelButton.clicked.connect(self.closeWindow)
        self.uw_okButton.clicked.connect(self.submitBox)
    
    def prepare_text(self):
        if len(self.units_list) > 1:
            text = ('<p>Too handle units properly, EGADS must validate and, probably, rewrite input and out'
                    + 'put units. Please check the <b>proposals</b> made by EGADS, and click Continue if you '
                    + 'are agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><ul><li>Inputs:<ul>')
            for sublist in self.units_list:
                if sublist[3] == 'input':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;<b>' + sublist[2] + '</b></li>'
            text += '</ul></li><br><li>Outputs:<ul>'
            for sublist in self.units_list:
                if sublist[3] == 'output':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;<b>' + sublist[2] + '</b></li>'
            text += '</ul></li></ul>'
        else:
            text = ('<p>Too handle units properly, EGADS must validate units in the current window. '
                    + 'Please check the <b>proposal</b> made by EGADS, and click Continue if you '
                    + 'are agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><p>Proposal:<br>')
            text += ('&nbsp;&nbsp;&nbsp;&nbsp;' + self.units_list[0][0] + ':&nbsp;&nbsp;&nbsp;&nbsp;' + self.units_list[0][1] 
                     + '&nbsp;&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;&nbsp;<b>' + self.units_list[0][2] + '</b></p>')
        return text
    
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()  
        
        
class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, button_string, title_string):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            widget.clicked.connect(lambda: self.closeWindow())
        self.iw_nosaveButton.setText(button_string + " without saving")
        self.setWindowTitle(title_string)

    def closeWindow(self):
        self.buttonName = self.sender().objectName()
        self.close()
        
        
        
        
        
