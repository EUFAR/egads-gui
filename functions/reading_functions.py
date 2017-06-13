# -*- coding: utf-8 -*-

from egads import input, EgadsData
import ntpath
import logging
'''from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QToolButton, QPlainTextEdit, QLineEdit
from PyQt4.QtCore import QObject, SIGNAL'''

from PyQt5 import QtCore, QtWidgets

from gui_functions import modify_attribute_gui
from gui_functions import update_icons_state
from gui_functions import clear_gui
from gui_functions import update_compatibility_label
from gui_functions import read_set_attribute_gui
from gui_functions import update_global_attribute_gui
from gui_functions import update_variable_attribute_gui
from other_functions import add_global_attributes_to_buttons
try:
    from netcdftime._netcdftime import utime
except ImportError:
    from netcdftime.netcdftime import utime
import copy


def netcdf_reading(self):
    logging.info('NetCDF Reading - loading netcdf')
    logging.info('NetCDF Reading -               ' + self.open_file_name)
    clear_gui(self)
    self.opened_file = input.EgadsNetCdf(self.open_file_name, 'a')
    self.list_of_variables = self.opened_file.get_variable_list()
    self.list_of_global_attributes = self.opened_file.get_attribute_list()
    self.list_of_dimensions = self.opened_file.get_dimension_list()
    add_global_attributes_to_buttons(self)
    for var in self.list_of_variables:
        dimensions = self.opened_file.get_dimension_list(str(var))
        list_of_var_attributes = self.opened_file.get_attribute_list(str(var))
        list_of_var_attributes['var_name'] = str(var)
        list_of_var_attributes = add_correct_units(self, list_of_var_attributes)
        egads_instance = self.opened_file.read_variable(var)
        self.list_of_variables_and_attributes[var] = [var, list_of_var_attributes, dimensions, egads_instance]
    update_compatibility_label(self)
    out_file_base, out_file_ext = ntpath.splitext(ntpath.basename(self.open_file_name))
    read_set_attribute_gui(self, self.gm_filename_ln, out_file_base + out_file_ext)
    update_global_attribute_gui(self, 'NetCDF')
    self.listWidget.addItems(sorted(self.list_of_variables))
    self.listWidget.itemClicked.connect(lambda: var_reading(self))
    self.tabWidget.currentChanged.connect(lambda: update_icons_state(self))
    all_buttons = self.findChildren(QtWidgets.QToolButton)
    for widget in all_buttons:
        widget.clicked.connect(lambda: modify_attribute_gui(self))
    logging.info("NetCDF Reading - netcdf loaded")
    

def nasaames_reading(self):
    logging.info('NASA Ames Reading - loading nasaames')
    logging.info('NASA Ames Reading -               ' + self.open_file_name)
    clear_gui(self)
    self.opened_file = input.NasaAmes(self.open_file_name, 'r')
    self.list_of_variables = self.opened_file.get_variable_list(vartype='independant') + self.opened_file.get_variable_list(vartype='main')
    list_of_attributes = self.opened_file.get_attribute_list()
    self.list_of_global_attributes = {}
    for attribute in list_of_attributes:
        if attribute != 'V' and attribute != 'X':
            self.list_of_global_attributes[attribute] = self.opened_file.get_attribute_value(attribute)
    self.list_of_dimensions = self.opened_file.get_dimension_list(vartype='independant')
    list_of_var_dimensions = self.opened_file.get_dimension_list(vartype='main')
    add_global_attributes_to_buttons(self)
    for var in self.list_of_variables:
        dimensions = self.list_of_dimensions 
        try:
            list_of_attributes = self.opened_file.get_attribute_list(str(var), vartype='main')
        except ValueError:
            list_of_attributes = self.opened_file.get_attribute_list(str(var), vartype='independant')
        list_of_var_attributes = {}
        for attribute in list_of_attributes:
            try:
                list_of_var_attributes[attribute] = self.opened_file.get_attribute_value(attribute, var, 'main')
            except ValueError:
                list_of_var_attributes[attribute] = self.opened_file.get_attribute_value(attribute, var, 'independant')
        list_of_var_attributes['var_name'] = str(var)
        list_of_var_attributes = add_correct_units(self, list_of_var_attributes)
        egads_instance = self.opened_file.read_variable(var)
        self.list_of_variables_and_attributes[var] = [var, list_of_var_attributes, dimensions, egads_instance]
    #update_compatibility_label(self)
    out_file_base, out_file_ext = ntpath.splitext(ntpath.basename(self.open_file_name))
    read_set_attribute_gui(self, self.gm_filename_ln, out_file_base + out_file_ext)
    update_global_attribute_gui(self, 'NASA Ames')
    self.listWidget.addItems(self.list_of_variables)
    self.listWidget.itemClicked.connect(lambda: var_reading(self))
    self.tabWidget.currentChanged.connect(lambda: update_icons_state(self))
    all_buttons = self.findChildren(QtWidgets.QToolButton)
    for widget in all_buttons:
        widget.clicked.connect(lambda: modify_attribute_gui(self))
    logging.info("NASA Ames Reading - nasaames loaded")


