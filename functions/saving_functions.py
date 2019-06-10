import egads
import logging
import datetime
import dateutil
from functions.other_windows_functions import MyInfo


def save_as_netcdf_for_na(self, save_file_name):
    logging.debug('gui - saving_functions.py - save_as_netcdf_for_na : save_file_name ' + save_file_name)
    format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                   'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
    title = self.list_of_global_attributes['MNAME']
    source = self.list_of_global_attributes['SNAME']
    institution = self.list_of_global_attributes['ORG']
    authors = self.list_of_global_attributes['ONAME']
    history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
               + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
               + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
               + ' - NetCDF file created using EGADS and its GUI.')
    rev_date = (str(self.list_of_global_attributes['RDATE'][0]) + '-' + str(self.list_of_global_attributes['RDATE'][1])
                + '-' + str(self.list_of_global_attributes['RDATE'][2]))
    scom = ''
    ncom = ''
    if isinstance(self.list_of_global_attributes['SCOM'], list):
        for i in self.list_of_global_attributes['SCOM']:
            scom += i + '\n'
        scom = scom[:-1]
    else:
        scom = self.list_of_global_attributes['SCOM']
        if scom[-1:] == '\n':
            scom = scom[:-1]
    if isinstance(self.list_of_global_attributes['NCOM'], list):
        for i in self.list_of_global_attributes['NCOM']:
            ncom += i + '\n'
        ncom = ncom[:-1]
    else:
        ncom = self.list_of_global_attributes['NCOM']
        if ncom[-1:] == '\n':
            ncom = ncom[:-1]
    new_file = egads.input.EgadsNetCdf(save_file_name, 'w')
    new_file.add_attribute('Conventions', 'CF-1.0')
    new_file.add_attribute('title', title)
    new_file.add_attribute('source', source)
    new_file.add_attribute('special_comments', scom)
    new_file.add_attribute('normal_comments', ncom)
    new_file.add_attribute('institution', institution)
    new_file.add_attribute('authors', authors)
    new_file.add_attribute('history', history)
    new_file.add_attribute('data_date_of_revision', rev_date)
    for key, value in self.list_of_dimensions.items():
        new_file.add_dim(key, value)
    for var_name, var in self.list_of_variables_and_attributes.items():
        dimensions_tuple = tuple(var[1].keys())
        try:
            var_format = format_dict[str(var[0].value.dtype)]
        except KeyError:
            var_format = 'double'
        new_file.write_variable(var[0], var_name, dimensions_tuple, var_format)
    new_file.close()


def save_as_netcdf_for_nc(self, save_file_name):
    logging.debug('gui - saving_functions.py - save_as_netcdf_for_nc : save_file_name ' + save_file_name)
    format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                   'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
    new_file = egads.input.EgadsNetCdf(save_file_name, 'w')
    for key, value in self.list_of_dimensions.items():
        new_file.add_dim(key, value)
    conventions_bool, history_bool = False, False
    for key, value in self.list_of_global_attributes.items():
        if 'Conventions' in key:
            conventions_bool = True
        if 'history' in key:
            history_bool = True
        try:
            new_file.add_attribute(key, float(value))
        except ValueError:
            new_file.add_attribute(key, str(value))

    if not conventions_bool:
        new_file.add_attribute('Conventions', 'CF-1.0')
    if not history_bool:
        history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
                   + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
                   + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
                   + ' - File created by EGADS and its GUI.')
        new_file.add_attribute('history', history)
    for var_name, var_sublist in self.list_of_variables_and_attributes.items():
        data = var_sublist[0]
        dimensions_tuple = []
        for key, value in var_sublist[1].items():
            dimensions_tuple.append(key)
        dimensions_tuple = tuple(dimensions_tuple)
        try:
            var_format = format_dict[str(data.value.dtype)]
        except KeyError:
            var_format = 'double'
        new_file.write_variable(data, var_name, dimensions_tuple, var_format)
    new_file.close()

    
def save_as_nasaames_for_na(self, save_file_name):
    logging.debug('gui - saving_functions.py - save_as_nasaames_for_na : save_file_name ' + str(save_file_name))
    new_file = egads.input.NasaAmes()
    na_dict = new_file.create_na_dict()
    new_file.write_attribute_value('ONAME', self.list_of_global_attributes['ONAME'], na_dict=na_dict)
    new_file.write_attribute_value('ORG', self.list_of_global_attributes['ORG'], na_dict=na_dict)
    new_file.write_attribute_value('SNAME', self.list_of_global_attributes['SNAME'], na_dict=na_dict)
    new_file.write_attribute_value('MNAME', self.list_of_global_attributes['MNAME'], na_dict=na_dict)
    new_file.write_attribute_value('DATE', self.list_of_global_attributes['DATE'], na_dict=na_dict)
    new_file.write_attribute_value('NIV', 1, na_dict=na_dict)
    new_file.write_attribute_value('NSCOML', len(self.list_of_global_attributes['SCOM']), na_dict=na_dict)
    new_file.write_attribute_value('NNCOML', len(self.list_of_global_attributes['NCOM']), na_dict=na_dict)
    new_file.write_attribute_value('SCOM', self.list_of_global_attributes['SCOM'], na_dict=na_dict)
    new_file.write_attribute_value('NCOM', self.list_of_global_attributes['NCOM'], na_dict=na_dict)
    for name in sorted(self.list_of_variables_and_attributes.keys()):
        var = self.list_of_variables_and_attributes[name]
        if name in self.list_of_dimensions:
            new_file.write_variable(var[0], vartype="independant", na_dict=na_dict)
        else:
            new_file.write_variable(var[0], vartype="main", na_dict=na_dict)
    new_file.save_na_file(save_file_name, na_dict)
    new_file.close()


