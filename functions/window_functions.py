# -*- coding: utf-8 -*-

import copy
import logging
import egads.algorithms as algorithms
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget, QCursor, QDialog, QFileDialog
from PyQt4.QtCore import QObject, SIGNAL
from ui.Ui_globalattributewindow import Ui_globalAttributeWindow
from ui.Ui_variableattributewindow import Ui_variableAttributeWindow
from ui.Ui_processwindow import Ui_processingWindow
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_displaywindow import Ui_displayWindow
from ui.Ui_plotwindow import Ui_plotWindow
from ui.Ui_logwindow import Ui_Changelog
from ui.Ui_aboutwindow import Ui_aboutWindow
from functions.gui_functions import clear_layout
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import numpy
import ntpath


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


class MyGlobalAttributes(QtGui.QDialog, Ui_globalAttributeWindow):
    def __init__(self, list_of_global_attributes):
        QWidget.__init__(self)
        self.setupUi(self)
        self.list_of_global_attributes = list_of_global_attributes.copy()
        self.gw_showButton.clicked.connect(self.other_attribute)
        self.gw_okButton.clicked.connect(self.close_window_save)
        self.gw_cancelButton.clicked.connect(self.close_window)
        self.gw_button_1.clicked.connect(self.add_attribute)
        self.populate_attribute()
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_spacer_1 = []
        self.add_list_spacer_2 = []
        self.add_list_del = []
        self.add_list_horizontal_layout = []
        self.attribute_num = 0
        self.attribute_display_size = {
                                       "comment":110,
                                       "date_created":110,
                                       "geospatial_lat_min":160,
                                       "geospatial_lat_max":160,
                                       "geospatial_lon_min":160,
                                       "geospatial_lon_max":160,
                                       "geospatial_vertical_min":210,
                                       "geospatial_vertical_max":210,
                                       "geospatial_vertical_positive":210,
                                       "geospatial_vertical_units":210,
                                       "history":110,
                                       "project":110,
                                       "references":110,
                                       "time_coverage_start":160,
                                       "time_coverage_end":160,
                                       "time_coverage_duration":210,
                                       }
        self.combobox_items = [
                               "comment",
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
                               "time_coverage_duration"
                               ]
        self.populate_combobox()
        logging.info("MyGlobalAttribute - window ready")


    def close_window(self):
        del(self.list_of_global_attributes)
        logging.info("MyGlobalAttribute - window closing")
        self.close()
        
        
    def close_window_save(self):
        try:
            logging.info("MyGlobalAttribute - saving global attributes")
            self.list_of_global_attributes["Conventions"] = str(self.gw_conventions_ln.text())
            self.list_of_global_attributes["title"] = str(self.gw_title_ln.text())
            self.list_of_global_attributes["institution"] = str(self.gw_institution_ln.text())
            self.list_of_global_attributes["source"] = str(self.gw_source_ln.text())
            try:
                for index, widget in enumerate(self.list_label):
                    try:
                        self.list_of_global_attributes[str(widget.text())] = float(self.list_line[index].text())
                    except ValueError:
                        self.list_of_global_attributes[str(widget.text())] = str(self.list_line[index].text())
            except AttributeError:
                pass
            for index, widget in enumerate (self.add_list_label):
                try:
                    self.list_of_global_attributes[widget.text()] = float(self.add_list_line[index].text())
                except ValueError:
                        self.list_of_global_attributes[str(widget.text())] = str(self.add_list_line[index].text())
            self.close()
        except Exception:
            logging.exception("MyGlobalAttribute - Exception")
        
    
    def add_attribute(self):
        try:
            logging.info("MyGlobalAttribute - adding attribute")
            selected_attribute =  self.gw_addAttribute_rl.currentText()
            logging.info("MyGlobalAttribute -               " + selected_attribute)
            if selected_attribute == "Make a choice...":
                return
            else:
                font = QtGui.QFont()
                font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
                font.setPointSize(12)
                font.setKerning(True)
                font.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
                icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.add_list_horizontal_layout.append(QtGui.QHBoxLayout())
                self.add_list_horizontal_layout[self.attribute_num].setObjectName(_fromUtf8("add_horizontal_layout_" + str(self.attribute_num)))
                self.add_list_spacer_1.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
                self.add_list_horizontal_layout[self.attribute_num].addItem(self.add_list_spacer_1[self.attribute_num])
                if selected_attribute == "Other...":
                    self.add_list_label.append(QtGui.QLineEdit())
                    self.add_list_label[self.attribute_num].setFrame(False)
                    self.add_list_label[self.attribute_num].setStyleSheet(_fromUtf8("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                    "\n"
                    "QLineEdit:disabled {background-color: rgb(200,200,200);}"))
                    self.add_list_label[self.attribute_num].setFont(font)
                    
                else:
                    self.add_list_label.append(QtGui.QLabel())
                    self.add_list_label[self.attribute_num].setText(selected_attribute)
                try:
                    size_value = self.attribute_display_size[str(selected_attribute)]
                except KeyError:
                    size_value = 150
                self.add_list_label[self.attribute_num].setMinimumSize(QtCore.QSize(size_value, 27))
                self.add_list_label[self.attribute_num].setMaximumSize(QtCore.QSize(size_value, 27))
                self.add_list_label[self.attribute_num].setObjectName(_fromUtf8("add_label_" + str(self.attribute_num)))
                self.add_list_horizontal_layout[self.attribute_num].addWidget(self.add_list_label[self.attribute_num])
                self.add_list_line.append(QtGui.QLineEdit())
                self.add_list_line[self.attribute_num].setEnabled(True)
                self.add_list_line[self.attribute_num].setMinimumSize(QtCore.QSize(400, 27))
                self.add_list_line[self.attribute_num].setMaximumSize(QtCore.QSize(400, 27))
                self.add_list_line[self.attribute_num].setPalette(palette)
                self.add_list_line[self.attribute_num].setFrame(False)
                self.add_list_line[self.attribute_num].setObjectName(_fromUtf8("add_line_" + str(self.attribute_num)))
                self.add_list_line[self.attribute_num].setFocus(True)
                self.add_list_line[self.attribute_num].setStyleSheet(_fromUtf8("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                "\n"
                "QLineEdit:disabled {background-color: rgb(200,200,200);}"))
                self.add_list_line[self.attribute_num].setFont(font)
                self.add_list_horizontal_layout[self.attribute_num].addWidget(self.add_list_line[self.attribute_num])
                self.add_list_del.append(QtGui.QToolButton())
                self.add_list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.attribute_num].setText(_fromUtf8(""))
                self.add_list_del[self.attribute_num].setIcon(icon)
                self.add_list_del[self.attribute_num].setIconSize(QtCore.QSize(27, 27))
                self.add_list_del[self.attribute_num].setAutoRaise(True)
                self.add_list_del[self.attribute_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
                "\n"
                "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                "\n"
                "QToolButton:flat {border: none;}"))
                self.add_list_del[self.attribute_num].setObjectName(_fromUtf8("add_list_del_" + str(self.attribute_num)))
                self.add_list_horizontal_layout[self.attribute_num].addWidget(self.add_list_del[self.attribute_num])
                self.add_list_spacer_2.append(QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
                self.add_list_horizontal_layout[self.attribute_num].addItem(self.add_list_spacer_2[self.attribute_num])
                self.vl_addAttribute.addLayout(self.add_list_horizontal_layout[self.attribute_num])
                self.add_list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                self.attribute_num += 1
                logging.info("MyGlobalAttribute - attribute added")
        except Exception:
            logging.exception("MyGlobalAttribute - Exception")
    
    
    def populate_attribute(self):
        logging.info("MyGlobalAttribute - populating attributes")
        try:
            try:
                self.gw_conventions_ln.setText(self.list_of_global_attributes["Conventions"])
                self.gw_title_ln.setCursorPosition(0)
            except KeyError:
                pass
            try:
                self.gw_title_ln.setText(self.list_of_global_attributes["title"])
                self.gw_title_ln.setCursorPosition(0)
            except KeyError:
                pass
            try:
                self.gw_institution_ln.setText(self.list_of_global_attributes["institution"])
                self.gw_institution_ln.setCursorPosition(0)
            except KeyError:
                pass
            try:
                self.gw_source_ln.setText(self.list_of_global_attributes["source"])
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
            self.list_spacer_1 = []
            self.list_spacer_2 = []
            self.list_horizontal_layout = []
            self.list_del = []
            self.attribute = 0
            for key, value in self.list_of_global_attributes.iteritems():
                if key != "Conventions" and key != "title" and key != "institution" and key != "source" and value != "deleted":
                    font = QtGui.QFont()
                    font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
                    font.setPointSize(12)
                    font.setKerning(True)
                    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
                    icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.list_horizontal_layout.append(QtGui.QHBoxLayout())
                    self.list_horizontal_layout[self.attribute].setObjectName(_fromUtf8("horizontal_layout_" + str(self.attribute)))
                    self.list_spacer_1.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
                    self.list_horizontal_layout[self.attribute].addItem(self.list_spacer_1[self.attribute])
                    self.list_label.append(QtGui.QLabel())
                    size_value = 150
                    self.list_label[self.attribute].setMinimumSize(QtCore.QSize(size_value, 27))
                    self.list_label[self.attribute].setMaximumSize(QtCore.QSize(size_value, 27))
                    self.list_label[self.attribute].setObjectName(_fromUtf8("label_" + str(self.attribute)))
                    self.list_label[self.attribute].setText(key)
                    self.list_label[self.attribute].setToolTip(key)
                    self.list_horizontal_layout[self.attribute].addWidget(self.list_label[self.attribute])
                    self.list_line.append(QtGui.QLineEdit())
                    self.list_line[self.attribute].setEnabled(True)
                    self.list_line[self.attribute].setMinimumSize(QtCore.QSize(400, 27))
                    self.list_line[self.attribute].setMaximumSize(QtCore.QSize(400, 27))
                    self.list_line[self.attribute].setPalette(palette)
                    self.list_line[self.attribute].setFrame(False)
                    self.list_line[self.attribute].setObjectName(_fromUtf8("line_" + str(self.attribute)))
                    self.list_line[self.attribute].setText(str(value))
                    self.list_line[self.attribute].setCursorPosition(0)
                    self.list_line[self.attribute].setFocus(True)
                    self.list_line[self.attribute].setStyleSheet(_fromUtf8("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                    "\n"
                    "QLineEdit:disabled {background-color: rgb(200,200,200);}"))
                    self.list_line[self.attribute].setFont(font)
                    self.list_horizontal_layout[self.attribute].addWidget(self.list_line[self.attribute])
                    self.list_del.append(QtGui.QToolButton())
                    self.list_del[self.attribute].setMinimumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute].setMaximumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute].setText(_fromUtf8(""))
                    self.list_del[self.attribute].setIcon(icon)
                    self.list_del[self.attribute].setIconSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute].setAutoRaise(True)
                    self.list_del[self.attribute].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
                    "\n"
                    "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                    "\n"
                    "QToolButton:flat {border: none;}"))
                    self.list_del[self.attribute].setObjectName(_fromUtf8("list_del_" + str(self.attribute)))
                    self.list_horizontal_layout[self.attribute].addWidget(self.list_del[self.attribute])
                    self.list_spacer_2.append(QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
                    self.list_horizontal_layout[self.attribute].addItem(self.list_spacer_2[self.attribute])
                    self.vl_otherAttribute.addLayout(self.list_horizontal_layout[self.attribute])
                    self.list_del[self.attribute].clicked.connect(self.delete_attribute)
                    self.attribute += 1
            if self.attribute != 0:
                self.gw_showButton.setText("Hide other attributes")
            else:
                logging.info("MyGlobalAttribute -               no more attribute")
                self.gw_showButton.setText("Hide other attributes")
                layout = QtGui.QHBoxLayout()
                layout.setObjectName(_fromUtf8("layout"))
                label = QtGui.QLabel()
                label.setMinimumSize(QtCore.QSize(110, 27))
                label.setMaximumSize(QtCore.QSize(110, 27))
                label.setObjectName(_fromUtf8("label"))
                label.setText("No more attribute")
                layout.addWidget(label)
                spacer = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                layout.addItem(spacer)
                self.vl_otherAttribute.addLayout(layout)
        elif self.gw_showButton.text() == "Hide other attributes":
            logging.info("MyGlobalAttribute -               hide")
            self.clear_layout(self.vl_otherAttribute)
            self.gw_showButton.setText("Show other attributes")
            
            
    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):   
            item = layout.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QtGui.QLayout):
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
            self.add_list_spacer_1.pop(index)
            self.add_list_spacer_2.pop(index)
            self.add_list_del[index].deleteLater()
            self.add_list_del.pop(index)
            self.add_list_horizontal_layout[index].deleteLater()
            self.add_list_horizontal_layout.pop(index)
            self.attribute_num -= 1
            if len(self.add_list_horizontal_layout) > 0:
                for i in range(0, len(self.add_list_horizontal_layout)):
                    self.add_list_horizontal_layout[i].setObjectName(_fromUtf8("add_horizontal_layout_" + str(i)))
                    self.add_list_line[i].setObjectName(_fromUtf8("add_line_" + str(i)))
                    self.add_list_label[i].setObjectName(_fromUtf8("add_label_" + str(i)))
                    self.add_list_del[i].setObjectName(_fromUtf8("add_list_del_" + str(i)))
        else:
            index = int(self.sender().objectName()[9:]) 
            logging.info("MyGlobalAttribute -                " + self.list_label[index].text())
            self.list_of_global_attributes[str(self.list_label[index].text())] = "deleted"
            self.list_label[index].deleteLater()
            self.list_label.pop(index)
            self.list_line[index].deleteLater()
            self.list_line.pop(index)
            self.list_spacer_1.pop(index)
            self.list_spacer_2.pop(index)
            self.list_del[index].deleteLater()
            self.list_del.pop(index)
            self.list_horizontal_layout[index].deleteLater()
            self.list_horizontal_layout.pop(index)
            self.attribute -= 1
            if len(self.list_horizontal_layout) > 0:
                for i in range(0, len(self.list_horizontal_layout)):
                    self.list_horizontal_layout[i].setObjectName(_fromUtf8("horizontal_layout_" + str(i)))
                    self.list_line[i].setObjectName(_fromUtf8("line_" + str(i)))
                    self.list_label[i].setObjectName(_fromUtf8("label_" + str(i)))
                    self.list_del[i].setObjectName(_fromUtf8("list_del_" + str(i)))
            
    
    def populate_combobox(self):
        self.gw_addAttribute_rl.addItem("Make a choice...")
        self.gw_addAttribute_rl.addItem("Other...")
        for item in self.combobox_items:
            try:
                self.list_of_global_attributes[item]
                if self.list_of_global_attributes[item] == "deleted":
                    self.gw_addAttribute_rl.addItem(item)
            except KeyError:
                self.gw_addAttribute_rl.addItem(item)


