# -*- coding: utf-8 -*-

import logging
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.mainwindow import MainWindow


def launch_egads_gui():
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('icons/egads_gui_splashscreen.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    ui = MainWindow()
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
    logging.getLogger('').handlers = []
    logging.basicConfig(filename = 'egads_gui.log',
                        level = logging.DEBUG,
                        filemode = 'w',
                        format = '%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('**********************************')
    logging.info('EGADS GUI is starting ...')
    logging.info('**********************************')
    launch_egads_gui()