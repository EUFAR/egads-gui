# -*- coding: utf-8 -*-

import egads
import ntpath
import logging
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QToolButton, QPlainTextEdit, QLineEdit
from PyQt4.QtCore import QObject, SIGNAL
from gui_functions import modify_attribute_gui
from gui_functions import tab_change
from other_functions import check_compatibility_netcdf
from netcdftime.netcdftime import utime
import copy


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


def netcdf_reading(self, out_file_name):
    logging.info("NetCDF Reading - loading netcdf")
    logging.info("NetCDF Reading -               " + out_file_name)
    self.gm_title_ln.setText("")
    self.gm_institution_ln.setText("")
    self.gm_source_ln.setText("")
    self.gm_project_ln.setText("")
    self.gm_dateCreation_ln.setText("")
    self.gm_history_ln.setPlainText("")
    self.va_varName_ln.setText("")
    self.va_longName_ln.setText("")
    self.va_category_ln.setText("")
    self.va_units_ln.setText("")
    self.va_fillValue_ln.setText("")
    self.va_dimensions_ln.setText("")
    self.va_egadsProcessor_ln.setPlainText("")
    self.opened_file = egads.input.EgadsNetCdf(out_file_name)  # @UndefinedVariable
    self.list_of_variables = self.opened_file.get_variable_list()
    self.list_of_global_attributes = self.opened_file.get_attribute_list()
    self.list_of_dimensions = self.opened_file.get_dimension_list()
    self.list_of_variables_and_attributes = []

    for var in self.opened_file.get_variable_list():
        dimensions = self.opened_file.get_dimension_list(str(var))
        list_of_var_attributes = self.opened_file.get_attribute_list(str(var))
        list_of_var_attributes["var_name"] = str(var)
        
        if "units" not in list_of_var_attributes.keys():
            if "Units" in list_of_var_attributes.keys():
                list_of_var_attributes["units"] = list_of_var_attributes["Units"]
            elif "Unit" in list_of_var_attributes.keys():
                list_of_var_attributes["units"] = list_of_var_attributes["Unit"]
            elif "unit" in list_of_var_attributes.keys():
                list_of_var_attributes["units"] = list_of_var_attributes["unit"]
                
        if "long_name" not in list_of_var_attributes.keys():
            if "LongName" in list_of_var_attributes.keys():
                list_of_var_attributes["long_name"] = list_of_var_attributes["LongName"]
            elif "long name" in list_of_var_attributes.keys():
                list_of_var_attributes["long_name"] = list_of_var_attributes["long name"]
        
        egads_instance = self.opened_file.read_variable(var)
        self.list_of_variables_and_attributes.append([var, list_of_var_attributes, dimensions, egads_instance])
        
    
    result = check_compatibility_netcdf(self, self.list_of_global_attributes, self.list_of_variables_and_attributes)
    
    for sublist in self.compatibility_level:
        if sublist[0] == result:
            self.gm_compatibility_lb.setPixmap(QtGui.QPixmap(_fromUtf8(sublist[2])))
            self.gm_details_lb.setText(sublist[3])
            self.gm_details_lb.setMinimumSize(QtCore.QSize(sublist[4], 27))
            self.gm_details_lb.setMaximumSize(QtCore.QSize(sublist[4], 54))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(sublist[5]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.gm_button_6.setIcon(icon)
            self.gm_button_6.setEnabled(sublist[6])
            self.gm_button_6.setVisible(sublist[6])
            break
    
    
    self.missing_global_attributes = []
    out_file_base, out_file_ext = ntpath.splitext(ntpath.basename(out_file_name))
    self.gm_filename_ln.setText(out_file_base + out_file_ext)
    try:
        self.gm_title_ln.setText(self.list_of_global_attributes["title"])
        self.gm_title_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("title")
    try:
        self.gm_institution_ln.setText(self.list_of_global_attributes["institution"])
        self.gm_institution_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("institution")
    try:
        self.gm_source_ln.setText(self.list_of_global_attributes["source"])
        self.gm_source_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("source")
    try:
        self.gm_project_ln.setText(self.list_of_global_attributes["project"])
        self.gm_project_ln.setCursorPosition(0)
    except KeyError:
        pass
    try:
        self.gm_dateCreation_ln.setText(self.list_of_global_attributes["date_created"])
    except KeyError:
        pass
    try:    
        self.gm_history_ln.setPlainText(self.list_of_global_attributes["history"])
    except KeyError:
        pass
    for var in self.list_of_variables:
        self.listWidget.addItem(var)
          
    QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), lambda: netcdf_var_reading(self))
    QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), lambda: tab_change(self))
    all_buttons = self.findChildren(QToolButton)
    for widget in all_buttons:
        QObject.connect(widget, SIGNAL("clicked()"), lambda: modify_attribute_gui(self))
    logging.info("NetCDF Reading - netcdf loaded")
    
    
