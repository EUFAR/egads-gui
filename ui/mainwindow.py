import logging
import time
import os
import pathlib
import io
import configparser
import copy
import numpy
import webbrowser
import egads
import shutil
import tempfile
import collections
import importlib
import xml
import datetime
import matplotlib
matplotlib.use('Qt5Agg')
from ui._version import _gui_version
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.other_windows_functions import MyAbout, MyDisplay, MyInfo, MyUpdate, MyAsk, MySubplot, MyWarningUpdate
from functions.other_windows_functions import MyUpdateAvailable, MyExistingVariable
from functions.variable_functions import MyVariable
from functions.option_window_functions import MyOptions
from functions.plot_window_functions import PlotWindow
from functions.metadata_windows_functions import MyGlobalAttributes, MyVariableAttributes, MyNAVariableAttributes
from functions.algorithm_windows_functions import MyProcessing, MyAlgorithm
from functions.gui_functions import gui_initialization, algorithm_menu_initialization, clear_gui
from functions.gui_functions import update_icons_state, status_bar_update, update_global_attribute_gui, file_drop_layout
from functions.gui_functions import update_variable_attribute_gui, update_new_variable_list_gui
from functions.gui_functions import create_quick_access_menu, create_recent_file_menu
from functions.reading_functions import add_new_variable_gui, var_reading, new_var_reading, reading_file
from functions.material_functions import setup_fonts, widgets_metadata_dict
from functions.thread_functions import CheckEGADSGuiUpdateOnline, CheckEGADSVersion, StatusbarMsgThread
from functions.utils import prepare_algorithm_categories, prepare_output_categories, create_algorithm_dict
from functions.utils import add_element, get_element_value
from functions.saving_functions import saving_file
from functions.batch_processing_window_functions import MyBatchProcessing
from functions.export_window_functions import MyExport


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, user_path, config_dict, frozen, system, installed, parent=None):
        logging.info('gui - egads version: ' + egads.__version__)
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.user_path = user_path
        self.egads_path = egads.user_path
        self.config_dict = config_dict
        self.frozen_app = frozen
        self.system = system
        self.installed_app = installed
        self.egads_config_dict = egads.config_dict
        self.setupUi(self)
        self.font_list, self.default_font = setup_fonts()
        self.list_of_algorithms = create_algorithm_dict()
        gui_initialization(self)
        self.modified = False
        self.opened_file = None
        self.file_name = ''
        self.file_ext = ''
        self.default_message = ''
        self.file_is_opened = False
        self.list_of_dimensions = {}
        self.list_of_global_attributes = {}
        self.list_of_variables_and_attributes = {}
        self.list_of_new_variables_and_attributes = {}
        self.list_of_unread_variables = {}
        self.x_axis_variable_set = False
        self.x_axis_variable_name = None
        self.new_variables = False
        self.x_variable = None
        self.first_time_x_variable = True
        self.gui_update_url = None
        self.statusbar_msg_thread = None
        self.min_egads_version = '1.1.2'
        self.min_egads_branch = 'Lineage'
        self.buttons_lines_dict = None
        self.variable_menu = None
        self.check_egads_version_thread = None
        self.check_gui_update_thread = None
        self.objects_metadata_dict = widgets_metadata_dict()
        algorithm_menu_initialization(self)
        self.make_window_title()
        self.variable_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.variable_list.customContextMenuRequested.connect(self.right_click_menu)
        self.opened_file_list = []
        self.create_quick_access()
        self.create_recent_access()
        self.check_egads_version()
        self.check_egads_gui_update()
        self.actionCreateVariableBar.setVisible(False)
        self.start_status_bar_msg_thread('Welcome to the EGADS Lineage GUI !')
        logging.info('gui - mainwindow.py - MainWindow ready')

    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

    @QtCore.pyqtSlot()
    def on_actionHelp_triggered(self):
        self.open_help()

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
    def on_actionSaveAsBar_triggered(self):
        self.save_file()

    @QtCore.pyqtSlot()
    def on_actionExport_triggered(self):
        self.export_variables()

    @QtCore.pyqtSlot()
    def on_actionBatch_processing_triggered(self):
        self.batch_processing()

    @QtCore.pyqtSlot()
    def on_actionCloseBar_triggered(self):
        self.before_close_file()

    @QtCore.pyqtSlot()
    def on_actionGlobalAttributesBar_triggered(self):
        self.global_attributes()

    @QtCore.pyqtSlot()
    def on_actionVariableAttributesBar_triggered(self):
        self.variable_attributes()

    @QtCore.pyqtSlot()
    def on_actionMigrateVariableBar_triggered(self):
        self.migrate_variable()

    @QtCore.pyqtSlot()
    def on_actionDeleteVariableBar_triggered(self):
        self.delete_variable()

    @QtCore.pyqtSlot()
    def on_actionAlgorithmsBar_triggered(self):
        self.process_variable()

    @QtCore.pyqtSlot()
    def on_actionCreatealgorithmBar_triggered(self):
        self.create_algorithm()

    @QtCore.pyqtSlot()
    def on_actionDisplayBar_triggered(self):
        self.display_variable()

    @QtCore.pyqtSlot()
    def on_actionPlotBar_triggered(self):
        self.plot_variable()

    @QtCore.pyqtSlot()
    def on_actionUpdate_triggered(self):
        self.gui_update_info()

    def right_click_menu(self, relative_position):
        logging.debug('gui - mainwindow.py - MainWindow - right_click_menu')
        if self.tab_view.currentIndex() == 1:
            var_reading(self)
        elif self.tab_view.currentIndex() == 2:
            new_var_reading(self)
        self.variable_menu = QtWidgets.QMenu()
        display_variable = self.variable_menu.addAction("Display variable")
        plot_variable = self.variable_menu.addAction("Plot variable")
        self.x_variable = self.variable_menu.addAction("Use variable as X axis in plot window")
        delete_variable = self.variable_menu.addAction("Delete variable")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/data_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/plot_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.x_axis_variable_name == str(self.variable_list.currentItem().text()):
            activated_icon = "icons/activated_icon.svg"
        else:
            activated_icon = "icons/none_icon.png"
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(activated_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        display_variable.setIcon(icon1)
        plot_variable.setIcon(icon2)
        self.x_variable.setIcon(icon3)
        delete_variable.setIcon(icon4)
        display_variable.triggered.connect(self.display_variable)
        plot_variable.triggered.connect(self.plot_variable)
        delete_variable.triggered.connect(self.delete_variable)
        self.x_variable.triggered.connect(self.set_x_variable)
        parent_position = self.variable_list.mapToGlobal(QtCore.QPoint(0, 0))
        self.variable_menu.move(parent_position + relative_position)
        self.variable_menu.exec_()

    def open_file(self, file_path=None):
        logging.debug('gui - mainwindow.py - MainWindow - open_file')
        if file_path is None:
            file_name, file_ext = self.get_file_name('open')
            if file_name:
                if self.file_name:
                    self.before_close_file()
                self.file_name = file_name
                self.file_ext = file_ext
            else:
                return
        else:
            if pathlib.Path(file_path).is_file():
                if self.file_name:
                    self.before_close_file()
                ext_dict = {'.nc': 'NetCDF Files (*.nc)', '.csv': 'CSV Files (*.csv *.dat *.txt)',
                            '.dat': 'CSV Files (*.csv *.dat *.txt)', '.txt': 'CSV Files (*.csv *.dat *.txt)',
                            '.na': 'NASA Ames Files (*.na)'}
                self.file_name = file_path
                self.file_ext = ext_dict[os.path.splitext(file_path)[1]]
            else:
                text = ('EGADS can\'t find the following file:\n\n\t\t\t' + file_path + '\n\nPlease check that the file'
                        + ' exists before trying to open it.')
                info_window = MyInfo(text)
                info_window.exec_()
                return
        if self.file_name:
            self.add_file_to_opened_file_list()
            if self.file_ext == 'NetCDF Files (*.nc)' or self.file_ext == 'NASA Ames Files (*.na)':
                reading_file(self)
            else:
                info_window = MyInfo('This format ' + self.file_ext + ' is not supported actually.')
                info_window.exec_()
            if self.list_of_unread_variables:
                info_text = 'The following variable(s) couldn\'t be loaded:<ul>'
                for var, reason in self.list_of_unread_variables.items():
                    info_text += '<li><b>' + var + '</b> &rarr; ' + reason + '</li>'
                info_text += '</ul><p>Please read the GUI log file to have more details on previous issues.'
                info_window = MyInfo(info_text)
                info_window.exec_()

    def save_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - save_file')
        if self.new_variables:
            text = ('New variables exist in the New variables workspace. If they are not migrated into the '
                    'Variables workspace, they won\'t be saved in the new file.')
            info_window = MyInfo(text)
            info_window.exec_()
        save_file_name, save_file_ext = self.get_file_name('save')
        if save_file_name:
            if save_file_ext == 'NetCDF Files (*.nc)' or save_file_ext == 'NASA Ames Files (*.na)':
                saving_file(self, save_file_name, save_file_ext, self.file_ext)
            elif save_file_ext == "CSV Files (*.csv *.dat *.txt)":
                info_window = MyInfo('This format ' + save_file_ext + ' is not supported actually.')
                info_window.exec_()

    def export_variables(self):
        logging.debug('gui - mainwindow.py - MainWindow - export_variables')
        export_window = MyExport(self.list_of_variables_and_attributes)
        export_window.exec_()

    def global_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - global_attributes')
        glob_attr_window = MyGlobalAttributes(copy.deepcopy(self.list_of_global_attributes), self.file_ext)
        glob_attr_window.exec_()
        if glob_attr_window.global_attributes is not None:
            self.list_of_global_attributes = glob_attr_window.global_attributes
            if self.file_ext == 'NetCDF Files (*.nc)':
                update_global_attribute_gui(self, 'NetCDF')
            elif self.file_ext == 'NASA Ames Files (*.na)':
                update_global_attribute_gui(self, 'NASA Ames')
            self.modified = True
            self.make_window_title()
            self.start_status_bar_msg_thread('Global attributes have been modified...')

    def variable_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - variable_attributes')
        if self.tab_view.currentIndex() == 1:
            variable = str(self.variable_list.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_variables_and_attributes[variable][0].metadata)
        else:
            variable = str(self.new_variable_list.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_new_variables_and_attributes[variable][0].metadata)
        if self.file_ext == 'NASA Ames Files (*.na)':
            var_attr_window = MyNAVariableAttributes(variable, variable_attributes)
        else:
            var_attr_window = MyVariableAttributes(variable, variable_attributes)
        var_attr_window.exec_()
        if var_attr_window.attributes is not None:
            if self.tab_view.currentIndex() == 1:
                self.list_of_variables_and_attributes[variable][0].metadata = var_attr_window.attributes
            elif self.tab_view.currentIndex() == 2:
                self.list_of_new_variables_and_attributes[variable][0].metadata = var_attr_window.attributes
            update_variable_attribute_gui(self)
            self.modified = True
            self.make_window_title()
            self.start_status_bar_msg_thread('Variable attributes have been modified...')
    
    def display_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_variable')
        variable = None
        var_name = ''
        if self.tab_view.currentIndex() == 1:
            var_name = str(self.variable_list.currentItem().text())
            variable = self.list_of_variables_and_attributes[var_name]
        elif self.tab_view.currentIndex() == 2:
            var_name = str(self.new_variable_list.currentItem().text())
            variable = self.list_of_new_variables_and_attributes[var_name]
        var_units = variable[0].metadata['units']
        fill_value = None
        try:
            fill_value = variable[0].metadata['_FillValue']
        except KeyError:
            try:
                fill_value = variable[0].metadata['missing_value']
            except KeyError:
                pass
        var_values = variable[0].value
        dimensions = collections.OrderedDict()
        i = 0
        for key, value in variable[1].items():
            dimensions[key] = {'length': value,
                               'values': self.list_of_variables_and_attributes[key][0].value,
                               'axis': i,
                               'units': self.list_of_variables_and_attributes[key][0].metadata['units']}
            i += 1
        logging.debug('gui - mainwindow.py - MainWindow - display_variable : tab index '
                      + str(self.tab_view.currentIndex()) + ', variable ' + var_name)
        display_window = MyDisplay(var_name, var_units, fill_value, var_values, dimensions)
        display_window.exec_()

    def plot_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_variable')
        variable_list = None
        list_of_variables_and_attributes = None
        if self.tab_view.currentIndex() == 1:
            variable_list = [str(item.text()) for item in self.variable_list.selectedItems()]
            list_of_variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tab_view.currentIndex() == 2:
            variable_list = [str(item.text()) for item in self.new_variable_list.selectedItems()]
            list_of_variables_and_attributes = self.list_of_new_variables_and_attributes
        variables = collections.OrderedDict()
        dimensions = {}
        for variable in variable_list:
            var_name = variable
            var_units = list_of_variables_and_attributes[variable][0].metadata['units']
            egads_units = list_of_variables_and_attributes[variable][0].units
            var = list_of_variables_and_attributes[variable][0].value
            try:
                fill_value = list_of_variables_and_attributes[variable][0].metadata['_FillValue']
                try:
                    var[var == fill_value] = numpy.nan
                except ValueError:
                    logging.error('gui - mainwindow.py - MainWindow - plot_variable - impossible to replace missing '
                                  'values by NaN, check variable type for integers')
            except KeyError:
                try:
                    fill_value = list_of_variables_and_attributes[variable][0].metadata['missing_value']
                    try:
                        var[var == fill_value] = numpy.nan
                    except ValueError:
                        logging.error('gui - mainwindow.py - MainWindow - plot_variable - impossible to replace '
                                      'missing values by NaN, check variable type for integers')
                except KeyError:
                    logging.error('gui - mainwindow.py - MainWindow - plot_variable - no missing value found, '
                                  'impossible to replace missing values by NaN')
            var_dimensions = []
            i = 0
            if self.x_axis_variable_name is None:
                for key in list_of_variables_and_attributes[variable][1]:
                    var_dimensions.append(key)
                    try:
                        dimensions[key]
                    except KeyError:
                        dimensions[key] = {'units': self.list_of_variables_and_attributes[key][0].metadata['units'],
                                           'values': self.list_of_variables_and_attributes[key][0].value,
                                           'axis': i}
                    i += 1
            else:
                var_dimensions.append(self.x_axis_variable_name)
                try:
                    dimensions[self.x_axis_variable_name]
                except KeyError:
                    dimensions[self.x_axis_variable_name] = {
                        'units': self.list_of_variables_and_attributes[self.x_axis_variable_name][0].metadata['units'],
                        'values': self.list_of_variables_and_attributes[self.x_axis_variable_name][0].value,
                        'axis': i}
                i += 1
            variables[var_name] = {'units': var_units,
                                   'egads_units': egads_units,
                                   'values': var,
                                   'dimensions': var_dimensions}
        plot_window = PlotWindow(variables, dimensions, self.x_axis_variable_name, self.font_list, self.default_font,
                                 self.config_dict, self.gui_path)
        plot_window.setModal(True)
        plot_window.exec_()

    def process_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - process_variable')
        processing_window = MyProcessing(self.list_of_algorithms, self.list_of_variables_and_attributes,
                                         self.list_of_new_variables_and_attributes)
        processing_window.exec_()
        if processing_window.new_var_list is not None:
            self.list_of_new_variables_and_attributes.update(processing_window.new_var_list)
            if not self.new_variables:
                self.new_variables = True
                add_new_variable_gui(self)
            update_new_variable_list_gui(self)
            self.modified = True
            self.make_window_title()
            self.start_status_bar_msg_thread('New variables have been created...')

    def create_algorithm(self):
        logging.debug('gui - mainwindow.py - MainWindow - create_algorithm')
        new_algorithm_window = MyAlgorithm(prepare_algorithm_categories(self.list_of_algorithms),
                                           prepare_output_categories(self.list_of_algorithms))
        new_algorithm_window.exec_()
        if not new_algorithm_window.cancel:
            try:
                algorithm_filename = new_algorithm_window.algorithm_filename
                algorithm_category = new_algorithm_window.algorithm_category
                algorithm_name = new_algorithm_window.algorithm_name
                success = new_algorithm_window.success
                if success is True:
                    info_text = ('<p>The algorithm has been successfully created with the following details:'
                                 + '<ul><li>File name: ' + algorithm_filename + '.py</li>'
                                 + '<li>Folder: .egads_lineage/user_algorithms/' + algorithm_category.lower() + '</li>'
                                 + '<li>Algorithm name: ' + algorithm_name + '</li></ul></p>')
                    self.start_status_bar_msg_thread('A new algorithm has been created and saved...')
                else:
                    info_text = ('A critical exception occured during algorithm creation and the \'.py\' file'
                                 + ' couldn\'t be written.')
                info_window = MyInfo(info_text)
                info_window.exec_()
                egads._reload_user_algorithms()
                self.list_of_algorithms = create_algorithm_dict()
                algorithm_menu_initialization(self)
            except AttributeError:
                logging.exception('gui - mainwindow.py - MainWindow - create_algorithm: an exception occurred during '
                                  'the initialization of the algorithm information window.')

    def migrate_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - migrate_variable')
        selected_var = self.new_variable_list.selectedItems()
        new_var_list = [str(var.text()) for var in selected_var]
        var_list = list(self.list_of_variables_and_attributes.keys())
        filtered_list = [string for string in new_var_list if string in var_list]
        if filtered_list:
            if len(filtered_list) > 1:
                text = 'The following variables already exist in the New variables workspace:<ul>'
                for var in filtered_list:
                    text += '<li>' + var + '</li>'
                text += ('</ul>Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on <b>Cancel</b> '
                         'to cancel the processing.')
            else:
                text = ('The following variable, ' + filtered_list[0] + ', already exists in the New variables '
                        'workspace. Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on '
                        '<b>Cancel</b> to cancel the processing.')
            existing_window = MyExistingVariable(text)
            existing_window.exec_()
            if not existing_window.overwrite:
                return
        for var in selected_var:
            var_name = str(var.text())
            sublist = self.list_of_new_variables_and_attributes[var_name]
            self.list_of_variables_and_attributes[var_name] = sublist
            self.list_of_new_variables_and_attributes.pop(var_name, 0)
            self.variable_list.addItem(var_name)
            self.new_variable_list.takeItem(self.new_variable_list.currentRow())
            self.modified = True
            self.make_window_title()
        self.start_status_bar_msg_thread('The selected variables have been migrated to the main workspace...')
        if not self.new_variable_list:
            self.tab_view.removeTab(2)
            self.new_variables = False

    def delete_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - delete_variable - tab index ' + str(
            self.tab_view.currentIndex()))
        variables_and_attributes = None
        list_object = None
        new_tab = False
        if self.tab_view.currentIndex() == 1:
            new_tab = False
            list_object = self.variable_list
            variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tab_view.currentIndex() == 2:
            new_tab = True
            list_object = self.new_variable_list
            variables_and_attributes = self.list_of_new_variables_and_attributes
        undeleted_list = []
        for var in list_object.selectedItems():
            var_name = str(var.text())
            if var_name not in self.list_of_dimensions:
                try:
                    del variables_and_attributes[var_name]
                    list_object.takeItem(list_object.row(var))
                    clear_gui(self, 'variable')
                    self.modified = True
                    self.make_window_title()
                except TypeError:
                    logging.exception('gui - mainwindow.py - MainWindow - delete_variable: an exception occured '
                                      'during the deletion of the variable ' + var_name)
                if new_tab:
                    if not self.new_variable_list:
                        self.tab_view.removeTab(2)
                        self.new_variables = False
                if not self.variable_list:
                    self.actionAlgorithmsBar.setEnabled(False)
                    self.actionDeleteVariableBar.setEnabled(False)
                    self.actionVariableAttributesBar.setEnabled(False)
                    self.actionPlotBar.setEnabled(False)
                    self.actionDisplayBar.setEnabled(False)
                    self.actionMigrateVariableBar.setEnabled(False)
            else:
                undeleted_list.append(var_name)
        if undeleted_list:
            if len(undeleted_list) > 1:
                text = 'Because they are considered as dimensions, the following variables couldn\'t be deleted:<ul>'
                for var in undeleted_list:
                    text += '<li>' + var + '</li>'
            else:
                text = ('Because it is considered as a dimension, the following variable couldn\'t be '
                        'deleted:<ul>''<li>' + undeleted_list[0] + '</li>')
            undeleted_window = MyInfo(text)
            undeleted_window.exec_()

    @staticmethod
    def about_egads():
        logging.debug('gui - mainwindow.py - MainWindow - about_egads')
        egads_version = egads.__version__
        text = ('<p align=\"justify\">EGADS (EUFAR General Airborne Data-processing Software, v' + egads_version
                + ') and its GUI (v' + _gui_version + ') are both Python-based toolboxes for processing airborne '
                + 'atmospheric data and data visualization. <p align=\"justify\">Based on Python 3.5.4 '
                + ' and PyQt 5.11.3, EGADS and its GUI provide a framework for researchers to apply '
                + 'expert-contributed algorithms to data files, and acts as a platform for data intercomparison. '
                + 'Algorithms in EGADS will be contributed by members of the EUFAR Expert Working Group if they are '
                + 'found to be mature and well-established in the scientific community.</p><p align=\"justify\">EGADS '
                + 'and its GUI are under development by EUFAR (European Facility for Airborne Research), an Integrating'
                + ' Activity funded by the European Commission. Specifically, the networking activity Standards & '
                + 'Protocols within EUFAR is responsible for development of toolbox, in addition to developing standar'
                + 'ds for use within the EUFAR community. A compilation of these standards and other Standards & Protoc'
                + 'ols products is available on the EUFAR website: <a http://www.eufar.net/tools><span style=\" text-de'
                + 'coration: underline; color:#0000ff;\">http://www.eufar.net/tools/</a></p>')
        about_window = MyAbout(text)
        about_window.exec_()
    
    def show_options(self):
        logging.debug('gui - mainwindow.py - MainWindow - show_options')
        config_string = io.StringIO()
        self.config_dict.write(config_string)
        config_string.seek(0)
        config_dict_copy = configparser.ConfigParser()
        config_dict_copy.read_file(config_string)
        config_string = io.StringIO()
        self.egads_config_dict.write(config_string)
        config_string.seek(0)
        egads_config_dict_copy = configparser.ConfigParser()
        egads_config_dict_copy.read_file(config_string)
        option_window = MyOptions(config_dict_copy, egads_config_dict_copy, self.frozen_app, self.system,
                                  self.installed_app, self.user_path)
        option_window.available_update.connect(self.display_gui_update_button)
        option_window.exec_()
        if not option_window.cancel:
            self.config_dict = option_window.config_dict
            self.egads_config_dict = option_window.egads_config_dict
            ini_file = open(str(pathlib.Path(self.user_path, 'egads_gui.ini')), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
            egads_ini_file = open(str(pathlib.Path(self.egads_path, 'egads.ini')), 'w')
            self.egads_config_dict.write(egads_ini_file)
            egads_ini_file.close()
            self.start_status_bar_msg_thread('Options have been modified and saved...')
            if self.config_dict['FILES_FOLDERS'].getboolean('enable_user_folders'):
                create_quick_access_menu(self)
            else:
                self.menuQuick_access.clear()
                self.menuQuick_access.setEnabled(False)
            if self.config_dict['FILES_FOLDERS'].getboolean('keep_opened_files'):
                self.menuOpen_recent.clear()
                self.menuOpen_recent.setEnabled(True)
            else:
                self.menuOpen_recent.clear()
                self.menuOpen_recent.setEnabled(False)
    
    def check_egads_version(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_egads_version')
        if not self.frozen_app:
            egads_version = egads.__version__
            try:
                egads_branch = egads.__branch__
            except KeyError:
                egads_branch = 'master'
            self.check_egads_version_thread = CheckEGADSVersion(egads_version, egads_branch, self.min_egads_version,
                                                                self.min_egads_branch)
            self.check_egads_version_thread.start()
            self.check_egads_version_thread.version_issue.connect(self.parse_egads_version)

    @staticmethod
    def parse_egads_version(version_issue):
        logging.debug('gui - mainwindow.py - MainWindow - parse_egads_version - version_issue ' + str(version_issue))
        egads_version = egads.__version__
        if not version_issue['version'] or not version_issue['branch']:
            info_text = ''
            if not version_issue['version'] and not version_issue['branch']:
                info_text = ('<p>The GUI has detected a deprecated version of EGADS (v' + egads_version + ') and a non'
                             + ' Lineage EGADS branch (master). Please consider updating EGADS Lineage before using '
                             + 'the GUI. Malfunctions can occur with a deprecated version or a wrong branch of the '
                             + 'toolbox.</p>')
            else:
                if not version_issue['version']:
                    info_text = ('<p>The GUI has detected a deprecated version of EGADS (v' + egads_version + '). '
                                 + 'Please consider updating EGADS Lineage before using the GUI. Malfunctions can '
                                 + 'occur with a deprecated version of the toolbox.</p>')
                if not version_issue['branch']:
                    info_text = ('<p>The GUI has detected a a non Lineage EGADS branch (master) . Please consider '
                                 + 'updating EGADS Lineage before using the GUI. Malfunctions can occur with a wrong'
                                 + ' branch of the toolbox.</p>')
            info_window = MyInfo(info_text)
            info_window.exec_()

    def check_egads_gui_update(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_egads_gui_updates')
        if self.config_dict['OPTIONS'].getboolean('check_update'):
            try:
                import requests
                self.check_gui_update_thread = CheckEGADSGuiUpdateOnline(_gui_version, self.frozen_app, self.system,
                                                                         self.installed_app)
                self.check_gui_update_thread.start()
                self.check_gui_update_thread.finished.connect(self.display_gui_update_button)
            except ImportError:
                logging.info('gui - mainwindow.py - check_egads_gui_updates - requests is not installed, '
                             'no update check')
        else:
            logging.info('gui - mainwindow.py - check_egads_gui_updates - from options, no update check')

    def display_gui_update_button(self, val):
        logging.debug('gui - mainwindow.py - MainWindow - display_gui_update_button - val ' + str(val))
        if val != 'no new version':
            self.gui_update_url = val
            self.actionSeparator5.setVisible(True)
            self.actionUpdate.setVisible(True)
            self.start_status_bar_msg_thread('An update is available...')

    def gui_update_info(self):
        logging.debug('gui - mainwindow.py - MainWindow - gui_update_info')
        if self.frozen_app:
            if self.system == 'Windows':
                if self.installed_app:
                    warning_update_window = MyWarningUpdate()
                    warning_update_window.exec_()
                    if warning_update_window.update:
                        temp_folder = tempfile.gettempdir()
                        download_window = MyUpdate(self.gui_update_url, temp_folder)
                        download_window.exec_()
                        filename = self.gui_update_url[self.gui_update_url.rfind('/') + 1:]
                        os.startfile(temp_folder + '\\' + filename)
                        time.sleep(0.1)
                        self.close()
                else:
                    updade_window = MyUpdateAvailable(self.gui_update_url)
                    updade_window.exec_()
            elif self.system == 'Linux':
                warning_update_window = MyWarningUpdate()
                warning_update_window.exec_()
                if warning_update_window.update:
                    temp_folder = tempfile.gettempdir()
                    download_window = MyUpdate(self.gui_update_url, temp_folder)
                    download_window.exec_()
                    filename = self.gui_update_url[self.gui_update_url.rfind('/') + 1:]
                    shutil.copy('functions/unzip_update.py', temp_folder)
                    install_folder = self.gui_path + '/'
                    command = ('python3 ' + temp_folder + '/unzip_update.py ' + temp_folder
                               + '/' + filename + ' ' + install_folder)
                    os.system('x-terminal-emulator -e ' + command)
                    time.sleep(1.5)
                    self.close()
        else:
            updade_window = MyUpdateAvailable(self.gui_update_url)
            updade_window.exec_()

    def batch_processing(self):
        logging.debug('gui - mainwindow.py - Mainwindow - batch_processing')
        batch_processing_window = MyBatchProcessing(self.list_of_algorithms, self.config_dict)
        batch_processing_window.exec_()

    def get_file_name(self, action, folder=None):
        logging.debug('gui - mainwindow.py - MainWindow - get_file_name : action ' + str(action))
        if folder is not None:
            file_dialog = QtWidgets.QFileDialog(directory=folder)
        else:
            file_dialog = QtWidgets.QFileDialog()
        filter_types = 'NetCDF Files (*.nc);;NASA Ames Files (*.na)'
        out_file_name, out_file_ext = None, None
        if action == 'save':
            out_file_name, out_file_ext = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
        elif action == 'open':
            out_file_name, out_file_ext = file_dialog.getOpenFileName(self, 'Open File', '', filter_types)
        return str(out_file_name), str(out_file_ext)
    
    def before_close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - before_close_file')
        if self.modified:
            ask_save_window = MyAsk('Close')
            ask_save_window.exec_()
            if ask_save_window.choice == 'save':
                self.save_file()
                self.close_file()
            elif ask_save_window.choice == 'cancel':
                pass
            elif ask_save_window.choice == 'close':
                self.close_file()
        else:
            self.close_file()

    def close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - close_file')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        all_buttons = self.tab_view.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            if 'none_button' not in widget.objectName() and widget.objectName():
                widget.setIcon(icon)
                linewidget = self.findChild(QtWidgets.QLineEdit, widget.objectName()[:-2] + 'ln')
                if not linewidget:
                    linewidget = self.findChild(QtWidgets.QPlainTextEdit, widget.objectName()[:-2] + 'ln')
                linewidget.setEnabled(False)
        self.opened_file.close()
        filename = self.file_name
        self.tab_view.setCurrentIndex(0)
        self.modified = False
        self.opened_file = None
        self.file_name = ''
        self.file_ext = ''
        self.default_message = ''
        self.file_is_opened = False
        self.list_of_dimensions = {}
        self.list_of_global_attributes = {}
        self.list_of_variables_and_attributes = {}
        self.list_of_new_variables_and_attributes = {}
        self.list_of_unread_variables = {}
        self.x_axis_variable_set = False
        self.x_axis_variable_name = None
        self.new_variables = False
        self.x_variable = None
        self.first_time_x_variable = True
        status_bar_update(self)
        clear_gui(self)
        update_icons_state(self, 'close_file')
        self.tab_view.removeTab(2)
        self.tab_view.setEnabled(False)
        self.tab_view.setVisible(False)
        self.gridLayout.removeWidget(self.tab_view)
        file_drop_layout(self)
        self.make_window_title()
        self.start_status_bar_msg_thread('The file ' + pathlib.PurePath(filename).name + ' has been closed...')

    def set_x_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_x_variable')
        if self.x_axis_variable_set:
            self.x_axis_variable_set = False
            self.x_axis_variable_name = None
            self.start_status_bar_msg_thread('No variable set as a temporary dimension...')
        else:
            self.x_axis_variable_set = True
            self.x_axis_variable_name = str(self.variable_list.currentItem().text())
            if self.first_time_x_variable:
                self.first_time_x_variable = False
                if not self.config_dict['PLOTS'].getboolean('x_info_disabled'):
                    info_text = ('You have replaced the default dimension by another variable for the first time. '
                                 'Please note that this option only works for time series (one dimension) and not for '
                                 + 'gridded data (two or more dimensions).')
                    info_window = MyInfo(info_text)
                    info_window.exec_()
            msg = 'The variable ' + self.x_axis_variable_name + ' has been set as a temporary dimension...'
            self.start_status_bar_msg_thread(msg)

    def make_window_title(self):
        logging.debug('gui - mainwindow.py - MainWindow - make_window_title : modified ' + str(self.modified))
        if self.modified:
            title_string = 'EUFAR General Airborne Data-processing Software - GUI' + ' - modified'
        else:
            title_string = 'EUFAR General Airborne Data-processing Software - GUI'
        self.setWindowTitle(title_string)

    def start_status_bar_msg_thread(self, message):
        if self.statusbar_msg_thread is not None:
            self.statusbar_msg_thread.stop()
        self.statusbar_msg_thread = StatusbarMsgThread(self.default_message, message)
        self.statusbar_msg_thread.display_msg.connect(self.display_status_bar_msg)
        self.statusbar_msg_thread.start()

    def display_status_bar_msg(self, string):
        self.statusBar.showMessage(string)

    @staticmethod
    def open_help():
        logging.debug('gui - mainwindow.py - MainWindow - open_help')
        webbrowser.open('https://egads-gui.readthedocs.io/en/lineage/')

    def create_quick_access(self):
        if self.config_dict['FILES_FOLDERS'].getboolean('enable_user_folders'):
            if pathlib.Path(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')).exists():
                create_quick_access_menu(self)
            else:
                doc = xml.dom.minidom.Document()
                doc_root = add_element(doc, "EGADSLineageGui", doc)
                add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
                add_element(doc, "Folders", doc_root)
                f = open(str(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')), 'w')
                f.write(doc.toprettyxml())
                f.close()

    def create_recent_access(self):
        if self.config_dict['FILES_FOLDERS'].getboolean('keep_opened_files'):
            if pathlib.Path(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')).exists():
                f = open(str(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')), 'r')
                doc = xml.dom.minidom.parse(f)
                folders = doc.getElementsByTagName('Files')[0]
                nodes = folders.getElementsByTagName('File')
                for node in nodes:
                    self.opened_file_list.append(get_element_value(node, 'Path'))
                f.close()
            else:
                doc = xml.dom.minidom.Document()
                doc_root = add_element(doc, "EGADSLineageGui", doc)
                add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
                add_element(doc, "Files", doc_root)
                f = open(str(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')), 'w')
                f.write(doc.toprettyxml())
                f.close()
            create_recent_file_menu(self)

    def add_file_to_opened_file_list(self):
        if self.file_name in self.opened_file_list:
            self.opened_file_list.remove(self.file_name)
            self.opened_file_list.insert(0, self.file_name)
        else:
            if len(self.opened_file_list) == 10:
                self.opened_file_list.pop(-1)
            self.opened_file_list.insert(0, self.file_name)
        create_recent_file_menu(self)

    def closeEvent(self, event):
        logging.debug('gui - mainwindow.py - MainWindow - closeEvent')
        if self.config_dict['FILES_FOLDERS'].getboolean('keep_opened_files'):
            if self.opened_file_list:
                doc = xml.dom.minidom.Document()
                doc_root = add_element(doc, "EGADSLineageGui", doc)
                add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
                files = add_element(doc, "Files", doc_root)
                for recent_file in self.opened_file_list:
                    file = add_element(doc, "File", files)
                    add_element(doc, "Path", file, recent_file)
                f = open(str(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')), 'w')
                f.write(doc.toprettyxml())
                f.close()
        if self.modified:
            ask_save_window = MyAsk('Quit')
            ask_save_window.exec_()
            if ask_save_window.choice == 'save':
                self.save_file()
                event.accept()
            elif ask_save_window.choice == 'cancel':
                event.ignore()
            elif ask_save_window.choice == 'close':
                event.accept()
        if self.file_is_opened:
            self.opened_file.close()
        logging.info('**********************************')
        logging.info('EGADS GUI ' + _gui_version + ' is closing ...')
        logging.info('**********************************')
