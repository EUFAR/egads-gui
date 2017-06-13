# -*- coding: utf-8 -*-

import ntpath
import egads
import os
import inspect
from PyQt5 import QtWidgets, QtCore, QtGui
from other_functions import check_compatibility_netcdf


def gui_position(self):
    self.resize(1150, 544)
    screen_height = QtWidgets.QDesktopWidget().screenGeometry().height()
    screen_width = QtWidgets.QDesktopWidget().screenGeometry().width()
    _, _, w, h = self.geometry().getRect()
    x = screen_width / 2 - w / 2
    y = screen_height / 2 - h / 2
    self.setGeometry(x, y, w, h)
    

def gui_initialization(self):
    self.actionSeparator.setText('')
    self.actionSeparator2.setText('')
    self.actionSeparator3.setText('')
    self.actionSeparator4.setText('')
    for i in range(self.tabWidget.count()):
        self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
    self.tabWidget.removeTab(2)
    self.tabWidget.setEnabled(False)
    self.tabWidget.setVisible(False)
    
    
def netcdf_gui_initialization(self):
    self.tabWidget.setEnabled(True)
    self.tabWidget.setVisible(True)
    self.gm_history_ln_2.setVisible(False)
    self.gm_history_lb_2.setVisible(False)
    self.gm_button_6.setVisible(False)
    
    
def nasaames_gui_initialization(self):
    self.tabWidget.setEnabled(True)
    self.tabWidget.setVisible(True)
    self.gm_details_lb.setVisible(False)
    self.gm_compatibility_lb.setVisible(False)
    self.gm_history_ln.setMinimumSize(QtCore.QSize(420, 140))
    self.gm_history_ln.setMaximumSize(QtCore.QSize(16777215, 140))
    self.gm_history_ln_2.setMinimumSize(QtCore.QSize(420, 140))
    self.gm_history_ln_2.setMaximumSize(QtCore.QSize(16777215, 140))
    self.gm_history_lb.setText('<html><head/><body><p>Normal<br>comments:</p></body></html>')
    self.gm_project_lb.setText('Author(s)')
    self.va_longName_lb.setVisible(False)
    self.va_category_lb.setVisible(False)
    self.va_egadsProcessor_lb.setVisible(False)
    self.va_longName_ln.setVisible(False)
    self.va_category_ln.setVisible(False)
    self.va_egadsProcessor_ln.setVisible(False)
    self.va_button_2.setVisible(False)
    self.va_button_3.setVisible(False)
     

def icons_initialization(self):
    self.actionOpenBar.setEnabled(True)
    self.actionSaveBar.setEnabled(False)
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


