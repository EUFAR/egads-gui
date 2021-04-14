import logging
from PyQt5 import QtWidgets
from functions.utils import font_creation_function, icon_creation_function
from functions.window_functions.algorithm_windows_functions import MyAlgorithmDisplay
from functions.help_functions import frozen_algorithm_formula_text


def algorithm_menu_initialization(self):
    logging.debug('gui - old_gui_global_functions.py - algorithm_list_initialization')
    self.menuEmbedded_algorithms.clear()
    self.menuUser_defined_algorithms.clear()
    font1 = font_creation_function('normal')
    icon1 = icon_creation_function('new_algo_icon.svg')
    icon2 = icon_creation_function('create_algo_icon.svg')
    previous_rep = None
    algo_folder_user = None
    algo_folder = None
    for key in sorted(self.list_of_algorithms.keys()):
        idx = key.find(' - ')
        rep, algo, user = key[:idx], key[idx + 3:], self.list_of_algorithms[key]['user']
        if user:
            algo_action = QtWidgets.QAction(self)
            algo_action.setIcon(icon2)
            algo_action.setFont(font1)
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
            algo_action.setFont(font1)
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


def display_algorithm_information(self):
    logging.debug('gui - old_gui_global_functions.py - display_algorithm_information')
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
