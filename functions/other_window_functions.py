# -*- coding: utf-8 -*-

import logging
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_displaywindow import Ui_displayWindow
from ui.Ui_logwindow import Ui_Changelog
from ui.Ui_aboutwindow import Ui_aboutWindow
from ui.Ui_addcategory import Ui_Addcategory
from ui.Ui_fillwindow import Ui_fillWindow
from ui.Ui_filenamewindow import Ui_Addfilename
from ui.Ui_unitwindow import Ui_unitWindow
from ui.Ui_presavewindow import Ui_presaveWindow
from ui.Ui_optionwindow import Ui_optionWindow
from ui.Ui_downloadwindow import Ui_downloadWindow
from functions.thread_functions import CheckEGADSGuiUpdateOnline

 
class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        logging.debug('gui - other_window_functions.py - MyInfo - __init__ : infoText ' + str(infoText))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)
        logging.info('gui - other_window_functions.py - MyInfo ready')

    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyInfo - closeWindow')
        self.close()


class MyDisplay(QtWidgets.QDialog, Ui_displayWindow):
    def __init__(self, variable):
        logging.debug('gui - other_window_functions.py - MyDisplay - __init__ : variable ' + str(variable[1]["var_name"]) )
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.variable = variable
        self.dw_line_1.setText(self.variable[1]["var_name"])
        self.dw_line_2.setText(self.variable[1]["units"])
        self.dw_okButton.clicked.connect(self.closeWindow)
        self.populate_table()
        logging.info('gui - other_window_functions.py - MyDisplay ready')

        
    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyDisplay - closeWindow')
        self.close()
        
        
    def populate_table(self):
        logging.debug('gui - other_window_functions.py - MyDisplay - populate_table')
        col, row = 1, 1
        try:
            col = self.variable[3].value.shape[0]
            row = self.variable[3].value.shape[1]
        except IndexError:
            col = self.variable[3].value.shape[0]
        self.dw_table.setRowCount(row)
        self.dw_table.setColumnCount(col)
        if row == 1:
            for x in range(col):
                try:
                    if self.variable[3].value[x] == self.variable[1]["_FillValue"]:
                        self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem("NaN"))
                    else:
                        self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[x])))
                except KeyError:
                    logging.exception('gui - other_window_functions.py - MyDisplay - populate_table : no _FillValue')
                    try: 
                        if self.variable[3].value[x] == self.variable[1]["missing_value"]:
                            self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem("NaN"))
                        else:
                            self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[x])))
                    except KeyError:
                        logging.exception('gui - other_window_functions.py - MyDisplay - populate_table : no missing_value')
                        self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[x])))
        else:
            for y in range(row):
                for x in range(col):
                    self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.variable[3].value[y][x])))

        
