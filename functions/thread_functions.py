# -*- coding: utf-8 -*-


import os
import logging
import requests
import time
from PyQt5 import QtCore, Qt
from ui._version import _gui_version
from egads._version import __version__ as _egads_version
from distutils.version import LooseVersion


class CheckEGADSGuiUpdateOnline(Qt.QThread):
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
        self.terminate()
        

class CheckEGADSVersion(Qt.QThread):
    deprecated = QtCore.pyqtSignal()
    
    def __init__(self):
        Qt.QThread.__init__(self)
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - __init__')
        
    def run(self):
        logging.debug('gui - thread_functions.py - CheckEGADSVersion - run')
        time.sleep(3)
        if LooseVersion(_egads_version) < LooseVersion('0.8.8'):
            self.deprecated.emit()
    
    def stop(self):
        self.terminate()
        
        