class MyVariableAttributes(QtGui.QDialog, Ui_variableAttributeWindow):
    def __init__(self, var, list_of_variables_and_attributes):
        QWidget.__init__(self)
        self.setupUi(self)
        self.variable = var
        self.setWindowTitle(self.variable)
        self.list_of_variables_and_attributes = copy.deepcopy(list_of_variables_and_attributes)
        self.vw_showButton.clicked.connect(self.other_attribute)
        self.vw_okButton.clicked.connect(self.close_window_save)
        self.vw_cancelButton.clicked.connect(self.close_window)
        self.vw_button_1.clicked.connect(self.add_attribute)
        self.combobox_items = [
                               "ancillary_variables",
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
                               "valid_range",
                               ]
        self.attribute_display_size = {
                                       "long_name":100,
                                       "standard_name":130,
                                       "valid_range":100,
                                       "valid_min":100,
                                       "valid_max":100,
                                       "SampledRate":100,
                                       "Category":100,
                                       "CalibrationCoefficients":170,
                                       "InstrumentLocation":170,
                                       "InstrumentCoordinates":180,
                                       "Dependencies":130,
                                       "Processor":100,
                                       "Comments":100,
                                       "ancillary_variables":150,
                                       "flag_values":100, 
                                       "flag_masks":100, 
                                       "flag_meaning":130,
                                       "long_name_<xx>":150,
                                       "missing_value":130,
                                       "fct_origin":100,
                                       }
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_spacer_1 = []
        self.add_list_spacer_2 = []
        self.add_list_del = []
        self.add_list_horizontal_layout = []
        self.add_attribute_num = 0
        for sublist in self.list_of_variables_and_attributes:
            if sublist[1]["var_name"] == self.variable:
                self.attributes = sublist[1]
                break
        self.populate_attribute()
        self.populate_combobox()
        logging.info("MyVariableAttribute - window ready")
        
        
    def close_window(self):
        logging.info("MyVariableAttribute - window closing")
        del(self.list_of_variables_and_attributes)
        self.close()
        
        
    def close_window_save(self):
        logging.info("MyVariableAttribute - saving variable attributes")
        self.attributes["units"] = str(self.vw_units_ln.text())
        try:
            for index, widget in enumerate(self.list_label):
                try:
                    self.attributes[str(widget.text())] = float(self.list_line[index].text())
                except ValueError:
                    self.attributes[str(widget.text())] = str(self.list_line[index].text())
        except AttributeError:
            pass
        for index, widget in enumerate (self.add_list_label):
            try:
                self.attributes[widget.text()] = float(self.add_list_line[index].text())
            except ValueError:
                    self.attributes[str(widget.text())] = str(self.add_list_line[index].text())
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
            self.list_spacer_1 = []
            self.list_spacer_2 = []
            self.list_horizontal_layout = []
            self.list_del = []
            self.attribute_num = 0
            for key, value in self.attributes.iteritems():
                if key != "units" and key != "_FillValue" and key != "var_name" and value != "deleted":
                    if isinstance(value, list):
                        value_string = ""
                        for string in value:
                            value_string += string + ", "
                        value = value_string[:-2]
                    font = QtGui.QFont()
                    font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
                    font.setPointSize(12)
                    font.setKerning(True)
                    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
                    icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.list_horizontal_layout.append(QtGui.QHBoxLayout())
                    self.list_horizontal_layout[self.attribute_num].setObjectName(_fromUtf8("horizontal_layout_" + str(self.attribute_num)))
                    self.list_spacer_1.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
                    self.list_horizontal_layout[self.attribute_num].addItem(self.list_spacer_1[self.attribute_num])
                    self.list_label.append(QtGui.QLabel()) 
                    size_value = 150
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(size_value, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(size_value, 27))
                    self.list_label[self.attribute_num].setObjectName(_fromUtf8("label_" + str(self.attribute_num)))
                    self.list_label[self.attribute_num].setText(key)
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_horizontal_layout[self.attribute_num].addWidget(self.list_label[self.attribute_num])
                    self.list_line.append(QtGui.QLineEdit())
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(400, 27))
                    self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(400, 27))
                    self.list_line[self.attribute_num].setPalette(palette)
                    self.list_line[self.attribute_num].setFrame(False)
                    self.list_line[self.attribute_num].setObjectName(_fromUtf8("line_" + str(self.attribute_num)))
                    self.list_line[self.attribute_num].setText(str(value))
                    self.list_line[self.attribute_num].setCursorPosition(0)
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setStyleSheet(_fromUtf8("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                    "\n"
                    "QLineEdit:disabled {background-color: rgb(200,200,200);}"))
                    self.list_line[self.attribute_num].setFont(font)
                    self.list_horizontal_layout[self.attribute_num].addWidget(self.list_line[self.attribute_num])
                    self.list_del.append(QtGui.QToolButton())
                    self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setText(_fromUtf8(""))
                    self.list_del[self.attribute_num].setIcon(icon)
                    self.list_del[self.attribute_num].setIconSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setAutoRaise(True)
                    self.list_del[self.attribute_num].setObjectName(_fromUtf8("list_del_" + str(self.attribute_num)))
                    self.list_del[self.attribute_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
                    "\n"
                    "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                    "\n"
                    "QToolButton:flat {border: none;}"))
                    self.list_horizontal_layout[self.attribute_num].addWidget(self.list_del[self.attribute_num])
                    self.list_spacer_2.append(QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
                    self.list_horizontal_layout[self.attribute_num].addItem(self.list_spacer_2[self.attribute_num])
                    self.vl_otherAttribute.addLayout(self.list_horizontal_layout[self.attribute_num])
                    self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                    
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setReadOnly(True)
                    
                    self.attribute_num += 1     
            if self.attribute_num != 0:
                self.vw_showButton.setText("Hide other attributes")
            else:
                logging.info("MyVariableAttribute -               no more attribute")
                self.vw_showButton.setText("Hide other attributes")
                layout = QtGui.QHBoxLayout()
                layout.setObjectName(_fromUtf8("layout"))   
                label = QtGui.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName(_fromUtf8("label"))
                label.setText("No more attribute")
                layout.addWidget(label)
                spacer = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                layout.addItem(spacer)
                self.vl_otherAttribute.addLayout(layout)
                
        elif self.vw_showButton.text() == "Hide other attributes":
            logging.info("MyVariableAttribute -               hide")
            self.list_label = []
            self.list_line = []
            self.list_spacer_1 = []
            self.list_spacer_2 = []
            self.list_horizontal_layout = []
            self.list_del = []
            self.attribute_num = 0
            self.clear_layout(self.vl_otherAttribute)
            self.vw_showButton.setText("Show other attributes")
    
    
    def add_attribute(self):
        logging.info("MyVariableAttribute - adding attribute")
        selected_attribute =  self.vw_addAttribute_rl.currentText()
        logging.info("MyVariableAttribute -               " + selected_attribute)
        if selected_attribute == "Make a choice...":
            return
        else:
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
            font.setPointSize(12)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.add_list_horizontal_layout.append(QtGui.QHBoxLayout())
            self.add_list_horizontal_layout[self.add_attribute_num].setObjectName(_fromUtf8("add_horizontal_layout_" + str(self.add_attribute_num)))
            self.add_list_spacer_1.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
            self.add_list_horizontal_layout[self.add_attribute_num].addItem(self.add_list_spacer_1[self.add_attribute_num])
            if selected_attribute == "Other..." or selected_attribute == "long_name_<xx>":
                self.add_list_label.append(QtGui.QLineEdit())
                self.add_list_label[self.add_attribute_num].setFrame(False)
                self.add_list_label[self.add_attribute_num].setStyleSheet(_fromUtf8("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
                "\n"
                "QLineEdit:disabled {background-color: rgb(200,200,200);}"))
                self.add_list_label[self.add_attribute_num].setFont(font)
                
                if selected_attribute == "long_name_<xx>":
                    self.add_list_label[self.add_attribute_num].setText("long_name_")
            else:
                self.add_list_label.append(QtGui.QLabel())
                self.add_list_label[self.add_attribute_num].setText(selected_attribute)
            try:
                size_value = self.attribute_display_size[str(selected_attribute)]
            except KeyError:
                size_value = 150
            self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(size_value, 27))
            self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(size_value, 27))
            self.add_list_label[self.add_attribute_num].setObjectName(_fromUtf8("add_label_" + str(self.add_attribute_num)))
            self.add_list_horizontal_layout[self.add_attribute_num].addWidget(self.add_list_label[self.add_attribute_num])
            self.add_list_line.append(QtGui.QLineEdit())
            self.add_list_line[self.add_attribute_num].setEnabled(True)
            self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(400, 27))
            self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(400, 27))
            self.add_list_line[self.add_attribute_num].setPalette(palette)
            self.add_list_line[self.add_attribute_num].setFrame(False)
            self.add_list_line[self.add_attribute_num].setObjectName(_fromUtf8("add_line_" + str(self.add_attribute_num)))
            self.add_list_line[self.add_attribute_num].setFocus(True)
            self.add_list_line[self.add_attribute_num].setStyleSheet(_fromUtf8("QLineEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
            "\n"
            "QLineEdit:disabled {background-color: rgb(200,200,200);}"))
            self.add_list_line[self.add_attribute_num].setFont(font)
            self.add_list_horizontal_layout[self.add_attribute_num].addWidget(self.add_list_line[self.add_attribute_num])
            self.add_list_del.append(QtGui.QToolButton())
            self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setText(_fromUtf8(""))
            self.add_list_del[self.add_attribute_num].setIcon(icon)
            self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setAutoRaise(True)
            self.add_list_del[self.add_attribute_num].setObjectName(_fromUtf8("add_list_del_" + str(self.add_attribute_num)))
            self.add_list_del[self.add_attribute_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
            "\n"
            "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
            "\n"
            "QToolButton:flat {border: none;}"))
            self.add_list_horizontal_layout[self.add_attribute_num].addWidget(self.add_list_del[self.add_attribute_num])
            self.add_list_spacer_2.append(QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
            self.add_list_horizontal_layout[self.add_attribute_num].addItem(self.add_list_spacer_2[self.add_attribute_num])
            self.vl_addAttribute.addLayout(self.add_list_horizontal_layout[self.add_attribute_num])
            self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
            self.add_attribute_num += 1
            logging.info("MyVariableAttribute - attribute added")
    
    
    def delete_attribute(self):
        logging.info("MyVariableAttribute - deleting attribute")
        if "add" in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            logging.info("MyVariableAttribute -               " + self.add_list_label[index].text())
            self.add_list_label[index].deleteLater()
            self.add_list_label.pop(index)
            self.add_list_line[index].deleteLater()
            self.add_list_line.pop(index)
            self.add_list_spacer_1.pop(index)
            self.add_list_spacer_2.pop(index)
            self.add_list_del[index].deleteLater()
            self.add_list_del.pop(index)
            self.add_list_horizontal_layout[index].deleteLater()
            self.add_list_horizontal_layout.pop(index)
            self.add_attribute_num -= 1
            if len(self.add_list_horizontal_layout) > 0:
                for i in range(0, len(self.add_list_horizontal_layout)):
                    self.add_list_horizontal_layout[i].setObjectName(_fromUtf8("add_horizontal_layout_" + str(i)))
                    self.add_list_line[i].setObjectName(_fromUtf8("add_line_" + str(i)))
                    self.add_list_label[i].setObjectName(_fromUtf8("add_label_" + str(i)))
                    self.add_list_del[i].setObjectName(_fromUtf8("add_list_del_" + str(i)))
        else:
            index = int(self.sender().objectName()[9:])
            logging.info("MyVariableAttribute -               " + self.list_label[index].text())
            self.attributes[str(self.list_label[index].text())] = "deleted"
            self.list_label[index].deleteLater()
            self.list_label.pop(index)
            self.list_line[index].deleteLater()
            self.list_line.pop(index)
            self.list_spacer_1.pop(index)
            self.list_spacer_2.pop(index)
            self.list_del[index].deleteLater()
            self.list_del.pop(index)
            self.list_horizontal_layout[index].deleteLater()
            self.list_horizontal_layout.pop(index)
            self.attribute_num -= 1
            if len(self.list_horizontal_layout) > 0:
                for i in range(0, len(self.list_horizontal_layout)):
                    self.list_horizontal_layout[i].setObjectName(_fromUtf8("horizontal_layout_" + str(i)))
                    self.list_line[i].setObjectName(_fromUtf8("line_" + str(i)))
                    self.list_label[i].setObjectName(_fromUtf8("label_" + str(i)))
                    self.list_del[i].setObjectName(_fromUtf8("list_del_" + str(i)))
        logging.info("MyVariableAttribute - attribute deleted")
        
    
    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):   
            item = layout.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QtGui.QLayout):
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
                
                
class MyProcessing(QtGui.QDialog, Ui_processingWindow):
    def __init__(self, list_of_algorithms, list_of_variables_and_attributes, list_of_new_variables_and_attributes):
        QWidget.__init__(self)
        QtGui.QFontDatabase.addApplicationFont("fonts/SourceSansPro-Regular.ttf")
        self.setupUi(self)
        self.hide_algorithm_information()
        self.list_of_algorithms = list_of_algorithms
        self.list_of_new_variables_and_attributes = list_of_new_variables_and_attributes
        self.list_of_variables_and_attributes = list_of_variables_and_attributes + list_of_new_variables_and_attributes
        self.algorithm = ""
        self.list_of_inputs = []
        self.list_of_outputs = []
        self.list_horizontal_layout_input = []
        self.list_vertical_layout_input = []
        self.list_vspacer_input = []
        self.list_hspacer_input = []
        self.list_hspacer2_input = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_button_input = []
        self.input_num = 0
        self.list_horizontal_layout_output = []
        self.list_vertical_layout_output = []
        self.list_vspacer_output = []
        self.list_hspacer_output = []
        self.list_hspacer2_output = []
        self.list_label_output = []
        self.list_lineedit_output = []
        self.list_button_output = []
        self.output_num = 0
        self.input_activate = 0
        self.output_activate = 0
        self.types_for_combobox = ["vector", "array","vector_optional","array_optional"]
        self.al_okButton.clicked.connect(self.close_window_save)
        self.al_cancelButton.clicked.connect(self.close_window)
        self.al_combobox_1.activated.connect(lambda: self.populate_combobox_2())
        self.al_combobox_2.activated.connect(lambda: self.prepare_layout())
        self.al_combobox_2.activated.connect(lambda: self.load_algorithm_information())
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
                    for sublist in self.list_of_variables_and_attributes:
                        if sublist[1]["var_name"] == item.currentText():
                            args.append(sublist[3])
                            if index == 0:
                                dimension_out = sublist[2]
                            break
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
                    for sublist in self.list_of_variables_and_attributes:
                        if sublist[1]["var_name"] == self.list_combobox_input[index].currentText():
                            metadata["_FillValue"] = sublist[1]["_FillValue"]
                            break
                    metadata["Processor"] = self.algorithm().metadata["Processor"]
                    metadata["long_name"] = output[index].metadata["long_name"]
                    metadata["DateProcessed"] = output[index].metadata["DateProcessed"]
                    metadata["Category"] = output[index].metadata["Category"]
                    
                    #dimensions = "None"
                    dimensions = dimension_out
                    
                    self.list_of_new_variables_and_attributes.append([str(self.list_lineedit_output[index].text()), metadata, dimensions, output[index]])
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
                for sublist in self.list_of_variables_and_attributes:
                    if sublist[1]["var_name"] == self.list_combobox_input[0].currentText():
                        metadata["_FillValue"] = sublist[1]["_FillValue"]
                        break
                metadata["Processor"] = self.algorithm().metadata["Processor"]
                metadata["long_name"] = output.metadata["long_name"]
                metadata["DateProcessed"] = output.metadata["DateProcessed"]
                metadata["Category"] = output.metadata["Category"]
                
                #dimensions = "None"
                dimensions = dimension_out
                
                self.list_of_new_variables_and_attributes.append([str(self.list_lineedit_output[0].text()), metadata, dimensions, output])
                self.close()
        except Exception:
            logging.exception("MyProcessingWindow - Exception")
        

    def populate_combobox_1(self):
        logging.info("MyProcessingWindow - populating combobox 1")
        self.al_combobox_1.addItem("Make a choice...")
        item_old = ["",""]
        for index, item in enumerate(self.list_of_algorithms):
            if index == 0:
                self.al_combobox_1.addItem(item[0].title())
            else:
                if item[0] != item_old[0]:
                    self.al_combobox_1.addItem(item[0].title())
            item_old = item
            
    
    def populate_combobox_2(self):
        logging.info("MyProcessingWindow - populating combobox 2")
        self.output_activate = 0
        self.input_activate = 0
        self.al_okButton.setEnabled(False)
        self.al_combobox_2.clear()
        if self.al_combobox_1.currentText() == "Make a choice...":
            self.al_combobox_2.setEnabled(False)
        else:
            self.al_combobox_2.setEnabled(True)
            self.al_combobox_2.addItem("Make a choice...")
            for item in self.list_of_algorithms:
                if item[0] == str(self.al_combobox_1.currentText()).lower():
                    self.al_combobox_2.addItem(item[1])
    
    
    def populate_input_output(self):
        if self.al_combobox_2.currentText() != "Make a choice..." and self.al_combobox_2.currentText() !="" :
            if self.tabWidget.currentIndex() == 1:
                logging.info("MyProcessingWindow - populating inputs")
                if len(self.list_vertical_layout_input) == 0:
                    for index, item in enumerate(self.algorithm().metadata["Inputs"]):
                        font = QtGui.QFont()
                        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
                        font.setPointSize(12)
                        font.setKerning(True)
                        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.list_vertical_layout_input.append(QtGui.QVBoxLayout())
                        self.list_vertical_layout_input[self.input_num].setObjectName(_fromUtf8("vertical_layout_input_"
                                                                                                   + str(self.input_num)))
                        self.list_horizontal_layout_input.append(QtGui.QHBoxLayout())
                        self.list_horizontal_layout_input[self.input_num].setObjectName(_fromUtf8("horizontal_layout_input_"
                                                                                                   + str(self.input_num)))
                        self.list_label_input.append(QtGui.QLabel())
                        self.list_label_input[self.input_num].setFont(font)
                        self.list_label_input[self.input_num].setText(item)
                        self.list_label_input[self.input_num].setMinimumSize(QtCore.QSize(100, 27))
                        self.list_label_input[self.input_num].setMaximumSize(QtCore.QSize(100, 27))
                        self.list_label_input[self.input_num].setObjectName(_fromUtf8("list_label_input_"
                                                                                       + str(self.input_num)))
                        self.list_horizontal_layout_input[self.input_num].addWidget(self.list_label_input[self.input_num])
                        if self.algorithm().metadata["InputTypes"][index] in self.types_for_combobox or self.algorithm().metadata["InputTypes"][index] == "time":
                            self.list_combobox_input.append(QtGui.QComboBox())
                            self.list_combobox_input[self.input_num].setEnabled(True)
                            self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                            self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                            self.list_combobox_input[self.input_num].setFrame(False)
                            self.list_combobox_input[self.input_num].setFont(font)
                            self.list_combobox_input[self.input_num].setStyleSheet(_fromUtf8("QComboBox {\n"
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
                            self.list_combobox_input[self.input_num].setObjectName(_fromUtf8("list_combobox_input_" 
                                                                                             + str(self.input_num)))
                            
                            self.list_combobox_input[self.input_num].addItem("Make a choice...")
                            for sublist in self.list_of_variables_and_attributes:
                                if self.algorithm().metadata["InputTypes"][index] in self.types_for_combobox:
                                    self.list_combobox_input[self.input_num].addItem(sublist[1]["var_name"])
                                else:
                                    if "time" in sublist[1]["var_name"]:
                                        self.list_combobox_input[self.input_num].addItem(sublist[1]["var_name"])
                            
                            QObject.connect(self.list_combobox_input[self.input_num], SIGNAL("activated(QString)"), 
                                            lambda: self.activate_save_button())
                            self.list_horizontal_layout_input[self.input_num].addWidget(self.list_combobox_input[self.input_num])
                        else:
                            
                            if "coeff.[" in self.algorithm().metadata["InputTypes"][index]:
                                line_edit_num = self.algorithm().metadata["InputTypes"][index][7:-1]
                                tmp = []
                                tmp_layout = QtGui.QHBoxLayout()
                                
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
                                    tmp.append(QtGui.QLineEdit())
                                    tmp[i].setEnabled(True)
                                    tmp[i].setFrame(False)
                                    tmp[i].setFont(font)
                                    tmp[i].setObjectName(_fromUtf8("multi_list_lineedit_input_" + str(i)))
                                    tmp[i].setMinimumSize(QtCore.QSize(size, 27))
                                    tmp[i].setMaximumSize(QtCore.QSize(size, 27))
                                    tmp[i].setStyleSheet(_fromUtf8("QLineEdit {\n"
                                    "    border-radius: 3px;\n"
                                    "    padding: 1px 4px 1px 4px;\n"
                                    "    background-color:  rgb(240, 240, 240);\n"
                                    "}\n"))
                                    QObject.connect(tmp[i], SIGNAL("textChanged(QString)"), lambda: self.activate_save_button())
                                    tmp_layout.addWidget(tmp[i])
                                    
                                    
                                self.list_combobox_input.append(tmp_layout)
                                self.list_horizontal_layout_input[self.input_num].addLayout(self.list_combobox_input[self.input_num])
                            
                            else:
                                self.list_combobox_input.append(QtGui.QLineEdit())
                                self.list_combobox_input[self.input_num].setEnabled(True)
                                self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                                self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                                self.list_combobox_input[self.input_num].setFrame(False)
                                self.list_combobox_input[self.input_num].setFont(font)
                                self.list_combobox_input[self.input_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
                                "    border-radius: 3px;\n"
                                "    padding: 1px 4px 1px 4px;\n"
                                "    background-color:  rgb(240, 240, 240);\n"
                                "}\n"))
                                
                                QObject.connect(self.list_combobox_input[self.input_num], SIGNAL("textChanged(QString)"), 
                                                lambda: self.activate_save_button())
                                if "optional" in self.algorithm().metadata["InputTypes"][index]:
                                    self.list_combobox_input[self.input_num].setObjectName(_fromUtf8("optional_list_lineedit_input_" 
                                                                                                     + str(self.input_num)))
                                else:
                                    self.list_combobox_input[self.input_num].setObjectName(_fromUtf8("list_lineedit_input_" 
                                                                                                     + str(self.input_num)))
                                self.list_horizontal_layout_input[self.input_num].addWidget(self.list_combobox_input[self.input_num])
                        
                        self.list_button_input.append(QtGui.QToolButton())
                        self.list_button_input[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
                        self.list_button_input[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
                        self.list_button_input[self.input_num].setText(_fromUtf8(""))
                        self.list_button_input[self.input_num].setIcon(icon)
                        self.list_button_input[self.input_num].setAutoRaise(True)
                        self.list_button_input[self.input_num].setIconSize(QtCore.QSize(27, 27))
                        self.list_button_input[self.input_num].setPopupMode(QtGui.QToolButton.InstantPopup)
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_button_input[self.input_num].setObjectName(_fromUtf8("optional_list_button_input_"
                                                                                           + str(self.input_num)))
                        else:
                            self.list_button_input[self.input_num].setObjectName(_fromUtf8("list_button_input_"
                                                                                           + str(self.input_num)))
                        self.list_hspacer2_input.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
                        self.list_horizontal_layout_input[self.input_num].addItem(self.list_hspacer2_input[self.input_num])
                        self.list_button_input[self.input_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
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
                        
                        
                        QObject.connect(self.list_button_input[self.input_num], SIGNAL("clicked()"), lambda: self.information_button())
                        
                        self.list_horizontal_layout_input[self.input_num].addWidget(self.list_button_input[self.input_num])
                        self.list_hspacer_input.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
                        self.list_horizontal_layout_input[self.input_num].addItem(self.list_hspacer_input[self.input_num])
                        self.list_vertical_layout_input[self.input_num].addLayout(self.list_horizontal_layout_input[self.input_num])
                        self.input_layout.addLayout(self.list_vertical_layout_input[self.input_num])
                        self.input_num += 1
            if self.tabWidget.currentIndex() == 2:
                if len(self.list_vertical_layout_output) == 0:
                    logging.info("MyProcessingWindow - populating outputs")
                    for item in self.algorithm().metadata["Outputs"]:
                        font = QtGui.QFont()
                        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
                        font.setPointSize(12)
                        font.setKerning(True)
                        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.list_vertical_layout_output.append(QtGui.QVBoxLayout())
                        self.list_vertical_layout_output[self.output_num].setObjectName(_fromUtf8("vertical_layout_output_"
                                                                                                   + str(self.output_num)))
                        self.list_horizontal_layout_output.append(QtGui.QHBoxLayout())
                        self.list_horizontal_layout_output[self.output_num].setObjectName(_fromUtf8("horizontal_layout_output_"
                                                                                                   + str(self.output_num)))
                        self.list_label_output.append(QtGui.QLabel())
                        self.list_label_output[self.output_num].setText(item)
                        self.list_label_output[self.output_num].setFont(font)
                        self.list_label_output[self.output_num].setMinimumSize(QtCore.QSize(100, 27))
                        self.list_label_output[self.output_num].setMaximumSize(QtCore.QSize(100, 27))
                        self.list_label_output[self.output_num].setObjectName(_fromUtf8("list_label_output_" + str(self.output_num)))
                        self.list_horizontal_layout_output[self.output_num].addWidget(self.list_label_output[self.output_num])
                        self.list_lineedit_output.append(QtGui.QLineEdit())
                        self.list_lineedit_output[self.output_num].setEnabled(True)
                        self.list_lineedit_output[self.output_num].setFont(font)
                        self.list_lineedit_output[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
                        self.list_lineedit_output[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
                        self.list_lineedit_output[self.output_num].setFrame(False)
                        self.list_lineedit_output[self.output_num].setStyleSheet("border-radius: 3px;"
                            + "padding: 1px 4px 1px 4px; background: rgb(240, 240, 240);")
                        self.list_lineedit_output[self.output_num].setObjectName(_fromUtf8("list_lineedit_output_" + str(self.output_num)))
                        QObject.connect(self.list_lineedit_output[self.output_num], SIGNAL("textChanged(QString)"), 
                                        lambda: self.activate_save_button())
                        self.list_horizontal_layout_output[self.output_num].addWidget(self.list_lineedit_output[self.output_num])
                        
                        self.list_button_output.append(QtGui.QToolButton())
                        self.list_button_output[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
                        self.list_button_output[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
                        self.list_button_output[self.output_num].setText(_fromUtf8(""))
                        self.list_button_output[self.output_num].setIcon(icon)
                        self.list_button_output[self.output_num].setAutoRaise(True)
                        self.list_button_output[self.output_num].setIconSize(QtCore.QSize(27, 27))
                        self.list_button_output[self.output_num].setPopupMode(QtGui.QToolButton.InstantPopup)
                        self.list_button_output[self.output_num].setObjectName(_fromUtf8("list_button_output_"
                                                                                       + str(self.output_num)))
                        self.list_hspacer2_output.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
                        self.list_horizontal_layout_output[self.output_num].addItem(self.list_hspacer2_output[self.output_num])
                        self.list_button_output[self.output_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
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
                        
                        QObject.connect(self.list_button_output[self.output_num], SIGNAL("clicked()"), lambda: self.information_button())
                        
                        self.list_horizontal_layout_output[self.output_num].addWidget(self.list_button_output[self.output_num])
                        
                        self.list_hspacer_output.append(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
                        self.list_horizontal_layout_output[self.output_num].addItem(self.list_hspacer_output[self.output_num])
                        self.list_vertical_layout_output[self.output_num].addLayout(self.list_horizontal_layout_output[self.output_num])
                        self.output_layout.addLayout(self.list_vertical_layout_output[self.output_num])
                        self.output_num += 1
    
    
    def prepare_layout(self):
        self.clear_layout(self.input_layout)
        self.clear_layout(self.output_layout)
        self.list_horizontal_layout_input = []
        self.list_vertical_layout_input = []
        self.list_vspacer_input = []
        self.list_hspacer_input = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_lineedit_input = []
        self.input_num = 0
        self.list_horizontal_layout_output = []
        self.list_vertical_layout_output = []
        self.list_vspacer_output = []
        self.list_hspacer_output = []
        self.list_label_output = []
        self.list_lineedit_output = []
        self.list_hspacer2_input = []
        self.list_button_input = []
        self.list_hspacer2_output = []
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
        self.al_label_6.hide()
        self.al_label_7.hide()
        self.al_textBrowser_1.hide()
        self.al_textBrowser_2.hide()
        
        
    def load_algorithm_information(self):
        logging.info("MyProcessingWindow - loading algorithm information")
        self.output_activate = 0
        self.input_activate = 0
        self.al_okButton.setEnabled(False)
        if self.al_combobox_2.currentText() != "Make a choice...":
            self.al_label_6.show()
            self.al_label_7.show()
            self.al_textBrowser_1.show()
            self.al_textBrowser_2.show()
            self.al_textBrowser_1.setPlainText("")
            self.al_textBrowser_2.setPlainText("")
            self.algorithm = getattr(getattr(algorithms, str(self.al_combobox_1.currentText()).lower()), 
                                         str(self.al_combobox_2.currentText()))
            try:
                description_string = '<p align="justify">' + str(self.algorithm().metadata["Description"]) + '</p>'
                self.al_textBrowser_2.setHtml(description_string)
            except KeyError:
                pass
            try:
                purpose_string = '<p align="justify">' + str(self.algorithm().metadata["Purpose"]) + '</p>'
                self.al_textBrowser_1.setHtml(purpose_string)
            except KeyError:
                pass

    
    def activate_save_button(self):
        if self.list_combobox_input:
            activate = 1
            for widget in self.list_combobox_input:
                try:
                    if widget.currentText == "Make a choice...":
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
            self.al_okButton.setEnabled(True)
        else:
            self.al_okButton.setEnabled(False)
    
    
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
        self.infoWindow.setGeometry(QCursor.pos().x() - 225, QCursor.pos().y() + 50, 450, 
                                    self.infoWindow.sizeHint().height())
        self.infoWindow.exec_()

 
class MyInfo(QtGui.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()


class MyDisplay(QtGui.QDialog, Ui_displayWindow):
    def __init__(self, variable):
        QWidget.__init__(self)
        QtGui.QFontDatabase.addApplicationFont("fonts/SourceSansPro-Regular.ttf")
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
                        self.dw_table.setItem(0, x, QtGui.QTableWidgetItem("NaN"))
                    else:
                        self.dw_table.setItem(0, x, QtGui.QTableWidgetItem(str(self.variable[3].value[x])))
                except KeyError:
                    try: 
                        if self.variable[3].value[x] == self.variable[1]["missing_value"]:
                            self.dw_table.setItem(0, x, QtGui.QTableWidgetItem("NaN"))
                        else:
                            self.dw_table.setItem(0, x, QtGui.QTableWidgetItem(str(self.variable[3].value[x])))
                    except KeyError:
                        self.dw_table.setItem(0, x, QtGui.QTableWidgetItem(str(self.variable[3].value[x])))
        else:
            for y in range(row):
                for x in range(col):
                    self.dw_table.setItem(y, x, QtGui.QTableWidgetItem(str(self.variable[3].value[y][x])))
        
        
class PlotWindow(QtGui.QDialog, Ui_plotWindow):
    def __init__(self, list_of_variables, list_of_new_variables):
        QDialog.__init__(self, parent=None)
        self.setupUi(self)
        self.setup_toolbar()
        self.list_of_variables_and_attributes = list_of_variables + list_of_new_variables
        self.figure = plt.figure(figsize=(20, 20))
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
        self.pw_figureOptions_vl_2 = []
        self.pw_figureOptions_hl_1 = []
        self.pw_figureOptions_hl_2 = []
        self.pw_figureOptions_hl_3 = []
        self.pw_figureOptions_hl_4 = []
        self.pw_figureOptions_hl_5 = []
        self.pw_figureOptions_hl_6 = []
        self.pw_figureOptions_hl_7 = []
        self.pw_figureOptions_hl_8 = []
        self.pw_figureOptions_hl_9 = []
        self.pw_figureOptions_hl_10 = []
        self.pw_figureOptions_hl_11 = []
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
        self.pw_figureOptions_bt_3 = []
        self.pw_figureOptions_bt_4 = []
        self.pw_figureOptions_bt_5 = []
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
        self.pw_plotOptions_rb_1 = []
        self.pw_plotOptions_rb_2 = []
        self.pw_plotOptions_bg_1 = []
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
        self.font_list = [font_manager.FontProperties(fname=fname).get_name() for fname in font_manager.get_fontconfig_fonts()]
        for index, item in enumerate(self.font_list):
            self.font_list[index] = str(item)
        self.font_list = sorted(set(self.font_list))
        self.default_font = font_manager.FontProperties(family=[str(matplotlib.rcParams['font.family'][0])]).get_name()
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
        self.toolBar = QtGui.QToolBar()
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.actionSave_as = QtGui.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save_as_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon1)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionSave_as.setEnabled(False)
        self.actionClose = QtGui.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/exit_icon_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionZoom = QtGui.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/zoom_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon4)
        self.actionZoom.setObjectName(_fromUtf8("actionZoom"))
        self.actionZoom.setEnabled(False)
        self.actionPan = QtGui.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pan_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon5)
        self.actionPan.setObjectName(_fromUtf8("actionPan"))
        self.actionPan.setEnabled(False)
        self.actionOrigin = QtGui.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/origin_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOrigin.setIcon(icon6)
        self.actionOrigin.setObjectName(_fromUtf8("actionOrigin"))
        self.actionOrigin.setEnabled(False)
        self.actionClear = QtGui.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon6)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionClear.setEnabled(False)
        self.actionSeparator1 = QtGui.QAction(self)
        self.actionSeparator1.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icons/separator_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSeparator1.setIcon(icon7)
        self.actionSeparator1.setObjectName(_fromUtf8("actionSeparator1"))
        self.actionSeparator2 = QtGui.QAction(self)
        self.actionSeparator2.setEnabled(False)
        self.actionSeparator2.setIcon(icon7)
        self.actionSeparator2.setObjectName(_fromUtf8("actionSeparator2"))
        self.actionSeparator3 = QtGui.QAction(self)
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
    
    
    def plot_type(self):
        if self.sender().objectName() == "pw_single_rd":
            if self.plot_type_str == "" or self.plot_type_str == "multiple":
                clear_layout(self, self.pw_graphType_la)
                self.plot_clear()
                self.plot_type_str = "single"
                self.setup_type_single()
                self.populate_comboboxes(self.pw_xvariable_rl)
                self.populate_comboboxes(self.pw_yvariable_rl)
                self.pw_addSingle_bt.clicked.connect(lambda: self.plot_variable_single())
        elif self.sender().objectName() == "pw_multiple_rd":
            if self.plot_type_str == "" or self.plot_type_str == "single":
                clear_layout(self, self.pw_graphType_la)
                self.plot_clear()
                self.plot_type_str = "multiple"
                self.setup_type_multiple()
    
    
    def populate_comboboxes(self, combobox):
        logging.info("PlotWindow - populating combobox")
        combobox.addItem("Make a choice...")
        for sublist in self.list_of_variables_and_attributes:
            combobox.addItem(sublist[1]["var_name"])
    
    
    def populate_comboboxes_regular(self, combobox, list):  # @ReservedAssignment
        logging.info("PlotWindow - populating combobox")
        for item in list:
            combobox.addItem(item)
            
    
    def plot_variable_single(self):
        if self.pw_xvariable_rl.currentText() != "Make a choice..." and self.pw_yvariable_rl.currentText() != "Make a choice...":
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
            for sublist in self.list_of_variables_and_attributes:
                if sublist[1]["var_name"] == self.pw_xvariable_rl.currentText():
                    logging.info("PlotWindow -               x: " + self.pw_xvariable_rl.currentText())
                    xvalue = copy.deepcopy(sublist[3].value)
                    xunits = copy.deepcopy(sublist[1]["units"])
                    #xname = copy.deepcopy(sublist[1]["var_name"])
                    try:
                        xnan = sublist[1]["_FillValue"]
                    except KeyError:
                        pass 
                    break
            for sublist in self.list_of_variables_and_attributes:
                if sublist[1]["var_name"] == self.pw_yvariable_rl.currentText():
                    logging.info("PlotWindow -               y: " + self.pw_yvariable_rl.currentText())
                    yvalue = copy.deepcopy(sublist[3].value)
                    yunits = copy.deepcopy(sublist[1]["units"])
                    yname = copy.deepcopy(sublist[1]["var_name"])
                    try:
                        ynan = sublist[1]["_FillValue"]
                    except KeyError:
                        pass 
                    break
            xvalue[xvalue == xnan] = numpy.nan
            yvalue[yvalue == ynan] = numpy.nan
            plt.plot(xvalue, yvalue, label = yname)
            plt.ylabel(yunits)
            plt.xlabel(xunits)
            lprop = {
                    "family":self.default_font,
                    "size":"12"
                    }
            leg = plt.legend(prop=lprop)
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
                plt.gca().legend().set_visible(False)
            self.canvas.draw()
            if self.option_num == 0:
                self.figure_options()
            self.plot_options()
 
            
    def add_variable_single(self):
        logging.info("PlotWindow - adding variable")
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.list_horLayout.append(QtGui.QHBoxLayout())
        self.list_horLayout[self.variable_num].setObjectName(_fromUtf8("list_horLayout_" + str(self.variable_num)))
        self.list_horLayout[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.list_label.append(QtGui.QLabel())
        self.list_label[self.variable_num].setFont(font)
        self.list_label[self.variable_num].setText(self.pw_yvariable_rl.currentText())
        logging.info("PlotWindow -                " + self.pw_yvariable_rl.currentText())
        self.list_label[self.variable_num].setToolTip(self.pw_yvariable_rl.currentText())
        self.list_label[self.variable_num].setMinimumSize(QtCore.QSize(150, 27))
        self.list_label[self.variable_num].setMaximumSize(QtCore.QSize(250, 27))
        self.list_label[self.variable_num].setObjectName(_fromUtf8("list_label_" + str(self.variable_num)))
        self.list_horLayout[self.variable_num].addWidget(self.list_label[self.variable_num])
        self.list_button.append(QtGui.QToolButton())
        self.list_button[self.variable_num].setMinimumSize(QtCore.QSize(27, 27))
        self.list_button[self.variable_num].setMaximumSize(QtCore.QSize(27, 27))
        self.list_button[self.variable_num].setText(_fromUtf8(""))
        self.list_button[self.variable_num].setIcon(icon)
        self.list_button[self.variable_num].setIconSize(QtCore.QSize(27, 27))
        self.list_button[self.variable_num].setPopupMode(QtGui.QToolButton.InstantPopup)
        self.list_button[self.variable_num].setAutoRaise(True)
        self.list_button[self.variable_num].setObjectName(_fromUtf8("list_button_" + str(self.variable_num)))
        self.list_button[self.variable_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "QToolButton:flat {\n"
        "    border: none; /* no border for a flat push button */\n"
        "}"))
        self.list_button[self.variable_num].clicked.connect(lambda: self.del_variable_single())
        self.list_horLayout[self.variable_num].addWidget(self.list_button[self.variable_num])
        self.list_horLayout[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_singleVerlayout_1.addLayout(self.list_horLayout[self.variable_num])
        self.variable_num += 1
        logging.info("PlotWindow - variable added")
        
        
    def del_variable_single(self, index = None):
        logging.info("PlotWindow - deleting variable")
        if index == None:
            index = int(self.sender().objectName()[12:])
        logging.info("PlotWindow -               " + self.list_label[index].text())
        plt.axes().lines[index].remove()
        lprop = {
                "family":self.default_font,
                "size":"12"
                }
        leg = plt.legend(prop=lprop)
        leg.draggable()
        if not self.legend_visibility:
            plt.gca().legend().set_visible(False)
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
                self.list_horLayout[i].setObjectName(_fromUtf8("list_horLayout_" + str(i)))
                self.list_button[i].setObjectName(_fromUtf8("list_button_" + str(i)))
                self.list_label[i].setObjectName(_fromUtf8("list_label_" + str(i)))
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
        logging.info("PlotWindow - deleting figure options")
        if index < 1:
            self.pw_figureOptions_vl_2[index].deleteLater()
            self.pw_figureOptions_vl_2.pop(index)
            self.pw_figureOptions_hl_9[index].deleteLater()
            self.pw_figureOptions_hl_9.pop(index)
            self.pw_figureOptions_hl_10[index].deleteLater()
            self.pw_figureOptions_hl_10.pop(index)
            self.pw_figureOptions_hl_11[index].deleteLater()
            self.pw_figureOptions_hl_11.pop(index)
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
        self.pw_figureOptions_hl_1[index].deleteLater()
        self.pw_figureOptions_hl_1.pop(index)
        self.pw_figureOptions_hl_2[index].deleteLater()
        self.pw_figureOptions_hl_2.pop(index)
        self.pw_figureOptions_hl_3[index].deleteLater()
        self.pw_figureOptions_hl_3.pop(index)
        self.pw_figureOptions_hl_4[index].deleteLater()
        self.pw_figureOptions_hl_4.pop(index)
        self.pw_figureOptions_hl_5[index].deleteLater()
        self.pw_figureOptions_hl_5.pop(index)
        self.pw_figureOptions_hl_6[index].deleteLater()
        self.pw_figureOptions_hl_6.pop(index)
        self.pw_figureOptions_hl_7[index].deleteLater()
        self.pw_figureOptions_hl_7.pop(index)
        self.pw_figureOptions_hl_8[index].deleteLater()
        self.pw_figureOptions_hl_8.pop(index)
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
        self.pw_figureOptions_bt_3[index].deleteLater()
        self.pw_figureOptions_bt_3.pop(index)
        self.pw_figureOptions_bt_4[index].deleteLater()
        self.pw_figureOptions_bt_4.pop(index)
        self.pw_figureOptions_bt_5[index].deleteLater()
        self.pw_figureOptions_bt_5.pop(index)
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
        
        
    def del_plot_options(self, index):
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
        
    
    def plot_pan(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/zoom_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon)
        self.actionZoom.setObjectName("actionZoom")
        if "activated" in self.actionPan.objectName():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pan_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPan.setIcon(icon)
            self.actionPan.setObjectName("actionPan")
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pan_icon_activated.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPan.setIcon(icon)
            self.actionPan.setObjectName("activated_actionPan")
        self.navigation_toolbar.pan()
        
        
    def plot_zoom(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pan_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon)
        self.actionPan.setObjectName("actionPan")
        if "activated" in self.actionZoom.objectName():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/zoom_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionZoom.setIcon(icon)
            self.actionZoom.setObjectName("actionZoom")
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/zoom_icon_activated.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionZoom.setIcon(icon)
            self.actionZoom.setObjectName("activated_actionZoom")
        self.navigation_toolbar.zoom()
        
        
    def plot_home(self):
        self.navigation_toolbar.home()
    
    
    def plot_save(self):
        save_file_name, save_file_ext = self.get_file_name()
        if not save_file_name:
            return
        out_file_name, out_file_ext = ntpath.splitext(ntpath.basename(save_file_name))  # @UnusedVariable
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
        
    
    def plot_clear(self):
        if self.plot_type_str == "single":
            for i in reversed(range(0, len(self.list_horLayout))):
                self.del_variable_single(i)
            plt.clf()
            self.canvas.draw()
        elif self.plot_type_str == "multiple":
            for i in reversed(range(0, len(self.subplot_data))):
                self.del_subplot(i)
            plt.clf()
            self.canvas.draw()
    
    
    def setup_type_single(self):
        self.legend_visibility = True
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/plus_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_singleHorlayout_1 = QtGui.QHBoxLayout()
        self.pw_singleHorlayout_1.setObjectName(_fromUtf8("pw_singleHorlayout_1"))
        self.pw_singleLabel_1 = QtGui.QLabel()
        self.pw_singleLabel_1.setMinimumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_1.setMaximumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_1.setFont(font)
        self.pw_singleLabel_1.setText("Please choose a variable for the X axis")
        self.pw_singleLabel_1.setObjectName(_fromUtf8("pw_singleLabel_1"))
        self.pw_singleHorlayout_1.addWidget(self.pw_singleLabel_1)
        self.pw_singleHorlayout_1.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_1)
        self.pw_singleHorlayout_2 = QtGui.QHBoxLayout()
        self.pw_singleHorlayout_2.setObjectName(_fromUtf8("pw_singleHorlayout_2"))
        self.pw_singleHorlayout_2.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_xvariable_rl = QtGui.QComboBox()
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
        self.pw_singleHorlayout_2.addWidget(self.pw_xvariable_rl)
        self.pw_singleHorlayout_2.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_2)
        self.pw_graphType_la.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
        self.pw_singleHorlayout_3 = QtGui.QHBoxLayout()
        self.pw_singleHorlayout_3.setObjectName(_fromUtf8("pw_singleHorlayout_3"))
        self.pw_singleLabel_2 = QtGui.QLabel()
        self.pw_singleLabel_2.setMinimumSize(QtCore.QSize(310, 60))
        self.pw_singleLabel_2.setMaximumSize(QtCore.QSize(310, 60))
        self.pw_singleLabel_2.setFont(font)
        self.pw_singleLabel_2.setText("Please choose one variable in the following list for the Y axis and click on the '+' button to add it to the plot")
        self.pw_singleLabel_2.setWordWrap(True)
        self.pw_singleLabel_2.setObjectName(_fromUtf8("pw_singleLabel_2"))
        self.pw_singleHorlayout_3.addWidget(self.pw_singleLabel_2)
        self.pw_singleHorlayout_3.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_3)
        self.pw_singleHorlayout_4 = QtGui.QHBoxLayout()
        self.pw_singleHorlayout_4.setObjectName(_fromUtf8("pw_singleHorlayout_4"))
        self.pw_singleHorlayout_4.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_yvariable_rl = QtGui.QComboBox()
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
        self.pw_singleHorlayout_4.addWidget(self.pw_yvariable_rl)
        self.pw_addSingle_bt = QtGui.QToolButton()
        self.pw_addSingle_bt.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_addSingle_bt.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_addSingle_bt.setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_addSingle_bt.setText(_fromUtf8(""))
        self.pw_addSingle_bt.setIcon(icon)
        self.pw_addSingle_bt.setIconSize(QtCore.QSize(27, 27))
        self.pw_addSingle_bt.setAutoRaise(True)
        self.pw_addSingle_bt.setObjectName(_fromUtf8("pw_addSingle_bt"))
        self.pw_singleHorlayout_4.addWidget(self.pw_addSingle_bt)
        self.pw_singleHorlayout_4.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_4)
        self.pw_graphType_la.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
        self.pw_singleHorlayout_5 = QtGui.QHBoxLayout()
        self.pw_singleHorlayout_5.setObjectName(_fromUtf8("self.pw_singleHorlayout_5"))
        self.pw_singleLabel_3 = QtGui.QLabel()
        self.pw_singleLabel_3.setMinimumSize(QtCore.QSize(250, 27))
        self.pw_singleLabel_3.setMaximumSize(QtCore.QSize(250, 27))
        font.setBold(True)
        font.setWeight(75)
        self.pw_singleLabel_3.setFont(font)
        self.pw_singleLabel_3.setText("List of plotted variables:")
        self.pw_singleLabel_3.setObjectName(_fromUtf8("pw_singleLabel_3"))
        self.pw_singleLabel_3.hide()
        self.pw_singleHorlayout_5.addWidget(self.pw_singleLabel_3)
        self.pw_singleHorlayout_5.addItem(QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_singleHorlayout_5)
        self.pw_singleVerlayout_1 = QtGui.QVBoxLayout()
        self.pw_singleVerlayout_1.setObjectName(_fromUtf8("pw_singleVerlayout_1"))
        self.pw_graphType_la.addLayout(self.pw_singleVerlayout_1)
        
        
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
        self.mult_line_option = []
        self.legend_visibility = []
        self.subplot_data = []
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/plus_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_multipleHorlayout_1 = QtGui.QHBoxLayout()
        self.pw_multipleHorlayout_1.setObjectName(_fromUtf8("pw_multipleHorlayout_1"))
        self.pw_multipleLabel_1 = QtGui.QLabel()
        self.pw_multipleLabel_1.setMinimumSize(QtCore.QSize(300, 27))
        self.pw_multipleLabel_1.setMaximumSize(QtCore.QSize(300, 27))
        self.pw_multipleLabel_1.setFont(font)
        self.pw_multipleLabel_1.setText("Please press the '+' to add a subplot")
        self.pw_multipleLabel_1.setObjectName(_fromUtf8("pw_multipleLabel_1"))
        self.pw_multipleHorlayout_1.addWidget(self.pw_multipleLabel_1)
        self.pw_addMultiple_bt = QtGui.QToolButton()
        self.pw_addMultiple_bt.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_addMultiple_bt.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_addMultiple_bt.setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_addMultiple_bt.setText(_fromUtf8(""))
        self.pw_addMultiple_bt.setIcon(icon)
        self.pw_addMultiple_bt.setIconSize(QtCore.QSize(27, 27))
        self.pw_addMultiple_bt.setAutoRaise(True)
        self.pw_addMultiple_bt.setObjectName(_fromUtf8("pw_addMultiple_bt"))
        self.pw_multipleHorlayout_1.addWidget(self.pw_addMultiple_bt)
        self.pw_multipleHorlayout_1.addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_graphType_la.addLayout(self.pw_multipleHorlayout_1)
        self.pw_addMultiple_bt.clicked.connect(lambda: self.add_subplot_selection())
        
    
    def add_subplot_selection(self):
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font.setBold(True)
        font.setWeight(75)
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font2.setPointSize(12)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_multipleVerlayout_2.append(QtGui.QVBoxLayout())
        self.pw_multipleVerlayout_2[self.multiple_num].setObjectName(_fromUtf8("pw_multipleVerlayout_2_" + str(self.multiple_num)))
        self.pw_multipleVerlayout_2[self.multiple_num].addItem(QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
        self.pw_multipleVerlayout_1.append(QtGui.QVBoxLayout())
        self.pw_multipleVerlayout_1[self.multiple_num].setObjectName(_fromUtf8("pw_multipleVerlayout_1_" + str(self.multiple_num)))
        self.pw_multipleHorlayout_2.append(QtGui.QHBoxLayout())
        self.pw_multipleHorlayout_2[self.multiple_num].setObjectName(_fromUtf8("pw_multipleHorlayout_2_" + str(self.multiple_num)))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_2[self.multiple_num])
        self.pw_singleLabel_1.append(QtGui.QLabel())
        self.pw_singleLabel_1[self.multiple_num].setMinimumSize(QtCore.QSize(150, 27))
        self.pw_singleLabel_1[self.multiple_num].setMaximumSize(QtCore.QSize(150, 27))
        self.pw_singleLabel_1[self.multiple_num].setFont(font)
        self.pw_singleLabel_1[self.multiple_num].setText("Subplot " + str(self.multiple_num + 1))
        self.pw_singleLabel_1[self.multiple_num].setObjectName(_fromUtf8("pw_singleLabel_1_" + str(self.multiple_num)))
        self.pw_multipleHorlayout_2[self.multiple_num].addWidget(self.pw_singleLabel_1[self.multiple_num])
        self.pw_multipleHorlayout_2[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_3.append(QtGui.QHBoxLayout())
        self.pw_multipleHorlayout_3[self.multiple_num].setObjectName(_fromUtf8("pw_multipleHorlayout_3_" + str(self.multiple_num)))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_3[self.multiple_num])
        self.pw_singleLabel_2.append(QtGui.QLabel())
        self.pw_singleLabel_2[self.multiple_num].setMinimumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_2[self.multiple_num].setMaximumSize(QtCore.QSize(300, 27))
        self.pw_singleLabel_2[self.multiple_num].setFont(font2)
        self.pw_singleLabel_2[self.multiple_num].setText("Please choose a variable for the X axis")
        self.pw_singleLabel_2[self.multiple_num].setObjectName(_fromUtf8("pw_singleLabel_2_" + str(self.multiple_num)))
        self.pw_multipleHorlayout_3[self.multiple_num].addWidget(self.pw_singleLabel_2[self.multiple_num])
        self.pw_multipleHorlayout_3[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_4.append(QtGui.QHBoxLayout())
        self.pw_multipleHorlayout_4[self.multiple_num].setObjectName(_fromUtf8("pw_multipleHorlayout_4_" + str(self.multiple_num)))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_4[self.multiple_num])
        self.pw_multipleHorlayout_4[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_multipleXvariable_rl.append(QtGui.QComboBox())
        self.pw_multipleXvariable_rl[self.multiple_num].setFont(font2)
        self.pw_multipleXvariable_rl[self.multiple_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_multipleXvariable_rl[self.multiple_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_multipleXvariable_rl[self.multiple_num].setStyleSheet(_fromUtf8("QComboBox {\n"
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
        self.pw_multipleXvariable_rl[self.multiple_num].setObjectName(_fromUtf8("pw_multipleXvariable_rl_" + str(self.multiple_num)))
        self.pw_multipleHorlayout_4[self.multiple_num].addWidget(self.pw_multipleXvariable_rl[self.multiple_num])
        self.pw_multipleHorlayout_4[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_5.append(QtGui.QHBoxLayout())
        self.pw_multipleHorlayout_5[self.multiple_num].setObjectName(_fromUtf8("pw_multipleHorlayout_5_" + str(self.multiple_num)))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_5[self.multiple_num])
        self.pw_singleLabel_3.append(QtGui.QLabel())
        self.pw_singleLabel_3[self.multiple_num].setMinimumSize(QtCore.QSize(310, 27))
        self.pw_singleLabel_3[self.multiple_num].setMaximumSize(QtCore.QSize(310, 27))
        self.pw_singleLabel_3[self.multiple_num].setFont(font2)
        self.pw_singleLabel_3[self.multiple_num].setText("Please choose a variable for the Y axis")
        self.pw_singleLabel_3[self.multiple_num].setObjectName(_fromUtf8("pw_singleLabel_3_" + str(self.multiple_num)))
        self.pw_singleLabel_3[self.multiple_num].setWordWrap(True)
        self.pw_multipleHorlayout_5[self.multiple_num].addWidget(self.pw_singleLabel_3[self.multiple_num])
        self.pw_multipleHorlayout_5[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_6.append(QtGui.QHBoxLayout())
        self.pw_multipleHorlayout_6[self.multiple_num].setObjectName(_fromUtf8("pw_multipleHorlayout_6_" + str(self.multiple_num)))
        self.pw_multipleVerlayout_1[self.multiple_num].addLayout(self.pw_multipleHorlayout_6[self.multiple_num])
        self.pw_multipleHorlayout_6[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_multipleYvariable_rl.append(QtGui.QComboBox())
        self.pw_multipleYvariable_rl[self.multiple_num].setFont(font2)
        self.pw_multipleYvariable_rl[self.multiple_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_multipleYvariable_rl[self.multiple_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_multipleYvariable_rl[self.multiple_num].setStyleSheet(_fromUtf8("QComboBox {\n"
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
        self.pw_multipleYvariable_rl[self.multiple_num].setObjectName(_fromUtf8("pw_multipleYvariable_rl_" + str(self.multiple_num)))
        self.pw_multipleHorlayout_6[self.multiple_num].addWidget(self.pw_multipleYvariable_rl[self.multiple_num])
        self.pw_multipleHorlayout_6[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_multipleHorlayout_7.append(QtGui.QHBoxLayout())
        self.pw_multipleHorlayout_7[self.multiple_num].setObjectName(_fromUtf8("pw_multipleHorlayout_7_" + str(self.multiple_num)))
        self.pw_multipleDel_bt.append(QtGui.QToolButton())
        self.pw_multipleDel_bt[self.multiple_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_multipleDel_bt[self.multiple_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_multipleDel_bt[self.multiple_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_multipleDel_bt[self.multiple_num].setText(_fromUtf8(""))
        self.pw_multipleDel_bt[self.multiple_num].setIcon(icon)
        self.pw_multipleDel_bt[self.multiple_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_multipleDel_bt[self.multiple_num].setAutoRaise(True)
        self.pw_multipleDel_bt[self.multiple_num].setObjectName(_fromUtf8("pw_multipleDel_bt_" + str(self.multiple_num)))
        self.pw_multipleHorlayout_7[self.multiple_num].addWidget(self.pw_multipleDel_bt[self.multiple_num])
        self.pw_multipleLine_1.append(QtGui.QFrame())
        self.pw_multipleLine_1[self.multiple_num].setFrameShape(QtGui.QFrame.VLine)
        self.pw_multipleLine_1[self.multiple_num].setFrameShadow(QtGui.QFrame.Sunken)
        self.pw_multipleLine_1[self.multiple_num].setObjectName(_fromUtf8("pw_multipleLine_1_" + str(self.multiple_num)))
        self.pw_multipleHorlayout_7[self.multiple_num].addWidget(self.pw_multipleLine_1[self.multiple_num])
        self.pw_multipleHorlayout_7[self.multiple_num].addLayout(self.pw_multipleVerlayout_1[self.multiple_num])
        self.pw_multipleHorlayout_7[self.multiple_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_multipleVerlayout_2[self.multiple_num].addLayout(self.pw_multipleHorlayout_7[self.multiple_num])
        self.pw_graphType_la.addLayout(self.pw_multipleVerlayout_2[self.multiple_num])
        self.populate_comboboxes(self.pw_multipleXvariable_rl[self.multiple_num])
        self.populate_comboboxes(self.pw_multipleYvariable_rl[self.multiple_num])
        self.pw_multipleXvariable_rl[self.multiple_num].activated.connect(lambda: self.add_subplot_plot())
        self.pw_multipleYvariable_rl[self.multiple_num].activated.connect(lambda: self.add_subplot_plot())
        self.pw_multipleDel_bt[self.multiple_num].clicked.connect(lambda: self.del_subplot())
        self.subplot_data.append([])
        self.multiple_num += 1
        
        
    def add_subplot_plot(self):
        index = int(self.sender().objectName()[24:])
        if "X" in self.sender().objectName():
            xcombobox = self.sender()
            ycombobox = self.findChild(QtGui.QComboBox, "pw_multipleYvariable_rl_" + str(index))
        elif "Y" in self.sender().objectName():
            xcombobox = self.findChild(QtGui.QComboBox, "pw_multipleXvariable_rl_" + str(index))
            ycombobox = self.sender()
        if ycombobox.currentText() != "Make a choice..." and xcombobox.currentText() != "Make a choice...":
            
            if index < self.option_num:
                print "you have to delete the current plot if you want to change one of the plot variables"
                return
            
            self.actionZoom.setEnabled(True)
            self.actionPan.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.actionOrigin.setEnabled(True)
            self.actionClear.setEnabled(True)
            logging.info("PlotWindow - ploting")
            xnan = ""
            ynan = ""
            self.mult_grid_option.append(False)
            self.mult_line_option.append(False)
            self.legend_visibility.append(True)
            for sublist in self.list_of_variables_and_attributes:
                if sublist[1]["var_name"] == xcombobox.currentText():
                    logging.info("PlotWindow -               x: " + xcombobox.currentText())
                    xvalue = copy.deepcopy(sublist[3].value)
                    xunits = copy.deepcopy(sublist[1]["units"])
                    xname = copy.deepcopy(sublist[1]["var_name"])
                    try:
                        xnan = sublist[1]["_FillValue"]
                    except KeyError:
                        pass 
                    break
            
            for sublist in self.list_of_variables_and_attributes:
                if sublist[1]["var_name"] == ycombobox.currentText():
                    logging.info("PlotWindow -               y: " + ycombobox.currentText())
                    yvalue = copy.deepcopy(sublist[3].value)
                    yunits = copy.deepcopy(sublist[1]["units"])
                    yname = copy.deepcopy(sublist[1]["var_name"])
                    try:
                        ynan = sublist[1]["_FillValue"]
                    except KeyError:
                        pass 
                    break
            xvalue[xvalue == xnan] = numpy.nan
            yvalue[yvalue == ynan] = numpy.nan
            self.subplot_data[index] = [xvalue, yvalue, xunits, yunits, xname, yname]
            plt.clf()
            self.subplot_plot = []
            tmp = []
            for item in self.subplot_data:
                if item:
                    tmp.append(item)
            lprop = {"family":self.default_font,
                    "size":"12"}
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
                    if not isinstance(self.mult_line_option[index], bool):
                        try:
                            self.subplot_plot[index].axes.lines[0].set_linestyle(self.mult_line_option[index]["line"])
                            self.subplot_plot[index].axes.lines[0].set_marker(None)
                        except KeyError:
                            self.subplot_plot[index].axes.lines[0].set_linestyle(self.mult_line_option[index]["marker"])
                            self.subplot_plot[index].axes.lines[0].set_marker(None)
                        else:
                            pass
                        try:
                            self.subplot_plot[index].axes.lines[0].set_color(self.mult_line_option[index]["color"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[index].axes.lines[0].set_linewidth(self.mult_line_option[index]["width"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[index].axes.lines[0].set_antialiased(self.mult_line_option[index]["antialiased"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[index].axes.lines[0].set_alpha(self.mult_line_option[index]["opacity"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[index].axes.lines[0].set_label(self.mult_line_option[index]["label"])
                        except KeyError:
                            pass
                    
                    leg = self.subplot_plot[index].legend(prop=lprop)
                    leg.draggable()
                    
                    if not isinstance(self.mult_grid_option[index], bool):
                        self.subplot_plot[index].grid(b=True, **self.mult_grid_option[index])
                        
                    if not self.legend_visibility[index]:
                        plt.gca().legend().set_visible(False)
            self.figure.tight_layout()
            plt.subplots_adjust(left=self.mult_margin_left,
                                right=self.mult_margin_right,
                                bottom=self.mult_margin_bottom,
                                top=self.mult_margin_top,
                                hspace=self.mult_vert_space)
            self.canvas.draw()
            if index == self.option_num:
                self.figure_options()
                self.plot_options()
            else:
                """ create a function to update the selected plot and options"""

    
    def del_subplot(self, index = None):
        if index == None:
            index = int(self.sender().objectName()[18:])
        self.subplot_data.pop(index)
        self.mult_grid_option.pop(index)
        self.mult_line_option.pop(index)
        if self.pw_multipleYvariable_rl[index].currentText() != "Make a choice..." and self.pw_multipleXvariable_rl[index].currentText() != "Make a choice...":
            plt.clf()
            self.subplot_plot = []
            tmp = []
            for item in self.subplot_data:
                if item:
                    tmp.append(item)
            lprop = {"family":self.default_font,
                    "size":"12"}
            for i, item in enumerate(tmp):
                if item:
                    self.subplot_plot.append(self.figure.add_subplot(len(tmp), 1, i + 1))
                    self.subplot_plot[i].plot(item[0], item[1], label = item[5])
                    self.subplot_plot[i].set_ylabel(item[3])
                    self.subplot_plot[i].set_xlabel(item[2])
                    self.subplot_plot[i].set_ylim([self.subplot_plot[i].axes.get_yticks()[0],
                                                           self.subplot_plot[i].axes.get_yticks()[-1]])
                    self.subplot_plot[i].set_xlim([self.subplot_plot[i].axes.get_xticks()[0],
                                                           self.subplot_plot[i].axes.get_xticks()[-1]])
                    self.subplot_plot[i].spines['top'].set_visible(False)
                    self.subplot_plot[i].spines['right'].set_visible(False)
                    self.subplot_plot[i].get_xaxis().tick_bottom()
                    self.subplot_plot[i].get_yaxis().tick_left()
                    self.subplot_plot[i].set_axisbelow(True)  
                    if not isinstance(self.mult_line_option[i], bool):
                        try:
                            self.subplot_plot[i].axes.lines[0].set_linestyle(self.mult_line_option[i]["line"])
                            self.subplot_plot[i].axes.lines[0].set_marker(None)
                        except KeyError:
                            self.subplot_plot[i].axes.lines[0].set_linestyle(self.mult_line_option[i]["marker"])
                            self.subplot_plot[i].axes.lines[0].set_marker(None)
                        else:
                            pass
                        try:
                            self.subplot_plot[i].axes.lines[0].set_color(self.mult_line_option[i]["color"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[i].axes.lines[0].set_linewidth(self.mult_line_option[i]["width"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[i].axes.lines[0].set_antialiased(self.mult_line_option[i]["antialiased"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[i].axes.lines[0].set_alpha(self.mult_line_option[i]["opacity"])
                        except KeyError:
                            pass
                        try:
                            self.subplot_plot[i].axes.lines[0].set_label(self.mult_line_option[i]["label"])
                        except KeyError:
                            pass
                        
                    leg = self.subplot_plot[i].legend(prop=lprop)
                    leg.draggable()
                    if not isinstance(self.mult_grid_option[i], bool):
                        self.subplot_plot[i].grid(b=True, **self.mult_grid_option[i])
                    if not self.legend_visibility[i]:
                        plt.gca().legend().set_visible(False)
            if self.subplot_data:
                self.figure.tight_layout()
                plt.subplots_adjust(left=self.mult_margin_left,
                                    right=self.mult_margin_right,
                                    bottom=self.mult_margin_bottom,
                                    top=self.mult_margin_top,
                                    hspace=self.mult_vert_space)
                self.canvas.draw()
            self.del_figure_options(index)
            self.del_plot_options(index)
            logging.info("PlotWindow - variable deleted")
        
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
        self.multiple_num -= 1
        if len(self.pw_multipleVerlayout_1) > 0:
            for i in range(0, len(self.pw_multipleVerlayout_1)):
                self.pw_singleLabel_1[i].setText("Subplot " + str(i + 1))
                self.pw_multipleVerlayout_2[i].setObjectName(_fromUtf8("pw_multipleVerlayout_2_" + str(i)))
                self.pw_multipleVerlayout_1[i].setObjectName(_fromUtf8("pw_multipleVerlayout_1_" + str(i)))
                self.pw_multipleHorlayout_2[i].setObjectName(_fromUtf8("pw_multipleHorlayout_2_" + str(i)))
                self.pw_singleLabel_1[i].setObjectName(_fromUtf8("pw_singleLabel_1_" + str(i)))
                self.pw_multipleHorlayout_3[i].setObjectName(_fromUtf8("pw_multipleHorlayout_3_" + str(i)))
                self.pw_singleLabel_2[i].setObjectName(_fromUtf8("pw_singleLabel_2_" + str(i)))
                self.pw_multipleHorlayout_4[i].setObjectName(_fromUtf8("pw_multipleHorlayout_4_" + str(i)))
                self.pw_multipleXvariable_rl[i].setObjectName(_fromUtf8("pw_multipleXvariable_rl_" + str(i)))
                self.pw_multipleHorlayout_5[i].setObjectName(_fromUtf8("pw_multipleHorlayout_5_" + str(i)))
                self.pw_singleLabel_3[i].setObjectName(_fromUtf8("pw_singleLabel_3_" + str(i)))
                self.pw_multipleHorlayout_6[i].setObjectName(_fromUtf8("pw_multipleHorlayout_6_" + str(i)))
                self.pw_multipleYvariable_rl[i].setObjectName(_fromUtf8("pw_multipleYvariable_rl_" + str(i)))
                self.pw_multipleHorlayout_7[i].setObjectName(_fromUtf8("pw_multipleHorlayout_7_" + str(i)))
                self.pw_multipleDel_bt[i].setObjectName(_fromUtf8("pw_multipleDel_bt_" + str(i)))
                self.pw_multipleLine_1[i].setObjectName(_fromUtf8("pw_multipleLine_1_" + str(i)))
        else:
            plt.clf()
            self.canvas.draw()
            self.actionZoom.setEnabled(False)
            self.actionPan.setEnabled(False)
            self.actionSave_as.setEnabled(False)
            self.actionOrigin.setEnabled(False)
            self.actionClear.setEnabled(False)
        
        
    def figure_options(self):
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_figureOptions_vl_1.append(QtGui.QVBoxLayout())
        self.pw_figureOptions_vl_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_vl_1_" + str(self.option_num)))
        self.pw_figureOptions_hl_1.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_1_" + str(self.option_num)))
        self.pw_figureOptions_lb_1.append(QtGui.QLabel())
        self.pw_figureOptions_lb_1[self.option_num].setMinimumSize(QtCore.QSize(300, 27))
        self.pw_figureOptions_lb_1[self.option_num].setMaximumSize(QtCore.QSize(300, 27))
        self.pw_figureOptions_lb_1[self.option_num].setFont(font2)
        if self.plot_type_str == "single":
            self.pw_figureOptions_lb_1[self.option_num].setText("Figure options:")
        else:
            self.pw_figureOptions_lb_1[self.option_num].setText("Subplot " + str(self.option_num + 1) + ": Figure options")
        self.pw_figureOptions_lb_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_1_" + str(self.option_num)))
        self.pw_figureOptions_hl_1[self.option_num].addWidget(self.pw_figureOptions_lb_1[self.option_num])
        self.pw_figureOptions_hl_1[self.option_num].addItem(QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_1[self.option_num])
        self.pw_figureOptions_hl_2.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_2[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_2_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_2.append(QtGui.QLabel())
        self.pw_figureOptions_lb_2[self.option_num].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_figureOptions_lb_2[self.option_num].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_figureOptions_lb_2[self.option_num].setFont(font)
        self.pw_figureOptions_lb_2[self.option_num].setText("Figure title:")
        self.pw_figureOptions_lb_2[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_2_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_lb_2[self.option_num])
        self.pw_figureOptions_ln_1.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_1[self.option_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_1[self.option_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_1[self.option_num].setFont(font)
        self.pw_figureOptions_ln_1[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_1[self.option_num].setObjectName(_fromUtf8("pw_lineEdit_1_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_ln_1[self.option_num])
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_3.append(QtGui.QLabel())
        self.pw_figureOptions_lb_3[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_3[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_3[self.option_num].setFont(font)
        self.pw_figureOptions_lb_3[self.option_num].setText("Font:")
        self.pw_figureOptions_lb_3[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_3_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_lb_3[self.option_num])
        self.pw_figureOptions_cb_1.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_1[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_1[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_1[self.option_num].setFont(font)
        self.pw_figureOptions_cb_1[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_1[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_1_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_cb_1[self.option_num])
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_4.append(QtGui.QLabel())
        self.pw_figureOptions_lb_4[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_4[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_4[self.option_num].setFont(font)
        self.pw_figureOptions_lb_4[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_4[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_4_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_lb_4[self.option_num])
        self.pw_figureOptions_cb_2.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_2[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_2[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_2[self.option_num].setFont(font)
        self.pw_figureOptions_cb_2[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_2[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_2[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_2_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_cb_2[self.option_num])
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_1.append(QtGui.QToolButton())
        self.pw_figureOptions_bt_1[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_1[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_1[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_figureOptions_bt_1[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_bt_1[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_1[self.option_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_1[self.option_num].setAutoRaise(True)
        self.pw_figureOptions_bt_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_1_" + str(self.option_num)))
        self.pw_figureOptions_hl_2[self.option_num].addWidget(self.pw_figureOptions_bt_1[self.option_num])
        self.pw_figureOptions_hl_2[self.option_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_2[self.option_num])
        self.pw_figureOptions_hl_3.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_3[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_3_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_5.append(QtGui.QLabel())
        self.pw_figureOptions_lb_5[self.option_num].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_figureOptions_lb_5[self.option_num].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_figureOptions_lb_5[self.option_num].setFont(font)
        self.pw_figureOptions_lb_5[self.option_num].setText("X axis label:")
        self.pw_figureOptions_lb_5[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_5_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_lb_5[self.option_num])
        self.pw_figureOptions_ln_2.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_2[self.option_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_2[self.option_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_2[self.option_num].setFont(font)
        self.pw_figureOptions_ln_2[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_2[self.option_num].setObjectName(_fromUtf8("pw_lineEdit_2_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_ln_2[self.option_num])
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_6.append(QtGui.QLabel())
        self.pw_figureOptions_lb_6[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_6[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_6[self.option_num].setFont(font)
        self.pw_figureOptions_lb_6[self.option_num].setText("Font:")
        self.pw_figureOptions_lb_6[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_6_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_lb_6[self.option_num])
        self.pw_figureOptions_cb_3.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_3[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_3[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_3[self.option_num].setFont(font)
        self.pw_figureOptions_cb_3[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_3[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_3[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_3_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_cb_3[self.option_num])
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_7.append(QtGui.QLabel())
        self.pw_figureOptions_lb_7[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_7[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_7[self.option_num].setFont(font)
        self.pw_figureOptions_lb_7[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_7[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_7_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_lb_7[self.option_num])
        self.pw_figureOptions_cb_4.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_4[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_4[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_4[self.option_num].setFont(font)
        self.pw_figureOptions_cb_4[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_4[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_4[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_4_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_cb_4[self.option_num])
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_2.append(QtGui.QToolButton())
        self.pw_figureOptions_bt_2[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_2[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_2[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_figureOptions_bt_2[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_bt_2[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_2[self.option_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_2[self.option_num].setAutoRaise(True)
        self.pw_figureOptions_bt_2[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_2_" + str(self.option_num)))
        self.pw_figureOptions_hl_3[self.option_num].addWidget(self.pw_figureOptions_bt_2[self.option_num])
        self.pw_figureOptions_hl_3[self.option_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_3[self.option_num])
        self.pw_figureOptions_hl_4.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_4[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_4_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_8.append(QtGui.QLabel())
        self.pw_figureOptions_lb_8[self.option_num].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_figureOptions_lb_8[self.option_num].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_figureOptions_lb_8[self.option_num].setFont(font)
        self.pw_figureOptions_lb_8[self.option_num].setText("Y axis label:")
        self.pw_figureOptions_lb_8[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_8_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addWidget(self.pw_figureOptions_lb_8[self.option_num])
        self.pw_figureOptions_ln_3.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_3[self.option_num].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_3[self.option_num].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_figureOptions_ln_3[self.option_num].setFont(font)
        self.pw_figureOptions_ln_3[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_3[self.option_num].setObjectName(_fromUtf8("pw_lineEdit_3_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addWidget(self.pw_figureOptions_ln_3[self.option_num])
        self.pw_figureOptions_hl_4[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_9.append(QtGui.QLabel())
        self.pw_figureOptions_lb_9[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_9[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_9[self.option_num].setFont(font)
        self.pw_figureOptions_lb_9[self.option_num].setText("Font:")
        self.pw_figureOptions_lb_9[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_9_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addWidget(self.pw_figureOptions_lb_9[self.option_num])
        self.pw_figureOptions_cb_5.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_5[self.option_num].setMinimumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_5[self.option_num].setMaximumSize(QtCore.QSize(240, 27))
        self.pw_figureOptions_cb_5[self.option_num].setFont(font)
        self.pw_figureOptions_cb_5[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_5[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_5[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_5_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addWidget(self.pw_figureOptions_cb_5[self.option_num])
        self.pw_figureOptions_hl_4[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_10.append(QtGui.QLabel())
        self.pw_figureOptions_lb_10[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_10[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_10[self.option_num].setFont(font)
        self.pw_figureOptions_lb_10[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_10[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_10_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addWidget(self.pw_figureOptions_lb_10[self.option_num])
        self.pw_figureOptions_cb_6.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_6[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_6[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_cb_6[self.option_num].setFont(font)
        self.pw_figureOptions_cb_6[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_6[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_6[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_6_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addWidget(self.pw_figureOptions_cb_6[self.option_num])
        self.pw_figureOptions_hl_4[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_3.append(QtGui.QToolButton())
        self.pw_figureOptions_bt_3[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_3[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_3[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_figureOptions_bt_3[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_bt_3[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_3[self.option_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_3[self.option_num].setAutoRaise(True)
        self.pw_figureOptions_bt_3[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_3_" + str(self.option_num)))
        self.pw_figureOptions_hl_4[self.option_num].addWidget(self.pw_figureOptions_bt_3[self.option_num])
        self.pw_figureOptions_hl_4[self.option_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_4[self.option_num])
        self.pw_figureOptions_hl_5.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_5[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_5_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_11.append(QtGui.QLabel())
        self.pw_figureOptions_lb_11[self.option_num].setMinimumSize(QtCore.QSize(190, 27))
        self.pw_figureOptions_lb_11[self.option_num].setMaximumSize(QtCore.QSize(190, 27))
        self.pw_figureOptions_lb_11[self.option_num].setFont(font)
        self.pw_figureOptions_lb_11[self.option_num].setText("X min / max / tick step:")
        self.pw_figureOptions_lb_11[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_11_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_lb_11[self.option_num])
        self.pw_figureOptions_ln_4.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_4[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_4[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_4[self.option_num].setFont(font)
        self.pw_figureOptions_ln_4[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_4[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ln_4_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_ln_4[self.option_num])
        self.pw_figureOptions_ln_5.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_5[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_5[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_5[self.option_num].setFont(font)
        self.pw_figureOptions_ln_5[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_5[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ln_5_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_ln_5[self.option_num])
        self.pw_figureOptions_ln_6.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_6[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_6[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_6[self.option_num].setFont(font)
        self.pw_figureOptions_ln_6[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_6[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ln_6_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_ln_6[self.option_num])
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_12.append(QtGui.QLabel())
        self.pw_figureOptions_lb_12[self.option_num].setMinimumSize(QtCore.QSize(80, 27))
        self.pw_figureOptions_lb_12[self.option_num].setMaximumSize(QtCore.QSize(80, 27))
        self.pw_figureOptions_lb_12[self.option_num].setFont(font)
        self.pw_figureOptions_lb_12[self.option_num].setText("Format:")
        self.pw_figureOptions_lb_12[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_12_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_lb_12[self.option_num])
        self.pw_figureOptions_cb_7.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_7[self.option_num].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_7[self.option_num].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_7[self.option_num].setFont(font)
        self.pw_figureOptions_cb_7[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_7[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_7[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_7_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_cb_7[self.option_num])
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_4.append(QtGui.QToolButton())
        self.pw_figureOptions_bt_4[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_4[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_4[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_figureOptions_bt_4[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_bt_4[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_4[self.option_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_4[self.option_num].setAutoRaise(True)
        self.pw_figureOptions_bt_4[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_4_" + str(self.option_num)))
        self.pw_figureOptions_hl_5[self.option_num].addWidget(self.pw_figureOptions_bt_4[self.option_num])
        self.pw_figureOptions_hl_5[self.option_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_5[self.option_num])
        self.pw_figureOptions_hl_6.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_6[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_6_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_13.append(QtGui.QLabel())
        self.pw_figureOptions_lb_13[self.option_num].setMinimumSize(QtCore.QSize(190, 27))
        self.pw_figureOptions_lb_13[self.option_num].setMaximumSize(QtCore.QSize(190, 27))
        self.pw_figureOptions_lb_13[self.option_num].setFont(font)
        self.pw_figureOptions_lb_13[self.option_num].setText("Y min / max / tick step:")
        self.pw_figureOptions_lb_13[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_13_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addWidget(self.pw_figureOptions_lb_13[self.option_num])
        self.pw_figureOptions_ln_7.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_7[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_7[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_7[self.option_num].setFont(font)
        self.pw_figureOptions_ln_7[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_7[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ln_7_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addWidget(self.pw_figureOptions_ln_7[self.option_num])
        self.pw_figureOptions_ln_8.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_8[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_8[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_8[self.option_num].setFont(font)
        self.pw_figureOptions_ln_8[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_8[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ln_8_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addWidget(self.pw_figureOptions_ln_8[self.option_num])
        self.pw_figureOptions_ln_9.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_9[self.option_num].setMinimumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_9[self.option_num].setMaximumSize(QtCore.QSize(70, 27))
        self.pw_figureOptions_ln_9[self.option_num].setFont(font)
        self.pw_figureOptions_ln_9[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_figureOptions_ln_9[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ln_9_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addWidget(self.pw_figureOptions_ln_9[self.option_num])
        self.pw_figureOptions_hl_6[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_14.append(QtGui.QLabel())
        self.pw_figureOptions_lb_14[self.option_num].setMinimumSize(QtCore.QSize(80, 27))
        self.pw_figureOptions_lb_14[self.option_num].setMaximumSize(QtCore.QSize(80, 27))
        self.pw_figureOptions_lb_14[self.option_num].setFont(font)
        self.pw_figureOptions_lb_14[self.option_num].setText("Format:")
        self.pw_figureOptions_lb_14[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_14_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addWidget(self.pw_figureOptions_lb_14[self.option_num])
        self.pw_figureOptions_cb_8.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_8[self.option_num].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_8[self.option_num].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_figureOptions_cb_8[self.option_num].setFont(font)
        self.pw_figureOptions_cb_8[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_figureOptions_cb_8[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_8[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_8_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addWidget(self.pw_figureOptions_cb_8[self.option_num])
        self.pw_figureOptions_hl_6[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_5.append(QtGui.QToolButton())
        self.pw_figureOptions_bt_5[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_5[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_5[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_figureOptions_bt_5[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_bt_5[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_5[self.option_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_5[self.option_num].setAutoRaise(True)
        self.pw_figureOptions_bt_5[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_5_" + str(self.option_num)))
        self.pw_figureOptions_hl_6[self.option_num].addWidget(self.pw_figureOptions_bt_5[self.option_num])
        self.pw_figureOptions_hl_6[self.option_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_6[self.option_num])
        self.pw_figureOptions_hl_7.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_7[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_7_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_15.append(QtGui.QLabel())
        self.pw_figureOptions_lb_15[self.option_num].setMinimumSize(QtCore.QSize(110, 27))
        self.pw_figureOptions_lb_15[self.option_num].setMaximumSize(QtCore.QSize(110, 27))
        self.pw_figureOptions_lb_15[self.option_num].setFont(font)
        self.pw_figureOptions_lb_15[self.option_num].setText("Display grid ?")
        self.pw_figureOptions_lb_15[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_15_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_lb_15[self.option_num])
        self.pw_figureOptions_ck_1.append(QtGui.QCheckBox())
        self.pw_figureOptions_ck_1[self.option_num].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_1[self.option_num].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_1[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_ck_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ck_1_" + str(self.option_num)))
        self.pw_figureOptions_ck_1[self.option_num].setStyleSheet(_fromUtf8("QCheckBox {\n"
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
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_ck_1[self.option_num])
        self.pw_figureOptions_hl_7[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_16.append(QtGui.QLabel())
        self.pw_figureOptions_lb_16[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_lb_16[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_lb_16[self.option_num].setFont(font)
        self.pw_figureOptions_lb_16[self.option_num].setText("Style:")
        self.pw_figureOptions_lb_16[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_16_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_lb_16[self.option_num])
        self.pw_figureOptions_cb_9.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_9[self.option_num].setEnabled(False)
        self.pw_figureOptions_cb_9[self.option_num].setMinimumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_9[self.option_num].setMaximumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_9[self.option_num].setFont(font)
        self.pw_figureOptions_cb_9[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
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
        self.pw_figureOptions_cb_9[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_9[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_9_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_cb_9[self.option_num])
        self.pw_figureOptions_hl_7[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_17.append(QtGui.QLabel())
        self.pw_figureOptions_lb_17[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_17[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
        self.pw_figureOptions_lb_17[self.option_num].setFont(font)
        self.pw_figureOptions_lb_17[self.option_num].setText("Size:")
        self.pw_figureOptions_lb_17[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_17_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_lb_17[self.option_num])
        self.pw_figureOptions_ln_10.append(QtGui.QLineEdit())
        self.pw_figureOptions_ln_10[self.option_num].setEnabled(False)
        self.pw_figureOptions_ln_10[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_ln_10[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_ln_10[self.option_num].setFont(font)
        self.pw_figureOptions_ln_10[self.option_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}"))
        self.pw_figureOptions_ln_10[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ln_10_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_ln_10[self.option_num])
        self.pw_figureOptions_hl_7[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        
        self.pw_figureOptions_lb_19.append(QtGui.QLabel())
        self.pw_figureOptions_lb_19[self.option_num].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_lb_19[self.option_num].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_figureOptions_lb_19[self.option_num].setFont(font)
        self.pw_figureOptions_lb_19[self.option_num].setText("Color:")
        self.pw_figureOptions_lb_19[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_19_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_lb_19[self.option_num])
        self.pw_figureOptions_cb_10.append(QtGui.QComboBox())
        self.pw_figureOptions_cb_10[self.option_num].setEnabled(False)
        self.pw_figureOptions_cb_10[self.option_num].setMinimumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_10[self.option_num].setMaximumSize(QtCore.QSize(160, 27))
        self.pw_figureOptions_cb_10[self.option_num].setFont(font)
        self.pw_figureOptions_cb_10[self.option_num].setStyleSheet(_fromUtf8("QComboBox {\n"
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
        self.pw_figureOptions_cb_10[self.option_num].setFrame(False)
        self.pw_figureOptions_cb_10[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_cb_10_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_cb_10[self.option_num])
        self.pw_figureOptions_hl_7[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        
        self.pw_figureOptions_bt_6.append(QtGui.QToolButton())
        self.pw_figureOptions_bt_6[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_6[self.option_num].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_6[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_figureOptions_bt_6[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_bt_6[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_6[self.option_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_6[self.option_num].setAutoRaise(True)
        self.pw_figureOptions_bt_6[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_6_" + str(self.option_num)))
        self.pw_figureOptions_hl_7[self.option_num].addWidget(self.pw_figureOptions_bt_6[self.option_num])
        self.pw_figureOptions_hl_7[self.option_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_7[self.option_num])
        self.pw_figureOptions_hl_8.append(QtGui.QHBoxLayout())
        self.pw_figureOptions_hl_8[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_8_" + str(self.option_num)))
        self.pw_figureOptions_hl_8[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_lb_18.append(QtGui.QLabel())
        self.pw_figureOptions_lb_18[self.option_num].setMinimumSize(QtCore.QSize(130, 27))
        self.pw_figureOptions_lb_18[self.option_num].setMaximumSize(QtCore.QSize(130, 27))
        self.pw_figureOptions_lb_18[self.option_num].setFont(font)
        self.pw_figureOptions_lb_18[self.option_num].setText("Display Legend ?")
        self.pw_figureOptions_lb_18[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_18_" + str(self.option_num)))
        self.pw_figureOptions_hl_8[self.option_num].addWidget(self.pw_figureOptions_lb_18[self.option_num])
        self.pw_figureOptions_ck_2.append(QtGui.QCheckBox())
        self.pw_figureOptions_ck_2[self.option_num].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_2[self.option_num].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_figureOptions_ck_2[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_ck_2[self.option_num].setChecked(True)
        self.pw_figureOptions_ck_2[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_ck_2_" + str(self.option_num)))
        self.pw_figureOptions_ck_2[self.option_num].setStyleSheet(_fromUtf8("QCheckBox {\n"
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
        self.pw_figureOptions_hl_8[self.option_num].addWidget(self.pw_figureOptions_ck_2[self.option_num])
        self.pw_figureOptions_hl_8[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_bt_7.append(QtGui.QToolButton())
        self.pw_figureOptions_bt_7[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_7[self.option_num].setMaximumSize(QtCore.QSize(27, 24))
        self.pw_figureOptions_bt_7[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_figureOptions_bt_7[self.option_num].setText(_fromUtf8(""))
        self.pw_figureOptions_bt_7[self.option_num].setIcon(icon)
        self.pw_figureOptions_bt_7[self.option_num].setIconSize(QtCore.QSize(27, 27))
        self.pw_figureOptions_bt_7[self.option_num].setAutoRaise(True)
        self.pw_figureOptions_bt_7[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_7_" + str(self.option_num)))
        self.pw_figureOptions_hl_8[self.option_num].addWidget(self.pw_figureOptions_bt_7[self.option_num])
        self.pw_figureOptions_hl_8[self.option_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_8[self.option_num])
        if self.option_num < 1:
            self.pw_figureOptions_hl_11.append(QtGui.QHBoxLayout())
            self.pw_figureOptions_hl_11[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_11_" + str(self.option_num)))
            self.pw_figureOptions_hl_11[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
            self.pw_figureOptions_lb_20.append(QtGui.QLabel())
            self.pw_figureOptions_lb_20[self.option_num].setMinimumSize(QtCore.QSize(170, 27))
            self.pw_figureOptions_lb_20[self.option_num].setMaximumSize(QtCore.QSize(170, 27))
            self.pw_figureOptions_lb_20[self.option_num].setFont(font)
            self.pw_figureOptions_lb_20[self.option_num].setText("Set figure margins:")
            self.pw_figureOptions_lb_20[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_20_" + str(self.option_num)))
            self.pw_figureOptions_hl_11[self.option_num].addWidget(self.pw_figureOptions_lb_20[self.option_num])
            self.pw_figureOptions_vl_2.append(QtGui.QVBoxLayout())
            self.pw_figureOptions_vl_2[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_vl_2_" + str(self.option_num)))
            self.pw_figureOptions_hl_9.append(QtGui.QHBoxLayout())
            self.pw_figureOptions_hl_9[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_9_" + str(self.option_num)))
            self.pw_figureOptions_lb_21.append(QtGui.QLabel())
            self.pw_figureOptions_lb_21[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_21[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_21[self.option_num].setFont(font)
            self.pw_figureOptions_lb_21[self.option_num].setText("Left:")
            self.pw_figureOptions_lb_21[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_21_" + str(self.option_num)))
            self.pw_figureOptions_hl_9[self.option_num].addWidget(self.pw_figureOptions_lb_21[self.option_num])
            self.pw_figureOptions_sl_1.append(QtGui.QSlider())
            self.pw_figureOptions_sl_1[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
            self.pw_figureOptions_sl_1[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
            self.pw_figureOptions_sl_1[self.option_num].setMinimum(0)
            self.pw_figureOptions_sl_1[self.option_num].setMaximum(40)
            self.pw_figureOptions_sl_1[self.option_num].setSingleStep(1)
            self.pw_figureOptions_sl_1[self.option_num].setPageStep(1)
            self.pw_figureOptions_sl_1[self.option_num].setOrientation(QtCore.Qt.Horizontal)
            self.pw_figureOptions_sl_1[self.option_num].setTickPosition(QtGui.QSlider.TicksBelow)
            self.pw_figureOptions_sl_1[self.option_num].setTickInterval(4)
            self.pw_figureOptions_sl_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_1_" + str(self.option_num)))
            self.pw_figureOptions_sl_1[self.option_num].setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
            "    border: 1px solid #999999;\n"
            "    height: 1px;\n"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
            "    margin: 2px 0;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
            "    border: 1px solid #5c5c5c;\n"
            "    width: 10px;\n"
            "    margin: -5px 0;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "    background: rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "    background: rgb(0,0,200);\n"
            "}"))
            self.pw_figureOptions_hl_9[self.option_num].addWidget(self.pw_figureOptions_sl_1[self.option_num])
            self.pw_figureOptions_lb_22.append(QtGui.QLabel())
            self.pw_figureOptions_lb_22[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_22[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_22[self.option_num].setFont(font)
            self.pw_figureOptions_lb_22[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_1_" + str(self.option_num) + "lb_" + str(self.option_num)))
            self.pw_figureOptions_hl_9[self.option_num].addWidget(self.pw_figureOptions_lb_22[self.option_num])
            self.pw_figureOptions_hl_9[self.option_num].addItem(QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
            self.pw_figureOptions_lb_23.append(QtGui.QLabel())
            self.pw_figureOptions_lb_23[self.option_num].setMinimumSize(QtCore.QSize(80, 27))
            self.pw_figureOptions_lb_23[self.option_num].setMaximumSize(QtCore.QSize(80, 27))
            self.pw_figureOptions_lb_23[self.option_num].setFont(font)
            self.pw_figureOptions_lb_23[self.option_num].setText("Right:")
            self.pw_figureOptions_lb_23[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_23_" + str(self.option_num)))
            self.pw_figureOptions_hl_9[self.option_num].addWidget(self.pw_figureOptions_lb_23[self.option_num])
            self.pw_figureOptions_sl_2.append(QtGui.QSlider())
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
            self.pw_figureOptions_sl_2[self.option_num].setTickPosition(QtGui.QSlider.TicksBelow)
            self.pw_figureOptions_sl_2[self.option_num].setTickInterval(4)
            self.pw_figureOptions_sl_2[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_2_" + str(self.option_num)))
            self.pw_figureOptions_sl_2[self.option_num].setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
            "    border: 1px solid #999999;\n"
            "    height: 1px;\n"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
            "    margin: 2px 0;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
            "    border: 1px solid #5c5c5c;\n"
            "    width: 10px;\n"
            "    margin: -5px 0;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "    background: rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "    background: rgb(0,0,200);\n"
            "}"))
            self.pw_figureOptions_hl_9[self.option_num].addWidget(self.pw_figureOptions_sl_2[self.option_num])
            self.pw_figureOptions_lb_24.append(QtGui.QLabel())
            self.pw_figureOptions_lb_24[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_24[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_24[self.option_num].setFont(font)
            self.pw_figureOptions_lb_24[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_2_" + str(self.option_num) + "lb_" + str(self.option_num)))
            self.pw_figureOptions_hl_9[self.option_num].addWidget(self.pw_figureOptions_lb_24[self.option_num])
            self.pw_figureOptions_vl_2[self.option_num].addLayout(self.pw_figureOptions_hl_9[self.option_num])
            self.pw_figureOptions_hl_10.append(QtGui.QHBoxLayout())
            self.pw_figureOptions_hl_10[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_10_" + str(self.option_num)))
            self.pw_figureOptions_lb_25.append(QtGui.QLabel())
            self.pw_figureOptions_lb_25[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_25[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_25[self.option_num].setFont(font)
            self.pw_figureOptions_lb_25[self.option_num].setText("Top:")
            self.pw_figureOptions_lb_25[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_25_" + str(self.option_num)))
            self.pw_figureOptions_hl_10[self.option_num].addWidget(self.pw_figureOptions_lb_25[self.option_num])
            self.pw_figureOptions_sl_3.append(QtGui.QSlider())
            self.pw_figureOptions_sl_3[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
            self.pw_figureOptions_sl_3[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
            self.pw_figureOptions_sl_3[self.option_num].setMinimum(0)
            self.pw_figureOptions_sl_3[self.option_num].setMaximum(40)
            self.pw_figureOptions_sl_3[self.option_num].setSingleStep(1)
            self.pw_figureOptions_sl_3[self.option_num].setPageStep(1)
            self.pw_figureOptions_sl_3[self.option_num].setOrientation(QtCore.Qt.Horizontal)
            self.pw_figureOptions_sl_3[self.option_num].setTickPosition(QtGui.QSlider.TicksBelow)
            self.pw_figureOptions_sl_3[self.option_num].setTickInterval(4)
            self.pw_figureOptions_sl_3[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_3_" + str(self.option_num)))
            self.pw_figureOptions_sl_3[self.option_num].setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
            "    border: 1px solid #999999;\n"
            "    height: 1px;\n"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
            "    margin: 2px 0;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
            "    border: 1px solid #5c5c5c;\n"
            "    width: 10px;\n"
            "    margin: -5px 0;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "    background: rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "    background: rgb(0,0,200);\n"
            "}"))
            self.pw_figureOptions_hl_10[self.option_num].addWidget(self.pw_figureOptions_sl_3[self.option_num])
            self.pw_figureOptions_lb_26.append(QtGui.QLabel())
            self.pw_figureOptions_lb_26[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_26[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_26[self.option_num].setFont(font)
            self.pw_figureOptions_lb_26[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_3_" + str(self.option_num) + "lb_" + str(self.option_num)))
            self.pw_figureOptions_hl_10[self.option_num].addWidget(self.pw_figureOptions_lb_26[self.option_num])
            self.pw_figureOptions_hl_10[self.option_num].addItem(QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
            self.pw_figureOptions_lb_27.append(QtGui.QLabel())
            self.pw_figureOptions_lb_27[self.option_num].setMinimumSize(QtCore.QSize(80, 27))
            self.pw_figureOptions_lb_27[self.option_num].setMaximumSize(QtCore.QSize(80, 27))
            self.pw_figureOptions_lb_27[self.option_num].setFont(font)
            self.pw_figureOptions_lb_27[self.option_num].setText("Bottom:")
            self.pw_figureOptions_lb_27[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_27_" + str(self.option_num)))
            self.pw_figureOptions_hl_10[self.option_num].addWidget(self.pw_figureOptions_lb_27[self.option_num])
            self.pw_figureOptions_sl_4.append(QtGui.QSlider())
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
            self.pw_figureOptions_sl_4[self.option_num].setTickPosition(QtGui.QSlider.TicksBelow)
            self.pw_figureOptions_sl_4[self.option_num].setTickInterval(4)
            self.pw_figureOptions_sl_4[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_4_" + str(self.option_num)))
            self.pw_figureOptions_sl_4[self.option_num].setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
            "    border: 1px solid #999999;\n"
            "    height: 1px;\n"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
            "    margin: 2px 0;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
            "    border: 1px solid #5c5c5c;\n"
            "    width: 10px;\n"
            "    margin: -5px 0;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "    background: rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "    background: rgb(0,0,200);\n"
            "}"))
            self.pw_figureOptions_hl_10[self.option_num].addWidget(self.pw_figureOptions_sl_4[self.option_num])
            self.pw_figureOptions_lb_28.append(QtGui.QLabel())
            self.pw_figureOptions_lb_28[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_28[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
            self.pw_figureOptions_lb_28[self.option_num].setFont(font)
            self.pw_figureOptions_lb_28[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_4_" + str(self.option_num) + "lb_" + str(self.option_num)))
            self.pw_figureOptions_hl_10[self.option_num].addWidget(self.pw_figureOptions_lb_28[self.option_num])
            self.pw_figureOptions_vl_2[self.option_num].addLayout(self.pw_figureOptions_hl_10[self.option_num])
            self.pw_figureOptions_hl_11[self.option_num].addLayout(self.pw_figureOptions_vl_2[self.option_num])
            self.pw_figureOptions_bt_8.append(QtGui.QToolButton())
            self.pw_figureOptions_bt_8[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
            self.pw_figureOptions_bt_8[self.option_num].setMaximumSize(QtCore.QSize(27, 24))
            self.pw_figureOptions_bt_8[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
            "\n"
            "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
            "\n"
            "QToolButton:flat {border: none;}"))
            self.pw_figureOptions_bt_8[self.option_num].setText(_fromUtf8(""))
            self.pw_figureOptions_bt_8[self.option_num].setIcon(icon)
            self.pw_figureOptions_bt_8[self.option_num].setIconSize(QtCore.QSize(27, 27))
            self.pw_figureOptions_bt_8[self.option_num].setAutoRaise(True)
            self.pw_figureOptions_bt_8[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_8_" + str(self.option_num)))
            self.pw_figureOptions_hl_11[self.option_num].addWidget(self.pw_figureOptions_bt_8[self.option_num])
            self.pw_figureOptions_hl_11[self.option_num].addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
            self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_11[self.option_num])
            
            if self.plot_type_str == "multiple":
            
                self.pw_figureOptions_hl_12.append(QtGui.QHBoxLayout())
                self.pw_figureOptions_hl_12[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_hl_12"))
                self.pw_figureOptions_hl_12[self.option_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
                self.pw_figureOptions_lb_29.append(QtGui.QLabel())
                self.pw_figureOptions_lb_29[self.option_num].setMinimumSize(QtCore.QSize(170, 27))
                self.pw_figureOptions_lb_29[self.option_num].setMaximumSize(QtCore.QSize(170, 27))
                self.pw_figureOptions_lb_29[self.option_num].setFont(font)
                self.pw_figureOptions_lb_29[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_29"))
                self.pw_figureOptions_lb_29[self.option_num].setText("Set subplot interval:")
                self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_lb_29[self.option_num])
                self.pw_figureOptions_sl_5.append(QtGui.QSlider())
                self.pw_figureOptions_sl_5[self.option_num].setMinimumSize(QtCore.QSize(200, 27))
                self.pw_figureOptions_sl_5[self.option_num].setMaximumSize(QtCore.QSize(200, 27))
                self.pw_figureOptions_sl_5[self.option_num].setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
                "    border: 1px solid #999999;\n"
                "    height: 1px;\n"
                "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                "    margin: 2px 0;\n"
                "}\n"
                "\n"
                "QSlider::handle:horizontal {\n"
                "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                "    border: 1px solid #5c5c5c;\n"
                "    width: 10px;\n"
                "    margin: -5px 0;\n"
                "    border-radius: 5px;\n"
                "}\n"
                "\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
                "}\n"
                "\n"
                "QSlider::add-page:horizontal {\n"
                "    background: rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QSlider::sub-page:horizontal {\n"
                "    background: rgb(0,0,200);\n"
                "}"))
                self.pw_figureOptions_sl_5[self.option_num].setMinimum(0)
                self.pw_figureOptions_sl_5[self.option_num].setMaximum(100)
                self.pw_figureOptions_sl_5[self.option_num].setSingleStep(1)
                self.pw_figureOptions_sl_5[self.option_num].setPageStep(1)
                self.pw_figureOptions_sl_5[self.option_num].setOrientation(QtCore.Qt.Horizontal)
                self.pw_figureOptions_sl_5[self.option_num].setTickPosition(QtGui.QSlider.TicksBelow)
                self.pw_figureOptions_sl_5[self.option_num].setTickInterval(10)
                self.pw_figureOptions_sl_5[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_sl_5"))
                self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_sl_5[self.option_num])
                self.pw_figureOptions_lb_30.append(QtGui.QLabel())
                self.pw_figureOptions_lb_30[self.option_num].setMinimumSize(QtCore.QSize(50, 27))
                self.pw_figureOptions_lb_30[self.option_num].setMaximumSize(QtCore.QSize(50, 27))
                self.pw_figureOptions_lb_30[self.option_num].setFont(font)
                self.pw_figureOptions_lb_30[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_lb_30"))
                self.pw_figureOptions_lb_30[self.option_num].setText("TMP")
                self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_lb_30[self.option_num])
                self.pw_figureOptions_bt_9.append(QtGui.QToolButton())
                self.pw_figureOptions_bt_9[self.option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_9[self.option_num].setMaximumSize(QtCore.QSize(27, 24))
                self.pw_figureOptions_bt_9[self.option_num].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
                "\n"
                "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                "\n"
                "QToolButton:flat {border: none;}"))
                self.pw_figureOptions_bt_9[self.option_num].setText(_fromUtf8(""))
                self.pw_figureOptions_bt_9[self.option_num].setIcon(icon)
                self.pw_figureOptions_bt_9[self.option_num].setIconSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_9[self.option_num].setAutoRaise(True)
                self.pw_figureOptions_bt_9[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_bt_9"))
                self.pw_figureOptions_hl_12[self.option_num].addWidget(self.pw_figureOptions_bt_9[self.option_num])
                self.pw_figureOptions_hl_12[self.option_num].addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.option_num].addLayout(self.pw_figureOptions_hl_12[self.option_num])
        self.pw_figureOptions_vl_1[self.option_num].addItem(QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
        self.pw_figureOptions_li_1.append(QtGui.QFrame())
        self.pw_figureOptions_li_1[self.option_num].setFrameShape(QtGui.QFrame.HLine)
        self.pw_figureOptions_li_1[self.option_num].setFrameShadow(QtGui.QFrame.Sunken)
        self.pw_figureOptions_li_1[self.option_num].setObjectName(_fromUtf8("pw_figureOptions_li_1_" + str(self.option_num)))
        self.pw_figureOptions_vl_1[self.option_num].addWidget(self.pw_figureOptions_li_1[self.option_num])
        self.pw_figureOptions_vl_1[self.option_num].addItem(QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
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
    
    
    def plot_options(self):
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_plotOptions_vl_1.append(QtGui.QVBoxLayout())
        self.pw_plotOptions_vl_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_vl_1_" + str(self.option_num2)))
        self.pw_plotOptions_hl_1.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_1_" + str(self.option_num2)))
        self.pw_plotOptions_lb_1.append(QtGui.QLabel())
        self.pw_plotOptions_lb_1[self.option_num2].setMinimumSize(QtCore.QSize(700, 27))
        self.pw_plotOptions_lb_1[self.option_num2].setMaximumSize(QtCore.QSize(700, 27))
        self.pw_plotOptions_lb_1[self.option_num2].setFont(font2)
        if self.plot_type_str == "single":
            self.pw_plotOptions_lb_1[self.option_num2].setText("Plot options - " + self.pw_yvariable_rl.currentText() + ":")
        else:
            self.pw_plotOptions_lb_1[self.option_num2].setText("Subplot " + str(self.option_num2 + 1) + ": Plot options - " + self.pw_multipleYvariable_rl[self.option_num2].currentText())
        self.pw_plotOptions_lb_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_1_" + str(self.option_num2)))
        self.pw_plotOptions_hl_1[self.option_num2].addWidget(self.pw_plotOptions_lb_1[self.option_num2])
        self.pw_plotOptions_hl_1[self.option_num2].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_1[self.option_num2])
        self.pw_plotOptions_hl_2.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_2[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_2_" + str(self.option_num2)))
        self.pw_plotOptions_hl_2[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_2.append(QtGui.QLabel())
        self.pw_plotOptions_lb_2[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_2[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_2[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_2[self.option_num2].setText("Line style:")
        self.pw_plotOptions_lb_2[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_2_" + str(self.option_num2)))
        self.pw_plotOptions_hl_2[self.option_num2].addWidget(self.pw_plotOptions_lb_2[self.option_num2])
        self.pw_plotOptions_hl_3.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_3[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_3_" + str(self.option_num2)))
        self.pw_plotOptions_rb_1.append(QtGui.QRadioButton())
        self.pw_plotOptions_rb_1[self.option_num2].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_rb_1[self.option_num2].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_rb_1[self.option_num2].setFont(font)
        self.pw_plotOptions_rb_1[self.option_num2].setText("Line")
        self.pw_plotOptions_rb_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_rb_1_" + str(self.option_num2)))
        self.pw_plotOptions_rb_1[self.option_num2].setStyleSheet(_fromUtf8("QRadioButton {\n"
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
        self.pw_plotOptions_hl_3[self.option_num2].addWidget(self.pw_plotOptions_rb_1[self.option_num2])
        self.pw_plotOptions_bg_1.append(QtGui.QButtonGroup())
        self.pw_plotOptions_bg_1[self.option_num2].addButton(self.pw_plotOptions_rb_1[self.option_num2])
        self.pw_plotOptions_rb_2.append(QtGui.QRadioButton())
        self.pw_plotOptions_rb_2[self.option_num2].setMinimumSize(QtCore.QSize(90, 27))
        self.pw_plotOptions_rb_2[self.option_num2].setMaximumSize(QtCore.QSize(90, 27))
        self.pw_plotOptions_rb_2[self.option_num2].setFont(font)
        self.pw_plotOptions_rb_2[self.option_num2].setText("Marker")
        self.pw_plotOptions_rb_2[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_rb_2_" + str(self.option_num2)))
        self.pw_plotOptions_rb_2[self.option_num2].setStyleSheet(_fromUtf8("QRadioButton {\n"
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
        self.pw_plotOptions_hl_3[self.option_num2].addWidget(self.pw_plotOptions_rb_2[self.option_num2])
        self.pw_plotOptions_bg_1[self.option_num2].addButton(self.pw_plotOptions_rb_2[self.option_num2])
        self.pw_plotOptions_hl_2[self.option_num2].addLayout(self.pw_plotOptions_hl_3[self.option_num2])
        self.pw_plotOptions_cb_1.append(QtGui.QComboBox())
        self.pw_plotOptions_cb_1[self.option_num2].setMinimumSize(QtCore.QSize(180, 27))
        self.pw_plotOptions_cb_1[self.option_num2].setMaximumSize(QtCore.QSize(180, 27))
        self.pw_plotOptions_cb_1[self.option_num2].setFont(font)
        self.pw_plotOptions_cb_1[self.option_num2].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(180, 180, 180);\n"
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
        self.pw_plotOptions_cb_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_cb_1_" + str(self.option_num2)))
        self.pw_plotOptions_hl_2[self.option_num2].addWidget(self.pw_plotOptions_cb_1[self.option_num2])
        self.pw_plotOptions_hl_2[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_1.append(QtGui.QToolButton())
        self.pw_plotOptions_bt_1[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_1[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_1[self.option_num2].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_plotOptions_bt_1[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_bt_1[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_1[self.option_num2].setIconSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_1[self.option_num2].setAutoRaise(True)
        self.pw_plotOptions_bt_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_bt_1_" + str(self.option_num2)))
        self.pw_plotOptions_hl_2[self.option_num2].addWidget(self.pw_plotOptions_bt_1[self.option_num2])
        self.pw_plotOptions_hl_2[self.option_num2].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_2[self.option_num2])
        self.pw_plotOptions_hl_4.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_4[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_4_" + str(self.option_num2)))
        self.pw_plotOptions_hl_4[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_3.append(QtGui.QLabel())
        self.pw_plotOptions_lb_3[self.option_num2].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_3[self.option_num2].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_3[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_3[self.option_num2].setText("Line / Marker color:")
        self.pw_plotOptions_lb_3[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_3_" + str(self.option_num2)))
        self.pw_plotOptions_hl_4[self.option_num2].addWidget(self.pw_plotOptions_lb_3[self.option_num2])
        self.pw_plotOptions_cb_2.append(QtGui.QComboBox())
        self.pw_plotOptions_cb_2[self.option_num2].setMinimumSize(QtCore.QSize(170, 27))
        self.pw_plotOptions_cb_2[self.option_num2].setMaximumSize(QtCore.QSize(170, 27))
        self.pw_plotOptions_cb_2[self.option_num2].setFont(font)
        self.pw_plotOptions_cb_2[self.option_num2].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
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
        self.pw_plotOptions_cb_2[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_cb_2_" + str(self.option_num2)))
        self.pw_plotOptions_hl_4[self.option_num2].addWidget(self.pw_plotOptions_cb_2[self.option_num2])
        self.pw_plotOptions_hl_5.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_5[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_5_" + str(self.option_num2)))
        self.pw_plotOptions_hl_5[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_8.append(QtGui.QLabel())
        self.pw_plotOptions_lb_8[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_8[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_8[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_8[self.option_num2].setText("RGB code:")
        self.pw_plotOptions_lb_8[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_8_" + str(self.option_num2)))
        self.pw_plotOptions_lb_8[self.option_num2].hide()
        self.pw_plotOptions_hl_5[self.option_num2].addWidget(self.pw_plotOptions_lb_8[self.option_num2])
        self.pw_plotOptions_ln_3.append(QtGui.QLineEdit())
        self.pw_plotOptions_ln_3[self.option_num2].setMinimumSize(QtCore.QSize(130, 27))
        self.pw_plotOptions_ln_3[self.option_num2].setMaximumSize(QtCore.QSize(130, 27))
        self.pw_plotOptions_ln_3[self.option_num2].setFont(font)
        self.pw_plotOptions_ln_3[self.option_num2].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_plotOptions_ln_3[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_ln_3_" + str(self.option_num2)))
        self.pw_plotOptions_ln_3[self.option_num2].hide()
        self.pw_plotOptions_hl_5[self.option_num2].addWidget(self.pw_plotOptions_ln_3[self.option_num2])
        self.pw_plotOptions_hl_4[self.option_num2].addLayout(self.pw_plotOptions_hl_5[self.option_num2])
        self.pw_plotOptions_bt_2.append(QtGui.QToolButton())
        self.pw_plotOptions_bt_2[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_2[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_2[self.option_num2].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_plotOptions_bt_2[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_bt_2[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_2[self.option_num2].setIconSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_2[self.option_num2].setAutoRaise(True)
        self.pw_plotOptions_bt_2[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_bt_2_" + str(self.option_num2)))
        self.pw_plotOptions_hl_4[self.option_num2].addWidget(self.pw_plotOptions_bt_2[self.option_num2])
        self.pw_plotOptions_hl_4[self.option_num2].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_4[self.option_num2])
        self.pw_plotOptions_hl_6.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_6[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_6_" + str(self.option_num2)))
        self.pw_plotOptions_hl_6[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_4.append(QtGui.QLabel())
        self.pw_plotOptions_lb_4[self.option_num2].setMinimumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_4[self.option_num2].setMaximumSize(QtCore.QSize(200, 27))
        self.pw_plotOptions_lb_4[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_4[self.option_num2].setText("Line width / Marker size:")
        self.pw_plotOptions_lb_4[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_4_" + str(self.option_num2)))
        self.pw_plotOptions_hl_6[self.option_num2].addWidget(self.pw_plotOptions_lb_4[self.option_num2])
        self.pw_plotOptions_ln_1.append(QtGui.QLineEdit())
        self.pw_plotOptions_ln_1[self.option_num2].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_1[self.option_num2].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_1[self.option_num2].setFont(font)
        self.pw_plotOptions_ln_1[self.option_num2].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_plotOptions_ln_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_ln_1_" + str(self.option_num2)))
        self.pw_plotOptions_hl_6[self.option_num2].addWidget(self.pw_plotOptions_ln_1[self.option_num2])
        self.pw_plotOptions_hl_6[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_3.append(QtGui.QToolButton())
        self.pw_plotOptions_bt_3[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_3[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_3[self.option_num2].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_plotOptions_bt_3[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_bt_3[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_3[self.option_num2].setIconSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_3[self.option_num2].setAutoRaise(True)
        self.pw_plotOptions_bt_3[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_bt_3_" + str(self.option_num2)))
        self.pw_plotOptions_hl_6[self.option_num2].addWidget(self.pw_plotOptions_bt_3[self.option_num2])
        self.pw_plotOptions_hl_6[self.option_num2].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_6[self.option_num2])
        self.pw_plotOptions_hl_7.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_7[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_7_" + str(self.option_num2)))
        self.pw_plotOptions_hl_7[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_5.append(QtGui.QLabel())
        self.pw_plotOptions_lb_5[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_5[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_5[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_5[self.option_num2].setText("Antialiased ?")
        self.pw_plotOptions_lb_5[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_5_" + str(self.option_num2)))
        self.pw_plotOptions_hl_7[self.option_num2].addWidget(self.pw_plotOptions_lb_5[self.option_num2])
        self.pw_plotOptions_ck_1.append(QtGui.QCheckBox())
        self.pw_plotOptions_ck_1[self.option_num2].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_1[self.option_num2].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_1[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_ck_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_ck_1_" + str(self.option_num2)))
        self.pw_plotOptions_ck_1[self.option_num2].setStyleSheet(_fromUtf8("QCheckBox {\n"
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
        self.pw_plotOptions_hl_7[self.option_num2].addWidget(self.pw_plotOptions_ck_1[self.option_num2])
        self.pw_plotOptions_hl_7[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_4.append(QtGui.QToolButton())
        self.pw_plotOptions_bt_4[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_4[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_4[self.option_num2].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_plotOptions_bt_4[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_bt_4[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_4[self.option_num2].setIconSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_4[self.option_num2].setAutoRaise(True)
        self.pw_plotOptions_bt_4[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_bt_4_" + str(self.option_num2)))
        self.pw_plotOptions_hl_7[self.option_num2].addWidget(self.pw_plotOptions_bt_4[self.option_num2])
        self.pw_plotOptions_hl_7[self.option_num2].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_7[self.option_num2])
        self.pw_plotOptions_hl_8.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_8[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_8_" + str(self.option_num2)))
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_6.append(QtGui.QLabel())
        self.pw_plotOptions_lb_6[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_6[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_6[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_6[self.option_num2].setText("Opacity ?")
        self.pw_plotOptions_lb_6[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_6_" + str(self.option_num2)))
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_lb_6[self.option_num2])
        self.pw_plotOptions_ck_2.append(QtGui.QCheckBox())
        self.pw_plotOptions_ck_2[self.option_num2].setMinimumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_2[self.option_num2].setMaximumSize(QtCore.QSize(25, 20))
        self.pw_plotOptions_ck_2[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_ck_2[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_ck_2_" + str(self.option_num2)))
        self.pw_plotOptions_ck_2[self.option_num2].setStyleSheet(_fromUtf8("QCheckBox {\n"
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
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_ck_2[self.option_num2])
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_7.append(QtGui.QLabel())
        self.pw_plotOptions_lb_7[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_7[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_7[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_7[self.option_num2].setText("Percentage:")
        self.pw_plotOptions_lb_7[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_7_" + str(self.option_num2)))
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_lb_7[self.option_num2])
        self.pw_plotOptions_ln_2.append(QtGui.QLineEdit())
        self.pw_plotOptions_ln_2[self.option_num2].setEnabled(False)
        self.pw_plotOptions_ln_2[self.option_num2].setMinimumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_2[self.option_num2].setMaximumSize(QtCore.QSize(60, 27))
        self.pw_plotOptions_ln_2[self.option_num2].setFont(font)
        self.pw_plotOptions_ln_2[self.option_num2].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "    background-color:  rgb(180, 180, 180);\n"
        "}"))
        self.pw_plotOptions_ln_2[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_ln_2_" + str(self.option_num2)))
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_ln_2[self.option_num2])
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_5.append(QtGui.QToolButton())
        self.pw_plotOptions_bt_5[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_5[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_5[self.option_num2].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_plotOptions_bt_5[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_bt_5[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_5[self.option_num2].setIconSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_5[self.option_num2].setAutoRaise(True)
        self.pw_plotOptions_bt_5[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_bt_5_" + str(self.option_num2)))
        self.pw_plotOptions_hl_8[self.option_num2].addWidget(self.pw_plotOptions_bt_5[self.option_num2])
        self.pw_plotOptions_hl_8[self.option_num2].addItem(QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_8[self.option_num2])
        
        self.pw_plotOptions_hl_9.append(QtGui.QHBoxLayout())
        self.pw_plotOptions_hl_9[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_hl_9_" + str(self.option_num2)))
        self.pw_plotOptions_hl_9[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_lb_9.append(QtGui.QLabel())
        self.pw_plotOptions_lb_9[self.option_num2].setMinimumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_9[self.option_num2].setMaximumSize(QtCore.QSize(100, 27))
        self.pw_plotOptions_lb_9[self.option_num2].setFont(font)
        self.pw_plotOptions_lb_9[self.option_num2].setText("Legend:")
        self.pw_plotOptions_lb_9[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_lb_9_" + str(self.option_num2)))
        self.pw_plotOptions_hl_9[self.option_num2].addWidget(self.pw_plotOptions_lb_9[self.option_num2])
        self.pw_plotOptions_ln_4.append(QtGui.QLineEdit())
        self.pw_plotOptions_ln_4[self.option_num2].setMinimumSize(QtCore.QSize(250, 27))
        self.pw_plotOptions_ln_4[self.option_num2].setMaximumSize(QtCore.QSize(250, 27))
        self.pw_plotOptions_ln_4[self.option_num2].setFont(font)
        self.pw_plotOptions_ln_4[self.option_num2].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.pw_plotOptions_ln_4[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_ln_4_" + str(self.option_num2)))
        self.pw_plotOptions_hl_9[self.option_num2].addWidget(self.pw_plotOptions_ln_4[self.option_num2])
        self.pw_plotOptions_hl_9[self.option_num2].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_bt_6.append(QtGui.QToolButton())
        self.pw_plotOptions_bt_6[self.option_num2].setMinimumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_6[self.option_num2].setMaximumSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_6[self.option_num2].setStyleSheet(_fromUtf8("QToolButton:hover {border: 1px solid gray; border-radius: 3px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); width: 27px; height: 27px;}\n"
        "\n"
        "QToolButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
        "\n"
        "QToolButton:flat {border: none;}"))
        self.pw_plotOptions_bt_6[self.option_num2].setText(_fromUtf8(""))
        self.pw_plotOptions_bt_6[self.option_num2].setIcon(icon)
        self.pw_plotOptions_bt_6[self.option_num2].setIconSize(QtCore.QSize(27, 27))
        self.pw_plotOptions_bt_6[self.option_num2].setAutoRaise(True)
        self.pw_plotOptions_bt_6[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_bt_6_" + str(self.option_num2)))
        self.pw_plotOptions_hl_9[self.option_num2].addWidget(self.pw_plotOptions_bt_6[self.option_num2])
        self.pw_plotOptions_hl_9[self.option_num2].addItem(QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.pw_plotOptions_vl_1[self.option_num2].addLayout(self.pw_plotOptions_hl_9[self.option_num2])
        self.pw_plotOptions_vl_1[self.option_num2].addItem(QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
        self.pw_plotOptions_li_1.append(QtGui.QFrame())
        self.pw_plotOptions_li_1[self.option_num2].setFrameShape(QtGui.QFrame.HLine)
        self.pw_plotOptions_li_1[self.option_num2].setFrameShadow(QtGui.QFrame.Sunken)
        self.pw_plotOptions_li_1[self.option_num2].setObjectName(_fromUtf8("pw_plotOptions_li_1_" + str(self.option_num2)))
        self.pw_plotOptions_vl_1[self.option_num2].addWidget(self.pw_plotOptions_li_1[self.option_num2])
        self.pw_plotOptions_vl_1[self.option_num2].addItem(QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
        self.pw_plotOptions_la.addLayout(self.pw_plotOptions_vl_1[self.option_num2])
        self.pw_plotOptions_la.setAlignment(QtCore.Qt.AlignTop)
        self.pw_plotOptions_cb_2[self.option_num2].addItem("Make a choice...")
        self.populate_comboboxes_regular(self.pw_plotOptions_cb_2[self.option_num2], self.colors)
        self.pw_plotOptions_cb_2[self.option_num2].activated.connect(lambda: self.activate_line_color())
        self.pw_plotOptions_ck_2[self.option_num2].stateChanged.connect(lambda: self.activate_opacity_options())
        self.pw_plotOptions_rb_1[self.option_num2].clicked.connect(lambda: self.activate_line_style())
        self.pw_plotOptions_rb_2[self.option_num2].clicked.connect(lambda: self.activate_line_style())
        self.pw_plotOptions_rb_1[self.option_num2].setChecked(True)
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
                    font = {'fontname':self.pw_figureOptions_cb_1[0].currentText(),
                            'fontsize':int(self.pw_figureOptions_cb_2[0].currentText())}
                    plt.title(self.pw_figureOptions_ln_1[0].text(), y=1.04, **font)
                if self.pw_figureOptions_ln_3[0].text():
                    font = {'fontname':self.pw_figureOptions_cb_5[0].currentText(),
                            'fontsize':int(self.pw_figureOptions_cb_6[0].currentText())}
                    plt.ylabel(self.pw_figureOptions_ln_3[0].text(), **font)
                if self.pw_figureOptions_ln_2[0].text():
                    font = {'fontname':self.pw_figureOptions_cb_3[0].currentText(),
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
            plt.gca().legend().draggable()
            if self.plot_type_str == "single":
                if self.pw_figureOptions_ck_2[0].isChecked():
                    plt.gca().legend().set_visible(True)
                    plt.gca().legend().draggable()
                    self.legend_visibility = True
                else:
                    plt.gca().legend().set_visible(False)
                    self.legend_visibility = False
            elif self.plot_type_str == "multiple":
                for i in range(0, len(self.pw_figureOptions_vl_1)):
                    if self.pw_figureOptions_ck_2[i].isChecked():
                        self.subplot_plot[i].legend().set_visible(True)
                        self.subplot_plot[i].legend().draggable()
                        self.legend_visibility[i] = True
                    else:
                        self.subplot_plot[i].legend().set_visible(False)
                        self.legend_visibility[i] = False
            self.canvas.draw()
    
    
    def update_plot_options(self):
        if self.plot_type_str and self.pw_plotOptions_vl_1:
            if self.plot_type_str == "single":
                for i in range(self.option_num2):
                    if self.pw_plotOptions_cb_1[i].currentText() != "" or self.pw_plotOptions_cb_1[i].currentText() != "Make a choice...":
                        try:
                            line_style = self.line_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
                            plt.axes().lines[i].set_linestyle(line_style)
                            plt.axes().lines[i].set_marker(None)
                        except KeyError:
                            line_style = self.marker_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
                            plt.axes().lines[i].set_marker(line_style)
                            plt.axes().lines[i].set_linestyle("None")
                    if self.pw_plotOptions_cb_2[i].currentText() != "Make a choice..." and self.pw_plotOptions_ln_3[i].text() != "":
                        if str(self.pw_plotOptions_cb_2[i].currentText()) == "HEX Color":
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                        elif str(self.pw_plotOptions_cb_2[i].currentText()) == "RGB Color":
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                            line_color = line_color.replace(" ", "")
                            indexes = []
                            for index, item in enumerate(line_color):
                                if item == ",":
                                    indexes.append(index)
                            line_color = (float(float(line_color[0:indexes[0]])/255),
                                          float(float(line_color[indexes[0]+1:indexes[1]])/255),
                                          float(float(line_color[indexes[1]+1:])/255))
                        else:
                            line_color = self.colors_dict[str(self.pw_plotOptions_cb_2[i].currentText())]
                        plt.axes().lines[i].set_color(line_color)

                    if self.pw_plotOptions_ln_1[i].text() != "":
                        line_width = float(self.pw_plotOptions_ln_1[i].text())
                        plt.axes().lines[i].set_linewidth(line_width)
                    if self.pw_plotOptions_ck_1[i].isChecked() == True:
                        plt.axes().lines[i].set_antialiased(True)
                    else:
                        plt.axes().lines[i].set_antialiased(False)
                    if self.pw_plotOptions_ck_2[i].isChecked() == True and self.pw_plotOptions_ln_2[i].text() != "":
                        line_opacity = str(self.pw_plotOptions_ln_2[i].text())
                        if "%" in line_opacity:
                            line_opacity = line_opacity[:-1]
                        line_opacity = float(line_opacity)/100
                        plt.axes().lines[i].set_alpha(line_opacity)
                    else:
                        line_opacity = plt.axes().lines[i].get_alpha()
                        if line_opacity:
                            plt.axes().lines[i].get_alpha(1)
                    if self.pw_plotOptions_ln_4[i].text() != "":
                        plt.axes().lines[i].set_label(str(self.pw_plotOptions_ln_4[i].text()))
                if self.pw_figureOptions_ck_2[0].isChecked(): 
                    plt.gca().legend().draggable()
            elif self.plot_type_str == "multiple":
                for i in range(self.option_num2):
                    args = {}
                    if self.pw_plotOptions_cb_1[i].currentText() != "" or self.pw_plotOptions_cb_1[i].currentText() != "Make a choice...":
                        try:
                            line_style = self.line_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
                            self.subplot_plot[i].axes.lines[0].set_linestyle(line_style)
                            self.subplot_plot[i].axes.lines[0].set_marker(None)
                            args["line"] = line_style
                        except KeyError:
                            line_style = self.marker_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
                            self.subplot_plot[i].axes.lines[0].set_marker(line_style)
                            self.subplot_plot[i].axes.lines[0].set_linestyle("None")
                            args["marker"] = line_style
                    if self.pw_plotOptions_cb_2[i].currentText() != "Make a choice..." and self.pw_plotOptions_ln_3[i].text() != "":
                        if str(self.pw_plotOptions_cb_2[i].currentText()) == "HEX Color":
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                        elif str(self.pw_plotOptions_cb_2[i].currentText()) == "RGB Color":
                            line_color = str(self.pw_plotOptions_ln_3[i].text())
                            line_color = line_color.replace(" ", "")
                            indexes = []
                            for index, item in enumerate(line_color):
                                if item == ",":
                                    indexes.append(index)
                            line_color = (float(float(line_color[0:indexes[0]])/255),
                                          float(float(line_color[indexes[0]+1:indexes[1]])/255),
                                          float(float(line_color[indexes[1]+1:])/255))
                        else:
                            line_color = self.colors_dict[str(self.pw_plotOptions_cb_2[i].currentText())]
                        self.subplot_plot[i].axes.lines[0].set_color(line_color)
                        args["color"] = line_color
                    if self.pw_plotOptions_ln_1[i].text() != "":
                        line_width = float(self.pw_plotOptions_ln_1[i].text())
                        self.subplot_plot[i].axes.lines[0].set_linewidth(line_width)
                        args["width"] = line_width
                    if self.pw_plotOptions_ck_1[i].isChecked() == True:
                        self.subplot_plot[i].axes.lines[0].set_antialiased(True)
                        args["antialiased"] = True
                    else:
                        self.subplot_plot[i].axes.lines[0].set_antialiased(False)
                        args["antialiased"] = False
                    if self.pw_plotOptions_ck_2[i].isChecked() == True and self.pw_plotOptions_ln_2[i].text() != "":
                        line_opacity = str(self.pw_plotOptions_ln_2[i].text())
                        if "%" in line_opacity:
                            line_opacity = line_opacity[:-1]
                        line_opacity = float(line_opacity)/100
                        self.subplot_plot[i].axes.lines[0].set_alpha(line_opacity)
                        args["opacity"] = line_opacity
                    else:
                        line_opacity = self.subplot_plot[i].axes.lines[0].get_alpha()
                        if line_opacity:
                            self.subplot_plot[i].axes.lines[0].set_alpha(1)
                            args["opacity"] = 1
                    if self.pw_plotOptions_ln_4[i].text() != "":
                        self.subplot_plot[i].axes.lines[0].set_label(str(self.pw_plotOptions_ln_4[i].text()))
                        args["label"] = str(self.pw_plotOptions_ln_4[i].text())
                    if self.pw_figureOptions_ck_2[i].isChecked(): 
                        self.subplot_plot[i].legend().draggable()
                    self.mult_line_option[i] = args
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
            label = self.findChild(QtGui.QLabel, str(self.sender().objectName() + "lb_" + str(self.sender().objectName()[22:])))
            label.setText(str(self.sender().value()) + "%")
    
    
    def get_file_name(self):
        file_dialog = QFileDialog()
        filter_types = "EPS Files (*.eps);;JPEG Files (*.jpg *.jpeg *.jpe);;PDF Files (*.pdf);;PNG Files (*.png *.pns);;TIFF Files (*.tif *.tiff)"
        out_file_name, out_file_ext = file_dialog.getSaveFileNameAndFilter(self, "Save File", "", filter_types)
        return str(out_file_name), str(out_file_ext)
    
    
class MyLog(QtGui.QDialog, Ui_Changelog):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.log_txBrower.setPlainText(open("doc/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()


class MyAbout(QtGui.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()