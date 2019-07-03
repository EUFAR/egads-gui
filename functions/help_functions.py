import logging


def option_information_text():
    logging.debug('gui - help_functions.py - option_information_text')
    info_dict = {'info_button_4': 'The user can change the verbose level of the logging system. '
                                  'If an issue is noticed, it is a good idea to change the level '
                                  'to DEBUG and send the log file to the developer.',
                 'info_button_5': 'The path and folder where to save the log file for the GUI, '
                                  'modifying this option assumes to restart the GUI',
                 'info_button_10': 'This option allows the GUI to check for an update online at '
                                  'startup automatically. The user has the possibility to check '
                                  'manually by clicking on the left button.',
                 'info_button_1': 'It is possible in EGADS to read the values of a variable '
                                  'stored in a NASA Ames/NetCDF file as floats. Selecting this '
                                  'option will ask EGADS to do so. Please read the documentation '
                                  'of EGADS to have more details.',
                 'info_button_2': 'By checking this option, EGADS will automatically replace '
                                  'missing values in data by Numpy NaN.',
                 'info_button_3': 'Numpy NaN is for float array only, thus it is not possible to '
                                  'replace missing values in variables composed of integer '
                                  'values. By checking this option, the user allows EGADS to '
                                  'switch back to the default option if the read of a variable '
                                  'fails in this particular situation.',
                 'info_button_6': 'The user can change the verbose level of the logging system. '
                                  'If an issue is noticed, it is a good idea to change the level '
                                  'to DEBUG and send the log file to the developer.',
                 'info_button_7': 'The path and folder where to save the log file for EGADS, '
                                  'modifying this option assumes to restart the GUI',
                 'info_button_11': 'This option allows the GUI to check EGADS update online at '
                                  'startup automatically. The user has the possibility to check '
                                  'manually by clicking on the left button.',
                 'info_button_8': 'When a user select more than one variables to plot them, '
                                   'based on this option, the GUI can ask him what to do, '
                                   'plot them on the same figure, or plot them on different '
                                   'subplots.',
                 'info_button_9': 'Based on this option, if multiple subplots are required, '
                                   'the GUI can organize the subplots automatically or let the '
                                   'user handle the layout himself.'}
    return info_dict


def export_information_text():
    logging.debug('gui - help_functions.py - export_information_text')
    info_dict = {'info_button_1': 'The GUI gives to the user the possibility to export data into few external '
                                  'formats. At this time, it is possible to export data along a path ('
                                  'georeferenced time series generally) to Google Earth KML/KMZ file format. Please '
                                  'read the documentation for more details.',
                 'info_button_2': 'Data in Google Earth are georeferenced. Thus it is mandatory to provide longitude, '
                                  'latitude and (if possible) altitude to create a path. All data have to be vectors '
                                  'with the same amount of samples.',
                 'info_button_3': 'Choose here one or more variables to be displayed in Google Earth. The chosen '
                                  'variables are not strictly drawn and displayed. Only the path is displayed with '
                                  'a colormap and units for each variable.<br><br>Important note : at this time, '
                                  'only one variable is handled by the export function, due to the size of the output '
                                  'file. It will change in the next version.',
                 'info_button_4': 'The width of the path in pixel. Minimum is 1 px and maximum is 20 px.',
                 'info_button_5': 'By default, only a path is rendered. If checked, and if the path is not stuck to '
                                  'the ground, this option allow the GUI to connect the path to the ground with '
                                  'polygons.',
                 'info_button_6': 'If the above option is checked, by default, the polygons are filled with the same '
                                  'color chosen for the path. This option will add a certain amount of transparency '
                                  'to the polygons.',
                 'info_button_7': 'Sometime, a path can be composed of a great number of samples, in particular '
                                  'with airborne data, increasing greatly the size of the KML/KMZ file. Thus with this '
                                  'option, it is possible to reduce the number of samples by keeping 1 sample on N '
                                  'samples. Only integers are accepted.',
                 'info_button_8': 'A colormap is mandatory to display the values of a variable along a path in Google '
                                  'Earth. The different colormaps are from Matplotlib. Select one of them to activate '
                                  'all colormap options.',
                 'info_button_9': 'The colormap can be displayed at four different positions in Google Earth and '
                                   'following two orientations:<ul><li>horizontal and at the '
                                   'bottom</li><li>horizontal and at the top</li><li>vertical and on the '
                                   'left</li><li>vertical and on the right</li></ul>',
                 'info_button_11': 'This option is used to reverse the colormap. If the colormap is starting with blue '
                                  'and ending with red, the reversed colormap will start with red and and end with '
                                  'blue.',
                 'info_button_10': 'The path is a succession of segments. Each segment is composed of a starting '
                                   'point and a ending point, each of them defined by its coordinates and its value. '
                                   'In Google Earth, for a path, the points are not colored, but the segments are. '
                                   'This option is used to choose how each segment is colored:<ul><li>mean: the color '
                                   'of the segment is based on the value of the mean between the starting point and '
                                   'the ending point</li><li>first point: the color of the segment is based on the '
                                   'value of the starting point</li><li>last point: the color of the segment is based '
                                   'on the value of the ending point',
                 'info_button_12': 'If handled automaticallu, the minimum and maximum values of the colormap are the '
                                  'minimum (integer) and the maximum value (integer + 1) of the displayed variable. '
                                  'The number of steps is set to 15 and is the number of intervals equally distributed '
                                  'between the minimum and maximum values. Uncheck this option to handle those values '
                                  'manually.',
                 'info_button_13': 'If checked, the GUI handles the colormap dimensions automatically. Uncheck this '
                                   'option to set the dimensions according to your needs. By default, dimensions are '
                                   'set this way:<ul><li>for a vertical colormap:<ul><li>figure width = 1 ('
                                   'inches)</li><li>figure height = 8 (inches)</li><li>position from left = '
                                   '0.05 (fraction)</li><li>position from bottom = 0.05 (fraction)</li><li>colormap '
                                   'width = 0.25 (fraction)</li><li>colormap height = 0.9 ('
                                   'fraction)</li></ul></li></ul>'
                                   '<ul><li>for an horizontal colormap:<ul><li>figure width = 8 (inches)</li><li>figure'
                                   ' height = 1 (inches)</li><li>position from left = 0.05 (fraction)</li><li>position '
                                   'from bottom = 0.60 (fraction)</li><li>colormap width = 0.9 ('
                                   'fraction)</li><li>colormap height = 0.25 (fraction)</li></ul></li></ul>'}
    return info_dict


