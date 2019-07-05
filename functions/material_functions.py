import logging
import platform
import matplotlib


def objects_initialization(self):
    logging.debug('gui - material_functions.py - objects_initialization')
    self.modified = False
    self.opened_file = None
    self.file_name = ''
    self.file_ext = ''
    self.file_is_opened = False
    self.list_of_variables_and_attributes = {}
    self.list_of_new_variables_and_attributes = {}
    self.list_of_unread_variables = {}
    self.x_axis_variable_set = False
    self.x_axis_variable_name = None
    self.new_variables = False
    self.x_variable = None
    self.first_time_x_variable = True
    self.gui_update_url = None
    self.min_egads_version = '0.9.3'
    self.min_egads_branch = 'Lineage'
    self.buttons_lines_dict = {
                        "gm_button_1": ["gm_title_ln", None, None],
                        "gm_button_2": ["gm_institution_ln", None, None],
                        "gm_button_3": ["gm_source_ln", None, None],
                        "gm_button_4": ["gm_project_ln", None, None],
                        "gm_button_5": ["gm_history_ln", None, None],
                        "gm_button_6": ["gm_comments_ln", None, None],
                        "va_button_1": ["va_varName_ln", self.variable_list, self.list_of_variables_and_attributes],
                        "va_button_2": ["va_longName_ln", self.variable_list, self.list_of_variables_and_attributes],
                        "va_button_3": ["va_category_ln", self.variable_list, self.list_of_variables_and_attributes],
                        "va_button_4": ["va_units_ln", self.variable_list, self.list_of_variables_and_attributes],
                        "new_button_1": ["new_varName_ln", self.new_variable_list,
                                         self.list_of_new_variables_and_attributes],
                        "new_button_2": ["new_longName_ln", self.new_variable_list,
                                         self.list_of_new_variables_and_attributes],
                        "new_button_3": ["new_category_ln", self.new_variable_list,
                                         self.list_of_new_variables_and_attributes],
                        "new_button_4": ["new_units_ln", self.new_variable_list,
                                         self.list_of_new_variables_and_attributes]
                        }
    
    self.objects_metadata_dict = {
                        "gm_title_ln": ["title", "MNAME"],
                        "gm_institution_ln": ["institution", "ORG"],
                        "gm_source_ln": ["source", "SNAME"],
                        "gm_project_ln": ["project", "ONAME"],
                        "gm_history_ln": ["history", "NCOM"],
                        "gm_comments_ln": ["", "SCOM"],
                        "va_varName_ln": "var_name",
                        "va_longName_ln": "long_name",
                        "va_category_ln": "Category",
                        "va_units_ln": "units",
                        "new_varName_ln": "var_name",
                        "new_longName_ln": "long_name",
                        "new_category_ln": "Category",
                        "new_units_ln": "units"}


def setup_fonts():
    logging.debug('gui - material_functions.py - setup_fonts')
    if platform.system() == 'Linux':
        font_list = ([str(f.name) for f in matplotlib.font_manager.fontManager.ttflist] + 
                     [str(f.name) for f in matplotlib.font_manager.fontManager.afmlist])
    elif platform.system() == 'Windows':
        font_list = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in matplotlib.
                     font_manager.win32InstalledFonts()]
    else:
        raise Exception('The program couldnt determined which os is intalled')
    for index, item in enumerate(font_list):
        font_list[index] = str(item)
    default_font = matplotlib.font_manager.FontProperties(family=[str(matplotlib.rcParams['font.family'][
                                                                           0])]).get_name()
    if default_font not in font_list:
        font_list.append(default_font)
    font_list = sorted(set(font_list))
    return font_list, default_font


