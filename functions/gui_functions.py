import logging
import pathlib
import xml
from PyQt5 import QtWidgets, QtCore, QtGui
from functions.algorithm_windows_functions import MyAlgorithmDisplay
from functions.other_windows_functions import MyInfo, MyUnit
from functions.utils import humansize, clear_layout, get_element_value, font_creation_function, icon_creation_function
from functions.gui_elements import DropFrame
from functions.help_functions import frozen_algorithm_formula_text
from functions.material_functions import widgets_metadata_dict
    

def gui_initialization(self):
    logging.debug('gui - gui_functions.py - gui_initialization')
    self.actionSeparator.setText('')
    self.actionSeparator2.setText('')
    self.actionSeparator3.setText('')
    self.actionSeparator4.setText('')
    self.actionSeparator5.setText('')
    self.actionSeparator5.setVisible(False)
    self.actionUpdate.setVisible(False)
    self.splitter.setSizes([270, 582])
    self.splitter_2.setSizes([270, 582])
    self.tab_view.removeTab(2)
    self.tab_view.setEnabled(False)
    self.tab_view.setVisible(False)
    self.gridLayout.removeWidget(self.tab_view)
    file_drop_layout(self)
    self.actionOpenBar.setEnabled(True)
    self.actionSaveAsBar.setEnabled(False)
    self.actionCloseBar.setEnabled(False)
    self.actionAlgorithmsBar.setEnabled(False)
    self.actionCreatealgorithmBar.setEnabled(True)
    self.actionCreateVariableBar.setEnabled(False)
    self.actionDeleteVariableBar.setEnabled(False)
    self.actionMigrateVariableBar.setEnabled(False)
    self.actionGlobalAttributesBar.setEnabled(False)
    self.actionVariableAttributesBar.setEnabled(False)
    self.actionDisplayBar.setEnabled(False)
    self.actionPlotBar.setEnabled(False)
    all_buttons = self.tab_view.findChildren(QtWidgets.QToolButton)
    for widget in all_buttons:
        if 'none_button' not in widget.objectName() and widget.objectName():
            if 'gm_' in widget.objectName():
                widget.clicked.connect(lambda: modify_attribute_gui_global(self, 'left'))
                widget.rightClick.connect(lambda: modify_attribute_gui_global(self, 'right'))
            elif 'va_' in widget.objectName():
                widget.clicked.connect(lambda: modify_attribute_gui_var(self, 'left'))
                widget.rightClick.connect(lambda: modify_attribute_gui_var(self, 'right'))
            elif 'new_' in widget.objectName():
                widget.clicked.connect(lambda: modify_attribute_gui_new(self, 'left'))
                widget.rightClick.connect(lambda: modify_attribute_gui_new(self, 'right'))


