# -*- coding: utf-8 -*-

import logging
import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.mainwindow import MainWindow
from ui._version import _gui_version
from egads._version import __version__ as egads_version
import ConfigParser


def launch_egads_gui(path):
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('icons/egads_gui_splashscreen.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    config_dict = ConfigParser.ConfigParser()
    if not os.path.exists(os.path.join(path, 'egads_gui.ini')):
        ini_file = open(os.path.join(path, 'egads_gui.ini'), 'w')
        config_dict.add_section('LOG')
        config_dict.add_section('OPTIONS')
        config_dict.set('LOG','level','DEBUG')
        config_dict.set('LOG','path', '')
        config_dict.set('OPTIONS','check_update','False')
        config_dict.write(ini_file)
        ini_file.close()   
    config_dict.read(os.path.join(path, 'egads_gui.ini'))
    log_filename = os.path.join(config_dict.get('LOG', 'path'),'egads_gui.log')
    logging.getLogger('').handlers = []
    logging.basicConfig(filename = log_filename,
                        level = getattr(logging, config_dict.get('LOG', 'level')),
                        filemode = 'w',
                        format = '%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('**********************************')
    logging.info('EGADS GUI ' + _gui_version + ' is starting ...')
    logging.info('**********************************')
    logging.info('gui - operating system: ' + str(sys.platform))
    python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
    logging.info('gui - python version: ' + python_version)
    logging.info('gui - egads version: ' + egads_version)
    
    ui = MainWindow(path, config_dict)
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    launch_egads_gui(path)
    