def netcdf_var_reading(self):
    logging.info("NetCDF Reading - loading variable information")
    logging.info("NetCDF Reading -                " + self.listWidget.currentItem().text())
    self.va_button_1.setEnabled(True)
    self.va_button_2.setEnabled(True)
    self.va_button_3.setEnabled(True)
    self.va_button_4.setEnabled(True)
    self.actionAlgorithmsBar.setEnabled(True)
    self.actionDeleteVariableBar.setEnabled(True)
    self.actionVariableAttributesBar.setEnabled(True)
    self.actionPlotBar.setEnabled(True)
    self.actionDisplayBar.setEnabled(True)
    self.va_varName_ln.setText("")
    self.va_longName_ln.setText("")
    self.va_category_ln.setText("")
    self.va_units_ln.setText("")
    self.va_fillValue_ln.setText("")
    self.va_dimensions_ln.setText("")
    self.va_egadsProcessor_ln.setPlainText("")
    all_lines_edit = self.findChildren(QLineEdit)
    for widget in all_lines_edit:
        if "va_" in widget.objectName():
            widget.setEnabled(False)
    all_text_edit = self.findChildren(QPlainTextEdit)
    for widget in all_text_edit:
        if "va_" in widget.objectName():
            widget.setEnabled(False)
    all_buttons = self.findChildren(QToolButton)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    for widget in all_buttons:
        if "va_" in widget.objectName():
            widget.setIcon(icon)
    for sublist in self.list_of_variables_and_attributes:
        try:
            if sublist[1]["var_name"] == self.listWidget.currentItem().text():
                break
        except TypeError:
            pass
        
        
    self.va_varName_ln.setText(sublist[1]["var_name"])
    self.va_varName_ln.setCursorPosition(0)
    try:
        if sublist[1]["long_name"] != "deleted":
            self.va_longName_ln.setText(' '.join(str(sublist[1]["long_name"]).split()))
            self.va_longName_ln.setCursorPosition(0)
        else:
            self.va_longName_ln.setText("")
    except KeyError:
        self.va_longName_ln.setText("")
    try:
        if sublist[1]["units"] != "deleted":
            self.va_units_ln.setText(str(sublist[1]["units"]))
            self.va_units_ln.setCursorPosition(0)
        else:
            self.va_units_ln.setText("")
    except KeyError:
        self.va_units_ln.setText("")
    try:
        if sublist[1]["Category"] != "deleted":
            if isinstance(sublist[1]["Category"], list):
                category_string = ""
                for string in sublist[1]["Category"]:
                    category_string += string + ", "
                self.va_category_ln.setText(category_string[:-2])
            else:
                self.va_category_ln.setText(str(sublist[1]["Category"]))
            self.va_category_ln.setCursorPosition(0)
        else:
            self.va_category_ln.setText("")
    except KeyError:
        self.va_category_ln.setText("")
    try:
        self.va_fillValue_ln.setText(str(sublist[1]["_FillValue"]))
    except KeyError:
        try:
            self.va_fillValue_ln.setText(str(sublist[1]["missing_value"]))
        except KeyError:
            self.va_fillValue_ln.setText("")
    dimensions_str = ""
    i = 0
    
    for key, value in sublist[2].iteritems():
        if i == 0:
            dimensions_str = str(value) + " (" + key + ")"
        else: 
            dimensions_str = dimensions_str + " x " + str(value) + " (" + key + ")"
        i += 1
    self.va_dimensions_ln.setText(dimensions_str)
    try:
        self.va_egadsProcessor_ln.setPlainText(str(sublist[1]["Processor"]))
    except KeyError:
        self.va_egadsProcessor_ln.setPlainText("")
    logging.info("NetCDF Reading - variable information loaded")


