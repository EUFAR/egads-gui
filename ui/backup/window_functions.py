# -*- coding: utf-8 -*-

import copy
import logging
import egads.algorithms as algorithms
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget, QCursor
from PyQt4.QtCore import QObject, SIGNAL, pyqtSignature
from ui.Ui_globalattributewindow import Ui_globalAttributeWindow
from ui.Ui_variableattributewindow import Ui_variableAttributeWindow
from ui.Ui_processwindow import Ui_processingWindow
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_displaywindow import Ui_displayWindow
from ui.Ui_plotwindow import Ui_PlotWindow
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.axis as ax
import numpy


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
            for item in self.list_combobox_input:
                try:
                    for sublist in self.list_of_variables_and_attributes:
                        if sublist[1]["var_name"] == item.currentText():
                            args.append(sublist[3])
                            break
                except AttributeError:
                    args.append(float(item.text()))
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
                    
                    dimensions = "None"
                    
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
                
                dimensions = "None"
                
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
        
        
class PlotWindow(QtGui.QDialog, Ui_PlotWindow):
    def __init__(self, list_of_variables, list_of_new_variables):
        QWidget.__init__(self)
        self.setupUi(self)
        self.list_of_variables_and_attributes = list_of_variables + list_of_new_variables
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.pw_plot_fr.addWidget(self.canvas)
        self.navigation_toolbar = NavigationToolbar(self.canvas, self)
        self.navigation_toolbar.hide()
        self.list_label = []
        self.list_button = []
        self.list_horLayout = []
        self.list_plot = []
        self.opt_verlayout = []
        self.opt_horlayout_1 = []
        self.opt_horlayout_2 = []
        self.opt_horlayout_3 = []
        self.opt_horlayout_4 = []
        self.opt_horlayout_5 = []
        self.opt_horlayout_6 = []
        self.opt_horlayout_7 = []
        self.opt_horlayout_8 = []
        self.opt_horlayout_9 = []
        self.opt_label_1 = []
        self.opt_label_2 = []
        self.opt_label_3 = []
        self.opt_label_4 = []
        self.opt_label_5 = []
        self.opt_label_6 = []
        self.opt_line_1 = []
        self.opt_line_2 = []
        self.opt_line_3 = []
        self.opt_line_4 = []
        self.opt_line_5 = []
        self.opt_radio_1 = []
        self.opt_radio_2 = []
        self.opt_combobox_1 = []
        self.opt_combobox_2 = []
        self.opt_check_1 = []
        self.opt_check_2 = []
        self.opt_icon_1 = []
        self.opt_icon_2 = []
        self.opt_icon_3 = []
        self.opt_button_1 = []
        self.opt_button_2 = []
        self.opt_button_3 = []
        self.opt_button_4 = []
        self.opt_button_5 = []
        
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
        self.populate_comboboxes()
        self.pw_addbutton.clicked.connect(lambda: self.plot_variable())
        self.toolButton.clicked.connect(lambda: self.update_plot())
        logging.info("PlotWindow - window ready")


        '''self.opt_line_3.append(QtGui.QLineEdit())
        self.opt_line_3[self.variable_num].setMinimumSize(QtCore.QSize(50, 27))
        self.opt_line_3[self.variable_num].setMaximumSize(QtCore.QSize(50, 27))
        self.opt_line_3[self.variable_num].setFont(font)
        self.opt_line_3[self.variable_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.opt_line_3[self.variable_num].setObjectName(_fromUtf8("opt_line_3_" + str([self.variable_num])))
        self.opt_horlayout_9[self.variable_num].addWidget(self.opt_line_3[self.variable_num])'''


        '''self.opt_line_4.append(QtGui.QLineEdit())
        self.opt_line_4[self.variable_num].setMinimumSize(QtCore.QSize(120, 27))
        self.opt_line_4[self.variable_num].setMaximumSize(QtCore.QSize(120, 27))
        self.opt_line_4[self.variable_num].setFont(font)
        self.opt_line_4[self.variable_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.opt_line_4[self.variable_num].setObjectName(_fromUtf8("opt_line_4_" + str(self.variable_num)))
        self.opt_horlayout_4[self.variable_num].addWidget(self.opt_line_4[self.variable_num])'''

    @pyqtSignature("")
    def on_actionSave_as_triggered(self):
        self.plot_save()
    
    
    @pyqtSignature("")
    def on_actionPan_triggered(self):
        self.plot_pan()
    
    
    @pyqtSignature("")
    def on_actionZoom_triggered(self):
        self.plot_zoom()
    
    
    @pyqtSignature("")
    def on_actionOrigin_triggered(self):
        self.plot_home()
        
        
    @pyqtSignature("")
    def on_actionClear_triggered(self):
        self.plot_clear()
    
    
    @pyqtSignature("")
    def on_actionClose_triggered(self):
        self.close_window()   
    
    
    def close_window(self):
        self.close()
    
    
    def populate_comboboxes(self):
        logging.info("PlotWindow - populating combobox")
        self.pw_xvariable_rl.addItem("Make a choice...")
        for sublist in self.list_of_variables_and_attributes:
            self.pw_xvariable_rl.addItem(sublist[1]["var_name"])
        self.pw_yvariable_rl.addItem("Make a choice...")
        for sublist in self.list_of_variables_and_attributes:
            self.pw_yvariable_rl.addItem(sublist[1]["var_name"])
    
    
    def plot_variable(self):
        if self.pw_xvariable_rl.currentText() != "Make a choice..." and self.pw_yvariable_rl.currentText() != "Make a choice...":
            self.actionZoom.setEnabled(True)
            self.actionPan.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.actionOrigin.setEnabled(True)
            self.actionClear.setEnabled(True)
            self.pw_label_11.show()
            self.add_variable()
            logging.info("PlotWindow - ploting")
            xnan = ""
            ynan = ""
            for sublist in self.list_of_variables_and_attributes:
                if sublist[1]["var_name"] == self.pw_xvariable_rl.currentText():
                    logging.info("PlotWindow -               x: " + self.pw_xvariable_rl.currentText())
                    xvalue = copy.deepcopy(sublist[3].value)
                    xunits = copy.deepcopy(sublist[1]["units"])
                    xname = copy.deepcopy(sublist[1]["var_name"])
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
            plt.axes().lines[0].set_linestyle('--')
            plt.ylabel(yunits)
            plt.xlabel(xunits)
            plt.legend()
            self.canvas.draw()
            
            
            self.pw_ylabel_ln.setText((plt.axes().yaxis.get_label_text()))
            self.pw_xlabel_ln.setText((plt.axes().xaxis.get_label_text()))
            
            
    def add_variable(self):
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
        self.list_button[self.variable_num].clicked.connect(lambda: self.del_variable())
        self.list_horLayout[self.variable_num].addWidget(self.list_button[self.variable_num])
        self.list_horLayout[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.verticalLayout_3.addLayout(self.list_horLayout[self.variable_num])
        self.opt_verlayout.append(QtGui.QVBoxLayout())
        self.opt_verlayout[self.variable_num].setObjectName(_fromUtf8("opt_verlayout" + str(self.variable_num)))
        self.opt_horlayout_1.append(QtGui.QHBoxLayout())
        self.opt_horlayout_1[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_1_" + str(self.variable_num)))
        self.opt_verlayout[self.variable_num].addLayout(self.opt_horlayout_1[self.variable_num])
        self.opt_label_1.append(QtGui.QLabel())
        self.opt_label_1[self.variable_num].setMinimumSize(QtCore.QSize(120, 27))
        self.opt_label_1[self.variable_num].setMaximumSize(QtCore.QSize(120, 27))
        self.opt_label_1[self.variable_num].setFont(font2)
        self.opt_label_1[self.variable_num].setText("Plot options:")
        self.opt_label_1[self.variable_num].setObjectName(_fromUtf8("opt_label_1_" + str(self.variable_num)))
        self.opt_horlayout_1[self.variable_num].addWidget(self.opt_label_1[self.variable_num])
        self.opt_line_1.append(QtGui.QLineEdit())
        self.opt_line_1[self.variable_num].setMinimumSize(QtCore.QSize(270, 27))
        self.opt_line_1[self.variable_num].setMaximumSize(QtCore.QSize(270, 27))
        self.opt_line_1[self.variable_num].setFont(font)
        self.opt_line_1[self.variable_num].setText(self.pw_yvariable_rl.currentText())
        self.opt_line_1[self.variable_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.opt_line_1[self.variable_num].setReadOnly(True)
        self.opt_line_1[self.variable_num].setObjectName(_fromUtf8("opt_line_1_" + str(self.variable_num)))
        self.opt_horlayout_1[self.variable_num].addWidget(self.opt_line_1[self.variable_num])
        self.opt_horlayout_1[self.variable_num].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.opt_horlayout_2.append(QtGui.QHBoxLayout())
        self.opt_horlayout_2[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_2_" + str(self.variable_num)))
        self.opt_horlayout_2[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_verlayout[self.variable_num].addLayout(self.opt_horlayout_2[self.variable_num])
        self.opt_label_2.append(QtGui.QLabel())
        self.opt_label_2[self.variable_num].setMinimumSize(QtCore.QSize(80, 27))
        self.opt_label_2[self.variable_num].setMaximumSize(QtCore.QSize(80, 27))
        self.opt_label_2[self.variable_num].setFont(font)
        self.opt_label_2[self.variable_num].setText("Line style:")
        self.opt_label_2[self.variable_num].setObjectName(_fromUtf8("opt_label_2_" + str(self.variable_num)))
        self.opt_horlayout_2[self.variable_num].addWidget(self.opt_label_2[self.variable_num])
        self.opt_horlayout_3.append(QtGui.QHBoxLayout())
        self.opt_horlayout_3[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_3_" + str(self.variable_num)))
        self.opt_horlayout_2[self.variable_num].addLayout(self.opt_horlayout_3[self.variable_num])
        self.opt_radio_1.append(QtGui.QRadioButton())
        self.opt_radio_1[self.variable_num].setMinimumSize(QtCore.QSize(60, 27))
        self.opt_radio_1[self.variable_num].setMaximumSize(QtCore.QSize(60, 27))
        self.opt_radio_1[self.variable_num].setFont(font)
        self.opt_radio_1[self.variable_num].setText("Line")
        self.opt_radio_1[self.variable_num].setObjectName(_fromUtf8("opt_radio_1_" + str(self.variable_num)))
        self.opt_horlayout_3[self.variable_num].addWidget(self.opt_radio_1[self.variable_num])
        self.opt_radio_2.append(QtGui.QRadioButton())
        self.opt_radio_2[self.variable_num].setMinimumSize(QtCore.QSize(80, 27))
        self.opt_radio_2[self.variable_num].setMaximumSize(QtCore.QSize(80, 27))
        self.opt_radio_2[self.variable_num].setFont(font)
        self.opt_radio_2[self.variable_num].setText("Marker")
        self.opt_radio_2[self.variable_num].setObjectName(_fromUtf8("opt_radio_2_" + str(self.variable_num)))
        self.opt_horlayout_3[self.variable_num].addWidget(self.opt_radio_2[self.variable_num])
        self.opt_horlayout_2[self.variable_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_icon_1.append(QtGui.QLabel())
        self.opt_icon_1[self.variable_num].setMinimumSize(QtCore.QSize(15, 10))
        self.opt_icon_1[self.variable_num].setMaximumSize(QtCore.QSize(15, 10))
        self.opt_icon_1[self.variable_num].setPixmap(QtGui.QPixmap(_fromUtf8("icons/fwd_arrow.png")))
        self.opt_icon_1[self.variable_num].setScaledContents(True)
        self.opt_icon_1[self.variable_num].setObjectName(_fromUtf8("opt_icon_1_" + str(self.variable_num)))
        self.opt_horlayout_2[self.variable_num].addWidget(self.opt_icon_1[self.variable_num])
        self.opt_horlayout_2[self.variable_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_combobox_1.append(QtGui.QComboBox())
        self.opt_combobox_1[self.variable_num].setMinimumSize(QtCore.QSize(180, 27))
        self.opt_combobox_1[self.variable_num].setMaximumSize(QtCore.QSize(180, 27))
        self.opt_combobox_1[self.variable_num].setFont(font)
        self.opt_combobox_1[self.variable_num].setEnabled(False)
        self.opt_combobox_1[self.variable_num].setObjectName(_fromUtf8("opt_combobox_1_" + str(self.variable_num)))
        self.opt_combobox_1[self.variable_num].setStyleSheet(_fromUtf8("QComboBox {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color: rgb(200, 200, 200);\n"
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
        self.opt_horlayout_2[self.variable_num].addWidget(self.opt_combobox_1[self.variable_num])
        self.opt_button_1.append(QtGui.QToolButton())
        self.opt_button_1[self.variable_num].setMinimumSize(QtCore.QSize(27, 27))
        self.opt_button_1[self.variable_num].setMaximumSize(QtCore.QSize(27, 27))
        self.opt_button_1[self.variable_num].setText(_fromUtf8(""))
        self.opt_button_1[self.variable_num].setIcon(icon2)
        self.opt_button_1[self.variable_num].setIconSize(QtCore.QSize(27, 27))
        self.opt_button_1[self.variable_num].setPopupMode(QtGui.QToolButton.InstantPopup) 
        self.opt_button_1[self.variable_num].setAutoRaise(True)
        self.opt_button_1[self.variable_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
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
        self.opt_button_1[self.variable_num].setObjectName("opt_button_1_" + str(self.variable_num))
        self.opt_horlayout_2[self.variable_num].addWidget(self.opt_button_1[self.variable_num])
        self.opt_horlayout_2[self.variable_num].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.opt_horlayout_5.append(QtGui.QHBoxLayout())
        self.opt_horlayout_5[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_5_" + str(self.variable_num)))
        self.opt_horlayout_5[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_verlayout[self.variable_num].addLayout(self.opt_horlayout_5[self.variable_num])
        self.opt_label_3.append(QtGui.QLabel())
        self.opt_label_3[self.variable_num].setMinimumSize(QtCore.QSize(190, 27))
        self.opt_label_3[self.variable_num].setMaximumSize(QtCore.QSize(190, 27))
        self.opt_label_3[self.variable_num].setFont(font)
        self.opt_label_3[self.variable_num].setText("Line / Marker color:")
        self.opt_label_3[self.variable_num].setObjectName(_fromUtf8("opt_label_3_" + str(self.variable_num)))
        self.opt_horlayout_5[self.variable_num].addWidget(self.opt_label_3[self.variable_num])
        self.opt_combobox_2.append(QtGui.QComboBox())
        self.opt_combobox_2[self.variable_num].setMinimumSize(QtCore.QSize(160, 27))
        self.opt_combobox_2[self.variable_num].setMaximumSize(QtCore.QSize(160, 27))
        self.opt_combobox_2[self.variable_num].setFont(font)
        self.opt_combobox_2[self.variable_num].setEnabled(True)
        self.opt_combobox_2[self.variable_num].setObjectName(_fromUtf8("opt_combobox_2_" + str(self.variable_num)))
        self.opt_combobox_2[self.variable_num].setStyleSheet(_fromUtf8("QComboBox {\n"
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
        self.opt_horlayout_5[self.variable_num].addWidget(self.opt_combobox_2[self.variable_num])
        self.opt_button_2.append(QtGui.QToolButton())
        self.opt_button_2[self.variable_num].setMinimumSize(QtCore.QSize(27, 27))
        self.opt_button_2[self.variable_num].setMaximumSize(QtCore.QSize(27, 27))
        self.opt_button_2[self.variable_num].setText(_fromUtf8(""))
        self.opt_button_2[self.variable_num].setIcon(icon2)
        self.opt_button_2[self.variable_num].setIconSize(QtCore.QSize(27, 27))
        self.opt_button_2[self.variable_num].setPopupMode(QtGui.QToolButton.InstantPopup) 
        self.opt_button_2[self.variable_num].setAutoRaise(True)
        self.opt_button_2[self.variable_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
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
        self.opt_button_2[self.variable_num].setObjectName("opt_button_2_" + str(self.variable_num))
        self.opt_horlayout_5[self.variable_num].addWidget(self.opt_button_2[self.variable_num])
        self.opt_horlayout_5[self.variable_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_icon_2.append(QtGui.QLabel())
        self.opt_icon_2[self.variable_num].setMinimumSize(QtCore.QSize(15, 10))
        self.opt_icon_2[self.variable_num].setMaximumSize(QtCore.QSize(15, 10))
        self.opt_icon_2[self.variable_num].setPixmap(QtGui.QPixmap(_fromUtf8("icons/fwd_arrow.png")))
        self.opt_icon_2[self.variable_num].setScaledContents(True)
        self.opt_icon_2[self.variable_num].hide()
        self.opt_icon_2[self.variable_num].setObjectName(_fromUtf8("opt_icon_2_" + str(self.variable_num)))
        self.opt_horlayout_5[self.variable_num].addWidget(self.opt_icon_2[self.variable_num])
        self.opt_horlayout_5[self.variable_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_horlayout_4.append(QtGui.QHBoxLayout())
        self.opt_horlayout_4[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_4_" + str(self.variable_num)))
        
        self.opt_line_4.append(QtGui.QLineEdit())
        self.opt_line_4[self.variable_num].setMinimumSize(QtCore.QSize(120, 27))
        self.opt_line_4[self.variable_num].setMaximumSize(QtCore.QSize(120, 27))
        self.opt_line_4[self.variable_num].setFont(font)
        self.opt_line_4[self.variable_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.opt_line_4[self.variable_num].setObjectName(_fromUtf8("opt_line_4_" + str(self.variable_num)))
        self.opt_line_4[self.variable_num].hide()
        self.opt_horlayout_4[self.variable_num].addWidget(self.opt_line_4[self.variable_num])
        
        self.opt_horlayout_5[self.variable_num].addLayout(self.opt_horlayout_4[self.variable_num])
        self.opt_horlayout_5[self.variable_num].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.opt_horlayout_6.append(QtGui.QHBoxLayout())
        self.opt_horlayout_6[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_6_" + str(self.variable_num)))
        self.opt_horlayout_6[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_verlayout[self.variable_num].addLayout(self.opt_horlayout_6[self.variable_num])
        self.opt_label_4.append(QtGui.QLabel())
        self.opt_label_4[self.variable_num].setMinimumSize(QtCore.QSize(190, 27))
        self.opt_label_4[self.variable_num].setMaximumSize(QtCore.QSize(190, 27))
        self.opt_label_4[self.variable_num].setFont(font)
        self.opt_label_4[self.variable_num].setText("Line width / Marker size:")
        self.opt_label_4[self.variable_num].setObjectName(_fromUtf8("opt_label_4_" + str(self.variable_num)))
        self.opt_horlayout_6[self.variable_num].addWidget(self.opt_label_4[self.variable_num])
        self.opt_line_2.append(QtGui.QLineEdit())
        self.opt_line_2[self.variable_num].setMinimumSize(QtCore.QSize(160, 27))
        self.opt_line_2[self.variable_num].setMaximumSize(QtCore.QSize(160, 27))
        self.opt_line_2[self.variable_num].setFont(font)
        self.opt_line_2[self.variable_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "   padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}"))
        self.opt_line_2[self.variable_num].setObjectName(_fromUtf8("opt_line_2_" + str(self.variable_num)))
        self.opt_horlayout_6[self.variable_num].addWidget(self.opt_line_2[self.variable_num])
        self.opt_button_3.append(QtGui.QToolButton())
        self.opt_button_3[self.variable_num].setMinimumSize(QtCore.QSize(27, 27))
        self.opt_button_3[self.variable_num].setMaximumSize(QtCore.QSize(27, 27))
        self.opt_button_3[self.variable_num].setText(_fromUtf8(""))
        self.opt_button_3[self.variable_num].setIcon(icon2)
        self.opt_button_3[self.variable_num].setIconSize(QtCore.QSize(27, 27))
        self.opt_button_3[self.variable_num].setPopupMode(QtGui.QToolButton.InstantPopup) 
        self.opt_button_3[self.variable_num].setAutoRaise(True)
        self.opt_button_3[self.variable_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
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
        self.opt_button_3[self.variable_num].setObjectName("opt_button_3_" + str(self.variable_num))
        self.opt_horlayout_6[self.variable_num].addWidget(self.opt_button_3[self.variable_num])
        self.opt_horlayout_6[self.variable_num].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.opt_horlayout_7.append(QtGui.QHBoxLayout())
        self.opt_horlayout_7[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_7_" + str(self.variable_num)))
        self.opt_horlayout_7[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_verlayout[self.variable_num].addLayout(self.opt_horlayout_7[self.variable_num])
        self.opt_label_5.append(QtGui.QLabel())
        self.opt_label_5[self.variable_num].setMinimumSize(QtCore.QSize(100, 27))
        self.opt_label_5[self.variable_num].setMaximumSize(QtCore.QSize(100, 27))
        self.opt_label_5[self.variable_num].setFont(font)
        self.opt_label_5[self.variable_num].setText("Antialiased ?")
        self.opt_label_5[self.variable_num].setObjectName(_fromUtf8("opt_label_5_" + str(self.variable_num)))
        self.opt_horlayout_7[self.variable_num].addWidget(self.opt_label_5[self.variable_num])
        self.opt_check_1.append(QtGui.QCheckBox())
        self.opt_check_1[self.variable_num].setMinimumSize(QtCore.QSize(20, 20))
        self.opt_check_1[self.variable_num].setMaximumSize(QtCore.QSize(20, 20))
        self.opt_check_1[self.variable_num].setText(_fromUtf8(""))
        self.opt_check_1[self.variable_num].setObjectName(_fromUtf8("opt_check_1_" + str(self.variable_num)))
        self.opt_horlayout_7[self.variable_num].addWidget(self.opt_check_1[self.variable_num])
        self.opt_button_4.append(QtGui.QToolButton())
        self.opt_button_4[self.variable_num].setMinimumSize(QtCore.QSize(27, 27))
        self.opt_button_4[self.variable_num].setMaximumSize(QtCore.QSize(27, 27))
        self.opt_button_4[self.variable_num].setText(_fromUtf8(""))
        self.opt_button_4[self.variable_num].setIcon(icon2)
        self.opt_button_4[self.variable_num].setIconSize(QtCore.QSize(27, 27))
        self.opt_button_4[self.variable_num].setPopupMode(QtGui.QToolButton.InstantPopup) 
        self.opt_button_4[self.variable_num].setAutoRaise(True)
        self.opt_button_4[self.variable_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
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
        self.opt_button_4[self.variable_num].setObjectName("opt_button_4_" + str(self.variable_num))
        self.opt_horlayout_7[self.variable_num].addWidget(self.opt_button_4[self.variable_num])
        self.opt_horlayout_7[self.variable_num].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.opt_horlayout_8.append(QtGui.QHBoxLayout())
        self.opt_horlayout_8[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_8_" + str(self.variable_num)))
        self.opt_horlayout_8[self.variable_num].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        self.opt_verlayout[self.variable_num].addLayout(self.opt_horlayout_8[self.variable_num])
        self.opt_label_6.append(QtGui.QLabel())
        self.opt_label_6[self.variable_num].setMinimumSize(QtCore.QSize(100, 27))
        self.opt_label_6[self.variable_num].setMaximumSize(QtCore.QSize(100, 27))
        self.opt_label_6[self.variable_num].setFont(font)
        self.opt_label_6[self.variable_num].setText("Opacity ?")
        self.opt_label_6[self.variable_num].setObjectName(_fromUtf8("opt_label_6_" + str(self.variable_num)))
        self.opt_horlayout_8[self.variable_num].addWidget(self.opt_label_6[self.variable_num])
        self.opt_check_2.append(QtGui.QCheckBox())
        self.opt_check_2[self.variable_num].setMinimumSize(QtCore.QSize(20, 20))
        self.opt_check_2[self.variable_num].setMaximumSize(QtCore.QSize(20, 20))
        self.opt_check_2[self.variable_num].setText(_fromUtf8(""))
        self.opt_check_2[self.variable_num].setObjectName(_fromUtf8("opt_check_2_" + str(self.variable_num)))
        self.opt_horlayout_8[self.variable_num].addWidget(self.opt_check_2[self.variable_num])
        self.opt_button_5.append(QtGui.QToolButton())
        self.opt_button_5[self.variable_num].setMinimumSize(QtCore.QSize(27, 27))
        self.opt_button_5[self.variable_num].setMaximumSize(QtCore.QSize(27, 27))
        self.opt_button_5[self.variable_num].setText(_fromUtf8(""))
        self.opt_button_5[self.variable_num].setIcon(icon2)
        self.opt_button_5[self.variable_num].setIconSize(QtCore.QSize(27, 27))
        self.opt_button_5[self.variable_num].setPopupMode(QtGui.QToolButton.InstantPopup) 
        self.opt_button_5[self.variable_num].setAutoRaise(True)
        self.opt_button_5[self.variable_num].setStyleSheet(_fromUtf8("QToolButton:hover {\n"
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
        self.opt_button_5[self.variable_num].setObjectName("opt_button_5_" + str(self.variable_num))
        self.opt_horlayout_8[self.variable_num].addWidget(self.opt_button_5[self.variable_num])
        
        self.opt_horlayout_8[self.variable_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        
        self.opt_icon_3.append(QtGui.QLabel())
        self.opt_icon_3[self.variable_num].setMinimumSize(QtCore.QSize(15, 10))
        self.opt_icon_3[self.variable_num].setMaximumSize(QtCore.QSize(15, 10))
        self.opt_icon_3[self.variable_num].setPixmap(QtGui.QPixmap(_fromUtf8("icons/fwd_arrow.png")))
        self.opt_icon_3[self.variable_num].setScaledContents(True)
        self.opt_icon_3[self.variable_num].hide()
        self.opt_icon_3[self.variable_num].setObjectName(_fromUtf8("opt_icon_3_" + str(self.variable_num)))
        self.opt_horlayout_8[self.variable_num].addWidget(self.opt_icon_3[self.variable_num])
        
        self.opt_horlayout_8[self.variable_num].addItem(QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum))
        
        self.opt_horlayout_9.append(QtGui.QHBoxLayout())
        self.opt_horlayout_9[self.variable_num].setObjectName(_fromUtf8("opt_horlayout_9_" + str(self.variable_num)))
        
        self.opt_line_5.append(QtGui.QLineEdit())
        self.opt_line_5[self.variable_num].setMinimumSize(QtCore.QSize(120, 27))
        self.opt_line_5[self.variable_num].setMaximumSize(QtCore.QSize(120, 27))
        self.opt_line_5[self.variable_num].setFont(font)
        self.opt_line_5[self.variable_num].setStyleSheet(_fromUtf8("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "}"))
        self.opt_line_5[self.variable_num].setObjectName(_fromUtf8("opt_line_5_" + str(self.variable_num)))
        self.opt_line_5[self.variable_num].hide()
        self.opt_horlayout_9[self.variable_num].addWidget(self.opt_line_5[self.variable_num])
        
        self.opt_horlayout_8[self.variable_num].addLayout(self.opt_horlayout_9[self.variable_num])
        self.opt_horlayout_8[self.variable_num].addItem(QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.opt_verlayout[self.variable_num].addItem(QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed))
        self.verticalLayout_7.addLayout(self.opt_verlayout[self.variable_num])
        self.opt_radio_1[self.variable_num].clicked.connect(lambda: self.line_style())
        self.opt_radio_2[self.variable_num].clicked.connect(lambda: self.line_style())
        self.populate_colorbox()
        self.opt_combobox_2[self.variable_num].activated.connect(lambda: self.line_color())
        self.opt_check_2[self.variable_num].clicked.connect(lambda: self.line_opacity())
        
        self.variable_num += 1
        logging.info("PlotWindow - variable added")
        
        
    def del_variable(self, index = None):
        logging.info("PlotWindow - deleting variable")
        if index == None:
            index = int(self.sender().objectName()[12:])
        logging.info("PlotWindow -               " + self.list_label[index].text())
        plt.axes().lines[index].remove()
        self.canvas.draw()
        self.list_label[index].deleteLater()
        self.list_label.pop(index)
        self.list_button[index].deleteLater()
        self.list_button.pop(index)
        self.list_horLayout[index].deleteLater()
        self.list_horLayout.pop(index)
        self.variable_num -= 1
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
        logging.info("PlotWindow - variable deleted")
        
    
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
        self.navigation_toolbar.save_figure()
        
    
    def plot_clear(self):
        
        
        
        #print dir(plt.axes().lines[0])
        
        
        
        #print ax.XAxis().get_label()
        
        print plt.axes().xaxis.get_label_text()
        
        for i in reversed(range(0, len(self.list_horLayout))):
            self.del_variable(i)
        plt.clf()
        self.canvas.draw()
    
    
    def populate_colorbox(self):
        self.opt_combobox_2[self.variable_num].addItem("Make a choice...")
        for i in self.colors:
            self.opt_combobox_2[self.variable_num].addItem(i)
    
    
    def line_style(self):
        index = int(self.sender().objectName()[12:])
        self.opt_combobox_1[index].setEnabled(True)
        if "opt_radio_1" in self.sender().objectName() and self.sender().isChecked() == True:
            self.opt_combobox_1[index].clear()
            self.opt_combobox_1[index].addItem("Make a choice...")
            for item in self.line_styles:
                self.opt_combobox_1[index].addItem(item)
        elif "opt_radio_2" in self.sender().objectName() and self.sender().isChecked() == True:
            self.opt_combobox_1[index].clear()
            self.opt_combobox_1[index].addItem("Make a choice...")
            for item in self.marker_styles:
                self.opt_combobox_1[index].addItem(item)
    
    def line_color(self):
        if self.sender().currentText() == "HEX Color" or self.sender().currentText() == "RGB Color":
            index = int(self.sender().objectName()[15:])
            self.opt_line_4[index].show()
            self.opt_icon_2[index].show()
        else:
            index = int(self.sender().objectName()[15:])
            self.opt_line_4[index].hide()
            self.opt_line_4[index].setText("")
            self.opt_icon_2[index].hide()
    
    
    def line_opacity(self):
        if self.sender().isChecked() == True:
            index = int(self.sender().objectName()[12:])
            self.opt_line_5[index].show()
            self.opt_icon_3[index].show()
        else:
            index = int(self.sender().objectName()[12:])
            self.opt_line_5[index].hide()
            self.opt_line_5[index].setText("")
            self.opt_icon_3[index].hide()

    
    def update_plot(self):
        return