def batch_processing_information_text():
    logging.debug('gui - help.py - batch_processing_information_buttons_text')
    info_dict = {'bw_info_1': 'At this time, the batch processing function has 6 different '
                              'processes:<ul><li>the concatenation of multiple files</li><li>the '
                              'conversion of multiple NetCDF files to NASA Ames file '
                              'format</li><li>the conversion of multiple NASA Ames files to '
                              'NetCDF format</li><li>the deletion of one or more global metadata '
                              '(only for NetCDF files)</li><li>the deletion of one or more '
                              'variables</li><li>and the use of an algorithm on multiple '
                              'files</li></ul>Select one of them to display options related to '
                              'the selected process.',
                 'bw_info_2': 'Once a category and an algorithm have been selected, the Algorithm '
                              'options tab will list the different input(s) and output(s).',
                 'bw_info_3': 'In case of error with one or more files, the GUI will decide to '
                              'continue or stop the processing based on this option.',
                 'bw_info_4': 'Select here all the files to be processed. It is possible to '
                              'select a specific format by playing the radiobuttons. If the GUI '
                              'detects files in the selected folder, those files are displayed '
                              'in the list below. Furthermore, it is possible to manipulate the '
                              'file list with the different buttons on the right of the file list.',
                 'bw_info_5': 'Select here the folder where to save files after the processing.',
                 'bw_info_6': 'If the previous option is selected, the GUI will handle the '
                              'filename automatically. However, if the user wants to manage '
                              'himself the name of all files after the processing, he can do it '
                              'by turning the option off. The creation of filenames is then '
                              'handles by the following widgets. In that case, the base filename '
                              'is the concatenation of the text displayed in each LineEdit below. '
                              'Each Combobox can be used to select pre-formated options or free '
                              'text.',
                 'Date and time': 'This option will display the actual date and time following '
                                  'the format:<ul><li><b>%Y</b> for year</li><li><b>%m</b> for '
                                  'month</li><li><b>%d</b> for day</li><li><b>%H</b> for '
                                  'hour</li><li><b>%M</b> for minute</li><li><b>%S</b> for '
                                  'second</li></ul>It is possible to mix text and options, '
                                  'or to write only date or time.<br><br><u>Ex:</u> '
                                  '<b>%Y-%m-%d-T%H:%M:%S</b> will display '
                                  '<b>2019-01-06T12:00:00</b>',
                 'Text': 'This option is used to write free text only.<br><br><u>Ex:</u> '
                         '<i>my_free_text</i>',
                 'Original filename': 'With this option, for each processed file, the new filename '
                                      'will contain the original filename. <br><br><u>Ex:</u> if '
                                      'the name of the processed file is '
                                      '<i>my_sea_level_measurements.nc</i>, the new filename will '
                                      'contain <i>my_sea_level_measurements</i>',
                 'Serial number with n digit': 'This option adds a number with n digit to the '
                                               'filename. As the processing iterates through the '
                                               'file list, the number increases by one at each '
                                               'iteration. It can be a number like <i>10</i> or a '
                                               'number preceded by one or more zeros like '
                                               '<i>0010</i>.<br><br><u>Ex:</u> 0010<br>&nbsp;&nbsp;'
                                               '&nbsp;&nbsp;sea_level_measurements_0010.nc<br>'
                                               '&nbsp;&nbsp;&nbsp;&nbsp;sea_level_measurements_'
                                               '0011.nc<br>&nbsp;&nbsp;&nbsp;&nbsp;sea_level_measu'
                                               'rements_0012.nc<br>&nbsp;&nbsp;&nbsp;&nbsp;...',
                 'Make a choice...': 'Please select an option first.',
                 'bw_info_7': 'bw_combobox_5',
                 'bw_info_8': 'bw_combobox_6',
                 'bw_info_9': 'bw_combobox_7',
                 'bw_info_10': 'bw_combobox_8',
                 'bw_info_11': 'bw_combobox_9'}

    return info_dict