def var_reading(self):
    logging.info("NetCDF Reading - loading variable information")
    logging.info("NetCDF Reading -                " + self.listWidget.currentItem().text())
    update_icons_state(self, 'var_reading')
    clear_gui(self, 'variable')
    all_lines_edit = self.tab_2.findChildren(QtWidgets.QLineEdit)
    for widget in all_lines_edit:
        widget.setEnabled(False)
    all_text_edit = self.tab_2.findChildren(QtWidgets.QPlainTextEdit)
    for widget in all_text_edit:
        widget.setEnabled(False)
    update_variable_attribute_gui(self, 1)
    logging.info("NetCDF Reading - variable information loaded")


    
'''def nasaames_var_reading(self):
    self.va_button_1.setEnabled(True)
    self.va_button_2.setEnabled(True)
    self.va_button_3.setEnabled(True)
    self.va_button_4.setEnabled(True)
    self.actionAlgorithmsBar.setEnabled(True)
    self.actionDeleteVariableBar.setEnabled(True)
    self.actionVariableAttributesBar.setEnabled(True)
    self.actionPlotBar.setEnabled(True)
    self.actionDisplayBar.setEnabled(True)
    all_lines_edit = self.findChildren(QLineEdit)
    for widget in all_lines_edit:
        if "va_" in widget.objectName():
            widget.setEnabled(False)
    all_text_edit = self.findChildren(QPlainTextEdit)
    for widget in all_text_edit:
        if "va" in widget.objectName():
            widget.setEnabled(False)
    all_buttons = self.findChildren(QToolButton)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    for widget in all_buttons:
        if "va" in widget.objectName():
            widget.setIcon(icon)
    self.actionAlgorithmsBar.setEnabled(True)
    self.actionDeleteVariableBar.setEnabled(True)
    self.actionVariableAttributesBar.setEnabled(True)
    self.actionPlotBar.setEnabled(True)
    var = self.listWidget.currentItem().text()
    for sublist in self.modified_variable_attributes:
        if sublist[2] == var and sublist[1] == "var_name":
            var = sublist[0]
    
    self.va_varName_ln.setText("")
    self.va_longName_ln.setText("")
    self.va_category_ln.setText("")
    self.va_units_ln.setText("")
    self.va_fillValue_ln.setText("")
    self.va_dimensions_ln.setText("")
    self.va_egadsProcessor_ln.setPlainText("")
    try:
        list_of_var_attributes = self.opened_file.get_attribute_list(str(var), "main")
    except ValueError:
        list_of_var_attributes = self.opened_file.get_attribute_list(str(var), "independant")
    
    var_name = var
    if self.modified_variable_attributes:
        for sublist in self.modified_variable_attributes:
            if sublist[1] != "var_name":
                for key, value in list_of_var_attributes.iteritems():  # @UnusedVariable
                    if sublist[0] == var and sublist[1] == key:
                            list_of_var_attributes[key] = sublist[2]
                            break
            elif sublist[1] == "var_name" and sublist[0] == var:
                var_name = sublist[2]
       
    self.va_varName_ln.setText(var_name)
    self.va_varName_ln.setCursorPosition(0)
                    
    try:
        self.va_longName_ln.setText(' '.join(str(list_of_var_attributes["name"]).split()))
        self.va_longName_ln.setCursorPosition(0)
    except KeyError:
        self.va_longName_ln.setText("")
    try:
        self.va_units_ln.setText(str(list_of_var_attributes["units"]))
        self.va_units_ln.setCursorPosition(0)
    except KeyError:
        self.va_units_ln.setText("")
    try:
        self.va_category_ln.setText(str(list_of_var_attributes["Category"]))
        self.va_category_ln.setCursorPosition(0)
    except KeyError:
        self.va_category_ln.setText("")
    try:
        self.va_fillValue_ln.setText(str(list_of_var_attributes["_FillValue"]))
    except KeyError:
        try:
            self.va_fillValue_ln.setText(str(list_of_var_attributes["missing_value"]))
        except KeyError:
            self.va_fillValue_ln.setText("")
    try:
        self.va_egadsProcessor_ln.setPlainText(str(list_of_var_attributes["Processor"]))
    except KeyError:
        self.va_egadsProcessor_ln.setPlainText("")'''
        
        
        
