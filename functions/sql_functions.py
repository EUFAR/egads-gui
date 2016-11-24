# -*- coding: utf-8 -*-


def objectsInit(self):
    self.modified = False
    self.file_is_opened = False
    self.list_of_new_variables_and_attributes = []
    self.new_variables = False
    
    self.compatibility_level = [
                                [1, "green", "icons/green_fire_icon.png", "The file is fully compatible with the EUFAR netcdf conven"
                                + "tion.", 400, "icons/none_icon.png", False],
                                [2, "orange", "icons/orange_fire_icon.png", "The file shows incompatibilities with the EUFAR netcdf "
                                + "convention. Please click on the following button to have details.", 750, "icons/info_icon.png", True],
                                [3, "red", "icons/red_fire_icon.png", "The file shows critical incompatibilities with the EUFAR netcdf "
                                 + "convention. Please click on the following button to have details.", 750, "icons/info_icon.png", True],
                                [4, "red", "icons/red_fire_icon.png", "The file shows critical incompatibilities with the EUFAR netcdf "
                                 + "convention. EGADS is in 'compatibility' mode and few functions are disabled. Please click on the "
                                 + "following button to have details.", 750, "icons/info_icon.png", True]
                                ]
    
    
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
                        "gm_button_1":"gm_title_ln",
                        "gm_button_2":"gm_institution_ln",
                        "gm_button_3":"gm_source_ln",
                        "gm_button_4":"gm_project_ln",
                        "gm_button_5":"gm_history_ln",
                        "va_button_1":"va_varName_ln",
                        "va_button_2":"va_longName_ln",
                        "va_button_3":"va_category_ln",
                        "va_button_4":"va_units_ln",
                        "new_button_1":"new_varName_ln",
                        "new_button_2":"new_longName_ln",
                        "new_button_3":"new_category_ln",
                        "new_button_4":"new_units_ln"
                        }
        
    self.objects_metadata_dict = {
                        "gm_title_ln":"title",
                        "gm_institution_ln":"institution",
                        "gm_source_ln":"source",
                        "gm_project_ln":"project",
                        "gm_history_ln":"history",
                        "va_varName_ln":"var_name",
                        "va_longName_ln":"long_name",
                        "va_category_ln":"Category",
                        "va_units_ln":"units",
                        "new_varName_ln":"var_name",
                        "new_longName_ln":"long_name",
                        "new_category_ln":"Category",
                        "new_units_ln":"units"
                        }
    
    
    
    
    
    
    
    