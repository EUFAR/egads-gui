# -*- coding: utf-8 -*-

import logging
import copy
import ntpath
import egads
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from Ui_mainwindow import Ui_MainWindow
from functions.metadata_window_functions import MyGlobalAttributes
from functions.metadata_window_functions import MyVariableAttributes
from functions.algorithm_window_functions import MyProcessing
from functions.other_window_functions import MyDisplay
from functions.plot_window_functions import PlotWindow
from functions.other_window_functions import MyLog
from functions.other_window_functions import MyAbout
from functions.other_window_functions import MyOptions
from functions.algorithm_window_functions import MyAlgorithm
from functions.other_window_functions import MyWarning
from functions.other_window_functions import MyInfo
from functions.other_window_functions import MyUpdate
from functions.thread_functions import CheckEGADSGuiUpdateOnline
from functions.thread_functions import CheckEGADSVersion
from functions.gui_functions import gui_initialization
from functions.gui_functions import icons_initialization
from functions.gui_functions import netcdf_gui_initialization
from functions.gui_functions import nasaames_gui_initialization
from functions.gui_functions import update_icons_state
from functions.gui_functions import statusBar_loading
from functions.gui_functions import statusBar_updating
from functions.gui_functions import update_global_attribute_gui
from functions.gui_functions import update_variable_attribute_gui
from functions.gui_functions import add_new_variable_gui
from functions.gui_functions import update_new_variable_list_gui
from functions.gui_functions import clear_gui
from functions.gui_functions import algorithm_list_menu_initialization
from functions.gui_functions import gui_position
from functions.reading_functions import netcdf_reading
from functions.reading_functions import nasaames_reading
from functions.saving_functions import save_netcdf
from functions.saving_functions import save_nasaames
from functions.saving_functions import save_as_netcdf
from functions.saving_functions import save_as_nasaames
#from functions.saving_functions import save_as_csv
from functions.sql_functions import objects_initialization
from functions.other_functions import prepare_algorithms_structure
from _version import _gui_version, _python_version, _qt_version
from distutils.version import LooseVersion


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, parent=None):
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.config_dict = config_dict
        self.setupUi(self)
        gui_position(self)
        gui_initialization(self)
        objects_initialization(self)
        icons_initialization(self)
        self.list_of_algorithms = prepare_algorithms_structure(self)
        algorithm_list_menu_initialization(self)
        statusBar_loading(self)
        self.menuBar.setStyleSheet("QMenuBar {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                      stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "}\n"
        "\n"
        "QMenuBar::item {\n"
        "    spacing: 3px;\n"
        "    padding: 5px 5px 5px 5px;\n"
        "    background: transparent;\n"
        "}\n"
        "\n"
        "QMenuBar::item:selected {\n"
        "    border: 0px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QMenu {\n"
        "    background-color: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QMenu::item:selected {\n"
        "    background-color: rgb(200,200,200);\n"
        "    color: black;\n"
        "}\n"
        "\n"
        "QMenu::icon {\n"
        "    margin-left: 20px;\n"
        "    background-color: red;\n"
        "    border: none;\n"
        "}")
        "patch for combobox stylesheet"
        self.make_window_title()
        self.check_egads_gui_update()
        self.check_egads_version()
        #self.open_nafile_for_test()
        logging.info('gui - mainwindow.py - MainWindow ready')
        
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
    
    
    @QtCore.pyqtSlot()
    def on_actionChangelog_triggered(self):
       	self.show_log()
    
    
    @QtCore.pyqtSlot()
    def on_actionAbout_EGADS_triggered(self):
        self.about_egads()
    
    
    @QtCore.pyqtSlot()
    def on_actionOptions_triggered(self):
        self.show_options()
    
    
    @QtCore.pyqtSlot()
    def on_actionOpenBar_triggered(self):
        self.before_open_file()
    
    
    @QtCore.pyqtSlot()
    def on_actionCloseBar_triggered(self):
        self.before_close_file()
    
    
    @QtCore.pyqtSlot()
    def on_actionSaveBar_triggered(self):
        self.save_file()
    
    
    @QtCore.pyqtSlot()
    def on_actionSaveAsBar_triggered(self):
        self.save_as_file()
    
    
    @QtCore.pyqtSlot()
    def on_actionCreatealgorithmBar_triggered(self):
        self.create_algorithm()
        
    
    @QtCore.pyqtSlot()
    def on_actionPlotBar_triggered(self):
        self.plot_variable()
    
    
    @QtCore.pyqtSlot()
    def on_actionGlobalAttributesBar_triggered(self):
        self.global_attributes()
    
    
    @QtCore.pyqtSlot()
    def on_actionVariableAttributesBar_triggered(self):
        self.variable_attributes()
    
    
    @QtCore.pyqtSlot()
    def on_actionCreateVariableBar_triggered(self):
        print "no function to create a new variable yet"
        
    
    @QtCore.pyqtSlot()
    def on_actionAlgorithmsBar_triggered(self):
        self.process_variable()
    
    
    @QtCore.pyqtSlot()
    def on_actionDeleteVariableBar_triggered(self):
        self.delete_variable()
        
        
    @QtCore.pyqtSlot()
    def on_actionDisplayBar_triggered(self):
        self.display_variable()
    
    
    @QtCore.pyqtSlot()
    def on_actionMigrateVariableBar_triggered(self):
        self.migrate_variable()
    
    
    '''def open_ncfile_for_test(self):
        self.open_file_name = '/home/henryo/Bureau/Datasets examples/fs-core_safire-fa20_TEST_FILE.nc'
        #self.open_file_name = '/home/henryo/Bureau/Datasets examples/as-core_safire-atr42_20100913_r1_as100051.nc'
        self.open_file_ext = 'NetCDF Files (*.nc)'
        self.file_is_opened = True
        logging.debug('gui - mainwindow.py - MainWindow - open_ncfile_for_test : open_file_name ' + str(self.open_file_name))
        netcdf_gui_initialization(self)
        update_icons_state(self, 'open_file')
        netcdf_reading(self)
        statusBar_updating(self, 'NetCDF')
        
        
    def open_nafile_for_test(self):
        self.open_file_name = '/home/henryo/Bureau/Datasets examples/main_example.na'
        self.open_file_ext = 'NASA Ames Files (*.na)'
        self.file_is_opened = True
        logging.debug('gui - mainwindow.py - MainWindow - open_nafile_for_test : open_file_name ' + str(self.open_file_name))
        nasaames_gui_initialization(self)
        update_icons_state(self, 'open_file')
        nasaames_reading(self)
        statusBar_updating(self, 'NASA Ames')'''
    
    
    def before_open_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - before_open_file : modified ' + str(self.modified) 
                      + ', file_is_opened ' + str(self.file_is_opened))
        if self.modified == True and self.file_is_opened == True:
            logging.info('gui - mainwindow.py - MainWindow - before_open_file : file is opened and modified')
            result = self.make_onsave_msg_box('Open', 'Open a file')
            if result == "iw_saveButton":
                self.save_file()
                self.close_file()
                self.open_file()
            elif result == "iw_nosaveButton":
                self.close_file()
                self.open_file()
            else:
                pass
        else:
            self.open_file()
    
    
    def open_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - open_file')
        self.open_file_name, self.open_file_ext = self.get_file_name("open")
        if self.open_file_name:
            if self.open_file_ext == "NetCDF Files (*.nc)":
                netcdf_gui_initialization(self)
                update_icons_state(self, 'open_file')
                netcdf_reading(self)
                statusBar_updating(self, 'NetCDF')
            elif self.open_file_ext == "NASA Ames Files (*.na)":
                nasaames_gui_initialization(self)
                update_icons_state(self, 'open_file')
                nasaames_reading(self)
                statusBar_updating(self, 'NASA Ames')
            elif self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
                print "this format is not yet supported"
                logging.debug('gui - mainwindow.py - MainWindow - open_file: CSV Files, this format is not yet supported')
                return
            else:
                print "this format is not supported"
                logging.debug('gui - mainwindow.py - MainWindow - open_file : Other, this format is not yet supported')
                return
            self.file_is_opened = True
            if self.list_of_unread_variables:
                infoText = ('<p>The following variable(s) couldn\'t be loaded:<ul>')
                for var in self.list_of_unread_variables:
                    infoText += '<li>' + var + '</li>'
                infoText += ('</ul></p><p>Please read the GUI log file to check why the previous variable'
                             + '(s) couldn\'t be read.')
                self.infoWindow = MyInfo(infoText)
                x1, y1, w1, h1 = self.geometry().getRect()
                _, _, w2, h2 = self.infoWindow.geometry().getRect()
                self.infoWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
                self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
                self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
                self.infoWindow.exec_()
    
    
    def before_close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - before_close_file : modified ' + str(self.modified) 
                      + ', file_is_opened ' + str(self.file_is_opened))
        if self.modified == True and self.file_is_opened == True:
            result = self.make_onsave_msg_box('Close', 'Close a file')
            if result == "iw_saveButton":
                self.save_file()
                self.close_file()
            elif result == "iw_nosaveButton":
                self.close_file()
            else:
                pass
        else:
            self.close_file()
            
            
    def close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - close_file')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        all_buttons = self.tabWidget.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            if widget.objectName() != '' and widget.objectName() != 'gm_button_7':
                widget.setIcon(icon)
                value = self.buttons_lines_dict[str(widget.objectName())]
                linewidget = self.findChildren(QtWidgets.QLineEdit, value[0])
                if not linewidget:
                    linewidget = self.findChildren(QtWidgets.QPlainTextEdit, value[0])
                linewidget[0].setEnabled(False)
        self.opened_file.close()
        self.tabWidget.setCurrentIndex(0)
        objects_initialization(self)
        statusBar_updating(self,'close_file')
        clear_gui(self)
        self.tabWidget.removeTab(2)
        self.tabWidget.setEnabled(False)
        self.tabWidget.setVisible(False)
        update_icons_state(self, 'close_file')
        self.modified = False
        self.file_is_opened = False
        self.make_window_title()
        self.opened_file = None
        all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            try:
                widget.clicked.disconnect()
            except TypeError:
                pass
            
    
    def save_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - save_file : open_file_ext ' + str(self.open_file_ext))
        if self.open_file_ext == 'NetCDF Files (*.nc)':
            save_netcdf(self)
            self.modified = False
        elif self.open_file_ext == 'NASA Ames Files (*.na)':
            save_nasaames(self)
            self.modified = False
        else:
            print "this format is not yet supported"
        self.make_window_title()
    
    
    def save_as_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - .save_as_file')
        self.save_file_name, self.save_file_ext = self.get_file_name("save")
        if self.save_file_name:
            if self.save_file_ext == "NetCDF Files (*.nc)":
                if not ntpath.splitext(ntpath.basename(self.save_file_name))[1]:
                    self.save_file_name = self.save_file_name + ".nc"
                save_as_netcdf(self, self.save_file_name)  
            elif self.save_file_ext == "NASA Ames Files (*.na)":
                if not ntpath.splitext(ntpath.basename(self.save_file_name))[1]:
                    self.save_file_name = self.save_file_name + ".na"
                save_as_nasaames(self, self.save_file_name)
            elif self.save_file_ext == "CSV Files (*.csv *.dat *.txt)":
                print "this format is not yet supported"
                return
                '''if not ntpath.splitext(ntpath.basename(self.save_file_name))[1]:
                    self.save_file_name = self.save_file_name + ".csv"
                save_as_csv(self, self.save_file_name)'''
    
    
    def get_file_name(self, action):
        logging.debug('gui - mainwindow.py - MainWindow - get_file_name : action ' + str(action))
        file_dialog = QtWidgets.QFileDialog()
        filter_types = 'NetCDF Files (*.nc);;CSV Files (*.csv *.dat *.txt);;NASA Ames Files (*.na)'
        if action == 'save':
            out_file_name, out_file_ext = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
        elif action == 'open':
            out_file_name, out_file_ext = file_dialog.getOpenFileName(self, 'Open XML File', '', filter_types)
        logging.debug('gui - mainwindow.py - MainWindow - get_file_name : action ' + str(action) + ', out_file_name ' 
                      + str(out_file_name) + ', out_file_ext ' + str(out_file_ext))
        return str(out_file_name), str(out_file_ext)
    
    
    def make_window_title(self):
        logging.debug('gui - mainwindow.py - MainWindow - make_window_title : modified ' + str(self.modified))
        if self.modified:
            title_string = "EGADS GUI v" + _gui_version + ' - modified'
            self.actionSaveBar.setEnabled(True)
        else:
            title_string = "EGADS GUI v" + _gui_version
            self.actionSaveBar.setEnabled(False)
        self.setWindowTitle(title_string)
    
    
    def global_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - global_attributes')
        global_attributes = copy.deepcopy(self.list_of_global_attributes)
        self.globalAttributesWindow = MyGlobalAttributes(global_attributes, self.open_file_ext)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.globalAttributesWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.globalAttributesWindow.setGeometry(x2, y2, w2, h2)
        self.globalAttributesWindow.exec_()
        try:
            self.list_of_global_attributes = self.globalAttributesWindow.global_attributes
            if self.open_file_ext == 'NetCDF Files (*.nc)':
                update_global_attribute_gui(self, 'NetCDF')
            elif self.open_file_ext == 'NASA Ames Files (*.na)':
                update_global_attribute_gui(self, 'NASA Ames')
            self.modified = True
            self.make_window_title()
        except AttributeError:
            logging.exception('gui - mainwindow.py - MainWindow - global_attributes: variableAttributesWindow.global_attributes not available')
            pass


    def variable_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - .variable_attributes')
        if self.tabWidget.currentIndex() == 1:
            variable = str(self.listWidget.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_variables_and_attributes[variable][1])
            self.variableAttributesWindow = MyVariableAttributes(variable, variable_attributes, self.open_file_ext)
        elif self.tabWidget.currentIndex() == 2:
            variable = str(self.new_listwidget.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_new_variables_and_attributes[variable][1])
            self.variableAttributesWindow = MyVariableAttributes(variable, variable_attributes, self.open_file_ext)
        logging.info('                ' + variable)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.variableAttributesWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.variableAttributesWindow.setGeometry(x2, y2, w2, h2)
        self.variableAttributesWindow.exec_()
        try:
            new_attributes = self.variableAttributesWindow.attributes
            if self.tabWidget.currentIndex() == 1:
                if self.open_file_ext == 'NASA Ames Files (*.na)':
                    self.list_of_variables_and_attributes[variable][1] = new_attributes
                    self.list_of_variables_and_attributes[new_attributes['standard_name']] = self.list_of_variables_and_attributes.pop(str(self.listWidget.currentItem().text()))
                    self.listWidget.currentItem().setText(new_attributes['standard_name'])
                    new_attributes['var_name'] = new_attributes['standard_name']
                    
                else:
                    self.list_of_variables_and_attributes[variable][1] = new_attributes    
            elif self.tabWidget.currentIndex() == 2:
                if self.open_file_ext == 'NASA Ames Files (*.na)':
                    self.list_of_new_variables_and_attributes[variable][1] = new_attributes
                    self.list_of_new_variables_and_attributes[new_attributes['standard_name']] = self.list_of_variables_and_attributes.pop(str(self.new_listwidget.currentItem().text()))
                    self.new_listwidget.currentItem().setText(new_attributes['standard_name'])
                    new_attributes['var_name'] = new_attributes['standard_name']
                self.list_of_new_variables_and_attributes[variable][1] = new_attributes    
            update_variable_attribute_gui(self)
            self.modified = True
            self.make_window_title()
        except AttributeError:
            logging.exception('gui - mainwindow.py - MainWindow - variable_attributes: variableAttributesWindow.attributes not available')
            pass


    def delete_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - delete_variable')
        if self.tabWidget.currentIndex() == 1:
            list_object = self.listWidget
            variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tabWidget.currentIndex() == 2:
            list_object = self.new_listwidget
            variables_and_attributes = self.list_of_new_variables_and_attributes
        logging.debug('gui - mainwindow.py - MainWindow - delete_variable : delete_first_variable ' 
                      + str(self.delete_first_variable) + ', tab index ' + str(self.tabWidget.currentIndex()) 
                      + ', variable ' + str(list_object.currentItem().text()))
        if self.delete_first_variable == False and self.open_file_ext == 'NetCDF Files (*.nc)':
            infoText = ('<p>Due to the fact that the netCDF interface doesn\'t provide a way to del'
                        + 'ete a variable or to change its type or shape, the deletion of a variabl'
                        + 'e in EGADS GUI can\'t be reflected in the opened NetCDF file. The user h'
                        + 'as to save its work to a new file in which deleted variables won\'t be s'
                        + 'tored.</p><p>This message is displayed only once.</p>')
            self.infoWindow = MyInfo(infoText)
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.infoWindow.geometry().getRect()
            self.infoWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
            self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.exec_()
            self.delete_first_variable = True
        variable = str(list_object.currentItem().text())
        sublist = variables_and_attributes[variable]
        try:
            sublist[1],sublist[2], sublist[3] = 'deleted', 'deleted', 'deleted'
            item=list_object.currentItem()
            list_object.takeItem(list_object.row(item))
        except TypeError:
            logging.exception('gui - mainwindow.py - MainWindow - delete_variable: an exception occured during the deletion '
                          + 'of the variable ' + str(variable))
            pass
        try:
            if not self.new_listwidget:
                self.tabWidget.removeTab(2)
                self.new_variables = False
        except AttributeError:
            logging.exception('gui - mainwindow.py - MainWindow - delete_variable: an exception occured during the removal '
                          + 'of the tab 2.')
            pass
        if not self.listWidget:
            self.actionAlgorithmsBar.setEnabled(False)
            self.actionDeleteVariableBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionPlotBar.setEnabled(False)
            self.actionDisplayBar.setEnabled(False)
            self.actionMigrateVariableBar.setEnabled(False)

    
    def process_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - process_variable')
        self.processingWindow = MyProcessing(self.list_of_algorithms, 
                                             self.list_of_variables_and_attributes, 
                                             self.list_of_new_variables_and_attributes)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.processingWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.processingWindow.setGeometry(x2, y2, w2, h2)
        self.processingWindow.exec_()
        try:
            self.list_of_new_variables_and_attributes = self.processingWindow.list_of_new_variables_and_attributes
            if not self.new_variables:
                self.new_variables = True
                add_new_variable_gui(self)
            update_new_variable_list_gui(self)
        except AttributeError:
            logging.exception('gui - mainwindow.py - MainWindow - process_variable: processingWindow.list_of_new_variables_and_attributes not available')
            pass


    def migrate_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - migrate_variable : variable ' + str(self.new_listwidget.currentItem().text()))
        sublist = self.list_of_new_variables_and_attributes[str(self.new_listwidget.currentItem().text())]
        self.list_of_variables_and_attributes[str(self.new_listwidget.currentItem().text())] = sublist
        self.list_of_new_variables_and_attributes.pop(str(self.new_listwidget.currentItem().text()), 0)
        self.new_listwidget.takeItem(self.new_listwidget.currentRow())
        self.listWidget.addItem(sublist[1]["var_name"])
        self.modified = True
        self.make_window_title()
        try:
            if not self.new_listwidget:
                self.tabWidget.removeTab(2)
                self.new_variables = False
        except AttributeError:
            logging.exception('gui - mainwindow.py - MainWindow - migrate_variable: an exception occured during the removal '
                          + 'of the tab 2.')
            pass

        
    def display_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_variable')
        if self.tabWidget.currentIndex() == 1:
            variable = self.list_of_variables_and_attributes[str(self.listWidget.currentItem().text())]
        elif self.tabWidget.currentIndex() == 2:
            variable = self.list_of_new_variables_and_attributes[str(self.new_listwidget.currentItem().text())]
        logging.debug('gui - mainwindow.py - MainWindow - display_variable : tab index ' + str(self.tabWidget.currentIndex())
                      + ', variable ' + str(variable[1]['var_name']))
        self.displayWindow = MyDisplay(variable)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.displayWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.displayWindow.setGeometry(x2, y2, w2, h2)
        self.displayWindow.exec_()
        
        
    def plot_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_variable')
        self.plotWindow = PlotWindow(self.list_of_variables_and_attributes,
                                     self.list_of_new_variables_and_attributes)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.plotWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.plotWindow.setGeometry(x2, y2, w2, h2)
        self.plotWindow.setModal(True)
        self.plotWindow.exec_()

        
    def show_log(self):
        logging.debug('gui - mainwindow.py - MainWindow - show_log')
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.logWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.logWindow.setGeometry(x2, y2, w2, h2)
        self.logWindow.exec_()
    
    
    def show_options(self):
        self.optionWindow = MyOptions(self.config_dict)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.optionWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.optionWindow.setGeometry(x2, y2, w2, h2)
        self.optionWindow.exec_()
        if not self.optionWindow.cancel:
            self.config_dict = self.optionWindow.config_dict
            ini_file = open(os.path.join(self.gui_path, 'egads_gui.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()  
        
        
    def create_algorithm(self):
        logging.debug('gui - mainwindow.py - MainWindow - create_algorithm')
        self.myAlgorithm = MyAlgorithm()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.myAlgorithm.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.myAlgorithm.setGeometry(x2, y2, w2, h2)
        self.myAlgorithm.setModal(True)
        self.myAlgorithm.exec_()
        try:
            algorithm_filename = self.myAlgorithm.algorithm_filename
            algorithm_category = self.myAlgorithm.algorithm_category
            algorithm_name = self.myAlgorithm.algorithm_name
            success = self.myAlgorithm.success
            if success is True:
                infoText = ('<p>The algorithm has been successfully created with the following details:'
                            + '<ul><li>File name: ' + algorithm_filename + '.py</li>'
                            + '<li>Folder: egads/algorithms/user/' + algorithm_category + '</li>'
                            + '<li>Algorithm name: ' + algorithm_name + '</li></ul></p>')
            else:
                infoText = ('A critical exception occured during algorithm creation and the \'.py\' file'
                            + ' couldn\'t be written.')
            self.infoWindow = MyInfo(infoText)
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.aboutWindow.geometry().getRect()
            x2 = x1 + w1/2 - w2/2
            y2 = y1 + h1/2 - h2/2
            self.infoWindow.setGeometry(x2, y2, w2, h2)
            self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.exec_()
        except AttributeError:
            logging.exception('gui - mainwindow.py - MainWindow - create_algorithm: an exception occured during the initial'
                          + 'ization of the algorithm information window.')
            print 'an exception occured during the initialization of the algorithm information window.'
        self.list_of_algorithms = prepare_algorithms_structure(self)
        algorithm_list_menu_initialization(self)
        
        
    def about_egads(self):
        logging.debug('gui - mainwindow.py - MainWindow - about_egads')
        aboutText = ("<p>EGADS (EUFAR General Airborne Data-processing Software) v%s is a Python-based to"
        + "olbox for processing airborne atmospheric data.</p><p>Based on Python %s and PyQt %s, EGADS pr"
        + "ovides a framework for researche"
        + "rs to apply expert-contributed algorithms to data files, and acts as a platform for data"
        + " intercomparison. Algorithms in EGADS will be contributed by members of the EUFAR Expert"
        + " Working Group if they are found to be mature and well-established in the scientific com"
        + "munity.</p><p>EGADS is under development by EUFAR (European Facility for Airborne Research), a"
        + "n Integrating Activity funded by the European Commission. Specifically, the networking "
        + "activity Standards & Protocols within EUFAR is responsible for development of toolbox, i"
        + "n addition to developing standards for use within the EUFAR community. A compilation of "
        + "these standards and other Standards & Protocols products is available on the EUFAR"
        + " website : <a http://www.eufar.net/tools><span style=\" text-decoration: under"
        + "line; color:#0000ff;\">http://www.eufar.net/tools/</a>.</p>") % (_gui_version,
                                                                        _python_version,
                                                                        _qt_version)
        self.aboutWindow = MyAbout(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.aboutWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()
        
        
    def make_onsave_msg_box(self, button_string, title_string):
        logging.debug('gui - mainwindow.py - MainWindow - make_onsave_msg_box : button_string ' + str(button_string)
                      + ', title_string ' + str(title_string))
        self.presaveWindow = MyWarning(button_string, title_string)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.presaveWindow.geometry().getRect()
        self.presaveWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.presaveWindow.setMinimumSize(QtCore.QSize(470, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.setMaximumSize(QtCore.QSize(470, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.exec_()
        try:
            return self.presaveWindow.buttonName
        except AttributeError:
            logging.exception('gui - mainwindow.py - MainWindow - make_onsave_msg_box : an exception occured')
            return
    
    
    def check_egads_gui_update(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_egads_gui_update')
        if self.config_dict.getboolean('OPTIONS', 'check_update'):
            self.check_gui_update = CheckEGADSGuiUpdateOnline()
            self.check_gui_update.start()
            self.check_gui_update.finished.connect(self.parse_egads_gui_update)
            
            
    def parse_egads_gui_update(self, val):
        logging.debug('gui - other_window_functions.py - MyOptions - parse_egads_gui_update - val ' + str(val))
        if val != 'no new version':
            self.updade_window = MyUpdate(val)
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.updade_window.geometry().getRect()
            x2 = x1 + w1/2 - w2/2
            y2 = y1 + h1/2 - h2/2
            self.updade_window.setGeometry(x2, y2, w2, h2)
            self.updade_window.setModal(True)
            self.updade_window.exec_()
    
    
    def check_egads_version(self):
        self.check_egads_version = CheckEGADSVersion()
        self.check_egads_version.start()
        self.check_egads_version.deprecated.connect(self.parse_egads_version)
        
    
    def parse_egads_version(self):
        infoText = ('<p>The GUI has detected a deprecated version of EGADS (v' + egads.__version__
                    + '). Please consider updating EGADS before using the GUI. Malfunctions can '
                    + 'occur with a deprecated version of the toolbox.</p>')
        self.infoWindow = MyInfo(infoText)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.infoWindow.geometry().getRect()
        self.infoWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.exec_()
    
    
    def closeEvent(self, event):
        logging.debug('gui - mainwindow.py - MainWindow - closeEvent')
        logging.info('**********************************')
        logging.info('EGADS GUI is closing ...')
        logging.info('**********************************')
        if self.modified == True and self.file_is_opened == True:
            result = self.make_onsave_msg_box('Close', 'Quit EGADS GUI')
            if result == "iw_saveButton":
                self.save_file()
                event.accept()
            elif result == "iw_nosaveButton":
                event.accept()
            else:
                event.ignore()
        if self.file_is_opened == True:
            self.opened_file.close()
        
