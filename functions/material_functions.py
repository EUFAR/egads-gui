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


def plot_information_buttons_text(self):
    logging.debug('gui - material_functions.py - plot_information_buttons_text')
    self.save_buttons_text = {'pw_info_bt_1': 'Control the size of the figure when it is saved, if the user wants a '
                                              'size different than the one of the window.',
                              'pw_info_bt_2': 'The resolution of the figure in dot per inch (dpi). Numbers up to 600 '
                                              'are accepted.',
                              'pw_info_bt_3': 'Use this checkbox to activate or deactivate the transparency of the '
                                              'background. 100 is the best possible quality, 1 is the worst.',
                              'pw_info_bt_4': 'This slider controls the quality of the picture if the JPEG format is '
                                              'selected when the picture is saved.'}

    self.figure_buttons_text = {'pw_figureOptions_bt_1': 'It is possible to customize the figure and axis titles, '
                                                         'their fonts and the size of their fonts.',
                                'pw_figureOptions_bt_2': 'Ticks are controled from here. Please note that the numbers '
                                                         'won\'t change if the user uses the pan and zoom functions.',
                                'pw_figureOptions_bt_6': 'A grid can be display and customized from here.',
                                'pw_figureOptions_bt_7': 'The legeng can move freely on the figure, this option '
                                                         'allows the user to set it visible or not.',
                                'pw_commonOptions_bt_1': 'Figure margins are set by moving the sliders. The greater '
                                                         'the number, the greater the margins. If multiple figures '
                                                         'are displayed, the last sliders control the distance '
                                                         'between those figures.',
                                'pw_plotOptions_bt_1': 'The line style is controled from here. The selection of the '
                                                       'style impacts the way the line is customized below.',
                                'pw_plotOptions_bt_2': 'The color of the line can be changed to a predefined color, '
                                                       'or a color defined by an RGB/HEX code.',
                                'pw_plotOptions_bt_3': 'This is the size of the line/marker.',
                                'pw_plotOptions_bt_4': 'This checkbox activates or deactivates the antialiasing '
                                                       'function',
                                'pw_plotOptions_bt_5': 'This checkbox activates or deactivates the opacity and the '
                                                       'value of opacity.',
                                'pw_plotOptions_bt_6': 'The name of the time series can be changed here.'}


