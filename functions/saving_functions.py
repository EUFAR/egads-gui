# -*- coding: utf-8 -*-

import egads
import tempfile


def save_as_netcdf(self, save_file_name):
    if self.open_file_ext == "NetCDF Files (*.nc)":
        self.newFile = egads.input.NetCdf(save_file_name, 'w')  # @UndefinedVariable
        for key, value in self.list_of_dimensions.iteritems():
            self.newFile.add_dim(key, value)
        for key, value in self.list_of_global_attributes.iteritems():
            if value != "deleted":
                try:
                    self.newFile.add_attribute(key, float(value))
                except ValueError:
                    self.newFile.add_attribute(key, str(value))
        for sublist in self.list_of_variables_and_attributes:
            
                if sublist[1] != "deleted":
                    data = sublist[3].value
                    dimensions_tuple = []
                    for key, value in sublist[2].iteritems():
                        dimensions_tuple.append(key)
                    dimensions_tuple = tuple(dimensions_tuple)
                    try:
                        fillvalue = sublist[1]["_FillValue"]
                    except KeyError:
                        try:
                            fillvalue = sublist[1]["missing_value"]
                        except KeyError:
                            fillvalue = None
                    self.newFile.write_variable(data, sublist[0], (dimensions_tuple), 'double', fillvalue)    
                    for key, value in sublist[1].iteritems():
                        if isinstance(value, list):
                            tmp = ""
                            for item in value:
                                tmp += item + ", "
                            tmp = tmp[:-2]
                            self.newFile.add_attribute(str(key), str(tmp), str(sublist[0]))
                        else:
                            if str(key) != "var_name" and str(key) != "_FillValue" and value != "deleted":
                                try:
                                    self.newFile.add_attribute(str(key), float(value), str(sublist[0]))
                                except ValueError:
                                    self.newFile.add_attribute(str(key), str(value), str(sublist[0]))
                    if sublist[0] != sublist[1]["var_name"]:
                        self.newFile.change_variable_name(str(sublist[0]), str(sublist[1]["var_name"]))
                        
                else:
                    pass
        self.newFile.close()
        return
    if self.open_file_ext == "NASA Ames Files (*.na)":
        self.opened_file.convert_to_netcdf(str(save_file_name))
    if self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
        print "this function is not available yet"
    
    
def save_as_nasaaimes(self, save_file_name):
    if self.open_file_ext == "NetCDF Files (*.nc)":
        temp_file_name = tempfile.NamedTemporaryFile()
        save_as_netcdf(self, temp_file_name.name + ".nc")
        self.opened_file.convert_to_nasa_ames(save_file_name, self.list_of_variables, temp_file = temp_file_name.name + ".nc")
        temp_file_name.close()
    if self.open_file_ext == "NASA Ames Files (*.na)":
        
        self.opened_file.save_new_na_file(save_file_name)
        
    if self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
        print "this function is not available yet"


def save_as_csv(self, save_file_name):
    if self.open_file_ext == "NetCDF Files (*.nc)":
        temp_file_name = tempfile.NamedTemporaryFile()
        save_as_netcdf(self, temp_file_name.name + ".nc")
        self.opened_file.convert_to_csv(save_file_name, temp_file = temp_file_name.name + ".nc")
        temp_file_name.close()
    if self.open_file_ext == "NASA Ames Files (*.na)":
        print "this function is not available yet"
    if self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
        print "this function is not available yet"
    