class MyLog(QtWidgets.QDialog, Ui_Changelog):
    def __init__(self):
        logging.debug('gui - other_window_functions.py - MyLog - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.log_txBrower.setPlainText(open("Documentation/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        logging.info('gui - other_window_functions.py - MyLog ready')
        
    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyLog - closeWindow')
        self.close()
    
    
class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        logging.debug('gui - other_window_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)
        logging.info('gui - other_window_functions.py - MyAbout ready')

    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyAbout - closeWindow')
        self.close()


class MyCategory(QtWidgets.QDialog, Ui_Addcategory):
    def __init__(self):
        logging.debug('gui - other_window_functions.py - MyCategory - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_window_functions.py - MyCategory ready')
        
    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyCategory - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_window_functions.py - MyCategory - submitBox')
        self.accept() 
        
        
class MyFilename(QtWidgets.QDialog, Ui_Addfilename):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('gui - other_window_functions.py - MyFilename - __init__')
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_window_functions.py - MyFilename ready')
        
    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyFilename - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_window_functions.py - MyFilename - submitBox')
        self.accept()        
        
        
class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self):
        logging.debug('gui - other_window_functions.py - MyFill - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.fw_cancelButton.clicked.connect(self.cancelWindow)
        self.cancel = False
        self.fw_cancelButton.setFocus(True)
        logging.info('gui - other_window_functions.py - MyFill ready')

    def cancelWindow(self):
        logging.debug('gui - other_window_functions.py - MyFill - cancelWindow')
        self.cancel = True
        self.close()
        
        
class MyUnit(QtWidgets.QDialog, Ui_unitWindow):
    def __init__(self, units_list):
        logging.debug('gui - other_window_functions.py - MyUnit - __init__ : unit_list ' + str(unit_list))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.units_list = units_list
        self.uw_label.setText(self.prepare_text())
        self.uw_cancelButton.clicked.connect(self.closeWindow)
        self.uw_okButton.clicked.connect(self.submitBox)
        logging.info('gui - other_window_functions.py - MyUnit ready')
    
    def prepare_text(self):
        logging.debug('gui - other_window_functions.py - MyUnit - prepare_text')
        if len(self.units_list) > 1:
            text = ('<p>Too handle units properly, EGADS must validate and, probably, rewrite input and out'
                    + 'put units. Please check the <b>proposals</b> made by EGADS, and click Continue if you '
                    + 'are agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><ul><li>Inputs:<ul>')
            for sublist in self.units_list:
                if sublist[3] == 'input':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;<b>' + sublist[2] + '</b></li>'
            text += '</ul></li><br><li>Outputs:<ul>'
            for sublist in self.units_list:
                if sublist[3] == 'output':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;<b>' + sublist[2] + '</b></li>'
            text += '</ul></li></ul>'
        else:
            text = ('<p>Too handle units properly, EGADS must validate units in the current window. '
                    + 'Please check the <b>proposal</b> made by EGADS, and click Continue if you '
                    + 'are agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><p>Proposal:<br>')
            text += ('&nbsp;&nbsp;&nbsp;&nbsp;' + self.units_list[0][0] + ':&nbsp;&nbsp;&nbsp;&nbsp;' + self.units_list[0][1] 
                     + '&nbsp;&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;&nbsp;<b>' + self.units_list[0][2] + '</b></p>')
        return text
    
    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyUnit - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_window_functions.py - MyUnit - submitBox')
        self.accept()  
        
        
class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, button_string, title_string):
        logging.debug('gui - other_window_functions.py - MyWarning - __init__ : button_string ' + str(button_string)
                      + ', title_string ' + str(title_string))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            widget.clicked.connect(lambda: self.closeWindow())
        self.iw_nosaveButton.setText(button_string + " without saving")
        self.setWindowTitle(title_string)
        logging.info('gui - other_window_functions.py - MyWarning ready')

    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyWarning - closeWindow : sender().objectName() '
                      + str(self.sender().objectName()))
        self.buttonName = self.sender().objectName()
        self.close()


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict):
        logging.debug('gui - other_window_functions.py - MyOptions - __init__ ')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.ow_comboBox_1.setItemDelegate(itemDelegate)
        self.config_dict = config_dict
        self.ow_okButton.clicked.connect(self.save_config_dict)
        self.ow_cancelButton.clicked.connect(self.closeWindow)
        self.ow_checkButton.clicked.connect(self.check_gui_update)
        self.cancel = True
        self.read_config_dict()
        logging.info('gui - other_window_functions.py - MyOptions ready')

    def read_config_dict(self):
        self.ow_comboBox_1.setCurrentIndex(self.ow_comboBox_1.findText(self.config_dict.get('LOG', 'level')))
        self.ow_lineEdit.setText(self.config_dict.get('LOG', 'path'))
        self.ow_checkBox_1.setChecked(self.config_dict.getboolean('OPTIONS', 'check_update'))


    def check_gui_update(self):
        logging.debug('gui - other_window_functions.py - MyOptions - check_gui_update')
        self.check_gui_update = CheckEGADSGuiUpdateOnline()
        self.check_gui_update.start()
        self.check_gui_update.finished.connect(self.parse_egads_gui_update)
        
    def parse_egads_gui_update(self, val):
        logging.debug('gui - other_window_functions.py - MyOptions - parse_egads_gui_update - val ' + str(val))
        if val != 'no new version':
            self.updade_window = MyUpdate(val)
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.updade_window.geometry().getRect()
            x2 = x1 + w1/2 - w2/2
            y2 = y1 + h1/2 - h2/2
            self.updade_window.setGeometry(x2, y2, w2, h2)
            self.updade_window.setModal(True)
            self.updade_window.exec_()


    def save_config_dict(self):
        logging.debug('gui - other_window_functions.py - MyOptions - save_config_dict')
        self.cancel = False
        self.config_dict.set('LOG','level',self.ow_comboBox_1.currentText())
        self.config_dict.set('LOG','path', self.ow_lineEdit.text())
        self.config_dict.set('OPTIONS','check_update', self.ow_checkBox_1.isChecked())
        self.closeWindow()


    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyOptions - closeWindow')
        self.close()


class MyUpdate(QtWidgets.QDialog, Ui_downloadWindow):
    def __init__(self, url):
        logging.debug('gui - other_window_functions.py - MyUpdate - __init__ ')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.url = url
        self.dw_okButton.clicked.connect(self.closeWindow)
        self.dw_downloadButton.clicked.connect(self.download_file)
        self.dw_downloadButton_2.clicked.connect(self.visit_github)
        logging.info('gui - other_window_functions.py - MyUpdate ready')

    def visit_github(self):
        webbrowser.open('https://github.com/eufarn7sp/egads-gui')


    def download_file(self):
        logging.debug('gui - other_window_functions.py - MyUpdate - download_file')
        webbrowser.open(self.url)


    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyUpdate - closeWindow')
        self.close()


        