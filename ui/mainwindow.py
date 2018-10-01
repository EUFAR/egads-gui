import logging
import os
import copy
import collections
import numpy
from ui._version import _gui_version, _python_version, _qt_version, _gui_branch
from egads._version import __version__ as _egads_version
try:
    from egads._version import __branch__ as _egads_branch
except ImportError:
    _egads_branch = 'master'
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.other_window_functions import MyAbout, MyOptions, MyDisplay, MyInfo
from functions.plot_window_functions import PlotWindow
from functions.metadata_window_functions import MyGlobalAttributes, MyVariableAttributes
from functions.gui_functions import gui_initialization, algorithm_list_menu_initialization, clear_gui
from functions.gui_functions import netcdf_gui_initialization, update_icons_state, status_bar_update

from functions.material_functions import objects_initialization

from functions.reading_functions import netcdf_reading
#from functions.thread_functions import CheckEGADSGuiUpdateOnline
from functions.thread_functions import CheckEGADSVersion
from functions.material_functions import setup_fonts


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, parent=None):
        logging.info('gui - egads version: ' + _egads_version)
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.config_dict = config_dict
        self.setupUi(self)
        self.font_list, self.default_font = setup_fonts(self)
        gui_initialization(self)
        objects_initialization(self)
        algorithm_list_menu_initialization(self)
        self.make_window_title()
        
        self.test_file()
        
        
        self.check_egads_version()
        logging.info('gui - mainwindow.py - MainWindow ready')
        
        
    
    
    def test_file(self):
        file_in = 'D:\\Temp\\dt_global_allsat_phy_l4_20180118_20180516_with_fake.nc'
        #file_in = 'D:\\Temp\\grepv1_gl1_201601.nc'
        #file_in = 'C:\\Users\\Olivier\\Downloads\\MSL_Serie_MERGED_Global_AVISO_GIA_Adjust_Filter2m_with_fake.nc'
        self.file_ext = 'NetCDF Files (*.nc)'
        self.file_name = file_in
        self.file_is_opened = True
        netcdf_gui_initialization(self)
        netcdf_reading(self)
        update_icons_state(self, 'open_file')
        status_bar_update(self)
        
        
        
        
    
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
    
    
    @QtCore.pyqtSlot()
    def on_actionAbout_EGADS_triggered(self):
        self.about_egads()
    
    
    @QtCore.pyqtSlot()
    def on_actionOptions_triggered(self):
        self.show_options()
    
    
    @QtCore.pyqtSlot()
    def on_actionOpenBar_triggered(self):
        self.open_file()
    
    
    @QtCore.pyqtSlot()
    def on_actionCloseBar_triggered(self):
        self.close_file()
    
    
    '''@QtCore.pyqtSlot()
    def on_actionSaveBar_triggered(self):
        self.save_file()'''
    
    
    '''@QtCore.pyqtSlot()
    def on_actionSaveAsBar_triggered(self):
        self.save_as_file()'''
    
    
    '''@QtCore.pyqtSlot()
    def on_actionCreatealgorithmBar_triggered(self):
        self.create_algorithm()'''
        
    
    @QtCore.pyqtSlot()
    def on_actionPlotBar_triggered(self):
        self.plot_variable()
    
    
    @QtCore.pyqtSlot()
    def on_actionGlobalAttributesBar_triggered(self):
        self.global_attributes()
    
    
    @QtCore.pyqtSlot()
    def on_actionVariableAttributesBar_triggered(self):
        self.variable_attributes()
    
    
    '''@QtCore.pyqtSlot()
    def on_actionCreateVariableBar_triggered(self):
        print("no function to create a new variable yet")'''
        
    
    '''@QtCore.pyqtSlot()
    def on_actionAlgorithmsBar_triggered(self):
        self.process_variable()'''
    
    
    '''@QtCore.pyqtSlot()
    def on_actionDeleteVariableBar_triggered(self):
        self.delete_variable()'''
        
        
    @QtCore.pyqtSlot()
    def on_actionDisplayBar_triggered(self):
        self.display_variable()
    
    
    '''@QtCore.pyqtSlot()
    def on_actionMigrateVariableBar_triggered(self):
        self.migrate_variable()'''
    
    def open_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - open_file')
        self.file_name, self.file_ext = self.get_file_name('open')
        if self.file_name:
            if self.file_ext == 'NetCDF Files (*.nc)' or self.file_ext == 'NASA Ames Files (*.na)':
                self.file_is_opened = True
                if self.file_ext == 'NetCDF Files (*.nc)':
                    netcdf_gui_initialization(self)
                    netcdf_reading(self)
                elif self.file_ext == 'NASA Ames Files (*.na)':
                    nasaames_gui_initialization(self)
                    nasaames_reading(self)
                update_icons_state(self, 'open_file')
                status_bar_update(self)
            else:
                print('this format is not supported')
            
            '''if self.list_of_unread_variables:
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
                self.infoWindow.exec_()'''
    
    
    def global_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - global_attributes')
        self.globalAttributesWindow = MyGlobalAttributes(copy.deepcopy(self.list_of_global_attributes), self.file_ext)
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
            pass
    
    
    def variable_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - .variable_attributes')
        if self.tab_view.currentIndex() == 1:
            variable = str(self.variable_list.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_variables_and_attributes[variable][1])
            self.variableAttributesWindow = MyVariableAttributes(variable, variable_attributes, self.file_ext)
        elif self.tab_view.currentIndex() == 2:
            variable = str(self.new_variable_list.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_new_variables_and_attributes[variable][1])
            self.variableAttributesWindow = MyVariableAttributes(variable, variable_attributes, self.open_file_ext)
        self.variableAttributesWindow.exec_()
        try:
            new_attributes = self.variableAttributesWindow.attributes
            if self.tab_view.currentIndex() == 1:
                if self.open_file_ext == 'NASA Ames Files (*.na)':
                    self.list_of_variables_and_attributes[variable][1] = new_attributes
                    self.list_of_variables_and_attributes[new_attributes['standard_name']] = self.list_of_variables_and_attributes.pop(
                        str(self.variable_list.currentItem().text()))
                    self.variable_list.currentItem().setText(new_attributes['standard_name'])
                    new_attributes['var_name'] = new_attributes['standard_name']
                    
                else:
                    self.list_of_variables_and_attributes[variable][1] = new_attributes    
            elif self.tab_view.currentIndex() == 2:
                if self.open_file_ext == 'NASA Ames Files (*.na)':
                    self.list_of_new_variables_and_attributes[variable][1] = new_attributes
                    self.list_of_new_variables_and_attributes[new_attributes['standard_name']] = self.list_of_variables_and_attributes.pop(
                        str(self.new_variable_list.currentItem().text()))
                    self.new_variable_list.currentItem().setText(new_attributes['standard_name'])
                    new_attributes['var_name'] = new_attributes['standard_name']
                self.list_of_new_variables_and_attributes[variable][1] = new_attributes    
            update_variable_attribute_gui(self)
            self.modified = True
            self.make_window_title()
        except AttributeError:
            pass
    
    def display_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_variable')
        if self.tab_view.currentIndex() == 1:
            variable = self.list_of_variables_and_attributes[str(self.variable_list.currentItem().text())]
        elif self.tab_view.currentIndex() == 2:
            variable = self.list_of_new_variables_and_attributes[str(self.new_variable_list.currentItem().text())]
        var_name = variable[1]['var_name']
        var_units = variable[1]['units']
        
        fill_value = None
        try:
            fill_value = variable[1]['_FillValue']
        except KeyError:
            try:
                fill_value = variable[1]['missing_value']
            except KeyError:
                pass
        var_values = variable[3].value
        dimensions = collections.OrderedDict()
        i = 0
        for key, value in variable[2].items():
            dimensions[key] = {'length':value,
                               'values': self.list_of_variables_and_attributes[key][3].value,
                               'axis':i,
                               'units':self.list_of_variables_and_attributes[key][1]['units']}
            i += 1
        logging.debug('gui - mainwindow.py - MainWindow - display_variable : tab index ' + str(self.tab_view.currentIndex())
                      + ', variable ' + str(variable[1]['var_name']))
        self.displayWindow = MyDisplay(var_name, var_units, fill_value, var_values, dimensions)
        self.displayWindow.exec_()
    
    
    def plot_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_variable')
        if self.tab_view.currentIndex() == 1:
            variable_list = [str(item.text()) for item in self.variable_list.selectedItems()]
            list_of_variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tab_view.currentIndex() == 2:
            variable_list = [str(item.text()) for item in self.new_variable_list.selectedItems()]
            list_of_variables_and_attributes = self.list_of_new_variables_and_attributes
        variables = collections.OrderedDict()
        dimensions = {}
        for variable in variable_list:
            var_name = list_of_variables_and_attributes[variable][1]['var_name']
            var_units = list_of_variables_and_attributes[variable][1]['units']
            var = list_of_variables_and_attributes[variable][3].value
            try:
                fill_value = list_of_variables_and_attributes[variable][1]['_FillValue']
                var[var == fill_value] = numpy.nan
            except KeyError:
                try:
                    fill_value = list_of_variables_and_attributes[variable][1]['missing_value']
                    var[var == fill_value] = numpy.nan
                except KeyError:
                    pass
            var_dimensions = []
            i = 0
            for key in list_of_variables_and_attributes[variable][2]:
                var_dimensions.append(key)
                try:
                    dimensions[key]
                except KeyError:
                    dimensions[key] = {'units':self.list_of_variables_and_attributes[key][1]['units'],
                                       'values': self.list_of_variables_and_attributes[key][3].value,
                                       'axis':i}
                i += 1
            variables[var_name] = {'units':var_units,
                                   'values': var,
                                   'dimensions': var_dimensions}
        self.plotWindow = PlotWindow(variables, dimensions, self.font_list, self.default_font)
        self.plotWindow.setModal(True)
        self.plotWindow.exec_()
    
    
    def about_egads(self):
        logging.debug('gui - mainwindow.py - MainWindow - about_egads')
        text = ('<p align=\"justify\">EGADS (EUFAR General Airborne Data-processing Software, v' + _egads_version
                + ') and its GUI (v' + _gui_version + ') are both Python-based toolboxes for processing airborne '
                + 'atmospheric data and data visualization. <p align=\"justify\">Based on Python ' + _python_version
                + ' and PyQt ' + _qt_version + ', EGADS and its GUI provide a framework for researchers to apply '
                + 'expert-contributed algorithms to data files, and acts as a platform for data intercomparison. '
                + 'Algorithms in EGADS will be contributed by members of the EUFAR Expert Working Group if they are '
                + 'found to be mature and well-established in the scientific community.</p><p align=\"justify\">EGADS '
                + 'and its GUI are under development by EUFAR (European Facility for Airborne Research), an Integrating '
                + 'Activity funded by the European Commission. Specifically, the networking activity Standards & '
                + 'Protocols within EUFAR is responsible for development of toolbox, in addition to developing standards '
                + 'for use within the EUFAR community. A compilation of these standards and other Standards & Protocols '
                + 'products is available on the EUFAR website: <a http://www.eufar.net/tools><span style=\" text-decorat'
                + 'ion: underline; color:#0000ff;\">http://www.eufar.net/tools/</a></p>')
        self.aboutWindow = MyAbout(text)
        self.aboutWindow.exec_()
    
    def show_options(self):
        self.optionWindow = MyOptions(self.config_dict)
        self.optionWindow.exec_()
        if not self.optionWindow.cancel:
            self.config_dict = self.optionWindow.config_dict
            ini_file = open(os.path.join(self.gui_path, 'egads_gui.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()  
    
    def check_egads_version(self):
        self.check_egads_version = CheckEGADSVersion(_egads_version, _egads_branch,
                                                     self.config_dict.get('OPTIONS', 'min_egads_version'),
                                                     self.config_dict.get('OPTIONS', 'egads_branch'))
        self.check_egads_version.start()
        self.check_egads_version.version_issue.connect(self.parse_egads_version)
    
    def parse_egads_version(self, version_issue):
        if not version_issue['version'] or not version_issue['branch']:
            if not version_issue['version'] and not version_issue['branch']:
                text = ('<p>The GUI has detected a deprecated version of EGADS (v' + _egads_version
                        + ') and a non Lineage EGADS branch (master). Please consider updating EGADS Lineage before using the GUI. Malfunctions can '
                        + 'occur with a deprecated version or a wrong branch of the toolbox.</p>')
            else:
                if not version_issue['version']:
                    text = ('<p>The GUI has detected a deprecated version of EGADS (v' + _egads_version
                            + '). Please consider updating EGADS Lineage before using the GUI. Malfunctions can '
                            + 'occur with a deprecated version of the toolbox.</p>')
                if not version_issue['branch']:
                    text = ('<p>The GUI has detected a a non Lineage EGADS branch (master)'
                            + '. Please consider updating EGADS Lineage before using the GUI. Malfunctions can '
                            + 'occur with a wrong branch of the toolbox.</p>')
            self.infoWindow = MyInfo(text)
            self.infoWindow.iw_label_1.setMinimumSize(QtCore.QSize(350, 16777215))
            self.infoWindow.resize(self.infoWindow.sizeHint())
            self.infoWindow.exec_()
    
    def get_file_name(self, action):
        logging.debug('gui - mainwindow.py - get_file_name : action ' + str(action))
        file_dialog = QtWidgets.QFileDialog()
        filter_types = 'NetCDF Files (*.nc);;CSV Files (*.csv *.dat *.txt);;NASA Ames Files (*.na)'
        if action == 'save':
            out_file_name, out_file_ext = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
        elif action == 'open':
            out_file_name, out_file_ext = file_dialog.getOpenFileName(self, 'Open File', '', filter_types)
        return str(out_file_name), str(out_file_ext)
    
    def close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - close_file')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        all_buttons = self.tab_view.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            if 'none_button' not in widget.objectName() and widget.objectName():
                widget.setIcon(icon)
                value = self.buttons_lines_dict[str(widget.objectName())]
                linewidget = self.findChildren(QtWidgets.QLineEdit, value[0])
                if not linewidget:
                    linewidget = self.findChildren(QtWidgets.QPlainTextEdit, value[0])
                linewidget[0].setEnabled(False)
                widget.clicked.disconnect()
        self.opened_file.close()
        self.tab_view.setCurrentIndex(0)
        self.file_is_opened = False
        objects_initialization(self)
        status_bar_update(self)
        clear_gui(self)
        update_icons_state(self, 'close_file')
        self.tab_view.removeTab(2)
        self.tab_view.setEnabled(False)
        self.tab_view.setVisible(False)
        self.modified = False
        self.make_window_title()
        self.opened_file = None
        '''all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            try:
                widget.clicked.disconnect()
            except TypeError:
                pass'''
    
    def make_window_title(self):
        logging.debug('gui - mainwindow.py - MainWindow - make_window_title : modified ' + str(self.modified))
        if self.modified:
            title_string = "EGADS GUI v" + _gui_version + ' - modified'
            self.actionSaveBar.setEnabled(True)
        else:
            title_string = "EGADS GUI v" + _gui_version
            self.actionSaveBar.setEnabled(False)
        self.setWindowTitle(title_string)
    
    
    
    
    def closeEvent(self, event):
        logging.debug('gui - mainwindow.py - MainWindow - closeEvent')
        logging.info('**********************************')
        logging.info('EGADS GUI is closing ...')
        logging.info('**********************************')
        '''if self.modified == True and self.file_is_opened == True:
            result = self.make_onsave_msg_box('Close', 'Quit EGADS GUI')
            if result == "iw_saveButton":
                self.save_file()
                event.accept()
            elif result == "iw_nosaveButton":
                event.accept()
            else:
                event.ignore()
        if self.file_is_opened == True:
            self.opened_file.close()'''
        