'''def new_var_reading(self):
    logging.info("NetCDF Reading - loading new variable information")
    logging.info("NetCDF Reading -                " + self.new_listwidget.currentItem().text())
    self.new_button_1.setEnabled(True)
    self.new_button_2.setEnabled(True)
    self.new_button_3.setEnabled(True)
    self.new_button_4.setEnabled(True)
    self.actionAlgorithmsBar.setEnabled(True)
    self.actionDeleteVariableBar.setEnabled(True)
    self.actionVariableAttributesBar.setEnabled(True)
    self.actionPlotBar.setEnabled(True)
    self.actionDisplayBar.setEnabled(True)
    all_lines_edit = self.findChildren(QLineEdit)
    for widget in all_lines_edit:
        if "new_" in widget.objectName():
            widget.setEnabled(False)
    all_text_edit = self.findChildren(QPlainTextEdit)
    for widget in all_text_edit:
        if "new_" in widget.objectName():
            widget.setEnabled(False)
    all_buttons = self.findChildren(QToolButton)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    for widget in all_buttons:
        if "new_" in widget.objectName():
            widget.setIcon(icon)
    
    for sublist in self.list_of_new_variables_and_attributes:
        try:
            if sublist[1]["var_name"] == self.new_listwidget.currentItem().text():
                break
        except TypeError:
            pass

    self.new_varName_ln.setText(sublist[1]["var_name"])
    self.new_varName_ln.setCursorPosition(0)
    try:
        if sublist[1]["long_name"] != "deleted":
            self.new_longName_ln.setText(' '.join(str(sublist[1]["long_name"]).split()))
            self.new_longName_ln.setCursorPosition(0)
        else:
            self.new_longName_ln.setText("")
    except KeyError:
        self.new_longName_ln.setText("")
    try:
        if sublist[1]["units"] != "deleted":
            self.new_units_ln.setText(str(sublist[1]["units"]))
            self.new_units_ln.setCursorPosition(0)
        else:
            self.new_units_ln.setText("")
    except KeyError:
        self.new_units_ln.setText("")
    try:
        if sublist[1]["Category"] != "deleted":
            if isinstance(sublist[1]["Category"], list):
                category_string = ""
                for string in sublist[1]["Category"]:
                    category_string += string + ", "
                self.new_category_ln.setText(category_string[:-2])
            else:
                self.new_category_ln.setText(str(sublist[1]["Category"]))
            self.new_category_ln.setCursorPosition(0)
        else:
            self.new_category_ln.setText("")
    except KeyError:
        self.new_category_ln.setText("")
    try:
        self.new_fillValue_ln.setText(str(sublist[1]["_FillValue"]))
    except KeyError:
        try:
            self.new_fillValue_ln.setText(str(sublist[1]["missing_value"]))
        except KeyError:
            self.new_fillValue_ln.setText("")
    dimensions_str = ""
    i = 0
    for key, value in sublist[2].iteritems():
        if i == 0:
            dimensions_str = str(value) + " (" + key + ")"
        else: 
            dimensions_str = dimensions_str + " x " + str(value) + " (" + key + ")"
        i += 1
    self.new_dimensions_ln.setText(dimensions_str)
    try:
        self.new_egadsProcessor_ln.setPlainText(str(sublist[1]["Processor"]))
    except KeyError:
        self.new_egadsProcessor_ln.setPlainText("")
    logging.info("NetCDF Reading - new variable information loaded")    '''
    
    
def add_correct_units(self, attr_list, egads_instance=None):
    if "units" not in attr_list.keys():
        if "Units" in attr_list.keys():
            attr_list["units"] = attr_list["Units"]
        elif "Unit" in attr_list.keys():
            attr_list["units"] = attr_list["Unit"]
        elif "unit" in attr_list.keys():
            attr_list["units"] = attr_list["unit"]
        else:
            if isinstance(egads_instance, EgadsData) and egads_instance != None:
                try:
                    attr_list["units"] = egads_instance.units
                except AttributeError:
                    attr_list["units"] = 'no units'
            else:
                attr_list["units"] = 'no units'
    return attr_list

    