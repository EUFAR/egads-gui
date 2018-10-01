import ntpath
import logging
import copy
from egads import input, EgadsData
from PyQt5 import QtCore, QtWidgets
from functions.gui_functions import modify_attribute_gui
from functions.gui_functions import update_icons_state
from functions.gui_functions import clear_gui
from functions.gui_functions import read_set_attribute_gui
from functions.gui_functions import update_global_attribute_gui
from functions.gui_functions import update_variable_attribute_gui
from functions.material_functions import add_global_attributes_to_buttons



def netcdf_reading(self):
    logging.debug('gui - reading_functions.py - netcdf_reading')
    clear_gui(self)
    self.opened_file = input.EgadsNetCdf(self.file_name, 'a')
    list_of_variables = sorted(self.opened_file.get_variable_list())
    self.list_of_global_attributes = self.opened_file.get_attribute_list()
    self.list_of_dimensions = self.opened_file.get_dimension_list()
    add_global_attributes_to_buttons(self)
    for var in list_of_variables:
        dimensions = self.opened_file.get_dimension_list(str(var))
        list_of_var_attributes = self.opened_file.get_attribute_list(str(var))
        list_of_var_attributes['var_name'] = str(var)
        list_of_var_attributes = add_correct_units(self, list_of_var_attributes)
        try:
            egads_instance = self.opened_file.read_variable(var)
            self.list_of_variables_and_attributes[var] = [var, list_of_var_attributes, dimensions, egads_instance]
        except Exception:
            self.list_of_unread_variables.append(var)
            logging.exception('gui - reading_functions.py - : an error occured during the re'
                              + 'ading of a variable, variable ' + str(var))
    update_global_attribute_gui(self, 'NetCDF')
    self.variable_list.addItems(list_of_variables)
    self.variable_list.itemClicked.connect(lambda: var_reading(self))
    self.tab_view.currentChanged.connect(lambda: update_icons_state(self))
    all_buttons = self.tab_view.findChildren(QtWidgets.QToolButton)
    for widget in all_buttons:
        if widget.objectName() != '':
            widget.clicked.connect(lambda: modify_attribute_gui(self, 'left'))
            try:
                widget.rightClick.connect(lambda: modify_attribute_gui(self, 'right'))
            except AttributeError:
                pass
    logging.debug('gui - reading_functions.py - netcdf_reading: netcdf file loaded')
    

def nasaames_reading(self):
    logging.debug('gui - reading_functions.py - nasaames_reading : open_file_name ' + str(self.open_file_name))
    clear_gui(self)
    self.opened_file = input.NasaAmes(self.open_file_name, 'r')
    list_of_variables = sorted(self.opened_file.get_variable_list(vartype='independant') + self.opened_file.get_variable_list(vartype='main'))
    list_of_attributes = self.opened_file.get_attribute_list()
    self.list_of_global_attributes = {}
    for attribute in list_of_attributes:
        if attribute != 'V' and attribute != 'X':
            self.list_of_global_attributes[attribute] = self.opened_file.get_attribute_value(attribute)
    self.list_of_dimensions = self.opened_file.get_dimension_list(vartype='independant')
    list_of_var_dimensions = self.opened_file.get_dimension_list(vartype='main')
    add_global_attributes_to_buttons(self)
    for var in list_of_variables:
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
    out_file_base, out_file_ext = ntpath.splitext(ntpath.basename(self.open_file_name))
    read_set_attribute_gui(self, self.gm_filename_ln, out_file_base + out_file_ext)
    update_global_attribute_gui(self, 'NASA Ames')
    self.listWidget.addItems(list_of_variables)
    self.listWidget.itemClicked.connect(lambda: var_reading(self))
    self.tabWidget.currentChanged.connect(lambda: update_icons_state(self))
    all_buttons = self.tabWidget.findChildren(QtWidgets.QToolButton)
    for widget in all_buttons:
        if widget.objectName() != 'gm_button_7' and widget.objectName() != '':
            widget.clicked.connect(lambda: modify_attribute_gui(self, 'left'))
            widget.rightClick.connect(lambda: modify_attribute_gui(self, 'right'))
    logging.debug('gui - reading_functions.py - nasaames_reading : nasa ames file loaded')


def var_reading(self):
    logging.debug('gui - reading_functions.py - var_reading : variable ' + str(self.variable_list.currentItem().text()))
    update_icons_state(self, 'var_reading')
    clear_gui(self, 'variable')
    all_lines_edit = self.tab_2.findChildren(QtWidgets.QLineEdit)
    for widget in all_lines_edit:
        widget.setEnabled(False)
    all_text_edit = self.tab_2.findChildren(QtWidgets.QPlainTextEdit)
    for widget in all_text_edit:
        widget.setEnabled(False)
    update_variable_attribute_gui(self, 1)
    
    
def add_correct_units(self, attr_list, egads_instance=None):
    logging.debug(' gui - reading_functions.py - add_correct_units')
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

    