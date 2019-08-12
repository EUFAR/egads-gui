import logging
import platform
import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.mainwindow import MainWindow
from ui._version import _gui_version
from functions.utils import create_option_file, create_logging_handlers
import configparser
from PyQt5.QtCore import QT_VERSION_STR as qt_version
from matplotlib import __version__ as mpl_version
from cartopy import __version__ as cy_version
from simplekml import __version__ as km_version


def launch_egads_gui(gui_path):
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('icons/egads_gui_splashscreen.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.show()
    if getattr(sys, 'frozen', False):
        frozen = True
    else:
        frozen = False
    if not os.path.exists(os.path.join(gui_path, 'egads_gui.ini')):
        create_option_file(gui_path)
    config_dict = configparser.ConfigParser()
    config_dict.read(os.path.join(gui_path, 'egads_gui.ini'))
    create_logging_handlers(config_dict, 'egads_gui.log', gui_path)
    logging.info('**********************************')
    logging.info('EGADS GUI ' + _gui_version + ' is starting ...')
    logging.info('**********************************')
    logging.debug('gui - gui frozen ? ' + str(frozen))
    system, release, version = platform.system_alias(platform.system(), platform.release(), platform.version())
    logging.debug('gui - operating system: ' + system + ' ' + release + ' (' + version + ')')
    python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
    logging.debug('gui - python version: ' + python_version)
    logging.debug('gui - pyqt5 version: ' + qt_version)
    logging.debug('gui - matplotlib version: ' + mpl_version)
    logging.debug('gui - cartopy version: ' + cy_version)
    logging.debug('gui - simplekml version: ' + km_version)
    ui = MainWindow(gui_path, config_dict, frozen)
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
    main_path = os.path.abspath(os.path.dirname(__file__))
    launch_egads_gui(main_path)
