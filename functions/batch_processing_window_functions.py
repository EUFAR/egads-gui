import logging
import datetime
import os
import pathlib
import egads
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_batchprocessingwindow import Ui_batchProcessingWindow
from ui.Ui_waitbatchwindow import Ui_waitBatchWindow
from ui.Ui_batchinfowindow import Ui_batchInfoWindow
from functions.other_windows_functions import MyInfo, MyCoeff
from functions.gui_elements import QtWaitingSpinner
from functions.thread_functions import BatchProcessingThread
from functions.material_functions import batch_processing_information_buttons_text
from functions.utils import humansize


class MyBatchProcessing(QtWidgets.QDialog, Ui_batchProcessingWindow):
    def __init__(self, list_of_algorithms, config_dict):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        batch_processing_information_buttons_text(self)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_of_algorithms = list_of_algorithms
        self.config_dict = config_dict
        self.bw_label_10.setText('')
        self.bw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_5.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_7.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_8.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_9.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_checkbox_1.stateChanged.connect(self.activate_filename_creation)
        self.bw_checkbox_1.stateChanged.connect(self.activate_launch_processing_button)
        self.bw_button_cancel.clicked.connect(self.closeWindow)
        self.bw_combobox_1.currentIndexChanged.connect(self.process_selection)
        self.bw_combobox_1.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_2.currentIndexChanged.connect(self.populate_combobox_algorithms)
        self.bw_combobox_2.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_3.currentIndexChanged.connect(self.set_algorithm_options)
        self.bw_combobox_3.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_5.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_6.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_7.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_8.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_9.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_5.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_6.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_7.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_8.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_9.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_5.textChanged.connect(self.set_filename_example)
        self.bw_edit_6.textChanged.connect(self.set_filename_example)
        self.bw_edit_7.textChanged.connect(self.set_filename_example)
        self.bw_edit_8.textChanged.connect(self.set_filename_example)
        self.bw_edit_9.textChanged.connect(self.set_filename_example)
        self.bw_edit_5.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_6.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_7.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_8.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_9.textChanged.connect(self.activate_launch_processing_button)
        self.bw_open_button_1.clicked.connect(self.get_folder_path)
        self.bw_open_button_2.clicked.connect(self.get_folder_path)
        self.bw_edit_2.textChanged.connect(self.populate_file_list_widget)
        self.bw_edit_2.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_3.textChanged.connect(self.activate_launch_processing_button)
        self.buttonGroup.buttonClicked.connect(self.populate_file_list_widget)
        self.buttonGroup.buttonClicked.connect(self.activate_launch_processing_button)
        self.filename_combobox_list = [self.bw_combobox_5, self.bw_combobox_6, self.bw_combobox_7, self.bw_combobox_8,
                                       self.bw_combobox_9]
        self.filename_edit_list = [self.bw_edit_5, self.bw_edit_6, self.bw_edit_7, self.bw_edit_8, self.bw_edit_9]
        self.button_format_text = {'NetCDF': '.nc', 'NASA Ames': '.na', 'no button': ('.nc', '.na')}
        self.listWidget.itemSelectionChanged.connect(self.activate_list_item_buttons)
        self.bw_up_button.clicked.connect(self.move_up_item)
        self.bw_down_button.clicked.connect(self.move_down_item)
        self.bw_plus_button.clicked.connect(self.add_new_item)
        self.bw_plus_button.clicked.connect(self.activate_launch_processing_button)
        self.bw_del_button.clicked.connect(self.delete_item)
        self.bw_del_button.clicked.connect(self.activate_launch_processing_button)
        self.bw_file_info.clicked.connect(self.info_item)
        self.bw_button_ok.clicked.connect(self.launch_processing)
        self.bw_info_1.clicked.connect(self.batch_button_info)
        self.bw_info_2.clicked.connect(self.batch_button_info)
        self.bw_info_3.clicked.connect(self.batch_button_info)
        self.bw_info_4.clicked.connect(self.batch_button_info)
        self.bw_info_5.clicked.connect(self.batch_button_info)
        self.bw_info_6.clicked.connect(self.batch_button_info)
        self.bw_info_7.clicked.connect(self.filename_button_info)
        self.bw_info_8.clicked.connect(self.filename_button_info)
        self.bw_info_9.clicked.connect(self.filename_button_info)
        self.bw_info_10.clicked.connect(self.filename_button_info)
        self.bw_info_11.clicked.connect(self.filename_button_info)
        self.bw_label_2.setVisible(False)
        self.bw_label_3.setVisible(False)
        self.bw_combobox_2.setVisible(False)
        self.bw_combobox_3.setVisible(False)
        self.bw_info_2.setVisible(False)
        self.bw_label_12.setVisible(False)
        self.bw_edit_4.setVisible(False)
        self.tabWidget.removeTab(2)
        self.algorithm = None
        self.options_hl_1 = None
        self.options_hl_2 = None
        self.options_label_1 = None
        self.options_label_2 = None
        self.options_combobox_1 = None
        self.options_list_1 = None
        self.options_hl_5 = None
        self.options_gl_1 = None
        self.options_label_4 = None
        self.options_hl_4 = None
        self.options_combobox_2 = None
        self.options_hl_3 = None
        self.options_label_3 = None
        self.options_button_1 = None
        self.grid_layout_input_1 = None
        self.grid_layout_input_2 = None
        self.infoWindow = None
        self.options_line_1 = None
        self.input_activate = 0
        self.list_of_inputs = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_button_input = []
        self.input_num = 0
        self.list_label_output = []
        self.list_edit_output = []
        self.list_button_output = []
        self.output_num = 0
        self.output_activate = 0
        self.list_of_outputs = []
        self.types_for_combobox = ["vector", "array", "vector_optional", "array_optional"]
        self.populate_combobox_category()
        logging.info('gui - batch_processing_window_functions.py - MyBatchProcessing ready')

    def process_selection(self, val):
        self.bw_radiobox_1.setEnabled(True)
        self.bw_radiobox_2.setEnabled(True)
        self.algorithm = None
        if val == 0:
            self.bw_combobox_3.clear()
            self.bw_combobox_2.setCurrentIndex(0)
            self.bw_edit_1.setPlainText('')
            self.bw_label_2.setEnabled(False)
            self.bw_label_3.setEnabled(False)
            self.bw_label_4.setEnabled(False)
            self.bw_combobox_2.setEnabled(False)
            self.bw_combobox_3.setEnabled(False)
            self.bw_edit_1.setEnabled(False)
            self.bw_info_2.setEnabled(False)
            self.bw_label_2.setVisible(False)
            self.bw_label_3.setVisible(False)
            self.bw_combobox_2.setVisible(False)
            self.bw_combobox_3.setVisible(False)
            self.bw_info_2.setVisible(False)
            self.bw_label_12.setVisible(False)
            self.bw_label_12.setEnabled(False)
            self.bw_edit_4.setVisible(False)
            self.bw_edit_4.setEnabled(False)
            self.bw_edit_4.setText('')
            if self.tabWidget.count() == 4:
                self.tabWidget.removeTab(2)
        elif val == 6:
            self.bw_combobox_3.clear()
            self.bw_combobox_2.setCurrentIndex(0)
            self.bw_edit_1.setText('<p align="justify">All EGADS algorithms are available in the batch processing '
                                   'window. Please select one of them to display information about it. An '
                                   'Algorithm options tab is then displayed to handle inputs and outputs for '
                                   'the algorithm. Please take note that the list of variables displayed in the '
                                   'Algorithm options tab are retrieve from the first file in the Source tab.</p>')
            self.bw_label_2.setEnabled(True)
            self.bw_label_3.setEnabled(True)
            self.bw_label_4.setEnabled(True)
            self.bw_combobox_2.setEnabled(True)
            self.bw_combobox_3.setEnabled(False)
            self.bw_edit_1.setEnabled(True)
            self.bw_info_2.setEnabled(True)
            self.bw_label_2.setVisible(True)
            self.bw_label_3.setVisible(True)
            self.bw_combobox_2.setVisible(True)
            self.bw_combobox_3.setVisible(True)
            self.bw_info_2.setVisible(True)
            if self.tabWidget.count() == 3:
                self.tabWidget.insertTab(2, self.tab_3, 'Algorithm options')
            else:
                self.tabWidget.setTabText(2, 'Algorithm options')
            clear_layout(self.options_layout)
        else:
            self.bw_combobox_3.clear()
            self.bw_combobox_2.setCurrentIndex(0)
            self.bw_label_2.setEnabled(False)
            self.bw_label_3.setEnabled(False)
            self.bw_combobox_2.setEnabled(False)
            self.bw_combobox_3.setEnabled(False)
            self.bw_info_2.setEnabled(False)
            self.bw_label_4.setEnabled(True)
            self.bw_edit_1.setEnabled(True)
            self.bw_label_2.setVisible(False)
            self.bw_label_3.setVisible(False)
            self.bw_combobox_2.setVisible(False)
            self.bw_combobox_3.setVisible(False)
            self.bw_info_2.setVisible(False)
            self.bw_label_12.setVisible(False)
            self.bw_label_12.setEnabled(False)
            self.bw_edit_4.setVisible(False)
            self.bw_edit_4.setEnabled(False)
            self.bw_edit_4.setText('')
            if val == 1:
                self.bw_edit_1.setText('<p align="justify">This function is usefull for those who wants to concatenate '
                                       'multiple files into one file. All metadata, variables, dimensions coming from '
                                       'each file are stored into one file. An option tab is available to let the '
                                       'user decide what to do with global attributes.<br><br>Please take note of few '
                                       'limitations:<ul><li>if different dimensions or variables have the same name, '
                                       'they will be overwritten in the destination file.</li><li>it is expected to '
                                       'have the same behaviour with metadata displaying the same name.</li><li>of '
                                       'course, it is not possible to concatenate NetCDF files AND NASA Ames file '
                                       'into the same file.</li><li>do not forget that EGADS only handles NASA Ames '
                                       'file with an FFI equal to 1001.</li></ul></p>')
                if self.tabWidget.count() == 3:
                    self.tabWidget.insertTab(2, self.tab_3, 'Concatenation options')
                else:
                    self.tabWidget.setTabText(2, 'Concatenation options')
                clear_layout(self.options_layout)
                self.set_concatenation_options()
            elif val == 2:
                self.bw_edit_1.setText('<p align="justify">This funtion allows the user to convert multiple NASA '
                                       'Ames files to NetCDF using the EGADS file conversion feature.</p>')
                if self.tabWidget.count() == 4:
                    self.tabWidget.removeTab(2)
                self.bw_radiobox_2.setChecked(True)
                self.bw_radiobox_1.setEnabled(False)
            elif val == 3:
                self.bw_edit_1.setText('<p align="justify">This funtion allows the user to convert multiple NetCDF '
                                       'files to NASA Ames file format using the EGADS file conversion feature.</p>')
                if self.tabWidget.count() == 4:
                    self.tabWidget.removeTab(2)
                self.bw_radiobox_1.setChecked(True)
                self.bw_radiobox_2.setEnabled(False)
            elif val == 4:
                self.bw_edit_1.setText('<p align="justify">Use this function to delete global metadata from a '
                                       'list of NetCDF files. If the metadata to be deleted are not found in one '
                                       'or more files, those files are simply ignored, but still saved with '
                                       'others.')
                if self.tabWidget.count() == 3:
                    self.tabWidget.insertTab(2, self.tab_3, 'Deletion options')
                else:
                    self.tabWidget.setTabText(2, 'Deletion options')
                self.bw_radiobox_1.setChecked(True)
                self.bw_radiobox_2.setEnabled(False)
                clear_layout(self.options_layout)
                self.set_delete_metadata_options()
            elif val == 5:
                self.bw_edit_1.setText('<p align="justify">Use this function to delete variables from a '
                                       'list of NetCDF or NASA Ames files. If the variable to be deleted is not '
                                       'found or is a dimension in one or more files, this variable is not '
                                       'deleted and simply ignored.')
                if self.tabWidget.count() == 3:
                    self.tabWidget.insertTab(2, self.tab_3, 'Deletion options')
                else:
                    self.tabWidget.setTabText(2, 'Deletion options')
                clear_layout(self.options_layout)
                self.set_delete_variable_options()

    def populate_combobox_category(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - populate_combobox_1')
        self.bw_combobox_2.addItem("Make a choice...")
        folder_list = []
        for key in self.list_of_algorithms.keys():
            folder_list.append(key[:key.find(' - ')].title())
        self.bw_combobox_2.addItems(sorted(list(dict.fromkeys(folder_list))))

    def populate_combobox_algorithms(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - populate_combobox_2')
        self.bw_label_12.setVisible(False)
        self.bw_label_12.setEnabled(False)
        self.bw_edit_4.setVisible(False)
        self.bw_edit_4.setEnabled(False)
        self.bw_edit_4.setText('')
        self.bw_combobox_3.clear()
        if self.bw_combobox_2.currentText() == "Make a choice...":
            self.bw_label_12.setVisible(False)
            self.bw_label_12.setEnabled(False)
            self.bw_edit_4.setVisible(False)
            self.bw_edit_4.setEnabled(False)
            self.bw_edit_4.setText('')
            self.bw_combobox_3.setEnabled(False)
            self.bw_combobox_3.clear()
        else:
            self.bw_combobox_3.setEnabled(True)
            self.bw_combobox_3.addItem("Make a choice...")
            algo_list = []
            for key in self.list_of_algorithms.keys():
                if str(self.bw_combobox_2.currentText()).lower() in key:
                    idx = key.find(' - ')
                    algo_list.append(key[idx + 3:])
            self.bw_combobox_3.addItems(sorted(algo_list))

    def activate_filename_creation(self):
        if not self.bw_checkbox_1.isChecked():
            self.bw_label_10.setText('')
            self.bw_label_10.setEnabled(True)
            self.bw_combobox_5.setEnabled(True)
            self.bw_combobox_6.setEnabled(True)
            self.bw_combobox_7.setEnabled(True)
            self.bw_combobox_8.setEnabled(True)
            self.bw_combobox_9.setEnabled(True)
            self.bw_info_7.setEnabled(True)
            self.bw_info_8.setEnabled(True)
            self.bw_info_9.setEnabled(True)
            self.bw_info_10.setEnabled(True)
            self.bw_info_11.setEnabled(True)
            self.bw_edit_5.setText('')
            self.bw_edit_6.setText('')
            self.bw_edit_7.setText('')
            self.bw_edit_8.setText('')
            self.bw_edit_9.setText('')
            self.bw_combobox_5.setCurrentIndex(0)
            self.bw_combobox_6.setCurrentIndex(0)
            self.bw_combobox_7.setCurrentIndex(0)
            self.bw_combobox_8.setCurrentIndex(0)
            self.bw_combobox_9.setCurrentIndex(0)
        else:
            self.bw_label_10.setEnabled(False)
            self.bw_edit_5.setEnabled(False)
            self.bw_edit_6.setEnabled(False)
            self.bw_edit_7.setEnabled(False)
            self.bw_edit_8.setEnabled(False)
            self.bw_edit_9.setEnabled(False)
            self.bw_combobox_5.setEnabled(False)
            self.bw_combobox_6.setEnabled(False)
            self.bw_combobox_7.setEnabled(False)
            self.bw_combobox_8.setEnabled(False)
            self.bw_combobox_9.setEnabled(False)
            self.bw_info_7.setEnabled(False)
            self.bw_info_8.setEnabled(False)
            self.bw_info_9.setEnabled(False)
            self.bw_info_10.setEnabled(False)
            self.bw_info_11.setEnabled(False)
            self.bw_edit_9.setText('')
            self.bw_edit_5.setText('')
            self.bw_edit_6.setText('')
            self.bw_edit_7.setText('')
            self.bw_edit_8.setText('')
            self.bw_combobox_5.setCurrentIndex(0)
            self.bw_combobox_6.setCurrentIndex(0)
            self.bw_combobox_7.setCurrentIndex(0)
            self.bw_combobox_8.setCurrentIndex(0)
            self.bw_combobox_9.setCurrentIndex(0)
            self.bw_label_10.setText('')

    def set_filename_options(self):
        combobox = self.sender()
        index = int(combobox.objectName()[-1:])
        edit = getattr(self, 'bw_edit_' + str(index))
        if combobox.currentIndex() == 0:
            edit.setText('')
            edit.setEnabled(False)
        else:
            edit.setText('')
            edit.setEnabled(True)
            if combobox.currentIndex() == 1:
                edit.setText('%Y%m%dT%H%M%S')
            elif combobox.currentIndex() == 2:
                edit.setEnabled(False)
                edit.setText('original filename')
            elif combobox.currentIndex() == 3:
                edit.setText('001')
            elif combobox.currentIndex() == 4:
                edit.setText('')

    def set_filename_example(self):
        self.bw_label_10.setText('standby...')
        filename_example_str = ''
        for i, combobox in enumerate(self.filename_combobox_list):
            edit = self.filename_edit_list[i]
            edit_str = ''
            if combobox.currentIndex() == 0:
                edit_str = ''
            elif combobox.currentIndex() == 1:
                try:
                    edit_str = datetime.datetime.now().strftime(str(edit.text()))
                except ValueError:
                    edit_str = ''
            elif combobox.currentIndex() == 2:
                try:
                    edit_str = self.listWidget.item(0).text()[:-3]
                except AttributeError:
                    edit_str = 'original_filename'
            elif combobox.currentIndex() == 3:
                try:
                    int(edit.text())
                    edit_str = str(edit.text())
                except ValueError:
                    edit_str = ''
            elif combobox.currentIndex() == 4:
                edit_str = str(edit.text())
            filename_example_str += edit_str
        self.bw_label_10.setText(filename_example_str)

    def get_folder_path(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - get_folder_path')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            if self.sender().objectName() == 'bw_open_button_1':
                self.bw_edit_2.setText(str(pathlib.Path(folder_path)))
            elif self.sender().objectName() == 'bw_open_button_2':
                self.bw_edit_3.setText(str(pathlib.Path(folder_path)))

    def populate_file_list_widget(self):
        self.listWidget.clear()
        if self.bw_combobox_1.currentText() == 'Delete one or more global metadata' or \
                self.bw_combobox_1.currentText() == 'Delete one or more variables':
            self.options_combobox_2.clear()
        elif self.bw_combobox_1.currentText() == 'Execute an algorithm':
            for widget in self.list_combobox_input:
                if isinstance(widget, QtWidgets.QComboBox):
                    widget.clear()
        path = str(self.bw_edit_2.text())
        try:
            button_text = self.buttonGroup.checkedButton().text()
        except AttributeError:
            button_text = 'no button'
        if os.path.isdir(path) and self.bw_edit_2.text():
            for file in os.listdir(path):
                if file.endswith(self.button_format_text[button_text]):
                    item = QtWidgets.QListWidgetItem(file)
                    item.setToolTip(os.path.join(path, file))
                    self.listWidget.addItem(item)
            self.populate_options_file_combobox()
            self.populate_algorithm_input_combobox()

    def activate_list_item_buttons(self):
        current_items = self.listWidget.selectedItems()
        if current_items:
            if len(current_items) == 1:
                self.bw_up_button.setEnabled(True)
                self.bw_down_button.setEnabled(True)
                self.bw_del_button.setEnabled(True)
                self.bw_file_info.setEnabled(True)
            else:
                self.bw_file_info.setEnabled(False)
                self.bw_up_button.setEnabled(False)
                self.bw_down_button.setEnabled(False)
                self.bw_del_button.setEnabled(True)
        else:
            self.bw_up_button.setEnabled(False)
            self.bw_down_button.setEnabled(False)
            self.bw_del_button.setEnabled(False)
            self.bw_file_info.setEnabled(False)

    def move_up_item(self):
        current_row = self.listWidget.currentRow()
        current_item = self.listWidget.takeItem(current_row)
        self.listWidget.insertItem(current_row - 1, current_item)
        self.listWidget.setCurrentItem(current_item)
        if current_row - 1 == 0:
            self.populate_algorithm_input_combobox()

    def move_down_item(self):
        current_row = self.listWidget.currentRow()
        current_item = self.listWidget.takeItem(current_row)
        self.listWidget.insertItem(current_row + 1, current_item)
        self.listWidget.setCurrentItem(current_item)
        if current_row == 0:
            self.populate_algorithm_input_combobox()

    def add_new_item(self):
        file_dialog = QtWidgets.QFileDialog()
        try:
            button_text = self.buttonGroup.checkedButton().text()
        except AttributeError:
            button_text = 'no button'
        if button_text == 'no button':
            filter_types = 'NetCDF Files (*.nc);;NASA Ames Files (*.na)'
        else:
            if self.button_format_text[button_text] == '.nc':
                filter_types = 'NetCDF Files (*.nc)'
            else:
                filter_types = 'NASA Ames Files (*.na)'
        file_path, _ = file_dialog.getOpenFileName(self, 'Select file', '', filter_types)
        path, file = os.path.split(file_path)
        item = QtWidgets.QListWidgetItem(file)
        item.setToolTip(os.path.join(str(pathlib.Path(path)), file))
        self.listWidget.addItem(item)
        self.populate_options_file_combobox()

    def delete_item(self):
        current_items = self.listWidget.selectedItems()
        for item in current_items:
            index = self.listWidget.row(item)
            self.listWidget.takeItem(index)
        self.populate_options_file_combobox()

    def info_item(self):
        self.batchInfoWindow = MyBatchInfo(self.listWidget.currentItem().toolTip())
        self.batchInfoWindow.exec_()

    def set_algorithm_options(self):
        self.bw_label_12.setVisible(True)
        self.bw_label_12.setEnabled(True)
        self.bw_edit_4.setVisible(True)
        self.bw_edit_4.setEnabled(True)
        self.bw_edit_4.setText('')
        clear_layout(self.options_layout)
        if self.bw_combobox_3.currentText() == 'Make a choice...' or self.bw_combobox_3.currentText() == '':
            return
        rep, algo = str(self.bw_combobox_2.currentText()).lower(), str(self.bw_combobox_3.currentText())
        self.algorithm = self.list_of_algorithms[rep + ' - ' + algo]['method']
        if self.algorithm is not None:
            self.bw_edit_4.setText(self.algorithm().metadata['Description'])
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font2 = QtGui.QFont()
            font2.setFamily("fonts/SourceSansPro-Regular.ttf")
            font2.setPointSize(10)
            font2.setKerning(True)
            font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font3 = QtGui.QFont()
            font3.setFamily("fonts/SourceSansPro-Regular.ttf")
            font3.setPointSize(9)
            font3.setKerning(True)
            font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.input_activate = 0
            self.list_of_inputs = []
            self.list_label_input = []
            self.list_combobox_input = []
            self.list_button_input = []
            self.list_label_output = []
            self.list_edit_output = []
            self.list_button_output = []
            self.output_num = 0
            self.output_activate = 0
            self.list_of_outputs = []
            self.input_num = 0
            self.coefficient_matrix_values = {}
            self.options_hl_1 = QtWidgets.QHBoxLayout()
            self.options_hl_1.setObjectName("options_hl_1")
            self.options_label_1 = QtWidgets.QLabel()
            self.options_label_1.setEnabled(True)
            self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
            self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
            self.options_label_1.setFont(font)
            self.options_label_1.setStyleSheet("QLabel {\n"
                                               "    color: rgb(45,45,45);\n"
                                               "}")
            self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.options_label_1.setObjectName("options_label_1")
            self.options_label_1.setText("Input(s)")
            self.options_hl_1.addWidget(self.options_label_1)
            self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum))
            self.options_layout.addLayout(self.options_hl_1)
            self.grid_layout_input_1 = QtWidgets.QGridLayout()
            self.grid_layout_input_1.setObjectName("grid_layout_input_1")
            self.options_layout.addLayout(self.grid_layout_input_1)
            for index, item in enumerate(self.algorithm().metadata["Inputs"]):
                self.list_label_input.append(QtWidgets.QLabel())
                self.list_label_input[self.input_num].setFont(font2)
                self.list_label_input[self.input_num].setText(item + ':')
                self.list_label_input[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
                self.list_label_input[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.list_label_input[self.input_num].setObjectName("list_label_input_" + str(self.input_num))
                self.list_label_input[self.input_num].setStyleSheet("QLabel {\n"
                                                                    "   color: rgb(45,45,45);\n"
                                                                    "}")
                self.list_label_input[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                   QtCore.Qt.AlignVCenter)
                self.grid_layout_input_1.addWidget(self.list_label_input[self.input_num], self.input_num, 0, 1, 1)
                self.grid_layout_input_1.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                       QtWidgets.QSizePolicy.Minimum),
                                                 self.input_num, 1, 1, 1)

                input_type = self.algorithm().metadata["InputTypes"][index]
                combobox_widget = False
                for var_type in self.types_for_combobox:
                    if var_type in input_type:
                        combobox_widget = True

                if combobox_widget:
                    self.list_combobox_input.append(QtWidgets.QComboBox())
                    self.list_combobox_input[self.input_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
                    self.list_combobox_input[self.input_num].setEnabled(True)
                    self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                    self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                    self.list_combobox_input[self.input_num].setFrame(False)
                    self.list_combobox_input[self.input_num].setFont(font3)
                    self.list_combobox_input[self.input_num].setStyleSheet("QComboBox {\n"
                                                                           "    border: 1px solid #acacac;\n"
                                                                           "    border-radius: 1px;\n"
                                                                           "    padding-left: 5px;\n"
                                                                           "    background-color: qlineargradient(x1: "
                                                                           "0, y1: 0, x2: 0, y2: 1, \n"
                                                                           "                                "
                                                                           "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                                                           "    color: rgb(45,45,45);\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox:disabled {\n"
                                                                           "    background-color:  rgb(200,200,200);\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox:hover {\n"
                                                                           "    border: 1px solid #7eb4ea;\n"
                                                                           "    border-radius: 1px;\n"
                                                                           "    background-color: qlineargradient(x1: "
                                                                           "0, y1: 0, x2: 0, y2: 1, \n"
                                                                           "                                stop: 0 "
                                                                           "#ecf4fc, stop: 1 #dcecfc);\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox::drop-down {\n"
                                                                           "    subcontrol-origin: padding;\n"
                                                                           "    subcontrol-position: top right;\n"
                                                                           "    width: 27px;\n"
                                                                           "    border-left-width: 1px;\n"
                                                                           "    border-left-color: darkgray;\n"
                                                                           "    border-left-style: solid;\n"
                                                                           "    border-top-right-radius: 3px;\n"
                                                                           "    border-bottom-right-radius: 3px;\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox::down-arrow {\n"
                                                                           "    image: url(icons/down_arrow_icon.svg)"
                                                                           "; \n"
                                                                           "    width: 16px;\n"
                                                                           "    height: 16px\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox QAbstractItemView {\n"
                                                                           "    selection-background-color: rgb(200,200"
                                                                           ",200);\n"
                                                                           "    selection-color: black;\n"
                                                                           "    background: #f0f0f0;\n"
                                                                           "    border: 0px solid #f0f0f0;\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox QAbstractItemView::item {\n"
                                                                           "    margin: 5px 5px 5px 5px;\n"
                                                                           "}")
                    self.list_combobox_input[self.input_num].setObjectName("list_combobox_input_" + str(self.input_num))
                    self.list_combobox_input[self.input_num].addItem("Make a choice...")
                    self.list_combobox_input[self.input_num].activated.connect(self.activate_launch_processing_button)
                    self.grid_layout_input_1.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2,
                                                       1, 1)
                else:
                    if "coeff.[" in self.algorithm().metadata["InputTypes"][index] or "coeff[" in self.algorithm(
                    ).metadata["InputTypes"][index]:
                        self.list_combobox_input.append(QtWidgets.QHBoxLayout())
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_combobox_input[self.input_num].setObjectName("optional_tmp_layout")
                        else:
                            self.list_combobox_input[self.input_num].setObjectName("tmp_layout")
                        tmp_button = QtWidgets.QToolButton()
                        tmp_button.setMinimumSize(QtCore.QSize(150, 27))
                        tmp_button.setMaximumSize(QtCore.QSize(150, 27))
                        tmp_button.setFont(font2)
                        tmp_button.setStyleSheet("QToolButton {\n"
                                                 "    border: 1px solid #acacac;\n"
                                                 "    border-radius: 1px;\n"
                                                 "    background-color: qlineargradient(x1: 0, y1: 0, "
                                                 "x2: 0, y2: 1, \n"
                                                 "                                stop: 0 #f0f0f0, "
                                                 "stop: 1 #e5e5e5);\n"
                                                 "    color: rgb(45,45,45)\n"
                                                 "}\n"
                                                 "\n"
                                                 "QToolButton:hover {\n"
                                                 "    border: 1px solid #7eb4ea;\n"
                                                 "    border-radius: 1px;\n"
                                                 "    background-color: qlineargradient(x1: 0, y1: 0, "
                                                 "x2: 0, y2: 1, \n"
                                                 "                                stop: 0 #ecf4fc, "
                                                 "stop: 1 #dcecfc);\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "QToolButton:pressed {\n"
                                                 "    border: 1px solid #579de5;\n"
                                                 "    border-radius: 1px;\n"
                                                 "    background-color: qlineargradient(x1: 0, y1: 0, "
                                                 "x2: 0, y2: 1,\n"
                                                 "                                      stop: 0 "
                                                 "#daecfc, stop: 1 #c4e0fc);\n"
                                                 "}")
                        tmp_button.setObjectName("coeff_set_button_" + str(index))
                        tmp_button.setText('Set coefficient')
                        tmp_button.clicked.connect(self.launch_coeff_window)
                        self.list_combobox_input[self.input_num].addWidget(tmp_button)
                        tmp_label = QtWidgets.QLabel()
                        tmp_label.setFont(font)
                        tmp_label.setText('')
                        tmp_label.setMinimumSize(QtCore.QSize(0, 27))
                        tmp_label.setMaximumSize(QtCore.QSize(16777215, 27))
                        tmp_label.setObjectName("coeff_set_label" + str(index))
                        tmp_label.setStyleSheet("QLabel {\n"
                                                "   color: rgb(45,45,45);\n"
                                                "}")
                        self.list_combobox_input[self.input_num].addWidget(tmp_label)
                        self.grid_layout_input_1.addLayout(self.list_combobox_input[self.input_num], self.input_num, 2,
                                                           1, 1)
                    else:
                        self.list_combobox_input.append(QtWidgets.QLineEdit())
                        self.list_combobox_input[self.input_num].setEnabled(True)
                        self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setFrame(False)
                        self.list_combobox_input[self.input_num].setFont(font3)
                        self.list_combobox_input[self.input_num].setStyleSheet("QLineEdit {\n"
                                                                               "    border-radius: 3px;\n"
                                                                               "    padding: 1px 4px 1px 4px;\n"
                                                                               "    background-color:  rgb(240,240,"
                                                                               "240);\n"
                                                                               "    color: rgb(45,45,45);\n"
                                                                               "}\n")
                        self.list_combobox_input[self.input_num].textChanged.connect(
                            self.activate_launch_processing_button)
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_combobox_input[self.input_num].setObjectName("optional_list_lineedit_input_" +
                                                                                   str(self.input_num))
                        else:
                            self.list_combobox_input[self.input_num].setObjectName("list_edit_input_" +
                                                                                   str(self.input_num))
                        self.grid_layout_input_1.addWidget(self.list_combobox_input[self.input_num],
                                                           self.input_num, 2, 1, 1)
                self.list_button_input.append(QtWidgets.QToolButton())
                self.list_button_input[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setText("")
                self.list_button_input[self.input_num].setIcon(icon)
                self.list_button_input[self.input_num].setIconSize(QtCore.QSize(23, 23))
                self.list_button_input[self.input_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                if "optional" in self.algorithm().metadata["InputTypes"][index]:
                    self.list_button_input[self.input_num].setObjectName("optional_list_button_input_" + str(
                        self.input_num))
                else:
                    self.list_button_input[self.input_num].setObjectName("list_button_input_" + str(self.input_num))
                self.grid_layout_input_1.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                       QtWidgets.QSizePolicy.Minimum),
                                                 self.input_num, 3, 1, 1)
                self.list_button_input[self.input_num].setStyleSheet("QToolButton {\n"
                                                                     "    border: 1px solid transparent;\n"
                                                                     "    background-color: transparent;\n"
                                                                     "    width: 27px;\n"
                                                                     "    height: 27px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QToolButton:flat {\n"
                                                                     "    border: none;\n"
                                                                     "}")
                self.list_button_input[self.input_num].clicked.connect(self.algorithm_information_button)
                self.grid_layout_input_1.addWidget(self.list_button_input[self.input_num], self.input_num, 4, 1, 1)
                self.grid_layout_input_1.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                                       QtWidgets.QSizePolicy.Minimum),
                                                 self.input_num, 5, 1, 1)
                self.input_num += 1
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_line_1 = QtWidgets.QFrame()
        self.options_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.options_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.options_line_1.setObjectName("options_line_1")
        self.options_line_1.setStyleSheet("QFrame {\n"
                                          "    background: rgb(190,190,190);\n"
                                          "    height: 5px;\n"
                                          "    border: 0px solid black;\n"
                                          "}")
        self.options_layout.addWidget(self.options_line_1)
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_1")
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font)
        self.options_label_2.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_2.setObjectName("options_label_2")
        self.options_label_2.setText("Output(s)")
        self.options_hl_2.addWidget(self.options_label_2)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_2)
        self.grid_layout_input_2 = QtWidgets.QGridLayout()
        self.grid_layout_input_2.setObjectName("grid_layout_input_2")
        self.options_layout.addLayout(self.grid_layout_input_2)
        for item in self.algorithm().metadata["Outputs"]:
            self.list_label_output.append(QtWidgets.QLabel())
            self.list_label_output[self.output_num].setText(item + ':')
            self.list_label_output[self.output_num].setFont(font2)
            self.list_label_output[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
            self.list_label_output[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.list_label_output[self.output_num].setObjectName("list_label_output_" + str(self.output_num))
            self.list_label_output[self.output_num].setStyleSheet("QLabel {\n"
                                                                  "    color: rgb(45,45,45);\n"
                                                                  "}")
            self.list_label_output[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                 QtCore.Qt.AlignVCenter)
            self.grid_layout_input_2.addWidget(self.list_label_output[self.output_num], self.output_num, 0, 1, 1)
            self.grid_layout_input_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                   QtWidgets.QSizePolicy.Minimum),
                                             self.output_num, 1, 1, 1)
            self.list_edit_output.append(QtWidgets.QLineEdit())
            self.list_edit_output[self.output_num].setEnabled(True)
            self.list_edit_output[self.output_num].setFont(font3)
            self.list_edit_output[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
            self.list_edit_output[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
            self.list_edit_output[self.output_num].setFrame(False)
            self.list_edit_output[self.output_num].setStyleSheet("QLineEdit {\n"
                                                                 "  border-radius: 3px;\n"
                                                                 "  padding: 1px 4px 1px 4px;\n"
                                                                 "  background-color: rgb(240, 240, 240);\n"
                                                                 "  color: rgb(45,45,45);\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QLineEdit:disabled {\n"
                                                                 "  background-color: rgb(240, 240, 240);\n"
                                                                 "}")
            self.list_edit_output[self.output_num].setObjectName("list_edit_output_" + str(self.output_num))
            self.list_edit_output[self.output_num].textChanged.connect(self.activate_launch_processing_button)
            self.grid_layout_input_2.addWidget(self.list_edit_output[self.output_num], self.output_num, 2, 1, 1)
            self.list_button_output.append(QtWidgets.QToolButton())
            self.list_button_output[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
            self.list_button_output[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
            self.list_button_output[self.output_num].setText("")
            self.list_button_output[self.output_num].setIcon(icon)
            self.list_button_output[self.output_num].setIconSize(QtCore.QSize(23, 23))
            self.list_button_output[self.output_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
            self.list_button_output[self.output_num].setObjectName("list_button_output_" + str(self.output_num))
            self.grid_layout_input_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                   QtWidgets.QSizePolicy.Minimum),
                                             self.output_num, 3, 1, 1)
            self.list_button_output[self.output_num].setStyleSheet("QToolButton {\n"
                                                                   "    border: 1px solid transparent;\n"
                                                                   "    background-color: transparent;\n"
                                                                   "    width: 27px;\n"
                                                                   "    height: 27px;\n"
                                                                   "}\n"
                                                                   "\n"
                                                                   "QToolButton:flat {\n"
                                                                   "    border: none;\n"
                                                                   "}")
            self.list_button_output[self.output_num].clicked.connect(self.algorithm_information_button)
            self.grid_layout_input_2.addWidget(self.list_button_output[self.output_num], self.output_num, 4, 1, 1)
            self.grid_layout_input_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                                   QtWidgets.QSizePolicy.Minimum),
                                             self.output_num, 5, 1, 1)
            self.output_num += 1
            self.populate_algorithm_input_combobox()

    def launch_coeff_window(self):
        index = int(self.sender().objectName()[17:])
        matrix_nbr_idx = self.algorithm().metadata["InputTypes"][index].index('[')
        matrix_nbr_str = self.algorithm().metadata["InputTypes"][index][matrix_nbr_idx + 1:-1]
        matrix_nbr_str = matrix_nbr_str.split(',')
        try:
            coefficient_data = self.coefficient_matrix_values[self.sender().objectName()]
        except KeyError:
            coefficient_data = None
        self.coefWindow = MyCoeff(matrix_nbr_str, coefficient_data, self.listWidget.item(0).toolTip())
        self.coefWindow.exec_()
        if self.coefWindow.coef_array is not None:
            self.coefficient_matrix_values[self.sender().objectName()] = self.coefWindow.coef_array
        self.activate_launch_processing_button()

    def set_delete_metadata_options(self):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.options_hl_1 = QtWidgets.QHBoxLayout()
        self.options_hl_1.setObjectName("options_hl_1")
        self.options_label_1 = QtWidgets.QLabel()
        self.options_label_1.setEnabled(True)
        self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_1.setFont(font)
        self.options_label_1.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_1.setObjectName("options_label_1")
        self.options_hl_1.addWidget(self.options_label_1)
        self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_1)
        self.options_hl_5 = QtWidgets.QHBoxLayout()
        self.options_hl_5.setObjectName("options_hl_5")
        self.options_hl_5.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1 = QtWidgets.QGridLayout()
        self.options_gl_1.setObjectName("options_gl_1")
        self.options_label_4 = QtWidgets.QLabel()
        self.options_label_4.setEnabled(True)
        self.options_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_4.setFont(font2)
        self.options_label_4.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_4.setIndent(-1)
        self.options_label_4.setObjectName("options_label_4")
        self.options_gl_1.addWidget(self.options_label_4, 0, 0, 1, 1)
        self.options_hl_4 = QtWidgets.QHBoxLayout()
        self.options_hl_4.setObjectName("options_hl_4")
        self.options_combobox_2 = QtWidgets.QComboBox()
        self.options_combobox_2.setMinimumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setMaximumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setFont(font3)
        self.options_combobox_2.setStyleSheet("QComboBox {\n"
                                              "    border: 1px solid #acacac;\n"
                                              "    border-radius: 1px;\n"
                                              "    padding-left: 5px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:disabled {\n"
                                              "    background-color:  rgb(200,200,200);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:hover {\n"
                                              "    border: 1px solid #7eb4ea;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::drop-down {\n"
                                              "    subcontrol-origin: padding;\n"
                                              "    subcontrol-position: top right;\n"
                                              "    width: 27px;\n"
                                              "    border-left-width: 1px;\n"
                                              "    border-left-color: darkgray;\n"
                                              "    border-left-style: solid;\n"
                                              "    border-top-right-radius: 3px;\n"
                                              "    border-bottom-right-radius: 3px;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::down-arrow {\n"
                                              "    image: url(icons/down_arrow_icon.svg); \n"
                                              "    width: 16px;\n"
                                              "    height: 16px\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView {\n"
                                              "    selection-background-color: rgb(200,200,200);\n"
                                              "    selection-color: black;\n"
                                              "    background: #f0f0f0;\n"
                                              "    border: 0px solid #f0f0f0;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView::item {\n"
                                              "    margin: 5px 5px 5px 5px;\n"
                                              "}")
        self.options_combobox_2.setFrame(False)
        self.options_combobox_2.setObjectName("options_combobox_2")
        self.options_hl_4.addWidget(self.options_combobox_2)
        self.options_hl_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_4, 0, 1, 1, 1)
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font2)
        self.options_label_2.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_2.setIndent(-1)
        self.options_label_2.setObjectName("options_label_2")
        self.options_gl_1.addWidget(self.options_label_2, 1, 0, 1, 1)
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_2")
        self.options_combobox_1 = QtWidgets.QComboBox()
        self.options_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setFont(font3)
        self.options_combobox_1.setStyleSheet("QComboBox {\n"
                                              "    border: 1px solid #acacac;\n"
                                              "    border-radius: 1px;\n"
                                              "    padding-left: 5px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:disabled {\n"
                                              "    background-color:  rgb(200,200,200);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:hover {\n"
                                              "    border: 1px solid #7eb4ea;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::drop-down {\n"
                                              "    subcontrol-origin: padding;\n"
                                              "    subcontrol-position: top right;\n"
                                              "    width: 27px;\n"
                                              "    border-left-width: 1px;\n"
                                              "    border-left-color: darkgray;\n"
                                              "    border-left-style: solid;\n"
                                              "    border-top-right-radius: 3px;\n"
                                              "    border-bottom-right-radius: 3px;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::down-arrow {\n"
                                              "    image: url(icons/down_arrow_icon.svg); \n"
                                              "    width: 16px;\n"
                                              "    height: 16px\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView {\n"
                                              "    selection-background-color: rgb(200,200,200);\n"
                                              "    selection-color: black;\n"
                                              "    background: #f0f0f0;\n"
                                              "    border: 0px solid #f0f0f0;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView::item {\n"
                                              "    margin: 5px 5px 5px 5px;\n"
                                              "}")
        self.options_combobox_1.setFrame(False)
        self.options_combobox_1.setObjectName("options_combobox_1")
        self.options_hl_2.addWidget(self.options_combobox_1)
        self.options_button_1 = QtWidgets.QToolButton()
        self.options_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.options_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.options_button_1.setStyleSheet("QToolButton {\n"
                                            "    border: 1px solid transparent;\n"
                                            "    background-color: transparent;\n"
                                            "    width: 27px;\n"
                                            "    height: 27px;\n"
                                            "}\n"
                                            "\n"
                                            "QToolButton:flat {\n"
                                            "    border: none;\n"
                                            "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.options_button_1.setIcon(icon1)
        self.options_button_1.setIconSize(QtCore.QSize(23, 23))
        self.options_button_1.setObjectName("options_button_1")
        self.options_hl_2.addWidget(self.options_button_1)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_2, 1, 1, 1, 1)
        self.options_hl_5.addLayout(self.options_gl_1)
        self.options_layout.addLayout(self.options_hl_5)
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_hl_3 = QtWidgets.QHBoxLayout()
        self.options_hl_3.setObjectName("options_hl_3")
        self.options_hl_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_label_3 = QtWidgets.QLabel()
        self.options_label_3.setEnabled(True)
        self.options_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.options_label_3.setFont(font2)
        self.options_label_3.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.options_label_3.setIndent(-1)
        self.options_label_3.setObjectName("options_label_3")
        self.options_hl_3.addWidget(self.options_label_3)
        self.options_list_1 = QtWidgets.QListWidget()
        self.options_list_1.setEnabled(True)
        self.options_list_1.setFont(font3)
        self.options_list_1.setMinimumSize(QtCore.QSize(0, 150))
        self.options_list_1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.options_list_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.options_list_1.setStyleSheet("QListWidget {\n"
                                          "    border-radius: 3px;\n"
                                          "    background-color: rgb(240,240,240);\n"
                                          "    color: rgb(45,45,45);\n"
                                          "}\n"
                                          "\n"
                                          "QListWidget:disabled {\n"
                                          "    background-color:  rgb(200,200,200);\n"
                                          "    color: rgb(45,45,45);\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item {\n"
                                          "    border: 0px solid rgb(240,240,240);\n"
                                          "    border-radius: 3px;\n"
                                          "    padding: 1px 1px 1px 1px;\n"
                                          "    margin: 3px 3px 3px 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:selected {\n"
                                          "    border: 0px solid rgb(240,240,240);\n"
                                          "    border-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:selected:!active {\n"
                                          "    background: rgb(200,200,200);\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:selected:active {\n"
                                          "    background: rgb(200,200,200);\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:hover {\n"
                                          "    background: rgb(230,230,230);\n"
                                          "    border-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:vertical {\n"
                                          "  border: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  width: 20px;\n"
                                          "  margin: 21px 0px 21px 0px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:horizontal {\n"
                                          "  border: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  height: 20px;\n"
                                          "  margin: 0px 21px 0px 21px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::handle:vertical {\n"
                                          "  background-color: rgb(205, 205, 205);\n"
                                          "  min-height: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:vertical:hover {\n"
                                          "  background-color: rgb(166, 166, 166);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:vertical:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::handle:horizontal {\n"
                                          "  background-color: rgb(205, 205, 205);\n"
                                          "  min-width: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:horizontal:hover {\n"
                                          "  background-color: rgb(166, 166, 166);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:horizontal:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:vertical {\n"
                                          "  border-top: 1px solid rgb(240,240,240);\n"
                                          "  border-left: 1px solid white;\n"
                                          "  border-right: 1px solid white;\n"
                                          "  border-bottom: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  height: 20px;\n"
                                          "  subcontrol-position: bottom;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  border-bottom-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:vertical:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:vertical:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical {\n"
                                          "  border-top: 1px solid white;\n"
                                          "  border-left: 1px solid white;\n"
                                          "  border-right: 1px solid white;\n"
                                          "  border-bottom: 1px solid rgb(240,240,240);\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  height: 20px;\n"
                                          "  subcontrol-position: top;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  border-top-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::up-arrow:vertical {\n"
                                          "  image: url(icons/up_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::up-arrow:vertical:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::down-arrow:vertical {\n"
                                          "  image: url(icons/down_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::down-arrow:vertical:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:horizontal {\n"
                                          "  border-top: 1px solid white;\n"
                                          "  border-left: 1px solid rgb(240,240,240);\n"
                                          "  border-right: 1px solid white;\n"
                                          "  border-bottom: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  width: 20px;\n"
                                          "  subcontrol-position: right;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  border-bottom-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:horizontal:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:horizontal:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:horizontal {\n"
                                          "  border-top: 1px solid white;\n"
                                          "  border-left: 1px solid white;\n"
                                          "  border-right: 1px solid rgb(240,240,240);\n"
                                          "  border-bottom: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  width: 20px;\n"
                                          "  subcontrol-position: left;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "border-bottom-left-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:horizontal:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:horizontal:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::left-arrow:horizontal {\n"
                                          "  image: url(icons/left_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::left-arrow:horizontal:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::right-arrow:horizontal {\n"
                                          "  image: url(icons/right_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::right-arrow:horizontal:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}")
        self.options_list_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.options_list_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.options_list_1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.options_list_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.options_list_1.setObjectName("options_list_1")
        self.options_hl_3.addWidget(self.options_list_1)
        self.options_layout.addLayout(self.options_hl_3)
        self.options_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_label_1.setText("Delete global metadata")
        self.options_label_4.setText("Global metadata from:")
        self.options_label_2.setText("Global metadata:")
        self.options_label_3.setText("The following metadata will be deleted:")
        self.options_button_1.clicked.connect(self.add_metadata_variable_to_list)
        self.options_combobox_2.currentTextChanged.connect(self.populate_options_metvar_combobox)
        self.options_list_1.itemDoubleClicked.connect(self.remove_metadata_variable_from_list)
        if self.listWidget.count() > 0:
            self.options_combobox_2.clear()
            item_list = []
            for i in range(self.listWidget.count()):
                item_list.append(self.listWidget.item(i).text())
            self.options_combobox_2.addItems(item_list)

    def set_delete_variable_options(self):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.options_hl_1 = QtWidgets.QHBoxLayout()
        self.options_hl_1.setObjectName("options_hl_1")
        self.options_label_1 = QtWidgets.QLabel()
        self.options_label_1.setEnabled(True)
        self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_1.setFont(font)
        self.options_label_1.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_1.setObjectName("options_label_1")
        self.options_hl_1.addWidget(self.options_label_1)
        self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_1)
        self.options_hl_5 = QtWidgets.QHBoxLayout()
        self.options_hl_5.setObjectName("options_hl_5")
        self.options_hl_5.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1 = QtWidgets.QGridLayout()
        self.options_gl_1.setObjectName("options_gl_1")
        self.options_label_4 = QtWidgets.QLabel()
        self.options_label_4.setEnabled(True)
        self.options_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_4.setFont(font2)
        self.options_label_4.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_4.setIndent(-1)
        self.options_label_4.setObjectName("options_label_4")
        self.options_gl_1.addWidget(self.options_label_4, 0, 0, 1, 1)
        self.options_hl_4 = QtWidgets.QHBoxLayout()
        self.options_hl_4.setObjectName("options_hl_4")
        self.options_combobox_2 = QtWidgets.QComboBox()
        self.options_combobox_2.setMinimumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setMaximumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setFont(font3)
        self.options_combobox_2.setStyleSheet("QComboBox {\n"
                                              "    border: 1px solid #acacac;\n"
                                              "    border-radius: 1px;\n"
                                              "    padding-left: 5px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:disabled {\n"
                                              "    background-color:  rgb(200,200,200);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:hover {\n"
                                              "    border: 1px solid #7eb4ea;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::drop-down {\n"
                                              "    subcontrol-origin: padding;\n"
                                              "    subcontrol-position: top right;\n"
                                              "    width: 27px;\n"
                                              "    border-left-width: 1px;\n"
                                              "    border-left-color: darkgray;\n"
                                              "    border-left-style: solid;\n"
                                              "    border-top-right-radius: 3px;\n"
                                              "    border-bottom-right-radius: 3px;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::down-arrow {\n"
                                              "    image: url(icons/down_arrow_icon.svg); \n"
                                              "    width: 16px;\n"
                                              "    height: 16px\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView {\n"
                                              "    selection-background-color: rgb(200,200,200);\n"
                                              "    selection-color: black;\n"
                                              "    background: #f0f0f0;\n"
                                              "    border: 0px solid #f0f0f0;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView::item {\n"
                                              "    margin: 5px 5px 5px 5px;\n"
                                              "}")
        self.options_combobox_2.setFrame(False)
        self.options_combobox_2.setObjectName("options_combobox_2")
        self.options_hl_4.addWidget(self.options_combobox_2)
        self.options_hl_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_4, 0, 1, 1, 1)
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font2)
        self.options_label_2.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_2.setIndent(-1)
        self.options_label_2.setObjectName("options_label_2")
        self.options_gl_1.addWidget(self.options_label_2, 1, 0, 1, 1)
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_2")
        self.options_combobox_1 = QtWidgets.QComboBox()
        self.options_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setFont(font3)
        self.options_combobox_1.setStyleSheet("QComboBox {\n"
                                              "    border: 1px solid #acacac;\n"
                                              "    border-radius: 1px;\n"
                                              "    padding-left: 5px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:disabled {\n"
                                              "    background-color:  rgb(200,200,200);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:hover {\n"
                                              "    border: 1px solid #7eb4ea;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::drop-down {\n"
                                              "    subcontrol-origin: padding;\n"
                                              "    subcontrol-position: top right;\n"
                                              "    width: 27px;\n"
                                              "    border-left-width: 1px;\n"
                                              "    border-left-color: darkgray;\n"
                                              "    border-left-style: solid;\n"
                                              "    border-top-right-radius: 3px;\n"
                                              "    border-bottom-right-radius: 3px;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::down-arrow {\n"
                                              "    image: url(icons/down_arrow_icon.svg); \n"
                                              "    width: 16px;\n"
                                              "    height: 16px\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView {\n"
                                              "    selection-background-color: rgb(200,200,200);\n"
                                              "    selection-color: black;\n"
                                              "    background: #f0f0f0;\n"
                                              "    border: 0px solid #f0f0f0;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView::item {\n"
                                              "    margin: 5px 5px 5px 5px;\n"
                                              "}")
        self.options_combobox_1.setFrame(False)
        self.options_combobox_1.setObjectName("options_combobox_1")
        self.options_hl_2.addWidget(self.options_combobox_1)
        self.options_button_1 = QtWidgets.QToolButton()
        self.options_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.options_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.options_button_1.setStyleSheet("QToolButton {\n"
                                            "    border: 1px solid transparent;\n"
                                            "    background-color: transparent;\n"
                                            "    width: 27px;\n"
                                            "    height: 27px;\n"
                                            "}\n"
                                            "\n"
                                            "QToolButton:flat {\n"
                                            "    border: none;\n"
                                            "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.options_button_1.setIcon(icon1)
        self.options_button_1.setIconSize(QtCore.QSize(23, 23))
        self.options_button_1.setObjectName("options_button_1")
        self.options_hl_2.addWidget(self.options_button_1)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_2, 1, 1, 1, 1)
        self.options_hl_5.addLayout(self.options_gl_1)
        self.options_layout.addLayout(self.options_hl_5)
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_hl_3 = QtWidgets.QHBoxLayout()
        self.options_hl_3.setObjectName("options_hl_3")
        self.options_hl_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_label_3 = QtWidgets.QLabel()
        self.options_label_3.setEnabled(True)
        self.options_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.options_label_3.setFont(font2)
        self.options_label_3.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.options_label_3.setIndent(-1)
        self.options_label_3.setObjectName("options_label_3")
        self.options_hl_3.addWidget(self.options_label_3)
        self.options_list_1 = QtWidgets.QListWidget()
        self.options_list_1.setEnabled(True)
        self.options_list_1.setFont(font3)
        self.options_list_1.setMinimumSize(QtCore.QSize(0, 150))
        self.options_list_1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.options_list_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.options_list_1.setStyleSheet("QListWidget {\n"
                                          "    border-radius: 3px;\n"
                                          "    background-color: rgb(240,240,240);\n"
                                          "    color: rgb(45,45,45);\n"
                                          "}\n"
                                          "\n"
                                          "QListWidget:disabled {\n"
                                          "    background-color:  rgb(200,200,200);\n"
                                          "    color: rgb(45,45,45);\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item {\n"
                                          "    border: 0px solid rgb(240,240,240);\n"
                                          "    border-radius: 3px;\n"
                                          "    padding: 1px 1px 1px 1px;\n"
                                          "    margin: 3px 3px 3px 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:selected {\n"
                                          "    border: 0px solid rgb(240,240,240);\n"
                                          "    border-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:selected:!active {\n"
                                          "    background: rgb(200,200,200);\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:selected:active {\n"
                                          "    background: rgb(200,200,200);\n"
                                          "}\n"
                                          "\n"
                                          "QListView::item:hover {\n"
                                          "    background: rgb(230,230,230);\n"
                                          "    border-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:vertical {\n"
                                          "  border: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  width: 20px;\n"
                                          "  margin: 21px 0px 21px 0px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:horizontal {\n"
                                          "  border: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  height: 20px;\n"
                                          "  margin: 0px 21px 0px 21px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::handle:vertical {\n"
                                          "  background-color: rgb(205, 205, 205);\n"
                                          "  min-height: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:vertical:hover {\n"
                                          "  background-color: rgb(166, 166, 166);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:vertical:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::handle:horizontal {\n"
                                          "  background-color: rgb(205, 205, 205);\n"
                                          "  min-width: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:horizontal:hover {\n"
                                          "  background-color: rgb(166, 166, 166);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle:horizontal:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:vertical {\n"
                                          "  border-top: 1px solid rgb(240,240,240);\n"
                                          "  border-left: 1px solid white;\n"
                                          "  border-right: 1px solid white;\n"
                                          "  border-bottom: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  height: 20px;\n"
                                          "  subcontrol-position: bottom;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  border-bottom-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:vertical:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:vertical:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical {\n"
                                          "  border-top: 1px solid white;\n"
                                          "  border-left: 1px solid white;\n"
                                          "  border-right: 1px solid white;\n"
                                          "  border-bottom: 1px solid rgb(240,240,240);\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  height: 20px;\n"
                                          "  subcontrol-position: top;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  border-top-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::up-arrow:vertical {\n"
                                          "  image: url(icons/up_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::up-arrow:vertical:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::down-arrow:vertical {\n"
                                          "  image: url(icons/down_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::down-arrow:vertical:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:horizontal {\n"
                                          "  border-top: 1px solid white;\n"
                                          "  border-left: 1px solid rgb(240,240,240);\n"
                                          "  border-right: 1px solid white;\n"
                                          "  border-bottom: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  width: 20px;\n"
                                          "  subcontrol-position: right;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  border-bottom-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:horizontal:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:horizontal:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:horizontal {\n"
                                          "  border-top: 1px solid white;\n"
                                          "  border-left: 1px solid white;\n"
                                          "  border-right: 1px solid rgb(240,240,240);\n"
                                          "  border-bottom: 1px solid white;\n"
                                          "  background-color: rgb(240, 240, 240);\n"
                                          "  width: 20px;\n"
                                          "  subcontrol-position: left;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "border-bottom-left-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:horizontal:hover {\n"
                                          "  background-color: rgb(218, 218, 218);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:horizontal:pressed {\n"
                                          "  background-color: rgb(96, 96, 96);\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::left-arrow:horizontal {\n"
                                          "  image: url(icons/left_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::left-arrow:horizontal:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::right-arrow:horizontal {\n"
                                          "  image: url(icons/right_arrow_icon.svg); \n"
                                          "  width: 16px;\n"
                                          "  height: 16px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::right-arrow:horizontal:pressed {\n"
                                          "  right: -1px;\n"
                                          "  bottom: -1px;\n"
                                          "}")
        self.options_list_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.options_list_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.options_list_1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.options_list_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.options_list_1.setObjectName("options_list_1")
        self.options_hl_3.addWidget(self.options_list_1)
        self.options_layout.addLayout(self.options_hl_3)
        self.options_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_label_1.setText("Delete variable(s)")
        self.options_label_4.setText("Variables from:")
        self.options_label_2.setText("Variables:")
        self.options_label_3.setText("The following variables will be deleted:")
        self.options_button_1.clicked.connect(self.add_metadata_variable_to_list)
        self.options_list_1.itemDoubleClicked.connect(self.remove_metadata_variable_from_list)
        self.options_combobox_2.currentTextChanged.connect(self.populate_options_metvar_combobox)
        if self.listWidget.count() > 0:
            self.options_combobox_2.clear()
            item_list = []
            for i in range(self.listWidget.count()):
                item_list.append(self.listWidget.item(i).text())
            self.options_combobox_2.addItems(item_list)

    def set_concatenation_options(self):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.options_hl_1 = QtWidgets.QHBoxLayout()
        self.options_hl_1.setObjectName("options_hl_1")
        self.options_label_1 = QtWidgets.QLabel()
        self.options_label_1.setEnabled(True)
        self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_1.setFont(font)
        self.options_label_1.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_1.setObjectName("options_label_1")
        self.options_hl_1.addWidget(self.options_label_1)
        self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_1)
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_2")
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font2)
        self.options_label_2.setStyleSheet("QLabel {\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}")
        self.options_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_2.setIndent(20)
        self.options_label_2.setObjectName("options_label_2")
        self.options_hl_2.addWidget(self.options_label_2)
        self.options_combobox_1 = QtWidgets.QComboBox()
        self.options_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setFont(font3)
        self.options_combobox_1.setStyleSheet("QComboBox {\n"
                                              "    border: 1px solid #acacac;\n"
                                              "    border-radius: 1px;\n"
                                              "    padding-left: 5px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:disabled {\n"
                                              "    background-color:  rgb(200,200,200);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:hover {\n"
                                              "    border: 1px solid #7eb4ea;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                              "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::drop-down {\n"
                                              "    subcontrol-origin: padding;\n"
                                              "    subcontrol-position: top right;\n"
                                              "    width: 27px;\n"
                                              "    border-left-width: 1px;\n"
                                              "    border-left-color: darkgray;\n"
                                              "    border-left-style: solid;\n"
                                              "    border-top-right-radius: 3px;\n"
                                              "    border-bottom-right-radius: 3px;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::down-arrow {\n"
                                              "    image: url(icons/down_arrow_icon.svg); \n"
                                              "    width: 16px;\n"
                                              "    height: 16px\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView {\n"
                                              "    selection-background-color: rgb(200,200,200);\n"
                                              "    selection-color: black;\n"
                                              "    background: #f0f0f0;\n"
                                              "    border: 0px solid #f0f0f0;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox QAbstractItemView::item {\n"
                                              "    margin: 5px 5px 5px 5px;\n"
                                              "}")
        self.options_combobox_1.setFrame(False)
        self.options_combobox_1.setObjectName("options_combobox_1")
        self.options_combobox_1.addItem("")
        self.options_combobox_1.addItem("")
        self.options_combobox_1.addItem("")
        self.options_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_hl_2.addWidget(self.options_combobox_1)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_2)
        self.options_label_1.setText("Global metadata")
        self.options_label_2.setText("Global metadata will be:")
        self.options_combobox_1.setItemText(0, "copied from the first file")
        self.options_combobox_1.setItemText(1, "concatenated from all files")
        self.options_combobox_1.setItemText(2, "deleted (no global metadata)")

    def populate_algorithm_input_combobox(self):
        if self.bw_combobox_1.currentText() == 'Execute an algorithm':
            if self.algorithm is not None:
                if self.bw_radiobox_1.isChecked():
                    input_class = egads.input.EgadsNetCdf
                else:
                    input_class = egads.input.NasaAmes
                if self.listWidget.count() > 0:
                    f = input_class(self.listWidget.item(0).toolTip(), 'r')
                    variable_list = f.get_variable_list()
                    f.close()
                    for widget in self.list_combobox_input:
                        if isinstance(widget, QtWidgets.QComboBox):
                            widget.clear()
                            widget.addItem('Make a choice...')
                            widget.addItems(sorted(variable_list))

    def populate_options_file_combobox(self):
        if self.bw_combobox_1.currentText() == 'Delete one or more global metadata' or \
                self.bw_combobox_1.currentText() == 'Delete one or more variables':
            self.options_combobox_2.clear()
            for i in range(self.listWidget.count()):
                self.options_combobox_2.addItem(self.listWidget.item(i).text())

    def populate_options_metvar_combobox(self):
        if self.bw_combobox_1.currentText() == 'Delete one or more global metadata':
            if self.options_combobox_2.currentText() != '':
                item = self.listWidget.findItems(self.options_combobox_2.currentText(), QtCore.Qt.MatchExactly)[0]
                f = egads.input.EgadsNetCdf(item.toolTip(), 'r')
                self.options_combobox_1.clear()
                self.options_combobox_1.addItems(f.get_attribute_list())
                f.close()
        elif self.bw_combobox_1.currentText() == 'Delete one or more variables':
            if self.options_combobox_2.currentText() != '':
                item = self.listWidget.findItems(self.options_combobox_2.currentText(), QtCore.Qt.MatchExactly)[0]
                dim_list = None
                if self.bw_radiobox_1.isChecked():
                    f = egads.input.EgadsNetCdf(item.toolTip(), 'r')
                    dim_list = f.get_dimension_list()
                else:
                    f = egads.input.NasaAmes(item.toolTip(), 'r')
                self.options_combobox_1.clear()
                var_list = f.get_variable_list()
                if dim_list is not None:
                    for var in var_list:
                        if var in dim_list.keys():
                            var_list.remove(var)
                self.options_combobox_1.addItems(var_list)
                f.close()

    def add_metadata_variable_to_list(self):
        in_list = False
        for i in range(self.options_list_1.count()):
            if self.options_combobox_1.currentText() == str(self.options_list_1.item(i).text()):
                in_list = True
                break
        if not in_list:
            self.options_list_1.addItem(self.options_combobox_1.currentText())

    def remove_metadata_variable_from_list(self):
        self.options_list_1.takeItem(self.options_list_1.currentRow())

    def algorithm_information_button(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - information_button : '
                      + 'sender().objectName() ' + str(self.sender().objectName()))
        if "optional" in self.sender().objectName():
            optional_str = '[Optional] '
            index = 27
        else:
            optional_str = ''
            index = 18
        if "input" in self.sender().objectName():
            description = self.algorithm().metadata["InputDescription"][int(self.sender().objectName()[index:])]
            units = self.algorithm().metadata["InputUnits"][int(self.sender().objectName()[index:])]
            if units is None:
                units = ''
            information_str = '<u>Description:</u> ' + optional_str + description + '<br><br><u>Units:</u> ' + units
        else:
            description = self.algorithm().metadata["OutputDescription"][int(self.sender().objectName()[index + 1:])]
            units = self.algorithm().metadata["OutputUnits"][int(self.sender().objectName()[index + 1:])]
            if units is None:
                units = ''
            if isinstance(self.algorithm().output_metadata, list):
                output_metadata = self.algorithm().output_metadata[int(self.sender().objectName()[index + 1:])]
            else:
                output_metadata = self.algorithm().output_metadata
            standard_name = output_metadata["standard_name"]
            long_name = output_metadata["long_name"]
            if isinstance(output_metadata["Category"], list):
                category_str = ''
                for category in output_metadata["Category"]:
                    category_str += category + ', '
                category_str = category_str[0:-2]
            else:
                category_str = output_metadata["Category"]
            information_str = '<u>Description:</u> ' + optional_str + description + '<br><br><u>Units:</u> ' + units \
                              + '<br><br><u>Standard name:</u> ' + standard_name + '<br><br><u>Long name:</u> ' + \
                              long_name + '<br><br><u>Category:</u> ' + category_str
        self.infoWindow = MyInfo(information_str)
        self.infoWindow.exec_()

    def activate_launch_processing_button(self):
        processing = True
        algorithm = True
        category = True
        file_in_list = True
        destination_folder = True
        file_naming = True
        options_metvar_list = True
        options_input = True
        options_output = True
        if self.bw_combobox_1.currentText() == 'Make a choice...':
            processing = False
        if self.listWidget.count() == 0:
            file_in_list = False
        if not self.bw_edit_3.text():
            destination_folder = False
        if not self.bw_checkbox_1.isChecked():
            if not self.bw_label_10.text():
                file_naming = False
        if self.bw_combobox_1.currentText() == 'Delete one or more global metadata' or \
                self.bw_combobox_1.currentText() == 'Delete one or more variables':
            if self.options_list_1.count() == 0:
                options_metvar_list = False
        if self.bw_combobox_1.currentText() == 'Execute an algorithm':
            if self.bw_combobox_2.currentText() == 'Make a choice...':
                algorithm = False
            if self.bw_combobox_3.currentText() == 'Make a choice...' or self.bw_combobox_3.currentText() == '':
                category = False
        for widget in self.list_combobox_input:
            if "optional" not in widget.objectName():
                if isinstance(widget, QtWidgets.QComboBox):
                    if widget.currentText() == "Make a choice...":
                        options_input = False
                elif isinstance(widget, QtWidgets.QLineEdit):
                    if widget.text() == '':
                        options_input = False
                elif isinstance(widget, QtWidgets.QHBoxLayout):
                    if widget.itemAt(0).widget().objectName()not in self.coefficient_matrix_values:
                        options_input = False
        for widget in self.list_edit_output:
            if widget.text() == '':
                options_output = False
        if processing and algorithm and category and file_in_list and destination_folder and file_naming and \
                options_metvar_list and options_input and options_output:
            self.bw_button_ok.setEnabled(True)
        else:
            self.bw_button_ok.setEnabled(False)

    def launch_processing(self):
        filename_options = None
        if not self.bw_checkbox_1.isChecked():
            filename_options = []
            widgets_dict = [[self.bw_edit_5, self.bw_combobox_5],
                            [self.bw_edit_6, self.bw_combobox_6],
                            [self.bw_edit_7, self.bw_combobox_7],
                            [self.bw_edit_8, self.bw_combobox_8],
                            [self.bw_edit_9, self.bw_combobox_9]]
            for couple in widgets_dict:
                line, combobox = couple
                if combobox.currentIndex() == 0:
                    filename_options.append('')
                elif combobox.currentIndex() == 1:
                    filename_options.append('date' + str(line.text()))
                elif combobox.currentIndex() == 2:
                    filename_options.append('original_filename')
                elif combobox.currentIndex() == 3:
                    filename_options.append('ndigit' + str(line.text()))
                elif combobox.currentIndex() == 4:
                    filename_options.append(str(line.text()))

        processing_options = None
        if self.bw_combobox_1.currentIndex() == 1:
            processing_options = int(self.options_combobox_1.currentIndex())
        elif self.bw_combobox_1.currentIndex() == 4 or self.bw_combobox_1.currentIndex() == 5:
            processing_options = [str(self.options_list_1.item(i).text()) for i in
                                  range(self.options_list_1.count())]
        elif self.bw_combobox_1.currentIndex() == 6:
            if self.algorithm is not None:
                input_list = []
                output_list = []
                for widget in self.list_combobox_input:
                    if isinstance(widget, QtWidgets.QComboBox):
                        input_list.append(str(widget.currentText()))
                    elif isinstance(widget, QtWidgets.QLineEdit):
                        try:
                            input_list.append(float(widget.text()))
                        except ValueError:
                            input_list.append(str(widget.text()))

                    elif isinstance(widget, QtWidgets.QHBoxLayout):
                        input_list.append(self.coefficient_matrix_values[widget.itemAt(0).widget().objectName()])
                for widget in self.list_edit_output:
                    output_list.append(str(widget.text()))
                processing_options = {'inputs': input_list, 'outputs': output_list}

        if self.bw_combobox_4.currentIndex() == 0:
            stop_processing = True
        else:
            stop_processing = False
        batch_dict = {'process': int(self.bw_combobox_1.currentIndex()),
                      'algorithm': self.algorithm,
                      'file_list': [str(self.listWidget.item(i).toolTip()) for i in range(self.listWidget.count())],
                      'destination_folder': str(self.bw_edit_3.text()),
                      'filename_options': filename_options,
                      'stop_processing': stop_processing,
                      'processing_options': processing_options,
                      'out_format': str(self.buttonGroup.checkedButton().text())
                      }
        self.processing_window = MyWaitProcessing(batch_dict, self.config_dict)
        self.processing_window.exec_()
        error_occurred = self.processing_window.error_occurred
        success = self.processing_window.success
        if error_occurred:
            info_str = ('An important error occurred during the batch processing. The GUI decided to stop the '
                        'processing based on the choice of the user (cf. first tab and error option). Please read the '
                        'log file to check which kind or error occurred.')
            self.infoWindow = MyInfo(info_str)
            self.infoWindow.exec_()
        if success:
            info_str = 'The batch processing has been well executed.'
            self.infoWindow = MyInfo(info_str)
            self.infoWindow.exec_()

    def batch_button_info(self):
        self.infoWindow = MyInfo(self.information_buttons_text[self.sender().objectName()])
        self.infoWindow.exec_()

    def filename_button_info(self):
        widget = self.information_buttons_text[self.sender().objectName()]
        self.infoWindow = MyInfo(self.information_buttons_text[widget.currentText()])
        self.infoWindow.exec_()

    def closeWindow(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - closeWindow')
        self.close()


class MyWaitProcessing(QtWidgets.QDialog, Ui_waitBatchWindow):
    def __init__(self, batch_dict, config_dict):
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.batch_dict = batch_dict
        self.config_dict = config_dict
        self.spinner = None
        self.batch_thread = None
        self.error_occurred = False
        self.success = True
        self.setup_spinner()
        self.launch_processing_thread()

    def update_progress(self, val):
        progress_str, progress_nbr = val[0], val[1]
        if len(progress_str) > 65:
            progress_str = progress_str[:32] + '...' + progress_str[-32:0]
        self.progress_label.setText(progress_str)
        self.progress_bar.setValue(progress_nbr)

    def launch_processing_thread(self):
        self.batch_thread = BatchProcessingThread(self.batch_dict, self.config_dict)
        self.batch_thread.start()
        self.batch_thread.progress.connect(self.update_progress)
        self.batch_thread.finished.connect(self.processing_finished)
        self.batch_thread.error.connect(self.processing_failed)

    def processing_finished(self):
        self.close()

    def processing_failed(self):
        self.error_occurred = True
        self.success = False
        self.close()

    def setup_spinner(self):
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
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - closeWindow')
        self.close()


class MyBatchInfo(QtWidgets.QDialog, Ui_batchInfoWindow):
    def __init__(self, file_path):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchInfo - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.file_path = file_path
        self.extension = os.path.splitext(file_path)[1]
        self.biw_ok_button.clicked.connect(self.close)
        self.met_label = []
        self.met_line = []
        self.var_label = []
        self.var_line = []
        self.horizontalLayout_4.removeItem(self.horizontalLayout_4.itemAt(1))
        self.splitter_1.setSizes([170, 200, 230])
        self.splitter_2.setSizes([216, 430])
        self.variable_list.currentTextChanged.connect(self.parse_variable_info)
        if self.extension == '.nc':
            self.file = egads.input.EgadsNetCdf(self.file_path, 'r')
        elif self.extension == '.na':
            self.file = egads.input.NasaAmes(self.file_path, 'r')
        self.parse_file_info()

    def parse_file_info(self):
        self.biw_line_1.setText(str(pathlib.Path(self.file_path).name))
        self.biw_line_2.setText(str(pathlib.Path(self.file_path).parent))
        self.biw_line_3.setText(humansize(pathlib.Path(self.file_path).stat().st_size))
        glob_attr = self.file.get_attribute_list()
        var_list = self.file.get_variable_list()
        if self.extension == '.na':
            var_list += self.file.get_variable_list(vartype='independant')
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        i = 0
        for key, value in glob_attr.items():
            self.met_label.append(QtWidgets.QLabel())
            self.met_label[i].setFont(font)
            self.met_label[i].setMinimumSize(QtCore.QSize(0, 27))
            self.met_label[i].setMaximumSize(QtCore.QSize(16777215, 27))
            self.met_label[i].setObjectName("met_label_" + str(i))
            self.met_label[i].setText(key + ':')
            self.met_label[i].setStyleSheet("QLabel {\n"
                                            "   color: rgb(45,45,45);\n"
                                            "}")
            self.met_label[i].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.global_attributes_layout.addWidget(self.met_label[i], i, 0, 1, 1)
            if key == "SCOM" or key == "NCOM":
                self.met_line.append(QtWidgets.QPlainTextEdit())
                self.met_line[i].setMinimumSize(QtCore.QSize(0, 100))
                self.met_line[i].setMaximumSize(QtCore.QSize(16777215, 100))
                self.met_line[i].setFrameShape(QtWidgets.QFrame.NoFrame)
                self.met_line[i].setPlainText(str(value))
                self.met_line[i].setStyleSheet("QPlainTextEdit {\n"
                                               "    border-radius: 3px;\n"
                                               "    padding: 1px 0px 1px 4px;\n"
                                               "    background-color:  rgb(240, 240, 240);\n"
                                               "    color: rgb(45,45,45);\n"
                                               "}\n"
                                               "    \n"
                                               "QPlainTextEdit:disabled {\n"
                                               "    background-color:  rgb(240, 240, 240);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar:horizontal {\n"
                                               "  border: 1px solid white;\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  height: 20px;\n"
                                               "  margin: 0px 21px 0px 21px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::handle:vertical {\n"
                                               "  background-color: rgb(205, 205, 205);\n"
                                               "  min-height: 25px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar:handle:vertical:hover {\n"
                                               "  background-color: rgb(166, 166, 166);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar:handle:vertical:pressed {\n"
                                               "  background-color: rgb(96, 96, 96);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::handle:horizontal {\n"
                                               "  background-color: rgb(205, 205, 205);\n"
                                               "  min-width: 25px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar:handle:horizontal:hover {\n"
                                               "  background-color: rgb(166, 166, 166);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar:handle:horizontal:pressed {\n"
                                               "  background-color: rgb(96, 96, 96);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::add-line:vertical {\n"
                                               "  border-top: 1px solid rgb(240,240,240);\n"
                                               "  border-left: 1px solid white;\n"
                                               "  border-right: 1px solid white;\n"
                                               "  border-bottom: 1px solid white;\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  height: 20px;\n"
                                               "  subcontrol-position: bottom;\n"
                                               "  subcontrol-origin: margin;\n"
                                               "  border-bottom-right-radius: 3px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::add-line:vertical:hover {\n"
                                               "  background-color: rgb(218, 218, 218);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::add-line:vertical:pressed {\n"
                                               "  background-color: rgb(96, 96, 96);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::sub-line:vertical {\n"
                                               "  border-top: 1px solid white;\n"
                                               "  border-left: 1px solid white;\n"
                                               "  border-right: 1px solid white;\n"
                                               "  border-bottom: 1px solid rgb(240,240,"
                                               "240);\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  height: 20px;\n"
                                               "  subcontrol-position: top;\n"
                                               "  subcontrol-origin: margin;\n"
                                               "  border-top-right-radius: 3px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::sub-line:vertical:hover {\n"
                                               "  background-color: rgb(218, 218, 218);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::sub-line:vertical:pressed {\n"
                                               "  background-color: rgb(96, 96, 96);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::up-arrow:vertical {\n"
                                               "  image: url(icons/up_arrow_icon.svg); \n"
                                               "  width: 16px;\n"
                                               "  height: 16px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::up-arrow:vertical:pressed {\n"
                                               "  right: -1px;\n"
                                               "  bottom: -1px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::down-arrow:vertical {\n"
                                               "  image: url(icons/down_arrow_icon.svg); \n"
                                               "  width: 16px;\n"
                                               "  height: 16px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::down-arrow:vertical:pressed {\n"
                                               "  right: -1px;\n"
                                               "  bottom: -1px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::add-line:horizontal {\n"
                                               "  border-top: 1px solid white;\n"
                                               "  border-left: 1px solid rgb(240,240,240);\n"
                                               "  border-right: 1px solid white;\n"
                                               "  border-bottom: 1px solid white;\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  width: 20px;\n"
                                               "  subcontrol-position: right;\n"
                                               "  subcontrol-origin: margin;\n"
                                               "  border-bottom-right-radius: 3px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::add-line:horizontal:hover {\n"
                                               "  background-color: rgb(218, 218, 218);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::add-line:horizontal:pressed {\n"
                                               "  background-color: rgb(96, 96, 96);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::sub-line:horizontal {\n"
                                               "  border-top: 1px solid white;\n"
                                               "  border-left: 1px solid white;\n"
                                               "  border-right: 1px solid rgb(240,240,240);\n"
                                               "  border-bottom: 1px solid white;\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  width: 20px;\n"
                                               "  subcontrol-position: left;\n"
                                               "  subcontrol-origin: margin;\n"
                                               "border-bottom-left-radius: 3px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::sub-line:horizontal:hover {\n"
                                               "  background-color: rgb(218, 218, 218);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::sub-line:horizontal:pressed {\n"
                                               "  background-color: rgb(96, 96, 96);\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::left-arrow:horizontal {\n"
                                               "  image: url(icons/left_arrow_icon.svg); \n"
                                               "  width: 16px;\n"
                                               "  height: 16px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::left-arrow:horizontal:pressed {\n"
                                               "  right: -1px;\n"
                                               "  bottom: -1px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::right-arrow:horizontal {\n"
                                               "  image: url(icons/right_arrow_icon.svg); \n"
                                               "  width: 16px;\n"
                                               "  height: 16px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar::right-arrow:horizontal:pressed "
                                               "{\n"
                                               "  right: -1px;\n"
                                               "  bottom: -1px;\n"
                                               "}")
            else:
                self.met_line.append(QtWidgets.QLineEdit())
                self.met_line[i].setMinimumSize(QtCore.QSize(0, 27))
                self.met_line[i].setMaximumSize(QtCore.QSize(16777215, 27))
                self.met_line[i].setFrame(False)
                self.met_line[i].setText(str(value))
                self.met_line[i].setCursorPosition(0)
                self.met_line[i].setStyleSheet("QLineEdit {\n"
                                               "  border-radius: 3px;\n"
                                               "  padding: 1px 4px 1px 4px;\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  color: rgb(45,45,45);\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:disabled {\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "}")
            self.met_line[i].setEnabled(True)
            self.met_line[i].setReadOnly(True)
            self.met_line[i].setObjectName("met_line_" + str(i))
            self.met_line[i].setFocus(True)
            self.met_line[i].setFont(font2)
            self.global_attributes_layout.addWidget(self.met_line[i], i, 1, 1, 1)
            i += 1
        self.horizontalLayout_4.addLayout(self.global_attributes_layout)
        self.variable_list.addItems(var_list)

    def parse_variable_info(self):
        var_attr = self.file.get_attribute_list(self.variable_list.currentItem().text())
        clear_layout(self.variables_layout)
        self.var_label.clear()
        self.var_line.clear()
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        i = 0
        for key, value in var_attr.items():
            self.var_label.append(QtWidgets.QLabel())
            self.var_label[i].setFont(font)
            self.var_label[i].setMinimumSize(QtCore.QSize(0, 27))
            self.var_label[i].setMaximumSize(QtCore.QSize(16777215, 27))
            self.var_label[i].setObjectName("var_label_" + str(i))
            self.var_label[i].setText(key + ':')

            self.var_label[i].setStyleSheet("QLabel {\n"
                                            "   color: rgb(45,45,45);\n"
                                            "}")
            self.var_label[i].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.variables_layout.addWidget(self.var_label[i], i, 0, 1, 1)
            self.var_line.append(QtWidgets.QLineEdit())
            self.var_line[i].setMinimumSize(QtCore.QSize(0, 27))
            self.var_line[i].setMaximumSize(QtCore.QSize(16777215, 27))
            self.var_line[i].setFrame(False)
            self.var_line[i].setText(str(value))
            self.var_line[i].setCursorPosition(0)
            self.var_line[i].setStyleSheet("QLineEdit {\n"
                                           "  border-radius: 3px;\n"
                                           "  padding: 1px 4px 1px 4px;\n"
                                           "  background-color: rgb(240, 240, 240);\n"
                                           "  color: rgb(45,45,45);\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:disabled {\n"
                                           "  background-color: rgb(240, 240, 240);\n"
                                           "}")
            self.var_line[i].setEnabled(True)
            self.var_line[i].setReadOnly(True)
            self.var_line[i].setObjectName("met_line_" + str(i))
            self.var_line[i].setFocus(True)
            self.var_line[i].setFont(font2)
            self.variables_layout.addWidget(self.var_line[i], i, 1, 1, 1)
            i += 1

    def closeWindow(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchInfo - closeWindow')
        self.file.close()
        self.close()


def clear_layout(layout):
    logging.debug('gui - batch_processing_window_functions.py - clear_layout')
    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)