def nasaames_reading(self, out_file_name):
    self.opened_file = egads.input.NasaAmes(out_file_name, 'r')  # @UndefinedVariable
    
    print dir(self.opened_file)
    
    
    '''self.list_of_variables = self.opened_file.get_variable_list("independant") + self.opened_file.get_variable_list("main")
    self.list_of_global_attributes = nasaames_global_attributes_formating(self, self.opened_file.get_attribute_list())



    self.list_of_dimensions = self.opened_file.get_dimension_list("independant") + self.opened_file.get_dimension_list("main")
    self.list_of_variables_and_attributes = []


    for index, var in enumerate(self.list_of_variables):
        dimension = self.list_of_dimensions[index]
        try:
            list_of_var_attributes = self.opened_file.get_attribute_list(str(var), "independant")
        except ValueError:
            list_of_var_attributes = self.opened_file.get_attribute_list(str(var), "main")
        list_of_var_attributes["var_name"] = str(var)
        
        if "units" not in list_of_var_attributes.keys():
            if "Units" in list_of_var_attributes.keys():
                list_of_var_attributes["units"] = list_of_var_attributes["Units"]
            elif "Unit" in list_of_var_attributes.keys():
                list_of_var_attributes["units"] = list_of_var_attributes["Unit"]
            elif "unit" in list_of_var_attributes.keys():
                list_of_var_attributes["units"] = list_of_var_attributes["unit"]
                
        if "long_name" not in list_of_var_attributes.keys():
            if "LongName" in list_of_var_attributes.keys():
                list_of_var_attributes["long_name"] = list_of_var_attributes["LongName"]
            elif "long name" in list_of_var_attributes.keys():
                list_of_var_attributes["long_name"] = list_of_var_attributes["long name"]
        
        egads_instance = self.opened_file.read_variable(var)
        self.list_of_variables_and_attributes.append([var, list_of_var_attributes, dimension, egads_instance])

    self.missing_global_attributes = []
    self.gm_title_ln.setText("")
    self.gm_institution_ln.setText("")
    self.gm_source_ln.setText("")
    self.gm_project_ln.setText("")
    self.gm_dateCreation_ln.setText("")
    self.gm_history_ln.setPlainText("")
    self.va_varName_ln.setText("")
    self.va_longName_ln.setText("")
    self.va_category_ln.setText("")
    self.va_units_ln.setText("")
    self.va_fillValue_ln.setText("")
    self.va_dimensions_ln.setText("")
    self.va_egadsProcessor_ln.setPlainText("")
    out_file_base, out_file_ext = ntpath.splitext(ntpath.basename(out_file_name))
    self.gm_filename_ln.setText(out_file_base + out_file_ext)
    
    try:
        self.gm_title_ln.setText(self.list_of_global_attributes["MNAME"])
        self.gm_title_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("title")
    try:
        self.gm_institution_ln.setText(self.list_of_global_attributes["ONAME"])
        self.gm_institution_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("institution")
    try:
        self.gm_source_ln.setText(self.list_of_global_attributes["SNAME"])
        self.gm_source_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("source")
    try:
        normal_comments = self.list_of_global_attributes["NCOM"]
        for comment in normal_comments:
            if "project:" in comment:
                self.gm_project_ln.setText(comment[8:].lstrip())
                break
        self.gm_project_ln.setCursorPosition(0)
    except KeyError:
        pass
    try:
        date_created = self.list_of_global_attributes["RDATE"]
        if isinstance(date_created , list):
            self.gm_dateCreation_ln.setText(str(date_created[0]) + "/" + str(date_created[1]) + "/" + str(date_created[2]))
        else:
            self.gm_dateCreation_ln.setText(str(date_created))
    except KeyError:
        pass
    try:
        normal_comments = self.list_of_global_attributes["NCOM"]
        history = ""
        for index, comment in enumerate(normal_comments):
            if "history:" in comment:
                history = comment[8:]
        self.gm_history_ln.setPlainText(history.lstrip())
    except KeyError:
        pass
    
    for var in self.list_of_variables:
        self.listWidget.addItem(var)
    self.listWidget.currentItemChanged.connect(lambda: nasaames_var_reading(self))
    QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), lambda: tab_change(self))
    all_buttons = self.findChildren(QToolButton)
    for widget in all_buttons:
        QObject.connect(widget, SIGNAL("clicked()"), lambda: modify_attribute_gui(self))'''
    
    
