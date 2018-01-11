# -*- coding: utf-8 -*-

import egads
import tempfile
import collections
import os
import copy
import logging
import datetime


def save_netcdf(self):
    logging.debug('gui - saving_functions.py - save_netcdf')
    list_of_global_attributes = self.opened_file.get_attribute_list()
    for key, value in self.list_of_global_attributes.iteritems():   
        try:
            if list_of_global_attributes[key] != value:
                if value == 'deleted':
                    self.opened_file.delete_attribute(key)
                else:
                    self.opened_file.add_attribute(key, value)
        except KeyError:
            if value != 'deleted':
                self.opened_file.add_attribute(key, value)
    del list_of_global_attributes
    list_of_variables = self.opened_file.get_variable_list()
    list_of_variables_and_attributes = copy.deepcopy(self.list_of_variables_and_attributes)
    for var_name in list_of_variables:
        try:
            var = list_of_variables_and_attributes[var_name]
            if var[1] != 'deleted':
                list_of_attributes = self.opened_file.get_attribute_list(var_name)
                for key, value in var[1].iteritems():
                    if key != 'var_name' and key != '_FillValue':
                        try:
                            if list_of_attributes[key] != value:
                                if value == 'deleted':
                                    self.opened_file.delete_attribute(key, var_name)
                                else:
                                    self.opened_file.add_attribute(key, value, var_name)
                        except KeyError:
                            if value != 'deleted':
                                self.opened_file.add_attribute(key, value, var_name)
                if var[1]['var_name'] != var_name:
                    self.opened_file.change_variable_name(var_name, var[1]['var_name'])
            list_of_variables_and_attributes.pop(var_name)
        except KeyError:
            pass
    if len(list_of_variables_and_attributes) > 0:
        for key, sublist in sorted(list_of_variables_and_attributes.iteritems()):
            if sublist[1] != "deleted" and key != 'time':
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
                self.opened_file.write_variable(data, sublist[0], (dimensions_tuple), 'double', fillvalue)    
                for key, value in sublist[1].iteritems():
                    if isinstance(value, list):
                        tmp = ""
                        for item in value:
                            tmp += item + ", "
                        tmp = tmp[:-2]
                        self.opened_file.add_attribute(str(key), str(tmp), str(sublist[0]))
                    else:
                        if str(key) != "var_name" and str(key) != "_FillValue" and value != "deleted":
                            try:
                                self.opened_file.add_attribute(str(key), float(value), str(sublist[0]))
                            except ValueError:
                                self.opened_file.add_attribute(str(key), str(value), str(sublist[0]))
                if sublist[0] != sublist[1]["var_name"]:
                    self.opened_file.change_variable_name(str(sublist[0]), str(sublist[1]["var_name"]))
            else:
                pass


def save_as_netcdf(self, save_file_name):
    logging.debug('gui - saving_functions.py - save_as_netcdf : save_file_name ' + str(save_file_name)
                  + ', open_file_ext ' + str(self.open_file_ext))
    if self.open_file_ext == "NetCDF Files (*.nc)":
        self.newFile = egads.input.NetCdf(save_file_name, 'w')
        for key, value in self.list_of_dimensions.iteritems():
            self.newFile.add_dim(key, value)
        for key, value in self.list_of_global_attributes.iteritems():
            if value != "deleted":
                try:
                    self.newFile.add_attribute(key, float(value))
                except ValueError:
                    self.newFile.add_attribute(key, str(value))
        try:
            sublist = self.list_of_variables_and_attributes['time']
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
        except KeyError:
            logging.exception('gui - saving_functions.py - save_as_netcdf : an exception occured')       
        for key, sublist in sorted(self.list_of_variables_and_attributes.iteritems()):
            if sublist[1] != "deleted" and key != 'time':
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
    if self.open_file_ext == "NASA Ames Files (*.na)":
        self.opened_file.convert_to_netcdf(save_file_name)
    if self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
        print "this function is not available yet"


def save_nasaames(self):
    logging.debug('gui - saving_functions.py - save_nasaames')
    save_as_nasaames(self, self.open_file_name)
    
    
def save_as_nasaames(self, save_file_name):
    logging.debug('gui - saving_functions.py - save_as_nasaaimes : save_file_name ' + str(save_file_name)
                  + ', open_file_ext ' + str(self.open_file_ext))
    if self.open_file_ext == "NetCDF Files (*.nc)":
        temp_file_name = tempfile.NamedTemporaryFile()
        tmp_name = str(temp_file_name.name) + '.nc'
        save_as_netcdf(self, tmp_name)
        f = egads.input.EgadsNetCdf(tmp_name, 'r')
        f.convert_to_nasa_ames(save_file_name)
        f.close()
        os.remove(tmp_name)
    if self.open_file_ext == "NASA Ames Files (*.na)":
        list_of_variables = []
        for key, _ in self.list_of_variables_and_attributes.iteritems():
            list_of_variables.append(key)
        list_of_variables = sorted(list_of_variables)
        f = egads.input.NasaAmes()
        na_dict = f.create_na_dict()
        f.write_attribute_value('ONAME', self.list_of_global_attributes['ONAME'], na_dict = na_dict)
        f.write_attribute_value('ORG', self.list_of_global_attributes['ORG'], na_dict = na_dict)
        f.write_attribute_value('SNAME', self.list_of_global_attributes['SNAME'], na_dict = na_dict)
        f.write_attribute_value('MNAME', self.list_of_global_attributes['MNAME'], na_dict = na_dict)
        f.write_attribute_value('DATE', self.list_of_global_attributes['DATE'], na_dict = na_dict)
        f.write_attribute_value('NIV', 1, na_dict = na_dict)
        f.write_attribute_value('NSCOML', len(self.list_of_global_attributes['SCOM']), na_dict = na_dict)
        f.write_attribute_value('NNCOML', len(self.list_of_global_attributes['NCOM']), na_dict = na_dict)
        f.write_attribute_value('SCOM', self.list_of_global_attributes['SCOM'], na_dict = na_dict)
        f.write_attribute_value('NCOM', self.list_of_global_attributes['NCOM'], na_dict = na_dict)
        for name in list_of_variables:
            var = self.list_of_variables_and_attributes[name]
            if name == 'time':
                f.write_variable(var[3], vartype="independant", na_dict = na_dict)
            else:
                f.write_variable(var[3], vartype="main", na_dict = na_dict)
        f.save_na_file(save_file_name, na_dict, '%f')
        f.close()
    if self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
        print "this function is not available yet"


def save_as_csv(self, save_file_name):
    logging.debug('gui - saving_functions.py - save_as_csv : save_file_name ' + str(save_file_name)
                  + ', open_file_ext ' + str(self.open_file_ext))
    if self.open_file_ext == "NetCDF Files (*.nc)":
        temp_file_name = tempfile.NamedTemporaryFile()
        save_as_netcdf(self, temp_file_name.name + ".nc")
        self.opened_file.convert_to_csv(save_file_name, temp_file = temp_file_name.name + ".nc")
        temp_file_name.close()
    if self.open_file_ext == "NASA Ames Files (*.na)":
        print "this function is not available yet"
    if self.open_file_ext == "CSV Files (*.csv *.dat *.txt)":
        print "this function is not available yet"


    