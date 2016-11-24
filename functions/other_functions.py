# -*- coding: utf-8 -*-
import egads.algorithms as algorithms

def prepare_algorithms_structure(self):
    directory_list = dir(algorithms)
    if "egads" in directory_list:
        directory_list.remove("egads")
    for index, item in enumerate(directory_list):
        if "__" not in item[:3]:
            break
    algorithm_structure = []
    for item in directory_list[index:]:
        algorithm_list = dir(getattr(algorithms, item))
        for index2, sublist in enumerate(algorithm_list):
            if "__" in sublist[:3]:
                break
        for sublist in algorithm_list[:index2]:
            algorithm_structure.append([item, sublist])
    return algorithm_structure

    
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
    
    for sublist in variable_attributes:
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

    