def save_as_nasaames_for_nc(self, save_file_name):
    logging.debug('gui - saving_functions.py - save_as_nasaames_for_na : save_file_name ' + str(save_file_name))
    if len(self.list_of_dimensions) > 1:
        info_text = ('The actual NASA Ames file class can only handle FFI equal to 1001. Thus it is not possible at '
                     + 'this time to save file with more than one dimension.')
        self.infoWindow = MyInfo(info_text)
        self.infoWindow.exec_()
    else:
        new_file = egads.input.NasaAmes()
        na_dict = new_file.create_na_dict()
        nlhead, ffi, org, oname, sname, mname, dx = -999, 1001, '', '', '', '', 0.0
        ivol, nvol = 1, 1
        try:
            org = self.list_of_global_attributes['institution']
        except KeyError:
            org = 'no institution'
        try:
            oname = self.list_of_global_attributes['authors']
        except KeyError:
            try:
                oname = self.list_of_global_attributes['institution']
            except KeyError:
                oname = 'no author'
        try:
            sname = self.list_of_global_attributes['source']
        except KeyError:
            sname = 'no source'
        try:
            mname = self.list_of_global_attributes['title']
        except KeyError:
            mname = 'no title'
        rdate = [datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day]
        date = None
        niv = 0
        for ivar in self.list_of_dimensions:
            data = self.list_of_variables_and_attributes[ivar][0]
            new_file.write_variable(data, ivar, vartype='independant', na_dict=na_dict)
            niv += 1
            if 'time' in ivar:
                units = data.metadata['units']
                ref_time = None
                try:
                    index = units.index(' since ')
                    ref_time = units[index + 7:]
                except (KeyError, ValueError):
                    pass
                try:
                    ref_time = dateutil.parser.parse(ref_time).strftime("%Y%m%dT%H%M%S")
                    isotime = egads.algorithms.transforms.SecondsToIsotime().run(data, ref_time)
                    y, m, d, _, _, _ = egads.algorithms.transforms.IsotimeToElements().run(isotime)
                    date = [y.value[0], m.value[0], d.value[0]]
                    if not date:
                        date = [999, 999, 999]
                except Exception:
                    date = [999, 999, 999]
        new_file.write_attribute_value('NLHEAD', nlhead, na_dict=na_dict)
        new_file.write_attribute_value('FFI', ffi, na_dict=na_dict)
        new_file.write_attribute_value('ONAME', oname, na_dict=na_dict)
        new_file.write_attribute_value('ONAME', oname, na_dict=na_dict)
        new_file.write_attribute_value('ORG', org, na_dict=na_dict)
        new_file.write_attribute_value('SNAME', sname, na_dict=na_dict)
        new_file.write_attribute_value('MNAME', mname, na_dict=na_dict)
        new_file.write_attribute_value('DATE', date, na_dict=na_dict)
        new_file.write_attribute_value('RDATE', rdate, na_dict=na_dict)
        new_file.write_attribute_value('NIV', niv, na_dict=na_dict)
        new_file.write_attribute_value('DX', dx, na_dict=na_dict)
        name_string = ''
        ncom = ['==== Normal Comments follow ====']
        for attr in self.list_of_global_attributes:
            if attr != 'institution' and attr != 'authors' and attr != 'source' and attr != 'title':
                ncom.append(attr + ': ' + str(self.list_of_global_attributes[attr]))
        ncom.append('==== Normal Comments end ====')
        ncom.append('=== Data Section begins on the next line ===')
        for name in self.list_of_dimensions:
            name_string += name + '    '
        scom = ['==== Special Comments follow ====',
                '=== Additional Variable Attributes defined in the source file ===',
                '== Variable attributes from source (NetCDF) file follow ==']
        for var, sublist in self.list_of_variables_and_attributes.items():
            if var not in self.list_of_dimensions:
                new_file.write_variable(sublist[0], var, na_dict=na_dict)
                first_line = True
                for metadata in sublist[0].metadata:
                    if metadata != '_FillValue' and metadata != 'scale_factor' and metadata != 'units' and metadata \
                            != 'var_name':
                        if first_line:
                            first_line = False
                            scom.append('  Variable ' + var + ':')
                        scom.append('    ' + metadata + ' = ' + str(sublist[0].metadata[metadata]))
                name_string += var + '    '
        name_string = name_string[:-4]
        ncom.append(name_string)
        scom.append('== Variable attributes from source (NetCDF) file end ==')
        scom.append('==== Special Comments end ====')
        new_file.write_attribute_value('NVOL', nvol, na_dict=na_dict)
        new_file.write_attribute_value('IVOL', ivol, na_dict=na_dict)
        new_file.write_attribute_value('SCOM', scom, na_dict=na_dict)
        new_file.write_attribute_value('NCOM', ncom, na_dict=na_dict)
        new_file.write_attribute_value('NSCOML', len(scom), na_dict=na_dict)
        new_file.write_attribute_value('NNCOML', len(ncom), na_dict=na_dict)
        new_file.save_na_file(save_file_name, na_dict)
