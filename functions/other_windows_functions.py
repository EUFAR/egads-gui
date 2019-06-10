import logging
import numpy
import datetime
import webbrowser
import egads
import pathlib
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_displaywindow import Ui_displayWindow
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_addcategorywindow import Ui_Addcategory
from ui.Ui_fillwindow import Ui_fillWindow
from ui.Ui_filenamewindow import Ui_Addfilename
from ui.Ui_unitwindow import Ui_unitWindow
from ui.Ui_optionwindow import Ui_optionWindow
from ui.Ui_waitwindow import Ui_waitWindow
from ui.Ui_downloadwindow import Ui_downloadWindow
from ui.Ui_coefwindow import Ui_coefWindow
from ui.Ui_asksavewindow import Ui_asksaveWindow
from functions.thread_functions import CheckEGADSGuiUpdateOnline
from functions.gui_elements import QtWaitingSpinner
from ui._version import _gui_version
from functions.material_functions import options_information_buttons_text


class MyAsk(QtWidgets.QDialog, Ui_asksaveWindow):
    def __init__(self, text):
        logging.debug('gui - other_windows_functions.py - MyAsk - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.choice = None
        self.cancel_button.clicked.connect(self.cancel_choice)
        self.save_button.clicked.connect(self.save_choice)
        self.close_button.clicked.connect(self.close_choice)
        self.close_button.setText(text + ' without saving')
        logging.info('gui - other_windows_functions.py - MyAsk ready')

    def save_choice(self):
        logging.info('gui - other_windows_functions.py - MyAsk - save_choice')
        self.choice = 'save'
        self.closeWindow()

    def close_choice(self):
        logging.info('gui - other_windows_functions.py - MyAsk - close_choice')
        self.choice = 'close'
        self.closeWindow()

    def cancel_choice(self):
        logging.info('gui - other_windows_functions.py - MyAsk - cancel_choice')
        self.choice = 'cancel'
        self.closeWindow()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyAsk - closeWindow')
        self.close()


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, info_text):
        logging.debug('gui - other_windows_functions.py - MyInfo - __init__ : infoText ' + str(info_text))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(info_text)
        self.iw_okButton.clicked.connect(self.closeWindow)
        logging.info('gui - other_windows_functions.py - MyInfo ready')

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyInfo - closeWindow')
        self.close()