def algorithm_list_menu_initialization(self):
    self.algorithm_folder_menu = []
    self.algorithm_folder_actions = []
    self.user_folder_menu = []
    self.user_folder_actions = []
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("icons/new_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2   .addPixmap(QtGui.QPixmap("icons/create_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    algorithm_path = egads.__path__[0] + '/algorithms'
    user_algorithm_path = egads.__path__[0] + '/algorithms/user'
    folder_list = []
    algorithm_structure = []
    user_algorithm_structure = []
    for item in os.walk(algorithm_path):
        index = item[0].find('algorithms')
        if item[0][index + 11:]:
            if not 'file_templates' in item[0][index + 11:] and not 'user' in item[0][index + 11:]:
                folder_list.append(item[0][index + 11:])
    for folder in folder_list:
        algorithm_tmp_list = dir(getattr(egads.algorithms, folder))
        algorithm_list = []
        for item in algorithm_tmp_list:
            if isinstance(getattr(getattr(egads.algorithms, folder), item), type):
                algorithm_list.append(item)
        algorithm_structure.append([folder, sorted(algorithm_list)])
    folder_list = []
    for item in os.walk(user_algorithm_path):
        index = item[0].find('user')
        if item[0][index + 5:]:
            folder_list.append(item[0][index + 5:])  
    for folder in folder_list:
        algorithm_tmp_list = dir(getattr(egads.algorithms.user, folder))
        algorithm_list = []
        for item in algorithm_tmp_list:
            if isinstance(getattr(getattr(egads.algorithms.user, folder), item), type):
                algorithm_list.append(item)
        user_algorithm_structure.append([folder, sorted(algorithm_list)])
    i = 0 
    for sublist in sorted(algorithm_structure):
        self.algorithm_folder_menu.append(QtWidgets.QMenu(self.menuEmbedded_algorithms))
        self.algorithm_folder_menu[i].setObjectName('embedded_category_' + sublist[0])
        self.algorithm_folder_menu[i].setTitle(sublist[0].title())
        self.menuEmbedded_algorithms.addAction(self.algorithm_folder_menu[i].menuAction())
        self.algorithm_folder_actions.append([])
        j = 0
        for algorithm in sublist[1]:
            self.algorithm_folder_actions[i].append(QtWidgets.QAction(self))
            self.algorithm_folder_actions[i][j].setIcon(icon1)
            self.algorithm_folder_actions[i][j].setFont(font)
            self.algorithm_folder_actions[i][j].setObjectName('embedded_' + sublist[0] + '_' + algorithm)
            self.algorithm_folder_actions[i][j].setText(algorithm)
            self.algorithm_folder_actions[i][j].triggered.connect(lambda: display_algorithm_information(self))
            self.algorithm_folder_menu[i].addAction(self.algorithm_folder_actions[i][j])
            j += 1
        i += 1
    i = 0
    for sublist in sorted(user_algorithm_structure):
        if sublist[1]:
            self.user_folder_menu.append(QtWidgets.QMenu(self.menuUser_defined_algorithms))
            self.user_folder_menu[i].setObjectName('user_category_' + sublist[0])
            self.user_folder_menu[i].setTitle(sublist[0].title())
            self.menuUser_defined_algorithms.addAction(self.user_folder_menu[i].menuAction())
            self.user_folder_actions.append([])
            j = 0
            for algorithm in sublist[1]:
                self.user_folder_actions[i].append(QtWidgets.QAction(self))
                self.user_folder_actions[i][j].setIcon(icon2)
                self.user_folder_actions[i][j].setFont(font)
                self.user_folder_actions[i][j].setObjectName('user_' + sublist[0] + '_' + algorithm)
                self.user_folder_actions[i][j].setText(algorithm)
                self.user_folder_actions[i][j].triggered.connect(lambda: display_algorithm_information(self))
                self.user_folder_menu[i].addAction(self.user_folder_actions[i][j])
                j += 1
            i += 1
    

def display_algorithm_information(self):
    
    print 'No function to display algorithms yet.'
    
    '''if 'embedded' in self.sender().objectName():
        second_index = self.sender().objectName().find('_', 9)
    elif 'user' in self.sender().objectName():
        second_index = self.sender().objectName().find('_', 5)
    first_index = self.sender().objectName().find('_')
        
    category = self.sender().objectName()[first_index + 1 : second_index]
    algorithm_name = self.sender().objectName()[second_index + 1 :]
    try:
        algorithm = getattr(getattr(egads.algorithms, category), algorithm_name)
    except AttributeError:
        algorithm = getattr(getattr(egads.algorithms.user, category), algorithm_name)
    
    file_path = inspect.getfile(algorithm)[:-1]
    
    with open(file_path, 'r') as in_file:
        init_file = in_file.readlines()
    
    author = init_file[0][14:-2]
    creation_date = init_file[1][20:-4]
    revision = init_file[2][27:-4].strip()
    
    file_index, version_index, category_index, purpose_index = None, None, None, None
    description_index, input_index, output_index, reference_index = None, None, None, None
    end_ref_index = None
    
    for index, line in enumerate(init_file):
        if '__author__' in line:
            author_index = index
        elif '__date__ ' in line:
            date_index = index
        elif 'FILE' in line:
            file_index = index
        elif 'VERSION' in line:
            version_index = index
        elif 'CATEGORY' in line:
            category_index = index
        elif 'PURPOSE' in line:
            purpose_index = index
        elif 'DESCRIPTION' in line:
            description_index = index
        elif 'INPUT' in line:
            input_index = index
        elif 'OUTPUT' in line:
            output_index = index
        elif 'SOURCE' in line:
            source_index = index
        elif 'REFERENCE' in line:
            reference_index = index
        elif 'def _algorithm' in line:
            algorithm_index = index + 1
        elif 'return ' in line:
            return_index = index
        elif 'def __init__(self, return_Egads=True):' in line:
            end_ref_index = index
        
    if (file_index == None or version_index == None or category_index == None or 
        purpose_index == None or description_index == None or input_index == None or 
        output_index == None or reference_index == None or end_ref_index == None or
        author_index == None or date_index == None):
        pass
        
    else:
        file_text, revision_text, category_text, purpose_text, description_text = '', '', '', '', ''
        input_text, output_text, source_text, reference_text, algorithm_text = '', '', '', '', ''
        author_text, date_text = '', ''
        
        author_text = ' '.join(''.join(init_file[author_index : author_index + 1]).strip().split())[14:-1]
        date_text = ' '.join(''.join(init_file[date_index : date_index + 1]).strip().split())[20:-3]
        file_text = ' '.join(''.join(init_file[file_index : version_index]).strip().split())[5:]
        revision_text = ' '.join(''.join(init_file[version_index : category_index]).strip().split())[19:-1]
        category_text = ' '.join(''.join(init_file[category_index : purpose_index]).strip().split())[9:]
        purpose_text = ' '.join(''.join(init_file[purpose_index : description_index]).strip().split())[8:]
        description_text = ' '.join(''.join(init_file[description_index : input_index]).strip().split())[12:]
        input_text = init_file[input_index : output_index]
        output_text = init_file[output_index : source_index]
        source_text = ' '.join(''.join(init_file[source_index : reference_index]).strip().split())[7:]
        reference_text = ' '.join(''.join(init_file[reference_index : end_ref_index]).strip().split())[11:-3]
        algorithm_text = ' '.join(''.join(init_file[algorithm_index : return_index]).strip().split())
        
        inputs = []
        input_text[0] = input_text[0].split('INPUT',1)[1]
        
        i = 0
        j = None
        for line in input_text:
            if len(line) - len(line.lstrip(' ')) > 20:
                if j == None:
                    j = i - 1
                inputs[j][1][2] = inputs[j][1][2] + ' ' + ' '.join(line.split())
            else:
                j = None
                tmp = line.split()
                if tmp:
                    inputs.append([tmp[0], [tmp[1], tmp[2], ' '.join(tmp[3:])]])
            i += 1
        
        
        outputs = []
        output_text[0] = output_text[0].split('OUTPUT',1)[1]
        
        i = 0
        j = None
        for line in output_text:
            if len(line) - len(line.lstrip(' ')) > 20:
                if j == None:
                    j = i - 1
                outputs[j][1][2] = outputs[j][1][2] + ' ' + ' '.join(line.split())
            else:
                j = None
                tmp = line.split()
                if tmp:
                    outputs.append([tmp[0], [tmp[1], tmp[2], ' '.join(tmp[3:])]])
            i += 1'''
        


def modify_attribute_gui(self):
    if self.sender().objectName() != "":
        value = self.buttons_lines_dict[str(self.sender().objectName())]
        widget = self.findChildren(QtWidgets.QLineEdit, value[0])
        if not widget:
            widget = self.findChildren(QtWidgets.QPlainTextEdit, value[0])
        list_widget = value[1]
        var_attr_list = value[2]
        if widget[0].isEnabled() == False:
            widget[0].setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/save_as_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.sender().setIcon(icon)
        else:
            self.modified = True
            self.make_window_title()
            widget[0].setEnabled(False)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.sender().setIcon(icon)
            value = self.objects_metadata_dict[str(widget[0].objectName())]
            if isinstance(value, list):
                if self.open_file_ext == 'NetCDF Files (*.nc)':
                    value = value[0]
                elif self.open_file_ext == 'NASA Ames Files (*.na)':
                    value = value[1]
            if list_widget is not None:
                try:
                    var_attr_list[str(list_widget.currentItem().text())][1][value] = str(widget[0].text())
                except AttributeError:
                    var_attr_list[str(list_widget.currentItem().text())][1][value] = str(widget[0].toPlainText())
                if value == "var_name":
                    var_attr_list[str(widget[0].text())] = var_attr_list.pop(str(list_widget.currentItem().text()))
                    list_widget.currentItem().setText(str(widget[0].text()))
            else:
                try:
                    var_attr_list[value] = str(widget[0].text())
                except AttributeError:
                    var_attr_list[value] = str(widget[0].toPlainText())
            

def update_global_attribute_gui(self, source):
    if source == 'NetCDF':
        read_set_attribute_gui(self, self.gm_title_ln, 'title', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_institution_ln, 'institution', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_source_ln, 'source', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_project_ln, 'project', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_dateCreation_ln, 'date_created', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_history_ln, 'history', self.list_of_global_attributes)
    elif source == 'NASA Ames':
        read_set_attribute_gui(self, self.gm_title_ln, 'MNAME', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_institution_ln, 'ORG', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_source_ln, 'SNAME', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_dateCreation_ln, 'DATE', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_history_ln, 'NCOM', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_history_ln_2, 'SCOM', self.list_of_global_attributes)
        read_set_attribute_gui(self, self.gm_project_ln, 'ONAME', self.list_of_global_attributes)
        

def update_variable_attribute_gui(self, index=None):
    if self.tabWidget.currentIndex() == 1 or index == 1:
        list_object = self.listWidget
        variables_and_attributes = self.list_of_variables_and_attributes 
        varName_ln = self.va_varName_ln
        longName_ln = self.va_longName_ln
        category_ln = self.va_category_ln
        processor_ln = self.va_egadsProcessor_ln
        units_ln = self.va_units_ln
        fillValue_ln = self.va_fillValue_ln
        dimensions_ln = self.va_dimensions_ln
    elif self.tabWidget.currentIndex() == 2 or index == 2:
        list_object = self.new_listwidget
        variables_and_attributes = self.list_of_new_variables_and_attributes
        varName_ln = self.new_varName_ln
        longName_ln = self.new_longName_ln
        category_ln = self.new_category_ln
        processor_ln = self.new_egadsProcessor_ln
        units_ln = self.new_units_ln
        fillValue_ln = self.new_fillValue_ln
        dimensions_ln = self.new_dimensions_ln
    sublist = variables_and_attributes[str(list_object.currentItem().text())]
    read_set_attribute_gui(self, varName_ln, 'var_name', sublist[1])
    read_set_attribute_gui(self, longName_ln, 'long_name', sublist[1])
    read_set_attribute_gui(self, units_ln, 'units', sublist[1])
    read_set_attribute_gui(self, category_ln, 'Category', sublist[1])
    read_set_attribute_gui(self, processor_ln, 'Processor', sublist[1])
    read_set_attribute_gui(self, fillValue_ln, '_FillValue', sublist[1])
    if not fillValue_ln.text():
        read_set_attribute_gui(self, fillValue_ln, 'missing_value', sublist[1])
    dimensions_str = ''
    for key, value in sublist[2].iteritems():
        dimensions_str = dimensions_str + str(value) + ' (' + key + '), '
    read_set_attribute_gui(self, dimensions_ln, dimensions_str[:-2])
    
    
def update_new_variable_list_gui(self):
    self.new_listwidget.clear()
    for _, sublist in self.list_of_new_variables_and_attributes.items():
        self.new_listwidget.addItem(sublist[0])


def add_new_variable_gui(self):
    self.tabWidget.insertTab(2, self.tab_3, 'New variables')
    self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(0,0,0))
    self.new_listwidget.itemClicked.connect(lambda: new_var_reading(self))


