# -*- coding: utf-8 -*-

import ntpath
import logging
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow, QFileDialog
from Ui_mainwindow import Ui_MainWindow
from functions.window_functions import MyGlobalAttributes
from functions.window_functions import MyVariableAttributes
from functions.window_functions import MyProcessing
from functions.window_functions import MyDisplay
from functions.window_functions import PlotWindow
from functions.window_functions import MyLog
from functions.window_functions import MyAbout
from functions.gui_functions import netcdf_gui
from functions.gui_functions import statusBar_loading
from functions.gui_functions import statusBar_updating
from functions.reading_functions import netcdf_reading
from functions.reading_functions import nasaames_reading
from functions.gui_functions import clear_layout
from functions.gui_functions import update_global_attribute_gui
from functions.gui_functions import update_variable_attribute_gui
from functions.gui_functions import add_new_variable_gui
from functions.gui_functions import update_new_variable_list_gui
from functions.saving_functions import save_as_netcdf
from functions.saving_functions import save_as_nasaaimes
#from functions.saving_functions import save_as_csv
from functions.sql_functions import objectsInit
from functions.other_functions import prepare_algorithms_structure
from hurry.filesize import size
from _version import _egads_version
from _version import _qt_version
from _version import _eclipse_version
from _version import _python_version


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        logging.info('MainWindow - GUI loaded')
        self.resolution = QtGui.QDesktopWidget().screenGeometry()
        if self.resolution.width() < 1900:
            self.resize(1000, 500)
        statusBar_loading(self)
        objectsInit(self)
        
        self.list_of_algorithms = prepare_algorithms_structure(self)
        
        self.open_file_name = ""
        self.open_file_ext = ""
        self.make_window_title()
    
    
    @pyqtSignature("")
    def on_actionExit_triggered(self):
        self.close()
    
    
    @pyqtSignature("")
    def on_actionChangelog_triggered(self):
        self.show_log()
    
    
    @pyqtSignature("")
    def on_actionAbout_EGADS_triggered(self):
        self.about_egads()
    
    
    @pyqtSignature("")
    def on_actionOpenBar_triggered(self):
        self.open_file()
    
    
    @pyqtSignature("")
    def on_actionCloseBar_triggered(self):
        self.close_file()
    
    
    @pyqtSignature("")
    def on_actionSaveAsBar_triggered(self):
        self.save_as_file()
    
    
    @pyqtSignature("")
    def on_actionCreatealgorithmBar_triggered(self):
        print "no window to create an algorithm yet"
        
    
    @pyqtSignature("")
    def on_actionPlotBar_triggered(self):
        self.plot_variable()
    
    
    @pyqtSignature("")
    def on_actionGlobalAttributesBar_triggered(self):
        self.global_attributes()
    
    
    @pyqtSignature("")
    def on_actionVariableAttributesBar_triggered(self):
        self.variable_attributes()
    
    
    @pyqtSignature("")
    def on_actionCreateVariableBar_triggered(self):
        print "no function to create a new variable yet"
        
    
    @pyqtSignature("")
    def on_actionSaveBar_triggered(self):
        print "no function to save the current file yet"    
    
    
    @pyqtSignature("")
    def on_actionAlgorithmsBar_triggered(self):
        self.process_variable()
    
    
    @pyqtSignature("")
    def on_actionDeleteVariableBar_triggered(self):
        self.delete_variable()
        
        
    @pyqtSignature("")
    def on_actionDisplayBar_triggered(self):
        self.display_variable()
    
    
    @pyqtSignature("")
    def on_actionMigrateVariableBar_triggered(self):
        self.migrate_variable()
    
    
    def open_file(self):
        logging.info('MainWindow - Opening file')
        if self.modified:
            ###
            # proposer de sauvegarder avant ouverture nouveau fichier
            ###
            pass
          
        self.open_file_name, self.open_file_ext = self.get_file_name("open")
        if not self.open_file_name:
            return
        
        if self.file_is_opened:
            print "test open | file exist | modified FALSE -> OK"
            self.close_file()
        
        out_file_base, out_file_ext = ntpath.splitext(ntpath.basename(self.open_file_name))
        open_file_size = size(ntpath.getsize(self.open_file_name))
        filename = out_file_base + out_file_ext
        if self.open_file_ext == "NetCDF Files (*.nc)":
            netcdf_gui(self)
            netcdf_reading(self, self.open_file_name)
            try:
                statusBar_updating(self, filename + "   |   " + open_file_size + "o   |   NetCDF   |   " 
                                   + self.list_of_global_attributes["Conventions"])
            except KeyError:
                self.missing_global_attributes.append("Conventions")
                statusBar_updating(self, filename + "   |   " + open_file_size + "o   |   NetCDF   |   " 
                                   + "no conventions")
                
        elif self.open_file_ext == "NASA Ames Files (*.na)":
            #print "this format is not yet supported"
            netcdf_gui(self)
            nasaames_reading(self, self.open_file_name)
            statusBar_updating(self, filename + "   |   " + open_file_size + "o   |   NASA Ames   |   " 
                               + "NASA Ames file conventions")
            return
        elif self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
            print "this format is not yet supported"
            return
        else:
            print "this format is not supported"
            return
        self.file_is_opened = True
    
    
    def close_file(self):
        logging.info('MainWindow - Closing file')
        ###
        # si fichier ouvert et self.modified = TRUE, proposer de sauvegarder avant fermeture
        ###
        if self.open_file_ext == "NetCDF Files (*.nc)":
            self.opened_file.close()
        if self.open_file_ext == "NASA Ames Files (*.na)":
            self.opened_file.close()
        objectsInit(self)
        statusBar_updating(self,"")
        clear_layout(self, self.verticalLayout3)
        self.actionCloseBar.setEnabled(False)
        self.actionSaveAsBar.setEnabled(False)
        self.actionSaveBar.setEnabled(False)
        self.actionAlgorithmsBar.setEnabled(False)
        self.actionCreateVariableBar.setEnabled(False)
        self.actionMigrateVariableBar.setEnabled(False)
        self.actionDeleteVariableBar.setEnabled(False)
        self.actionGlobalAttributesBar.setEnabled(False)
        self.actionVariableAttributesBar.setEnabled(False)
        self.actionPlotBar.setEnabled(False)
        self.actionDisplayBar.setEnabled(False)
        self.modified = False
        self.file_is_opened = False
        self.make_window_title()
        
        
        
    def save_as_file(self):
        logging.info('MainWindow - Saving_as file')
        self.save_file_name, self.save_file_ext = self.get_file_name("save")
        if not self.save_file_name:
            return
        out_file_name, out_file_ext = ntpath.splitext(ntpath.basename(self.save_file_name))  # @UnusedVariable
        if not out_file_ext:
            if self.save_file_ext == "NetCDF Files (*.nc)":
                self.save_file_name = self.save_file_name + ".nc"
            elif self.save_file_ext == "CSV Files (*.csv *.dat *.txt)":
                self.save_file_name = self.save_file_name + ".csv"
            elif self.save_file_ext == "NASA Ames Files (*.na)":
                self.save_file_name = self.save_file_name + ".na"
        if self.save_file_ext == "NetCDF Files (*.nc)":
            save_as_netcdf(self, self.save_file_name)  
        elif self.save_file_ext == "NASA Ames Files (*.na)":
            '''print "this format is not yet supported"
            return'''
            save_as_nasaaimes(self, self.save_file_name)
        elif self.save_file_ext == "CSV Files (*.csv *.dat *.txt)":
            print "this format is not yet supported"
            return
            #save_as_csv(self, self.save_file_name)
        self.make_window_title()
    
    
    def get_file_name(self, action):
        file_dialog = QFileDialog()
        filter_types = "NetCDF Files (*.nc);;CSV Files (*.csv *.dat *.txt);;NASA Ames Files (*.na)"
        if action == "save":
            out_file_name, out_file_ext = file_dialog.getSaveFileNameAndFilter(self, "Save File", "", filter_types)
        elif action == "open":
            out_file_name, out_file_ext = file_dialog.getOpenFileNameAndFilter(self, "Open File", "", filter_types)
        return str(out_file_name), str(out_file_ext)
    
    
    def make_window_title(self):
        if self.modified:
            title_string = "EGADS v" + _egads_version + ' - modified'
            self.actionSaveBar.setEnabled(True)
        else:
            title_string = "EGADS v" + _egads_version
            self.actionSaveBar.setEnabled(False)
        self.setWindowTitle(title_string)
    
    
    def global_attributes(self):
        logging.info('MainWindow - Global attributes window invoked')
        self.globalAttributesWindow = MyGlobalAttributes(self.list_of_global_attributes)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.globalAttributesWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.globalAttributesWindow.setGeometry(x2, y2, w2, h2)
        self.globalAttributesWindow.exec_()
        try:
            self.list_of_global_attributes = self.globalAttributesWindow.list_of_global_attributes
            update_global_attribute_gui(self)
            self.modified = True
            self.make_window_title()
        except AttributeError:
            pass


    def variable_attributes(self):
        logging.info('MainWindow - Variable attributes window invoked:')
        if self.tabWidget.currentIndex() == 1:
            variable = str(self.listWidget.currentItem().text())
            self.variableAttributesWindow = MyVariableAttributes(variable, self.list_of_variables_and_attributes)
        elif self.tabWidget.currentIndex() == 2:
            variable = str(self.new_listwidget.currentItem().text())
            self.variableAttributesWindow = MyVariableAttributes(variable, self.list_of_new_variables_and_attributes)
        logging.info('                ' + variable)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.variableAttributesWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.variableAttributesWindow.setGeometry(x2, y2, w2, h2)
        self.variableAttributesWindow.exec_()
        try:
            if self.tabWidget.currentIndex() == 1:
                self.list_of_variables_and_attributes = self.variableAttributesWindow.list_of_variables_and_attributes
            elif self.tabWidget.currentIndex() == 2:
                self.list_of_new_variables_and_attributes = self.variableAttributesWindow.list_of_variables_and_attributes
            update_variable_attribute_gui(self)
            self.modified = True
            self.make_window_title()
        except AttributeError:
            pass


    def delete_variable(self):
        logging.info('MainWindow - Deleting variable:')
        if self.tabWidget.currentIndex() == 1:
            list_object = self.listWidget
            variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tabWidget.currentIndex() == 2:
            list_object = self.new_listwidget
            variables_and_attributes = self.list_of_new_variables_and_attributes
        variable = str(list_object.currentItem().text())
        logging.info('                ' + variable)
        for sublist in variables_and_attributes:
            try:
                if sublist[1]["var_name"] == variable:
                    sublist[1],sublist[2] = "deleted", "deleted"
                    item=list_object.currentItem()
                    list_object.takeItem(list_object.row(item))
                    break
            except TypeError:
                pass
        try:
            if not self.new_listwidget:
                self.tabWidget.removeTab(2)
        except AttributeError:
            pass
        if not self.listWidget:
            self.actionAlgorithmsBar.setEnabled(False)
            self.actionDeleteVariableBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionPlotBar.setEnabled(False)
            self.actionDisplayBar.setEnabled(False)
            self.actionMigrateVariableBar.setEnabled(False)

    
    def process_variable(self):
        logging.info('MainWindow - Process window invoked')
        self.processingWindow = MyProcessing(self.list_of_algorithms, 
                                             self.list_of_variables_and_attributes, 
                                             self.list_of_new_variables_and_attributes)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.processingWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.processingWindow.setGeometry(x2, y2, w2, h2)
        self.processingWindow.exec_()
        try:
            self.list_of_new_variables_and_attributes = self.processingWindow.list_of_new_variables_and_attributes
            if not self.new_variables:
                add_new_variable_gui(self)
            update_new_variable_list_gui(self)
        except AttributeError:
            pass


    def migrate_variable(self):
        logging.info('MainWindow - Migrating variable:')
        variable = str(self.new_listwidget.currentItem().text())
        logging.info('                ' + variable)
        for index, sublist in enumerate(self.list_of_new_variables_and_attributes):
            if sublist[1]["var_name"] == variable:
                self.list_of_variables_and_attributes.append(self.list_of_new_variables_and_attributes[index])
                self.new_listwidget.takeItem(index)
                self.listWidget.addItem(sublist[1]["var_name"])
                self.list_of_new_variables_and_attributes.pop(index)
                break
        try:
            if not self.new_listwidget:
                self.tabWidget.removeTab(2)
        except AttributeError:
            pass
        
        
    def display_variable(self):
        logging.info('MainWindow - Display window invoked:')
        if self.tabWidget.currentIndex() == 1:
            for sublist in self.list_of_variables_and_attributes:
                if sublist[1]["var_name"] == self.listWidget.currentItem().text():
                    variable = sublist
                    break
        elif self.tabWidget.currentIndex() == 2:
            for sublist in self.list_of_new_variables_and_attributes:
                if sublist[1]["var_name"] == self.new_listwidget.currentItem().text():
                    variable = sublist
                    break
        logging.info('                ' + variable[1]["var_name"])
        self.displayWindow = MyDisplay(variable)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.displayWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.displayWindow.setGeometry(x2, y2, w2, h2)
        self.displayWindow.exec_()
        
        
    def plot_variable(self):
        logging.info('MainWindow - Plot window invoked:')
        self.plotWindow = PlotWindow(self.list_of_variables_and_attributes,
                                     self.list_of_new_variables_and_attributes)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.plotWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.plotWindow.setGeometry(x2, y2, w2, h2)
        self.plotWindow.setModal(True)
        self.plotWindow.exec_()
    
    
    def show_log(self):
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.logWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.logWindow.setGeometry(x2, y2, w2, h2)
        self.logWindow.exec_()
        
        
    def about_egads(self):
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
        + "line; color:#0000ff;\">http://www.eufar.net/tools/</a>.</p>") % (_egads_version,
                                                                        _python_version,
                                                                        _qt_version)
        
        self.aboutWindow = MyAbout(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()