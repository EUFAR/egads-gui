# -*- coding: utf-8 -*-
import egads
import os

def reload_user_directories(self):
    reload(egads.algorithms.user.comparisons)
    reload(egads.algorithms.user.corrections)
    reload(egads.algorithms.user.mathematics)
    reload(egads.algorithms.user.microphysics)
    reload(egads.algorithms.user.radiation)
    reload(egads.algorithms.user.thermodynamics)
    reload(egads.algorithms.user.transforms)
    # add folders created by user


def prepare_algorithms_structure(self):
    reload_user_directories(self)
    algorithm_path = egads.__path__[0] + '/algorithms'
    user_algorithm_path = egads.__path__[0] + '/algorithms/user'
    folder_list = []
    new_algorithm_structure = {}
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
        new_algorithm_structure[folder] = sorted(algorithm_list)
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
        try:
            tmp_list = new_algorithm_structure[folder] + algorithm_list
            new_algorithm_structure[folder] = sorted(tmp_list)
        except KeyError:
            new_algorithm_structure[folder] = sorted(algorithm_list)   
    return new_algorithm_structure

    
def check_compatibility_netcdf(self, global_attributes, variable_attributes):
    self.missing_global_attributes = []
    self.missing_variable_attributes = []
    self.missing_units = []
    number_missing_global_attributes = 0
    number_missing_unit = 0
    number_missing_fill = 0
    compatibility_metadata = 1
    compatibility_units = 1
    for key in self.required_eufar_global_attributes:
        if key not in global_attributes.keys():
            self.missing_global_attributes.append(key)
            number_missing_global_attributes += 1
    if number_missing_global_attributes > 0:
        compatibility_metadata = 2
    for key, sublist in variable_attributes.iteritems():
        append_unit = None
        append_fill = None
        if sublist[-1].units == "dimensionless":
            number_missing_unit += 1
            append_unit = "units"
        if "_FillValue" not in sublist[1].keys():
            if "missing_value" not in sublist[1].keys():
                if sublist[0] != "time" and sublist[0] != "Time":
                    number_missing_fill += 1
                    append_fill = "_FillValue"
        if append_unit or append_fill:
            self.missing_variable_attributes.append([sublist[0], append_unit, append_fill])
    if number_missing_fill > 0:
        compatibility_metadata = 2
    if number_missing_unit > 0 and number_missing_unit < len(variable_attributes)/float(3):
        compatibility_units = 3
    elif number_missing_unit >= len(variable_attributes)/float(3):
        compatibility_units = 4
    return max([compatibility_metadata, compatibility_units])


def add_global_attributes_to_buttons(self):
    self.buttons_lines_dict['gm_button_1'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_2'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_3'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_4'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_5'][2] = self.list_of_global_attributes
    
    
    

    