def new_var_reading(self):
    update_icons_state(self, 'new_var_reading')
    clear_gui(self, 'new_variable')
    all_lines_edit = self.tab_3.findChildren(QtWidgets.QLineEdit)
    for widget in all_lines_edit:
            widget.setEnabled(False)
    all_text_edit = self.tab_3.findChildren(QtWidgets.QPlainTextEdit)
    for widget in all_text_edit:
            widget.setEnabled(False)
    all_buttons = self.tab_3.findChildren(QtWidgets.QToolButton)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    for widget in all_buttons:
            widget.setIcon(icon)
    sublist = self.list_of_new_variables_and_attributes[self.new_listwidget.currentItem().text()]
    read_set_attribute_gui(self, self.new_varName_ln, 'var_name', sublist[1])
    read_set_attribute_gui(self, self.new_longName_ln, 'long_name', sublist[1])
    read_set_attribute_gui(self, self.new_units_ln, 'units', sublist[1])
    read_set_attribute_gui(self, self.new_category_ln, 'Category', sublist[1])
    read_set_attribute_gui(self, self.new_egadsProcessor_ln, 'Processor', sublist[1])
    read_set_attribute_gui(self, self.new_fillValue_ln, '_FillValue', sublist[1])
    if not self.new_fillValue_ln.text():
        read_set_attribute_gui(self, self.new_fillValue_ln, 'missing_value', sublist[1])
    dimensions_str = ''
    for key, value in sublist[2].iteritems():
        dimensions_str = dimensions_str + str(value) + ' (' + key + '), '
    read_set_attribute_gui(self, self.new_dimensions_ln, dimensions_str[:-2])