class MyDisplay(QtWidgets.QDialog, Ui_displayWindow):
    def __init__(self, var_name, var_units, fill_value, var_values, dimensions):
        logging.debug('gui - other_windows_functions.py - MyDisplay - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.fill_value = fill_value
        self.var = var_values
        self.dimensions = dimensions
        self.splitter.setSizes([100, 200])
        self.dw_line_1.setText(var_name)
        self.dw_line_2.setText(var_units)
        self.dw_okButton.clicked.connect(self.closeWindow)
        self.current_row = 0
        self.current_col = 0
        self.dw_label_4.setVisible(False)
        self.dw_label_5.setText('')
        self.dw_label_5.setVisible(False)
        self.gridLayout_2.removeWidget(self.dw_label_5)
        self.dw_label_5.deleteLater()
        self.populate_dimensions()
        self.populate_table()
        logging.info('gui - other_windows_functions.py - MyDisplay ready')

    def connect_scrollbars(self):
        h_scrollbar = self.dw_table.horizontalScrollBar()
        v_scrollbar = self.dw_table.verticalScrollBar()
        h_scrollbar.valueChanged.connect(lambda val: self.load_more_data(val, col=True))
        v_scrollbar.valueChanged.connect(lambda val: self.load_more_data(val, row=True))
        
    def load_more_data(self, val, row=False, col=False):
        if row:
            self.current_row = val
        elif col:
            self.current_col = val
        for x in range(self.current_col - 20, self.current_col + 20):
            for y in range(self.current_row - 20, self.current_row + 20):
                try:     
                    if not self.dw_table.item(y, x):
                        self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[y, x])))
                except IndexError:
                    pass

    def populate_dimensions(self):
        dimensions_str = ''
        for key, value in self.dimensions.items():
            dimensions_str = dimensions_str + str(value['length']) + ' (' + key + '), '
        self.dw_line_3.setText(dimensions_str[:-2])
        
    def populate_table(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - populate_table')
        if self.fill_value is not None:
            try:
                self.var[self.var == self.fill_value] = numpy.nan
            except ValueError:
                pass
        data_shape = self.var.shape
        row, col = None, None
        if len(data_shape) >= 3 and data_shape[0] > 1 and data_shape[1] > 1 and data_shape[2] > 1:
            print('It is not possible to display data with 3 dimensions and more yet.')
        else:
            row, col = self.populate_headers()
        if row is not None:
            data_shape = self.var.shape
            if len(data_shape) > 1:
                connect = False
                if data_shape[0] > 50:
                    row = 50
                    connect = True
                if data_shape[1] > 50:
                    col = 50
                    connect = True
                if connect:
                    self.connect_scrollbars()
                for x in range(col):
                    for y in range(row):
                        self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[y, x])))
            else:
                for x in range(col):
                    self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.var[x])))

    def populate_headers(self):
        dim_num = len(self.var.shape)
        row_size, col_size = None, None
        if dim_num == 1:
            col_size, row_size = self.var.shape[0], 1
            self.dw_table.setColumnCount(col_size)
            self.dw_table.setRowCount(row_size) 
            for dim, value in self.dimensions.items():
                self.dw_label_4.setVisible(True)
                if 'time' in dim.lower():
                    self.dw_label_4.setText('Time')
                    units = value['units']
                    if 'since' in units:
                        if 'days' in units or 'day' in units:
                            date = units[units.index('since') + 6:]
                            value['values'] = [str((datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:10]),
                                                                      0, 0) + datetime.timedelta(i - 1)).strftime(
                                "%Y-%m-%d")) for i in value['values']]
                elif dim.lower() in ['longitude', 'lon', 'long']:
                    self.dw_label_4.setText('Longitude')
                elif dim.lower() in ['latitude', 'lat']:
                    self.dw_label_4.setText('Latitude')
                val_list = [str(i) for i in value['values']]
                self.dw_table.setHorizontalHeaderLabels(val_list)
        elif dim_num == 2:
            time_in, lon_in, lat_in = False, False, False
            time_name = None
            lon_name = None
            for dim, value in self.dimensions.items():
                if 'time' in dim.lower():
                    time_in = True
                    time_name = dim
                if dim.lower() in ['longitude', 'lon', 'long']:
                    lon_in = True
                    lon_name = dim
            if time_in:
                if self.dimensions[time_name]['axis'] == 0:
                    self.var = numpy.transpose(self.var)
                row_size, col_size = self.var.shape
                self.dw_table.setColumnCount(col_size)
                self.dw_table.setRowCount(row_size)
                val_list = [str(i) for i in self.dimensions[time_name]['values']]
                self.dw_label_4.setVisible(True)
                self.dw_label_4.setText('Time')
                self.dw_table.setHorizontalHeaderLabels(val_list)
                self.dimensions.pop(time_name)
                for key, value in self.dimensions.items():
                    val_list = [str(i) for i in value['values']]
                    self.dw_table.setVerticalHeaderLabels(val_list)
                    self.set_row_label(key.title())
            else:
                if lon_in:
                    if self.dimensions[lon_name]['axis'] == 0:
                        self.var = numpy.transpose(self.var)
                    row_size, col_size = self.var.shape
                    self.dw_table.setColumnCount(col_size)
                    self.dw_table.setRowCount(row_size)
                    val_list = [str(i) for i in self.dimensions[lon_name]['values']]
                    self.dw_label_4.setVisible(True)
                    self.dw_label_4.setText('Longitude')
                    self.dw_table.setHorizontalHeaderLabels(val_list)
                    self.dimensions.pop(lon_name)
                    for key, value in self.dimensions.items():
                        val_list = [str(i) for i in value['values']]
                        self.dw_table.setVerticalHeaderLabels(val_list)
                        self.set_row_label(key.title())
                else:
                    row_size, col_size = self.var.shape
                    self.dw_table.setColumnCount(col_size)
                    self.dw_table.setRowCount(row_size)
        elif dim_num == 3:
            time_in, lon_in, lat_in = False, False, False
            time_name, lon_name = None, None
            for dim, value in self.dimensions.items():
                if value['length'] == 1:
                    self.var = numpy.squeeze(self.var, value['axis'])
                    break
            self.dimensions.pop(dim)
            for dim, value in self.dimensions.items():
                if 'time' in dim.lower():
                    time_in = True
                    time_name = dim
                if dim.lower() in ['longitude', 'lon', 'long']:
                    lon_in = True
                    lon_name = dim
            if time_in:
                if self.dimensions[time_name]['axis'] == 0:
                    self.var = numpy.transpose(self.var)
                val_list = [str(i) for i in self.dimensions[time_name]['values']]
                row_size, col_size = self.var.shape
                self.dw_table.setColumnCount(col_size)
                self.dw_table.setRowCount(row_size)
                self.dw_label_4.setVisible(True)
                self.dw_label_4.setText('Time')
                self.dw_table.setHorizontalHeaderLabels(val_list)
                self.dimensions.pop(time_name)
                for key, value in self.dimensions.items():
                    val_list = [str(i) for i in value['values']]
                    self.dw_table.setVerticalHeaderLabels(val_list)
                    self.set_row_label(key.title())
            else:
                if lon_in:
                    if self.dimensions[lon_name]['axis'] == 0:
                        self.var = numpy.transpose(self.var)
                    val_list = [str(i) for i in self.dimensions[lon_name]['values']]
                    row_size, col_size = self.var.shape
                    self.dw_table.setColumnCount(col_size)
                    self.dw_table.setRowCount(row_size)
                    self.dw_label_4.setVisible(True)
                    self.dw_label_4.setText('Longitude')
                    self.dw_table.setHorizontalHeaderLabels(val_list)
                    self.dimensions.pop(lon_name)
                    for key, value in self.dimensions.items():
                        val_list = [str(i) for i in value['values']]
                        self.dw_table.setVerticalHeaderLabels(val_list)
                        self.set_row_label(key.title())
                else:
                    row_size, col_size = self.var.shape
                    self.dw_table.setColumnCount(col_size)
                    self.dw_table.setRowCount(row_size)   
        return row_size, col_size
            
    def set_row_label(self, text):
        self.dw_label_5 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_label_5.setFont(font)
        self.dw_label_5.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "    margin-bottom: 5px;\n"
                                      "}")
        self.dw_label_5.setText(text)
        self.dw_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.dw_label_5.setObjectName("dw_label_5")
        self.gridLayout_2.addWidget(self.dw_label_5, 1, 0, 1, 1)

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - closeWindow')
        self.close()
    
    
