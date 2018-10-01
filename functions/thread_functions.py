import os
import logging
import time
import cartopy
import collections
#from cmocean import cm as cmo
from PyQt5 import QtCore, Qt, QtWidgets
from ui._version import _gui_version
from egads._version import __version__ as _egads_version
from distutils.version import LooseVersion
from docutils.nodes import row
import matplotlib.pyplot as plt



'''class CheckEGADSGuiUpdateOnline(Qt.QThread):
    finished = QtCore.pyqtSignal(str)

    def __init__(self):
        Qt.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - __init__')
    
    def run(self):
        logging.debug('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run')
        url = 'https://api.github.com/repos/eufarn7sp/egads-gui/releases/latest'
        try:
            json_object = requests.get(url=url).json()
            if LooseVersion(_gui_version) < LooseVersion(json_object['tag_name']):
                self.finished.emit(json_object['assets'][0]['browser_download_url'])
            else:
                self.finished.emit('no new version')
        except Exception:
            logging.exception('gui - thread_functions.py - CheckEGADSGuiUpdateOnline - run - internet connection error - url ' + url)
         
    def stop(self):
        self.terminate()'''
        

class CheckEGADSVersion(Qt.QThread):
    version_issue = QtCore.pyqtSignal(dict)
    
    def __init__(self, egads_version, egads_branch, min_egads_version, gui_branch):
        Qt.QThread.__init__(self)
        self.egads_version = egads_version
        self.min_egads_version = min_egads_version
        self.egads_branch = egads_branch
        self.gui_branch = gui_branch
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - __init__')
        
    def run(self):
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - run')
        
        print(self.egads_version, self.egads_branch)
        
        version_issue = {'version': True,
                         'branch': True}
        if LooseVersion(self.egads_version) < LooseVersion(self.min_egads_version):
            logging.info('gui - thread_functions.py - CheckEGADSVersion - run - an old version of EGADS has been found: ' + self.egads_version)
            version_issue['version'] = False
        if self.egads_branch != self.gui_branch:
            logging.info('gui - thread_functions.py - CheckEGADSVersion - run - a different branch of EGADS has been found: ' + self.egads_branch)
            version_issue['branch'] = False
        if version_issue:
            self.version_issue.emit(version_issue)
    
    def stop(self):
        self.terminate()


class DrawGriddedMap(Qt.QThread):
    started = QtCore.pyqtSignal()
    finished  = QtCore.pyqtSignal(collections.OrderedDict)
    
    def __init__(self, subplot_object):
        Qt.QThread.__init__(self)
        self.subplot_object = subplot_object
        
    def run(self):
        self.started.emit()
        for key, subplot in self.subplot_object.items():
            pcolormesh = subplot['ax'].pcolormesh(subplot['lon_values'], subplot['lat_values'], subplot['var_values'], transform=subplot['projection'], cmap='jet')
            self.subplot_object[key]['pcolormesh'] = pcolormesh
            cax = plt.axes([0.9, 0.13, 0.02, 0.72])
            plt.colorbar(pcolormesh, cax=cax, orientation='vertical')
        
        self.finished.emit(self.subplot_object)
    
    def stop(self):
        self.terminate()


class ProvideWidthHeight(Qt.QThread):
    #finished  = QtCore.pyqtSignal(float())
    
    def __init__(self, height_widget, width_widget):
        Qt.QThread.__init__(self)
        self.height_widget = height_widget
        self.width_widget = width_widget
        
    def run(self):
        time.sleep(1)
        self.height_widget.setText(str(6.2))
        self.width_widget.setText(str(11.52))
    
    def stop(self):
        self.terminate()