def statusBar_loading(self):
    self.sb_filename_lb = QtWidgets.QLabel()
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.sb_filename_lb.sizePolicy().hasHeightForWidth())
    self.sb_filename_lb.setSizePolicy(sizePolicy)
    self.sb_filename_lb.setMinimumSize(QtCore.QSize(0, 20))
    self.sb_filename_lb.setMaximumSize(QtCore.QSize(16777215, 20))
    font = QtGui.QFont()
    font.setFamily("font/SourceSansPro-Regular.ttf")
    font.setPointSize(9)
    font.setItalic(True)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.sb_filename_lb.setFont(font)
    self.sb_filename_lb.setObjectName("sb_filename_lb")
    self.sb_filename_lb.setText("")
    self.statusBar.addWidget(self.sb_filename_lb)


def statusBar_updating(self, filetype):
    if filetype == 'close_file':
        string = ''
    else:
        out_file_base, out_file_ext = ntpath.splitext(ntpath.basename(self.open_file_name))
        open_file_size = humansize(self, ntpath.getsize(self.open_file_name))
        filename = out_file_base + out_file_ext
        try:
            conventions = self.list_of_global_attributes['Conventions']
        except KeyError:
            conventions =  'no conventions'
        if filetype == 'NASA Ames':
            conventions = 'NASA Ames file conventions'
        string = filename + '   |   ' + open_file_size + '   |   ' + filetype + '   |   ' + conventions
    self.sb_filename_lb.setText(string)