class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, text):
        logging.info('gui - other_windows_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.browser_1.setHtml(text)
        self.browser_2.setPlainText(open("documentation/changelog.txt").read())
        self.button.clicked.connect(self.closeWindow)
        self.splitter.setSizes([170, 130])

    def closeWindow(self):
        logging.info('gui - other_windows_functions.py - MyAbout - closeWindow')
        self.close()


class MyCategory(QtWidgets.QDialog, Ui_Addcategory):
    def __init__(self):
        logging.debug('gui - other_windows_functions.py - MyCategory - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.close_window)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyCategory ready')

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyCategory - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyCategory - submitBox')
        self.accept()
        
        
class MyFilename(QtWidgets.QDialog, Ui_Addfilename):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('gui - other_windows_functions.py - MyFilename - __init__')
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyFilename ready')

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyFilename - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyFilename - submitBox')
        self.accept()


class MyOverwriteFilename(QtWidgets.QDialog, Ui_Addfilename):
    def __init__(self, old_filename, category):
        QtWidgets.QWidget.__init__(self)
        logging.debug('gui - other_windows_functions.py - MyOverwriteFilename - __init__')
        self.setupUi(self)
        self.old_filename = old_filename
        self.ac_label.setText('A file with the same name already exists in the ' + category + ' folder. You can '
                              + 'overwrite the file, or choose another name.')
        self.ac_submitButton.setText('Overwrite')
        self.ac_line.setText(self.old_filename)
        self.ac_line.textChanged.connect(self.check_filename)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyOverwriteFilename ready')

    def check_filename(self):
        new_filename = str(self.ac_line.text())
        if self.old_filename == new_filename or self.old_filename == new_filename + '.py':
            self.ac_submitButton.setText('Overwrite')
        else:
            self.ac_submitButton.setText('Submit')

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyOverwriteFilename - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyOverwriteFilename - submitBox')
        self.accept()
        
        
class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self):
        logging.debug('gui - other_windows_functions.py - MyFill - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.fw_cancelButton.clicked.connect(self.cancel_window)
        self.fw_okButton.clicked.connect(self.closeWindow)
        self.cancel = False
        self.fw_cancelButton.setFocus(True)
        logging.info('gui - other_windows_functions.py - MyFill ready')

    def cancel_window(self):
        logging.debug('gui - other_windows_functions.py - MyFill - cancel_window')
        self.cancel = True
        self.closeWindow()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyFill - closeWindow')
        self.close()
        
        
class MyUnit(QtWidgets.QDialog, Ui_unitWindow):
    def __init__(self, units_list):
        logging.debug('gui - other_windows_functions.py - MyUnit - __init__ : unit_list ' + str(units_list))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.units_list = units_list
        self.uw_label.setText(self.prepare_text())
        self.uw_cancelButton.clicked.connect(self.closeWindow)
        self.uw_okButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyUnit ready')
    
    def prepare_text(self):
        logging.debug('gui - other_windows_functions.py - MyUnit - prepare_text')
        if len(self.units_list) > 1:
            text = ('<p>Too handle units properly, EGADS must validate and, probably, rewrite input and out'
                    + 'put units. Please check the <b>proposals</b> made by EGADS, and click Continue if you '
                    + 'are agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><ul><li><u>Inputs:</u><ul>')
            for sublist in self.units_list:
                if sublist[3] == 'input':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;' \
                                                                                       '&nbsp;&nbsp;<b>' + sublist[2]\
                            + '</b></li>'
            text += '</ul></li><br><li><u>Outputs:</u><ul>'
            for sublist in self.units_list:
                if sublist[3] == 'output':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;' \
                                                                                       '&nbsp;&nbsp;<b>' + sublist[2]\
                            + '</b></li>'
            text += '</ul></li></ul>'
        else:
            text = ('<p>Too handle units properly, EGADS must validate units in the current window. '
                    + 'Please check the <b>proposal</b> made by EGADS, and click Continue if you '
                    + 'are agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><p><u>Proposal:</u><br>')
            text += ('&nbsp;&nbsp;&nbsp;&nbsp;' + self.units_list[0][0] + ':&nbsp;&nbsp;&nbsp;&nbsp;' +
                     self.units_list[0][1] + '&nbsp;&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;&nbsp;<b>' +
                     self.units_list[0][2] + '</b></p>')
        return text
    
    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyUnit - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyUnit - submitBox')
        self.accept()


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict):
        logging.info('gui - other_windows_functions.py - MyOptions - __init__ ')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        options_information_buttons_text(self)
        self.combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ok_button.clicked.connect(self.save_config_dict)
        self.cancel_button.clicked.connect(self.closeWindow)
        self.check_button.clicked.connect(self.check_gui_update)
        self.info_button_1.clicked.connect(self.button_info)
        self.info_button_2.clicked.connect(self.button_info)
        self.info_button_3.clicked.connect(self.button_info)
        self.info_button_4.clicked.connect(self.button_info)
        self.info_button_5.clicked.connect(self.button_info)
        self.info_button_6.clicked.connect(self.button_info)
        self.open_button_1.clicked.connect(self.get_folder_path)
        self.checkbox_3.clicked.connect(self.activate_checkbox_4)
        self.cancel = True
        self.read_config_dict()

    def activate_checkbox_4(self):
        if self.checkbox_3.isChecked():
            self.checkbox_4.setEnabled(True)
        else:
            self.checkbox_4.setChecked(False)
            self.checkbox_4.setEnabled(False)

    def read_config_dict(self):
        logging.debug('gui - other_windows_functions.py - MyOptions - read_config_dict')
        self.combobox_1.setCurrentIndex(self.combobox_1.findText(self.config_dict.get('LOG', 'level')))
        self.line_1.setText(self.config_dict.get('LOG', 'path'))
        self.checkbox_1.setChecked(self.config_dict.getboolean('OPTIONS', 'check_update'))
        self.checkbox_2.setChecked(self.config_dict.getboolean('SYSTEM', 'read_as_float'))
        self.checkbox_3.setChecked(self.config_dict.getboolean('SYSTEM', 'replace_fill_value'))
        self.checkbox_4.setChecked(self.config_dict.getboolean('SYSTEM', 'switch_fill_value'))
        self.activate_checkbox_4()

    def check_gui_update(self):
        logging.debug('gui - other_windows_functions.py - MyOptions - check_gui_update')
        self.check_gui_update_thread = CheckEGADSGuiUpdateOnline(_gui_version)
        self.check_gui_update_thread.start()
        self.check_gui_update_thread.finished.connect(self.parse_egads_gui_update)
        
    def parse_egads_gui_update(self, val):
        logging.debug('gui - other_windows_functions.py - MyOptions - parse_egads_gui_update - val ' + str(val))
        if val != 'no new version':
            self.updade_window = MyUpdate(val)
            self.updade_window.exec_()
        else:
            info_text = 'No new update available on GitHub.'
            self.infoWindow = MyInfo(info_text)
            self.infoWindow.exec_()

    def save_config_dict(self):
        logging.debug('gui - other_windows_functions.py - MyOptions - save_config_dict')
        self.cancel = False
        self.config_dict.set('LOG', 'level', self.combobox_1.currentText())
        self.config_dict.set('LOG', 'path', self.line_1.text())
        self.config_dict.set('SYSTEM', 'read_as_float', str(self.checkbox_2.isChecked()))
        self.config_dict.set('SYSTEM', 'replace_fill_value', str(self.checkbox_3.isChecked()))
        self.config_dict.set('SYSTEM', 'switch_fill_value', str(self.checkbox_4.isChecked()))
        self.config_dict.set('OPTIONS', 'check_update', str(self.checkbox_1.isChecked()))
        self.closeWindow()

    def button_info(self):
        self.infoWindow = MyInfo(self.information_buttons_text[self.sender().objectName()])
        self.infoWindow.exec_()

    def get_folder_path(self):
        logging.debug('gui - other_windows_functions.py - MyOptions - get_folder_path')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.line_1.setText(str(pathlib.Path(folder_path)))

    def closeWindow(self):
        logging.info('gui - other_windows_functions.py - MyOptions - closeWindow')
        self.close()


