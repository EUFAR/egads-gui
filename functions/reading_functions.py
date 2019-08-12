import logging
import pathlib
from PyQt5 import QtCore, QtWidgets, QtGui
from ui.Ui_waitbatchwindow import Ui_waitBatchWindow
from functions.gui_functions import modify_attribute_gui, update_icons_state, clear_gui
from functions.gui_functions import update_global_attribute_gui, update_variable_attribute_gui, status_bar_update
from functions.gui_functions import netcdf_gui_initialization, nasaames_gui_initialization
from functions.material_functions import add_global_attributes_to_buttons
from functions.gui_elements import QtWaitingSpinner
from functions.thread_functions import ReadFileThread
from functions.other_windows_functions import MyInfo


def reading_file(self):
    logging.debug('gui - reading_functions.py - reading_file - file_name ' + self.file_name)
    clear_gui(self)
    self.reading_window = MyWaitReading(self.file_name, self.file_ext, self.config_dict)
    self.reading_window.exec_()
    if self.reading_window.error_occurred:
        info_str = ('An unexpected error occurred during the reading of the file, thus the GUI decided to stop the '
                    'reading. Please read the log file to check which kind of error occurred.')
        self.infoWindow = MyInfo(info_str)
        self.infoWindow.exec_()
    if self.reading_window.success:
        self.opened_file = self.reading_window.final_dict['opened_file']
        list_of_variables = self.reading_window.final_dict['var_list']
        self.list_of_global_attributes = self.reading_window.final_dict['glob_attr_list']
        self.list_of_dimensions = self.reading_window.final_dict['dim_list']
        self.list_of_variables_and_attributes = self.reading_window.final_dict['var_attr_list']
        self.list_of_unread_variables = self.reading_window.final_dict['unread_var']
        add_global_attributes_to_buttons(self)
        if self.file_ext == 'NetCDF Files (*.nc)':
            netcdf_gui_initialization(self)
            update_global_attribute_gui(self, 'NetCDF')
        elif self.file_ext == 'NASA Ames Files (*.na)':
            nasaames_gui_initialization(self)
            update_global_attribute_gui(self, 'NASA Ames')
        self.variable_list.addItems(list_of_variables)
        self.variable_list.itemClicked.connect(lambda: var_reading(self))
        self.tab_view.currentChanged.connect(lambda: update_icons_state(self))
        self.file_is_opened = True
        update_icons_state(self, 'open_file')
        status_bar_update(self)
        self.buttons_lines_dict["va_button_1"] = ["va_varName_ln", self.variable_list,
                                                  self.list_of_variables_and_attributes]
        self.buttons_lines_dict["va_button_2"] = ["va_longName_ln", self.variable_list,
                                                  self.list_of_variables_and_attributes]
        self.buttons_lines_dict["va_button_3"] = ["va_category_ln", self.variable_list,
                                                  self.list_of_variables_and_attributes]
        self.buttons_lines_dict["va_button_4"] = ["va_units_ln", self.variable_list,
                                                  self.list_of_variables_and_attributes]
        self.opened_file.close()
        self.start_status_bar_msg_thread('The file ' + pathlib.PurePath(self.file_name).name + ' has been opened...')
        logging.info('gui - reading_functions.py - reading_file: file loaded, file_ext ' + self.file_ext)


def var_reading(self):
    logging.debug('gui - reading_functions.py - var_reading : variable ' + str(self.variable_list.currentItem().text()))
    update_icons_state(self, 'var_reading')
    clear_gui(self, 'variable')
    if len(self.variable_list.selectedItems()) == 1:
        all_lines_edit = self.tab_2.findChildren(QtWidgets.QLineEdit)
        for widget in all_lines_edit:
            widget.setEnabled(False)
        all_text_edit = self.tab_2.findChildren(QtWidgets.QPlainTextEdit)
        for widget in all_text_edit:
            widget.setEnabled(False)
        update_variable_attribute_gui(self, 1)
    

def add_new_variable_gui(self):
    logging.debug('gui - gui_functions.py - add_new_variable_gui')
    self.tab_view.insertTab(2, self.tab_3, 'New variables')
    self.new_variable_list.setEnabled(True)
    self.new_variable_list.itemClicked.connect(lambda: new_var_reading(self))


def new_var_reading(self):
    logging.debug('gui - gui_functions.py - new_var_reading : variable ' + str(self.new_variable_list.currentItem(
    ).text()))
    update_icons_state(self, 'new_var_reading')
    clear_gui(self, 'new_variable')
    if len(self.new_variable_list.selectedItems()) == 1:
        all_lines_edit = self.tab_3.findChildren(QtWidgets.QLineEdit)
        for widget in all_lines_edit:
            widget.setEnabled(False)
        all_text_edit = self.tab_3.findChildren(QtWidgets.QPlainTextEdit)
        for widget in all_text_edit:
            widget.setEnabled(False)
        update_variable_attribute_gui(self, 2)


class MyWaitReading(QtWidgets.QDialog, Ui_waitBatchWindow):
    def __init__(self, file_name, file_ext, config_dict):
        logging.debug('gui - reading_functions.py - MyWaitReading - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.file_name = file_name
        self.file_ext = file_ext
        self.config_dict = config_dict
        self.spinner = None
        self.read_thread = None
        self.error_occurred = False
        self.success = True
        self.final_dict = None
        self.setup_spinner()
        self.launch_reading_thread()

    def update_progress(self, val):
        progress_str, progress_nbr = val[0], val[1]
        if len(progress_str) > 65:
            progress_str = progress_str[:32] + '...' + progress_str[-32:0]
        self.progress_label.setText(progress_str)
        self.progress_bar.setValue(progress_nbr)

    def launch_reading_thread(self):
        logging.debug('gui - reading_functions.py - MyWaitReading - launch_reading_thread')
        self.read_thread = ReadFileThread(self.file_name, self.file_ext, self.config_dict)
        self.read_thread.start()
        self.read_thread.progress.connect(self.update_progress)
        self.read_thread.finished.connect(self.reading_finished)
        self.read_thread.error.connect(self.reading_failed)

    def reading_finished(self, final_dict):
        logging.debug('gui - reading_functions.py - MyWaitReading - reading_finished')
        self.final_dict = final_dict
        self.close()

    def reading_failed(self):
        logging.debug('gui - reading_functions.py - MyWaitReading - reading_failed')
        self.error_occurred = True
        self.success = False
        self.close()

    def setup_spinner(self):
        logging.debug('gui - reading_functions.py - MyWaitReading - setup_spinner')
        self.spinner = QtWaitingSpinner(self, centerOnParent=False)
        self.spinner_layout.addWidget(self.spinner)
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
        logging.debug('gui - reading_functions.py - MyWaitReading - closeWindow')
        self.close()
