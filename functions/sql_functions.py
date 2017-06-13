# -*- coding: utf-8 -*-


def objects_initialization(self):
    self.modified = False
    self.open_file_name = ''
    self.open_file_ext = ''
    self.file_is_opened = False
    self.list_of_variables_and_attributes = {}
    self.list_of_new_variables_and_attributes = {}
    self.new_variables = False
    self.delete_first_variable = False
    self.compatibility_level = {
                                  1:["green", "icons/green_fire_icon.svg", "The file is fully compa"
                                     + "tible with the EUFAR netcdf convention.", False],
                                  2:["orange", "icons/orange_fire_icon.svg", "The file shows incomp"
                                     + "atibilities with the EUFAR netcdf convention. Please click "
                                     + "on the following button to have details.", True],
                                  3:["red", "icons/red_fire_icon.svg", "The file shows critical inc"
                                     + "ompatibilities with the EUFAR netcdf convention. Please cli"
                                     + "ck on the following button to have details.", True],
                                  4:["red", "icons/red_fire_icon.svg", "The file shows critical inc"
                                     + "ompatibilities with the EUFAR netcdf convention. EGADS is i"
                                     + "n 'compatibility' mode and few functions are disabled. Plea"
                                     + "se click on the following button to have details.", True]
                                  }
    
    self.required_eufar_global_attributes = [
                                              "Conventions",
                                              "title",
                                              "source",
                                              "institution",
                                              ]
    
    self.required_eufar_variable_attributes = [
                                               "units",
                                               "_FillValue"
                                               ]
    
    self.buttons_lines_dict = {
                        "gm_button_1":["gm_title_ln", None, None],
                        "gm_button_2":["gm_institution_ln", None, None],
                        "gm_button_3":["gm_source_ln", None, None],
                        "gm_button_4":["gm_project_ln", None, None],
                        "gm_button_5":["gm_history_ln", None, None],
                        "gm_button_6":["gm_history_ln_2", None, None],
                        "va_button_1":["va_varName_ln", self.listWidget, self.list_of_variables_and_attributes],
                        "va_button_2":["va_longName_ln", self.listWidget, self.list_of_variables_and_attributes],
                        "va_button_3":["va_category_ln", self.listWidget, self.list_of_variables_and_attributes],
                        "va_button_4":["va_units_ln", self.listWidget, self.list_of_variables_and_attributes],
                        "new_button_1":["new_varName_ln", self.new_listwidget, self.list_of_new_variables_and_attributes],
                        "new_button_2":["new_longName_ln", self.new_listwidget, self.list_of_new_variables_and_attributes],
                        "new_button_3":["new_category_ln", self.new_listwidget, self.list_of_new_variables_and_attributes],
                        "new_button_4":["new_units_ln", self.new_listwidget, self.list_of_new_variables_and_attributes]
                        }
    
    self.objects_metadata_dict = {
                        "gm_title_ln":"title",
                        "gm_institution_ln":"institution",
                        "gm_source_ln":"source",
                        "gm_project_ln":["project","ONAME"],
                        "gm_history_ln":["history","NCOM"],
                        "gm_history_ln_2":["","SCOM"],
                        "va_varName_ln":"var_name",
                        "va_longName_ln":"long_name",
                        "va_category_ln":"Category",
                        "va_units_ln":"units",
                        "new_varName_ln":"var_name",
                        "new_longName_ln":"long_name",
                        "new_category_ln":"Category",
                        "new_units_ln":"units"
                        }
    
    
    