class MyUpdate(QtWidgets.QDialog, Ui_downloadWindow):
    def __init__(self, url):
        logging.debug('gui - other_windows_functions.py - MyUpdate - __init__ ')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.url = url
        self.dw_okButton.clicked.connect(self.closeWindow)
        self.dw_downloadButton.clicked.connect(self.download_file)
        self.dw_downloadButton_2.clicked.connect(self.visit_github)
        logging.info('gui - other_windows_functions.py - MyUpdate ready')

    def visit_github(self):
        webbrowser.open('https://github.com/EUFAR/egads-gui/tree/Lineage')

    def download_file(self):
        logging.debug('gui - other_windows_functions.py - MyUpdate - download_file')
        webbrowser.open(self.url)

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyUpdate - closeWindow')
        self.close()


class MyWait(QtWidgets.QDialog, Ui_waitWindow):
    def __init__(self, info_text):
        logging.debug('gui - other_windows_functions.py - MyWait - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.label.setText(info_text)
        self.spinner = None
        self.setup_spinner()
        
    def setup_spinner(self):
        self.spinner = QtWaitingSpinner(self, centerOnParent=False)
        self.verticalLayout.addWidget(self.spinner)
        self.spinner.setRoundness(70.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(12)
        self.spinner.setLineLength(10)
        self.spinner.setLineWidth(5)
        self.spinner.setInnerRadius(10)
        self.spinner.setRevolutionsPerSecond(1)
        self.spinner.setColor(QtGui.QColor(45, 45, 45))
        self.spinner.start()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyWait - closeWindow')
        self.close()


class MyCoeff(QtWidgets.QDialog, Ui_coefWindow):
    def __init__(self, matrix_nbr_str, coefficient_data, variable_list):
        logging.debug('gui - other_windows_functions.py - MyCoeff - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.combobox.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.coefficient_data = coefficient_data
        self.matrix_nbr_str = matrix_nbr_str
        self.variable_list = variable_list
        self.ok_button.clicked.connect(self.set_coef)
        self.cancel_button.clicked.connect(self.closeWindow)
        self.combobox.currentTextChanged.connect(self.populate_table)
        self.row = 0
        self.col = 0
        self.coef_array = None
        self.populate_variable_combobox()
        self.set_table()
        logging.info('gui - other_windows_functions.py - MyCoeff ready')

    def populate_table(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - populate_table')
        self.table.clear()
        if self.combobox.currentIndex() != 0:
            if isinstance(self.variable_list, str):
                f = egads.input.EgadsNetCdf(self.variable_list, 'r')
                self.parse_data(f.read_variable(str(self.combobox.currentText())).value)
                f.close()
            elif isinstance(self.variable_list, dict):
                self.parse_data(self.variable_list[str(self.combobox.currentText())][3].value)

    def parse_data(self, data):
        logging.debug('gui - other_windows_functions.py - MyCoeff - parse_data')
        try:
            row, col = data.shape
            if row == self.row and col == self.col:
                for i in range(row):
                    for j in range(col):
                        self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i, j])))
        except ValueError:
            var_len = data.shape
            if self.row == 1:
                if var_len == self.col:
                    for i in range(var_len):
                        self.table.setItem(0, i, QtWidgets.QTableWidgetItem(str(data[i])))
            if self.col == 1:
                if var_len == self.row:
                    for i in range(var_len):
                        self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data[i])))

    def populate_variable_combobox(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - populate_variable_combobox')
        variable_list = []
        if isinstance(self.variable_list, str):
            f = egads.input.EgadsNetCdf(self.variable_list, 'r')
            variable_list = f.get_variable_list()
            f.close()
        elif isinstance(self.variable_list, dict):
            for _, sublist in self.variable_list.items():
                if sublist[2] != 'deleted':
                    variable_list.append(sublist[1]["var_name"])
        self.combobox.addItem('Make a choice...')
        self.combobox.addItems(sorted(variable_list))

    def set_table(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - set_table')
        self.row = int(self.matrix_nbr_str[0])
        self.col = int(self.matrix_nbr_str[1])
        self.table.setColumnCount(self.col)
        self.table.setRowCount(self.row)
        x = self.table.verticalHeader().size().width()
        for i in range(self.table.columnCount()):
            x += self.table.columnWidth(i)
        y = self.table.horizontalHeader().size().height()
        for i in range(self.table.rowCount()):
            y += self.table.rowHeight(i)
        w, h = self.size().width(), self.size().height()
        if x + 30 > w:
            w = x + 30
        if y + 187 > h:
            h = y + 187
        self.resize(w, h)
        if self.coefficient_data is not None:
            self.parse_data(self.coefficient_data)

    def set_coef(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - set_coef')
        self.coef_array = numpy.zeros((self.table.rowCount(), self.table.columnCount()))
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.coef_array[i, j] = float(self.table.item(i, j).text())
        self.close()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - closeWindow')
        self.close()
