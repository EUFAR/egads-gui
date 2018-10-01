import copy
import logging
import numpy
import ntpath
import platform
import os
import matplotlib
import cartopy
import collections
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_plotwindow import Ui_plotWindow
from ui.Ui_plottypewindow import Ui_plottypeWindow
from ui.Ui_tickslabelswindow import Ui_tickslabelsWindow
from functions.gui_functions import clear_layout
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#from cmocean import cm as cmo
from cartopy.util import add_cyclic_point
from scipy.interpolate import griddata, interp2d
from functions.other_window_functions import MyWait, MyInfo
from functions.thread_functions import DrawGriddedMap, ProvideWidthHeight
from functions.material_functions import setup_plot_material
        
        
class PlotWindow(QtWidgets.QDialog, Ui_plotWindow):
    def __init__(self, variables, dimensions, font_list, default_font):
        logging.debug('gui - plot_window_functions.py - PlotWindow - __init__')
        QtWidgets.QDialog.__init__(self, parent=None)
        self.setupUi(self)
        self.resize(1250, 750)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.pw_saveOptions_cb_1.setItemDelegate(itemDelegate)
        self.pw_saveOptions_cb_2.setItemDelegate(itemDelegate)
        self.variables = variables
        self.dimensions = dimensions
        self.font_list = font_list
        self.default_font = default_font
        setup_plot_material(self)
        self.setup_toolbar()
        self.setup_plot_area()
        self.actionClose.triggered.connect(self.close_window)
        self.actionSave_as.triggered.connect(self.plot_save)
        self.actionPan.triggered.connect(self.plot_pan)
        self.actionZoom.triggered.connect(self.plot_zoom)
        self.actionOrigin.triggered.connect(self.plot_home)
        self.pw_lock_bt_1.clicked.connect(self.unlock_size_edit)
        self.pw_saveOptions_cb_1.currentIndexChanged.connect(self.convert_inch_cm)
        self.pw_saveOptions_cb_2.currentIndexChanged.connect(self.convert_inch_cm)
        self.pw_saveOptions_sl_1.valueChanged.connect(self.update_quality_value)
        self.pw_saveOptions_ln_3.setText('100')
        self.pw_saveOptions_lb_7.setText('95')
        self.select_plot_type()
        self.thread_set_width_height = ProvideWidthHeight(self.pw_saveOptions_ln_1, self.pw_saveOptions_ln_2)
        self.thread_set_width_height.start()
        logging.info('gui - plot_window_functions.py - PlotWindow - ready')
    
    
    def select_plot_type(self):
        if len(self.variables) == 1:
            logging.debug('gui - plot_window_functions.py - PlotWindow - select_plot_type - only one variable has been found.')
            dim_num = len(self.variables[list(self.variables.keys())[0]]['dimensions'])
            if dim_num == 1:
                self.plot_timeseries('plot')
            elif dim_num == 2:
                lon_in, lat_in = False, False
                georeferenced = []
                for dim in self.variables[list(self.variables.keys())[0]]['dimensions']:
                    if dim.lower() in ['longitude', 'long', 'lon']:
                        lon_in = True
                    if dim.lower() in ['latitude', 'lat']:
                        lat_in = True
                    if lon_in and lat_in:
                        georeferenced.append(True)
                
                info_text = ('Actually, the function to plot gridded data is still beta. Thus it is not possible yet to modify '
                             + 'the figure and options are not available.')
                self.infoWindow = MyInfo(info_text)
                x1, y1, w1, h1 = self.geometry().getRect()
                self.infoWindow.exec_()
                
                self.plot_single_grid_start(georeferenced)
            elif dim_num == 3:
                data_shape = self.variables[list(self.variables.keys())[0]]['values'].shape
                if data_shape[0] > 1 and data_shape[1] > 1 and data_shape[2] > 1:
                    logging.info('gui - plot_window_functions.py - PlotWindow - select_plot_type - EGADS GUI can\'t plot variables with more than 2 dimensions.')
                    print('EGADS GUI can\'t plot variables with more than 2 dimensions.')
                else:
                    for dim, value in self.dimensions.items():
                        if len(value['values']) == 1:
                            self.variables[list(self.variables.keys())[0]]['values'] = numpy.squeeze(self.variables[list(self.variables.keys())[0]]['values'], value['axis'])
                            break
                    self.dimensions.pop(dim)
                    self.variables[list(self.variables.keys())[0]]['dimensions'].remove(dim)
                    lon_in, lat_in = False, False
                    georeferenced = []
                    for dim in self.variables[list(self.variables.keys())[0]]['dimensions']:
                        if dim.lower() in ['longitude', 'long', 'lon']:
                            lon_in = True
                        if dim.lower() in ['latitude', 'lat']:
                            lat_in = True
                        if lon_in and lat_in:
                            georeferenced.append(True)
                            
                    info_text = ('Actually, the function to plot gridded data is still beta. Thus it is not possible yet to modify '
                                 + 'the figure and options are not available.')
                    self.infoWindow = MyInfo(info_text)
                    x1, y1, w1, h1 = self.geometry().getRect()
                    self.infoWindow.exec_()
                    
                    self.plot_single_grid_start(georeferenced)
            else:
                print('EGADS GUI can\'t plot variables with more than 2 dimensions.')
                logging.info('gui - plot_window_functions.py - PlotWindow - select_plot_type - EGADS GUI can\'t plot variables with more than 2 dimensions.')
        elif len(self.variables) > 1:
            logging.debug('gui - plot_window_functions.py - PlotWindow - select_plot_type - more than one variable have been found, ' + str(len(self.variables)))
            dim_num = []
            units = []
            dim_name = []
            for _, value in self.variables.items():
                dim_num.append(len(value['dimensions']))
                dim_name.append(value['dimensions'])
                units.append(value['units'])
            if dim_num.count(dim_num[0]) == len(dim_num):
                if dim_num[0] == 1:
                    if dim_name.count(dim_name[0]) == len(dim_name):
                        if units.count(units[0]) == len(units):
                            self.plottypeWindow = PlotTypeWindow()
                            self.plottypeWindow.exec_()
                            self.plot_timeseries(self.plottypeWindow.result)
                        else:
                            self.plot_timeseries('subplot')                  
                    else:
                        self.plot_timeseries('subplot')    
                else:
                    print('EGADS GUI can\'t plot more than 1 variable with more than 1 dimensions')
                    logging.info('gui - plot_window_functions.py - PlotWindow - select_plot_type - EGADS GUI can\'t plot more than 1 '
                                 + 'variable with more than 1 dimensions')
            else:
                print('Each variable has a different number of dimensions, this is not yet supported')
                logging.info('gui - plot_window_functions.py - PlotWindow - select_plot_type - Each variable has a different number of dimensions, '
                             + 'this is not yet supported')
            
    def plot_timeseries(self, plot_type):
        if plot_type == 'plot':
            subplot_plot = [self.figure.add_subplot(1, 1, 1)]
            for yname in self.variables:
                yvalues = self.variables[yname]['values']
                yunits = self.variables[yname]['units']
                xname = self.variables[yname]['dimensions'][0]
                xvalues = self.dimensions[xname]['values']
                xunits = self.dimensions[xname]['units']
                subplot_plot[0].plot(xvalues, yvalues, label = yname)
            subplot_plot[0].set_ylabel(yunits)
            subplot_plot[0].set_xlabel(xunits)
            subplot_plot[0].set_ylim([subplot_plot[0].axes.get_yticks()[0], subplot_plot[0].axes.get_yticks()[-1]])
            subplot_plot[0].set_xlim([subplot_plot[0].axes.get_xticks()[0], subplot_plot[0].axes.get_xticks()[-1]])
            subplot_plot[0].spines['top'].set_visible(False)
            subplot_plot[0].spines['right'].set_visible(False)
            leg = subplot_plot[0].legend(prop={'family':self.default_font, 'size':'10'})
            leg.draggable()
            plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.90, wspace=0.4, hspace=0.4)
            self.set_figure_options('plot', subplot_plot)
            self.set_plot_options('plot', subplot_plot)
        elif plot_type == 'subplot':
            subplot_plot = []
            i = 0
            for yname in self.variables:
                yvalues = self.variables[yname]['values']
                yunits = self.variables[yname]['units']
                xname = self.variables[yname]['dimensions'][0]
                xvalues = self.dimensions[xname]['values']
                xunits = self.dimensions[xname]['units']
                subplot_plot.append(self.figure.add_subplot(len(self.variables), 1, i + 1))
                subplot_plot[i].plot(xvalues, yvalues, label = yname)
                subplot_plot[i].set_ylabel(yunits)
                subplot_plot[i].set_xlabel(xunits)
                subplot_plot[i].set_ylim([subplot_plot[i].axes.get_yticks()[0], subplot_plot[i].axes.get_yticks()[-1]])
                subplot_plot[i].set_xlim([subplot_plot[i].axes.get_xticks()[0], subplot_plot[i].axes.get_xticks()[-1]])
                subplot_plot[i].spines['top'].set_visible(False)
                subplot_plot[i].spines['right'].set_visible(False)
                leg = subplot_plot[i].legend(prop={'family':self.default_font, 'size':'10'})
                leg.draggable()
                i += 1
            #self.figure.tight_layout()
            plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.90, wspace=0.4, hspace=0.4)
            self.set_figure_options('subplot', subplot_plot)
            self.set_plot_options('subplot', subplot_plot)
        self.canvas.draw()
        self.add_figure_options('timeseries')
        self.add_plot_options('timeseries')
        self.pw_update_bt_1.clicked.connect(lambda: self.update_figure_options('timeseries'))
        self.pw_update_bt_2.clicked.connect(lambda: self.update_plot_options('timeseries'))
    
    def plot_single_grid_start(self, georeferenced):
        self.tab_view.removeTab(2)
        self.tab_view.removeTab(1)
        
        subplot_object = collections.OrderedDict()
        i = 0
        high_density = False
        for var_name in self.variables:
            lon, lat = None, None
            subplot_dict = {}
            subplot_dict['var_values'] = self.variables[var_name]['values']
            subplot_dict['var_units'] = self.variables[var_name]['units']
            subplot_dict['var_dims'] = self.variables[var_name]['dimensions']
            if georeferenced[i]:
                subplot_dict['georeferenced'] = georeferenced
                for dim in self.variables[var_name]['dimensions']:
                    if dim.lower() in ['longitude', 'long', 'lon']:
                        subplot_dict['lon_name'] = dim
                        subplot_dict['lon_values'] = self.dimensions[dim]['values']
                        subplot_dict['lon_units'] = self.dimensions[dim]['units']
                    if dim.lower() in ['latitude', 'lat']:
                        subplot_dict['lat_name'] = dim
                        subplot_dict['lat_values'] = self.dimensions[dim]['values']
                        subplot_dict['lat_units'] = self.dimensions[dim]['units']
                subplot_dict['var_values'], subplot_dict['lon_values'] = add_cyclic_point(subplot_dict['var_values'], coord=subplot_dict['lon_values'])
                subplot_dict['projection'] = cartopy.crs.PlateCarree(central_longitude=0)   
            else:
                subplot_dict['lon_name'] = var_dims[0]
                subplot_dict['lon_values'] = self.dimensions[var_dims[0]]['values']
                subplot_dict['lon_units'] = self.dimensions[var_dims[0]]['units']
                subplot_dict['lat_name'] = var_dims[1]
                subplot_dict['lat_values'] = self.dimensions[var_dims[1]]['values']
                subplot_dict['lat_units'] = self.dimensions[var_dims[1]]['units']
                subplot_dict['projection'] = None
            subplot_dict['ax'] = plt.subplot(len(self.variables), 1, i + 1, projection=subplot_dict['projection'])
            subplot_object[var_name] = subplot_dict
            if len(subplot_dict['lon_values']) * len(subplot_dict['lat_values']) > 65000:
                high_density = True
        if high_density:
            self.thread = DrawGriddedMap(subplot_object)
            self.thread.started.connect(self.wait_window)
            self.thread.finished.connect(self.close_wait_window)
            self.thread.start()
        else:
            for sublot in subplot_object:
                sublot['ax'].pcolormesh(lon_values, lat_values, var_values, transform=subplot['projection'], cmap='jet')
            self.plot_single_grid_end(subplot_object)
        
    def plot_single_grid_end(self, subplot_object):
        for key, subplot in subplot_object.items():
            if subplot['georeferenced']:
                coastline_shp_file = 'functions/shape_files/ne_110m_coastline.shp'
                land_shp_file = 'functions/shape_files/ne_110m_land.shp'
                for land in cartopy.io.shapereader.Reader(land_shp_file).records():
                    subplot['ax'].add_geometries(land.geometry, subplot['projection'], facecolor='#e6e6e6')
                for coastline in cartopy.io.shapereader.Reader(coastline_shp_file).records():
                    subplot['ax'].add_geometries(coastline.geometry, subplot['projection'], edgecolor='black', linewidth=1.0, facecolor='None', antialiased=True)
                
                gl = subplot['ax'].gridlines(crs=subplot['projection'], draw_labels=True, linewidth=1, color='black', alpha=1, linestyle='-')
                gl.xlabels_top = True
                gl.ylabels_left = True
                gl.xlines = True
                gl.ylines = True
                #gl.xlocator = matplotlib.ticker.FixedLocator([-180, -120, -60, -30, 0, 30, 60, 120, 180])
                #gl.ylocator = matplotlib.ticker.FixedLocator([-80, -40, 0, 40, 80])
                gl.xformatter = cartopy.mpl.gridliner.LONGITUDE_FORMATTER
                gl.yformatter = cartopy.mpl.gridliner.LATITUDE_FORMATTER
                subplot['ax'].text(-0.07, 0.55, 'Latitude', va='bottom', ha='center',
                                   rotation='vertical', rotation_mode='anchor',
                                   transform=subplot['ax'].transAxes)
                subplot['ax'].text(0.5, -0.1, 'Longitude', va='bottom', ha='center',
                                   rotation='horizontal', rotation_mode='anchor',
                                   transform=subplot['ax'].transAxes)
                subplot_object[key]['gl'] = gl
                
        plt.subplots_adjust(left=0.085, right=0.85, bottom=0.085, top=0.9)
        self.canvas.draw()
        #self.set_figure_options('grid', subplot_object)
        #self.add_figure_options('grids')
        
    
        
    def set_figure_options(self, plot_type, subplot_list=None):
        if plot_type == 'plot' or plot_type == 'subplot':
            self.figure_options['title'] = []
            self.figure_options['title_font'] = []
            self.figure_options['title_size'] = []
            self.figure_options['xlabel'] = []
            self.figure_options['xlabel_font'] = []
            self.figure_options['xlabel_size'] = []
            self.figure_options['ylabel'] = []
            self.figure_options['ylabel_font'] = []
            self.figure_options['ylabel_size'] = []
            self.figure_options['spine_top'] = []
            self.figure_options['spine_right'] = []
            self.figure_options['margin_left'] = []
            self.figure_options['margin_right'] = []
            self.figure_options['margin_bottom'] = []
            self.figure_options['margin_top'] = []
            self.figure_options['horizontal_space'] = []
            self.figure_options['vertical_space'] = []
            self.figure_options['grid'] = []
            self.figure_options['grid_style'] = []
            self.figure_options['grid_size'] = []
            self.figure_options['grid_color'] = []
            self.figure_options['display_legend'] = []
            self.figure_options['xlim_max'] = []
            self.figure_options['xlim_min'] = []
            self.figure_options['ylim_max'] = []
            self.figure_options['ylim_min'] = []
            self.figure_options['xlim_step'] = []
            self.figure_options['ylim_step'] = []
            self.figure_options['xticks'] = []
            self.figure_options['yticks'] = []
        elif plot_type == 'grid' or plot_type == 'subgrid':
            self.figure_options['title'] = []
            self.figure_options['title_font'] = []
            self.figure_options['title_size'] = []
            self.figure_options['xlabel'] = []
            self.figure_options['xlabel_font'] = []
            self.figure_options['xlabel_size'] = []
            self.figure_options['ylabel'] = []
            self.figure_options['ylabel_font'] = []
            self.figure_options['ylabel_size'] = []
            self.figure_options['margin_left'] = []
            self.figure_options['margin_right'] = []
            self.figure_options['margin_bottom'] = []
            self.figure_options['margin_top'] = []
            self.figure_options['grid'] = []
            self.figure_options['grid_style'] = []
            self.figure_options['grid_size'] = []
            self.figure_options['grid_color'] = []
            self.figure_options['xlim_max'] = []
            self.figure_options['xlim_min'] = []
            self.figure_options['ylim_max'] = []
            self.figure_options['ylim_min'] = []
            self.figure_options['xticks'] = []
            self.figure_options['yticks'] = []
            self.figure_options['projection'] = []
            self.figure_options['projection_central_longitude'] = []
            self.figure_options['projection_central_latitude'] = []
            self.figure_options['colorbar'] = []
            self.figure_options['colorbar_orientation'] = []
            self.figure_options['colorbar_height'] = []
            self.figure_options['colorbar_width'] = []
            self.figure_options['colorbar_axis_xposition'] = []
            self.figure_options['colorbar_axis_yposition'] = []
            
            
            
        if plot_type == 'plot':
            self.figure_options['title'].append('')
            self.figure_options['title_font'].append(self.default_font)
            self.figure_options['title_size'].append(10)
            self.figure_options['xlabel'].append(plt.axes().xaxis.get_label_text())
            self.figure_options['xlabel_font'].append(self.default_font)
            self.figure_options['xlabel_size'].append(10)
            self.figure_options['ylabel'].append(plt.axes().yaxis.get_label_text())
            self.figure_options['ylabel_font'].append(self.default_font)
            self.figure_options['ylabel_size'].append(10)
            self.figure_options['spine_top'].append(False)
            self.figure_options['spine_right'].append(False)
            self.figure_options['margin_left'].append(0.1)
            self.figure_options['margin_right'].append(0.95)
            self.figure_options['margin_bottom'].append(0.1)
            self.figure_options['margin_top'].append(0.90)
            self.figure_options['horizontal_space'].append(None)
            self.figure_options['vertical_space'].append(None)
            self.figure_options['grid'].append(False)
            self.figure_options['grid_style'].append('-')
            self.figure_options['grid_size'].append(0.5)
            self.figure_options['grid_color'].append('Black')
            self.figure_options['display_legend'].append(True)
            self.figure_options['xlim_max'].append(plt.axes().get_xlim()[1])
            self.figure_options['xlim_min'].append(plt.axes().get_xlim()[0])
            self.figure_options['ylim_max'].append(plt.axes().get_ylim()[1])
            self.figure_options['ylim_min'].append(plt.axes().get_ylim()[0])
            self.figure_options['xlim_step'].append(plt.axes().get_xticks()[1] - plt.axes().get_xticks()[0])
            self.figure_options['ylim_step'].append(plt.axes().get_yticks()[1] - plt.axes().get_yticks()[0])
            self.figure_options['xticks'].append(plt.axes().get_xticks())
            self.figure_options['yticks'].append(plt.axes().get_yticks())
        elif plot_type == 'subplot':
            self.figure_options['figure_instance'] = subplot_list
            for i, subplot in enumerate(self.figure_options['figure_instance']):
                self.figure_options['title'].append('')
                self.figure_options['title_font'].append(self.default_font)
                self.figure_options['title_size'].append(10)
                self.figure_options['xlabel'].append(subplot.axes.xaxis.get_label_text())
                self.figure_options['xlabel_font'].append(self.default_font)
                self.figure_options['xlabel_size'].append(10)
                self.figure_options['ylabel'].append(subplot.axes.yaxis.get_label_text())
                self.figure_options['ylabel_font'].append(self.default_font)
                self.figure_options['ylabel_size'].append(10)
                self.figure_options['spine_top'].append(False)
                self.figure_options['spine_right'].append(False)
                self.figure_options['margin_left'].append(0.1)
                self.figure_options['margin_right'].append(0.95)
                self.figure_options['margin_bottom'].append(0.1)
                self.figure_options['margin_top'].append(0.90)
                self.figure_options['horizontal_space'].append(0.4)
                self.figure_options['vertical_space'].append(0.4)
                self.figure_options['grid'].append(False)
                self.figure_options['grid_style'].append('-')
                self.figure_options['grid_size'].append(0.5)
                self.figure_options['grid_color'].append('Black')
                self.figure_options['display_legend'].append(True)
                self.figure_options['xlim_max'].append(subplot.axes.get_xlim()[1])
                self.figure_options['xlim_min'].append(subplot.axes.get_xlim()[0])
                self.figure_options['ylim_max'].append(subplot.axes.get_ylim()[1])
                self.figure_options['ylim_min'].append(subplot.axes.get_ylim()[0])
                self.figure_options['xlim_step'].append(subplot.axes.get_xticks()[1] - subplot.axes.get_xticks()[0])
                self.figure_options['ylim_step'].append(subplot.axes.get_yticks()[1] - subplot.axes.get_yticks()[0])
                self.figure_options['xticks'].append(subplot.axes.get_xticks())
                self.figure_options['yticks'].append(subplot.axes.get_yticks())
        elif plot_type == 'grid':
            self.figure_options['title'].append('')
            self.figure_options['title_font'].append(self.default_font)
            self.figure_options['title_size'].append(10)
            #self.figure_options['xlabel'].append(plt.axes().xaxis.get_label_text())
            self.figure_options['xlabel_font'].append(self.default_font)
            self.figure_options['xlabel_size'].append(10)
            #self.figure_options['ylabel'].append(plt.axes().yaxis.get_label_text())
            self.figure_options['ylabel_font'].append(self.default_font)
            self.figure_options['ylabel_size'].append(10)
            self.figure_options['margin_left'].append(0.085)
            self.figure_options['margin_right'].append(0.85)
            self.figure_options['margin_bottom'].append(0.085)
            self.figure_options['margin_top'].append(0.90)
            self.figure_options['grid'].append(False)
            self.figure_options['grid_style'].append('-')
            self.figure_options['grid_size'].append(1)
            self.figure_options['grid_color'].append('Black')
            
            for key, subplot in subplot_list.items():
                xlim_min, xlim_max = subplot['ax'].axes.get_xlim()
                ylim_min, ylim_max = subplot['ax'].axes.get_ylim()
            self.figure_options['xlim_max'].append(xlim_max)
            self.figure_options['xlim_min'].append(xlim_min)
            self.figure_options['ylim_max'].append(ylim_max)
            self.figure_options['ylim_min'].append(ylim_min)
            self.figure_options['xticks'].append(None)
            self.figure_options['yticks'].append(None)
            self.figure_options['projection'].append('PlateCarree')
            self.figure_options['colorbar'].append('jet')
            self.figure_options['colorbar_orientation'].append('vertical')
            self.figure_options['colorbar_height'].append(0.7)
            self.figure_options['colorbar_width'].append(0.02)
            self.figure_options['colorbar_axis_xposition'].append(0.9)
            self.figure_options['colorbar_axis_yposition'].append(0.13)
            
            
            
    
    def set_plot_options(self, plot_type, subplot_list=None):
        if plot_type == 'plot' or plot_type == 'subplot':
            self.plot_options['line_style'] = []
            self.plot_options['line_marker'] = []
            self.plot_options['line_color'] = []
            self.plot_options['line_width'] = []
            self.plot_options['line_antialiased'] = []
            self.plot_options['line_alpha'] = []
            self.plot_options['line_alpha_perc'] = []
            self.plot_options['legend_label'] = []
        if plot_type == 'plot':
            for line in plt.axes().lines:
                self.plot_options['line_style'].append(line.get_linestyle())
                self.plot_options['line_marker'].append('line')
                self.plot_options['line_color'].append(line.get_color())
                self.plot_options['line_width'].append(line.get_linewidth())
                self.plot_options['line_antialiased'].append(line.get_antialiased())
                self.plot_options['line_alpha'].append(False)
                self.plot_options['line_alpha_perc'].append(line.get_alpha())
                self.plot_options['legend_label'].append(line.get_label())
        elif plot_type == 'subplot':
            self.plot_options['figure_instance'] = subplot_list
            for i, subplot in enumerate(self.plot_options['figure_instance']):
                self.plot_options['line_style'].append(subplot.axes.lines[0].get_linestyle())
                self.plot_options['line_marker'].append('line')
                self.plot_options['line_color'].append(subplot.axes.lines[0].get_color())
                self.plot_options['line_width'].append(subplot.axes.lines[0].get_linewidth())
                self.plot_options['line_antialiased'].append(subplot.axes.lines[0].get_antialiased())
                self.plot_options['line_alpha'].append(False)
                self.plot_options['line_alpha_perc'].append(subplot.axes.lines[0].get_alpha())
                self.plot_options['legend_label'].append(subplot.axes.lines[0].get_label())

    def add_figure_options(self, plot_type):
        logging.debug('gui - plot_window_functions.py - PlotWindow - figure_options')
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/tick_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if plot_type == 'timeseries':
            for _ in self.figure_options['title']:
                if self.figure_option_num == 0:
                    self.figure_options_sliders()
                self.pw_figureOptions_vl_1.append(QtWidgets.QVBoxLayout())
                self.pw_figureOptions_vl_1[self.figure_option_num].setObjectName("pw_figureOptions_vl_1_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_1.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_1[self.figure_option_num].setObjectName("pw_figureOptions_hl_1_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_1.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_1[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_1[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_1[self.figure_option_num].setFont(font2)
                if 'figure_instance' in self.figure_options:
                    text = 'Subplot ' + str(self.figure_option_num + 1) + ': Figure options'
                else:
                    text = 'Figure options:'
                self.pw_figureOptions_lb_1[self.figure_option_num].setText(text)     
                self.pw_figureOptions_lb_1[self.figure_option_num].setObjectName("pw_figureOptions_lb_1_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_1[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_hl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_1[self.figure_option_num])
                self.pw_figureOptions_hl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_1[self.figure_option_num])
                self.pw_figureOptions_hl_2.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_2[self.figure_option_num].setObjectName("pw_figureOptions_hl_2_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_gl_1.append(QtWidgets.QGridLayout())
                self.pw_figureOptions_gl_1[self.figure_option_num].setObjectName("pw_figureOptions_gl_1_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_2[self.figure_option_num].addLayout(self.pw_figureOptions_gl_1[self.figure_option_num])
                self.pw_figureOptions_lb_2.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_2[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_2[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_2[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_2[self.figure_option_num].setText("Figure title:")
                self.pw_figureOptions_lb_2[self.figure_option_num].setObjectName("pw_figureOptions_lb_2_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_2[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_2[self.figure_option_num], 0, 0, 1, 1)
                self.pw_figureOptions_ln_1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_ln_1[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_1[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_1[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_1[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_1[self.figure_option_num].setObjectName("pw_lineEdit_1_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_ln_1[self.figure_option_num], 0, 1, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 2, 1, 1)
                self.pw_figureOptions_lb_3.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_3[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_3[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_3[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_3[self.figure_option_num].setText("Font:")
                self.pw_figureOptions_lb_3[self.figure_option_num].setObjectName("pw_figureOptions_lb_3_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_3[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_3[self.figure_option_num], 0, 3, 1, 1)
                self.pw_figureOptions_cb_1.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_1[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_1[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_1[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_1[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_1[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_1[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_1[self.figure_option_num].setObjectName("pw_figureOptions_cb_1_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_1[self.figure_option_num], 0, 4, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 5, 1, 1)
                self.pw_figureOptions_lb_4.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_4[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_4[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_4[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_4[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_4[self.figure_option_num].setObjectName("pw_figureOptions_lb_4_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_4[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_4[self.figure_option_num], 0, 6, 1, 1)
                self.pw_figureOptions_cb_2.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_2[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_2[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_2[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_2[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_2[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_2[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_2[self.figure_option_num].setObjectName("pw_figureOptions_cb_2_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_2[self.figure_option_num], 0, 7, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 8, 1, 1)
                self.pw_figureOptions_lb_5.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_5[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_5[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_5[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_5[self.figure_option_num].setText("X axis label:")
                self.pw_figureOptions_lb_5[self.figure_option_num].setObjectName("pw_figureOptions_lb_5_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_5[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_5[self.figure_option_num], 1, 0, 1, 1)
                self.pw_figureOptions_ln_2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_ln_2[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_2[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_2[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_2[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_2[self.figure_option_num].setObjectName("pw_lineEdit_2_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_ln_2[self.figure_option_num], 1, 1, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
                self.pw_figureOptions_lb_6.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_6[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_6[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_6[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_6[self.figure_option_num].setText("Font:")
                self.pw_figureOptions_lb_6[self.figure_option_num].setObjectName("pw_figureOptions_lb_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_6[self.figure_option_num], 1, 3, 1, 1)
                self.pw_figureOptions_cb_3.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_3[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_3[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_3[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_3[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_3[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_3[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_3[self.figure_option_num].setObjectName("pw_figureOptions_cb_3_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_3[self.figure_option_num], 1, 4, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 5, 1, 1)
                self.pw_figureOptions_lb_7.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_7[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_7[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_7[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_7[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_7[self.figure_option_num].setObjectName("pw_figureOptions_lb_7_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_7[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_7[self.figure_option_num], 1, 6, 1, 1)
                self.pw_figureOptions_cb_4.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_4[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_4[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_4[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_4[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_4[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_4[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_4[self.figure_option_num].setObjectName("pw_figureOptions_cb_4_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_4[self.figure_option_num], 1, 7, 1, 1)
                self.pw_figureOptions_lb_8.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_8[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_8[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_8[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_8[self.figure_option_num].setText("Y axis label:")
                self.pw_figureOptions_lb_8[self.figure_option_num].setObjectName("pw_figureOptions_lb_8_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_8[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_8[self.figure_option_num], 2, 0, 1, 1)
                self.pw_figureOptions_ln_3.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_ln_3[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_3[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_3[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_3[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "   padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_3[self.figure_option_num].setObjectName("pw_lineEdit_3_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_ln_3[self.figure_option_num], 2, 1, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 2, 2, 1, 1)
                self.pw_figureOptions_lb_9.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_9[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_9[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_9[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_9[self.figure_option_num].setText("Font:")
                self.pw_figureOptions_lb_9[self.figure_option_num].setObjectName("pw_figureOptions_lb_9_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_9[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_9[self.figure_option_num], 2, 3, 1, 1)
                self.pw_figureOptions_cb_5.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_5[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_5[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_5[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_5[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_5[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_5[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_5[self.figure_option_num].setObjectName("pw_figureOptions_cb_5_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_5[self.figure_option_num], 2, 4, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 2, 5, 1, 1)
                self.pw_figureOptions_lb_10.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_10[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_10[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_10[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_10[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_10[self.figure_option_num].setObjectName("pw_figureOptions_lb_10_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_10[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_10[self.figure_option_num], 2, 6, 1, 1)
                self.pw_figureOptions_cb_6.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_6[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_6[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_6[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_6[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_6[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_6[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_6[self.figure_option_num].setObjectName("pw_figureOptions_cb_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_6[self.figure_option_num], 2, 7, 1, 1)
                self.pw_figureOptions_hl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_bt_1.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_1[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_1[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_1[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_1[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_1[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_1[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_1[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_1[self.figure_option_num].setObjectName("pw_figureOptions_bt_1_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_2[self.figure_option_num].addWidget(self.pw_figureOptions_bt_1[self.figure_option_num])
                self.pw_figureOptions_hl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_2[self.figure_option_num])
                self.pw_figureOptions_hl_3.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_3[self.figure_option_num].setObjectName("pw_figureOptions_hl_3_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_gl_2.append(QtWidgets.QGridLayout())
                self.pw_figureOptions_gl_2[self.figure_option_num].setObjectName("pw_figureOptions_gl_2_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_3[self.figure_option_num].addLayout(self.pw_figureOptions_gl_2[self.figure_option_num])
                self.pw_figureOptions_lb_11.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_11[self.figure_option_num].setMinimumSize(QtCore.QSize(200, 27))
                self.pw_figureOptions_lb_11[self.figure_option_num].setMaximumSize(QtCore.QSize(200, 27))
                self.pw_figureOptions_lb_11[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_11[self.figure_option_num].setText("X min / max / tick step:")
                self.pw_figureOptions_lb_11[self.figure_option_num].setObjectName("pw_figureOptions_lb_11_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_11[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_lb_11[self.figure_option_num], 0, 0, 1, 1)
                self.pw_figureOptions_ln_4.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_4[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_4[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_4[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_4[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_4[self.figure_option_num].setObjectName("pw_figureOptions_ln_4_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_4[self.figure_option_num], 0, 1, 1, 1)
                self.pw_figureOptions_ln_5.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_5[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_5[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_5[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_5[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_5[self.figure_option_num].setObjectName("pw_figureOptions_ln_5_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_5[self.figure_option_num], 0, 2, 1, 1)
                self.pw_figureOptions_ln_6.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_6[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_6[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_6[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_6[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_6[self.figure_option_num].setObjectName("pw_figureOptions_ln_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_6[self.figure_option_num], 0, 3, 1, 1)
                self.pw_figureOptions_gl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 4, 1, 1)
                '''self.pw_figureOptions_lb_12.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_12[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_12[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_12[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_12[self.figure_option_num].setText("Format:")
                self.pw_figureOptions_lb_12[self.figure_option_num].setObjectName("pw_figureOptions_lb_12_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_12[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_lb_12[self.figure_option_num], 0, 5, 1, 1)
                self.pw_figureOptions_cb_7.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_7[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_7[self.figure_option_num].setMinimumSize(QtCore.QSize(180, 27))
                self.pw_figureOptions_cb_7[self.figure_option_num].setMaximumSize(QtCore.QSize(180, 27))
                self.pw_figureOptions_cb_7[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_7[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_7[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_7[self.figure_option_num].setObjectName("pw_figureOptions_cb_7_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_cb_7[self.figure_option_num], 0, 6, 1, 1)'''
                self.pw_figureOptions_lb_13.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_13[self.figure_option_num].setMinimumSize(QtCore.QSize(200, 27))
                self.pw_figureOptions_lb_13[self.figure_option_num].setMaximumSize(QtCore.QSize(200, 27))
                self.pw_figureOptions_lb_13[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_13[self.figure_option_num].setText("Y min / max / tick step:")
                self.pw_figureOptions_lb_13[self.figure_option_num].setObjectName("pw_figureOptions_lb_13_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_13[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_lb_13[self.figure_option_num], 1, 0, 1, 1)
                self.pw_figureOptions_ln_7.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_7[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_7[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_7[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_7[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_7[self.figure_option_num].setObjectName("pw_figureOptions_ln_7_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_7[self.figure_option_num], 1, 1, 1, 1)
                self.pw_figureOptions_ln_8.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_8[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_8[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_8[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_8[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "   padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "}")
                self.pw_figureOptions_ln_8[self.figure_option_num].setObjectName("pw_figureOptions_ln_8_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_8[self.figure_option_num], 1, 2, 1, 1)
                self.pw_figureOptions_ln_9.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_9[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_9[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_9[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_9[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "   padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "}")
                self.pw_figureOptions_ln_9[self.figure_option_num].setObjectName("pw_figureOptions_ln_9_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_9[self.figure_option_num], 1, 3, 1, 1)
                self.pw_figureOptions_gl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 4, 1, 1)
                '''self.pw_figureOptions_lb_14.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_14[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_14[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_14[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_14[self.figure_option_num].setText("Format:")
                self.pw_figureOptions_lb_14[self.figure_option_num].setObjectName("pw_figureOptions_lb_14_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_14[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_lb_14[self.figure_option_num], 1, 5, 1, 1)
                self.pw_figureOptions_cb_8.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_8[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_8[self.figure_option_num].setMinimumSize(QtCore.QSize(180, 27))
                self.pw_figureOptions_cb_8[self.figure_option_num].setMaximumSize(QtCore.QSize(180, 27))
                self.pw_figureOptions_cb_8[self.figure_option_num].setFont(font)
                self.pw_figureOptions_cb_8[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_8[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_8[self.figure_option_num].setObjectName("pw_figureOptions_cb_8_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_cb_8[self.figure_option_num], 1, 6, 1, 1)
                self.pw_figureOptions_hl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))'''
                self.pw_figureOptions_bt_2.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_2[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_2[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_2[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_2[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_2[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_2[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_2[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_2[self.figure_option_num].setObjectName("pw_figureOptions_bt_2_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_3[self.figure_option_num].addWidget(self.pw_figureOptions_bt_2[self.figure_option_num])
                self.pw_figureOptions_hl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_3[self.figure_option_num])
                self.pw_figureOptions_hl_4.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_4[self.figure_option_num].setObjectName("pw_figureOptions_hl_4_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_gl_3.append(QtWidgets.QGridLayout())
                self.pw_figureOptions_gl_3[self.figure_option_num].setObjectName("pw_figureOptions_gl_3_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_4[self.figure_option_num].addLayout(self.pw_figureOptions_gl_3[self.figure_option_num])
                self.pw_figureOptions_lb_15.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_15[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_15[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_15[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_15[self.figure_option_num].setText("Display grid ?")
                self.pw_figureOptions_lb_15[self.figure_option_num].setObjectName("pw_figureOptions_lb_15_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_15[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_15[self.figure_option_num], 0, 0, 1, 1)
                self.pw_figureOptions_ck_1.append(QtWidgets.QCheckBox())
                self.pw_figureOptions_ck_1[self.figure_option_num].setMinimumSize(QtCore.QSize(25, 20))
                self.pw_figureOptions_ck_1[self.figure_option_num].setMaximumSize(QtCore.QSize(25, 20))
                self.pw_figureOptions_ck_1[self.figure_option_num].setText("")
                self.pw_figureOptions_ck_1[self.figure_option_num].setObjectName("pw_figureOptions_ck_1_" + str(self.figure_option_num))
                self.pw_figureOptions_ck_1[self.figure_option_num].setStyleSheet("QCheckBox {\n"
                "    spacing: 5px;\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_ck_1[self.figure_option_num], 0, 1, 1, 1)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 2, 1, 1)
                self.pw_figureOptions_lb_16.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_16[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_16[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_16[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_16[self.figure_option_num].setText("Style:")
                self.pw_figureOptions_lb_16[self.figure_option_num].setObjectName("pw_figureOptions_lb_16_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_16[self.figure_option_num], 0, 3, 1, 1)
                self.pw_figureOptions_cb_9.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_9[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_9[self.figure_option_num].setEnabled(False)
                self.pw_figureOptions_cb_9[self.figure_option_num].setMinimumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_9[self.figure_option_num].setMaximumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_9[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_9[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_9[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_9[self.figure_option_num].setObjectName("pw_figureOptions_cb_9_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_cb_9[self.figure_option_num], 0, 4, 1, 1)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 5, 1, 1)
                self.pw_figureOptions_lb_17.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_17[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_17[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_17[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_17[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_17[self.figure_option_num].setObjectName("pw_figureOptions_lb_17_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_17[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_17[self.figure_option_num], 0, 6, 1, 1)
                self.pw_figureOptions_ln_10.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_10[self.figure_option_num].setEnabled(False)
                self.pw_figureOptions_ln_10[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_ln_10[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_ln_10[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_10[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QLineEdit:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}")
                self.pw_figureOptions_ln_10[self.figure_option_num].setObjectName("pw_figureOptions_ln_10_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_ln_10[self.figure_option_num], 0, 7, 1, 1)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 8, 1, 1)
                self.pw_figureOptions_lb_19.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_19[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_19[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_19[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_19[self.figure_option_num].setText("Color:")
                self.pw_figureOptions_lb_19[self.figure_option_num].setObjectName("pw_figureOptions_lb_19_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_19[self.figure_option_num], 0, 9, 1, 1)
                self.pw_figureOptions_cb_10.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_10[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_10[self.figure_option_num].setEnabled(False)
                self.pw_figureOptions_cb_10[self.figure_option_num].setMinimumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_10[self.figure_option_num].setMaximumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_10[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_10[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_10[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_10[self.figure_option_num].setObjectName("pw_figureOptions_cb_10_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_cb_10[self.figure_option_num], 0, 10, 1, 1)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 11, 1, 1)
                self.pw_figureOptions_bt_6.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_6[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_6[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_6[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_6[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_6[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_6[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_6[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_6[self.figure_option_num].setObjectName("pw_figureOptions_bt_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_bt_6[self.figure_option_num], 0, 12, 1, 1)
                self.pw_figureOptions_lb_18.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_18[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_18[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_18[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_18[self.figure_option_num].setText("Display Legend ?")
                self.pw_figureOptions_lb_18[self.figure_option_num].setObjectName("pw_figureOptions_lb_18_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_18[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_18[self.figure_option_num], 1, 0, 1, 1)
                self.pw_figureOptions_ck_2.append(QtWidgets.QCheckBox())
                self.pw_figureOptions_ck_2[self.figure_option_num].setMinimumSize(QtCore.QSize(25, 20))
                self.pw_figureOptions_ck_2[self.figure_option_num].setMaximumSize(QtCore.QSize(25, 20))
                self.pw_figureOptions_ck_2[self.figure_option_num].setText("")
                self.pw_figureOptions_ck_2[self.figure_option_num].setChecked(True)
                self.pw_figureOptions_ck_2[self.figure_option_num].setObjectName("pw_figureOptions_ck_2_" + str(self.figure_option_num))
                self.pw_figureOptions_ck_2[self.figure_option_num].setStyleSheet("QCheckBox {\n"
                "    spacing: 5px;\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_ck_2[self.figure_option_num], 1, 1, 1, 1)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
                self.pw_figureOptions_bt_7.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_7[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_7[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_7[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_7[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_7[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_7[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_7[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_7[self.figure_option_num].setObjectName("pw_figureOptions_bt_7_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_bt_7[self.figure_option_num], 1, 3, 1, 1)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 4, 1, 1)
                self.pw_figureOptions_hl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_4[self.figure_option_num])
                self.pw_figureOptions_vl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
                self.pw_figureOptions_li_1.append(QtWidgets.QFrame())
                self.pw_figureOptions_li_1[self.figure_option_num].setFrameShape(QtWidgets.QFrame.HLine)
                self.pw_figureOptions_li_1[self.figure_option_num].setFrameShadow(QtWidgets.QFrame.Sunken)
                self.pw_figureOptions_li_1[self.figure_option_num].setStyleSheet("QFrame {\n"
                "    background: rgb(190,190,190);\n"
                "    height: 5px;\n"
                "    border: 0px solid black;\n"
                "}")
                self.pw_figureOptions_li_1[self.figure_option_num].setObjectName("pw_figureOptions_li_1_" + str(self.figure_option_num))
                self.pw_figureOptions_vl_1[self.figure_option_num].addWidget(self.pw_figureOptions_li_1[self.figure_option_num])
                self.pw_figureOptions_vl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
                self.pw_figureOptions_la.addLayout(self.pw_figureOptions_vl_1[self.figure_option_num])
                self.pw_figureOptions_la.setAlignment(QtCore.Qt.AlignTop)
                self.populate_combobox(self.pw_figureOptions_cb_1[self.figure_option_num], self.font_list, False, self.default_font)
                self.populate_combobox(self.pw_figureOptions_cb_3[self.figure_option_num], self.font_list, False, self.default_font)
                self.populate_combobox(self.pw_figureOptions_cb_5[self.figure_option_num], self.font_list, False, self.default_font)
                self.populate_combobox(self.pw_figureOptions_cb_2[self.figure_option_num], [str(x) for x in range(1,49,1)], False, 9)
                self.populate_combobox(self.pw_figureOptions_cb_4[self.figure_option_num], [str(x) for x in range(1,49,1)], False, 9)
                self.populate_combobox(self.pw_figureOptions_cb_6[self.figure_option_num], [str(x) for x in range(1,49,1)], False, 9)
                self.pw_figureOptions_ck_1[self.figure_option_num].stateChanged.connect(self.activate_grid_options(val, plot_type='timeseries'))
                if 'figure_instance' in self.figure_options:
                    subplot = self.figure_options['figure_instance'][self.figure_option_num]
                    self.pw_figureOptions_ln_2[self.figure_option_num].setText(subplot.axes.xaxis.get_label_text())
                    self.pw_figureOptions_ln_2[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_3[self.figure_option_num].setText(subplot.axes.yaxis.get_label_text())
                    self.pw_figureOptions_ln_3[self.figure_option_num].setCursorPosition(0)
                    xlim_up = subplot.axes.get_xlim()[1]
                    xlim_dn = subplot.axes.get_xlim()[0]
                    ylim_up = subplot.axes.get_ylim()[1]
                    ylim_dn = subplot.axes.get_ylim()[0]
                    xstep = subplot.axes.get_xticks()[1] - subplot.axes.get_xticks()[0]
                    ystep = subplot.axes.get_yticks()[1] - subplot.axes.get_yticks()[0]
                    self.pw_figureOptions_ln_4[self.figure_option_num].setText(str(xlim_dn))
                    self.pw_figureOptions_ln_4[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_5[self.figure_option_num].setText(str(xlim_up))
                    self.pw_figureOptions_ln_5[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_6[self.figure_option_num].setText(str(xstep))
                    self.pw_figureOptions_ln_6[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_7[self.figure_option_num].setText(str(ylim_dn))
                    self.pw_figureOptions_ln_7[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_8[self.figure_option_num].setText(str(ylim_up))
                    self.pw_figureOptions_ln_8[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_9[self.figure_option_num].setText(str(ystep))
                    self.pw_figureOptions_ln_9[self.figure_option_num].setCursorPosition(0)
                else:
                    self.pw_figureOptions_ln_2[self.figure_option_num].setText(plt.axes().xaxis.get_label_text())
                    self.pw_figureOptions_ln_2[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_3[self.figure_option_num].setText(plt.axes().yaxis.get_label_text())
                    self.pw_figureOptions_ln_3[self.figure_option_num].setCursorPosition(0)
                    xlim_up = plt.axes().get_xlim()[1]
                    xlim_dn = plt.axes().get_xlim()[0]
                    ylim_up = plt.axes().get_ylim()[1]
                    ylim_dn = plt.axes().get_ylim()[0]
                    xstep = plt.axes().get_xticks()[1] - plt.axes().get_xticks()[0]
                    ystep = plt.axes().get_yticks()[1] - plt.axes().get_yticks()[0]
                    self.pw_figureOptions_ln_4[self.figure_option_num].setText(str(xlim_dn))
                    self.pw_figureOptions_ln_4[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_5[self.figure_option_num].setText(str(xlim_up))
                    self.pw_figureOptions_ln_5[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_6[self.figure_option_num].setText(str(xstep))
                    self.pw_figureOptions_ln_6[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_7[self.figure_option_num].setText(str(ylim_dn))
                    self.pw_figureOptions_ln_7[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_8[self.figure_option_num].setText(str(ylim_up))
                    self.pw_figureOptions_ln_8[self.figure_option_num].setCursorPosition(0)
                    self.pw_figureOptions_ln_9[self.figure_option_num].setText(str(ystep))
                    self.pw_figureOptions_ln_9[self.figure_option_num].setCursorPosition(0)
                self.figure_option_num +=1
        elif plot_type == 'grids':
            for _ in self.figure_options['title']:
                if self.figure_option_num == 0:
                    self.figure_options_sliders()
                
                self.pw_figureOptions_vl_1.append(QtWidgets.QVBoxLayout())
                self.pw_figureOptions_vl_1[self.figure_option_num].setObjectName("pw_figureOptions_vl_1_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_1.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_1[self.figure_option_num].setObjectName("pw_figureOptions_hl_1_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_1.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_1[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_1[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_1[self.figure_option_num].setFont(font2)
                if 'figure_instance' in self.figure_options:
                    text = 'Subplot ' + str(self.figure_option_num + 1) + ': Figure options'
                else:
                    text = 'Figure options:'
                self.pw_figureOptions_lb_1[self.figure_option_num].setText(text)     
                self.pw_figureOptions_lb_1[self.figure_option_num].setObjectName("pw_figureOptions_lb_1_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_1[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_hl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_1[self.figure_option_num])
                self.pw_figureOptions_hl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_1[self.figure_option_num])
                self.pw_figureOptions_hl_2.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_2[self.figure_option_num].setObjectName("pw_figureOptions_hl_2_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_gl_1.append(QtWidgets.QGridLayout())
                self.pw_figureOptions_gl_1[self.figure_option_num].setObjectName("pw_figureOptions_gl_1_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_2[self.figure_option_num].addLayout(self.pw_figureOptions_gl_1[self.figure_option_num])
                self.pw_figureOptions_lb_2.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_2[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_2[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_2[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_2[self.figure_option_num].setText("Figure title:")
                self.pw_figureOptions_lb_2[self.figure_option_num].setObjectName("pw_figureOptions_lb_2_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_2[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_2[self.figure_option_num], 0, 0, 1, 1)
                self.pw_figureOptions_ln_1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_ln_1[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_1[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_1[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_1[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_1[self.figure_option_num].setObjectName("pw_lineEdit_1_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_ln_1[self.figure_option_num], 0, 1, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 2, 1, 1)
                self.pw_figureOptions_lb_3.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_3[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_3[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_3[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_3[self.figure_option_num].setText("Font:")
                self.pw_figureOptions_lb_3[self.figure_option_num].setObjectName("pw_figureOptions_lb_3_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_3[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_3[self.figure_option_num], 0, 3, 1, 1)
                self.pw_figureOptions_cb_1.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_1[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_1[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_1[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_1[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_1[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_1[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_1[self.figure_option_num].setObjectName("pw_figureOptions_cb_1_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_1[self.figure_option_num], 0, 4, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 5, 1, 1)
                self.pw_figureOptions_lb_4.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_4[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_4[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_4[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_4[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_4[self.figure_option_num].setObjectName("pw_figureOptions_lb_4_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_4[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_4[self.figure_option_num], 0, 6, 1, 1)
                self.pw_figureOptions_cb_2.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_2[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_2[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_2[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_2[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_2[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_2[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_2[self.figure_option_num].setObjectName("pw_figureOptions_cb_2_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_2[self.figure_option_num], 0, 7, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 8, 1, 1)
                self.pw_figureOptions_lb_5.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_5[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_5[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_5[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_5[self.figure_option_num].setText("X axis label:")
                self.pw_figureOptions_lb_5[self.figure_option_num].setObjectName("pw_figureOptions_lb_5_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_5[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_5[self.figure_option_num], 1, 0, 1, 1)
                self.pw_figureOptions_ln_2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_ln_2[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_2[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_2[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_2[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_2[self.figure_option_num].setObjectName("pw_lineEdit_2_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_ln_2[self.figure_option_num], 1, 1, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
                self.pw_figureOptions_lb_6.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_6[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_6[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_6[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_6[self.figure_option_num].setText("Font:")
                self.pw_figureOptions_lb_6[self.figure_option_num].setObjectName("pw_figureOptions_lb_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_6[self.figure_option_num], 1, 3, 1, 1)
                self.pw_figureOptions_cb_3.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_3[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_3[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_3[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_3[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_3[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_3[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_3[self.figure_option_num].setObjectName("pw_figureOptions_cb_3_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_3[self.figure_option_num], 1, 4, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 1, 5, 1, 1)
                self.pw_figureOptions_lb_7.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_7[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_7[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_7[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_7[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_7[self.figure_option_num].setObjectName("pw_figureOptions_lb_7_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_7[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_7[self.figure_option_num], 1, 6, 1, 1)
                self.pw_figureOptions_cb_4.append(QtWidgets.QComboBox(self.scrollAreaWidgetContents_3))
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_4[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_4[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_4[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_4[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_4[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_4[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_4[self.figure_option_num].setObjectName("pw_figureOptions_cb_4_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_4[self.figure_option_num], 1, 7, 1, 1)
                self.pw_figureOptions_lb_8.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_lb_8[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_8[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_8[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_8[self.figure_option_num].setText("Y axis label:")
                self.pw_figureOptions_lb_8[self.figure_option_num].setObjectName("pw_figureOptions_lb_8_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_8[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_8[self.figure_option_num], 2, 0, 1, 1)
                self.pw_figureOptions_ln_3.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
                self.pw_figureOptions_ln_3[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_3[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
                self.pw_figureOptions_ln_3[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_3[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "   padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_3[self.figure_option_num].setObjectName("pw_lineEdit_3_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_ln_3[self.figure_option_num], 2, 1, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 2, 2, 1, 1)
                self.pw_figureOptions_lb_9.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_9[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_9[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_9[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_9[self.figure_option_num].setText("Font:")
                self.pw_figureOptions_lb_9[self.figure_option_num].setObjectName("pw_figureOptions_lb_9_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_9[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_9[self.figure_option_num], 2, 3, 1, 1)
                self.pw_figureOptions_cb_5.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_5[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_5[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_5[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
                self.pw_figureOptions_cb_5[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_5[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_5[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_5[self.figure_option_num].setObjectName("pw_figureOptions_cb_5_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_5[self.figure_option_num], 2, 4, 1, 1)
                self.pw_figureOptions_gl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 2, 5, 1, 1)
                self.pw_figureOptions_lb_10.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_10[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_10[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_10[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_10[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_10[self.figure_option_num].setObjectName("pw_figureOptions_lb_10_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_10[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_10[self.figure_option_num], 2, 6, 1, 1)
                self.pw_figureOptions_cb_6.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_6[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_6[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_6[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_cb_6[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_6[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_6[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_6[self.figure_option_num].setObjectName("pw_figureOptions_cb_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_cb_6[self.figure_option_num], 2, 7, 1, 1)
                self.pw_figureOptions_hl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_bt_1.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_1[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_1[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_1[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_1[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_1[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_1[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_1[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_1[self.figure_option_num].setObjectName("pw_figureOptions_bt_1_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_2[self.figure_option_num].addWidget(self.pw_figureOptions_bt_1[self.figure_option_num])
                self.pw_figureOptions_hl_2[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_2[self.figure_option_num])
                
                
                
                
                self.pw_figureOptions_hl_3.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_3[self.figure_option_num].setObjectName("pw_figureOptions_hl_3_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_3[self.figure_option_num])
                self.pw_figureOptions_lb_11.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_11[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_11[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.pw_figureOptions_lb_11[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_11[self.figure_option_num].setText("X/Y extension:")
                self.pw_figureOptions_lb_11[self.figure_option_num].setObjectName("pw_figureOptions_lb_11_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_11[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_hl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_11[self.figure_option_num])
                self.pw_figureOptions_hl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_gl_2.append(QtWidgets.QGridLayout())
                self.pw_figureOptions_gl_2[self.figure_option_num].setObjectName("pw_figureOptions_gl_2_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_3[self.figure_option_num].addLayout(self.pw_figureOptions_gl_2[self.figure_option_num])
                self.pw_figureOptions_lb_12.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_12[self.figure_option_num].setMinimumSize(QtCore.QSize(100, 27))
                self.pw_figureOptions_lb_12[self.figure_option_num].setMaximumSize(QtCore.QSize(100, 27))
                self.pw_figureOptions_lb_12[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_12[self.figure_option_num].setText("X min/max:")
                self.pw_figureOptions_lb_12[self.figure_option_num].setObjectName("pw_figureOptions_lb_12_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_12[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_lb_12[self.figure_option_num], 0, 0, 1, 1)
                self.pw_figureOptions_ln_4.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_4[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_4[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_4[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_4[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_4[self.figure_option_num].setObjectName("pw_figureOptions_ln_4_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_4[self.figure_option_num], 0, 1, 1, 1)
                self.pw_figureOptions_ln_5.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_5[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_5[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_5[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_5[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_5[self.figure_option_num].setObjectName("pw_figureOptions_ln_5_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_5[self.figure_option_num], 0, 2, 1, 1)
                self.pw_figureOptions_lb_13.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_13[self.figure_option_num].setMinimumSize(QtCore.QSize(100, 27))
                self.pw_figureOptions_lb_13[self.figure_option_num].setMaximumSize(QtCore.QSize(100, 27))
                self.pw_figureOptions_lb_13[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_13[self.figure_option_num].setText("Y min/max:")
                self.pw_figureOptions_lb_13[self.figure_option_num].setObjectName("pw_figureOptions_lb_13_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_13[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_lb_13[self.figure_option_num], 1, 0, 1, 1)
                self.pw_figureOptions_ln_6.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_6[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_6[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_6[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_6[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_ln_6[self.figure_option_num].setObjectName("pw_figureOptions_ln_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_6[self.figure_option_num], 1, 1, 1, 1)
                self.pw_figureOptions_ln_7.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_7[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_7[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
                self.pw_figureOptions_ln_7[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_7[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "   padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "}")
                self.pw_figureOptions_ln_7[self.figure_option_num].setObjectName("pw_figureOptions_ln_7_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_2[self.figure_option_num].addWidget(self.pw_figureOptions_ln_7[self.figure_option_num], 1, 2, 1, 1)
                self.pw_figureOptions_hl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_bt_2.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_2[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_2[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_2[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_2[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_2[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_2[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_2[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_2[self.figure_option_num].setObjectName("pw_figureOptions_bt_2_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_3[self.figure_option_num].addWidget(self.pw_figureOptions_bt_2[self.figure_option_num])
                self.pw_figureOptions_hl_3[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                
                
                
                
                
                self.pw_figureOptions_hl_4.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_4[self.figure_option_num].setObjectName("pw_figureOptions_hl_4_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_4[self.figure_option_num])
                self.pw_figureOptions_gl_3.append(QtWidgets.QGridLayout())
                self.pw_figureOptions_gl_3[self.figure_option_num].setObjectName("pw_figureOptions_gl_3_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_4[self.figure_option_num].addLayout(self.pw_figureOptions_gl_3[self.figure_option_num])
                
                self.pw_figureOptions_lb_14.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_14[self.figure_option_num].setMinimumSize(QtCore.QSize(120, 27))
                self.pw_figureOptions_lb_14[self.figure_option_num].setMaximumSize(QtCore.QSize(120, 27))
                self.pw_figureOptions_lb_14[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_14[self.figure_option_num].setText("X ticks/labels:")
                self.pw_figureOptions_lb_14[self.figure_option_num].setObjectName("pw_figureOptions_lb_14_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_14[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_14[self.figure_option_num], 0, 0, 1, 1)
                
                self.pw_figureOptions_lb_15.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_15[self.figure_option_num].setMinimumSize(QtCore.QSize(120, 27))
                self.pw_figureOptions_lb_15[self.figure_option_num].setMaximumSize(QtCore.QSize(120, 27))
                self.pw_figureOptions_lb_15[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_15[self.figure_option_num].setText("Y ticks/labels:")
                self.pw_figureOptions_lb_15[self.figure_option_num].setObjectName("pw_figureOptions_lb_15_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_15[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_15[self.figure_option_num], 1, 0, 1, 1)
                
                self.pw_figureOptions_bt_3.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_3[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_3[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_3[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_3[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_3[self.figure_option_num].setIcon(icon2)
                self.pw_figureOptions_bt_3[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_3[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_3[self.figure_option_num].setObjectName("pw_ticks_bt_1_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_bt_3[self.figure_option_num], 0, 1, 1, 1)
                
                self.pw_figureOptions_bt_4.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_4[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_4[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_4[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_4[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_4[self.figure_option_num].setIcon(icon2)
                self.pw_figureOptions_bt_4[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_4[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_4[self.figure_option_num].setObjectName("pw_ticks_bt_2_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_bt_4[self.figure_option_num], 1, 1, 1, 1)
                
                space1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(space1, 0, 2, 1, 1)
                
                space2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.pw_figureOptions_gl_3[self.figure_option_num].addItem(space2, 1, 2, 1, 1)
                
                self.pw_figureOptions_lb_16.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_16[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_16[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_16[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_16[self.figure_option_num].setText("")
                self.pw_figureOptions_lb_16[self.figure_option_num].setObjectName("pw_figureOptions_lb_16_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_16[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_16[self.figure_option_num], 0, 3, 1, 1)
                
                self.pw_figureOptions_lb_17.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_17[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_17[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_17[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_17[self.figure_option_num].setText("")
                self.pw_figureOptions_lb_17[self.figure_option_num].setObjectName("pw_figureOptions_lb_17_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_17[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_3[self.figure_option_num].addWidget(self.pw_figureOptions_lb_17[self.figure_option_num], 1, 3, 1, 1)
                self.pw_figureOptions_hl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                
                self.pw_figureOptions_bt_5.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_5[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_5[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_5[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_5[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_5[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_5[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_5[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_5[self.figure_option_num].setObjectName("pw_figureOptions_bt_5_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_4[self.figure_option_num].addWidget(self.pw_figureOptions_bt_5[self.figure_option_num])
                self.pw_figureOptions_hl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                
                
                
                
                
                
                self.pw_figureOptions_hl_5.append(QtWidgets.QHBoxLayout())
                self.pw_figureOptions_hl_5[self.figure_option_num].setObjectName("pw_figureOptions_hl_5_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_5[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_gl_4.append(QtWidgets.QGridLayout())
                self.pw_figureOptions_gl_4[self.figure_option_num].setObjectName("pw_figureOptions_gl_4_" + str(self.figure_option_num))
                self.pw_figureOptions_hl_5[self.figure_option_num].addLayout(self.pw_figureOptions_gl_4[self.figure_option_num])
                self.pw_figureOptions_lb_18.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_18[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_18[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_18[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_18[self.figure_option_num].setText("Display grid ?")
                self.pw_figureOptions_lb_18[self.figure_option_num].setObjectName("pw_figureOptions_lb_18_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_18[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_lb_18[self.figure_option_num], 0, 0, 1, 1)
                self.pw_figureOptions_ck_1.append(QtWidgets.QCheckBox())
                self.pw_figureOptions_ck_1[self.figure_option_num].setMinimumSize(QtCore.QSize(25, 20))
                self.pw_figureOptions_ck_1[self.figure_option_num].setMaximumSize(QtCore.QSize(25, 20))
                self.pw_figureOptions_ck_1[self.figure_option_num].setText("")
                self.pw_figureOptions_ck_1[self.figure_option_num].setObjectName("pw_figureOptions_ck_1_" + str(self.figure_option_num))
                self.pw_figureOptions_ck_1[self.figure_option_num].setStyleSheet("QCheckBox {\n"
                "    spacing: 5px;\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_ck_1[self.figure_option_num], 0, 1, 1, 1)
                self.pw_figureOptions_gl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 2, 1, 1)
                self.pw_figureOptions_lb_19.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_19[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_19[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_19[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_19[self.figure_option_num].setText("Style:")
                self.pw_figureOptions_lb_19[self.figure_option_num].setObjectName("pw_figureOptions_lb_19_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_lb_19[self.figure_option_num], 0, 3, 1, 1)
                self.pw_figureOptions_cb_7.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_7[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_7[self.figure_option_num].setEnabled(False)
                self.pw_figureOptions_cb_7[self.figure_option_num].setMinimumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_7[self.figure_option_num].setMaximumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_7[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_7[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_7[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_7[self.figure_option_num].setObjectName("pw_figureOptions_cb_7_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_cb_7[self.figure_option_num], 0, 4, 1, 1)
                self.pw_figureOptions_gl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 5, 1, 1)
                self.pw_figureOptions_lb_20.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_20[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_20[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_20[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_20[self.figure_option_num].setText("Size:")
                self.pw_figureOptions_lb_20[self.figure_option_num].setObjectName("pw_figureOptions_lb_20_" + str(self.figure_option_num))
                self.pw_figureOptions_lb_20[self.figure_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_lb_20[self.figure_option_num], 0, 6, 1, 1)
                self.pw_figureOptions_ln_8.append(QtWidgets.QLineEdit())
                self.pw_figureOptions_ln_8[self.figure_option_num].setEnabled(False)
                self.pw_figureOptions_ln_8[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_ln_8[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_figureOptions_ln_8[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_ln_8[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QLineEdit:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}")
                self.pw_figureOptions_ln_8[self.figure_option_num].setObjectName("pw_figureOptions_ln_8_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_ln_8[self.figure_option_num], 0, 7, 1, 1)
                self.pw_figureOptions_gl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 8, 1, 1)
                self.pw_figureOptions_lb_21.append(QtWidgets.QLabel())
                self.pw_figureOptions_lb_21[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
                self.pw_figureOptions_lb_21[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.pw_figureOptions_lb_21[self.figure_option_num].setFont(font)
                self.pw_figureOptions_lb_21[self.figure_option_num].setText("Color:")
                self.pw_figureOptions_lb_21[self.figure_option_num].setObjectName("pw_figureOptions_lb_21_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_lb_21[self.figure_option_num], 0, 9, 1, 1)
                self.pw_figureOptions_cb_8.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_figureOptions_cb_8[self.figure_option_num].setItemDelegate(itemDelegate)
                self.pw_figureOptions_cb_8[self.figure_option_num].setEnabled(False)
                self.pw_figureOptions_cb_8[self.figure_option_num].setMinimumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_8[self.figure_option_num].setMaximumSize(QtCore.QSize(160, 27))
                self.pw_figureOptions_cb_8[self.figure_option_num].setFont(font3)
                self.pw_figureOptions_cb_8[self.figure_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_figureOptions_cb_8[self.figure_option_num].setFrame(False)
                self.pw_figureOptions_cb_8[self.figure_option_num].setObjectName("pw_figureOptions_cb_8_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_cb_8[self.figure_option_num], 0, 10, 1, 1)
                self.pw_figureOptions_gl_4[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 11, 1, 1)
                self.pw_figureOptions_bt_6.append(QtWidgets.QToolButton())
                self.pw_figureOptions_bt_6[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_6[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_figureOptions_bt_6[self.figure_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_figureOptions_bt_6[self.figure_option_num].setText("")
                self.pw_figureOptions_bt_6[self.figure_option_num].setIcon(icon)
                self.pw_figureOptions_bt_6[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_figureOptions_bt_6[self.figure_option_num].setAutoRaise(False)
                self.pw_figureOptions_bt_6[self.figure_option_num].setObjectName("pw_figureOptions_bt_6_" + str(self.figure_option_num))
                self.pw_figureOptions_gl_4[self.figure_option_num].addWidget(self.pw_figureOptions_bt_6[self.figure_option_num], 0, 12, 1, 1)
                self.pw_figureOptions_hl_5[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_5[self.figure_option_num])
                
                
                
                
                
                
                
                
                
                
                self.pw_figureOptions_ln_2[self.figure_option_num].setText('Longitude')
                self.pw_figureOptions_ln_2[self.figure_option_num].setCursorPosition(0)
                self.pw_figureOptions_ln_3[self.figure_option_num].setText('Latitude')
                self.pw_figureOptions_ln_3[self.figure_option_num].setCursorPosition(0)
                
                
                
                self.pw_figureOptions_la.addLayout(self.pw_figureOptions_vl_1[self.figure_option_num])
                self.pw_figureOptions_la.setAlignment(QtCore.Qt.AlignTop)
                
                self.pw_figureOptions_bt_3[self.figure_option_num].clicked.connect(self.set_axis_ticks_labels)
                self.pw_figureOptions_bt_4[self.figure_option_num].clicked.connect(self.set_axis_ticks_labels)
                self.pw_figureOptions_ck_1[self.figure_option_num].stateChanged.connect(lambda val, plot_type='grids': self.activate_grid_options(val, plot_type))
                
                self.figure_option_num +=1
                
    
    def figure_options_sliders(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - figure_options_sliders')
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_commonOptions_hl_1 = QtWidgets.QHBoxLayout()
        self.pw_commonOptions_hl_1.setObjectName("pw_commonOptions_hl_1")
        self.pw_commonOptions_lb_1 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_commonOptions_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_1.setFont(font2)
        self.pw_commonOptions_lb_1.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_1.setObjectName("pw_commonOptions_lb_1")
        self.pw_commonOptions_hl_1.addWidget(self.pw_commonOptions_lb_1)
        spacerItem = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pw_commonOptions_hl_1.addItem(spacerItem)
        self.pw_figureOptions_la.addLayout(self.pw_commonOptions_hl_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pw_commonOptions_lb_2 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_2.setMinimumSize(QtCore.QSize(90, 0))
        self.pw_commonOptions_lb_2.setMaximumSize(QtCore.QSize(90, 16777215))
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_commonOptions_lb_2.setFont(font)
        self.pw_commonOptions_lb_2.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_2.setWordWrap(True)
        self.pw_commonOptions_lb_2.setObjectName("pw_commonOptions_lb_2")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_2, 0, 0, 2, 1)
        self.pw_commonOptions_lb_3 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_3.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_commonOptions_lb_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_3.setFont(font)
        self.pw_commonOptions_lb_3.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_3.setObjectName("pw_commonOptions_lb_3")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_3, 0, 1, 1, 1)
        self.pw_commonOptions_sl_1 = QtWidgets.QSlider()
        self.pw_commonOptions_sl_1.setMinimumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_1.setMaximumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_1.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 1px;\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "    margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "    border: 1px solid #5c5c5c;\n"
        "    width: 10px;\n"
        "    margin: -5px 0;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(0,0,200);\n"
        "}")
        self.pw_commonOptions_sl_1.setMinimum(0)
        self.pw_commonOptions_sl_1.setMaximum(40)
        self.pw_commonOptions_sl_1.setSingleStep(1)
        self.pw_commonOptions_sl_1.setPageStep(1)
        self.pw_commonOptions_sl_1.setOrientation(QtCore.Qt.Horizontal)
        self.pw_commonOptions_sl_1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_commonOptions_sl_1.setTickInterval(4)
        self.pw_commonOptions_sl_1.setObjectName("pw_commonOptions_sl_1")
        self.gridLayout_3.addWidget(self.pw_commonOptions_sl_1, 0, 2, 1, 1)
        self.pw_commonOptions_lb_5 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_5.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_5.setMaximumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_5.setFont(font3)
        self.pw_commonOptions_lb_5.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_5.setObjectName("slider_lb_1")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_5, 0, 3, 1, 1)
        self.pw_commonOptions_lb_7 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_7.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_commonOptions_lb_7.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_7.setFont(font)
        self.pw_commonOptions_lb_7.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_7.setObjectName("pw_commonOptions_lb_7")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_7, 0, 4, 1, 1)
        self.pw_commonOptions_sl_2 = QtWidgets.QSlider()
        self.pw_commonOptions_sl_2.setMinimumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_2.setMaximumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_2.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 1px;\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "    margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "    border: 1px solid #5c5c5c;\n"
        "    width: 10px;\n"
        "    margin: -5px 0;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "background: rgb(0,0,200);\n"
        "}")
        self.pw_commonOptions_sl_2.setMinimum(0)
        self.pw_commonOptions_sl_2.setMaximum(40)
        self.pw_commonOptions_sl_2.setSingleStep(1)
        self.pw_commonOptions_sl_2.setPageStep(1)
        self.pw_commonOptions_sl_2.setProperty("value", 0)
        self.pw_commonOptions_sl_2.setSliderPosition(0)
        self.pw_commonOptions_sl_2.setOrientation(QtCore.Qt.Horizontal)
        self.pw_commonOptions_sl_2.setInvertedAppearance(True)
        self.pw_commonOptions_sl_2.setInvertedControls(False)
        self.pw_commonOptions_sl_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_commonOptions_sl_2.setTickInterval(4)
        self.pw_commonOptions_sl_2.setObjectName("pw_commonOptions_sl_2")
        self.gridLayout_3.addWidget(self.pw_commonOptions_sl_2, 0, 5, 1, 1)
        self.pw_commonOptions_lb_9 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_9.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_9.setMaximumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_9.setFont(font3)
        self.pw_commonOptions_lb_9.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_9.setObjectName("slider_lb_2")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_9, 0, 6, 1, 1)
        self.pw_commonOptions_lb_11 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_11.setMinimumSize(QtCore.QSize(90, 0))
        self.pw_commonOptions_lb_11.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pw_commonOptions_lb_11.setFont(font)
        self.pw_commonOptions_lb_11.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_11.setWordWrap(True)
        self.pw_commonOptions_lb_11.setObjectName("pw_commonOptions_lb_11")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_11, 0, 7, 2, 1)
        self.pw_commonOptions_lb_14 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_14.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_commonOptions_lb_14.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_14.setFont(font)
        self.pw_commonOptions_lb_14.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_14.setObjectName("pw_commonOptions_lb_14")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_14, 1, 8, 1, 1)
        
        
        self.pw_commonOptions_lb_13 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_13.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_commonOptions_lb_13.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_13.setFont(font)
        self.pw_commonOptions_lb_13.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_13.setObjectName("pw_commonOptions_lb_13")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_13, 0, 8, 1, 1)
        self.pw_commonOptions_sl_5 = QtWidgets.QSlider()
        self.pw_commonOptions_sl_5.setMinimumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_5.setMaximumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_5.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 1px;\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "    margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "    border: 1px solid #5c5c5c;\n"
        "    width: 10px;\n"
        "    margin: -5px 0;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(0,0,200);\n"
        "}")
        self.pw_commonOptions_sl_5.setMinimum(1)
        self.pw_commonOptions_sl_5.setMaximum(100)
        self.pw_commonOptions_sl_5.setSingleStep(1)
        self.pw_commonOptions_sl_5.setPageStep(1)
        self.pw_commonOptions_sl_5.setOrientation(QtCore.Qt.Horizontal)
        self.pw_commonOptions_sl_5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_commonOptions_sl_5.setTickInterval(4)
        self.pw_commonOptions_sl_5.setObjectName("pw_commonOptions_sl_5")
        self.gridLayout_3.addWidget(self.pw_commonOptions_sl_5, 0, 9, 1, 1)
        self.pw_commonOptions_sl_6 = QtWidgets.QSlider()
        self.pw_commonOptions_sl_6.setMinimumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_6.setMaximumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_6.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 1px;\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "    margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "    border: 1px solid #5c5c5c;\n"
        "    width: 10px;\n"
        "    margin: -5px 0;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(0,0,200);\n"
        "}")
        self.pw_commonOptions_sl_6.setMinimum(0)
        self.pw_commonOptions_sl_6.setMaximum(100)
        self.pw_commonOptions_sl_6.setSingleStep(1)
        self.pw_commonOptions_sl_6.setPageStep(1)
        self.pw_commonOptions_sl_6.setOrientation(QtCore.Qt.Horizontal)
        self.pw_commonOptions_sl_6.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_commonOptions_sl_6.setTickInterval(4)
        self.pw_commonOptions_sl_6.setObjectName("pw_commonOptions_sl_6")
        self.gridLayout_3.addWidget(self.pw_commonOptions_sl_6, 1, 9, 1, 1)
        self.pw_commonOptions_lb_12 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_12.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_12.setMaximumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_12.setFont(font3)
        self.pw_commonOptions_lb_12.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_12.setObjectName("slider_lb_5")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_12, 0, 10, 1, 1)
        self.pw_commonOptions_lb_15 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_15.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_15.setMaximumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_15.setFont(font)
        self.pw_commonOptions_lb_15.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_15.setObjectName("slider_lb_6")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_15, 1, 10, 1, 1)
        self.pw_commonOptions_lb_4 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_commonOptions_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_4.setFont(font)
        self.pw_commonOptions_lb_4.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_4.setObjectName("pw_commonOptions_lb_4")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_4, 1, 1, 1, 1)
        self.pw_commonOptions_sl_3 = QtWidgets.QSlider()
        self.pw_commonOptions_sl_3.setMinimumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_3.setMaximumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_3.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 1px;\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "    margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "    border: 1px solid #5c5c5c;\n"
        "    width: 10px;\n"
        "    margin: -5px 0;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(0,0,200);\n"
        "}")
        self.pw_commonOptions_sl_3.setMinimum(0)
        self.pw_commonOptions_sl_3.setMaximum(40)
        self.pw_commonOptions_sl_3.setSingleStep(1)
        self.pw_commonOptions_sl_3.setPageStep(1)
        self.pw_commonOptions_sl_3.setOrientation(QtCore.Qt.Horizontal)
        self.pw_commonOptions_sl_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_commonOptions_sl_3.setTickInterval(4)
        self.pw_commonOptions_sl_3.setObjectName("pw_commonOptions_sl_3")
        self.gridLayout_3.addWidget(self.pw_commonOptions_sl_3, 1, 2, 1, 1)
        self.pw_commonOptions_lb_6 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_6.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_6.setFont(font3)
        self.pw_commonOptions_lb_6.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_6.setObjectName("slider_lb_3")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_6, 1, 3, 1, 1)
        self.pw_commonOptions_lb_8 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_8.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_commonOptions_lb_8.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pw_commonOptions_lb_8.setFont(font)
        self.pw_commonOptions_lb_8.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_8.setObjectName("pw_commonOptions_lb_8")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_8, 1, 4, 1, 1)
        self.pw_commonOptions_sl_4 = QtWidgets.QSlider()
        self.pw_commonOptions_sl_4.setMinimumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_4.setMaximumSize(QtCore.QSize(180, 27))
        self.pw_commonOptions_sl_4.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 1px;\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
        "    margin: 2px 0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
        "    border: 1px solid #5c5c5c;\n"
        "    width: 10px;\n"
        "    margin: -5px 0;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "background: rgb(0,0,200);\n"
        "}")
        self.pw_commonOptions_sl_4.setMinimum(0)
        self.pw_commonOptions_sl_4.setMaximum(40)
        self.pw_commonOptions_sl_4.setSingleStep(1)
        self.pw_commonOptions_sl_4.setPageStep(1)
        self.pw_commonOptions_sl_4.setProperty("value", 0)
        self.pw_commonOptions_sl_4.setOrientation(QtCore.Qt.Horizontal)
        self.pw_commonOptions_sl_4.setInvertedAppearance(True)
        self.pw_commonOptions_sl_4.setInvertedControls(False)
        self.pw_commonOptions_sl_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pw_commonOptions_sl_4.setTickInterval(4)
        self.pw_commonOptions_sl_4.setObjectName("pw_commonOptions_sl_4")
        self.gridLayout_3.addWidget(self.pw_commonOptions_sl_4, 1, 5, 1, 1)
        self.pw_commonOptions_lb_10 = QtWidgets.QLabel()
        self.pw_commonOptions_lb_10.setMinimumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_10.setMaximumSize(QtCore.QSize(50, 27))
        self.pw_commonOptions_lb_10.setFont(font3)
        self.pw_commonOptions_lb_10.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.pw_commonOptions_lb_10.setObjectName("slider_lb_4")
        self.gridLayout_3.addWidget(self.pw_commonOptions_lb_10, 1, 6, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.pw_commonOptions_bt_1 = QtWidgets.QToolButton()
        self.pw_commonOptions_bt_1.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_commonOptions_bt_1.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_commonOptions_bt_1.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.pw_commonOptions_bt_1.setIcon(icon)
        self.pw_commonOptions_bt_1.setIconSize(QtCore.QSize(23, 23))
        self.pw_commonOptions_bt_1.setObjectName("pw_commonOptions_bt_1")
        self.horizontalLayout_2.addWidget(self.pw_commonOptions_bt_1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pw_figureOptions_la.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.pw_figureOptions_la.addItem(spacerItem3)
        self.line = QtWidgets.QFrame()
        self.line.setStyleSheet("QFrame {\n"
        "    background: rgb(190,190,190);\n"
        "    height: 5px;\n"
        "    border: 0px solid black;\n"
        "}")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pw_figureOptions_la.addWidget(self.line)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.pw_figureOptions_la.addItem(spacerItem4)
        self.pw_commonOptions_lb_1.setText("Common options:")
        self.pw_commonOptions_lb_2.setText("Set figure margins:")
        self.pw_commonOptions_lb_3.setText("Left:")
        self.pw_commonOptions_lb_5.setText("TMP")
        self.pw_commonOptions_lb_7.setText("Right:")
        self.pw_commonOptions_lb_9.setText("TMP")
        self.pw_commonOptions_lb_11.setText("Set subplot interval:")
        self.pw_commonOptions_lb_12.setText("TMP")
        self.pw_commonOptions_lb_4.setText("Bottom:")
        self.pw_commonOptions_lb_6.setText("TMP")
        self.pw_commonOptions_lb_8.setText("Top:")
        self.pw_commonOptions_lb_10.setText("TMP")
        self.pw_commonOptions_lb_14.setText("Vertical:")
        self.pw_commonOptions_lb_13.setText("Horizontal:")
        self.pw_commonOptions_lb_15.setText("TMP")
        self.pw_commonOptions_sl_1.valueChanged.connect(self.update_slider_value)
        self.pw_commonOptions_sl_2.valueChanged.connect(self.update_slider_value)
        self.pw_commonOptions_sl_3.valueChanged.connect(self.update_slider_value)
        self.pw_commonOptions_sl_4.valueChanged.connect(self.update_slider_value)
        self.pw_commonOptions_sl_5.valueChanged.connect(self.update_slider_value)
        self.pw_commonOptions_sl_6.valueChanged.connect(self.update_slider_value)
        self.pw_commonOptions_sl_1.setSliderPosition(10)
        self.pw_commonOptions_sl_2.setSliderPosition(5)
        self.pw_commonOptions_sl_3.setSliderPosition(10)
        self.pw_commonOptions_sl_4.setSliderPosition(10)
        self.pw_commonOptions_sl_5.setSliderPosition(40)
        self.pw_commonOptions_sl_6.setSliderPosition(40)
        self.pw_commonOptions_sl_1.setValue(10)
        self.pw_commonOptions_sl_2.setValue(5)
        self.pw_commonOptions_sl_3.setValue(10)
        self.pw_commonOptions_sl_4.setValue(10)
        self.pw_commonOptions_sl_5.setValue(40)
        self.pw_commonOptions_sl_6.setValue(40)
        if 'figure_instance' not in self.figure_options:
            self.pw_commonOptions_lb_11.setVisible(False)
            self.pw_commonOptions_sl_5.setVisible(False)
            self.pw_commonOptions_lb_12.setVisible(False)
            self.pw_commonOptions_sl_6.setVisible(False)
            self.pw_commonOptions_lb_13.setVisible(False)
            self.pw_commonOptions_lb_14.setVisible(False)
            self.pw_commonOptions_lb_15.setVisible(False)
    
    def add_plot_options(self, plot_type):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_options')
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font3 = QtGui.QFont()
        font3.setFamily("fonts/SourceSansPro-Regular.ttf")
        font3.setPointSize(9)
        font3.setKerning(True)
        font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if plot_type == 'timeseries':
            for _ in self.plot_options['line_style']:
                self.pw_plotOptions_vl_1.append(QtWidgets.QVBoxLayout())
                self.pw_plotOptions_vl_1[self.plot_option_num].setObjectName("pw_plotOptions_vl_1_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_1.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_1[self.plot_option_num].setObjectName("pw_plotOptions_hl_1_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_1.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_1[self.plot_option_num].setMinimumSize(QtCore.QSize(700, 27))
                self.pw_plotOptions_lb_1[self.plot_option_num].setMaximumSize(QtCore.QSize(700, 27))
                self.pw_plotOptions_lb_1[self.plot_option_num].setFont(font2)
                
                if 'figure_instance' in self.plot_options:
                    text = 'Subplot ' + str(self.plot_option_num + 1) + ': Plot options - '
                else:
                    text = 'Plot options - '
                
                self.pw_plotOptions_lb_1[self.plot_option_num].setText(text + self.plot_options['legend_label'][self.plot_option_num] + ":")
                self.pw_plotOptions_lb_1[self.plot_option_num].setObjectName("pw_plotOptions_lb_1_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_1[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_1[self.plot_option_num].addWidget(self.pw_plotOptions_lb_1[self.plot_option_num])
                self.pw_plotOptions_hl_1[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_1[self.plot_option_num])
                self.pw_plotOptions_hl_2.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_2[self.plot_option_num].setObjectName("pw_plotOptions_hl_2_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_2[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_2.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_2[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_2[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_2[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_2[self.plot_option_num].setText("Line style:")
                self.pw_plotOptions_lb_2[self.plot_option_num].setObjectName("pw_plotOptions_lb_2_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_2[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_2[self.plot_option_num].addWidget(self.pw_plotOptions_lb_2[self.plot_option_num])
                self.pw_plotOptions_hl_3.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_3[self.plot_option_num].setObjectName("pw_plotOptions_hl_3_" + str(self.plot_option_num))
                self.pw_plotOptions_rb_1.append(QtWidgets.QRadioButton())
                self.pw_plotOptions_rb_1[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_rb_1[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_rb_1[self.plot_option_num].setFont(font)
                self.pw_plotOptions_rb_1[self.plot_option_num].setText("Line")
                self.pw_plotOptions_rb_1[self.plot_option_num].setObjectName("pw_plotOptions_rb_1_" + str(self.plot_option_num))
                self.pw_plotOptions_rb_1[self.plot_option_num].setStyleSheet("QRadioButton {\n"
                "    spacing: 5px;\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_hl_3[self.plot_option_num].addWidget(self.pw_plotOptions_rb_1[self.plot_option_num])
                self.pw_plotOptions_rb_2.append(QtWidgets.QRadioButton())
                self.pw_plotOptions_rb_2[self.plot_option_num].setMinimumSize(QtCore.QSize(90, 27))
                self.pw_plotOptions_rb_2[self.plot_option_num].setMaximumSize(QtCore.QSize(90, 27))
                self.pw_plotOptions_rb_2[self.plot_option_num].setFont(font)
                self.pw_plotOptions_rb_2[self.plot_option_num].setText("Marker")
                self.pw_plotOptions_rb_2[self.plot_option_num].setObjectName("pw_plotOptions_rb_2_" + str(self.plot_option_num))
                self.pw_plotOptions_rb_2[self.plot_option_num].setStyleSheet("QRadioButton {\n"
                "    spacing: 5px;\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_hl_3[self.plot_option_num].addWidget(self.pw_plotOptions_rb_2[self.plot_option_num])
                self.pw_plotOptions_bg_1.append(QtWidgets.QButtonGroup())
                self.pw_plotOptions_bg_1[self.plot_option_num].setObjectName("pw_plotOptions_bg_1_" + str(self.plot_option_num))
                self.pw_plotOptions_bg_1[self.plot_option_num].addButton(self.pw_plotOptions_rb_1[self.plot_option_num])
                self.pw_plotOptions_bg_1[self.plot_option_num].addButton(self.pw_plotOptions_rb_2[self.plot_option_num])
                self.pw_plotOptions_hl_2[self.plot_option_num].addLayout(self.pw_plotOptions_hl_3[self.plot_option_num])
                self.pw_plotOptions_cb_1.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_plotOptions_cb_1[self.plot_option_num].setItemDelegate(itemDelegate)
                self.pw_plotOptions_cb_1[self.plot_option_num].setMinimumSize(QtCore.QSize(180, 27))
                self.pw_plotOptions_cb_1[self.plot_option_num].setMaximumSize(QtCore.QSize(180, 27))
                self.pw_plotOptions_cb_1[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_cb_1[self.plot_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_plotOptions_cb_1[self.plot_option_num].setObjectName("pw_plotOptions_cb_1_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_2[self.plot_option_num].addWidget(self.pw_plotOptions_cb_1[self.plot_option_num])
                self.pw_plotOptions_hl_2[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_bt_1.append(QtWidgets.QToolButton())
                self.pw_plotOptions_bt_1[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_1[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_1[self.plot_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_plotOptions_bt_1[self.plot_option_num].setText("")
                self.pw_plotOptions_bt_1[self.plot_option_num].setIcon(icon)
                self.pw_plotOptions_bt_1[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_plotOptions_bt_1[self.plot_option_num].setAutoRaise(False)
                self.pw_plotOptions_bt_1[self.plot_option_num].setObjectName("pw_plotOptions_bt_1_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_2[self.plot_option_num].addWidget(self.pw_plotOptions_bt_1[self.plot_option_num])
                self.pw_plotOptions_hl_2[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_2[self.plot_option_num])
                self.pw_plotOptions_hl_4.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_4[self.plot_option_num].setObjectName("pw_plotOptions_hl_4_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_4[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_3.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_3[self.plot_option_num].setMinimumSize(QtCore.QSize(200, 27))
                self.pw_plotOptions_lb_3[self.plot_option_num].setMaximumSize(QtCore.QSize(200, 27))
                self.pw_plotOptions_lb_3[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_3[self.plot_option_num].setText("Line / Marker color:")
                self.pw_plotOptions_lb_3[self.plot_option_num].setObjectName("pw_plotOptions_lb_3_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_3[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_4[self.plot_option_num].addWidget(self.pw_plotOptions_lb_3[self.plot_option_num])
                self.pw_plotOptions_cb_2.append(QtWidgets.QComboBox())
                itemDelegate = QtWidgets.QStyledItemDelegate()
                self.pw_plotOptions_cb_2[self.plot_option_num].setItemDelegate(itemDelegate)
                self.pw_plotOptions_cb_2[self.plot_option_num].setMinimumSize(QtCore.QSize(170, 27))
                self.pw_plotOptions_cb_2[self.plot_option_num].setMaximumSize(QtCore.QSize(170, 27))
                self.pw_plotOptions_cb_2[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_cb_2[self.plot_option_num].setStyleSheet("QComboBox {\n"
                "    border: 1px solid #acacac;\n"
                "    border-radius: 1px;\n"
                "    padding-left: 5px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QComboBox:disabled {\n"
                "    background-color:  rgb(200,200,200);\n"
                "}\n"
                "\n"
                "QComboBox:hover {\n"
                "    border: 1px solid #7eb4ea;\n"
                "    border-radius: 1px;\n"
                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
                "}\n"
                "\n"
                "QComboBox::drop-down {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::drop-down:hover {\n"
                "    subcontrol-origin: padding;\n"
                "    subcontrol-position: top right;\n"
                "    width: 27px;\n"
                "    border-left-width: 1px;\n"
                "    border-left-color: darkgray;\n"
                "    border-left-style: solid;\n"
                "    border-top-right-radius: 3px;\n"
                "    border-bottom-right-radius: 3px;\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow {\n"
                "    image: url(icons/down_arrow_icon.svg); \n"
                "    width: 16px;\n"
                "    height: 16px\n"
                "}\n"
                "\n"
                "QComboBox::down-arrow:on {\n"
                "    top: 1px; \n"
                "    left: 1px;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: rgb(200,200,200);\n"
                "    selection-color: black;\n"
                "    background: #f0f0f0;\n"
                "    border: 0px solid #f0f0f0;\n"
                "}\n"
                "\n"
                "QComboBox QAbstractItemView::item {\n"
                "    margin: 5px 5px 5px 5px;\n"
                "}")
                self.pw_plotOptions_cb_2[self.plot_option_num].setObjectName("pw_plotOptions_cb_2_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_4[self.plot_option_num].addWidget(self.pw_plotOptions_cb_2[self.plot_option_num])
                self.pw_plotOptions_hl_5.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_5[self.plot_option_num].setObjectName("pw_plotOptions_hl_5_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_5[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_8.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_8[self.plot_option_num].setMinimumSize(QtCore.QSize(80, 27))
                self.pw_plotOptions_lb_8[self.plot_option_num].setMaximumSize(QtCore.QSize(80, 27))
                self.pw_plotOptions_lb_8[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_8[self.plot_option_num].setText("RGB code:")
                self.pw_plotOptions_lb_8[self.plot_option_num].setObjectName("pw_plotOptions_lb_8_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_8[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_lb_8[self.plot_option_num].hide()
                self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_lb_8[self.plot_option_num])
                self.pw_plotOptions_ln_3.append(QtWidgets.QLineEdit())
                self.pw_plotOptions_ln_3[self.plot_option_num].setMinimumSize(QtCore.QSize(130, 27))
                self.pw_plotOptions_ln_3[self.plot_option_num].setMaximumSize(QtCore.QSize(130, 27))
                self.pw_plotOptions_ln_3[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_ln_3[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_ln_3[self.plot_option_num].setObjectName("pw_plotOptions_ln_3_" + str(self.plot_option_num))
                self.pw_plotOptions_ln_3[self.plot_option_num].hide()
                self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_ln_3[self.plot_option_num])
                self.pw_plotOptions_ln_5.append(QtWidgets.QLineEdit())
                self.pw_plotOptions_ln_5[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_5[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_5[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_ln_5[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_ln_5[self.plot_option_num].setObjectName("pw_plotOptions_ln_5_" + str(self.plot_option_num))
                self.pw_plotOptions_ln_5[self.plot_option_num].hide()
                self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_ln_5[self.plot_option_num])
                self.pw_plotOptions_ln_6.append(QtWidgets.QLineEdit())
                self.pw_plotOptions_ln_6[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_6[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_6[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_ln_6[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_ln_6[self.plot_option_num].setObjectName("pw_plotOptions_ln_6_" + str(self.plot_option_num))
                self.pw_plotOptions_ln_6[self.plot_option_num].hide()
                self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_ln_6[self.plot_option_num])
                self.pw_plotOptions_hl_4[self.plot_option_num].addLayout(self.pw_plotOptions_hl_5[self.plot_option_num])
                self.pw_plotOptions_bt_2.append(QtWidgets.QToolButton())
                self.pw_plotOptions_bt_2[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_2[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_2[self.plot_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_plotOptions_bt_2[self.plot_option_num].setText("")
                self.pw_plotOptions_bt_2[self.plot_option_num].setIcon(icon)
                self.pw_plotOptions_bt_2[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_plotOptions_bt_2[self.plot_option_num].setAutoRaise(False)
                self.pw_plotOptions_bt_2[self.plot_option_num].setObjectName("pw_plotOptions_bt_2_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_4[self.plot_option_num].addWidget(self.pw_plotOptions_bt_2[self.plot_option_num])
                self.pw_plotOptions_hl_4[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_4[self.plot_option_num])
                self.pw_plotOptions_hl_6.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_6[self.plot_option_num].setObjectName("pw_plotOptions_hl_6_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_6[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_4.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_4[self.plot_option_num].setMinimumSize(QtCore.QSize(200, 27))
                self.pw_plotOptions_lb_4[self.plot_option_num].setMaximumSize(QtCore.QSize(200, 27))
                self.pw_plotOptions_lb_4[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_4[self.plot_option_num].setText("Line width / Marker size:")
                self.pw_plotOptions_lb_4[self.plot_option_num].setObjectName("pw_plotOptions_lb_4_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_4[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_6[self.plot_option_num].addWidget(self.pw_plotOptions_lb_4[self.plot_option_num])
                self.pw_plotOptions_ln_1.append(QtWidgets.QLineEdit())
                self.pw_plotOptions_ln_1[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_1[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_1[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_ln_1[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_ln_1[self.plot_option_num].setObjectName("pw_plotOptions_ln_1_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_6[self.plot_option_num].addWidget(self.pw_plotOptions_ln_1[self.plot_option_num])
                self.pw_plotOptions_hl_6[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_bt_3.append(QtWidgets.QToolButton())
                self.pw_plotOptions_bt_3[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_3[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_3[self.plot_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_plotOptions_bt_3[self.plot_option_num].setText("")
                self.pw_plotOptions_bt_3[self.plot_option_num].setIcon(icon)
                self.pw_plotOptions_bt_3[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_plotOptions_bt_3[self.plot_option_num].setAutoRaise(False)
                self.pw_plotOptions_bt_3[self.plot_option_num].setObjectName("pw_plotOptions_bt_3_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_6[self.plot_option_num].addWidget(self.pw_plotOptions_bt_3[self.plot_option_num])
                self.pw_plotOptions_hl_6[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_6[self.plot_option_num])
                self.pw_plotOptions_hl_7.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_7[self.plot_option_num].setObjectName("pw_plotOptions_hl_7_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_7[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_5.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_5[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_5[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_5[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_5[self.plot_option_num].setText("Antialiased ?")
                self.pw_plotOptions_lb_5[self.plot_option_num].setObjectName("pw_plotOptions_lb_5_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_5[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_7[self.plot_option_num].addWidget(self.pw_plotOptions_lb_5[self.plot_option_num])
                self.pw_plotOptions_ck_1.append(QtWidgets.QCheckBox())
                self.pw_plotOptions_ck_1[self.plot_option_num].setMinimumSize(QtCore.QSize(25, 20))
                self.pw_plotOptions_ck_1[self.plot_option_num].setMaximumSize(QtCore.QSize(25, 20))
                self.pw_plotOptions_ck_1[self.plot_option_num].setText("")
                self.pw_plotOptions_ck_1[self.plot_option_num].setObjectName("pw_plotOptions_ck_1_" + str(self.plot_option_num))
                self.pw_plotOptions_ck_1[self.plot_option_num].setStyleSheet("QCheckBox {\n"
                "    spacing: 5px;\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_hl_7[self.plot_option_num].addWidget(self.pw_plotOptions_ck_1[self.plot_option_num])
                self.pw_plotOptions_hl_7[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_bt_4.append(QtWidgets.QToolButton())
                self.pw_plotOptions_bt_4[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_4[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_4[self.plot_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_plotOptions_bt_4[self.plot_option_num].setText("")
                self.pw_plotOptions_bt_4[self.plot_option_num].setIcon(icon)
                self.pw_plotOptions_bt_4[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_plotOptions_bt_4[self.plot_option_num].setAutoRaise(False)
                self.pw_plotOptions_bt_4[self.plot_option_num].setObjectName("pw_plotOptions_bt_4_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_7[self.plot_option_num].addWidget(self.pw_plotOptions_bt_4[self.plot_option_num])
                self.pw_plotOptions_hl_7[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_7[self.plot_option_num])
                self.pw_plotOptions_hl_8.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_8[self.plot_option_num].setObjectName("pw_plotOptions_hl_8_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_6.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_6[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_6[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_6[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_6[self.plot_option_num].setText("Opacity ?")
                self.pw_plotOptions_lb_6[self.plot_option_num].setObjectName("pw_plotOptions_lb_6_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_6[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_lb_6[self.plot_option_num])
                self.pw_plotOptions_ck_2.append(QtWidgets.QCheckBox())
                self.pw_plotOptions_ck_2[self.plot_option_num].setMinimumSize(QtCore.QSize(25, 20))
                self.pw_plotOptions_ck_2[self.plot_option_num].setMaximumSize(QtCore.QSize(25, 20))
                self.pw_plotOptions_ck_2[self.plot_option_num].setText("")
                self.pw_plotOptions_ck_2[self.plot_option_num].setObjectName("pw_plotOptions_ck_2_" + str(self.plot_option_num))
                self.pw_plotOptions_ck_2[self.plot_option_num].setStyleSheet("QCheckBox {\n"
                "    spacing: 5px;\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_ck_2[self.plot_option_num])
                self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_7.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_7[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_7[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_7[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_7[self.plot_option_num].setText("Percentage:")
                self.pw_plotOptions_lb_7[self.plot_option_num].setObjectName("pw_plotOptions_lb_7_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_7[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_lb_7[self.plot_option_num])
                self.pw_plotOptions_ln_2.append(QtWidgets.QLineEdit())
                self.pw_plotOptions_ln_2[self.plot_option_num].setEnabled(False)
                self.pw_plotOptions_ln_2[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_2[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_2[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_ln_2[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}\n"
                "\n"
                "QLineEdit:disabled {\n"
                "    background-color:  rgb(180, 180, 180);\n"
                "}")
                self.pw_plotOptions_ln_2[self.plot_option_num].setObjectName("pw_plotOptions_ln_2_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_ln_2[self.plot_option_num])
                self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_bt_5.append(QtWidgets.QToolButton())
                self.pw_plotOptions_bt_5[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_5[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_5[self.plot_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_plotOptions_bt_5[self.plot_option_num].setText("")
                self.pw_plotOptions_bt_5[self.plot_option_num].setIcon(icon)
                self.pw_plotOptions_bt_5[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_plotOptions_bt_5[self.plot_option_num].setAutoRaise(False)
                self.pw_plotOptions_bt_5[self.plot_option_num].setObjectName("pw_plotOptions_bt_5_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_bt_5[self.plot_option_num])
                self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_8[self.plot_option_num])
                self.pw_plotOptions_hl_9.append(QtWidgets.QHBoxLayout())
                self.pw_plotOptions_hl_9[self.plot_option_num].setObjectName("pw_plotOptions_hl_9_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_9[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_lb_9.append(QtWidgets.QLabel())
                self.pw_plotOptions_lb_9[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_9[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
                self.pw_plotOptions_lb_9[self.plot_option_num].setFont(font)
                self.pw_plotOptions_lb_9[self.plot_option_num].setText("Legend:")
                self.pw_plotOptions_lb_9[self.plot_option_num].setObjectName("pw_plotOptions_lb_9_" + str(self.plot_option_num))
                self.pw_plotOptions_lb_9[self.plot_option_num].setStyleSheet("QLabel {color: rgb(45,45,45);}")
                self.pw_plotOptions_hl_9[self.plot_option_num].addWidget(self.pw_plotOptions_lb_9[self.plot_option_num])
                self.pw_plotOptions_ln_4.append(QtWidgets.QLineEdit())
                self.pw_plotOptions_ln_4[self.plot_option_num].setMinimumSize(QtCore.QSize(250, 27))
                self.pw_plotOptions_ln_4[self.plot_option_num].setMaximumSize(QtCore.QSize(250, 27))
                self.pw_plotOptions_ln_4[self.plot_option_num].setFont(font3)
                self.pw_plotOptions_ln_4[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                "    border-radius: 3px;\n"
                "    padding: 1px 4px 1px 4px;\n"
                "    background-color:  rgb(240, 240, 240);\n"
                "    color: rgb(45,45,45);\n"
                "}")
                self.pw_plotOptions_ln_4[self.plot_option_num].setObjectName("pw_plotOptions_ln_4_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_9[self.plot_option_num].addWidget(self.pw_plotOptions_ln_4[self.plot_option_num])
                self.pw_plotOptions_hl_9[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_bt_6.append(QtWidgets.QToolButton())
                self.pw_plotOptions_bt_6[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_6[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
                self.pw_plotOptions_bt_6[self.plot_option_num].setStyleSheet("QToolButton {\n"
                "    border: 1px solid transparent;\n"
                "    background-color: transparent;\n"
                "    width: 27px;\n"
                "    height: 27px;\n"
                "}\n"
                "\n"
                "QToolButton:flat {\n"
                "    border: none;\n"
                "}")
                self.pw_plotOptions_bt_6[self.plot_option_num].setText("")
                self.pw_plotOptions_bt_6[self.plot_option_num].setIcon(icon)
                self.pw_plotOptions_bt_6[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
                self.pw_plotOptions_bt_6[self.plot_option_num].setAutoRaise(False)
                self.pw_plotOptions_bt_6[self.plot_option_num].setObjectName("pw_plotOptions_bt_6_" + str(self.plot_option_num))
                self.pw_plotOptions_hl_9[self.plot_option_num].addWidget(self.pw_plotOptions_bt_6[self.plot_option_num])
                self.pw_plotOptions_hl_9[self.plot_option_num].addItem(QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_9[self.plot_option_num])
                self.pw_plotOptions_vl_1[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
                self.pw_plotOptions_li_1.append(QtWidgets.QFrame())
                self.pw_plotOptions_li_1[self.plot_option_num].setFrameShape(QtWidgets.QFrame.HLine)
                self.pw_plotOptions_li_1[self.plot_option_num].setFrameShadow(QtWidgets.QFrame.Sunken)
                self.pw_plotOptions_li_1[self.plot_option_num].setStyleSheet("QFrame {\n"
                "    background: rgb(190,190,190);\n"
                "    height: 5px;\n"
                "    border: 0px solid black;\n"
                "}")
                self.pw_plotOptions_li_1[self.plot_option_num].setObjectName("pw_plotOptions_li_1_" + str(self.plot_option_num))
                self.pw_plotOptions_vl_1[self.plot_option_num].addWidget(self.pw_plotOptions_li_1[self.plot_option_num])
                self.pw_plotOptions_vl_1[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
                self.pw_plotOptions_la.addLayout(self.pw_plotOptions_vl_1[self.plot_option_num])
                self.pw_plotOptions_la.setAlignment(QtCore.Qt.AlignTop)
                self.pw_plotOptions_cb_2[self.plot_option_num].currentIndexChanged.connect(self.activate_line_color)
                if self.plot_options['line_color'][self.plot_option_num] in self.colors:
                    item = self.plot_options['line_color'][self.plot_option_num]
                else:
                    if '#' in self.plot_options['line_color'][self.plot_option_num]:
                        item = 'HEX Color'
                    else:
                        item = 'RGB Color'
                self.populate_combobox(self.pw_plotOptions_cb_2[self.plot_option_num], self.colors, False, item)
                self.pw_plotOptions_ln_3[self.plot_option_num].setText(str(self.plot_options['line_color'][self.plot_option_num]))
                self.pw_plotOptions_ck_2[self.plot_option_num].stateChanged.connect(self.activate_opacity_options)
                self.pw_plotOptions_bg_1[self.plot_option_num].buttonClicked.connect(self.activate_line_style)
                self.pw_plotOptions_rb_1[self.plot_option_num].click() 
                self.pw_plotOptions_ln_1[self.plot_option_num].setText(str(self.plot_options['line_width'][self.plot_option_num]))
                self.pw_plotOptions_ck_1[self.plot_option_num].setChecked(self.plot_options['line_antialiased'][self.plot_option_num])
                self.pw_plotOptions_ck_2[self.plot_option_num].setChecked(self.plot_options['line_alpha'][self.plot_option_num])
                self.pw_plotOptions_ln_4[self.plot_option_num].setText(self.plot_options['legend_label'][self.plot_option_num])
                self.plot_option_num +=1
    
        elif plot_type == 'grids':
            pass
    
    
    
    def update_figure_options(self, plot_type):
        logging.debug('gui - plot_window_functions.py - PlotWindow - update_figure_options')
        if plot_type == 'timeseries':
            figure_options = {}
            figure_options['figure_instance'] = []
            figure_options['title'] = []
            figure_options['title_font'] = []
            figure_options['title_size'] = []
            figure_options['xlabel'] = []
            figure_options['xlabel_font'] = []
            figure_options['xlabel_size'] = []
            figure_options['ylabel'] = []
            figure_options['ylabel_font'] = []
            figure_options['ylabel_size'] = []
            figure_options['spine_top'] = []
            figure_options['spine_right'] = []
            figure_options['margin_left'] = []
            figure_options['margin_right'] = []
            figure_options['margin_bottom'] = []
            figure_options['margin_top'] = []
            figure_options['horizontal_space'] = []
            figure_options['vertical_space'] = []
            figure_options['grid'] = []
            figure_options['grid_style'] = []
            figure_options['grid_size'] = []
            figure_options['grid_color'] = []
            figure_options['display_legend'] = []
            figure_options['xlim_max'] = []
            figure_options['xlim_min'] = []
            figure_options['ylim_max'] = []
            figure_options['ylim_min'] = []
            figure_options['xlim_step'] = []
            figure_options['ylim_step'] = []
            figure_options['xticks'] = []
            figure_options['yticks'] = []
            for i in range(self.figure_option_num):
                figure_options['title'].append(str(self.pw_figureOptions_ln_1[i].text()))
                figure_options['title_font'].append(str(self.pw_figureOptions_cb_1[i].currentText()))
                figure_options['title_size'].append(int(self.pw_figureOptions_cb_2[i].currentText()))
                figure_options['xlabel'].append(str(self.pw_figureOptions_ln_2[i].text()))
                figure_options['xlabel_font'].append(str(self.pw_figureOptions_cb_3[i].currentText()))
                figure_options['xlabel_size'].append(int(self.pw_figureOptions_cb_4[i].currentText()))
                figure_options['ylabel'].append(str(self.pw_figureOptions_ln_3[i].text()))
                figure_options['ylabel_font'].append(str(self.pw_figureOptions_cb_5[i].currentText()))
                figure_options['ylabel_size'].append(int(self.pw_figureOptions_cb_6[i].currentText()))
                try:
                    figure_options['xlim_step'].append(float(self.pw_figureOptions_ln_6[i].text()))
                except ValueError:
                    figure_options['xlim_step'].append('')
                try:
                    figure_options['xlim_max'].append(float(self.pw_figureOptions_ln_5[i].text()))
                except ValueError:
                    figure_options['xlim_max'].append('')
                try:
                    figure_options['xlim_min'].append(float(self.pw_figureOptions_ln_4[i].text()))
                except ValueError:
                    figure_options['xlim_min'].append('')
                try:
                    figure_options['xticks'].append(numpy.arange(figure_options['xlim_min'][i] - figure_options['xlim_step'][i] * 10,
                                                            figure_options['xlim_max'][i] + figure_options['xlim_step'][i] * 10,
                                                            figure_options['xlim_step'][i]))
                except (ValueError, TypeError):
                    figure_options['xticks'].append('')
                try:
                    figure_options['ylim_step'].append(float(self.pw_figureOptions_ln_9[i].text()))
                except ValueError:
                    figure_options['ylim_step'].append('')
                try:
                    figure_options['ylim_max'].append(float(self.pw_figureOptions_ln_8[i].text()))
                except ValueError:
                    figure_options['ylim_max'].append('')
                try:
                    figure_options['ylim_min'].append(float(self.pw_figureOptions_ln_7[i].text()))
                except ValueError:
                    figure_options['ylim_min'].append('')
                try:
                    figure_options['yticks'].append(numpy.arange(figure_options['ylim_min'][i] - figure_options['ylim_step'][i] * 10,
                                                            figure_options['ylim_max'][i] + figure_options['ylim_step'][i] * 10,
                                                            figure_options['ylim_step'][i]))
                except (ValueError, TypeError):
                    figure_options['yticks'].append('')
                if self.pw_figureOptions_ck_1[i].isChecked():
                    figure_options['grid'].append(True)
                    figure_options['grid_style'].append(self.line_styles_dict[str(self.pw_figureOptions_cb_9[i].currentText())])
                    figure_options['grid_size'].append(float(self.pw_figureOptions_ln_10[i].text()))
                    figure_options['grid_color'].append(self.colors_dict[str(self.pw_figureOptions_cb_10[i].currentText())])
                else:
                    figure_options['grid'].append(False)
                    figure_options['grid_style'].append('')
                    figure_options['grid_size'].append('')
                    figure_options['grid_color'].append('')
                figure_options['display_legend'].append(self.pw_figureOptions_ck_2[i].isChecked())
            figure_options['margin_left'].append(float(self.pw_commonOptions_lb_5.text()))
            figure_options['margin_right'].append(1 - float(self.pw_commonOptions_lb_9.text()))
            figure_options['margin_bottom'].append(float(self.pw_commonOptions_lb_10.text()))
            figure_options['margin_top'].append(1 - float(self.pw_commonOptions_lb_6.text()))
            if 'figure_instance' in self.figure_options:
                figure_options['horizontal_space'].append(None)
                figure_options['vertical_space'].append(float(self.pw_figureOptions_lb_30[0].text()))
            else:
                figure_options['horizontal_space'].append(None)
                figure_options['vertical_space'].append(None)
            for i in range(self.figure_option_num):
                if figure_options['title'][i]:
                    if (figure_options['title'][i] != self.figure_options['title'][i] or 
                        figure_options['title_font'][i] != self.figure_options['title_font'][i] or 
                        figure_options['title_size'][i] != self.figure_options['title_size'][i]):
                        self.figure_options['title'][i] = figure_options['title'][i]
                        self.figure_options['title_font'][i] = figure_options['title_font'][i]
                        self.figure_options['title_size'][i] = figure_options['title_size'][i]
                        font = {'fontname': figure_options['title_font'][i], 'fontsize': figure_options['title_size'][i]}
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].set_title(figure_options['title'][i], **font)
                        else:
                            plt.title(figure_options['title'][i], y=1.04, **font)
                if figure_options['xlabel'][i]:
                    if (figure_options['xlabel'][i] != self.figure_options['xlabel'][i] or 
                        figure_options['xlabel_font'][i] != self.figure_options['xlabel_font'][i] or 
                        figure_options['xlabel_size'][i] != self.figure_options['xlabel_size'][i]):
                        self.figure_options['xlabel'][i] = figure_options['xlabel'][i]
                        self.figure_options['xlabel_font'][i] = figure_options['xlabel_font'][i]
                        self.figure_options['xlabel_size'][i] = figure_options['xlabel_size'][i]
                        font = {'fontname': figure_options['xlabel_font'][i], 'fontsize': figure_options['xlabel_size'][i]}
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].set_xlabel(figure_options['xlabel'][i], **font)
                        else:
                            plt.xlabel(figure_options['xlabel'][i], **font) 
                if figure_options['ylabel'][i]:
                    if (figure_options['ylabel'][i] != self.figure_options['ylabel'][i] or 
                        figure_options['ylabel_font'][i] != self.figure_options['ylabel_font'][i] or 
                        figure_options['ylabel_size'][i] != self.figure_options['ylabel_size'][i]):
                        self.figure_options['ylabel'][i] = figure_options['ylabel'][i]
                        self.figure_options['ylabel_font'][i] = figure_options['ylabel_font'][i]
                        self.figure_options['ylabel_size'][i] = figure_options['ylabel_size'][i]
                        font = {'fontname': figure_options['ylabel_font'][i], 'fontsize': figure_options['ylabel_size'][i]}
                        
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].set_ylabel(figure_options['ylabel'][i], **font)
                        else:
                            plt.ylabel(figure_options['ylabel'][i], **font)
                if isinstance(figure_options['xticks'][i], numpy.ndarray):
                    if not numpy.array_equal(figure_options['xticks'][i], self.figure_options['xticks'][i]):
                        self.figure_options['xlim_step'][i] =figure_options['xlim_step'][i]
                        self.figure_options['xlim_max'][i] = figure_options['xlim_max'][i]
                        self.figure_options['xlim_min'][i] = figure_options['xlim_min'][i]
                        self.figure_options['xticks'][i] = figure_options['xticks'][i]
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].set_xticks(figure_options['xticks'][i])
                            self.figure_options['figure_instance'][i].set_xlim([figure_options['xlim_min'][i], figure_options['xlim_max'][i]])
                        else:
                            plt.xticks(figure_options['xticks'][i])
                            plt.xlim([figure_options['xlim_min'][i], figure_options['xlim_max'][i]])
                if isinstance(figure_options['yticks'][i], numpy.ndarray):
                    if not numpy.array_equal(figure_options['yticks'][i], self.figure_options['yticks'][i]):
                        self.figure_options['ylim_step'][i] =figure_options['ylim_step'][i]
                        self.figure_options['ylim_max'][i] = figure_options['ylim_max'][i]
                        self.figure_options['ylim_min'][i] = figure_options['ylim_min'][i]
                        self.figure_options['yticks'][i] = figure_options['yticks'][i]
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].set_yticks(figure_options['yticks'][i])
                            self.figure_options['figure_instance'][i].set_ylim([figure_options['ylim_min'][i], figure_options['ylim_max'][i]])
                        else:
                            plt.yticks(figure_options['yticks'][i])
                            plt.ylim([figure_options['ylim_min'][i], figure_options['ylim_max'][i]])
                if figure_options['grid'][i]:
                    if (figure_options['grid'][i] != self.figure_options['grid'][i] or
                        self.figure_options['grid_style'][i] != figure_options['grid_style'][i] or
                        self.figure_options['grid_size'][i] != figure_options['grid_size'][i] or
                        self.figure_options['grid_color'][i] != figure_options['grid_color'][i]):
                        self.figure_options['grid'][i] = figure_options['grid'][i]
                        self.figure_options['grid_style'][i] = figure_options['grid_style'][i]
                        self.figure_options['grid_size'][i] = figure_options['grid_size'][i]
                        self.figure_options['grid_color'][i] = figure_options['grid_color'][i]
                        args = {'linestyle': figure_options['grid_style'][i],
                                'linewidth': figure_options['grid_size'][i],
                                'color': figure_options['grid_color'][i]}
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].grid(b=True, **args)
                        else:
                            plt.grid(b=True, **args)        
                elif not figure_options['grid'][i] and figure_options['grid'][i] != self.figure_options['grid'][i]:
                    self.figure_options['grid'][i] = figure_options['grid'][i]
                    if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].grid(b=False)
                    else:
                        plt.grid(b=False)  
                if figure_options['display_legend'][i]:
                    if figure_options['display_legend'][i] != self.figure_options['display_legend'][i]:
                        self.figure_options['display_legend'][i] = figure_options['display_legend'][i]
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].legend(prop={'family':self.default_font, 'size':'10'})
                            self.figure_options['figure_instance'][i].set_visible(True)
                            self.figure_options['figure_instance'][i].draggable()
                        else:
                            plt.gca().legend(prop={'family':self.default_font, 'size':'10'})
                            plt.gca().legend().set_visible(True)
                            plt.gca().legend().draggable()
                else:
                    if figure_options['display_legend'][i] != self.figure_options['display_legend'][i]:
                        self.figure_options['display_legend'][i] = figure_options['display_legend'][i]
                        
                        if 'figure_instance' in self.figure_options:
                            self.figure_options['figure_instance'][i].set_visible(True)
                        else:
                            plt.gca().legend().set_visible(False)
            margin_left, margin_right, margin_bottom, margin_top, wspace, hspace = None, None, None, None, None, None
            if figure_options['margin_left'][0] != self.figure_options['margin_left'][0]:
                self.figure_options['margin_left'][0], margin_left = figure_options['margin_left'][0], figure_options['margin_left'][0]
            if figure_options['margin_right'][0] != self.figure_options['margin_right'][0]:
                self.figure_options['margin_right'][0], margin_right = figure_options['margin_right'][0], figure_options['margin_right'][0]
            if figure_options['margin_bottom'][0] != self.figure_options['margin_bottom'][0]:
                self.figure_options['margin_bottom'][0], margin_bottom = figure_options['margin_bottom'][0], figure_options['margin_bottom'][0]
            if figure_options['margin_top'][0] != self.figure_options['margin_top'][0]:
                self.figure_options['margin_top'][0], margin_top = figure_options['margin_top'][0], figure_options['margin_top'][0]
            if figure_options['vertical_space'][0] != self.figure_options['vertical_space'][0]:
                self.figure_options['vertical_space'][0], hspace = figure_options['vertical_space'][0], figure_options['vertical_space'][0]
            if figure_options['horizontal_space'][0] != self.figure_options['horizontal_space'][0]:
                self.figure_options['horizontal_space'][0], wspace = figure_options['horizontal_space'][0], figure_options['horizontal_space'][0]
            plt.subplots_adjust(left=margin_left, right=margin_right, bottom=margin_bottom, top=margin_top, wspace=wspace, hspace=hspace)
            self.canvas.draw()
    
    def update_plot_options(self, plot_type):
        if plot_type == 'timeseries':
            plot_options = {}
            plot_options['line_style'] = []
            plot_options['line_marker'] = []
            plot_options['line_color'] = []
            plot_options['line_width'] = []
            plot_options['line_antialiased'] = []
            plot_options['line_alpha'] = []
            plot_options['line_alpha_perc'] = []
            plot_options['legend_label'] = []
            for i in range(self.plot_option_num):
                try:
                    plot_options['line_style'].append(self.line_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())])
                    plot_options['line_marker'].append('line')
                except KeyError:
                    plot_options['line_style'].append(self.marker_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())])
                    plot_options['line_marker'].append('marker')
                if str(self.pw_plotOptions_cb_2[i].currentText()) == 'HEX Color':
                    if '#' not in str(self.pw_plotOptions_ln_3[i].text()):
                        plot_options['line_color'].append('#' + str(self.pw_plotOptions_ln_3[i].text()))
                    else:
                        plot_options['line_color'].append(str(self.pw_plotOptions_ln_3[i].text()))
                elif str(self.pw_plotOptions_cb_2[i].currentText()) == 'RGB Color':
                    r = float(self.pw_plotOptions_ln_3[i].text()) / 255.
                    g = float(self.pw_plotOptions_ln_5[i].text()) / 255.
                    b = float(self.pw_plotOptions_ln_6[i].text()) / 255.
                    plot_options['line_color'].append((r, g, b))
                else:
                    plot_options['line_color'].append(self.colors_dict[str(self.pw_plotOptions_cb_2[i].currentText())])
                plot_options['line_width'].append(float(self.pw_plotOptions_ln_1[i].text()))
                plot_options['line_antialiased'].append(self.pw_plotOptions_ck_1[i].isChecked())
                plot_options['line_alpha'].append(self.pw_plotOptions_ck_2[i].isChecked())
                if plot_options['line_alpha'][i]:
                    if ' %' in self.pw_plotOptions_ln_2[i].text():
                        plot_options['line_alpha_perc'].append(float(self.pw_plotOptions_ln_2[i].text()[:-2]))
                    elif '%' in self.pw_plotOptions_ln_2[i].text():
                        plot_options['line_alpha_perc'].append(float(self.pw_plotOptions_ln_2[i].text()[:-1]))
                    else:
                        plot_options['line_alpha_perc'].append(float(self.pw_plotOptions_ln_2[i].text()))
                plot_options['legend_label'].append(str(self.pw_plotOptions_ln_4[i].text()))
            for i in range(self.plot_option_num):
                if plot_options['line_style'][i] != self.plot_options['line_style'][i]:
                    self.plot_options['line_style'][i] = plot_options['line_style'][i]
                    self.plot_options['line_marker'][i] = plot_options['line_marker'][i]
                    if plot_options['line_marker'][i] == 'line':
                        if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_linestyle(plot_options['line_style'])
                            self.plot_options['figure_instance'][i].axes.lines[0].set_marker(None)
                        else:
                            plt.axes().lines[i].set_linestyle(plot_options['line_style'])
                            plt.axes().lines[i].set_marker(None)
                    else:
                        if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_linestyle('None')
                            self.plot_options['figure_instance'][i].axes.lines[0].set_marker(plot_options['line_style'][i])
                        else:
                            plt.axes().lines[i].set_linestyle('None')
                            plt.axes().lines[i].set_marker(plot_options['line_style'][i])
                if plot_options['line_color'][i] != self.plot_options['line_color'][i]:
                    self.plot_options['line_color'][i] = plot_options['line_color'][i]
                    if 'figure_instance' in self.plot_options:
                        self.plot_options['figure_instance'][i].axes.lines[0].set_color(plot_options['line_color'][i])
                    else:
                        plt.axes().lines[i].set_color(plot_options['line_color'][i])
                    if self.figure_options['display_legend'][i]:
                        if 'figure_instance' in self.plot_options:
                            leg = self.plot_options['figure_instance'][i].legend(prop={'family':self.default_font, 'size':'10'})  
                            leg.draggable()
                        else:
                            plt.gca().legend().draggable()
                if plot_options['line_width'][i] != self.plot_options['line_width'][i]:
                    self.plot_options['line_width'][i] = plot_options['line_width'][i]
                    if plot_options['line_marker'][i] == 'line':
                        if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_linewidth(plot_options['line_width'][i])
                        else:
                            plt.axes().lines[i].set_linewidth(plot_options['line_width'][i])
                    else:
                        if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_markersize(plot_options['line_width'][i])
                        else:
                            plt.axes().lines[i].set_markersize(plot_options['line_width'][i])
                if plot_options['line_antialiased'][i] != self.plot_options['line_antialiased'][i]:
                    self.plot_options['line_antialiased'][i] = plot_options['line_antialiased'][i]
                    if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_antialiased(plot_options['line_antialiased'][i])
                    else:
                        plt.axes().lines[i].set_antialiased(plot_options['line_antialiased'][i])
                if plot_options['line_alpha'][i]:
                    if plot_options['line_alpha'][i] != self.plot_options['line_alpha'][i] or plot_options['line_alpha_perc'][i] != self.plot_options['line_alpha_perc'][i]:
                        self.plot_options['line_alpha'][i] = plot_options['line_alpha'][i]
                        self.plot_options['line_alpha_perc'][i] = plot_options['line_alpha_perc'][i]
                        if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_alpha(float(plot_options['line_alpha_perc'][i]) / 100.)
                        else:
                            plt.axes().lines[i].set_alpha(float(plot_options['line_alpha_perc'][i]) / 100.)
                else:
                    if plot_options['line_alpha'][i] != self.plot_options['line_alpha'][i]:
                        self.plot_options['line_alpha'][i] = plot_options['line_alpha'][i]
                        if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_alpha(1)
                        else:
                            plt.axes().lines[i].set_alpha(1)
                if plot_options['legend_label'][i] != self.plot_options['legend_label'][i]:
                    self.plot_options['legend_label'][i] = plot_options['legend_label'][i]
                    if 'figure_instance' in self.plot_options:
                            self.plot_options['figure_instance'][i].axes.lines[0].set_label(str(plot_options['legend_label'][i]))
                    else:
                        plt.axes().lines[i].set_label(str(plot_options['legend_label'][i]))
                    if self.figure_options['display_legend'][i]:
                        if 'figure_instance' in self.plot_options:
                            leg = self.plot_options['figure_instance'][i].legend(prop={'family':self.default_font, 'size':'10'})  
                            leg.draggable()
                        else:
                            plt.gca().legend().draggable()
        self.canvas.draw()
    
    def plot_pan(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_pan: actionPan.objectName() '
                      + str(self.actionPan.objectName()))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon)
        self.actionZoom.setObjectName("actionZoom")
        if "activated" in self.actionPan.objectName():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/pan_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPan.setIcon(icon)
            self.actionPan.setObjectName("actionPan")
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/pan_icon_activated.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPan.setIcon(icon)
            self.actionPan.setObjectName("activated_actionPan")
        self.navigation_toolbar.pan()
        
    def plot_zoom(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_zoom : actionZoom.objectName() '
                      + str(self.actionZoom.objectName()))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/pan_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon)
        self.actionPan.setObjectName("actionPan")
        if "activated" in self.actionZoom.objectName():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionZoom.setIcon(icon)
            self.actionZoom.setObjectName("actionZoom")
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/zoom_icon_activated.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionZoom.setIcon(icon)
            self.actionZoom.setObjectName("activated_actionZoom")
        self.navigation_toolbar.zoom()
        
    def plot_home(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_home')
        self.navigation_toolbar.home()
    
    def plot_save(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_save')
        save_file_name, save_file_ext = self.get_file_name()
        if save_file_name:
            _, out_file_ext = ntpath.splitext(ntpath.basename(save_file_name))
            if not out_file_ext:
                save_file_name += self.image_extensions[save_file_ext]
            _, out_file_ext = ntpath.splitext(ntpath.basename(save_file_name))
            real_width, real_height = plt.gcf().get_size_inches()
            set_height, set_width = None, None
            if self.pw_saveOptions_ln_1.text():
                set_height = float(self.pw_saveOptions_ln_1.text())
                if self.pw_saveOptions_cb_1.currentText() == 'Centimeters':
                    set_height = round((set_height / 2.54) * 100) / 100
            if self.pw_saveOptions_ln_2.text():
                set_width = float(self.pw_saveOptions_ln_2.text())
                if self.pw_saveOptions_cb_2.currentText() == 'Centimeters':
                    set_width = round((set_width / 2.54) * 100) / 100
            user_size = False
            if set_height is not None and set_width is not None:
                if (real_height - 0.1) <= set_height <= (real_height + 0.1) and (real_width - 0.1) <= set_width <= (real_width + 0.1):
                    pass
                else:
                    user_size = True
                    plt.gcf().set_size_inches(set_width, set_height)
            kwargs = {"orientation": None, "papertype": None, "format": None,
                      "bbox_inches": None, "pad_inches": 0.1, "frameon": None,
                      'dpi': 100}
            try:
                kwargs['dpi'] = int(self.pw_saveOptions_ln_3.text())
            except ValueError:
                pass
            if out_file_ext == '.jpg':
                kwargs['quality'] = self.pw_saveOptions_sl_1.value()
            kwargs['transparent'] = self.pw_saveOptions_ck_1.isChecked()
            plt.savefig(save_file_name, **kwargs)
            if user_size:
                plt.gcf().set_size_inches(real_width, real_height)
                self.canvas.draw()
    
    def wait_window(self):
        self.waitWindow = MyWait()
        self.waitWindow.exec_()
        
    def close_wait_window(self, val):
        self.plot_single_grid_end(val)
        self.waitWindow.close()
    
    def setup_toolbar(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - setup_toolbar')
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.toolBar = QtWidgets.QToolBar()
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setFont(font)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(35, 35))
        self.actionSave_as = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/save_as_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon1)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.setEnabled(True)
        self.actionClose = QtWidgets.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName("actionClose")
        self.actionZoom = QtWidgets.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon4)
        self.actionZoom.setObjectName("actionZoom")
        self.actionZoom.setEnabled(True)
        self.actionPan = QtWidgets.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/pan_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon5)
        self.actionPan.setObjectName("actionPan")
        self.actionPan.setEnabled(True)
        self.actionOrigin = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/origin_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOrigin.setIcon(icon6)
        self.actionOrigin.setObjectName("actionOrigin")
        self.actionOrigin.setEnabled(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.actionSeparator1 = QtWidgets.QAction(self)
        self.actionSeparator1.setEnabled(False)
        self.actionSeparator1.setIcon(icon7)
        self.actionSeparator1.setObjectName("actionSeparator1")
        self.actionSeparator3 = QtWidgets.QAction(self)
        self.actionSeparator3.setEnabled(False)
        self.actionSeparator3.setIcon(icon7)
        self.actionSeparator3.setObjectName("actionSeparator3")
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionSeparator1)
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionZoom)
        self.toolBar.addAction(self.actionOrigin)
        self.toolBar.addAction(self.actionSeparator3)
        self.toolBar.addAction(self.actionClose)
        self.pw_toolbar_fr.addWidget(self.toolBar)
        self.toolBar.setWindowTitle("toolBar")
        self.actionSave_as.setText("Save as...")
        self.actionSave_as.setToolTip("Save to a graphic file")
        self.actionClose.setText("Close...")
        self.actionClose.setToolTip("Close the plot window")
        self.actionZoom.setText("Zoom")
        self.actionZoom.setToolTip("Zoom to rectangle")
        self.actionPan.setText("Pan")
        self.actionPan.setToolTip("Pan axes")
        self.actionOrigin.setText("Origin")
        self.actionOrigin.setToolTip("Reset to original view")
        
    def setup_plot_area(self):
        self.figure = plt.figure(facecolor='white')
        self.canvas = FigureCanvas(self.figure)
        self.pw_plot_fr.addWidget(self.canvas)
        self.navigation_toolbar = NavigationToolbar(self.canvas, self)
        self.navigation_toolbar.hide()
    
    def activate_grid_options(self, val, plot_type):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_grid_options :')
        index = int(self.sender().objectName()[22:])
        if plot_type == 'timeseries':
            if val == 2:
                self.pw_figureOptions_cb_9[index].setEnabled(True)
                self.pw_figureOptions_cb_10[index].setEnabled(True)
                self.pw_figureOptions_ln_10[index].setEnabled(True)
                self.populate_combobox(self.pw_figureOptions_cb_9[index], self.line_styles, False, 3)
                self.populate_combobox(self.pw_figureOptions_cb_10[index], self.colors_grid, False)
                self.pw_figureOptions_ln_10[index].setText('1')
            else:
                self.pw_figureOptions_cb_9[index].setDisabled(True)
                self.pw_figureOptions_cb_9[index].clear()
                self.pw_figureOptions_cb_10[index].setDisabled(True)
                self.pw_figureOptions_cb_10[index].clear()
                self.pw_figureOptions_ln_10[index].setDisabled(True)
                self.pw_figureOptions_ln_10[index].setText("")
        elif plot_type == 'grids':
            if val == 2:
                self.pw_figureOptions_cb_7[index].setEnabled(True)
                self.pw_figureOptions_cb_8[index].setEnabled(True)
                self.pw_figureOptions_ln_8[index].setEnabled(True)
                self.populate_combobox(self.pw_figureOptions_cb_7[index], self.line_styles, False, 3)
                self.populate_combobox(self.pw_figureOptions_cb_8[index], self.colors_grid, False)
                self.pw_figureOptions_ln_8[index].setText('1')
            else:
                self.pw_figureOptions_cb_7[index].setDisabled(True)
                self.pw_figureOptions_cb_7[index].clear()
                self.pw_figureOptions_cb_8[index].setDisabled(True)
                self.pw_figureOptions_cb_8[index].clear()
                self.pw_figureOptions_ln_8[index].setDisabled(True)
                self.pw_figureOptions_ln_8[index].setText("")
    
    def populate_combobox(self, combobox, item_list, make_choice=True, set_index=None):
        logging.debug('gui - plot_window_functions.py - PlotWindow - populate_combobox')
        if make_choice:
            combobox.addItem("Make a choice...")
        if isinstance(item_list, dict):
            item_list = [key for key in sorted(item_list)]
        combobox.addItems(item_list)
        if set_index is not None:
            if isinstance(set_index, str):
                combobox.setCurrentIndex(combobox.findText(set_index))
            else:
                combobox.setCurrentIndex(set_index)
    
    def update_slider_value(self, val):
        self.findChild(QtWidgets.QLabel, 'slider_lb_' + str(self.sender().objectName()[-1:])).setText(str(float(val) / 100))
        
    def activate_line_style(self, val):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_line_style')
        self.pw_plotOptions_cb_1[int(val.objectName()[20:])].clear()
        if "pw_plotOptions_rb_1" in val.objectName():
            self.populate_combobox(self.pw_plotOptions_cb_1[int(val.objectName()[20:])], self.line_styles, False, 'Solid')
            self.pw_plotOptions_ln_1[int(val.objectName()[20:])].setText('1.25')
        else:
            self.populate_combobox(self.pw_plotOptions_cb_1[int(val.objectName()[20:])], self.marker_styles, False)
            self.pw_plotOptions_ln_1[int(val.objectName()[20:])].setText('10')
    
    def activate_line_color(self, val):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_line_color')
        if self.sender().currentText() == "HEX Color" or self.sender().currentText() == "RGB Color":
            index = int(self.sender().objectName()[20:])
            self.pw_plotOptions_ln_3[index].setText("")
            self.pw_plotOptions_ln_3[index].setMinimumSize(QtCore.QSize(130, 27))
            self.pw_plotOptions_ln_3[index].setMaximumSize(QtCore.QSize(130, 27))
            self.pw_plotOptions_lb_8[index].show()
            self.pw_plotOptions_ln_3[index].show()
            self.pw_plotOptions_lb_8[index].setText(self.sender().currentText()[0:3] + " code:")
            self.pw_plotOptions_ln_3[index].setText("")
            self.pw_plotOptions_ln_5[index].hide()
            self.pw_plotOptions_ln_6[index].hide()
            self.pw_plotOptions_ln_5[index].setText("")
            self.pw_plotOptions_ln_6[index].setText("")
            if self.sender().currentText() == "RGB Color":
                self.pw_plotOptions_ln_3[index].setMinimumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_3[index].setMaximumSize(QtCore.QSize(60, 27))
                self.pw_plotOptions_ln_5[index].show()
                self.pw_plotOptions_ln_6[index].show()
        else:
            index = int(self.sender().objectName()[20:])
            self.pw_plotOptions_lb_8[index].hide()
            self.pw_plotOptions_ln_3[index].hide()
            self.pw_plotOptions_lb_8[index].setText("")
            self.pw_plotOptions_ln_3[index].setText("")
            self.pw_plotOptions_ln_5[index].hide()
            self.pw_plotOptions_ln_6[index].hide()
            self.pw_plotOptions_ln_5[index].setText("")
            self.pw_plotOptions_ln_6[index].setText("")
    
    def activate_opacity_options(self, val):
        logging.debug('gui - plot_window_functions.py - PlotWindow - activate_opacity_options')
        index = int(self.sender().objectName()[20:])
        if val == 2:
            self.pw_plotOptions_ln_2[index].setEnabled(True)
            self.pw_plotOptions_ln_2[index].setText("100")
        else:    
            self.pw_plotOptions_ln_2[index].setDisabled(True)
            self.pw_plotOptions_ln_2[index].setText("")
    
    def resizeEvent(self, event):
        width, height = plt.gcf().get_size_inches()
        if self.pw_saveOptions_cb_1.currentText() == 'Centimeters':
            height *= 2.54
        if self.pw_saveOptions_cb_2.currentText() == 'Centimeters':
            width *= 2.54
        height = round(height * 100) / 100
        width = round(width * 100) / 100
        self.pw_saveOptions_ln_1.setText(str(height))
        self.pw_saveOptions_ln_2.setText(str(width))
    
    def unlock_size_edit(self):
        if not self.pw_saveOptions_ln_1.isEnabled():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/unlock_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pw_lock_bt_1.setIcon(icon)
            self.pw_saveOptions_ln_1.setEnabled(True)
            self.pw_saveOptions_ln_2.setEnabled(True)
            self.pw_saveOptions_cb_1.setEnabled(True)
            self.pw_saveOptions_cb_2.setEnabled(True)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/lock_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pw_lock_bt_1.setIcon(icon)
            self.pw_saveOptions_ln_1.setEnabled(False)
            self.pw_saveOptions_ln_2.setEnabled(False)
            self.pw_saveOptions_cb_1.setEnabled(False)
            self.pw_saveOptions_cb_2.setEnabled(False)
        
    def convert_inch_cm(self, index):
        if self.sender().objectName() == 'pw_saveOptions_cb_1':
            if index == 0:
                value = round((float(self.pw_saveOptions_ln_1.text()) * 2.54) * 100) / 100
                self.pw_saveOptions_ln_1.setText(str(value))
            else:
                value = round((float(self.pw_saveOptions_ln_1.text()) / 2.54) * 100) / 100
                self.pw_saveOptions_ln_1.setText(str(value))
        else:
            if index == 0:
                value = round((float(self.pw_saveOptions_ln_2.text()) * 2.54) * 100) / 100
                self.pw_saveOptions_ln_2.setText(str(value))
            else:
                value = round((float(self.pw_saveOptions_ln_2.text()) / 2.54) * 100) / 100
                self.pw_saveOptions_ln_2.setText(str(value))
    
    def update_quality_value(self, val):
        self.pw_saveOptions_lb_7.setText(str(val))
    
    def set_axis_ticks_labels(self, val):
        if 'pw_ticks_bt_1' in self.sender().objectName():
            text = 'X'
            label = self.pw_figureOptions_lb_16[int(self.sender().objectName()[14:])]
        elif 'pw_ticks_bt_2' in self.sender().objectName():
            text = 'Y'
            label = self.pw_figureOptions_lb_17[int(self.sender().objectName()[14:])]
        text += ' ticks/labels:'
        self.tickslabelsWindow = TicksLabelsWindow(text)
        self.tickslabelsWindow.exec_()
        label.setText(self.tickslabelsWindow.ticks_labels)
    
    def get_file_name(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        try:
            import pillow
            filter_types = "EPS Files (*.eps);;JPEG Files (*.jpg *.jpeg *.jpe);;PDF Files (*.pdf);;PNG Files (*.png *.pns);;TIFF Files (*.tif *.tiff)"
        except:
            filter_types = "EPS Files (*.eps);;PDF Files (*.pdf);;PNG Files (*.png *.pns);;TIFF Files (*.tif *.tiff)"
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, "Save File", "", filter_types)
        return str(out_file_name), str(out_file_ext)
    
    def close_window(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - close_window')
        self.close()  


class PlotTypeWindow(QtWidgets.QDialog, Ui_plottypeWindow):
    def __init__(self):
        logging.debug('gui - plot_window_functions.py - PlotTypeWindow - __init__')
        QtWidgets.QDialog.__init__(self, parent=None)
        self.setupUi(self)
        self.button.clicked.connect(self.close_window)
        self.result = None
        
    def close_window(self):
        if self.radio_button_1.isChecked():
            self.result = 'plot'
        else:
            self.result = 'subplot'
        logging.debug('gui - plot_window_functions.py - PlotWindow - close_window')
        self.close() 
    

class TicksLabelsWindow(QtWidgets.QDialog, Ui_tickslabelsWindow):
    def __init__(self, text):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - __init__')
        QtWidgets.QDialog.__init__(self, parent=None)
        self.setupUi(self)
        self.label.setText(text)
        self.ok_button.clicked.connect(self.set_ticks)
        self.cancel_button.clicked.connect(self.close_window)
        self.add_button.clicked.connect(self.add_cell)
        self.del_button.clicked.connect(self.del_cell)
    
    def add_cell(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - add_cell')
        self.table.insertColumn(self.table.columnCount())
    
    def del_cell(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - del_cell')
        self.table.removeColumn(self.table.columnCount() - 1)
    
    def set_ticks(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - set_ticks')
        self.ticks_labels = ''
        for i in range(self.table.columnCount()):
            if self.table.item(0, i).text():
                self.ticks_labels += self.table.item(0, i).text() + '|'
        self.ticks_labels = self.ticks_labels[:-1]
        self.close_window()
    
    def close_window(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - close_window')
        self.close()

