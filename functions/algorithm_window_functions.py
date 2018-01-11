# -*- coding: utf-8 -*-

import logging
import egads
import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_processwindow import Ui_processingWindow
from ui.Ui_creationwindow import Ui_creationWindow
from ui.Ui_displayalgorithmwindow import Ui_displayAlgorithmWindow
from functions.other_window_functions import MyCategory
from functions.other_window_functions import MyFilename
from functions.other_window_functions import MyUnit
from functions.other_window_functions import MyFill
from functions.other_window_functions import MyInfo
from functions import syntax_function
              
                
class MyProcessing(QtWidgets.QDialog, Ui_processingWindow):
    def __init__(self, list_of_algorithms, list_of_variables_and_attributes, list_of_new_variables_and_attributes):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.aw_combobox_1.setItemDelegate(itemDelegate)
        self.aw_combobox_2.setItemDelegate(itemDelegate)
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
        logging.info('gui - algorithm_window_functions.py - MyProcessing ready')

    
    def close_window(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - close_window')
        del(self.list_of_variables_and_attributes)
        del(self.list_of_new_variables_and_attributes)
        self.close()
    
    
    def close_window_save(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - close_window_save : algorithm '
                      + self.algorithm().metadata["Processor"])
        try:
            args = []
            for index, item in enumerate(self.list_combobox_input):
                try:
                    sublist = self.list_of_variables_and_attributes[item.currentText()]
                    args.append(sublist[3])
                    if index == 0:
                        dimension_out = sublist[2]
                except AttributeError:
                    try:
                        args.append(float(item.text()))
                    except ValueError:
                        args.append(str(item.text()))
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
                try:
                    metadata["_FillValue"] = self.list_of_variables_and_attributes[self.list_combobox_input[0].currentText()][1]["_FillValue"]
                except KeyError:
                    pass
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
            logging.exception('gui - algorithm_window_functions.py - MyProcessing - close_window_save : an exception occured')
        

    def populate_combobox_1(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - populate_combobox_1')
        self.aw_combobox_1.addItem("Make a choice...")
        folder_list = []
        for key, _ in self.list_of_algorithms.iteritems():
            folder_list.append(key.title())
        folder_list = sorted(folder_list)
        self.aw_combobox_1.addItems(folder_list)
            
    
    def populate_combobox_2(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - populate_combobox_2')
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
    
    
    def populate_input_output(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - populate_input_output : tabWidget.currentIndex()'
        + str(self.tabWidget.currentIndex()) + ', algorithm ' + str(self.aw_combobox_2.currentText()))
        if self.aw_combobox_2.currentText() != "Make a choice..." and self.aw_combobox_2.currentText() !="" :
            if self.tabWidget.currentIndex() == 1:
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
                            itemDelegate = QtWidgets.QStyledItemDelegate()
                            self.list_combobox_input[self.input_num].setItemDelegate(itemDelegate)
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
                            self.list_combobox_input[self.input_num].setObjectName("list_combobox_input_" + str(self.input_num))
                            self.list_combobox_input[self.input_num].addItem("Make a choice...")
                            variable_list = []
                            for _, sublist in self.list_of_variables_and_attributes.items():
                                if self.algorithm().metadata["InputTypes"][index] in self.types_for_combobox:
                                    if sublist[2] != 'deleted':
                                        variable_list.append(sublist[1]["var_name"])
                                else:
                                    if "time" in sublist[1]["var_name"]:
                                        if sublist[2] != 'deleted':
                                            variable_list.append(sublist[1]["var_name"])
                            self.list_combobox_input[self.input_num].addItems(sorted(variable_list))
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
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - prepare_layout')
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
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - clear_layout')
        for i in reversed(range(layout.count())):   
            item = layout.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QtGui.QLayout):
                self.clear_layout(item.layout())
            layout.removeItem(item)               
    
    
    def hide_algorithm_information(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - hide_algorithm_information')
        self.aw_label_4.hide()
        self.aw_label_5.hide()
        self.aw_textbrowser_1.hide()
        self.aw_textbrowser_2.hide()
        
        
    def load_algorithm_information(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - load_algorithm_information : algorithm '
                      + str(self.aw_combobox_2.currentText()))
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
                logging.exception('gui - algorithm_window_functions.py - MyProcessing - load_algorithm_information : no description')
                pass
            try:
                purpose_string = '<p align="justify">' + str(self.algorithm().metadata["Purpose"]) + '</p>'
                self.aw_textbrowser_1.setHtml(purpose_string)
            except KeyError:
                logging.exception('gui - algorithm_window_functions.py - MyProcessing - load_algorithm_information : no purpose')
                pass

    
    def activate_save_button(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - activate_save_button')
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
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - activate_save_button : aw_okButton.isEnabled() '
                      + str(self.aw_okButton.isEnabled()))
    
    
    def information_button(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - information_button : sender().objectName() '
                      + str(self.sender().objectName()))
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
        
  
class MyAlgorithm(QtWidgets.QDialog, Ui_creationWindow):
    def __init__(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.cw_combobox_1.setItemDelegate(itemDelegate)
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
            if folder[0][index + 5:] and folder[0][index + 5:] != 'file_templates':
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
        
        #self.unit_window_test()
        logging.info('gui - algorithm_window_functions.py - MyAlgorithm -  ready')
        
        
    def unit_window_test(self):
        self.add_input()
        #self.add_input()
        self.add_output()
        self.cw_input_ln_1[0].setText('var')
        self.cw_input_ln_2[0].setText('')
        self.cw_input_ln_3[0].setText('vector')
        self.cw_input_ln_4[0].setText('une premiere variable de test')
        '''self.cw_input_ln_1[1].setText('B')
        self.cw_input_ln_2[1].setText('m*s^2')
        self.cw_input_ln_3[1].setText('vector')
        self.cw_input_ln_4[1].setText('une deuxieme variable de test')'''
        self.cw_output_ln_1[0].setText('res')
        self.cw_output_ln_2[0].setText('input0 corr')
        self.cw_output_ln_3[0].setText('input0')
        self.cw_output_ln_4[0].setText('input0 corr')
        self.cw_output_ln_5[0].setText('une troisieme variable de test')
        self.cw_output_ln_6[0].setText('vector')
        self.cw_output_lw_1[0].addItem('Aircraft State')
        self.cw_line_1.setText('MyAlgorithmForCorrection')
        self.cw_line_3.setText('no sources')
        self.cw_line_2.setText('Myself')
        self.cw_line_4.setText('Myself')
        self.cw_plain_2.setPlainText('To help developping algorithm creation window')
        self.cw_plain_1.setPlainText('To help developping algorithm creation window')
        self.listWidget.addItem('Corrections')
        self.cw_plain_4.setPlainText('res = var / 3.45\nreturn res')
        
        
    def add_input(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - add_input')
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - add_output')
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
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.cw_output_cb_1[self.output_num].setItemDelegate(itemDelegate)
        self.cw_output_cb_1[self.output_num].setMinimumSize(QtCore.QSize(160, 27))
        self.cw_output_cb_1[self.output_num].setMaximumSize(QtCore.QSize(160, 27))
        self.cw_output_cb_1[self.output_num].setFont(font2)
        self.cw_output_cb_1[self.output_num].setStyleSheet("QComboBox {\n"
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - del_input : index ' + str(index)
                      + ', sender().objectName() ' + str(self.sender().objectName()))
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - del_output : index ' + str(index)
                      + ', sender().objectName() ' + str(self.sender().objectName()))
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - add_category : algorithm ' + str(algorithm))
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - remove_category : algorithm ' + str(algorithm))
        if not algorithm:
            index = int(self.sender().objectName()[15:])
            self.cw_output_lw_1[index].takeItem(self.cw_output_lw_1[index].currentRow())
        else:
            self.listWidget.takeItem(self.listWidget.currentRow())
    
    
    def prepare_units_validation(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_units_validation')
        cancel = self.check_all_fields()
        if cancel == True:
            return
        units_list = self.validate_units()
        if units_list:
            self.unitWindow = MyUnit(self.validate_units())
            x1, y1, w1, h1 = self.geometry().getRect()
            x2, y2, w2, h2 = self.unitWindow.geometry().getRect()
            self.unitWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
            self.unitWindow.setMinimumSize(QtCore.QSize(550, self.unitWindow.sizeHint().height()))
            self.unitWindow.setMaximumSize(QtCore.QSize(550, self.unitWindow.sizeHint().height()))
            if self.unitWindow.exec_():
                self.prepare_algorithm()
        else:
            self.prepare_algorithm()
    
    
    def prepare_algorithm(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_algorithm')
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
                date = '__date__ = "' + self.egads_algorithm_datestring() + '"\n'
                version = '__version__ = "1.0"\n'
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
                            + '    VERSION     1.0\n'
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
                complete_string = (author + date + version + all + alg_imports + alg_class + alg_help
                                   + alg_init + alg_out_metadata + alg_metadata + alg_run + algorithm)
                try:
                    self.write_algorithm(filename, complete_string, category, str(self.cw_line_2.text()))
                    self.success = True
                except Exception:
                    logging.exception('gui - algorithm_window_functions.py - MyAlgorithm - prepare_algorithm : an exception'
                                      + ' occured when writing the algorithm file.')
                    self.success = False
                self.algorithm_filename = filename
                self.algorithm_category = category
                self.algorithm_name = str(self.cw_line_1.text())
                self.close()
            
            
    def write_algorithm(self, filename, string, category, author):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - write_algorithm : filename '
                      + str(filename) + ', category' + str(category) + ', author ' + str(author)
                      + ', string ' + str(string))
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
                           + "    logging.info('egads [user/" + category + "] algorithms have been loaded')\n"
                           + 'except Exception:\n'
                           + "    logging.error('an error occured during the loading of a [user/" + category + "] algorithm')\n")
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - egads_algorithm_datestring')
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        hour = str(datetime.datetime.now().hour)
        minute = str(datetime.datetime.now().minute)
        date_string = year + '-' + month + '-' + day + ' ' + hour + ':' + minute
        return date_string
    
    
    def prepare_long_string(self, string, length, space_num):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_long_string')
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_inputs')
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_outputs')
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_algorithm_metadata')
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
            if self.cw_input_ln_2[i].text():
                input_units += "'" + str(self.cw_input_ln_2[i].text()) + "',"
            else:
                input_units += "None,"
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
                       +
                       
                       
                       
                       
                       
                       + "                                                          'Processor':self.name,\n"
                       + "                                                          'ProcessorDate':__date__,\n"
                       + "                                                          'ProcessorVersion':__version__,\n"
                       + "                                                          'DateProcessed':self.now()},\n"
                       + "                                                          self.output_metadata)\n\n")
        return metadata_string

    
    def prepare_output_metadata(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_output_metadata')
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
                
                ##########################
                #
                # temporaire
                #
                ##########################
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
                
            ##########################
            #
            # temporaire
            #
            #########################
            output_string += ("        self.output_metadata = egads_metadata.VariableMetadata({"
                                  + "'units':'" + units + "',\n"
                                  + ' ' * 63 + "'long_name':'" + long_name + "',\n"
                                  + ' ' * 63 + "'standard_name':'" + standard_name + "',\n"
                                  + ' ' * 63 + "'Category':" + category + "})\n\n")
            
        return output_string
    
    
    def prepare_algorithm_run(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_algorithm_run')
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - prepare_algorithm_text')
        algorithm_string = ''
        if self.cw_plain_4.toPlainText():
            algorithm = ' ' * 8 + str(self.cw_plain_4.toPlainText())
            algorithm_string = algorithm.replace('\n', '\n        ')
            algorithm_string += '\n'
        return algorithm_string
    
    
    def check_string_max_length(self, string_list):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - check_string_max_length')
        max_length = 0
        for string in string_list:
            if len(string) > max_length:
                max_length = len(string)
        return max_length
    
    
    def check_all_fields(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - check_all_fields')
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
            result = self.fillWindow.cancel
        else:
            result = False
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - check_all_fields : result ' + str(result))
        return result
    
    
    def validate_units(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - validate_units')
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
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - closeWindow')
        self.close()


class MyAlgorithmDisplay(QtWidgets.QDialog, Ui_displayAlgorithmWindow):
    def __init__(self, algorithm_dict):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithmDisplay - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.algorithm_dict = algorithm_dict
        self.daw_okButton.clicked.connect(self.closeWindow)
        self.input_grid_lay = []
        self.input_hor_lay_1 = []
        self.input_hor_lay_2 = []
        self.input_label_1 = []
        self.input_label_2 = []
        self.input_label_3 = []
        self.input_label_4 = []
        self.input_edit_1 = []
        self.input_edit_2 = []
        self.input_edit_3 = []
        self.input_plain_1 = []
        self.input_line = []
        self.input_num = 0
        self.output_grid_lay = []
        self.output_hor_lay_1 = []
        self.output_hor_lay_2 = []
        self.output_hor_lay_3 = []
        self.output_label_1 = []
        self.output_label_2 = []
        self.output_label_3 = []
        self.output_label_4 = []
        self.output_label_5 = []
        self.output_label_6 = []
        self.output_label_7 = []
        self.output_edit_1 = []
        self.output_edit_2 = []
        self.output_edit_3 = []
        self.output_edit_4 = []
        self.output_edit_5 = []
        self.output_edit_6 = []
        self.output_plain_1 = []
        self.output_line = []
        self.output_num = 0
        self.parse_algorithm_dict()
        
    def parse_algorithm_dict(self):
        x = syntax_function.PythonHighlighter(self.daw_plain_5.document())
        self.daw_plain_5.setPlainText(self.algorithm_dict['Algorithm'])
        self.daw_line_1.setText(self.algorithm_dict['Name'])
        self.daw_line_2.setText(self.algorithm_dict['Date'])
        self.daw_line_3.setText(self.algorithm_dict['Version'])
        self.daw_plain_1.setPlainText(self.algorithm_dict['Purpose'])
        self.daw_plain_2.setPlainText(self.algorithm_dict['Description'])
        self.daw_plain_3.setPlainText(self.algorithm_dict['Source'])
        self.daw_plain_3.setPlainText(self.algorithm_dict['References'])
        for input in self.algorithm_dict['Input']:
            self.create_input(input)
            
        for output in self.algorithm_dict['Output']:
            self.create_output(output) 
        
    def create_input(self, input_dict):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        if self.input_num > 0:
            self.verticalLayout_2.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
            self.input_line.append(QtWidgets.QFrame())
            self.input_line[self.input_num].setFrameShape(QtWidgets.QFrame.HLine)
            self.input_line[self.input_num].setFrameShadow(QtWidgets.QFrame.Sunken)
            self.input_line[self.input_num].setObjectName("input_line_" + str(self.input_num))
            self.verticalLayout_2.addWidget(self.input_line[self.input_num])
            self.verticalLayout_2.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        else:
            self.input_line.append(None)
        self.input_hor_lay_1.append(QtWidgets.QHBoxLayout())
        self.input_hor_lay_1[self.input_num].setObjectName('input_hor_lay_1_' + str(self.input_num))
        self.input_grid_lay.append(QtWidgets.QGridLayout())
        self.input_grid_lay[self.input_num].setObjectName('input_grid_lay_' + str(self.input_num))
        self.input_hor_lay_1[self.input_num].addLayout(self.input_grid_lay[self.input_num])
        self.input_hor_lay_1[self.input_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.input_label_1.append(QtWidgets.QLabel())
        self.input_label_1[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.input_label_1[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.input_label_1[self.input_num].setFont(font)
        self.input_label_1[self.input_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.input_label_1[self.input_num].setText("Symbol:")
        self.input_label_1[self.input_num].setObjectName("input_label_1_" + str(self.input_num))
        self.input_grid_lay[self.input_num].addWidget(self.input_label_1[self.input_num], 0, 0, 1, 1)
        self.input_label_2.append(QtWidgets.QLabel())
        self.input_label_2[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.input_label_2[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.input_label_2[self.input_num].setFont(font)
        self.input_label_2[self.input_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.input_label_2[self.input_num].setText("Units:")
        self.input_label_2[self.input_num].setObjectName("input_label_2_" + str(self.input_num))
        self.input_grid_lay[self.input_num].addWidget(self.input_label_2[self.input_num], 1, 0, 1, 1)
        self.input_label_3.append(QtWidgets.QLabel())
        self.input_label_3[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.input_label_3[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.input_label_3[self.input_num].setFont(font)
        self.input_label_3[self.input_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.input_label_3[self.input_num].setText("Type:")
        self.input_label_3[self.input_num].setObjectName("input_label_3_" + str(self.input_num))
        self.input_label_4.append(QtWidgets.QLabel())
        self.input_label_4[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.input_label_4[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.input_label_4[self.input_num].setFont(font)
        self.input_label_4[self.input_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.input_label_4[self.input_num].setText("Description:")
        self.input_label_4[self.input_num].setObjectName("input_label_4_" + str(self.input_num))
        self.input_grid_lay[self.input_num].addWidget(self.input_label_4[self.input_num], 2, 0, 1, 1)
        self.input_hor_lay_2.append(QtWidgets.QHBoxLayout())
        self.input_hor_lay_2[self.input_num].setObjectName('input_hor_lay_2_' + str(self.input_num))
        self.input_grid_lay[self.input_num].addLayout(self.input_hor_lay_2[self.input_num], 1, 1, 1, 1)
        self.input_edit_1.append(QtWidgets.QLineEdit())
        self.input_edit_1[self.input_num].setEnabled(True)
        self.input_edit_1[self.input_num].setReadOnly(True)
        self.input_edit_1[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
        self.input_edit_1[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.input_edit_1[self.input_num].setFont(font2)
        self.input_edit_1[self.input_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.input_edit_1[self.input_num].setText("")
        self.input_edit_1[self.input_num].setFrame(False)
        self.input_edit_1[self.input_num].setPalette(palette)
        self.input_edit_1[self.input_num].setObjectName("input_edit_1_" + str(self.input_num))
        self.input_grid_lay[self.input_num].addWidget(self.input_edit_1[self.input_num], 0, 1, 1, 1)
        self.input_edit_2.append(QtWidgets.QLineEdit())
        self.input_edit_2[self.input_num].setEnabled(True)
        self.input_edit_2[self.input_num].setReadOnly(True)
        self.input_edit_2[self.input_num].setMinimumSize(QtCore.QSize(100, 27))
        self.input_edit_2[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.input_edit_2[self.input_num].setFont(font2)
        self.input_edit_2[self.input_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.input_edit_2[self.input_num].setText("")
        self.input_edit_2[self.input_num].setFrame(False)
        self.input_edit_2[self.input_num].setPalette(palette)
        self.input_edit_2[self.input_num].setObjectName("input_edit_2_" + str(self.input_num))
        self.input_edit_3.append(QtWidgets.QLineEdit())
        self.input_edit_3[self.input_num].setEnabled(True)
        self.input_edit_3[self.input_num].setReadOnly(True)
        self.input_edit_3[self.input_num].setMinimumSize(QtCore.QSize(100, 27))
        self.input_edit_3[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.input_edit_3[self.input_num].setFont(font2)
        self.input_edit_3[self.input_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.input_edit_3[self.input_num].setText("")
        self.input_edit_3[self.input_num].setFrame(False)
        self.input_edit_3[self.input_num].setPalette(palette)
        self.input_edit_3[self.input_num].setObjectName("input_edit_3_" + str(self.input_num))
        self.input_hor_lay_2[self.input_num].addWidget(self.input_edit_2[self.input_num])
        self.input_hor_lay_2[self.input_num].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.input_hor_lay_2[self.input_num].addWidget(self.input_label_3[self.input_num])
        self.input_hor_lay_2[self.input_num].addWidget(self.input_edit_3[self.input_num])
        self.input_plain_1.append(QtWidgets.QPlainTextEdit())
        self.input_plain_1[self.input_num].setEnabled(True)
        self.input_plain_1[self.input_num].setReadOnly(True)
        self.input_plain_1[self.input_num].setMinimumSize(QtCore.QSize(300, 60))
        self.input_plain_1[self.input_num].setMaximumSize(QtCore.QSize(16777215, 60))
        self.input_plain_1[self.input_num].setFont(font2)
        self.input_plain_1[self.input_num].setStyleSheet("QPlainTextEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}\n"
        "    \n"
        "QPlainTextEdit:disabled {\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.input_plain_1[self.input_num].setPlainText("")
        self.input_plain_1[self.input_num].setFrameShape(QtWidgets.QFrame.NoFrame)
        self.input_plain_1[self.input_num].setPalette(palette)
        self.input_plain_1[self.input_num].setObjectName("input_plain_1_" + str(self.input_num))
        self.input_grid_lay[self.input_num].addWidget(self.input_plain_1[self.input_num], 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.input_hor_lay_1[self.input_num])
        self.input_edit_1[self.input_num].setText(input_dict['Symbol'])
        self.input_edit_2[self.input_num].setText(input_dict['Units'])
        self.input_edit_3[self.input_num].setText(input_dict['Type'])
        self.input_plain_1[self.input_num].setPlainText(input_dict['Description'])
        self.input_num += 1
        
    def create_output(self, output_dict):    
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        if self.output_num > 0:
            self.verticalLayout_2.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
            self.output_line.append(QtWidgets.QFrame())
            self.output_line[self.output_num].setFrameShape(QtWidgets.QFrame.HLine)
            self.output_line[self.output_num].setFrameShadow(QtWidgets.QFrame.Sunken)
            self.output_line[self.output_num].setObjectName("output_line_" + str(self.output_num))
            self.verticalLayout_2.addWidget(self.output_line[self.output_num])
            self.verticalLayout_2.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        else:
            self.output_line.append(None)
        self.output_hor_lay_1.append(QtWidgets.QHBoxLayout())
        self.output_hor_lay_1[self.output_num].setObjectName('output_hor_lay_1_' + str(self.output_num))
        self.output_grid_lay.append(QtWidgets.QGridLayout())
        self.output_grid_lay[self.output_num].setObjectName('output_grid_lay_' + str(self.output_num))
        self.output_hor_lay_1[self.output_num].addLayout(self.output_grid_lay[self.output_num])
        self.output_hor_lay_1[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.output_label_1.append(QtWidgets.QLabel())
        self.output_label_1[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.output_label_1[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_label_1[self.output_num].setFont(font)
        self.output_label_1[self.output_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.output_label_1[self.output_num].setText("Symbol:")
        self.output_label_1[self.output_num].setObjectName("output_num" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_label_1[self.output_num], 0, 0, 1, 1)
        self.output_label_5.append(QtWidgets.QLabel())
        self.output_label_5[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.output_label_5[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_label_5[self.output_num].setFont(font)
        self.output_label_5[self.output_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.output_label_5[self.output_num].setText("Standard name:")
        self.output_label_5[self.output_num].setObjectName("output_label_5_" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_label_5[self.output_num], 1, 0, 1, 1)
        self.output_label_7.append(QtWidgets.QLabel())
        self.output_label_7[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.output_label_7[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_label_7[self.output_num].setFont(font)
        self.output_label_7[self.output_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.output_label_7[self.output_num].setText("Category:")
        self.output_label_7[self.output_num].setObjectName("output_label_7_" + str(self.output_num))
        self.output_label_6.append(QtWidgets.QLabel())
        self.output_label_6[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.output_label_6[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_label_6[self.output_num].setFont(font)
        self.output_label_6[self.output_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.output_label_6[self.output_num].setText("Long name:")
        self.output_label_6[self.output_num].setObjectName("output_label_6_" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_label_6[self.output_num], 2, 0, 1, 1)
        self.output_label_2.append(QtWidgets.QLabel())
        self.output_label_2[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.output_label_2[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_label_2[self.output_num].setFont(font)
        self.output_label_2[self.output_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.output_label_2[self.output_num].setText("Units:")
        self.output_label_2[self.output_num].setObjectName("output_label_2_" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_label_2[self.output_num], 3, 0, 1, 1)
        self.output_label_3.append(QtWidgets.QLabel())
        self.output_label_3[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.output_label_3[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_label_3[self.output_num].setFont(font)
        self.output_label_3[self.output_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.output_label_3[self.output_num].setText("Type:")
        self.output_label_3[self.output_num].setObjectName("output_label_3_" + str(self.output_num))
        self.output_label_4.append(QtWidgets.QLabel())
        self.output_label_4[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.output_label_4[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_label_4[self.output_num].setFont(font)
        self.output_label_4[self.output_num].setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}")
        self.output_label_4[self.output_num].setText("Description:")
        self.output_label_4[self.output_num].setObjectName("output_label_4_" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_label_4[self.output_num], 4, 0, 1, 1)
        self.output_hor_lay_2.append(QtWidgets.QHBoxLayout())
        self.output_hor_lay_2[self.output_num].setObjectName('output_hor_lay_2_' + str(self.output_num))
        self.output_grid_lay[self.output_num].addLayout(self.output_hor_lay_2[self.output_num], 3, 1, 1, 1)
        self.output_hor_lay_3.append(QtWidgets.QHBoxLayout())
        self.output_hor_lay_3[self.output_num].setObjectName('output_hor_lay_3_' + str(self.output_num))
        self.output_grid_lay[self.output_num].addLayout(self.output_hor_lay_3[self.output_num], 1, 1, 1, 1)
        self.output_edit_1.append(QtWidgets.QLineEdit())
        self.output_edit_1[self.output_num].setEnabled(True)
        self.output_edit_1[self.output_num].setReadOnly(True)
        self.output_edit_1[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
        self.output_edit_1[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_edit_1[self.output_num].setFont(font2)
        self.output_edit_1[self.output_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.output_edit_1[self.output_num].setText("")
        self.output_edit_1[self.output_num].setFrame(False)
        self.output_edit_1[self.output_num].setPalette(palette)
        self.output_edit_1[self.output_num].setObjectName("output_edit_1_" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_edit_1[self.output_num], 0, 1, 1, 1)
        self.output_edit_4.append(QtWidgets.QLineEdit())
        self.output_edit_4[self.output_num].setEnabled(True)
        self.output_edit_4[self.output_num].setReadOnly(True)
        self.output_edit_4[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.output_edit_4[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_edit_4[self.output_num].setFont(font2)
        self.output_edit_4[self.output_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.output_edit_4[self.output_num].setText("")
        self.output_edit_4[self.output_num].setFrame(False)
        self.output_edit_4[self.output_num].setPalette(palette)
        self.output_edit_4[self.output_num].setObjectName("output_edit_4_" + str(self.output_num))
        self.output_edit_6.append(QtWidgets.QLineEdit())
        self.output_edit_6[self.output_num].setEnabled(True)
        self.output_edit_6[self.output_num].setReadOnly(True)
        self.output_edit_6[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.output_edit_6[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_edit_6[self.output_num].setFont(font2)
        self.output_edit_6[self.output_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.output_edit_6[self.output_num].setText("")
        self.output_edit_6[self.output_num].setFrame(False)
        self.output_edit_6[self.output_num].setPalette(palette)
        self.output_edit_6[self.output_num].setObjectName("output_edit_6_" + str(self.output_num))
        self.output_hor_lay_3[self.output_num].addWidget(self.output_edit_4[self.output_num])
        self.output_hor_lay_3[self.output_num].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.output_hor_lay_3[self.output_num].addWidget(self.output_label_7[self.output_num])
        self.output_hor_lay_3[self.output_num].addWidget(self.output_edit_6[self.output_num])
        self.output_edit_5.append(QtWidgets.QLineEdit())
        self.output_edit_5[self.output_num].setEnabled(True)
        self.output_edit_5[self.output_num].setReadOnly(True)
        self.output_edit_5[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
        self.output_edit_5[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_edit_5[self.output_num].setFont(font2)
        self.output_edit_5[self.output_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.output_edit_5[self.output_num].setText("")
        self.output_edit_5[self.output_num].setFrame(False)
        self.output_edit_5[self.output_num].setPalette(palette)
        self.output_edit_5[self.output_num].setObjectName("output_edit_5_" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_edit_5[self.output_num], 2, 1, 1, 1)
        self.output_edit_2.append(QtWidgets.QLineEdit())
        self.output_edit_2[self.output_num].setEnabled(True)
        self.output_edit_2[self.output_num].setReadOnly(True)
        self.output_edit_2[self.output_num].setMinimumSize(QtCore.QSize(100, 27))
        self.output_edit_2[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_edit_2[self.output_num].setFont(font2)
        self.output_edit_2[self.output_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.output_edit_2[self.output_num].setText("")
        self.output_edit_2[self.output_num].setFrame(False)
        self.output_edit_2[self.output_num].setPalette(palette)
        self.output_edit_2[self.output_num].setObjectName("output_edit_2_" + str(self.output_num))
        self.output_edit_3.append(QtWidgets.QLineEdit())
        self.output_edit_3[self.output_num].setEnabled(True)
        self.output_edit_3[self.output_num].setReadOnly(True)
        self.output_edit_3[self.output_num].setMinimumSize(QtCore.QSize(100, 27))
        self.output_edit_3[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.output_edit_3[self.output_num].setFont(font2)
        self.output_edit_3[self.output_num].setStyleSheet("QLineEdit {\n"
        "  border-radius: 3px;\n"
        "  padding: 1px 4px 1px 4px;\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QLineEdit:disabled {\n"
        "  background-color: rgb(240, 240, 240);\n"
        "}")
        self.output_edit_3[self.output_num].setText("")
        self.output_edit_3[self.output_num].setFrame(False)
        self.output_edit_3[self.output_num].setPalette(palette)
        self.output_edit_3[self.output_num].setObjectName("output_edit_3_" + str(self.output_num))
        self.output_hor_lay_2[self.output_num].addWidget(self.output_edit_2[self.output_num])
        self.output_hor_lay_2[self.output_num].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.output_hor_lay_2[self.output_num].addWidget(self.output_label_3[self.output_num])
        self.output_hor_lay_2[self.output_num].addWidget(self.output_edit_3[self.output_num])
        self.output_plain_1.append(QtWidgets.QPlainTextEdit())
        self.output_plain_1[self.output_num].setEnabled(True)
        self.output_plain_1[self.output_num].setReadOnly(True)
        self.output_plain_1[self.output_num].setMinimumSize(QtCore.QSize(300, 60))
        self.output_plain_1[self.output_num].setMaximumSize(QtCore.QSize(16777215, 60))
        self.output_plain_1[self.output_num].setFont(font2)
        self.output_plain_1[self.output_num].setStyleSheet("QPlainTextEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}\n"
        "    \n"
        "QPlainTextEdit:disabled {\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.output_plain_1[self.output_num].setPlainText("")
        self.output_plain_1[self.output_num].setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_plain_1[self.output_num].setPalette(palette)
        self.output_plain_1[self.output_num].setObjectName("output_plain_1_" + str(self.output_num))
        self.output_grid_lay[self.output_num].addWidget(self.output_plain_1[self.output_num], 4, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.output_hor_lay_1[self.output_num])
        self.output_edit_1[self.output_num].setText(output_dict['Symbol'])
        self.output_edit_2[self.output_num].setText(output_dict['Units'])
        self.output_edit_3[self.output_num].setText(output_dict['Type'])
        self.output_edit_4[self.output_num].setText(output_dict['StandardName'])
        self.output_edit_5[self.output_num].setText(output_dict['LongName'])
        self.output_plain_1[self.output_num].setPlainText(output_dict['Description'])
        category = ''
        if isinstance(output_dict['Category'], list):
            for cat in output_dict['Category']:
                category += cat +', '
            category = category[:-2]
        else:
            category = output_dict['Category']
        self.output_edit_6[self.output_num].setText(category)
        self.input_num += 1
    
    def closeWindow(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithmDisplay - closeWindow')
        self.close()
        