def nasaames_var_reading(self):
    self.va_button_1.setEnabled(True)
    self.va_button_2.setEnabled(True)
    self.va_button_3.setEnabled(True)
    self.va_button_4.setEnabled(True)
    self.actionAlgorithmsBar.setEnabled(True)
    self.actionDeleteVariableBar.setEnabled(True)
    self.actionVariableAttributesBar.setEnabled(True)
    self.actionPlotBar.setEnabled(True)
    self.actionDisplayBar.setEnabled(True)
    self.va_varName_ln.setText("")
    self.va_longName_ln.setText("")
    self.va_category_ln.setText("")
    self.va_units_ln.setText("")
    self.va_fillValue_ln.setText("")
    self.va_dimensions_ln.setText("")
    self.va_egadsProcessor_ln.setPlainText("")
    all_lines_edit = self.findChildren(QLineEdit)
    for widget in all_lines_edit:
        if "va_" in widget.objectName():
            widget.setEnabled(False)
    all_text_edit = self.findChildren(QPlainTextEdit)
    for widget in all_text_edit:
        if "va_" in widget.objectName():
            widget.setEnabled(False)
    all_buttons = self.findChildren(QToolButton)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    for widget in all_buttons:
        if "va_" in widget.objectName():
            widget.setIcon(icon)
    for sublist in self.list_of_variables_and_attributes:
        try:
            if sublist[1]["var_name"] == self.listWidget.currentItem().text():
                break
        except TypeError:
            pass
    

    self.va_varName_ln.setText(sublist[1]["var_name"])
    self.va_varName_ln.setCursorPosition(0)
    try:
        if sublist[1]["long_name"] != "deleted":
            self.va_longName_ln.setText(' '.join(str(sublist[1]["long_name"]).split()))
            self.va_longName_ln.setCursorPosition(0)
        else:
            self.va_longName_ln.setText("")
    except KeyError:
        self.va_longName_ln.setText("")
    try:
        if sublist[1]["units"] != "deleted":
            self.va_units_ln.setText(str(sublist[1]["units"]))
            self.va_units_ln.setCursorPosition(0)
        else:
            self.va_units_ln.setText("")
    except KeyError:
        self.va_units_ln.setText("")
    try:
        if sublist[1]["Category"] != "deleted":
            if isinstance(sublist[1]["Category"], list):
                category_string = ""
                for string in sublist[1]["Category"]:
                    category_string += string + ", "
                self.va_category_ln.setText(category_string[:-2])
            else:
                self.va_category_ln.setText(str(sublist[1]["Category"]))
            self.va_category_ln.setCursorPosition(0)
        else:
            self.va_category_ln.setText("")
    except KeyError:
        self.va_category_ln.setText("")
    try:
        self.va_fillValue_ln.setText(str(sublist[1]["_FillValue"]))
    except KeyError:
        try:
            self.va_fillValue_ln.setText(str(sublist[1]["missing_value"]))
        except KeyError:
            self.va_fillValue_ln.setText("")
    dimensions_str = ""
    i = 0
    
    for key, value in sublist[2].iteritems():
        if i == 0:
            dimensions_str = str(value) + " (" + key + ")"
        else: 
            dimensions_str = dimensions_str + " x " + str(value) + " (" + key + ")"
        i += 1
    self.va_dimensions_ln.setText(dimensions_str)
    try:
        self.va_egadsProcessor_ln.setPlainText(str(sublist[1]["Processor"]))
    except KeyError:
        self.va_egadsProcessor_ln.setPlainText("")


def nasaames_global_attributes_formating(self, attr_dict):
    
    #new_dict = {}
    #new_dict[""] = attr_dict[""]
    
    '''na_dictionary_keys = ("A", "AMISS", "ANAME", "ASCAL", "DATE", "DX",
                     "FFI", "IVOL", "LENA", "LENX", "MNAME", "NAUXC",
                     "NAUXV", "NCOM", "NIV", "NLHEAD", "NNCOML",
                     "NSCOML", "NV", "NVOL", "NVPM", "NX", "NXDEF",
                     "ONAME", "ORG", "RDATE", "SCOM", "SNAME", "V",
                     "VMISS", "VNAME", "VSCAL", "X", "XNAME")'''
    
    '''new_dict["authors"] = attr_dict["ONAME"]
    new_dict["institution"] = attr_dict["ORG"]
    new_dict["source"] = attr_dict["SNAME"]
    new_dict["project"] = attr_dict["MNAME"]
    new_dict["date_created"] = attr_dict["DATE"]
    
    try:
        normal_comments = attr_dict["NCOM"]
        comments_dict = {}
        read = 0
        for comment in normal_comments:
            if read == 0 :
                if "==== Normal Comments follow ====" in comment:
                    read = 1
                else:
                    pass
            else:
                if "==== Normal Comments end ====" in comment:
                    break
                else:
                    try:
                        ddot_index = comment.index(":")
                        comments_dict[comment[0:ddot_index]] = comment[ddot_index + 1:].strip()
                    except ValueError:
                        pass
        
        try:
            new_dict["title"] = comments_dict["title"]
        except KeyError:
            new_dict["title"] = ""
            
        try: 
            new_dict["history"] = comments_dict["history"]
        except KeyError:
            new_dict["history"] = ""
            
        try: 
            new_dict["references"] = comments_dict["references"]
        except KeyError:
            new_dict["references"] = ""
            
        try: 
            new_dict["comments"] = comments_dict["comments"]
        except KeyError:
            new_dict["comments"] = ""
    
    except KeyError:
        pass'''
    
    
    return attr_dict    
        
        
def new_var_reading(self):
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
    logging.info("NetCDF Reading - new variable information loaded")    
    

    