def algorithm_information_buttons_text(self):
    logging.debug('gui - material_functions.py - algorithm_information_buttons_text')
    self.information_buttons_text = {'cw_info_3': 'The name of the algorithm as implemented in EGADS. To aid in '
                                                  'algorithm usage and discovery, there is a general naming scheme '
                                                  'for egads algorithms. Generally, algorithm names are composed as '
                                                  'follows: {Measurement}{Context/Detail/Instrument}{'
                                                  'Source}<br><br><u>Ex</u>: AltitudePressureRaf',
                                     'cw_info_4': 'The person who developed the algorithm.<br><br><u>Ex</u>: John '
                                                  'Doe',
                                     'cw_info_5': 'The person, institution or entity who provided the algorithm.'
                                                  '<br><br><u>Ex</u>: NCAR - Earth Observing Laboratory',
                                     'cw_info_6': 'Any references to literature, journals or documents with more '
                                                  'information on the current algorithm.<br><br><u>Ex</u>: A.C. van '
                                                  'der Kroonenberg et al, "Measuring the wind vector using the '
                                                  'autonomous mini aerial vehicle M^2AV", J. Atmos. Oceanic Technol., '
                                                  '25 (2008), pp. 1969-1982.',
                                     'cw_info_7': 'The purpose of the algorithm.<br><br><u>Ex</u>: The '
                                                  'algorithm calculates static pressure',
                                     'cw_info_8': 'A short description of what the algorithm does. <br><br><u>Ex</u>: '
                                                  'It calculates static pressure and dynamic pressure by correction of '
                                                  'static error. Angle of attack and sideslip are calculated from the'
                                                  ' horizontal and vertical differential pressures.',
                                     'cw_info_9': 'General category of algorithm. The algorithm will be saved into '
                                                  'a folder with the name of the category.<br><br><u>Ex</u>: '
                                                  'Thermodynamics',
                                     'cw_info_10': 'The algorithm itself. It has to be coded using Python 3. It is '
                                                   'still possible to import modules like numpy. Input and output '
                                                   'variables should be well defined, and the last line of the '
                                                   'algorithm has to return the output variable('
                                                   's).<br><br><u>Ex</u>:<br>&nbsp;&nbsp;&nbsp;&nbsp;a, b = 2, -6'
                                                   '<br>&nbsp;&nbsp;&nbsp;&nbsp;output_var = a * input_var + '
                                                   'b<br><br>&nbsp;&nbsp;&nbsp;&nbsp;return output_var',
                                     'cw_info_1': 'The purpose of this tab is to create input variable(s) used in the '
                                                  'previous algorithm field. Each variable required by the algorithm '
                                                  'should be created here.',
                                     'cw_info_2': 'The purpose of this tab is to create output variable(s) used in the '
                                                  'previous algorithm field. Each variable returned by the algorithm '
                                                  'should be created here.'}

    self.input_output_button_text = {'cw_info_bt_1': 'This is the input symbol. It has to correspond to the input '
                                                     'symbol used in the previous algorithm field.<br><br><u>Ex</u>: '
                                                     's_p',
                                     'cw_info_bt_2': 'This is the unit of the input. There are 3 different ways to '
                                                     'write the unit:<ol><li>by using text, ex: <b>m.s-1</b>, '
                                                     'to inform EGADS that the unit of the input has to be '
                                                     '<b>m.s-1</b></li><li>by using <b>None</b>, to inform EGADS that '
                                                     'the input doesn\'t need a particular unit</li><li>by using a '
                                                     'space, " ", to inform EGADS that the input has to be '
                                                     'dimensionless.',
                                     'cw_info_bt_3': 'This is the type of the input. The type can be an array ('
                                                     'written <b>array</b>), a vector (written <b>vector</b>), '
                                                     'or a coefficient (written <b>coeff</b>). If the input is '
                                                     'optional, <b>_optional</b> should be added to the type.'
                                                     '<br><br><u>Ex</u>: array or coeff_optional',
                                     'cw_info_bt_4': 'A short description of the input.<br><br><u>Ex</u>: Particle '
                                                     'counts in each bin over time',
                                     'cw_info_bt_5': 'This is the output symbol. It has to correspond to the output '
                                                     'symbol used in the previous algorithm field. '
                                                     'It has to be return by the algorithm<br><br><u>Ex</u>: '
                                                     'return out_altitude',
                                     'cw_info_bt_6': 'This is the unit of the output. There are 2 different ways to '
                                                     'write the unit:<ol><li>by using text, ex: <b>m.s-1</b>, '
                                                     'to inform EGADS that the unit of the output has to be '
                                                     '<b>m.s-1</b></li><li>by using <b>input<i>n</i></b> to inform '
                                                     'EGADS that this output has to use the unit of the input <i>n</i>',
                                     'cw_info_bt_7': 'This is the type of the input. The type can be an array ('
                                                     'written <b>array</b>), a vector (written <b>vector</b>), '
                                                     'or a coefficient (written <b>coeff</b>).<br><br><u>Ex</u>: '
                                                     'array',
                                     'cw_info_bt_8': 'This is the standard name of the output. There are 2 different '
                                                     'ways to write the standard name:<ol><li>by using text, '
                                                     'ex: pressure altitude </li><li>by using <b>input<i>n</i></b> '
                                                     'with or without more text, this way egads knows that it has to '
                                                     'take the standard name of the input <i>n</i>, ex: input0 '
                                                     'corrected for something',
                                     'cw_info_bt_9': 'This is the long name of the output. There are 2 different '
                                                     'ways to write the long name:<ol><li>by using text, '
                                                     'ex: pressure altitude computed from static pressure</li><li>by '
                                                     'using <b>input<i>n</i></b> with or without more text, '
                                                     'this way egads knows that it has to take the long name of the '
                                                     'input <i>n</i>, ex: input0 corrected for something',
                                     'cw_info_bt_10': 'A short description of the output.<br><br><u>Ex</u>: Mean '
                                                      'diameter of the particles',
                                     'cw_info_bt_11': 'Each output has to be linked to one or more categories.'}
