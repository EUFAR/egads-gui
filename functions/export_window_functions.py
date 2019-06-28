import logging
import ntpath
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_exportwindow import Ui_exportWindow
from ui.Ui_waitwindow import Ui_waitWindow
from functions.gui_elements import QtWaitingSpinner
from functions.thread_functions import ExportThread
from functions.other_windows_functions import MyInfo
from functions.material_functions import export_main_information_buttons_text, export_ge_ts_information_buttons_text
from functions.utils import clear_layout


class MyExport(QtWidgets.QDialog, Ui_exportWindow):
    def __init__(self, list_of_variables_and_attributes):
        logging.debug('gui - export_window_functions.py - MyExport - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.list_of_variables_and_attributes = list_of_variables_and_attributes
        self.ow_splitter.setSizes([140, 608])  # 748
        self.ew_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.main_information_buttons_text = export_main_information_buttons_text()
        self.ge_ts_information_buttons_text = export_ge_ts_information_buttons_text()
        self.ew_combobox_1.currentIndexChanged.connect(self.populate_format_options)
        self.ew_option_list.itemSelectionChanged.connect(self.populate_options)
        self.ew_cancel_button.clicked.connect(self.closeWindow)
        self.ew_export_button.clicked.connect(self.export_function)
        self.info_button_1.clicked.connect(self.export_button_info)
        self.export_format = None
        self.export_dict = {}
        self.colormap_dict = {1: 'coolwarm', 2: 'jet', 3: 'ocean', 4: 'spectral', 5: 'hot', 6: 'hsv', 7: 'seismic',
                              8: 'terrain'}
        self.var_list = []
        logging.info('gui - export_window_functions.py - MyExport - ready')

    def populate_format_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - populate_format_options')
        if self.ew_combobox_1.currentIndex() == 0:
            self.setWindowTitle('Export to')
            self.export_format = None
            self.ew_option_list.clear()
            clear_layout(self.ew_vertical_layout)
        elif self.ew_combobox_1.currentIndex() == 1:
            self.setWindowTitle('Export to Google Earth - Time Series')
            self.export_format = 'GE-TS'
            self.ew_option_list.clear()
            clear_layout(self.ew_vertical_layout)
            self.ew_option_list.addItems(['Coordinates', 'Variables', 'Options', 'Colormap'])
            self.export_dict = {'Coordinates': {'lon': None, 'lat': None, 'alt': None},
                                'Variables': [],
                                'Options': {'wall': False, 'wall_transparency': False, 'transparency': 100,
                                            'reduce_samples': False, 'reduce_value': None, 'path_width': 5},
                                'Colormap': {'colormap': None, 'position': 0, 'reversed': False, 'automatic': True,
                                             'min': None, 'max': None, 'steps': None, 'auto_dimension': True,
                                             'fig_height': None, 'fig_width': None, 'pos_left': None,
                                             'pos_bottom': None, 'width': None, 'height': None, 'color_value': 0}}
        else:
            self.setWindowTitle('Export to')
            self.export_format = None
            self.ew_option_list.clear()
            clear_layout(self.ew_vertical_layout)
        self.prepare_var_list()

    def prepare_var_list(self):
        logging.debug('gui - export_window_functions.py - MyExport - prepare_var_list')
        if self.export_format == 'GE-TS':
            for key, val in self.list_of_variables_and_attributes.items():
                if len(val[0].value.shape) == 1:
                    self.var_list.append(key)
        self.var_list = sorted(self.var_list)

    def populate_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - populate_options')
        if self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Coordinates':
            clear_layout(self.ew_vertical_layout)
            self.set_ge_ts_coordinates_options()
        elif self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Variables':
            clear_layout(self.ew_vertical_layout)
            self.set_ge_ts_variables_options()
        elif self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Options':
            clear_layout(self.ew_vertical_layout)
            self.set_ge_ts_options_options()
        elif self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Colormap':
            clear_layout(self.ew_vertical_layout)
            self.set_ge_ts_colormap_options()

    def set_ge_ts_coordinates_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_ge_ts_coordinates_options')
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ew_label_2 = QtWidgets.QLabel()
        self.ew_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_2.setFont(font)
        self.ew_label_2.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
        self.ew_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_2.setObjectName("ew_label_2")
        self.gridLayout_2.addWidget(self.ew_label_2, 0, 0, 1, 1)
        self.ew_combobox_2 = QtWidgets.QComboBox()
        self.ew_combobox_2.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_2.setMaximumSize(QtCore.QSize(250, 27))
        self.ew_combobox_2.setFont(font2)
        self.ew_combobox_2.setStyleSheet("QComboBox {\n"
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
                                         "QComboBox QAbstractItemView {\n"
                                         "    background: #f0f0f0;\n"
                                         "    border: 0px solid #f0f0f0;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox QAbstractItemView::item {\n"
                                         "    margin: 5px 5px 5px 5px;\n"
                                         "}")
        self.ew_combobox_2.setObjectName("ew_combobox_2")
        self.ew_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.gridLayout_2.addWidget(self.ew_combobox_2, 0, 1, 1, 1)
        self.ew_label_3 = QtWidgets.QLabel()
        self.ew_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_3.setFont(font)
        self.ew_label_3.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
        self.ew_label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_3.setObjectName("ew_label_3")
        self.gridLayout_2.addWidget(self.ew_label_3, 1, 0, 1, 1)
        self.ew_combobox_3 = QtWidgets.QComboBox()
        self.ew_combobox_3.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_3.setMaximumSize(QtCore.QSize(250, 27))
        self.ew_combobox_3.setFont(font2)
        self.ew_combobox_3.setStyleSheet("QComboBox {\n"
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
        self.ew_combobox_3.setObjectName("ew_combobox_3")
        self.ew_combobox_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.gridLayout_2.addWidget(self.ew_combobox_3, 1, 1, 1, 1)
        self.ew_label_4 = QtWidgets.QLabel()
        self.ew_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_4.setFont(font)
        self.ew_label_4.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
        self.ew_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_4.setObjectName("ew_label_4")
        self.gridLayout_2.addWidget(self.ew_label_4, 2, 0, 1, 1)
        self.ew_combobox_4 = QtWidgets.QComboBox()
        self.ew_combobox_4.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_4.setMaximumSize(QtCore.QSize(250, 27))
        self.ew_combobox_4.setFont(font2)
        self.ew_combobox_4.setStyleSheet("QComboBox {\n"
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
        self.ew_combobox_4.setObjectName("ew_combobox_4")
        self.ew_combobox_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.gridLayout_2.addWidget(self.ew_combobox_4, 2, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_2 = QtWidgets.QToolButton()
        self.info_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_2.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_2.setText("")
        self.info_button_2.setIcon(icon1)
        self.info_button_2.setIconSize(QtCore.QSize(23, 23))
        self.info_button_2.setAutoRaise(False)
        self.info_button_2.setObjectName("info_button_2")
        self.horizontalLayout_3.addWidget(self.info_button_2)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout_3)
        self.ew_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ew_label_1.setText("Choose a format:")
        self.ew_label_2.setText("Longitude:")
        self.ew_label_3.setText("Latitude:")
        self.ew_label_4.setText("Altitude:")
        self.ew_combobox_2.addItems(['Make a choice...'] + self.var_list)
        self.ew_combobox_3.addItems(['Make a choice...'] + self.var_list)
        self.ew_combobox_4.addItems(['Make a choice...', 'Stick path to ground'] + self.var_list)
        self.ew_combobox_2.currentIndexChanged.connect(self.set_combobox_options)
        self.ew_combobox_3.currentIndexChanged.connect(self.set_combobox_options)
        self.ew_combobox_4.currentIndexChanged.connect(self.set_combobox_options)
        self.ew_combobox_2.currentIndexChanged.connect(self.activate_export_button)
        self.ew_combobox_3.currentIndexChanged.connect(self.activate_export_button)
        self.ew_combobox_4.currentIndexChanged.connect(self.activate_export_button)
        self.info_button_2.clicked.connect(self.export_ge_ts_button_info)
        self.read_export_dict()

    def set_ge_ts_variables_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_ge_ts_variables_options')
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ew_label_2 = QtWidgets.QLabel()
        self.ew_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_2.setFont(font)
        self.ew_label_2.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
        self.ew_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_2.setObjectName("ew_label_2")
        self.gridLayout_2.addWidget(self.ew_label_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ew_combobox_5 = QtWidgets.QComboBox()
        self.ew_combobox_5.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_5.setMaximumSize(QtCore.QSize(250, 27))
        self.ew_combobox_5.setFont(font2)
        self.ew_combobox_5.setStyleSheet("QComboBox {\n"
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
        self.ew_combobox_5.setObjectName("ew_combobox_5")
        self.ew_combobox_5.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout_4.addWidget(self.ew_combobox_5)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_add_button = QtWidgets.QToolButton()
        self.ew_add_button.setMinimumSize(QtCore.QSize(27, 27))
        self.ew_add_button.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_add_button.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")

        self.ew_add_button.setIcon(icon2)
        self.ew_add_button.setIconSize(QtCore.QSize(23, 23))
        self.ew_add_button.setObjectName("ew_add_button")
        self.horizontalLayout_4.addWidget(self.ew_add_button)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.ew_label_3 = QtWidgets.QLabel()
        self.ew_label_3.setMinimumSize(QtCore.QSize(200, 27))
        self.ew_label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ew_label_3.setFont(font)
        self.ew_label_3.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
        self.ew_label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.ew_label_3.setWordWrap(True)
        self.ew_label_3.setObjectName("ew_label_3")
        self.gridLayout_2.addWidget(self.ew_label_3, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ew_varlist_1 = QtWidgets.QListWidget()
        self.ew_varlist_1.setEnabled(True)
        self.ew_varlist_1.setMinimumSize(QtCore.QSize(0, 150))
        self.ew_varlist_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ew_varlist_1.setFont(font2)
        self.ew_varlist_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ew_varlist_1.setStyleSheet("QListWidget {\n"
                                        "    border-radius: 3px;\n"
                                        "    background-color: rgb(240,240,240);\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QListWidget:disabled {\n"
                                        "    background-color:  rgb(200,200,200);\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QListView::item {\n"
                                        "    border: 0px solid rgb(240,240,240);\n"
                                        "    border-radius: 3px;\n"
                                        "    padding: 1px 1px 1px 1px;\n"
                                        "    margin: 3px 3px 3px 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QListView::item:selected {\n"
                                        "    border: 0px solid rgb(240,240,240);\n"
                                        "    border-radius: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QListView::item:selected:!active {\n"
                                        "    background: rgb(200,200,200);\n"
                                        "}\n"
                                        "\n"
                                        "QListView::item:selected:active {\n"
                                        "    background: rgb(200,200,200);\n"
                                        "}\n"
                                        "\n"
                                        "QListView::item:hover {\n"
                                        "    background: rgb(230,230,230);\n"
                                        "    border-radius: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar:vertical {\n"
                                        "  border: 1px solid white;\n"
                                        "  background-color: rgb(240, 240, 240);\n"
                                        "  width: 20px;\n"
                                        "  margin: 21px 0px 21px 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar:horizontal {\n"
                                        "  border: 1px solid white;\n"
                                        "  background-color: rgb(240, 240, 240);\n"
                                        "  height: 20px;\n"
                                        "  margin: 0px 21px 0px 21px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::handle:vertical {\n"
                                        "  background-color: rgb(205, 205, 205);\n"
                                        "  min-height: 25px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar:handle:vertical:hover {\n"
                                        "  background-color: rgb(166, 166, 166);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar:handle:vertical:pressed {\n"
                                        "  background-color: rgb(96, 96, 96);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::handle:horizontal {\n"
                                        "  background-color: rgb(205, 205, 205);\n"
                                        "  min-width: 25px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar:handle:horizontal:hover {\n"
                                        "  background-color: rgb(166, 166, 166);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar:handle:horizontal:pressed {\n"
                                        "  background-color: rgb(96, 96, 96);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::add-line:vertical {\n"
                                        "  border-top: 1px solid rgb(240,240,240);\n"
                                        "  border-left: 1px solid white;\n"
                                        "  border-right: 1px solid white;\n"
                                        "  border-bottom: 1px solid white;\n"
                                        "  background-color: rgb(240, 240, 240);\n"
                                        "  height: 20px;\n"
                                        "  subcontrol-position: bottom;\n"
                                        "  subcontrol-origin: margin;\n"
                                        "  border-bottom-right-radius: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::add-line:vertical:hover {\n"
                                        "  background-color: rgb(218, 218, 218);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::add-line:vertical:pressed {\n"
                                        "  background-color: rgb(96, 96, 96);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:vertical {\n"
                                        "  border-top: 1px solid white;\n"
                                        "  border-left: 1px solid white;\n"
                                        "  border-right: 1px solid white;\n"
                                        "  border-bottom: 1px solid rgb(240,240,240);\n"
                                        "  background-color: rgb(240, 240, 240);\n"
                                        "  height: 20px;\n"
                                        "  subcontrol-position: top;\n"
                                        "  subcontrol-origin: margin;\n"
                                        "  border-top-right-radius: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:vertical:hover {\n"
                                        "  background-color: rgb(218, 218, 218);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:vertical:pressed {\n"
                                        "  background-color: rgb(96, 96, 96);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::up-arrow:vertical {\n"
                                        "  image: url(icons/up_arrow_icon.svg); \n"
                                        "  width: 16px;\n"
                                        "  height: 16px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::up-arrow:vertical:pressed {\n"
                                        "  right: -1px;\n"
                                        "  bottom: -1px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::down-arrow:vertical {\n"
                                        "  image: url(icons/down_arrow_icon.svg); \n"
                                        "  width: 16px;\n"
                                        "  height: 16px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::down-arrow:vertical:pressed {\n"
                                        "  right: -1px;\n"
                                        "  bottom: -1px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::add-line:horizontal {\n"
                                        "  border-top: 1px solid white;\n"
                                        "  border-left: 1px solid rgb(240,240,240);\n"
                                        "  border-right: 1px solid white;\n"
                                        "  border-bottom: 1px solid white;\n"
                                        "  background-color: rgb(240, 240, 240);\n"
                                        "  width: 20px;\n"
                                        "  subcontrol-position: right;\n"
                                        "  subcontrol-origin: margin;\n"
                                        "  border-bottom-right-radius: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::add-line:horizontal:hover {\n"
                                        "  background-color: rgb(218, 218, 218);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::add-line:horizontal:pressed {\n"
                                        "  background-color: rgb(96, 96, 96);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:horizontal {\n"
                                        "  border-top: 1px solid white;\n"
                                        "  border-left: 1px solid white;\n"
                                        "  border-right: 1px solid rgb(240,240,240);\n"
                                        "  border-bottom: 1px solid white;\n"
                                        "  background-color: rgb(240, 240, 240);\n"
                                        "  width: 20px;\n"
                                        "  subcontrol-position: left;\n"
                                        "  subcontrol-origin: margin;\n"
                                        "border-bottom-left-radius: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:horizontal:hover {\n"
                                        "  background-color: rgb(218, 218, 218);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:horizontal:pressed {\n"
                                        "  background-color: rgb(96, 96, 96);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::left-arrow:horizontal {\n"
                                        "  image: url(icons/left_arrow_icon.svg); \n"
                                        "  width: 16px;\n"
                                        "  height: 16px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::left-arrow:horizontal:pressed {\n"
                                        "  right: -1px;\n"
                                        "  bottom: -1px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::right-arrow:horizontal {\n"
                                        "  image: url(icons/right_arrow_icon.svg); \n"
                                        "  width: 16px;\n"
                                        "  height: 16px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::right-arrow:horizontal:pressed {\n"
                                        "  right: -1px;\n"
                                        "  bottom: -1px;\n"
                                        "}")
        self.ew_varlist_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ew_varlist_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ew_varlist_1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ew_varlist_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ew_varlist_1.setObjectName("ew_varlist_1")
        self.horizontalLayout_3.addWidget(self.ew_varlist_1)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_button_3 = QtWidgets.QToolButton()
        self.info_button_3.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_3.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_3.setText("")
        self.info_button_3.setIcon(icon1)
        self.info_button_3.setIconSize(QtCore.QSize(23, 23))
        self.info_button_3.setAutoRaise(False)
        self.info_button_3.setObjectName("info_button_3")
        self.verticalLayout.addWidget(self.info_button_3)
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Expanding))
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.ew_vertical_layout.addLayout(self.gridLayout_2)
        self.ew_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ew_label_2.setText("Add one or more variables:")
        self.ew_label_3.setText("Variable(s) displayed in Google Earth:")
        self.ew_combobox_5.addItems(['Make a choice...'] + self.var_list)
        self.ew_add_button.clicked.connect(self.set_button_options)
        self.ew_varlist_1.itemDoubleClicked.connect(self.remove_variable_from_list)
        self.ew_add_button.clicked.connect(self.activate_export_button)
        self.ew_varlist_1.itemDoubleClicked.connect(self.activate_export_button)
        self.info_button_3.clicked.connect(self.export_ge_ts_button_info)
        self.read_export_dict()

    def set_ge_ts_options_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_ge_ts_options_options')
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ew_label_5 = QtWidgets.QLabel()
        self.ew_label_5.setEnabled(True)
        self.ew_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_5.setFont(font)
        self.ew_label_5.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_5.setObjectName("ew_label_5")
        self.horizontalLayout.addWidget(self.ew_label_5)
        self.ew_slider_2 = QtWidgets.QSlider()
        self.ew_slider_2.setEnabled(True)
        self.ew_slider_2.setMinimumSize(QtCore.QSize(180, 27))
        self.ew_slider_2.setMaximumSize(QtCore.QSize(180, 27))
        self.ew_slider_2.setStyleSheet("QSlider::groove:horizontal {\n"
                                       "    border: 1px solid #999999;\n"
                                       "    height: 1px;\n"
                                       "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, "
                                       "stop:1 #c4c4c4);\n"
                                       "    margin: 2px 0;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal {\n"
                                       "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, "
                                       "stop:1 #8f8f8f);\n"
                                       "    border: 1px solid #5c5c5c;\n"
                                       "    width: 10px;\n"
                                       "    margin: -5px 0;\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal:hover {\n"
                                       "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, "
                                       "stop:1 #a7a7a7);\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::add-page:horizontal {\n"
                                       "    background: rgb(200,200,200);\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::sub-page:horizontal {\n"
                                       "    background: rgb(0,0,200);\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::sub-page:horizontal:disabled {\n"
                                       "    background: rgb(145,145,145);\n"
                                       "}\n"
                                       "")
        self.ew_slider_2.setMinimum(1)
        self.ew_slider_2.setMaximum(20)
        self.ew_slider_2.setSingleStep(1)
        self.ew_slider_2.setPageStep(1)
        self.ew_slider_2.setProperty("value", 5)
        self.ew_slider_2.setSliderPosition(5)
        self.ew_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.ew_slider_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.ew_slider_2.setObjectName("ew_slider_2")
        self.horizontalLayout.addWidget(self.ew_slider_2)
        self.ew_label_6 = QtWidgets.QLabel()
        self.ew_label_6.setEnabled(True)
        self.ew_label_6.setMinimumSize(QtCore.QSize(45, 27))
        self.ew_label_6.setMaximumSize(QtCore.QSize(45, 27))
        self.ew_label_6.setFont(font)
        self.ew_label_6.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_6.setObjectName("ew_label_6")
        self.horizontalLayout.addWidget(self.ew_label_6)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.info_button_12 = QtWidgets.QToolButton()
        self.info_button_12.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_12.setStyleSheet("QToolButton {\n"
                                          "    border: 1px solid transparent;\n"
                                          "    background-color: transparent;\n"
                                          "    width: 27px;\n"
                                          "    height: 27px;\n"
                                          "}\n"
                                          "\n"
                                          "QToolButton:flat {\n"
                                          "    border: none;\n"
                                          "}")
        self.info_button_12.setText("")
        self.info_button_12.setIcon(icon1)
        self.info_button_12.setIconSize(QtCore.QSize(23, 23))
        self.info_button_12.setAutoRaise(False)
        self.info_button_12.setObjectName("info_button_12")
        self.horizontalLayout.addWidget(self.info_button_12)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ew_checkbox_1 = QtWidgets.QCheckBox()
        self.ew_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_checkbox_1.setFont(font)
        self.ew_checkbox_1.setStyleSheet("QCheckBox {\n"
                                         "   color: rgb(45,45,45);\n"
                                         "}")
        self.ew_checkbox_1.setObjectName("ew_checkbox_1")
        self.horizontalLayout_3.addWidget(self.ew_checkbox_1)
        self.info_button_4 = QtWidgets.QToolButton()
        self.info_button_4.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_4.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_4.setText("")
        self.info_button_4.setIcon(icon1)
        self.info_button_4.setIconSize(QtCore.QSize(23, 23))
        self.info_button_4.setAutoRaise(False)
        self.info_button_4.setObjectName("info_button_4")
        self.horizontalLayout_3.addWidget(self.info_button_4)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ew_checkbox_2 = QtWidgets.QCheckBox()
        self.ew_checkbox_2.setEnabled(False)
        self.ew_checkbox_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_checkbox_2.setFont(font)
        self.ew_checkbox_2.setStyleSheet("QCheckBox {\n"
                                         "   color: rgb(45,45,45);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox:disabled {\n"
                                         "    color: rgb(145,145,145);\n"
                                         "}")
        self.ew_checkbox_2.setObjectName("ew_checkbox_2")
        self.horizontalLayout_4.addWidget(self.ew_checkbox_2)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_5 = QtWidgets.QToolButton()
        self.info_button_5.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_5.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_5.setText("")
        self.info_button_5.setIcon(icon1)
        self.info_button_5.setIconSize(QtCore.QSize(23, 23))
        self.info_button_5.setAutoRaise(False)
        self.info_button_5.setObjectName("info_button_5")
        self.horizontalLayout_4.addWidget(self.info_button_5)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_label_2 = QtWidgets.QLabel()
        self.ew_label_2.setEnabled(False)
        self.ew_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_2.setFont(font)
        self.ew_label_2.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_2.setObjectName("ew_label_2")
        self.horizontalLayout_5.addWidget(self.ew_label_2)
        self.ew_slider_1 = QtWidgets.QSlider()
        self.ew_slider_1.setEnabled(False)
        self.ew_slider_1.setMinimumSize(QtCore.QSize(180, 27))
        self.ew_slider_1.setMaximumSize(QtCore.QSize(180, 27))
        self.ew_slider_1.setStyleSheet("QSlider::groove:horizontal {\n"
                                       "    border: 1px solid #999999;\n"
                                       "    height: 1px;\n"
                                       "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, "
                                       "stop:1 #c4c4c4);\n"
                                       "    margin: 2px 0;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal {\n"
                                       "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, "
                                       "stop:1 #8f8f8f);\n"
                                       "    border: 1px solid #5c5c5c;\n"
                                       "    width: 10px;\n"
                                       "    margin: -5px 0;\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal:hover {\n"
                                       "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, "
                                       "stop:1 #a7a7a7);\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::add-page:horizontal {\n"
                                       "    background: rgb(200,200,200);\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::sub-page:horizontal {\n"
                                       "    background: rgb(0,0,200);\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::sub-page:horizontal:disabled {\n"
                                       "    background: rgb(145,145,145);\n"
                                       "}\n"
                                       "")
        self.ew_slider_1.setMinimum(0)
        self.ew_slider_1.setMaximum(100)
        self.ew_slider_1.setSingleStep(1)
        self.ew_slider_1.setPageStep(1)
        self.ew_slider_1.setProperty("value", 0)
        self.ew_slider_1.setSliderPosition(0)
        self.ew_slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.ew_slider_1.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.ew_slider_1.setObjectName("ew_slider_1")
        self.horizontalLayout_5.addWidget(self.ew_slider_1)
        self.ew_label_3 = QtWidgets.QLabel()
        self.ew_label_3.setEnabled(False)
        self.ew_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_3.setFont(font)
        self.ew_label_3.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_3.setObjectName("ew_label_3")
        self.horizontalLayout_5.addWidget(self.ew_label_3)
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ew_checkbox_3 = QtWidgets.QCheckBox()
        self.ew_checkbox_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_checkbox_3.setFont(font)
        self.ew_checkbox_3.setStyleSheet("QCheckBox {\n"
                                         "   color: rgb(45,45,45);\n"
                                         "}")
        self.ew_checkbox_3.setObjectName("ew_checkbox_3")
        self.horizontalLayout_6.addWidget(self.ew_checkbox_3)
        self.info_button_6 = QtWidgets.QToolButton()
        self.info_button_6.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_6.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_6.setText("")
        self.info_button_6.setIcon(icon1)
        self.info_button_6.setIconSize(QtCore.QSize(23, 23))
        self.info_button_6.setAutoRaise(False)
        self.info_button_6.setObjectName("info_button_6")
        self.horizontalLayout_6.addWidget(self.info_button_6)
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_label_4 = QtWidgets.QLabel()
        self.ew_label_4.setEnabled(False)
        self.ew_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_4.setFont(font)
        self.ew_label_4.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_4.setObjectName("ew_label_4")
        self.horizontalLayout_7.addWidget(self.ew_label_4)
        self.ew_line_1 = QtWidgets.QLineEdit()
        self.ew_line_1.setEnabled(False)
        self.ew_line_1.setMinimumSize(QtCore.QSize(50, 27))
        self.ew_line_1.setMaximumSize(QtCore.QSize(50, 27))
        self.ew_line_1.setFont(font2)
        self.ew_line_1.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_1.setObjectName("ew_line_1")
        self.horizontalLayout_7.addWidget(self.ew_line_1)
        self.horizontalLayout_7.addItem(QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout_7)
        self.ew_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ew_label_5.setText("Path width:")
        self.ew_label_6.setText("5 px")
        self.ew_checkbox_1.setText("Connect the path to the ground")
        self.ew_checkbox_2.setText("Add transparency to the wall")
        self.ew_label_2.setText("Transparency:")
        self.ew_label_3.setText("0 %")
        self.ew_checkbox_3.setText("Reduce the number of samples in time series")
        self.ew_label_4.setText("Keep 1 sample on:")
        self.ew_checkbox_1.clicked.connect(self.set_checkbox_options)
        self.ew_checkbox_2.clicked.connect(self.set_checkbox_options)
        self.ew_checkbox_3.clicked.connect(self.set_checkbox_options)
        self.ew_checkbox_1.clicked.connect(self.activate_transparency_checkbox)
        self.ew_checkbox_2.clicked.connect(self.activate_transparency_slider)
        self.ew_checkbox_3.clicked.connect(self.activate_reduce_value)
        self.ew_slider_1.valueChanged.connect(self.update_slider_value)
        self.ew_slider_1.valueChanged.connect(self.set_slider_options)
        self.ew_slider_2.valueChanged.connect(self.update_slider_value)
        self.ew_slider_2.valueChanged.connect(self.set_slider_options)
        self.ew_line_1.textChanged.connect(self.set_line_options)
        self.ew_checkbox_1.clicked.connect(self.activate_export_button)
        self.ew_checkbox_2.clicked.connect(self.activate_export_button)
        self.ew_checkbox_3.clicked.connect(self.activate_export_button)
        self.ew_slider_1.valueChanged.connect(self.activate_export_button)
        self.ew_line_1.textChanged.connect(self.activate_export_button)
        self.info_button_12.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_4.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_5.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_6.clicked.connect(self.export_ge_ts_button_info)
        self.read_export_dict()

    def set_ge_ts_colormap_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_ge_ts_colormap_options')
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ew_label_2 = QtWidgets.QLabel()
        self.ew_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_2.setFont(font)
        self.ew_label_2.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
        self.ew_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_2.setObjectName("ew_label_2")
        self.horizontalLayout_5.addWidget(self.ew_label_2)
        self.ew_combobox_6 = QtWidgets.QComboBox()
        self.ew_combobox_6.setMinimumSize(QtCore.QSize(244, 30))
        self.ew_combobox_6.setMaximumSize(QtCore.QSize(244, 30))
        self.ew_combobox_6.setFont(font2)
        self.ew_combobox_6.setStyleSheet("QComboBox {\n"
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
                                         "    width: 30px;\n"
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
        self.ew_combobox_6.setIconSize(QtCore.QSize(200, 22))
        self.ew_combobox_6.setObjectName("ew_combobox_6")
        self.ew_combobox_6.addItem("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/colormap_coolwarm.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon9, "")
        self.ew_combobox_6.setItemText(1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/colormap_jet.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon2, "")
        self.ew_combobox_6.setItemText(2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/colormap_ocean.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon3, "")
        self.ew_combobox_6.setItemText(3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/colormap_spectral.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon4, "")
        self.ew_combobox_6.setItemText(4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/hot.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon5, "")
        self.ew_combobox_6.setItemText(5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/hsv.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon6, "")
        self.ew_combobox_6.setItemText(6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/seismic.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon7, "")
        self.ew_combobox_6.setItemText(7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/terrain.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon8, "")
        self.ew_combobox_6.setItemText(8, "")
        self.horizontalLayout_5.addWidget(self.ew_combobox_6)
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_7 = QtWidgets.QToolButton()
        self.info_button_7.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_7.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_7.setText("")
        self.info_button_7.setIcon(icon1)
        self.info_button_7.setIconSize(QtCore.QSize(23, 23))
        self.info_button_7.setAutoRaise(False)
        self.info_button_7.setObjectName("info_button_7")
        self.horizontalLayout_5.addWidget(self.info_button_7)
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.ew_vertical_layout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ew_label_6 = QtWidgets.QLabel()
        self.ew_label_6.setEnabled(False)
        self.ew_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_6.setFont(font)
        self.ew_label_6.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_6.setObjectName("ew_label_6")
        self.horizontalLayout_8.addWidget(self.ew_label_6)
        self.ew_combobox_7 = QtWidgets.QComboBox()
        self.ew_combobox_7.setEnabled(False)
        self.ew_combobox_7.setMinimumSize(QtCore.QSize(170, 27))
        self.ew_combobox_7.setMaximumSize(QtCore.QSize(170, 27))
        self.ew_combobox_7.setFont(font2)
        self.ew_combobox_7.setStyleSheet("QComboBox {\n"
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
        self.ew_combobox_7.setObjectName("ew_combobox_7")
        self.ew_combobox_7.addItem("")
        self.ew_combobox_7.addItem("")
        self.ew_combobox_7.addItem("")
        self.ew_combobox_7.addItem("")
        self.horizontalLayout_8.addWidget(self.ew_combobox_7)
        self.horizontalLayout_8.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_11 = QtWidgets.QToolButton()
        self.info_button_11.setEnabled(False)
        self.info_button_11.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_11.setStyleSheet("QToolButton {\n"
                                          "    border: 1px solid transparent;\n"
                                          "    background-color: transparent;\n"
                                          "    width: 27px;\n"
                                          "    height: 27px;\n"
                                          "}\n"
                                          "\n"
                                          "QToolButton:flat {\n"
                                          "    border: none;\n"
                                          "}")
        self.info_button_11.setText("")
        self.info_button_11.setIcon(icon1)
        self.info_button_11.setIconSize(QtCore.QSize(23, 23))
        self.info_button_11.setAutoRaise(False)
        self.info_button_11.setObjectName("info_button_11")
        self.horizontalLayout_8.addWidget(self.info_button_11)
        self.horizontalLayout_8.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ew_checkbox_4 = QtWidgets.QCheckBox()
        self.ew_checkbox_4.setEnabled(False)
        self.ew_checkbox_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_checkbox_4.setFont(font)
        self.ew_checkbox_4.setStyleSheet("QCheckBox {\n"
                                         "   color: rgb(45,45,45);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox:disabled {\n"
                                         "    color: rgb(145,145,145);\n"
                                         "}")
        self.ew_checkbox_4.setObjectName("ew_checkbox_4")
        self.horizontalLayout_3.addWidget(self.ew_checkbox_4)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_8 = QtWidgets.QToolButton()
        self.info_button_8.setEnabled(False)
        self.info_button_8.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_8.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_8.setText("")
        self.info_button_8.setIcon(icon1)
        self.info_button_8.setIconSize(QtCore.QSize(23, 23))
        self.info_button_8.setAutoRaise(False)
        self.info_button_8.setObjectName("info_button_8")
        self.horizontalLayout_3.addWidget(self.info_button_8)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ew_label_7 = QtWidgets.QLabel()
        self.ew_label_7.setEnabled(False)
        self.ew_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_7.setFont(font)
        self.ew_label_7.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ew_label_7.setObjectName("ew_label_7")
        self.horizontalLayout.addWidget(self.ew_label_7)
        self.ew_combobox_8 = QtWidgets.QComboBox()
        self.ew_combobox_8.setEnabled(False)
        self.ew_combobox_8.setMinimumSize(QtCore.QSize(110, 27))
        self.ew_combobox_8.setMaximumSize(QtCore.QSize(110, 27))
        self.ew_combobox_8.setFont(font2)
        self.ew_combobox_8.setStyleSheet("QComboBox {\n"
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
        self.ew_combobox_8.setObjectName("ew_combobox_8")
        self.ew_combobox_8.addItem("")
        self.ew_combobox_8.addItem("")
        self.ew_combobox_8.addItem("")
        self.horizontalLayout.addWidget(self.ew_combobox_8)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.info_button_13 = QtWidgets.QToolButton()
        self.info_button_13.setEnabled(False)
        self.info_button_13.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_13.setStyleSheet("QToolButton {\n"
                                          "    border: 1px solid transparent;\n"
                                          "    background-color: transparent;\n"
                                          "    width: 27px;\n"
                                          "    height: 27px;\n"
                                          "}\n"
                                          "\n"
                                          "QToolButton:flat {\n"
                                          "    border: none;\n"
                                          "}")
        self.info_button_13.setText("")
        self.info_button_13.setIcon(icon1)
        self.info_button_13.setIconSize(QtCore.QSize(23, 23))
        self.info_button_13.setAutoRaise(False)
        self.info_button_13.setObjectName("info_button_13")
        self.horizontalLayout.addWidget(self.info_button_13)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ew_checkbox_5 = QtWidgets.QCheckBox()
        self.ew_checkbox_5.setEnabled(False)
        self.ew_checkbox_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_checkbox_5.setFont(font)
        self.ew_checkbox_5.setStyleSheet("QCheckBox {\n"
                                         "   color: rgb(45,45,45);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox:disabled {\n"
                                         "    color: rgb(145,145,145);\n"
                                         "}")
        self.ew_checkbox_5.setChecked(True)
        self.ew_checkbox_5.setObjectName("ew_checkbox_5")
        self.horizontalLayout_4.addWidget(self.ew_checkbox_5)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_9 = QtWidgets.QToolButton()
        self.info_button_9.setEnabled(False)
        self.info_button_9.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_9.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid transparent;\n"
                                         "    background-color: transparent;\n"
                                         "    width: 27px;\n"
                                         "    height: 27px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:flat {\n"
                                         "    border: none;\n"
                                         "}")
        self.info_button_9.setText("")
        self.info_button_9.setIcon(icon1)
        self.info_button_9.setIconSize(QtCore.QSize(23, 23))
        self.info_button_9.setAutoRaise(False)
        self.info_button_9.setObjectName("info_button_9")
        self.horizontalLayout_4.addWidget(self.info_button_9)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ew_label_4 = QtWidgets.QLabel()
        self.ew_label_4.setEnabled(False)
        self.ew_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_4.setFont(font)
        self.ew_label_4.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_4.setObjectName("ew_label_4")
        self.gridLayout_2.addWidget(self.ew_label_4, 1, 0, 1, 1)
        self.ew_line_3 = QtWidgets.QLineEdit()
        self.ew_line_3.setEnabled(False)
        self.ew_line_3.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_3.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_3.setFont(font2)
        self.ew_line_3.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_3.setObjectName("ew_line_3")
        self.gridLayout_2.addWidget(self.ew_line_3, 2, 1, 1, 1)
        self.ew_line_2 = QtWidgets.QLineEdit()
        self.ew_line_2.setEnabled(False)
        self.ew_line_2.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_2.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_2.setFont(font2)
        self.ew_line_2.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_2.setObjectName("ew_line_2")
        self.gridLayout_2.addWidget(self.ew_line_2, 1, 1, 1, 1)
        self.ew_line_4 = QtWidgets.QLineEdit()
        self.ew_line_4.setEnabled(False)
        self.ew_line_4.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_4.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_4.setFont(font2)
        self.ew_line_4.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_4.setObjectName("ew_line_4")
        self.gridLayout_2.addWidget(self.ew_line_4, 0, 1, 1, 1)
        self.ew_label_3 = QtWidgets.QLabel()
        self.ew_label_3.setEnabled(False)
        self.ew_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_3.setFont(font)
        self.ew_label_3.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_3.setObjectName("ew_label_3")
        self.gridLayout_2.addWidget(self.ew_label_3, 0, 0, 1, 1)
        self.ew_label_5 = QtWidgets.QLabel()
        self.ew_label_5.setEnabled(False)
        self.ew_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_5.setFont(font)
        self.ew_label_5.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_5.setObjectName("ew_label_5")
        self.gridLayout_2.addWidget(self.ew_label_5, 2, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_2)
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ew_checkbox_6 = QtWidgets.QCheckBox()
        self.ew_checkbox_6.setEnabled(False)
        self.ew_checkbox_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_checkbox_6.setFont(font)
        self.ew_checkbox_6.setStyleSheet("QCheckBox {\n"
                                         "   color: rgb(45,45,45);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox:disabled {\n"
                                         "    color: rgb(145,145,145);\n"
                                         "}")
        self.ew_checkbox_6.setChecked(True)
        self.ew_checkbox_6.setObjectName("ew_checkbox_6")
        self.horizontalLayout_2.addWidget(self.ew_checkbox_6)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_10 = QtWidgets.QToolButton()
        self.info_button_10.setEnabled(False)
        self.info_button_10.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_10.setStyleSheet("QToolButton {\n"
                                          "    border: 1px solid transparent;\n"
                                          "    background-color: transparent;\n"
                                          "    width: 27px;\n"
                                          "    height: 27px;\n"
                                          "}\n"
                                          "\n"
                                          "QToolButton:flat {\n"
                                          "    border: none;\n"
                                          "}")
        self.info_button_10.setText("")
        self.info_button_10.setIcon(icon1)
        self.info_button_10.setIconSize(QtCore.QSize(23, 23))
        self.info_button_10.setAutoRaise(False)
        self.info_button_10.setObjectName("info_button_10")
        self.horizontalLayout_2.addWidget(self.info_button_10)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ew_label_8 = QtWidgets.QLabel()
        self.ew_label_8.setEnabled(False)
        self.ew_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_8.setFont(font)
        self.ew_label_8.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_8.setObjectName("ew_label_8")
        self.gridLayout.addWidget(self.ew_label_8, 0, 0, 1, 1)
        self.ew_line_5 = QtWidgets.QLineEdit()
        self.ew_line_5.setEnabled(False)
        self.ew_line_5.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_5.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_5.setFont(font2)
        self.ew_line_5.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_5.setObjectName("ew_line_5")
        self.gridLayout.addWidget(self.ew_line_5, 0, 1, 1, 1)
        self.gridLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                      QtWidgets.QSizePolicy.Minimum), 0, 2, 1, 1)
        self.ew_label_9 = QtWidgets.QLabel()
        self.ew_label_9.setEnabled(False)
        self.ew_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_9.setFont(font)
        self.ew_label_9.setStyleSheet("QLabel {\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:disabled {\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
        self.ew_label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_9.setObjectName("ew_label_9")
        self.gridLayout.addWidget(self.ew_label_9, 0, 3, 1, 1)
        self.ew_line_6 = QtWidgets.QLineEdit()
        self.ew_line_6.setEnabled(False)
        self.ew_line_6.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_6.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_6.setFont(font2)
        self.ew_line_6.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_6.setObjectName("ew_line_6")
        self.gridLayout.addWidget(self.ew_line_6, 0, 4, 1, 1)
        self.ew_label_10 = QtWidgets.QLabel()
        self.ew_label_10.setEnabled(False)
        self.ew_label_10.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_10.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_10.setFont(font)
        self.ew_label_10.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLabel:disabled {\n"
                                       "    color: rgb(145,145,145);\n"
                                       "}")
        self.ew_label_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_10.setObjectName("ew_label_10")
        self.gridLayout.addWidget(self.ew_label_10, 1, 0, 1, 1)
        self.ew_line_7 = QtWidgets.QLineEdit()
        self.ew_line_7.setEnabled(False)
        self.ew_line_7.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_7.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_7.setFont(font2)
        self.ew_line_7.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_7.setObjectName("ew_line_7")
        self.gridLayout.addWidget(self.ew_line_7, 1, 1, 1, 1)
        self.gridLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                      QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
        self.ew_label_12 = QtWidgets.QLabel()
        self.ew_label_12.setEnabled(False)
        self.ew_label_12.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_12.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_12.setFont(font)
        self.ew_label_12.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLabel:disabled {\n"
                                       "    color: rgb(145,145,145);\n"
                                       "}")
        self.ew_label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_12.setObjectName("ew_label_12")
        self.gridLayout.addWidget(self.ew_label_12, 1, 3, 1, 1)
        self.ew_line_9 = QtWidgets.QLineEdit()
        self.ew_line_9.setEnabled(False)
        self.ew_line_9.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_9.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_9.setFont(font2)
        self.ew_line_9.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_9.setObjectName("ew_line_9")
        self.gridLayout.addWidget(self.ew_line_9, 1, 4, 1, 1)
        self.ew_label_11 = QtWidgets.QLabel()
        self.ew_label_11.setEnabled(False)
        self.ew_label_11.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_11.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_11.setFont(font)
        self.ew_label_11.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLabel:disabled {\n"
                                       "    color: rgb(145,145,145);\n"
                                       "}")
        self.ew_label_11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_11.setObjectName("ew_label_11")
        self.gridLayout.addWidget(self.ew_label_11, 2, 0, 1, 1)
        self.ew_line_8 = QtWidgets.QLineEdit()
        self.ew_line_8.setEnabled(False)
        self.ew_line_8.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_8.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_8.setFont(font2)
        self.ew_line_8.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 3px;\n"
                                     "    padding: 1px 4px 1px 4px;\n"
                                     "    background-color:  rgb(240, 240, 240);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}\n"
                                     "    \n"
                                     "QLineEdit:disabled {\n"
                                     "    background-color:  rgb(200,200,200);\n"
                                     "    color: rgb(45,45,45);\n"
                                     "}")
        self.ew_line_8.setObjectName("ew_line_8")
        self.gridLayout.addWidget(self.ew_line_8, 2, 1, 1, 1)
        self.gridLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                      QtWidgets.QSizePolicy.Minimum), 2, 2, 1, 1)
        self.ew_label_13 = QtWidgets.QLabel()
        self.ew_label_13.setEnabled(False)
        self.ew_label_13.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_13.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ew_label_13.setFont(font)
        self.ew_label_13.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLabel:disabled {\n"
                                       "    color: rgb(145,145,145);\n"
                                       "}")
        self.ew_label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ew_label_13.setObjectName("ew_label_13")
        self.gridLayout.addWidget(self.ew_label_13, 2, 3, 1, 1)
        self.ew_line_10 = QtWidgets.QLineEdit()
        self.ew_line_10.setEnabled(False)
        self.ew_line_10.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_10.setMaximumSize(QtCore.QSize(70, 27))
        self.ew_line_10.setFont(font2)
        self.ew_line_10.setStyleSheet("QLineEdit {\n"
                                      "    border-radius: 3px;\n"
                                      "    padding: 1px 4px 1px 4px;\n"
                                      "    background-color:  rgb(240, 240, 240);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "    \n"
                                      "QLineEdit:disabled {\n"
                                      "    background-color:  rgb(200,200,200);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
        self.ew_line_10.setObjectName("ew_line_10")
        self.gridLayout.addWidget(self.ew_line_10, 2, 4, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout)
        self.horizontalLayout_7.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.ew_vertical_layout.addLayout(self.horizontalLayout_9)
        self.ew_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ew_label_2.setText("Choose a colormap:")
        self.ew_combobox_6.setItemText(0, "Make a choice...")
        self.ew_label_6.setText("Colormap position:")
        self.ew_combobox_7.setItemText(0, "horizontal - bottom")
        self.ew_combobox_7.setItemText(1, "horizontal - top")
        self.ew_combobox_7.setItemText(2, "vertical - left")
        self.ew_combobox_7.setItemText(3, "vertical - right")
        self.ew_checkbox_4.setText("Reverse colormap ?")
        self.ew_checkbox_5.setText("Handle colormap values automatically ?")
        self.ew_label_3.setText("min:")
        self.ew_label_4.setText("max:")
        self.ew_label_5.setText("nbr of steps:")
        self.ew_label_7.setText("Value used for colorization:")
        self.ew_combobox_8.setItemText(0, "mean")
        self.ew_combobox_8.setItemText(1, "first point")
        self.ew_combobox_8.setItemText(2, "last point")
        self.ew_checkbox_6.setText("Handle colormap dimensions automatically ?")
        self.ew_label_8.setText("figure width:")
        self.ew_label_9.setText("figure height:")
        self.ew_label_10.setText("position from left:")
        self.ew_label_12.setText("colormap width:")
        self.ew_label_11.setText("position from bottom:")
        self.ew_label_13.setText("colormap height:")
        self.ew_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_7.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_8.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_6.currentIndexChanged.connect(self.activate_colormap_options)
        self.ew_combobox_6.currentIndexChanged.connect(self.set_combobox_options)
        self.ew_combobox_6.currentIndexChanged.connect(self.activate_export_button)
        self.ew_combobox_7.currentIndexChanged.connect(self.set_combobox_options)
        self.ew_combobox_7.currentIndexChanged.connect(self.activate_export_button)
        self.ew_combobox_8.currentIndexChanged.connect(self.activate_export_button)
        self.ew_combobox_8.currentIndexChanged.connect(self.set_combobox_options)
        self.ew_checkbox_4.clicked.connect(self.set_checkbox_options)
        self.ew_checkbox_4.clicked.connect(self.activate_export_button)
        self.ew_checkbox_5.clicked.connect(self.activate_colormap_values)
        self.ew_checkbox_5.clicked.connect(self.set_checkbox_options)
        self.ew_checkbox_5.clicked.connect(self.activate_export_button)
        self.ew_checkbox_6.clicked.connect(self.activate_colormap_dimensions)
        self.ew_checkbox_6.clicked.connect(self.set_checkbox_options)
        self.ew_checkbox_6.clicked.connect(self.activate_export_button)
        self.ew_line_4.textChanged.connect(self.set_line_options)
        self.ew_line_2.textChanged.connect(self.set_line_options)
        self.ew_line_3.textChanged.connect(self.set_line_options)
        self.ew_line_5.textChanged.connect(self.set_line_options)
        self.ew_line_6.textChanged.connect(self.set_line_options)
        self.ew_line_7.textChanged.connect(self.set_line_options)
        self.ew_line_8.textChanged.connect(self.set_line_options)
        self.ew_line_9.textChanged.connect(self.set_line_options)
        self.ew_line_10.textChanged.connect(self.set_line_options)
        self.ew_line_4.textChanged.connect(self.activate_export_button)
        self.ew_line_2.textChanged.connect(self.activate_export_button)
        self.ew_line_3.textChanged.connect(self.activate_export_button)
        self.ew_line_5.textChanged.connect(self.activate_export_button)
        self.ew_line_6.textChanged.connect(self.activate_export_button)
        self.ew_line_7.textChanged.connect(self.activate_export_button)
        self.ew_line_8.textChanged.connect(self.activate_export_button)
        self.ew_line_9.textChanged.connect(self.activate_export_button)
        self.ew_line_10.textChanged.connect(self.activate_export_button)
        self.info_button_7.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_11.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_8.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_13.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_9.clicked.connect(self.export_ge_ts_button_info)
        self.info_button_10.clicked.connect(self.export_ge_ts_button_info)
        self.read_export_dict()

    def activate_colormap_dimensions(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_colormap_dimensions')
        if not self.ew_checkbox_6.isChecked():
            self.ew_line_5.setEnabled(True)
            self.ew_line_6.setEnabled(True)
            self.ew_line_7.setEnabled(True)
            self.ew_line_8.setEnabled(True)
            self.ew_line_9.setEnabled(True)
            self.ew_line_10.setEnabled(True)
            self.ew_line_5.setText('')
            self.ew_line_6.setText('')
            self.ew_line_7.setText('')
            self.ew_line_8.setText('')
            self.ew_line_9.setText('')
            self.ew_line_10.setText('')
            self.ew_label_8.setEnabled(True)
            self.ew_label_9.setEnabled(True)
            self.ew_label_10.setEnabled(True)
            self.ew_label_11.setEnabled(True)
            self.ew_label_12.setEnabled(True)
            self.ew_label_13.setEnabled(True)
        else:
            self.ew_line_5.setEnabled(False)
            self.ew_line_6.setEnabled(False)
            self.ew_line_7.setEnabled(False)
            self.ew_line_8.setEnabled(False)
            self.ew_line_9.setEnabled(False)
            self.ew_line_10.setEnabled(False)
            self.ew_line_5.setText('')
            self.ew_line_6.setText('')
            self.ew_line_7.setText('')
            self.ew_line_8.setText('')
            self.ew_line_9.setText('')
            self.ew_line_10.setText('')
            self.ew_label_8.setEnabled(False)
            self.ew_label_9.setEnabled(False)
            self.ew_label_10.setEnabled(False)
            self.ew_label_11.setEnabled(False)
            self.ew_label_12.setEnabled(False)
            self.ew_label_13.setEnabled(False)

    def activate_colormap_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_colormap_options')
        if self.ew_combobox_6.currentIndex() != 0:
            self.ew_label_6.setEnabled(True)
            self.ew_label_7.setEnabled(True)
            self.ew_combobox_7.setEnabled(True)
            self.ew_combobox_8.setEnabled(True)
            self.info_button_11.setEnabled(True)
            self.ew_checkbox_4.setEnabled(True)
            self.ew_checkbox_5.setEnabled(True)
            self.ew_checkbox_6.setEnabled(True)
            self.info_button_8.setEnabled(True)
            self.info_button_9.setEnabled(True)
            self.info_button_13.setEnabled(True)
            self.info_button_10.setEnabled(True)
            self.ew_combobox_7.setCurrentIndex(0)
            self.ew_combobox_8.setCurrentIndex(0)
            self.ew_checkbox_4.setChecked(False)
            self.ew_checkbox_5.setChecked(True)
            self.ew_checkbox_6.setChecked(True)
        else:
            self.ew_label_6.setEnabled(False)
            self.ew_label_7.setEnabled(False)
            self.ew_combobox_7.setEnabled(False)
            self.ew_combobox_8.setEnabled(False)
            self.info_button_11.setEnabled(False)
            self.ew_checkbox_4.setEnabled(False)
            self.ew_checkbox_5.setEnabled(False)
            self.ew_checkbox_6.setEnabled(False)
            self.info_button_8.setEnabled(False)
            self.info_button_9.setEnabled(False)
            self.info_button_13.setEnabled(False)
            self.info_button_10.setEnabled(False)
            self.ew_combobox_7.setCurrentIndex(0)
            self.ew_combobox_8.setCurrentIndex(0)
            self.ew_checkbox_4.setChecked(False)
            self.ew_checkbox_5.setChecked(True)
            self.ew_checkbox_6.setChecked(True)
            self.export_dict['Colormap']['automatic'] = True
        self.activate_colormap_values()

    def activate_colormap_values(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_colormap_values')
        if self.ew_checkbox_5.isChecked():
            self.ew_line_4.setEnabled(False)
            self.ew_line_2.setEnabled(False)
            self.ew_line_3.setEnabled(False)
            self.ew_line_4.setText('')
            self.ew_line_2.setText('')
            self.ew_line_3.setText('')
            self.ew_label_3.setEnabled(False)
            self.ew_label_4.setEnabled(False)
            self.ew_label_5.setEnabled(False)
        else:
            self.ew_line_4.setEnabled(True)
            self.ew_line_2.setEnabled(True)
            self.ew_line_3.setEnabled(True)
            self.ew_line_4.setText('')
            self.ew_line_2.setText('')
            self.ew_line_3.setText('')
            self.ew_label_3.setEnabled(True)
            self.ew_label_4.setEnabled(True)
            self.ew_label_5.setEnabled(True)

    def activate_transparency_checkbox(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_transparency_checkbox')
        if self.ew_checkbox_1.isChecked():
            self.ew_checkbox_2.setEnabled(True)
            self.ew_checkbox_2.setChecked(False)
            self.info_button_5.setEnabled(True)
        else:
            self.info_button_5.setEnabled(False)
            self.ew_checkbox_2.setEnabled(False)
            self.ew_checkbox_2.setChecked(False)
            self.export_dict['Options']['wall_transparency'] = False
        self.activate_transparency_slider()

    def activate_transparency_slider(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_transparency_slider')
        if self.ew_checkbox_2.isChecked():
            self.ew_label_2.setEnabled(True)
            self.ew_slider_1.setEnabled(True)
            self.ew_label_3.setEnabled(True)
            self.ew_label_3.setText('0 %')
            self.ew_slider_1.setValue(0)
        else:
            self.ew_label_2.setEnabled(False)
            self.ew_slider_1.setEnabled(False)
            self.ew_label_3.setEnabled(False)
            self.ew_label_3.setText('0 %')
            self.ew_slider_1.setValue(0)

    def update_slider_value(self, val):
        logging.debug('gui - export_window_functions.py - MyExport - update_slider_value')
        if self.sender().objectName() == 'ew_slider_1':
            self.ew_label_3.setText(str(val) + ' %')
        elif self.sender().objectName() == 'ew_slider_2':
            self.ew_label_6.setText(str(val) + ' px')

    def activate_reduce_value(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_reduce_value')
        if self.ew_checkbox_3.isChecked():
            self.ew_label_4.setEnabled(True)
            self.ew_line_1.setEnabled(True)
            self.ew_line_1.setText('')
        else:
            self.ew_label_4.setEnabled(False)
            self.ew_line_1.setEnabled(False)
            self.ew_line_1.setText('')

    def remove_variable_from_list(self, item):
        logging.debug('gui - export_window_functions.py - MyExport - remove_variable_from_list')
        self.export_dict['Variables'].remove(str(item.text()))
        self.ew_varlist_1.takeItem(self.ew_varlist_1.row(item))

    def set_line_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_line_options')
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_1':
            if self.ew_line_1.text():
                try:
                    self.export_dict['Options']['reduce_value'] = int(self.ew_line_1.text())
                except ValueError:
                    self.export_dict['Options']['reduce_value'] = None
            else:
                self.export_dict['Options']['reduce_value'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_4':
            if self.ew_line_4.text():
                try:
                    self.export_dict['Colormap']['min'] = float(self.ew_line_4.text())
                except ValueError:
                    self.export_dict['Colormap']['min'] = None
            else:
                self.export_dict['Colormap']['min'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_2':
            if self.ew_line_2.text():
                try:
                    self.export_dict['Colormap']['max'] = float(self.ew_line_2.text())
                except ValueError:
                    self.export_dict['Colormap']['max'] = None
            else:
                self.export_dict['Colormap']['max'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_3':
            if self.ew_line_3.text():
                try:
                    self.export_dict['Colormap']['steps'] = float(self.ew_line_3.text())
                except ValueError:
                    self.export_dict['Colormap']['steps'] = None
            else:
                self.export_dict['Colormap']['steps'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_5':
            if self.ew_line_5.text():
                try:
                    self.export_dict['Colormap']['fig_width'] = float(self.ew_line_5.text())
                except ValueError:
                    self.export_dict['Colormap']['fig_width'] = None
            else:
                self.export_dict['Colormap']['fig_width'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_6':
            if self.ew_line_6.text():
                try:
                    self.export_dict['Colormap']['fig_height'] = float(self.ew_line_6.text())
                except ValueError:
                    self.export_dict['Colormap']['fig_height'] = None
            else:
                self.export_dict['Colormap']['fig_height'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_7':
            if self.ew_line_7.text():
                try:
                    self.export_dict['Colormap']['pos_left'] = float(self.ew_line_7.text())
                except ValueError:
                    self.export_dict['Colormap']['pos_left'] = None
            else:
                self.export_dict['Colormap']['pos_left'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_8':
            if self.ew_line_8.text():
                try:
                    self.export_dict['Colormap']['pos_bottom'] = float(self.ew_line_8.text())
                except ValueError:
                    self.export_dict['Colormap']['pos_bottom'] = None
            else:
                self.export_dict['Colormap']['pos_bottom'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_9':
            if self.ew_line_9.text():
                try:
                    self.export_dict['Colormap']['width'] = float(self.ew_line_9.text())
                except ValueError:
                    self.export_dict['Colormap']['width'] = None
            else:
                self.export_dict['Colormap']['width'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_line_10':
            if self.ew_line_10.text():
                try:
                    self.export_dict['Colormap']['height'] = float(self.ew_line_10.text())
                except ValueError:
                    self.export_dict['Colormap']['height'] = None
            else:
                self.export_dict['Colormap']['height'] = None

    def set_slider_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_slider_options')
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_slider_1':
            self.export_dict['Options']['transparency'] = int(self.ew_slider_1.value())
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_slider_2':
            self.export_dict['Options']['path_width'] = int(self.ew_slider_2.value())

    def set_checkbox_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_checkbox_options')
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_checkbox_1':
            if self.ew_checkbox_1.isChecked():
                self.export_dict['Options']['wall'] = True
            else:
                self.export_dict['Options']['wall'] = False
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_checkbox_2':
            if self.ew_checkbox_2.isChecked():
                self.export_dict['Options']['wall_transparency'] = True
            else:
                self.export_dict['Options']['wall_transparency'] = False
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_checkbox_3':
            if self.ew_checkbox_3.isChecked():
                self.export_dict['Options']['reduce_samples'] = True
            else:
                self.export_dict['Options']['reduce_samples'] = False
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_checkbox_4':
            if self.ew_checkbox_4.isChecked():
                self.export_dict['Colormap']['reversed'] = True
            else:
                self.export_dict['Colormap']['reversed'] = False
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_checkbox_5':
            if self.ew_checkbox_5.isChecked():
                self.export_dict['Colormap']['automatic'] = True
            else:
                self.export_dict['Colormap']['automatic'] = False
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_checkbox_6':
            if self.ew_checkbox_6.isChecked():
                self.export_dict['Colormap']['auto_dimension'] = True
            else:
                self.export_dict['Colormap']['auto_dimension'] = False

    def set_button_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_button_options')
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_add_button':
            if self.ew_combobox_5.currentText() != 'Make a choice...':
                if self.ew_combobox_5.currentText() not in self.export_dict['Variables']:
                    if len(self.export_dict['Variables']) < 1:  # MODIFY ONCE WINDOW IS READY
                        self.ew_varlist_1.addItem(self.ew_combobox_5.currentText())
                        self.export_dict['Variables'].append(self.ew_combobox_5.currentText())

    def set_combobox_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_combobox_options')
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_combobox_2':
            if self.ew_combobox_2.currentText() != 'Make a choice...':
                self.export_dict['Coordinates']['lon'] = self.ew_combobox_2.currentText()
            else:
                self.export_dict['Coordinates']['lon'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_combobox_3':
            if self.ew_combobox_3.currentText() != 'Make a choice...':
                self.export_dict['Coordinates']['lat'] = self.ew_combobox_3.currentText()
            else:
                self.export_dict['Coordinates']['lat'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_combobox_4':
            if self.ew_combobox_4.currentText() == 'Make a choice...':
                self.export_dict['Coordinates']['alt'] = None
            elif self.ew_combobox_4.currentText() == 'Stick path to ground':
                self.export_dict['Coordinates']['alt'] = 'ground'
            else:
                self.export_dict['Coordinates']['alt'] = self.ew_combobox_4.currentText()
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_combobox_6':
            if self.ew_combobox_6.currentText() != 'Make a choice...':
                self.export_dict['Colormap']['colormap'] = self.colormap_dict[self.ew_combobox_6.currentIndex()]
            else:
                self.export_dict['Colormap']['colormap'] = None
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_combobox_7':
            self.export_dict['Colormap']['position'] = int(self.ew_combobox_7.currentIndex())
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_combobox_8':
            self.export_dict['Colormap']['color_value'] = int(self.ew_combobox_8.currentIndex())

    def read_export_dict(self):
        logging.debug('gui - export_window_functions.py - MyExport - read_export_dict')
        if self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Coordinates':
            if self.export_dict['Coordinates']['lon'] is not None:
                self.ew_combobox_2.setCurrentIndex(self.ew_combobox_2.findText(self.export_dict['Coordinates']['lon']))
            if self.export_dict['Coordinates']['lat'] is not None:
                self.ew_combobox_3.setCurrentIndex(self.ew_combobox_3.findText(self.export_dict['Coordinates']['lat']))
            if self.export_dict['Coordinates']['alt'] is not None:
                if self.export_dict['Coordinates']['alt'] == 'ground':
                    self.ew_combobox_4.setCurrentIndex(1)
                else:
                    self.ew_combobox_4.setCurrentIndex(self.ew_combobox_4.findText(self.export_dict['Coordinates']
                                                                                   ['alt']))
        elif self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Variables':
            if self.export_dict['Variables']:
                self.ew_varlist_1.addItems(self.export_dict['Variables'])
        elif self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Options':
            self.ew_slider_2.setValue(self.export_dict['Options']['path_width'])
            if self.export_dict['Options']['wall']:
                self.ew_checkbox_1.setChecked(True)
                self.activate_transparency_checkbox()
            if self.export_dict['Options']['wall_transparency']:
                self.ew_checkbox_2.setChecked(True)
                self.activate_transparency_slider()
                self.ew_slider_1.setValue(self.export_dict['Options']['transparency'])
            if self.export_dict['Options']['reduce_samples']:
                self.ew_checkbox_3.setChecked(True)
                self.activate_reduce_value()
                if self.export_dict['Options']['reduce_value'] is not None:
                    self.ew_line_1.setText(str(self.export_dict['Options']['reduce_value']))
        elif self.export_format == 'GE-TS' and self.ew_option_list.currentItem().text() == 'Colormap':
            if self.export_dict['Colormap']['colormap'] is not None:
                for key, value in self.colormap_dict.items():
                    if self.export_dict['Colormap']['colormap'] == value:
                        self.ew_combobox_6.setCurrentIndex(key)
            self.ew_combobox_7.setCurrentIndex(self.export_dict['Colormap']['position'])
            self.ew_combobox_8.setCurrentIndex(self.export_dict['Colormap']['color_value'])
            if self.export_dict['Colormap']['reversed']:
                self.ew_checkbox_4.setChecked(True)
            if not self.export_dict['Colormap']['automatic']:
                self.ew_checkbox_5.setChecked(False)
                self.activate_colormap_values()
                if self.export_dict['Colormap']['min'] is not None:
                    self.ew_line_4.setText(str(self.export_dict['Colormap']['min']))
                if self.export_dict['Colormap']['max'] is not None:
                    self.ew_line_2.setText(str(self.export_dict['Colormap']['max']))
                if self.export_dict['Colormap']['steps'] is not None:
                    self.ew_line_3.setText(str(self.export_dict['Colormap']['steps']))
            if not self.export_dict['Colormap']['auto_dimension']:
                self.ew_checkbox_6.setChecked(False)
                self.activate_colormap_dimensions()
                if self.export_dict['Colormap']['fig_width'] is not None:
                    self.ew_line_5.setText(str(self.export_dict['Colormap']['fig_width']))
                if self.export_dict['Colormap']['fig_height'] is not None:
                    self.ew_line_6.setText(str(self.export_dict['Colormap']['fig_height']))
                if self.export_dict['Colormap']['pos_left'] is not None:
                    self.ew_line_7.setText(str(self.export_dict['Colormap']['pos_left']))
                if self.export_dict['Colormap']['pos_bottom'] is not None:
                    self.ew_line_8.setText(str(self.export_dict['Colormap']['pos_bottom']))
                if self.export_dict['Colormap']['width'] is not None:
                    self.ew_line_9.setText(str(self.export_dict['Colormap']['width']))
                if self.export_dict['Colormap']['height'] is not None:
                    self.ew_line_10.setText(str(self.export_dict['Colormap']['height']))

    def activate_export_button(self):
        coordinate, variables, colormap = True, False, True
        if self.export_dict['Coordinates']['lon'] is None:
            coordinate = False
        if self.export_dict['Coordinates']['lat'] is None:
            coordinate = False
        if self.export_dict['Coordinates']['alt'] is None:
            coordinate = False
        if self.export_dict['Variables']:
            variables = True
        if self.export_dict['Colormap']['colormap'] is None:
            colormap = False
        if coordinate and variables and colormap:
            self.ew_export_button.setEnabled(True)
        else:
            self.ew_export_button.setEnabled(False)

    def export_function(self):
        logging.debug('gui - export_window_functions.py - MyExport - export_function')
        file_name, file_ext = self.get_file_name()
        if file_name:
            if not ntpath.splitext(ntpath.basename(file_name))[1]:
                if file_ext == 'Google Earth KML (*.kml)':
                    file_name += '.kml'
                else:
                    file_name += '.kmz'
            self.export_window = MyWaitExport(self.export_format, self.export_dict,
                                              self.list_of_variables_and_attributes, file_name, file_ext)
            self.export_window.exec_()
            error_occurred = self.export_window.error_occurred
            success = self.export_window.success
            if error_occurred:
                info_str = ('An important error occurred during the process. Please read the log file to check which '
                            'kind or error occurred.')
                self.infoWindow = MyInfo(info_str)
                self.infoWindow.exec_()
            if success:
                info_str = 'The file has been well exported.'
                self.infoWindow = MyInfo(info_str)
                self.infoWindow.exec_()

    def get_file_name(self):
        logging.debug('gui - export_window_functions.py - MyExport - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        filter_types = 'Google Earth KML (*.kml);;Google Earth KMZ (*.kmz)'
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
        return str(out_file_name), str(out_file_ext)

    def export_button_info(self):
        logging.debug('gui - export_window_functions.py - MyExport - export_button_info')
        self.infoWindow = MyInfo(self.main_information_buttons_text[self.sender().objectName()])
        self.infoWindow.exec_()

    def export_ge_ts_button_info(self):
        logging.debug('gui - export_window_functions.py - MyExport - export_ge_ts_button_info')
        self.infoWindow = MyInfo(self.ge_ts_information_buttons_text[self.sender().objectName()])
        self.infoWindow.exec_()

    def closeWindow(self):
        logging.debug('gui - export_window_functions.py - MyExport - closeWindow')
        self.close()


class MyWaitExport(QtWidgets.QDialog, Ui_waitWindow):
    def __init__(self, export_format, export_dict, var_dict, file_name, file_ext):
        logging.debug('gui - export_window_functions.py - MyWaitExport - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.export_format = export_format
        self.export_dict = export_dict
        self.var_dict = var_dict
        self.file_name = file_name
        self.file_ext = file_ext
        self.label.setText('Please wait...')
        self.spinner = None
        self.export_thread = None
        self.error_occurred = False
        self.success = True
        self.setup_spinner()
        self.launch_export_thread()
        logging.info('gui - export_window_functions.py - MyWaitExport - ready')

    def launch_export_thread(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - launch_export_thread')
        self.export_thread = ExportThread(self.export_format, self.export_dict, self.var_dict, self.file_name,
                                          self.file_ext)
        self.export_thread.start()
        self.export_thread.finished.connect(self.export_finished)
        self.export_thread.error.connect(self.export_failed)

    def export_finished(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - export_finished')
        self.close()

    def export_failed(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - export_failed')
        self.error_occurred = True
        self.success = False
        self.close()

    def setup_spinner(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - setup_spinner')
        self.spinner = QtWaitingSpinner(self, centerOnParent=False)
        self.verticalLayout.addWidget(self.spinner)
        self.spinner.setRoundness(70.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(12)
        self.spinner.setLineLength(10)
        self.spinner.setLineWidth(5)
        self.spinner.setInnerRadius(10)
        self.spinner.setRevolutionsPerSecond(1)
        self.spinner.setColor(QtGui.QColor(45, 45, 45))
        self.spinner.start()

    def closeWindow(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - closeWindow')
        self.close()
