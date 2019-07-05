import logging
import time
import pathlib
import datetime
import os
import egads
import math
import copy
import simplekml
import numpy
import zipfile
import tempfile
import collections
from PyQt5 import QtCore, QtWidgets
from distutils.version import LooseVersion
import matplotlib as mpl
from functions.utils import transparency_hexa_dict_function


class CheckEGADSGuiUpdateOnline(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal()

    def __init__(self, gui_version):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - __init__')
        self.gui_version = gui_version
    
    def run(self):
        logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run')
        url = 'https://api.github.com/repos/eufarn7sp/egads-gui/releases'
        try:
            import requests
            json_object = requests.get(url=url, timeout=5).json()
            lineage_list = []
            for egads_package in json_object:
                if 'Lineage' in egads_package['name']:
                    lineage_list.append([egads_package['tag_name'], egads_package['assets'][0]['browser_download_url']])
            lineage_list = sorted(lineage_list)
            if lineage_list:
                if LooseVersion(self.gui_version) < LooseVersion(lineage_list[-1][0]):
                    self.finished.emit(lineage_list[-1][1])
                else:
                    logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                    self.finished.emit('no new version')
            else:
                logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                self.finished.emit('no new version')
        except ImportError:
            logging.exception('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - requests is not available')
        except Exception:
            logging.exception('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - internet connection '
                              'error - url ' + url)
         
    def stop(self):
        logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - stop')
        self.terminate()


class CheckEGADSUpdateOnline(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)

    def __init__(self, version):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - __init__')
        self.version = version

    def run(self):
        logging.debug('gui - thread_functions.py - CheckEGADSUpdateOnline - run')
        url = 'https://api.github.com/repos/eufarn7sp/egads/releases'
        try:
            import requests
            json_object = requests.get(url=url, timeout=5).json()
            lineage_list = []
            for egads_package in json_object:
                if 'Lineage' in egads_package['name']:
                    lineage_list.append([egads_package['tag_name'], egads_package['assets'][0]['browser_download_url']])
            lineage_list = sorted(lineage_list)
            if lineage_list:
                if LooseVersion(self.version) < LooseVersion(lineage_list[-1][0]):
                    self.finished.emit(lineage_list[-1][1])
                else:
                    logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                    self.finished.emit('no new version')
            else:
                logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                self.finished.emit('no new version')
        except ImportError:
            logging.exception('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - requests is not available')
            self.error.emit('requests is not available')
        except Exception:
            logging.exception('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - internet connection '
                              'error - url ' + url)
            self.error.emit('internet connection error')

    def stop(self):
        logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - stop')
        self.terminate()


class CheckEGADSVersion(QtCore.QThread):
    version_issue = QtCore.pyqtSignal(dict)
    
    def __init__(self, egads_version, egads_branch, min_egads_version, gui_branch):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - __init__')
        self.egads_version = egads_version
        self.min_egads_version = min_egads_version
        self.egads_branch = egads_branch
        self.gui_branch = gui_branch

    def run(self):
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - run')
        version_issue = {'version': True, 'branch': True}
        if LooseVersion(self.egads_version) < LooseVersion(self.min_egads_version):
            logging.info('gui - thread_functions.py - CheckEGADSVersion - run - an old version of EGADS has been '
                         'found: ' + self.egads_version)
            version_issue['version'] = False
        if self.egads_branch != self.gui_branch:
            logging.info('gui - thread_functions.py - CheckEGADSVersion - run - a different branch of EGADS has been '
                         'found: ' + self.egads_branch)
            version_issue['branch'] = False
        if version_issue:
            self.version_issue.emit(version_issue)
    
    def stop(self):
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - stop')
        self.terminate()


class DrawGriddedMap(QtCore.QThread):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal(collections.OrderedDict)
    
    def __init__(self, subplot_object):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - DrawGriddedMap - __init__')
        self.subplot_object = subplot_object
        
    def run(self):
        logging.debug('gui - thread_functions.py - DrawGriddedMap - run')
        self.started.emit()
        for key, subplot in self.subplot_object.items():
            pcolormesh = subplot['ax'].pcolormesh(subplot['lon_values'], subplot['lat_values'],
                                                  subplot['var_values'], transform=subplot['projection'], cmap='jet')
            self.subplot_object[key]['pcolormesh'] = pcolormesh
            cax = mpl.pyplot.axes([0.9, 0.13, 0.02, 0.72])
            mpl.pyplot.colorbar(pcolormesh, cax=cax, orientation='vertical')
        self.finished.emit(self.subplot_object)
    
    def stop(self):
        logging.debug('gui - thread_functions.py - DrawGriddedMap - stop')
        self.terminate()


class ProvideWidthHeight(QtCore.QThread):
    finished = QtCore.pyqtSignal(list)
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - ProvideWidthHeight - __init__')
        
    def run(self):
        logging.debug('gui - thread_functions.py - ProvideWidthHeight - run')
        time.sleep(1)
        self.finished.emit([str(6.2), str(12.02)])
    
    def stop(self):
        logging.debug('gui - thread_functions.py - ProvideWidthHeight - stop')
        self.terminate()


class VariableProcessingThread(QtCore.QThread):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal()

    def __init__(self, algorithm, list_combobox_input, coefficient_matrix_values, list_edit_output,
                 list_of_variables_and_attributes):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - VariableProcessingThread - __init__')
        self.algorithm = algorithm
        self.list_combobox_input = list_combobox_input
        self.coefficient_matrix_values = coefficient_matrix_values
        self.list_edit_output = list_edit_output
        self.list_of_variables_and_attributes = list_of_variables_and_attributes
        self.list_of_new_variables_and_attributes = dict()

    def run(self):
        logging.debug('gui - thread_functions.py - VariableProcessingThread - run')
        self.started.emit()
        try:
            args = []
            dimension_out = None
            first_var = True
            for index, item in enumerate(self.list_combobox_input):
                if isinstance(item, QtWidgets.QComboBox):
                    sublist = self.list_of_variables_and_attributes[item.currentText()]
                    args.append(sublist[0])
                    if first_var:
                        dimension_out = sublist[1]
                        first_var = False
                elif isinstance(item, QtWidgets.QLineEdit):
                    try:
                        args.append(float(item.text()))
                    except ValueError:
                        args.append(str(item.text()))
                elif isinstance(item, QtWidgets.QHBoxLayout):
                    args.append(self.coefficient_matrix_values[item.itemAt(0).widget().objectName()])
            output = self.algorithm().run(*args)
            if isinstance(output, tuple):
                for index, var_out in enumerate(output):
                    var_name = str(self.list_edit_output[index].text())
                    self.list_of_new_variables_and_attributes[var_name] = [var_out, dimension_out]
            else:
                var_name = str(self.list_edit_output[0].text())
                self.list_of_new_variables_and_attributes[var_name] = [output, dimension_out]
            self.finished.emit(self.list_of_new_variables_and_attributes)
        except Exception:
            logging.exception('gui - thread_functions.py - VariableProcessingThread - an exception occurred')
            self.error.emit()

    def stop(self):
        logging.debug('gui - thread_functions.py - VariableProcessingThread - stop')
        self.terminate()


class BatchProcessingThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(list)
    error = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self, batch_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - BatchProcessingThread - __init__')
        self.batch_dict = batch_dict
        self.config_dict = config_dict

    def run(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - run')
        if self.batch_dict['process'] == 1:
            self.concatenate_files()
        elif self.batch_dict['process'] == 2:
            self.na_to_nc()
        elif self.batch_dict['process'] == 3:
            self.nc_to_na()
        elif self.batch_dict['process'] == 4:
            self.delete_metadata()
        elif self.batch_dict['process'] == 5:
            self.delete_variable()
        elif self.batch_dict['process'] == 6:
            self.algorithm_processing()

    def algorithm_processing(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - algorithm_processing')
        self.progress.emit(['Standby...', 0])
        read_as_float = self.config_dict['SYSTEM'].getboolean('read_as_float')
        replace_fill_value = self.config_dict['SYSTEM'].getboolean('replace_fill_value')
        switch_fill_value = self.config_dict['SYSTEM'].getboolean('switch_fill_value')
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        algorithm = self.batch_dict['algorithm']
        input_output = self.batch_dict['processing_options']
        out_format = self.batch_dict['out_format']
        error = False
        f = None
        filename_base = None
        start_nbr = None
        digit_nbr = None
        if self.batch_dict['filename_options'] is not None:
            filename_base = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        filename_base += str('original_filename')
                    elif 'date' in option:
                        filename_base += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename_base += 'ndigit'
                        start_nbr = int(option[6:])
                        digit_nbr = len(option[6:])
                    else:
                        filename_base += option
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                if filename_base is not None:
                    filename = filename_base
                    if 'original_filename' in filename:
                        original_filename = os.path.split(file_path)[1][:-3]
                        filename = filename.replace('original_filename', original_filename)
                    if 'ndigit' in filename:
                        file_nbr = str(start_nbr + i)
                        file_nbr_str = '0' * (digit_nbr - len(file_nbr)) + file_nbr
                        filename = filename.replace('ndigit', file_nbr_str)
                else:
                    filename = os.path.split(file_path)[1]
                if out_format == 'NetCDF':
                    if not filename.endswith('.nc'):
                        filename += '.nc'
                    f = egads.input.EgadsNetCdf(file_path, 'r')
                    var_list = f.get_variable_list()
                else:
                    if not filename.endswith('.na'):
                        filename += '.na'
                    f = egads.input.NasaAmes(file_path, 'r')
                    if len(f.get_dimension_list()) > 1:
                        raise Exception('NASA Ames files with more than 1 dimension can\'t be processed at this time')
                    var_list = f.get_variable_list() + f.get_variable_list(vartype='independant')
                args = []
                dimension_out = None
                first_var = True
                for item in input_output['inputs']:
                    if item in var_list:
                        try:
                            data = f.read_variable(str(item), read_as_float=read_as_float,
                                                   replace_fill_value=replace_fill_value)
                            args.append(data)
                        except ValueError as ve:
                            if 'cannot convert float NaN to integer' in str(ve):
                                if switch_fill_value:
                                    data = f.read_variable(str(item), read_as_float=read_as_float,
                                                           replace_fill_value=False)
                                    args.append(data)
                                else:
                                    raise Exception('cannot convert float NaN to integer')
                            else:
                                raise Exception('')
                        if out_format == 'NetCDF':
                            if first_var:
                                dimension_out = f.get_dimension_list(str(item))
                                first_var = False
                    else:
                        args.append(item)
                output = algorithm().run(*args)
                if out_format == 'NetCDF':
                    new_file = egads.input.EgadsNetCdf(os.path.join(dest_folder, filename), 'w')
                    for key, value in f.get_attribute_list().items():
                        try:
                            new_file.add_attribute(key, float(value))
                        except ValueError:
                            new_file.add_attribute(key, str(value))
                    for key, value in f.get_dimension_list().items():
                        new_file.add_dim(key, value)
                    for var in f.get_variable_list():
                        var_data = f.read_variable(var)
                        dim_tuple = tuple([key for key in f.get_dimension_list(var)])
                        try:
                            var_format = format_dict[str(var_data.value.dtype)]
                        except KeyError:
                            var_format = 'double'
                        new_file.write_variable(var_data, var, dim_tuple, var_format)
                    dim_tuple = tuple([key for key in dimension_out])
                    if isinstance(output, tuple):
                        for index, var in enumerate(output):
                            var_name = input_output['outputs'][index]
                            try:
                                var_format = format_dict[str(var.value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            new_file.write_variable(var, var_name, dim_tuple, var_format)
                    else:
                        var_name = input_output['outputs'][0]
                        try:
                            var_format = format_dict[str(output.value.dtype)]
                        except KeyError:
                            var_format = 'double'
                        new_file.write_variable(output, var_name, dim_tuple, var_format)
                    new_file.close()
                else:
                    na_dict = copy.deepcopy(f.na_dict)
                    if isinstance(output, tuple):
                        for index, var in enumerate(output):
                            var_name = input_output['outputs'][index]
                            f.write_variable(var, varname=var_name, vartype="main", na_dict=na_dict)
                    else:
                        var_name = input_output['outputs'][0]
                        f.write_variable(output, varname=var_name, vartype="main", na_dict=na_dict)
                    f.save_na_file(os.path.join(dest_folder, filename), na_dict)
                f.close()
            except Exception:
                logging.exception('gui - thread_functions.py - BatchProcessingThread - algorithm_processing - an '
                                  'exception occurred during concatenation - stop_processing ' + str(stop_processing))
                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit()

    def delete_variable(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - delete_variable')
        self.progress.emit(['Standby...', 0])
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        targeted_variable = self.batch_dict['processing_options']
        out_format = self.batch_dict['out_format']
        error = False
        f = None
        filename_base = None
        start_nbr = None
        digit_nbr = None
        if self.batch_dict['filename_options'] is not None:
            filename_base = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        filename_base += str('original_filename')
                    elif 'date' in option:
                        filename_base += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename_base += 'ndigit'
                        start_nbr = int(option[6:])
                        digit_nbr = len(option[6:])
                    else:
                        filename_base += option
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                if filename_base is not None:
                    filename = filename_base
                    if 'original_filename' in filename:
                        original_filename = os.path.split(file_path)[1][:-3]
                        filename = filename.replace('original_filename', original_filename)
                    if 'ndigit' in filename:
                        file_nbr = str(start_nbr + i)
                        file_nbr_str = '0' * (digit_nbr - len(file_nbr)) + file_nbr
                        filename = filename.replace('ndigit', file_nbr_str)
                else:
                    filename = os.path.split(file_path)[1]
                if out_format == 'NetCDF':
                    if not filename.endswith('.nc'):
                        filename += '.nc'
                    f = egads.input.EgadsNetCdf(file_path, 'r')
                    new_file = egads.input.EgadsNetCdf(os.path.join(dest_folder, filename), 'w')
                    for key, value in f.get_attribute_list().items():
                        try:
                            new_file.add_attribute(key, float(value))
                        except ValueError:
                            new_file.add_attribute(key, str(value))
                    for key, value in f.get_dimension_list().items():
                        new_file.add_dim(key, value)
                    for var in f.get_variable_list():
                        if var not in targeted_variable:
                            var_data = f.read_variable(var)
                            dim_tuple = []
                            for key, _ in f.get_dimension_list(var).items():
                                dim_tuple.append(key)
                            dim_tuple = tuple(dim_tuple)
                            try:
                                var_format = format_dict[str(var_data.value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            new_file.write_variable(var_data, var, dim_tuple, var_format)
                    new_file.close()
                    f.close()

                else:
                    if not filename.endswith('.na'):
                        filename += '.na'
                    f = egads.input.NasaAmes(file_path, 'r')
                    if len(f.get_dimension_list()) > 1:
                        raise Exception('NASA Ames files with more than 1 dimension can\'t be processed at this time')
                    na_dict = copy.deepcopy(f.na_dict)
                    na_dict['V'] = []
                    na_dict['NV'] = 0
                    na_dict['VMISS'] = []
                    na_dict['VNAME'] = []
                    na_dict['VSCAL'] = []
                    for var in f.get_variable_list():
                        if var not in targeted_variable:
                            var_data = f.read_variable(var)
                            f.write_variable(var_data, vartype="main", na_dict=na_dict)
                    f.save_na_file(os.path.join(dest_folder, filename), na_dict)
                    f.close()
            except Exception:
                logging.exception('gui - thread_functions.py - BatchProcessingThread - nc_to_na - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))
                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit()

    def delete_metadata(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - delete_metadata')
        self.progress.emit(['Standby...', 0])
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        targeted_metadata = self.batch_dict['processing_options']
        error = False
        f = None
        filename_base = None
        start_nbr = None
        digit_nbr = None
        if self.batch_dict['filename_options'] is not None:
            filename_base = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        filename_base += str('original_filename')
                    elif 'date' in option:
                        filename_base += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename_base += 'ndigit'
                        start_nbr = int(option[6:])
                        digit_nbr = len(option[6:])
                    else:
                        filename_base += option
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                f = egads.input.EgadsNetCdf(file_path, 'r')
                if filename_base is not None:
                    filename = filename_base
                    if 'original_filename' in filename:
                        original_filename = os.path.split(file_path)[1][:-3]
                        filename = filename.replace('original_filename', original_filename)
                    if 'ndigit' in filename:
                        file_nbr = str(start_nbr + i)
                        file_nbr_str = '0' * (digit_nbr - len(file_nbr)) + file_nbr
                        filename = filename.replace('ndigit', file_nbr_str)
                else:
                    filename = os.path.split(file_path)[1]
                if not filename.endswith('.nc'):
                    filename += '.nc'
                new_file = egads.input.EgadsNetCdf(os.path.join(dest_folder, filename), 'w')
                for key, value in f.get_attribute_list().items():
                    if key not in targeted_metadata:
                        try:
                            new_file.add_attribute(key, float(value))
                        except ValueError:
                            new_file.add_attribute(key, str(value))

                for key, value in f.get_dimension_list().items():
                    new_file.add_dim(key, value)
                for var in f.get_variable_list():
                    var_data = f.read_variable(var)
                    dim_tuple = []
                    for key, _ in f.get_dimension_list(var).items():
                        dim_tuple.append(key)
                    dim_tuple = tuple(dim_tuple)
                    try:
                        var_format = format_dict[str(var_data.value.dtype)]
                    except KeyError:
                        var_format = 'double'
                    new_file.write_variable(var_data, var, dim_tuple, var_format)
                new_file.close()
            except Exception:
                logging.exception('gui - thread_functions.py - BatchProcessingThread - delete_metadata - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))
                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit()

    def nc_to_na(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - nc_to_na')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base = None
        start_nbr = None
        digit_nbr = None
        if self.batch_dict['filename_options'] is not None:
            filename_base = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        filename_base += str('original_filename')
                    elif 'date' in option:
                        filename_base += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename_base += 'ndigit'
                        start_nbr = int(option[6:])
                        digit_nbr = len(option[6:])
                    else:
                        filename_base += option
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                f = egads.input.EgadsNetCdf(file_path, 'r')
                if filename_base is not None:
                    filename = filename_base
                    if 'original_filename' in filename:
                        original_filename = os.path.split(file_path)[1][:-3]
                        filename = filename.replace('original_filename', original_filename)
                    if 'ndigit' in filename:
                        file_nbr = str(start_nbr + i)
                        file_nbr_str = '0' * (digit_nbr - len(file_nbr)) + file_nbr
                        filename = filename.replace('ndigit', file_nbr_str)
                else:
                    filename = os.path.split(file_path)[1][:-3]
                if not filename.endswith('.na'):
                    filename += '.na'
                f.convert_to_nasa_ames(na_file=os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - thread_functions.py - BatchProcessingThread - nc_to_na - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))
                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit()

    def na_to_nc(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - na_to_nc')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base = None
        start_nbr = None
        digit_nbr = None
        if self.batch_dict['filename_options'] is not None:
            filename_base = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        filename_base += str('original_filename')
                    elif 'date' in option:
                        filename_base += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename_base += 'ndigit'
                        start_nbr = int(option[6:])
                        digit_nbr = len(option[6:])
                    else:
                        filename_base += option
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                f = egads.input.NasaAmes(file_path, 'r')
                if filename_base is not None:
                    filename = filename_base
                    if 'original_filename' in filename:
                        original_filename = os.path.split(file_path)[1][:-3]
                        filename = filename.replace('original_filename', original_filename)
                    if 'ndigit' in filename:
                        file_nbr = str(start_nbr + i)
                        file_nbr_str = '0' * (digit_nbr - len(file_nbr)) + file_nbr
                        filename = filename.replace('ndigit', file_nbr_str)
                else:
                    filename = os.path.split(file_path)[1][:-3]
                if not filename.endswith('.nc'):
                    filename += '.nc'
                f.convert_to_netcdf(nc_file=os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - thread_functions.py - BatchProcessingThread - na_to_nc - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))
                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit()

    def concatenate_files(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - concatenate_files')
        self.progress.emit(['Standby...', 0])
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        processing_options = self.batch_dict['processing_options']
        dest_folder = self.batch_dict['destination_folder']
        out_format = self.batch_dict['out_format']
        error = False
        f = None
        if self.batch_dict['filename_options'] is None:
            if out_format == 'NetCDF':
                ext = '.nc'
            else:
                ext = '.na'
            date_time = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
            final_filename = os.path.join(dest_folder, 'concatenated_file_EGADS_' + date_time + ext)
        else:
            filename = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        _, file = os.path.split(self.batch_dict['file_list'][0])
                        filename += str(file)
                    elif 'date' in option:
                        filename += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename += option[6:]
                    else:
                        filename += option
            final_filename = os.path.join(dest_folder, filename)
        global_attributes = {}
        if out_format == 'NetCDF':
            final_file = egads.input.EgadsNetCdf(final_filename, 'w')
            for i, file_path in enumerate(self.batch_dict['file_list']):
                try:
                    self.progress.emit([os.path.split(file_path)[1],
                                        math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                    f = egads.input.EgadsNetCdf(pathlib.Path(file_path), 'r')
                    for key, value in f.get_dimension_list().items():
                        try:
                            final_file.add_dim(key, value)
                        except RuntimeError as e:
                            if 'String match to name in use' in str(e):
                                logging.error('gui - thread_functions.py - BatchProcessingThread - concatenate_files '
                                              '- dimension already in file, skipping dimension')
                    if i == 0:
                        if processing_options != 2:
                            global_attributes = f.get_attribute_list()
                    else:
                        if processing_options == 1:
                            tmp = f.get_attribute_list()
                            global_attributes = {**global_attributes, **tmp}
                    for var in f.get_variable_list():
                        egads_instance = f.read_variable(var)
                        dim_tuple = tuple([key for key, _ in f.get_dimension_list(str(var)).items()])
                        try:
                            var_format = format_dict[str(egads_instance.value.dtype)]
                        except KeyError:
                            var_format = 'double'
                        final_file.write_variable(egads_instance, var, dim_tuple, var_format)
                    f.close()
                except Exception:
                    logging.exception('gui - thread_functions.py - BatchProcessingThread - concatenate_files - an '
                                      'exception occurred during concatenation - stop_processing '
                                      + str(stop_processing))
                    if stop_processing == 0:
                        f.close()
                        continue
                    else:
                        f.close()
                        error = True
                        break
            if not error:
                if processing_options == 0 or processing_options == 1:
                    for key, value in global_attributes.items():
                        try:
                            final_file.add_attribute(key, float(value))
                        except ValueError:
                            final_file.add_attribute(key, str(value))
                final_file.close()
                self.finished.emit()
            else:
                final_file.close()
                self.error.emit()
        elif out_format == 'NASA Ames':
            final_file = egads.input.NasaAmes()
            na_dict = final_file.create_na_dict()
            global_attributes = None
            for i, file_path in enumerate(self.batch_dict['file_list']):
                try:
                    self.progress.emit([os.path.split(file_path)[1],
                                        math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                    f = egads.input.NasaAmes(str(pathlib.Path(file_path)), 'r')
                    if i == 0:
                        if processing_options != 2:
                            global_attributes = {'ONAME': f.get_attribute_value('ONAME'),
                                                 'ORG': f.get_attribute_value('ORG'),
                                                 'SNAME': f.get_attribute_value('SNAME'),
                                                 'MNAME': f.get_attribute_value('MNAME'),
                                                 'SCOM': f.get_attribute_value('SCOM'),
                                                 'NCOM': f.get_attribute_value('NCOM')}
                    else:
                        if processing_options == 1:
                            global_attributes['ONAME'] = global_attributes['ONAME'] + ' ' + f.get_attribute_value(
                                'ONAME')
                            global_attributes['ORG'] = global_attributes['ORG'] + ' ' + f.get_attribute_value('ORG')
                            global_attributes['SNAME'] = global_attributes['SNAME'] + ' ' + f.get_attribute_value(
                                'SNAME')
                            global_attributes['MNAME'] = global_attributes['MNAME'] + ' ' + f.get_attribute_value(
                                'MNAME')
                            global_attributes['SCOM'] = global_attributes['SCOM'] + ' ' + f.get_attribute_value('SCOM')
                            global_attributes['NCOM'] = global_attributes['NCOM'] + ' ' + f.get_attribute_value('NCOM')
                    ind_variable_list = f.get_variable_list(vartype='independant')
                    variable_list = f.get_variable_list(vartype='main')
                    if i == 0:
                        for name in ind_variable_list:
                            egads_instance = f.read_variable(name)
                            final_file.write_variable(egads_instance, varname=name, vartype="independant",
                                                      na_dict=na_dict)
                    for name in variable_list:
                        egads_instance = f.read_variable(name)
                        final_file.write_variable(egads_instance, varname=name, vartype="main", na_dict=na_dict)
                    f.close()
                except Exception:
                    logging.exception('gui - thread_functions.py - BatchProcessingThread - concatenate_files - an '
                                      'exception occurred during concatenation - stop_processing '
                                      + str(stop_processing))
                    if stop_processing == 0:
                        f.close()
                        continue
                    else:
                        f.close()
                        error = True
                        break
            if not error:
                no_header = False
                if processing_options == 2:
                    no_header = True
                else:
                    date = [datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day]
                    final_file.write_attribute_value('ONAME', global_attributes['ONAME'], na_dict=na_dict)
                    final_file.write_attribute_value('ORG', global_attributes['ORG'], na_dict=na_dict)
                    final_file.write_attribute_value('SNAME', global_attributes['SNAME'], na_dict=na_dict)
                    final_file.write_attribute_value('MNAME', global_attributes['MNAME'], na_dict=na_dict)
                    final_file.write_attribute_value('DATE', date, na_dict=na_dict)
                    final_file.write_attribute_value('RDATE', date, na_dict=na_dict)
                    final_file.write_attribute_value('NIV', 1, na_dict=na_dict)
                    final_file.write_attribute_value('NSCOML', len(global_attributes['SCOM']), na_dict=na_dict)
                    final_file.write_attribute_value('NNCOML', len(global_attributes['NCOM']), na_dict=na_dict)
                    final_file.write_attribute_value('SCOM', global_attributes['SCOM'], na_dict=na_dict)
                    final_file.write_attribute_value('NCOM', global_attributes['NCOM'], na_dict=na_dict)
                final_file.save_na_file(final_filename, na_dict, no_header=no_header)
                final_file.close()
                self.finished.emit()
            else:
                final_file.close()
                self.error.emit()

    def stop(self):
        logging.debug('gui - thread_functions.py - BatchProcessingThread - stop')
        self.terminate()


class ReadFileThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(list)
    error = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal(dict)

    def __init__(self, file_path, file_ext, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - ReadFileThread - __init__')
        self.file_path = file_path
        self.file_ext = file_ext
        self.config_dict = config_dict

    def run(self):
        logging.debug('gui - thread_functions.py - ReadFileThread - run')
        self.progress.emit(['Standby...', 0])
        raf = self.config_dict['SYSTEM'].getboolean('read_as_float')
        rfv = self.config_dict['SYSTEM'].getboolean('replace_fill_value')
        sfv = self.config_dict['SYSTEM'].getboolean('switch_fill_value')
        f = None
        var_attr_list = {}
        var_list = []
        glob_attr_list = {}
        unread_var = {}
        self.progress.emit(['Opening file...', 0])
        try:
            if self.file_ext == 'NetCDF Files (*.nc)':
                f = egads.input.EgadsNetCdf(self.file_path, 'r')
                var_list = sorted(f.get_variable_list())
                glob_attr_list = f.get_attribute_list()
            elif self.file_ext == 'NASA Ames Files (*.na)':
                f = egads.input.EgadsNasaAmes(self.file_path, 'r')
                var_list = sorted(f.get_variable_list() + f.get_variable_list(vartype='independant'))
                for attribute in f.get_attribute_list():
                    if attribute != 'V' and attribute != 'X':
                        glob_attr_list[attribute] = f.get_attribute_value(attribute)
            dim_list = f.get_dimension_list()
            for i, var in enumerate(var_list):
                text = 'Reading variable <i>' + var + '</i>...'
                self.progress.emit([text, math.floor(100 * float(i) / float(len(var_list)))])
                if self.file_ext == 'NetCDF Files (*.nc)':
                    var_dim = f.get_dimension_list(str(var))
                else:
                    var_dim = f.get_dimension_list()
                try:
                    egads_instance = f.read_variable(var, read_as_float=raf, replace_fill_value=rfv)
                    var_attr_list[var] = [egads_instance, var_dim]
                except Exception as e:
                    if 'dimensionality' in str(e):
                        reason = 'unit was not handled properly by EGADS'
                    elif 'cannot convert float NaN to integer' in str(e):
                        if sfv:
                            egads_instance = f.read_variable(var, read_as_float=raf, replace_fill_value=False)
                            var_attr_list[var] = [egads_instance, var_dim]
                            continue
                        else:
                            reason = 'integer can\'t be converted to NaN in INT-type variable'
                    else:
                        reason = 'no reason detected'
                    unread_var[var] = reason
                    logging.exception('gui - thread_functions.py - ReadFileThread : an error occured during the '
                                      'reading of a variable, variable ' + str(var))
            for var in unread_var:
                var_list.remove(var)
            final_dict = {'dim_list': dim_list, 'var_list': var_list, 'unread_var': unread_var,
                          'var_attr_list': var_attr_list, 'glob_attr_list': glob_attr_list, 'opened_file': f}
            self.finished.emit(final_dict)
        except Exception:
            logging.exception('gui - thread_functions.py - ReadFileThread : an error occured during the reading of a '
                              'file')
            self.error.emit()

    def stop(self):
        logging.debug('gui - thread_functions.py - ReadFileThread - stop')
        self.terminate()


class SaveFileThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(list)
    error = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()

    def __init__(self, file_name, file_ext, open_file_ext, glob_attr, dim_list, var_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - SaveFileThread - __init__')
        self.file_name = file_name
        self.file_ext = file_ext
        self.open_file_ext = open_file_ext
        self.glob_attr = glob_attr
        self.dim_list = dim_list
        self.var_dict = var_dict

    def run(self):
        logging.debug('gui - thread_functions.py - SaveFileThread - run')
        if self.file_ext == "NetCDF Files (*.nc)":
            format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                           'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
            if self.open_file_ext == 'NetCDF Files (*.nc)':
                try:
                    self.progress.emit(['Standby...', 0])
                    step_nbr = 3 + len(self.var_dict.keys())
                    step_val = 100. / step_nbr
                    prog_val = 0
                    new_file = egads.input.EgadsNetCdf(self.file_name, 'w')
                    prog_val += step_val
                    self.progress.emit(['Adding dimensions...', int(prog_val)])
                    for key, value in self.dim_list.items():
                        new_file.add_dim(key, value)
                    prog_val += step_val
                    self.progress.emit(['Adding global attributes...', int(prog_val)])
                    conventions_bool, history_bool = False, False
                    for key, value in self.glob_attr.items():
                        if 'Conventions' in key:
                            conventions_bool = True
                        if 'history' in key:
                            history_bool = True
                        try:
                            new_file.add_attribute(key, float(value))
                        except ValueError:
                            new_file.add_attribute(key, str(value))
                    if not conventions_bool:
                        new_file.add_attribute('Conventions', 'CF-1.0')
                    if not history_bool:
                        history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
                                   + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
                                   + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
                                   + ' - File created by EGADS and its GUI.')
                        new_file.add_attribute('history', history)
                    for var_name, var_sublist in self.var_dict.items():
                        prog_val += step_val
                        self.progress.emit(['Adding variable ' + var_name + '...', int(prog_val)])
                        data = var_sublist[0]
                        dimensions_tuple = []
                        for key, value in var_sublist[1].items():
                            dimensions_tuple.append(key)
                        dimensions_tuple = tuple(dimensions_tuple)
                        try:
                            var_format = format_dict[str(data.value.dtype)]
                        except KeyError:
                            var_format = 'double'
                        new_file.write_variable(data, var_name, dimensions_tuple, var_format)
                    prog_val += step_val
                    self.progress.emit(['Closing NetCdf file...', int(prog_val)])
                    new_file.close()
                    self.finished.emit()
                except Exception:
                    logging.exception('gui - thread_functions.py - SaveFileThread : an error occured during the '
                                      'saving of a file')
                    self.error.emit('')
            elif self.open_file_ext == 'NASA Ames Files (*.na)':
                try:
                    self.progress.emit(['Standby...', 0])
                    step_nbr = 3 + len(self.var_dict.keys())
                    step_val = 100. / step_nbr
                    prog_val = 0
                    prog_val += step_val
                    self.progress.emit(['Adding global attributes...', int(prog_val)])
                    title = self.glob_attr['MNAME']
                    source = self.glob_attr['SNAME']
                    institution = self.glob_attr['ORG']
                    authors = self.glob_attr['ONAME']
                    history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
                               + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
                               + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
                               + ' - NetCDF file created using EGADS and its GUI.')
                    rev_date = (str(self.glob_attr['RDATE'][0]) + '-' + str(self.glob_attr['RDATE'][1]) + '-'
                                + str(self.glob_attr['RDATE'][2]))
                    scom = ''
                    ncom = ''
                    if isinstance(self.glob_attr['SCOM'], list):
                        for i in self.glob_attr['SCOM']:
                            scom += i + '\n'
                        scom = scom[:-1]
                    else:
                        scom = self.glob_attr['SCOM']
                        if scom[-1:] == '\n':
                            scom = scom[:-1]
                    if isinstance(self.glob_attr['NCOM'], list):
                        for i in self.glob_attr['NCOM']:
                            ncom += i + '\n'
                        ncom = ncom[:-1]
                    else:
                        ncom = self.glob_attr['NCOM']
                        if ncom[-1:] == '\n':
                            ncom = ncom[:-1]
                    new_file = egads.input.EgadsNetCdf(self.file_name, 'w')
                    new_file.add_attribute('Conventions', 'CF-1.0')
                    new_file.add_attribute('title', title)
                    new_file.add_attribute('source', source)
                    new_file.add_attribute('special_comments', scom)
                    new_file.add_attribute('normal_comments', ncom)
                    new_file.add_attribute('institution', institution)
                    new_file.add_attribute('authors', authors)
                    new_file.add_attribute('history', history)
                    new_file.add_attribute('data_date_of_revision', rev_date)
                    prog_val += step_val
                    self.progress.emit(['Adding dimensions...', int(prog_val)])
                    for key, value in self.dim_list.items():
                        new_file.add_dim(key, value)
                    for var_name, var in self.var_dict.items():
                        prog_val += step_val
                        self.progress.emit(['Adding variable ' + var_name + '...', int(prog_val)])
                        dimensions_tuple = tuple(var[1].keys())
                        try:
                            var_format = format_dict[str(var[0].value.dtype)]
                        except KeyError:
                            var_format = 'double'
                        new_file.write_variable(var[0], var_name, dimensions_tuple, var_format)
                    self.progress.emit(['Closing NetCdf file...', int(prog_val)])
                    new_file.close()
                    self.finished.emit()
                except Exception:
                    logging.exception('gui - thread_functions.py - SaveFileThread : an error occured during the '
                                      'saving of a file')
                    self.error.emit('')
        elif self.file_ext == "NASA Ames Files (*.na)":
            if self.open_file_ext == 'NetCDF Files (*.nc)':
                try:
                    self.progress.emit(['Standby...', 0])
                    if len(self.dim_list) > 1:
                        info_text = ('The actual NASA Ames file class can only handle FFI equal to 1001. Thus it is '
                                     'not possible at this time to save file with more than one dimension.')
                        self.error.emit(info_text)
                    else:
                        step_nbr = 5 + len(self.var_dict.keys())
                        step_val = 100. / step_nbr
                        prog_val = 0
                        new_file = egads.input.EgadsNasaAmes()
                        na_dict = new_file.create_na_dict()
                        prog_val += step_val
                        self.progress.emit(['Preparing global attributes...', int(prog_val)])
                        nlhead, ffi, org, oname, sname, mname, dx = -999, 1001, '', '', '', '', 0.0
                        ivol, nvol = 1, 1
                        try:
                            org = self.glob_attr['institution']
                        except KeyError:
                            org = 'no institution'
                        try:
                            oname = self.glob_attr['authors']
                        except KeyError:
                            try:
                                oname = self.glob_attr['institution']
                            except KeyError:
                                oname = 'no author'
                        try:
                            sname = self.glob_attr['source']
                        except KeyError:
                            sname = 'no source'
                        try:
                            mname = self.glob_attr['title']
                        except KeyError:
                            mname = 'no title'
                        rdate = [datetime.datetime.now().year, datetime.datetime.now().month,
                                 datetime.datetime.now().day]
                        date = None
                        niv = 0
                        prog_val += step_val
                        self.progress.emit(['Adding dimensions...', int(prog_val)])
                        for ivar in self.dim_list:
                            data = self.var_dict[ivar][0]
                            new_file.write_variable(data, ivar, vartype='independant', na_dict=na_dict)
                            niv += 1
                            if 'time' in ivar:
                                units = data.metadata['units']
                                ref_time = None
                                try:
                                    index = units.index(' since ')
                                    ref_time = units[index + 7:]
                                except (KeyError, ValueError):
                                    pass
                                try:
                                    ref_time = dateutil.parser.parse(ref_time).strftime("%Y%m%dT%H%M%S")
                                    isotime = egads.algorithms.transforms.SecondsToIsotime().run(data, ref_time)
                                    y, m, d, _, _, _ = egads.algorithms.transforms.IsotimeToElements().run(isotime)
                                    date = [y.value[0], m.value[0], d.value[0]]
                                    if not date:
                                        date = [999, 999, 999]
                                except Exception:
                                    date = [999, 999, 999]
                        prog_val += step_val
                        self.progress.emit(['Adding global attributes...', int(prog_val)])
                        new_file.write_attribute_value('NLHEAD', nlhead, na_dict=na_dict)
                        new_file.write_attribute_value('FFI', ffi, na_dict=na_dict)
                        new_file.write_attribute_value('ONAME', oname, na_dict=na_dict)
                        new_file.write_attribute_value('ONAME', oname, na_dict=na_dict)
                        new_file.write_attribute_value('ORG', org, na_dict=na_dict)
                        new_file.write_attribute_value('SNAME', sname, na_dict=na_dict)
                        new_file.write_attribute_value('MNAME', mname, na_dict=na_dict)
                        new_file.write_attribute_value('DATE', date, na_dict=na_dict)
                        new_file.write_attribute_value('RDATE', rdate, na_dict=na_dict)
                        new_file.write_attribute_value('NIV', niv, na_dict=na_dict)
                        new_file.write_attribute_value('DX', dx, na_dict=na_dict)
                        name_string = ''
                        ncom = ['==== Normal Comments follow ====']
                        for attr in self.glob_attr:
                            if attr != 'institution' and attr != 'authors' and attr != 'source' and attr != 'title':
                                ncom.append(attr + ': ' + str(self.glob_attr[attr]))
                        ncom.append('==== Normal Comments end ====')
                        ncom.append('=== Data Section begins on the next line ===')
                        for name in self.dim_list:
                            name_string += name + '    '
                        scom = ['==== Special Comments follow ====',
                                '=== Additional Variable Attributes defined in the source file ===',
                                '== Variable attributes from source (NetCDF) file follow ==']
                        for var, sublist in self.var_dict.items():
                            if var not in self.dim_list:
                                prog_val += step_val
                                self.progress.emit(['Adding variable ' + var + '...', int(prog_val)])
                                new_file.write_variable(sublist[0], var, na_dict=na_dict)
                                first_line = True
                                for metadata in sublist[0].metadata:
                                    if metadata != '_FillValue' and metadata != 'scale_factor' and metadata != \
                                            'units' and metadata != 'var_name':
                                        if first_line:
                                            first_line = False
                                            scom.append('  Variable ' + var + ':')
                                        scom.append('    ' + metadata + ' = ' + str(sublist[0].metadata[metadata]))
                                name_string += var + '    '
                        prog_val += step_val
                        self.progress.emit(['Adding last global attributes...', int(prog_val)])
                        name_string = name_string[:-4]
                        ncom.append(name_string)
                        scom.append('== Variable attributes from source (NetCDF) file end ==')
                        scom.append('==== Special Comments end ====')
                        new_file.write_attribute_value('NVOL', nvol, na_dict=na_dict)
                        new_file.write_attribute_value('IVOL', ivol, na_dict=na_dict)
                        new_file.write_attribute_value('SCOM', scom, na_dict=na_dict)
                        new_file.write_attribute_value('NCOM', ncom, na_dict=na_dict)
                        new_file.write_attribute_value('NSCOML', len(scom), na_dict=na_dict)
                        new_file.write_attribute_value('NNCOML', len(ncom), na_dict=na_dict)
                        new_file.save_na_file(self.file_name, na_dict)
                        self.progress.emit(['Closing NasaAmes file...', 100])
                        new_file.close()
                        self.finished.emit()
                except Exception:
                    logging.exception('gui - thread_functions.py - SaveFileThread : an error occured during the '
                                      'saving of a file')
                    self.error.emit('')
            elif self.open_file_ext == 'NASA Ames Files (*.na)':
                try:
                    self.progress.emit(['Standby...', 0])
                    step_nbr = 3 + len(self.var_dict.keys())
                    step_val = 100. / step_nbr
                    prog_val = 0
                    new_file = egads.input.EgadsNasaAmes()
                    na_dict = new_file.create_na_dict()
                    prog_val += step_val
                    self.progress.emit(['Adding global attributes...', int(prog_val)])
                    new_file.write_attribute_value('ONAME', self.glob_attr['ONAME'], na_dict=na_dict)
                    new_file.write_attribute_value('ORG', self.glob_attr['ORG'], na_dict=na_dict)
                    new_file.write_attribute_value('SNAME', self.glob_attr['SNAME'], na_dict=na_dict)
                    new_file.write_attribute_value('MNAME', self.glob_attr['MNAME'], na_dict=na_dict)
                    new_file.write_attribute_value('DATE', self.glob_attr['DATE'], na_dict=na_dict)
                    new_file.write_attribute_value('NIV', 1, na_dict=na_dict)
                    new_file.write_attribute_value('NSCOML', len(self.glob_attr['SCOM']), na_dict=na_dict)
                    new_file.write_attribute_value('NNCOML', len(self.glob_attr['NCOM']), na_dict=na_dict)
                    new_file.write_attribute_value('SCOM', self.glob_attr['SCOM'], na_dict=na_dict)
                    new_file.write_attribute_value('NCOM', self.glob_attr['NCOM'], na_dict=na_dict)
                    for name in sorted(self.var_dict.keys()):
                        var = self.var_dict[name]
                        if name in self.dim_list:
                            prog_val += step_val
                            self.progress.emit(['Adding dimension ' + name + '...', int(prog_val)])
                            new_file.write_variable(var[0], vartype="independant", na_dict=na_dict)
                        else:
                            prog_val += step_val
                            self.progress.emit(['Adding variable ' + name + '...', int(prog_val)])
                            new_file.write_variable(var[0], vartype="main", na_dict=na_dict)
                    self.progress.emit(['Closing NasaAmes file...', 100])
                    new_file.save_na_file(self.file_name, na_dict)
                    new_file.close()
                    self.finished.emit()
                except Exception:
                    logging.exception('gui - thread_functions.py - SaveFileThread : an error occured during the '
                                      'saving of a file')
                    self.error.emit('')

    def stop(self):
        logging.debug('gui - thread_functions.py - SaveFileThread - stop')
        self.terminate()


class ExportThread(QtCore.QThread):
    error = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self, export_format, export_dict, var_dict, file_name, file_ext):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - ExportThread - __init__')
        self.export_format = export_format
        self.export_dict = export_dict
        self.var_dict = var_dict
        self.file_name = file_name
        self.file_ext = file_ext

    def run(self):
        logging.debug('gui - thread_functions.py - ExportThread - run')
        colormap_dict = {0: {'fig_height': 1, 'fig_width': 8, 'left': 0.05, 'bottom': 0.60, 'width': 0.9,
                             'height': 0.25, 'position': 'bottom', 'orientation': 'horizontal'},
                         1: {'fig_height': 1, 'fig_width': 8, 'left': 0.05, 'bottom': 0.60, 'width': 0.9,
                             'height': 0.25, 'position': 'top', 'orientation': 'horizontal'},
                         2: {'fig_height': 8, 'fig_width': 1, 'left': 0.05, 'bottom': 0.05, 'width': 0.25,
                             'height': 0.9, 'position': 'left', 'orientation': 'vertical'},
                         3: {'fig_height': 8, 'fig_width': 1, 'left': 0.05, 'bottom': 0.05, 'width': 0.25,
                             'height': 0.9, 'position': 'right', 'orientation': 'vertical'}}
        if self.export_format == 'GE-TS':
            try:
                if self.export_dict['Options']['reduce_samples']:
                    redux = int(self.export_dict['Options']['reduce_value'])
                else:
                    redux = 1
                lon = self.var_dict[self.export_dict['Coordinates']['lon']][0].value.tolist()[::redux]
                lat = self.var_dict[self.export_dict['Coordinates']['lat']][0].value.tolist()[::redux]
                if self.export_dict['Coordinates']['alt'] == 'ground':
                    alt = None
                else:
                    alt = self.var_dict[self.export_dict['Coordinates']['alt']][0].value.tolist()[::redux]
                var = self.var_dict[self.export_dict['Variables'][0]][0].value.tolist()[::redux]
                var_units = self.var_dict[self.export_dict['Variables'][0]][0].metadata['units']
                var_name = self.export_dict['Variables'][0]
                if self.export_dict['Colormap']['automatic']:
                    var_min = math.floor(min(var))
                    var_max = math.ceil(max(var))
                    var_steps = 15
                else:
                    if self.export_dict['Colormap']['min'] is not None:
                        var_min = float(self.export_dict['Colormap']['min'])
                    else:
                        var_min = math.floor(min(var))
                    if self.export_dict['Colormap']['max'] is not None:
                        var_max = float(self.export_dict['Colormap']['max'])
                    else:
                        var_max = math.ceil(max(var))
                    if self.export_dict['Colormap']['steps'] is not None:
                        var_steps = int(self.export_dict['Colormap']['steps'])
                    else:
                        var_steps = 15
                if self.export_dict['Colormap']['auto_dimension']:
                    fig_width = colormap_dict[self.export_dict['Colormap']['position']]['fig_width']
                    fig_height = colormap_dict[self.export_dict['Colormap']['position']]['fig_height']
                    left = colormap_dict[self.export_dict['Colormap']['position']]['left']
                    bottom = colormap_dict[self.export_dict['Colormap']['position']]['bottom']
                    width = colormap_dict[self.export_dict['Colormap']['position']]['width']
                    height = colormap_dict[self.export_dict['Colormap']['position']]['height']
                else:
                    if self.export_dict['Colormap']['fig_width'] is not None:
                        fig_width = self.export_dict['Colormap']['fig_width']
                    else:
                        fig_width = colormap_dict[self.export_dict['Colormap']['position']]['fig_width']
                    if self.export_dict['Colormap']['fig_height'] is not None:
                        fig_height = self.export_dict['Colormap']['fig_height']
                    else:
                        fig_height = colormap_dict[self.export_dict['Colormap']['position']]['fig_height']
                    if self.export_dict['Colormap']['pos_left'] is not None:
                        left = self.export_dict['Colormap']['pos_left']
                    else:
                        left = colormap_dict[self.export_dict['Colormap']['position']]['left']
                    if self.export_dict['Colormap']['pos_bottom'] is not None:
                        bottom = self.export_dict['Colormap']['pos_bottom']
                    else:
                        bottom = colormap_dict[self.export_dict['Colormap']['position']]['bottom']
                    if self.export_dict['Colormap']['width'] is not None:
                        width = self.export_dict['Colormap']['width']
                    else:
                        width = colormap_dict[self.export_dict['Colormap']['position']]['width']
                    if self.export_dict['Colormap']['height'] is not None:
                        height = self.export_dict['Colormap']['height']
                    else:
                        height = colormap_dict[self.export_dict['Colormap']['position']]['height']
                fig = mpl.pyplot.figure(figsize=(fig_width, fig_height))
                ax1 = fig.add_axes([left, bottom, width, height])
                cmap_name = self.export_dict['Colormap']['colormap']
                if self.export_dict['Colormap']['reversed']:
                    cmap_name += '_r'
                cmap = getattr(mpl.cm, cmap_name)
                norm = mpl.colors.Normalize(vmin=var_min, vmax=var_max)
                cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm,
                                                orientation=colormap_dict[self.export_dict['Colormap']['position']]
                                                ['orientation'])
                cb1.set_label(var_units)
                value_range = numpy.linspace(var_min, var_max, var_steps + 1)
                color_range = []
                for color in cmap(numpy.linspace(0, 1, var_steps)):
                    color_range.append(mpl.colors.rgb2hex(color[:3])[1:])
                if self.export_dict['Options']['wall_transparency']:
                    transparency = transparency_hexa_dict_function()[100 - self.export_dict['Options']['transparency']]
                else:
                    transparency = None
                style_list = []
                line_list = []
                for i, color in enumerate(color_range):
                    style_list.append(simplekml.Style())
                    style_list[i].linestyle.color = simplekml.Color.hex(color)
                    style_list[i].linestyle.width = self.export_dict['Options']['path_width']
                    if transparency is not None:
                        style_list[i].polystyle.color = simplekml.Color.hexa(color + transparency)
                    else:
                        style_list[i].polystyle.color = simplekml.Color.hex(color)
                kml = simplekml.Kml(name="Aircraft path & data", open=1)
                doc = kml.newdocument(name='Data', snippet=simplekml.Snippet(str(datetime.datetime.now())))
                fol = doc.newfolder(name=var_name)
                for i, _ in enumerate(var[:-1]):
                    line_list.append(fol.newlinestring(name=var_name))
                    if alt == 'ground':
                        alt_val = [0, 0]
                    else:
                        alt_val = [alt[i], alt[i + 1]]
                    line_list[i].coords = [(lon[i], lat[i], alt_val[0]), (lon[i + 1], lat[i + 1], alt_val[1])]
                    line_list[i].altitudemode = simplekml.AltitudeMode.absolute
                    if self.export_dict['Options']['wall']:
                        line_list[i].extrude = 1
                    else:
                        line_list[i].extrude = 0
                    if self.export_dict['Colormap']['color_value'] == 0:
                        var_moy = float(var[i] + var[i + 1]) / 2.
                    elif self.export_dict['Colormap']['color_value'] == 1:
                        var_moy = var[i]
                    else:
                        var_moy = var[i + 1]
                    idx = None
                    if var_moy < value_range[0]:
                        idx = 0
                    elif var_moy > value_range[-1]:
                        idx = -1
                    else:
                        for j, _ in enumerate(value_range):
                            if value_range[j] <= var_moy < value_range[j + 1]:
                                idx = j
                                break
                    line_list[i].style = style_list[idx]
                cmap_x = 0
                cmap_y = 0
                if colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'bottom':
                    cmap_x = 0.5
                    cmap_y = 0
                elif colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'top':
                    cmap_x = 0.5
                    cmap_y = 1
                elif colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'left':
                    cmap_x = 0
                    cmap_y = 0.5
                elif colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'right':
                    cmap_x = 1
                    cmap_y = 0.5
                screen = doc.newscreenoverlay(name='colormap')
                screen.icon.href = 'colormap.jpg'
                screen.overlayxy = simplekml.OverlayXY(x=cmap_x, y=cmap_y, xunits=simplekml.Units.fraction,
                                                       yunits=simplekml.Units.fraction)
                screen.screenxy = simplekml.ScreenXY(x=cmap_x, y=cmap_y, xunits=simplekml.Units.fraction,
                                                     yunits=simplekml.Units.fraction)
                screen.size.x = -1
                screen.size.y = -1
                screen.size.xunits = simplekml.Units.fraction
                screen.size.yunits = simplekml.Units.fraction
                if self.file_ext == 'Google Earth KMZ (*.kmz)':
                    kmz = zipfile.ZipFile(self.file_name, 'w', zipfile.ZIP_DEFLATED)
                    kml_filename = os.path.basename(self.file_name)[0:-3] + 'kml'
                    kmz.writestr(kml_filename, kml.kml())
                    jpg_filename = tempfile.mkstemp('.jpg')[1]
                    mpl.pyplot.savefig(jpg_filename)
                    kmz.write(jpg_filename, 'colormap.jpg')
                    kmz.close()
                else:
                    mpl.pyplot.savefig(os.path.join(os.path.dirname(self.file_name), 'colormap.jpg'))
                    kml.save(self.file_name)
                self.finished.emit()
            except Exception:
                logging.exception('gui - thread_functions.py - ExportThread - run : an error occured during the '
                                  'creation of the file')
                self.error.emit()
        elif self.export_format == 'GE-MP':
            pass

    def stop(self):
        logging.debug('gui - thread_functions.py - ExportThread - stop')
        self.terminate()