def update_icons_state(self, string=None):
    if string == 'close_file':
        icons_initialization(self)
    if string == 'open_file':
        self.actionSaveAsBar.setEnabled(True)
        self.actionCloseBar.setEnabled(True)
        self.actionCreateVariableBar.setEnabled(True)
        self.actionGlobalAttributesBar.setEnabled(True)
    if string == 'var_reading':
        self.va_button_1.setEnabled(True)
        self.va_button_2.setEnabled(True)
        self.va_button_3.setEnabled(True)
        self.va_button_4.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.va_button_1.setIcon(icon)
        self.va_button_2.setIcon(icon)
        self.va_button_3.setIcon(icon)
        self.va_button_4.setIcon(icon)
        self.actionAlgorithmsBar.setEnabled(True)
        self.actionDeleteVariableBar.setEnabled(True)
        self.actionVariableAttributesBar.setEnabled(True)
        self.actionPlotBar.setEnabled(True)
        self.actionDisplayBar.setEnabled(True)
    if string == 'new_var_reading':
        self.new_button_1.setEnabled(True)
        self.new_button_2.setEnabled(True)
        self.new_button_3.setEnabled(True)
        self.new_button_4.setEnabled(True)
        self.actionAlgorithmsBar.setEnabled(True)
        self.actionDeleteVariableBar.setEnabled(True)
        self.actionVariableAttributesBar.setEnabled(True)
        self.actionPlotBar.setEnabled(True)
        self.actionDisplayBar.setEnabled(True)
        self.actionMigrateVariableBar.setEnabled(True)
    if string == None:
        self.actionAlgorithmsBar.setEnabled(False)
        self.actionDeleteVariableBar.setEnabled(False)
        self.actionVariableAttributesBar.setEnabled(False)
        self.actionPlotBar.setEnabled(False)
        self.actionDisplayBar.setEnabled(False)
        self.actionMigrateVariableBar.setEnabled(False)
        if self.tabWidget.currentIndex() == 1:
            self.actionAlgorithmsBar.setEnabled(True)
            self.actionPlotBar.setEnabled(True)
            try:
                if self.listWidget.currentItem().text() == "":
                    self.actionDisplayBar.setEnabled(False)
                    self.actionVariableAttributesBar.setEnabled(False)
                    self.actionDeleteVariableBar.setEnabled(False)
                else:
                    self.actionDisplayBar.setEnabled(True)
                    self.actionVariableAttributesBar.setEnabled(True)
                    self.actionDeleteVariableBar.setEnabled(True)
            except AttributeError:
                self.actionDisplayBar.setEnabled(False)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDeleteVariableBar.setEnabled(False)
        elif self.tabWidget.currentIndex() == 2:
            self.actionAlgorithmsBar.setEnabled(True)
            self.actionPlotBar.setEnabled(True)
            try:
                if self.new_listwidget.currentItem().text() == "":
                    self.actionDisplayBar.setEnabled(False)
                    self.actionVariableAttributesBar.setEnabled(False)
                    self.actionDeleteVariableBar.setEnabled(False)
                    self.actionMigrateVariableBar.setEnabled(False)
                else:
                    self.actionDisplayBar.setEnabled(True)
                    self.actionVariableAttributesBar.setEnabled(True)
                    self.actionDeleteVariableBar.setEnabled(True)
                    self.actionMigrateVariableBar.setEnabled(True)
            except AttributeError:
                self.actionDisplayBar.setEnabled(False)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDeleteVariableBar.setEnabled(False)
                self.actionMigrateVariableBar.setEnabled(False)