def algorithm_menu_initialization(self):
    logging.debug('gui - gui_functions.py - algorithm_list_initialization')
    self.menuEmbedded_algorithms.clear()
    self.menuUser_defined_algorithms.clear()
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("icons/new_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/create_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    previous_rep = None
    algo_folder_user = None
    algo_folder = None
    for key in sorted(self.list_of_algorithms.keys()):
        idx = key.find(' - ')
        rep, algo, user = key[:idx], key[idx + 3:], self.list_of_algorithms[key]['user']
        if user:
            algo_action = QtWidgets.QAction(self)
            algo_action.setIcon(icon1)
            algo_action.setFont(font)
            algo_action.setText(algo)
            algo_action.triggered.connect(lambda: display_algorithm_information(self))
            if rep == previous_rep:
                algo_action.setObjectName('user_' + rep + ' - ' + algo)
                algo_folder_user.addAction(algo_action)
            else:
                previous_rep = rep
                algo_folder_user = QtWidgets.QMenu(self.menuUser_defined_algorithms)
                algo_folder_user.setObjectName('user_category_' + rep)
                algo_folder_user.setTitle(rep.title())
                self.menuUser_defined_algorithms.addAction(algo_folder_user.menuAction())
                algo_action.setObjectName('user_' + rep + ' - ' + algo)
                algo_folder_user.addAction(algo_action)
    for key in sorted(self.list_of_algorithms.keys()):
        idx = key.find(' - ')
        rep, algo, user = key[:idx], key[idx + 3:], self.list_of_algorithms[key]['user']
        if not user:
            algo_action = QtWidgets.QAction(self)
            algo_action.setIcon(icon1)
            algo_action.setFont(font)
            algo_action.setText(algo)
            algo_action.triggered.connect(lambda: display_algorithm_information(self))
            if rep == previous_rep:
                algo_action.setObjectName('embedded_' + rep + ' - ' + algo)
                algo_folder.addAction(algo_action)
            else:
                previous_rep = rep
                algo_folder = QtWidgets.QMenu(self.menuEmbedded_algorithms)
                algo_folder.setObjectName('embedded_category_' + rep)
                algo_folder.setTitle(rep.title())
                self.menuEmbedded_algorithms.addAction(algo_folder.menuAction())
                algo_action.setObjectName('embedded_' + rep + ' - ' + algo)
                algo_folder.addAction(algo_action)

    
def netcdf_gui_initialization(self):
    logging.debug('gui - gui_functions.py - netcdf_gui_initialization')
    clear_layout(self.gridLayout)
    self.gridLayout.addWidget(self.tab_view, 0, 0, 1, 1)
    self.tab_view.setEnabled(True)
    self.tab_view.setVisible(True)
    self.gm_comments_ln.setVisible(False)
    self.gm_comments_lb.setVisible(False)
    self.gm_comments_bt.setVisible(False)
    self.gm_project_lb.setText('Project:')
    self.gm_history_lb.setText('History:')
    self.gm_title_lb.setText('Title:')
    self.gm_source_lb.setText('Source:')
    self.gm_institution_lb.setText('Institution:')
    self.va_longName_lb.setVisible(True)
    self.va_category_lb.setVisible(True)
    self.va_egadsProcessor_lb.setVisible(True)
    self.va_longName_ln.setVisible(True)
    self.va_category_ln.setVisible(True)
    self.va_egadsProcessor_ln.setVisible(True)
    self.va_longName_bt.setVisible(True)
    self.va_category_bt.setVisible(True)
    self.variable_list.setVisible(True)
    self.variable_list.setEnabled(True)
    
    
def nasaames_gui_initialization(self):
    logging.debug('gui - gui_functions.py - nasaames_gui_initialization')
    clear_layout(self.gridLayout)
    self.gridLayout.addWidget(self.tab_view, 0, 0, 1, 1)
    self.tab_view.setEnabled(True)
    self.tab_view.setVisible(True)
    self.gm_comments_ln.setVisible(True)
    self.gm_comments_lb.setVisible(True)
    self.gm_title_lb.setText('Title - MNAME:')
    self.gm_source_lb.setText('Source - SNAME:')
    self.gm_institution_lb.setText('Institution - ORG:')
    self.gm_history_lb.setText('Normal<br>comments<br>- NCOM:')
    self.gm_project_lb.setText('Author - ONAME:')
    self.va_longName_lb.setVisible(True)
    self.va_category_lb.setVisible(True)
    self.va_egadsProcessor_lb.setVisible(True)
    self.va_longName_ln.setVisible(True)
    self.va_category_ln.setVisible(True)
    self.va_egadsProcessor_ln.setVisible(True)
    self.va_longName_bt.setVisible(True)
    self.va_category_bt.setVisible(True)
    self.variable_list.setVisible(True)
    self.variable_list.setEnabled(True)
     

def display_algorithm_information(self):
    logging.debug('gui - gui_functions.py - display_algorithm_information')
    if 'embedded' in self.sender().objectName():
        rep_algo = self.sender().objectName()[9:]
    else:
        rep_algo = self.sender().objectName()[5:]
    file_path = self.list_of_algorithms[rep_algo]['path']
    if 'c' == file_path[-1:]:
        file_path = file_path[:-1]
    algorithm = self.list_of_algorithms[rep_algo]['method']
    algorithm_name = self.list_of_algorithms[rep_algo]['name']
    algorithm_metadata = algorithm().metadata
    output_metadata = algorithm().output_metadata
    algorithm_dict = dict()
    algorithm_dict['Name'] = algorithm_metadata['Processor']
    algorithm_dict['File'] = algorithm_name + '.py'
    algorithm_dict['Purpose'] = algorithm_metadata['Purpose']
    algorithm_dict['Description'] = algorithm_metadata['Description']
    algorithm_dict['Source'] = algorithm_metadata['Source']
    algorithm_dict['References'] = algorithm_metadata['References']
    algorithm_dict['Version'] = algorithm_metadata['ProcessorVersion']
    algorithm_dict['Date'] = algorithm_metadata['ProcessorDate']
    inputs = algorithm_metadata['Inputs']
    outputs = algorithm_metadata['Outputs']
    algorithm_inputs = []
    algorithm_outputs = []
    for index, str_input in enumerate(inputs):
        input_dict = dict()
        input_dict['Symbol'] = str_input
        input_dict['Units'] = algorithm_metadata['InputUnits'][index]
        input_dict['Type'] = algorithm_metadata['InputTypes'][index]
        input_dict['Description'] = algorithm_metadata['InputDescription'][index]
        algorithm_inputs.append(input_dict)
    for index, str_output in enumerate(outputs):
        output_dict = dict()
        output_dict['Symbol'] = str_output
        output_dict['Units'] = algorithm_metadata['OutputUnits'][index]
        output_dict['Type'] = algorithm_metadata['OutputTypes'][index]
        output_dict['Description'] = algorithm_metadata['OutputDescription'][index]
        try:
            output_dict['StandardName'] = output_metadata[index]['standard_name']
            output_dict['LongName'] = output_metadata[index]['long_name']
            output_dict['Category'] = output_metadata[index]['Category']
        except KeyError:
            output_dict['StandardName'] = output_metadata['standard_name']
            output_dict['LongName'] = output_metadata['long_name']
            output_dict['Category'] = output_metadata['Category']
        algorithm_outputs.append(output_dict)
    algorithm_dict['Input'] = algorithm_inputs
    algorithm_dict['Output'] = algorithm_outputs
    if self.frozen_app:
        try:
            algorithm_dict['Algorithm'] = frozen_algorithm_formula_text()[rep_algo]
        except KeyError:
            lines = []
            read = False
            f = open(file_path, 'r')
            for line in f:
                if 'def _algorithm' in line:
                    read = True
                    continue
                if read:
                    lines.append(line)
            f.close()
            algorithm_dict['Algorithm'] = ''.join(lines)
    else:
        lines = []
        read = False
        f = open(file_path, 'r')
        for line in f:
            if 'def _algorithm' in line:
                read = True
                continue
            if read:
                lines.append(line)
        f.close()
        algorithm_dict['Algorithm'] = ''.join(lines)
    self.displayAlgorithmWindow = MyAlgorithmDisplay(algorithm_dict)
    self.displayAlgorithmWindow.exec_()


def modify_attribute_gui_global(self, click):
    button = self.sender()
    line = self.findChild(QtWidgets.QLineEdit, button.objectName()[:-2] + 'ln')
    if not line:
        line = self.findChild(QtWidgets.QPlainTextEdit, button.objectName()[:-2] + 'ln')
    if not line.isEnabled():
        if click == 'left':
            line.setEnabled(True)
            button.setIcon(icon_creation_function('save_as_icon.svg'))
    else:
        if click == 'left':
            metadata = widgets_metadata_dict()[str(line.objectName())]
            if isinstance(metadata, list):
                if self.file_ext == 'NetCDF Files (*.nc)':
                    metadata = metadata[0]
                elif self.file_ext == 'NASA Ames Files (*.na)':
                    metadata = metadata[1]
            try:
                self.list_of_global_attributes[metadata] = str(line.text())
            except AttributeError:
                self.list_of_global_attributes[metadata] = str(line.toPlainText())
            self.start_status_bar_msg_thread('Global attributes have been modified...')
            self.modified = True
            self.make_window_title()
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
        elif click == 'right':
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
            metadata = widgets_metadata_dict()[str(line.objectName())]
            if isinstance(metadata, list):
                if self.file_ext == 'NetCDF Files (*.nc)':
                    metadata = metadata[0]
                elif self.file_ext == 'NASA Ames Files (*.na)':
                    metadata = metadata[1]
            if isinstance(self.list_of_global_attributes[metadata], list):
                long_string = ''
                for string in self.list_of_global_attributes[metadata]:
                    if isinstance(string, int):
                        long_string += str(string) + '-'
                    else:
                        long_string += string + ', '
                if long_string[-1:] == '-':
                    text = long_string[:-1]
                else:
                    text = long_string[:-2]
            else:
                text = self.list_of_global_attributes[metadata]
            try:
                line.setText(text)
                line.setCursorPosition(0)
            except AttributeError:
                line.setPlainText(text)
            self.start_status_bar_msg_thread('The modification has been canceled...')


def modify_attribute_gui_var(self, click):
    button = self.sender()
    line = self.findChild(QtWidgets.QLineEdit, button.objectName()[:-2] + 'ln')
    if not line:
        line = self.findChild(QtWidgets.QPlainTextEdit, button.objectName()[:-2] + 'ln')
    if not line.isEnabled():
        if click == 'left':
            line.setEnabled(True)
            button.setIcon(icon_creation_function('save_as_icon.svg'))
    else:
        if click == 'left':
            metadata = widgets_metadata_dict()[str(line.objectName())]
            if metadata == 'var_name':
                self.list_of_variables_and_attributes[str(line.text())] = self.list_of_variables_and_attributes.pop(str(
                    self.variable_list.currentItem().text()))
                self.variable_list.currentItem().setText(str(line.text()))
            else:
                var = str(self.variable_list.currentItem().text())
                try:
                    self.list_of_variables_and_attributes[var][0].metadata[metadata] = str(line.text())
                except AttributeError:
                    self.list_of_variables_and_attributes[var][0].metadata[metadata] = str(line.toPlainText())
            self.start_status_bar_msg_thread('Variable attributes have been modified...')
            self.modified = True
            self.make_window_title()
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
        elif click == 'right':
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
            metadata = widgets_metadata_dict()[str(line.objectName())]
            if isinstance(metadata, list):
                if self.file_ext == 'NetCDF Files (*.nc)':
                    metadata = metadata[0]
                elif self.file_ext == 'NASA Ames Files (*.na)':
                    metadata = metadata[1]
            var = str(self.variable_list.currentItem().text())
            if value == 'var_name':
                line.setText(var)
            else:
                try:
                    line.setText(self.list_of_variables_and_attributes[var][0].metadata[metadata])
                    line.setCursorPosition(0)
                except AttributeError:
                    line.toPlainText(self.list_of_variables_and_attributes[var][0].metadata[metadata])


def modify_attribute_gui_new(self, click):
    button = self.sender()
    line = self.findChild(QtWidgets.QLineEdit, button.objectName()[:-2] + 'ln')
    if not line:
        line = self.findChild(QtWidgets.QPlainTextEdit, button.objectName()[:-2] + 'ln')
    if not line.isEnabled():
        if click == 'left':
            line.setEnabled(True)
            button.setIcon(icon_creation_function('save_as_icon.svg'))
    else:
        if click == 'left':
            metadata = widgets_metadata_dict()[str(line.objectName())]
            if metadata == 'var_name':
                self.list_of_new_variables_and_attributes[str(line.text())] =\
                    self.list_of_new_variables_and_attributes.pop(str(self.variable_list.currentItem().text()))
                self.new_variable_list.currentItem().setText(str(line.text()))
            else:
                var = str(self.new_variable_list.currentItem().text())
                try:
                    self.list_of_new_variables_and_attributes[var][0].metadata[metadata] = str(line.text())
                except AttributeError:
                    self.list_of_new_variables_and_attributes[var][0].metadata[metadata] = str(line.toPlainText())
            self.start_status_bar_msg_thread('Variable attributes have been modified...')
            self.modified = True
            self.make_window_title()
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
        elif click == 'right':
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
            metadata = widgets_metadata_dict()[str(line.objectName())]
            var = str(self.new_variable_list.currentItem().text())
            if value == 'var_name':
                line.setText(var)
            else:
                try:
                    line.setText(self.list_of_new_variables_and_attributes[var][0].metadata[metadata])
                    line.setCursorPosition(0)
                except AttributeError:
                    line.toPlainText(self.list_of_new_variables_and_attributes[var][0].metadata[metadata])


def update_global_attribute_gui(self, source):
    logging.debug('gui - gui_functions.py - update_global_attribute_gui : source ' + str(source))
    if source == 'NetCDF':
        read_set_attribute_gui(self.gm_title_ln, 'title', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_institution_ln, 'institution', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_source_ln, 'source', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_project_ln, 'project', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_history_ln, 'history', self.list_of_global_attributes)
    elif source == 'NASA Ames':
        read_set_attribute_gui(self.gm_title_ln, 'MNAME', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_institution_ln, 'ORG', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_source_ln, 'SNAME', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_history_ln, 'NCOM', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_comments_ln, 'SCOM', self.list_of_global_attributes)
        read_set_attribute_gui(self.gm_project_ln, 'ONAME', self.list_of_global_attributes)
    dimension_str = ''
    for key, value in self.list_of_dimensions.items():
        dimension_str += key + ': ' + str(value) + ' ; '
    self.va_dimensionList_ln.setPlainText(dimension_str[:-3])
    self.new_dimensionList_ln.setPlainText(dimension_str[:-3])
        

def update_variable_attribute_gui(self, index=None):
    logging.debug('gui - gui_functions.py - update_variable_attribute_gui : index ' + str(index))
    list_object, variables_and_attributes, var_name, long_name = None, None, None, None
    fill_value, units, category, processor, dimensions = None, None, None, None, None
    if self.tab_view.currentIndex() == 1 or index == 1:
        list_object = self.variable_list
        variables_and_attributes = self.list_of_variables_and_attributes 
        var_name = self.va_varName_ln
        long_name = self.va_longName_ln
        category = self.va_category_ln
        processor = self.va_egadsProcessor_ln
        units = self.va_units_ln
        fill_value = self.va_fill_ln
        dimensions = self.va_dimensions_ln
    elif self.tab_view.currentIndex() == 2 or index == 2:
        list_object = self.new_variable_list
        variables_and_attributes = self.list_of_new_variables_and_attributes
        var_name = self.new_varName_ln
        long_name = self.new_longName_ln
        category = self.new_category_ln
        processor = self.new_egadsProcessor_ln
        units = self.new_units_ln
        fill_value = self.new_fill_ln
        dimensions = self.new_dimensions_ln
    var = str(list_object.currentItem().text())
    sublist = variables_and_attributes[var]
    metadata_dict = sublist[0].metadata
    var_name.setText(var)
    read_set_attribute_gui(long_name, 'long_name', metadata_dict)
    read_set_attribute_gui(units, 'units', metadata_dict)
    read_set_attribute_gui(category, 'Category', metadata_dict)
    read_set_attribute_gui(processor, 'Processor', metadata_dict)
    read_set_attribute_gui(fill_value, '_FillValue', metadata_dict)
    if not fill_value.text():
        read_set_attribute_gui(fill_value, 'missing_value', metadata_dict)
    dimensions_str = ''
    for key, value in sublist[1].items():
        dimensions_str = dimensions_str + str(value) + ' (' + key + '), '
    read_set_attribute_gui(dimensions, dimensions_str[:-2])
    
    
def update_new_variable_list_gui(self):
    logging.debug('gui - gui_functions.py - update_new_variable_list_gui')
    self.new_variable_list.clear()
    for key in self.list_of_new_variables_and_attributes:
        self.new_variable_list.addItem(key)


def status_bar_update(self):
    logging.debug('gui - gui_functions.py - status_bar_update')
    if self.file_is_opened:
        filename = pathlib.PurePath(self.file_name).name
        filesize = humansize(pathlib.Path(self.file_name).stat().st_size)
        filetype = ''
        conventions = ''
        if self.file_ext == 'NetCDF Files (*.nc)':
            filetype = 'NetCDF'
            try:
                conventions = self.list_of_global_attributes['Conventions']
            except KeyError:
                logging.debug('gui - gui_functions.py - status_bar_update : no conventions')
                conventions = 'no conventions'
        elif self.file_ext == 'NASA Ames Files (*.na)':
            filetype = 'NASA Ames'
            conventions = 'NASA Ames file conventions'
        self.default_message = filename + '   |   ' + filesize + '   |   ' + filetype + '   |   ' + conventions
    else:
        self.default_message = ''
    self.statusBar.showMessage(self.default_message)


def update_icons_state(self, string=None):
    logging.debug('gui - gui_functions.py - update_icons_state : string ' + str(string))
    if string == 'close_file':
        self.actionOpenBar.setEnabled(True)
        self.actionSaveAsBar.setEnabled(False)
        self.actionCloseBar.setEnabled(False)
        self.actionExport.setEnabled(False)
        self.actionAlgorithmsBar.setEnabled(False)
        self.actionCreateVariableBar.setEnabled(False)
        self.actionDeleteVariableBar.setEnabled(False)
        self.actionMigrateVariableBar.setEnabled(False)
        self.actionGlobalAttributesBar.setEnabled(False)
        self.actionVariableAttributesBar.setEnabled(False)
        self.actionDisplayBar.setEnabled(False)
        self.actionPlotBar.setEnabled(False)
    if string == 'open_file':
        self.actionSaveAsBar.setEnabled(True)
        self.actionCloseBar.setEnabled(True)
        self.actionExport.setEnabled(True)
        self.actionAlgorithmsBar.setEnabled(True)
        self.actionGlobalAttributesBar.setEnabled(True)
        self.actionCreateVariableBar.setEnabled(True)
    if string == 'var_reading':
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.va_varName_bt.setIcon(icon)
        self.va_longName_bt.setIcon(icon)
        self.va_category_bt.setIcon(icon)
        if len(self.variable_list.selectedItems()) > 1:
            self.va_varName_bt.setEnabled(False)
            self.va_longName_bt.setEnabled(False)
            self.va_category_bt.setEnabled(False)
            self.actionDisplayBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionDeleteVariableBar.setEnabled(True)
            self.actionPlotBar.setEnabled(True)
        else:
            self.va_varName_bt.setEnabled(True)
            self.va_longName_bt.setEnabled(True)
            self.va_category_bt.setEnabled(True)
            self.actionDisplayBar.setEnabled(True)
            self.actionVariableAttributesBar.setEnabled(True)
            self.actionDeleteVariableBar.setEnabled(True)
            self.actionPlotBar.setEnabled(True)
    if string == 'new_var_reading':
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_varName_bt.setIcon(icon)
        self.new_longName_bt.setIcon(icon)
        self.new_category_bt.setIcon(icon)
        if len(self.new_variable_list.selectedItems()) > 1:
            self.new_varName_bt.setEnabled(False)
            self.new_longName_bt.setEnabled(False)
            self.new_category_bt.setEnabled(False)
            self.actionDisplayBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionDeleteVariableBar.setEnabled(True)
            self.actionPlotBar.setEnabled(True)
            self.actionMigrateVariableBar.setEnabled(True)
        else:
            self.new_varName_bt.setEnabled(True)
            self.new_longName_bt.setEnabled(True)
            self.new_category_bt.setEnabled(True)
            self.actionDisplayBar.setEnabled(True)
            self.actionVariableAttributesBar.setEnabled(True)
            self.actionDeleteVariableBar.setEnabled(True)
            self.actionPlotBar.setEnabled(True)
            self.actionMigrateVariableBar.setEnabled(True)
    if string is None:
        self.actionDeleteVariableBar.setEnabled(False)
        self.actionVariableAttributesBar.setEnabled(False)
        self.actionPlotBar.setEnabled(False)
        self.actionDisplayBar.setEnabled(False)
        self.actionMigrateVariableBar.setEnabled(False)
        if self.tab_view.currentIndex() == 1:
            try:
                if not self.variable_list.selectedItems():
                    self.actionDisplayBar.setEnabled(False)
                    self.actionVariableAttributesBar.setEnabled(False)
                    self.actionDeleteVariableBar.setEnabled(False)
                    self.actionPlotBar.setEnabled(False)
                else:
                    if len(self.variable_list.selectedItems()) > 1:
                        self.actionDisplayBar.setEnabled(False)
                        self.actionVariableAttributesBar.setEnabled(False)
                        self.actionDeleteVariableBar.setEnabled(True)
                        self.actionPlotBar.setEnabled(True)
                    else:
                        self.actionDisplayBar.setEnabled(True)
                        self.actionVariableAttributesBar.setEnabled(True)
                        self.actionDeleteVariableBar.setEnabled(True)
                        self.actionPlotBar.setEnabled(True)
            except AttributeError:
                self.actionDisplayBar.setEnabled(False)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDeleteVariableBar.setEnabled(False)
                self.actionPlotBar.setEnabled(False)
        elif self.tab_view.currentIndex() == 2:
            try:
                if not self.new_variable_list.selectedItems():
                    self.actionDisplayBar.setEnabled(False)
                    self.actionVariableAttributesBar.setEnabled(False)
                    self.actionDeleteVariableBar.setEnabled(False)
                    self.actionPlotBar.setEnabled(False)
                    self.actionMigrateVariableBar.setEnabled(False)
                else:
                    if len(self.new_variable_list.selectedItems()) > 1:
                        self.actionDisplayBar.setEnabled(False)
                        self.actionVariableAttributesBar.setEnabled(False)
                        self.actionDeleteVariableBar.setEnabled(True)
                        self.actionPlotBar.setEnabled(True)
                        self.actionMigrateVariableBar.setEnabled(True)
                    else:
                        self.actionDisplayBar.setEnabled(True)
                        self.actionVariableAttributesBar.setEnabled(True)
                        self.actionDeleteVariableBar.setEnabled(True)
                        self.actionPlotBar.setEnabled(True)
                        self.actionMigrateVariableBar.setEnabled(True)
            except AttributeError:
                self.actionDisplayBar.setEnabled(False)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDeleteVariableBar.setEnabled(False)
                self.actionMigrateVariableBar.setEnabled(False)
                self.actionPlotBar.setEnabled(False)


def clear_gui(self, part=None):
    logging.debug('gui - gui_functions.py - clear_gui : part ' + str(part))
    if part is None or part == 'global':
        self.gm_title_ln.setText("")
        self.gm_institution_ln.setText("")
        self.gm_source_ln.setText("")
        self.gm_project_ln.setText("")
        self.gm_history_ln.setPlainText("")
        self.va_dimensionList_ln.setPlainText('')
    if part is None or part == 'variable':
        self.va_varName_ln.setText("")
        self.va_longName_ln.setText("")
        self.va_category_ln.setText("")
        self.va_units_ln.setText("")
        self.va_fill_ln.setText("")
        self.va_dimensions_ln.setText("")
        self.va_egadsProcessor_ln.setPlainText("")
    if part is None or part == 'new_variable':
        self.new_varName_ln.setText("")
        self.new_longName_ln.setText("")
        self.new_category_ln.setText("")
        self.new_units_ln.setText("")
        self.new_fill_ln.setText("")
        self.new_dimensions_ln.setText("")
        self.new_egadsProcessor_ln.setPlainText("")
    if part is None:
        self.variable_list.clear()
        self.new_variable_list.clear()
   
        
def read_set_attribute_gui(gui_object, attr_name, attr_dict=None):
    logging.debug('gui - gui_functions.py - read_set_attribute_gui')
    if attr_dict is not None:
        try:
            value = attr_dict[attr_name]
        except KeyError:
            value = ''
        if isinstance(value, list):
            long_string = ''
            for string in value:
                if isinstance(string, int):
                    long_string += str(string) + '-'
                else:
                    long_string += string + ', '
            if long_string[-1:] == '-':
                value = long_string[:-1]
            else:
                value = long_string[:-2]
        try:
            gui_object.setText(str(value))
            if not isinstance(gui_object, QtWidgets.QLabel):
                gui_object.setCursorPosition(0)
        except AttributeError:
            gui_object.setPlainText(str(value))
    else:
        try:
            gui_object.setText(str(attr_name))
            if not isinstance(gui_object, QtWidgets.QLabel):
                gui_object.setCursorPosition(0)
        except AttributeError:
            gui_object.setPlainText(str(attr_name))


def file_drop_layout(self):
    logging.debug('gui - gui_functions.py - file_drop_layout')
    self.drop_grid_layout_2 = QtWidgets.QGridLayout()
    self.drop_grid_layout_2.setObjectName("drop_grid_layout_2")
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Expanding), 0, 1, 1, 1)
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum), 1, 0, 1, 1)
    self.drop_frame = DropFrame()
    self.drop_frame.setMinimumSize(QtCore.QSize(380, 190))
    self.drop_frame.setMaximumSize(QtCore.QSize(380, 190))
    self.drop_frame.setAcceptDrops(True)
    self.drop_frame.setStyleSheet("QFrame {\n"
                                  "   background: rgb(230, 230, 230);\n"
                                  "   border: 3px dashed rgb(150,150,150);\n"
                                  "}")
    self.drop_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.drop_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.drop_frame.setObjectName("drop_frame")
    self.drop_grid_layout = QtWidgets.QGridLayout(self.drop_frame)
    self.drop_grid_layout.setObjectName("drop_grid_layout")
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum,
                                                        QtWidgets.QSizePolicy.Expanding), 0, 1, 1, 1)
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum), 1, 0, 1, 1)
    self.drop_vert_layout = QtWidgets.QVBoxLayout()
    self.drop_vert_layout.setObjectName("drop_vert_layout")
    self.drop_hor_layout = QtWidgets.QHBoxLayout()
    self.drop_hor_layout.setObjectName("drop_hor_layout")
    self.drop_hor_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                       QtWidgets.QSizePolicy.Minimum))
    self.drop_label_1 = QtWidgets.QLabel(self.drop_frame)
    self.drop_label_1.setMinimumSize(QtCore.QSize(50, 50))
    self.drop_label_1.setMaximumSize(QtCore.QSize(50, 50))
    self.drop_label_1.setStyleSheet("QLabel {\n"
                                    "   background: transparent;\n"
                                    "   border: 0px solid black;\n"
                                    "   color: rgb(45,45,45);\n"
                                    "}")
    self.drop_label_1.setText("")
    self.drop_label_1.setPixmap(QtGui.QPixmap("icons/egads_icon.svg"))
    self.drop_label_1.setScaledContents(True)
    self.drop_label_1.setObjectName("drop_label_1")
    self.drop_hor_layout.addWidget(self.drop_label_1)
    self.drop_hor_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                       QtWidgets.QSizePolicy.Minimum))
    self.drop_vert_layout.addLayout(self.drop_hor_layout)
    self.drop_label_2 = QtWidgets.QLabel(self.drop_frame)
    self.drop_label_2.setMinimumSize(QtCore.QSize(0, 27))
    self.drop_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.drop_label_2.setFont(font)
    self.drop_label_2.setStyleSheet("QLabel {\n"
                                    "   background: transparent;\n"
                                    "   border: 0px solid black;\n"
                                    "   color: rgb(45,45,45);\n"
                                    "}")
    self.drop_label_2.setObjectName("drop_label_2")
    self.drop_label_2.setText("<html><head/><body><p><span style=\" font-weight:600;\">Choose</span> a file or <span "
                              "style=\" font-weight:600;\">drop</span> it here.</p></body></html>")
    self.drop_vert_layout.addWidget(self.drop_label_2)
    self.drop_grid_layout.addLayout(self.drop_vert_layout, 1, 1, 1, 1)
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum,
                                                        QtWidgets.QSizePolicy.Expanding), 2, 1, 1, 1)
    self.drop_grid_layout_2.addWidget(self.drop_frame, 1, 1, 1, 1)
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Expanding), 2, 1, 1, 1)
    self.gridLayout.addLayout(self.drop_grid_layout_2, 0, 0, 1, 1)
    self.drop_frame.leftClick.connect(self.open_file)
    self.drop_frame.dropFile.connect(self.open_file)
    self.drop_frame.manyFiles.connect(lambda: too_many_files(self))


