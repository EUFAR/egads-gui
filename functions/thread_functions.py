import logging
import time
import collections
from PyQt5 import QtCore
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
                    lineage_list.append([egads_package['tag_name'], egads_package['assets'][2]['browser_download_url']])

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
        self.egads_version = egads_version
        self.min_egads_version = min_egads_version
        self.egads_branch = egads_branch
        self.gui_branch = gui_branch
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - __init__')
        
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
        self.subplot_object = subplot_object
        
    def run(self):
        self.started.emit()
        for key, subplot in self.subplot_object.items():
            pcolormesh = subplot['ax'].pcolormesh(subplot['lon_values'], subplot['lat_values'],
                                                  subplot['var_values'], transform=subplot['projection'], cmap='jet')
            self.subplot_object[key]['pcolormesh'] = pcolormesh
            cax = plt.axes([0.9, 0.13, 0.02, 0.72])
            plt.colorbar(pcolormesh, cax=cax, orientation='vertical')
        self.finished.emit(self.subplot_object)
    
    def stop(self):
        self.terminate()


class ProvideWidthHeight(QtCore.QThread):
    
    def __init__(self, height_widget, width_widget):
        QtCore.QThread.__init__(self)
        self.height_widget = height_widget
        self.width_widget = width_widget
        
    def run(self):
        time.sleep(1)
        self.height_widget.setText(str(6.2))
        self.width_widget.setText(str(11.52))
    
    def stop(self):
        self.terminate()


class VariableProcessingThread(QtCore.QThread):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal()

    def __init__(self, algorithm, list_combobox_input, list_edit_output, list_of_variables_and_attributes):
        QtCore.QThread.__init__(self)
        self.algorithm = algorithm
        self.list_combobox_input = list_combobox_input
        self.list_edit_output = list_edit_output
        self.list_of_variables_and_attributes = list_of_variables_and_attributes
        self.list_of_new_variables_and_attributes = dict()

    def run(self):
        self.started.emit()
        try:
            args = []
            sublist = None
            dimension_out = None
            index = None
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
                    metadata = dict()
                    metadata["var_name"] = str(self.list_edit_output[index].text())
                    metadata["units"] = output[index].metadata["units"]
                    metadata["_FillValue"] = self.list_of_variables_and_attributes[
                        self.list_combobox_input[0].currentText()]
                    metadata["Processor"] = self.algorithm().metadata["Processor"]
                    metadata["long_name"] = output[index].metadata["long_name"]
                    metadata["standard_name"] = output[index].metadata["standard_name"]
                    metadata["DateProcessed"] = output[index].metadata["DateProcessed"]
                    metadata["Category"] = output[index].metadata["Category"]
                    dimensions = dimension_out
                    self.list_of_new_variables_and_attributes[str(self.list_edit_output[index].text())] = [
                        str(self.list_edit_output[index].text()),
                        metadata,
                        dimensions,
                        output[index]]
            else:
                metadata = dict()
                metadata["var_name"] = str(self.list_edit_output[0].text())
                metadata["units"] = output.metadata["units"]
                try:
                    metadata["_FillValue"] = self.list_of_variables_and_attributes[self.list_combobox_input[
                        0].currentText()][1]["_FillValue"]
                except KeyError:
                    metadata["_FillValue"] = ''
                metadata["Processor"] = self.algorithm().metadata["Processor"]
                metadata["long_name"] = output.metadata["long_name"]
                metadata["standard_name"] = output[index].metadata["standard_name"]
                metadata["DateProcessed"] = output.metadata["DateProcessed"]
                metadata["Category"] = output.metadata["Category"]
                dimensions = dimension_out
                self.list_of_new_variables_and_attributes[str(self.list_edit_output[0].text())] = [
                    str(self.list_edit_output[0].text()),
                    metadata,
                    dimensions,
                    output]
            self.finished.emit(self.list_of_new_variables_and_attributes)
        except Exception:
            logging.exception('gui - algorithm_window_functions.py - MyProcessing - close_window_save: an exception '
                              'occurred')
            self.error.emit()

    def stop(self):
        self.terminate()