def setup_plot_material(self):
    logging.debug('gui - material_functions.py - setup_plot_material')
    self.plot_options = {}
    self.figure_options = {}
    self.line_styles = ["Dashed",
                        "Dash-dot",
                        "Dotted",
                        "Solid"]
    
    self.line_styles_dict = {"Dashed": "--",
                             "Dash-dot": "-.",
                             "Dotted": ":",
                             "Solid": "-"}
    self.line_styles_dict_inv = {v: k for k, v in self.line_styles_dict.items()}
    
    self.marker_styles = ["Circle",
                          "Diamond",
                          "Hegagon",
                          "Pentagon",
                          "Plus",
                          "Point",
                          "Square",
                          "Star",
                          "Triangle",
                          "X"]
    
    self.marker_styles_dict = {"Circle": "o",
                               "Diamond": "d",
                               "Hegagon": "h",
                               "Pentagon": "p",
                               "Plus": "+",
                               "Point": ".",
                               "Square": "s",
                               "Star": "*",
                               "Triangle": "^",
                               "X": "x"}
    self.marker_styles_dict_inv = {v: k for k, v in self.marker_styles_dict.items()}
    
    self.colors = ["HEX Color",
                   "RGB Color",
                   "Black",
                   "Blue",
                   "Cyan",
                   "Green",
                   "Magenta",
                   "Red",
                   "Yellow",
                   "White"]
    
    self.colors_grid = ["Black",
                        "Blue",
                        "Cyan",
                        "Green",
                        "Magenta",
                        "Red",
                        "Yellow",
                        "White"]
    
    self.colors_dict = {"Black": "k",
                        "Blue": "b",
                        "Cyan": "c",
                        "Green": "g",
                        "Magenta": "m",
                        "Red": "r",
                        "Yellow": "y",
                        "White": "w"}
    self.colors_dict_inv = {v: k for k, v in self.colors_dict.items()}
    
    self.image_extensions = {'EPS Files (*.eps)': '.eps',
                             'JPEG Files (*.jpg *.jpeg *.jpe)': '.jpg',
                             'PDF Files (*.pdf)': '.pdf',
                             'PNG Files (*.png *.pns)': '.png',
                             'TIFF Files (*.tif *.tiff)': '.tif'}

    self.pw_figureOptions_vl_1 = []
    self.pw_figureOptions_vl_2 = []
    self.pw_figureOptions_gl_1 = []
    self.pw_figureOptions_gl_2 = []
    self.pw_figureOptions_gl_3 = []
    self.pw_figureOptions_gl_4 = []
    self.pw_figureOptions_hl_1 = []
    self.pw_figureOptions_hl_2 = []
    self.pw_figureOptions_hl_3 = []
    self.pw_figureOptions_hl_4 = []
    self.pw_figureOptions_hl_5 = []
    self.pw_figureOptions_hl_12 = []
    self.pw_figureOptions_lb_1 = []
    self.pw_figureOptions_lb_2 = []
    self.pw_figureOptions_lb_3 = []
    self.pw_figureOptions_lb_4 = []
    self.pw_figureOptions_lb_5 = []
    self.pw_figureOptions_lb_6 = []
    self.pw_figureOptions_lb_7 = []
    self.pw_figureOptions_lb_8 = []
    self.pw_figureOptions_lb_9 = []
    self.pw_figureOptions_lb_10 = []
    self.pw_figureOptions_lb_11 = []
    self.pw_figureOptions_lb_12 = []
    self.pw_figureOptions_lb_13 = []
    self.pw_figureOptions_lb_14 = []
    self.pw_figureOptions_lb_15 = []
    self.pw_figureOptions_lb_16 = []
    self.pw_figureOptions_lb_17 = []
    self.pw_figureOptions_lb_18 = []
    self.pw_figureOptions_lb_19 = []
    self.pw_figureOptions_lb_20 = []
    self.pw_figureOptions_lb_21 = []
    self.pw_figureOptions_lb_22 = []
    self.pw_figureOptions_lb_23 = []
    self.pw_figureOptions_lb_24 = []
    self.pw_figureOptions_lb_25 = []
    self.pw_figureOptions_lb_26 = []
    self.pw_figureOptions_lb_27 = []
    self.pw_figureOptions_lb_28 = []
    self.pw_figureOptions_lb_29 = []
    self.pw_figureOptions_lb_30 = []
    self.pw_figureOptions_ln_1 = []
    self.pw_figureOptions_ln_2 = []
    self.pw_figureOptions_ln_3 = []
    self.pw_figureOptions_ln_4 = []
    self.pw_figureOptions_ln_5 = []
    self.pw_figureOptions_ln_6 = []
    self.pw_figureOptions_ln_7 = []
    self.pw_figureOptions_ln_8 = []
    self.pw_figureOptions_ln_9 = []
    self.pw_figureOptions_ln_10 = []
    self.pw_figureOptions_cb_1 = []
    self.pw_figureOptions_cb_2 = []
    self.pw_figureOptions_cb_3 = []
    self.pw_figureOptions_cb_4 = []
    self.pw_figureOptions_cb_5 = []
    self.pw_figureOptions_cb_6 = []
    self.pw_figureOptions_cb_7 = []
    self.pw_figureOptions_cb_8 = []
    self.pw_figureOptions_cb_9 = []
    self.pw_figureOptions_cb_10 = []
    self.pw_figureOptions_bt_1 = []
    self.pw_figureOptions_bt_2 = []
    self.pw_figureOptions_bt_3 = []
    self.pw_figureOptions_bt_4 = []
    self.pw_figureOptions_bt_5 = []
    self.pw_figureOptions_bt_6 = []
    self.pw_figureOptions_bt_7 = []
    self.pw_figureOptions_bt_8 = []
    self.pw_figureOptions_bt_9 = []
    self.pw_figureOptions_ck_1 = []
    self.pw_figureOptions_ck_2 = []
    self.pw_figureOptions_li_1 = []
    self.pw_figureOptions_sl_1 = []
    self.pw_figureOptions_sl_2 = []
    self.pw_figureOptions_sl_3 = []
    self.pw_figureOptions_sl_4 = []
    self.pw_figureOptions_sl_5 = []
    self.figure_option_num = 0
    self.pw_plotOptions_vl_1 = []
    self.pw_plotOptions_hl_1 = []
    self.pw_plotOptions_hl_2 = []
    self.pw_plotOptions_hl_3 = []
    self.pw_plotOptions_hl_4 = []
    self.pw_plotOptions_hl_5 = []
    self.pw_plotOptions_hl_6 = []
    self.pw_plotOptions_hl_7 = []
    self.pw_plotOptions_hl_8 = []
    self.pw_plotOptions_hl_9 = []
    self.pw_plotOptions_lb_1 = []
    self.pw_plotOptions_lb_2 = []
    self.pw_plotOptions_lb_3 = []
    self.pw_plotOptions_lb_4 = []
    self.pw_plotOptions_lb_5 = []
    self.pw_plotOptions_lb_6 = []
    self.pw_plotOptions_lb_7 = []
    self.pw_plotOptions_lb_8 = []
    self.pw_plotOptions_lb_9 = []
    self.pw_plotOptions_bg_1 = []
    self.pw_plotOptions_rb_1 = []
    self.pw_plotOptions_rb_2 = []
    self.pw_plotOptions_cb_1 = []
    self.pw_plotOptions_cb_2 = []
    self.pw_plotOptions_ln_1 = []
    self.pw_plotOptions_ln_2 = []
    self.pw_plotOptions_ln_3 = []
    self.pw_plotOptions_ln_4 = []
    self.pw_plotOptions_ln_5 = []
    self.pw_plotOptions_ln_6 = []
    self.pw_plotOptions_ck_1 = []
    self.pw_plotOptions_ck_2 = []
    self.pw_plotOptions_bt_1 = []
    self.pw_plotOptions_bt_2 = []
    self.pw_plotOptions_bt_3 = []
    self.pw_plotOptions_bt_4 = []
    self.pw_plotOptions_bt_5 = []
    self.pw_plotOptions_bt_6 = []
    self.pw_plotOptions_li_1 = []
    self.plot_option_num = 0


def add_global_attributes_to_buttons(self):
    logging.debug('gui - material_functions.py - add_global_attributes_to_buttons')
    self.buttons_lines_dict['gm_button_1'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_2'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_3'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_4'][2] = self.list_of_global_attributes
    self.buttons_lines_dict['gm_button_5'][2] = self.list_of_global_attributes
