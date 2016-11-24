# -*- coding: utf-8 -*-

import logging
from PyQt4 import QtGui
from ui.mainwindow import MainWindow


def launch_egads_gui():
    logging.getLogger('').handlers = []
    logging.basicConfig(filename = 'myapp.log',
                        level = logging.DEBUG,
                        filemode = 'w',
                        format = '%(asctime)s : %(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('Main - EGADS GUI launch')
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch_egads_gui()