def too_many_files(self):
    logging.debug('gui - gui_functions.py - too_many_files')
    info_text = 'It is nos possible to open more than one file with the GUI at this time. If multiple files have to ' \
                'be processed, please use the Bath processing function in the File menu.'
    self.infoWindow = MyInfo(info_text)
    self.infoWindow.exec_()


def create_quick_access_menu(self):
    self.menuQuick_access.clear()
    self.menuQuick_access.setEnabled(True)
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/quick_access_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    f = open(str(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')), 'r')
    doc = xml.dom.minidom.parse(f)
    folders = doc.getElementsByTagName('Folders')[0]
    nodes = folders.getElementsByTagName('Folder')
    for node in nodes:
        quick_folder = QtWidgets.QAction(self)
        quick_folder.setIcon(icon)
        quick_folder.setFont(font)
        quick_folder.setText(get_element_value(node, 'Name'))
        quick_folder.setToolTip(get_element_value(node, 'Path'))
        quick_folder.triggered.connect(lambda: quick_access_open_folder(self))
        quick_folder.setObjectName(get_element_value(node, 'Name'))
        self.menuQuick_access.addAction(quick_folder)
    f.close()


def quick_access_open_folder(self):
    path = self.sender().toolTip()
    file_name, _ = self.get_file_name('open', path)
    if file_name:
        self.open_file(file_name)


def create_recent_file_menu(self):
    self.menuOpen_recent.clear()
    self.menuOpen_recent.setEnabled(True)
    if self.opened_file_list:
        font = font_creation_function('normal')
        icon = icon_creation_function('del_icon.svg')
        for i, file in enumerate(self.opened_file_list):
            recent_file = QtWidgets.QAction(self)
            recent_file.setFont(font)
            recent_file.setToolTip(file)
            recent_file.setObjectName(file)
            if len(file) > 65:
                file = file[:30] + ' ... ' + file[-30:]
            recent_file.setText(file)
            recent_file.triggered.connect(lambda: open_recent_filename(self))
            self.menuOpen_recent.addAction(recent_file)
        self.menuOpen_recent.addSeparator()
        del_action = QtWidgets.QAction(self)
        del_action.setFont(font)
        del_action.setIcon(icon)
        del_action.setText('Clear the list...')
        del_action.triggered.connect(lambda: clear_file_list_in_menu(self))
        del_action.setObjectName('del_action')
        self.menuOpen_recent.addAction(del_action)


def clear_file_list_in_menu(self):
    self.opened_file_list.clear()
    create_recent_file_menu(self)


def open_recent_filename(self):
    self.open_file(self.sender().objectName())
