import logging
import time
import collections
import pathlib
import datetime
import os
import egads
import math
import copy
from PyQt5 import QtCore, QtWidgets
from distutils.version import LooseVersion
import matplotlib.pyplot as plt


class CheckEGADSGuiUpdateOnline(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)

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
            cax = plt.axes([0.9, 0.13, 0.02, 0.72])
            plt.colorbar(pcolormesh, cax=cax, orientation='vertical')
        self.finished.emit(self.subplot_object)
    
    def stop(self):
        logging.debug('gui - thread_functions.py - DrawGriddedMap - stop')
        self.terminate()


class ProvideWidthHeight(QtCore.QThread):
    
    def __init__(self, height_widget, width_widget):
        QtCore.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - ProvideWidthHeight - __init__')
        self.height_widget = height_widget
        self.width_widget = width_widget
        
    def run(self):
        logging.debug('gui - thread_functions.py - ProvideWidthHeight - run')
        time.sleep(1)
        self.height_widget.setText(str(6.2))
        self.width_widget.setText(str(11.52))
    
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
        egads_instance = None
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
                f = egads.input.NasaAmes(self.file_path, 'r')
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
                    logging.exception('gui - reading_functions.py - : an error occured during the reading of a '
                                      'variable, variable ' + str(var))
            for var in unread_var:
                var_list.remove(var)
            final_dict = {'dim_list': dim_list, 'var_list': var_list, 'unread_var': unread_var,
                          'var_attr_list': var_attr_list, 'glob_attr_list': glob_attr_list, 'opened_file': f}
            self.finished.emit(final_dict)
        except Exception:
            logging.exception('gui - reading_functions.py - : an error occured during the reading of a file')
            self.error.emit()

    def stop(self):
        logging.debug('gui - thread_functions.py - ReadFileThread - stop')
        self.terminate()