def clear_gui(self, part=None):
    if part == None or part == 'global':
        self.gm_filename_ln.setText('')
        self.gm_title_ln.setText("")
        self.gm_institution_ln.setText("")
        self.gm_source_ln.setText("")
        self.gm_project_ln.setText("")
        self.gm_dateCreation_ln.setText("")
        self.gm_history_ln.setPlainText("")
        update_compatibility_label(self, 'clear')
    if part == None or part == 'variable':
        self.va_varName_ln.setText("")
        self.va_longName_ln.setText("")
        self.va_category_ln.setText("")
        self.va_units_ln.setText("")
        self.va_fillValue_ln.setText("")
        self.va_dimensions_ln.setText("")
        self.va_egadsProcessor_ln.setPlainText("")
    if part == None or part == 'new_variable':
        self.new_varName_ln.setText("")
        self.new_longName_ln.setText("")
        self.new_category_ln.setText("")
        self.new_units_ln.setText("")
        self.new_fillValue_ln.setText("")
        self.new_dimensions_ln.setText("")
        self.new_egadsProcessor_ln.setPlainText("")
    if part == None:
        self.listWidget.clear()
        self.new_listwidget.clear()
 
       
def update_compatibility_label(self, string=None):
    if string is None:
        result = check_compatibility_netcdf(self, self.list_of_global_attributes, self.list_of_variables_and_attributes)
        sublist = self.compatibility_level[result]
        self.gm_compatibility_lb.setEnabled(True)
        self.gm_compatibility_lb.setVisible(True)
        self.gm_compatibility_lb.setPixmap(QtGui.QPixmap(sublist[1]))
        self.gm_details_lb.setText(sublist[2])
        self.gm_button_7.setEnabled(sublist[3])
        self.gm_button_7.setVisible(sublist[3])
    else:
        self.gm_compatibility_lb.setEnabled(False)
        self.gm_compatibility_lb.setVisible(False)
        self.gm_details_lb.setText('')
        self.gm_button_7.setEnabled(False)
        self.gm_button_7.setVisible(False)
        
        
def read_set_attribute_gui(self, gui_object, attr_name, attr_dict=None):
    if attr_dict is not None:
        try:
            value = attr_dict[attr_name]
        except KeyError:
            value = '' 
        if value == 'deleted':
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
        if attr_name == 'deleted':
            attr_name = ''
        try:
            gui_object.setText(str(attr_name))
            if not isinstance(gui_object, QtWidgets.QLabel):
                gui_object.setCursorPosition(0)
        except AttributeError:
            gui_object.setPlainText(str(attr_name))


def clear_layout(self, layout):
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(self, item.layout())
        layout.removeItem(item)
        
        

def humansize(self, nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])
       
