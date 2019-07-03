import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_globalattributewindow import Ui_globalAttributeWindow
from ui.Ui_variableattributewindow import Ui_variableAttributeWindow
from ui.Ui_navariableattributewindow import Ui_naVariableAttributeWindow
from functions.utils import clear_layout


class MyGlobalAttributes(QtWidgets.QDialog, Ui_globalAttributeWindow):
    def __init__(self, global_attributes, open_file_ext):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.gw_addAttribute_rl.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.global_attributes = global_attributes
        self.open_file_ext = open_file_ext
        self.gw_showButton.clicked.connect(self.other_attribute)
        self.gw_okButton.clicked.connect(self.close_window_save)
        self.gw_cancelButton.clicked.connect(self.close_window)
        self.gw_button_1.clicked.connect(self.add_attribute)
        if self.open_file_ext == 'NetCDF Files (*.nc)':
            self.populate_attribute_netcdf()
        elif self.open_file_ext == 'NASA Ames Files (*.na)':
            clear_layout(self.verticalLayout_3)
            self.gw_addAttribute_lb.setVisible(False)
            self.gw_addAttribute_rl.setVisible(False)
            self.gw_button_1.setVisible(False)
            self.splitter.setSizes([177, 400, 0])
            self.populate_attribute_nasaames()
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_del = []
        self.add_attribute_num = 0
        self.attribute_num = 0
        self.combobox_items = ["comment",
                               "date_created",
                               "geospatial_lat_min",
                               "geospatial_lat_max",
                               "geospatial_lon_min",
                               "geospatial_lon_max",
                               "geospatial_vertical_min",
                               "geospatial_vertical_max",
                               "geospatial_vertical_positive",
                               "geospatial_vertical_units",
                               "history", "project",
                               "references",
                               "time_coverage_start",
                               "time_coverage_end",
                               "time_coverage_duration"]
        self.na_metadata_not_for_user = ['NLHEAD',
                                         'FFI',
                                         'IVOL',
                                         'NVOL',
                                         'DX',
                                         'NIV',
                                         'NV',
                                         'VSCAL',
                                         'VMISS',
                                         'VNAME',
                                         'NSCOML',
                                         'NNCOML',
                                         'ORG',
                                         'SNAME',
                                         'MNAME']
        self.populate_combobox()
        logging.info('gui - metadata_windows_functions.py - MyGlobalAttributes - ready')

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - close_window')
        self.global_attributes = None
        self.close()
        
    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - close_window_save')
        try:
            if self.open_file_ext == 'NetCDF Files (*.nc)':
                self.global_attributes["Conventions"] = str(self.gw_conventions_ln.text())
                self.global_attributes["title"] = str(self.gw_title_ln.text())
                self.global_attributes["institution"] = str(self.gw_institution_ln.text())
                self.global_attributes["source"] = str(self.gw_source_ln.text())
            elif self.open_file_ext == 'NASA Ames Files (*.na)':
                self.global_attributes["MNAME"] = str(self.gw_title_ln.text())
                self.global_attributes["ORG"] = str(self.gw_institution_ln.text())
                self.global_attributes["SNAME"] = str(self.gw_source_ln.text())
            try:
                for index, widget in enumerate(self.list_label):
                    try:

                        if isinstance(self.list_line[index], QtWidgets.QPlainTextEdit):
                            self.global_attributes[str(widget.text()[:-1])] = float(self.list_line[index].toPlainText())
                        else:
                            self.global_attributes[str(widget.text()[:-1])] = float(self.list_line[index].text())
                    except ValueError:
                        if isinstance(self.list_line[index], QtWidgets.QPlainTextEdit):
                            self.global_attributes[str(widget.text()[:-1])] = str(self.list_line[index].toPlainText())
                        else:
                            self.global_attributes[str(widget.text()[:-1])] = str(self.list_line[index].text())
            except AttributeError:
                pass
            for index, widget in enumerate(self.add_list_label):
                try:
                    self.global_attributes[str(widget.text())]
                except KeyError:
                    try:
                        self.global_attributes[str(widget.text()[:-1])] = float(self.add_list_line[index].text())
                    except ValueError:
                        self.global_attributes[str(widget.text()[:-1])] = str(self.add_list_line[index].text())
            self.close()
        except Exception:
            logging.exception("gui - metadata_windows_functions.py - MyGlobalAttributes - close_window_save : an "
                              "exception occured")

    def add_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - add_attribute : gw_addAttribu'
                      + 'te_rl.currentText() ' + str(self.gw_addAttribute_rl.currentText()))
        selected_attribute = self.gw_addAttribute_rl.currentText()
        if selected_attribute != "Make a choice...":
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font2 = QtGui.QFont()
            font2.setFamily("fonts/SourceSansPro-Regular.ttf")
            font2.setPointSize(9)
            font2.setKerning(True)
            font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if selected_attribute == "Other..." or selected_attribute == "long_name_<xx>":
                self.add_list_label.append(QtWidgets.QLineEdit())
                self.add_list_label[self.add_attribute_num].setFrame(False)
                self.add_list_label[self.add_attribute_num].setStyleSheet("QLineEdit {\n"
                                                                          "  border-radius: 3px;\n"
                                                                          "  padding: 1px 4px 1px 4px;\n"
                                                                          "  background-color: rgb(240, 240, 240);\n"
                                                                          "  color: rgb(45,45,45);\n"
                                                                          "}\n"
                                                                          "\n"
                                                                          "QLineEdit:disabled {\n"
                                                                          "  background-color: rgb(240, 240, 240);\n"
                                                                          "}")
                self.add_list_label[self.add_attribute_num].setFont(font2)
                if selected_attribute == "long_name_<xx>":
                    self.add_list_label[self.add_attribute_num].setText("long_name_")
            else:
                self.add_list_label.append(QtWidgets.QLabel())
                self.add_list_label[self.add_attribute_num].setFont(font)
                self.add_list_label[self.add_attribute_num].setToolTip(selected_attribute)
                self.add_list_label[self.add_attribute_num].setText(selected_attribute + ':')
                self.add_list_label[self.add_attribute_num].setStyleSheet("QLabel {\n"
                                                                          "   color: rgb(45,45,45);\n"
                                                                          "}")
                self.add_list_label[self.add_attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing
                                                                         | QtCore.Qt.AlignVCenter)
            self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
            self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.add_list_label[self.add_attribute_num].setObjectName("add_label_" + str(self.add_attribute_num))
            self.gridLayout_3.addWidget(self.add_list_label[self.add_attribute_num], self.add_attribute_num, 0, 1, 1)
            self.add_list_line.append(QtWidgets.QLineEdit())
            self.add_list_line[self.add_attribute_num].setEnabled(True)
            self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
            self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.add_list_line[self.add_attribute_num].setPalette(palette)
            self.add_list_line[self.add_attribute_num].setFrame(False)
            self.add_list_line[self.add_attribute_num].setObjectName("add_line_" + str(self.add_attribute_num))
            self.add_list_line[self.add_attribute_num].setFocus(True)
            self.add_list_line[self.add_attribute_num].setStyleSheet("QLineEdit {\n"
                                                                     "  border-radius: 3px;\n"
                                                                     "  padding: 1px 4px 1px 4px;\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "  color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QLineEdit:disabled {\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "}")
            self.add_list_line[self.add_attribute_num].setFont(font2)
            self.gridLayout_3.addWidget(self.add_list_line[self.add_attribute_num], self.add_attribute_num, 1, 1, 1)
            self.add_list_del.append(QtWidgets.QToolButton())
            self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setText("")
            self.add_list_del[self.add_attribute_num].setIcon(icon)
            self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(23, 23))
            self.add_list_del[self.add_attribute_num].setAutoRaise(True)
            self.add_list_del[self.add_attribute_num].setObjectName("add_list_del_" + str(self.add_attribute_num))
            self.add_list_del[self.add_attribute_num].setStyleSheet("QToolButton {\n"
                                                                    "    border: 1px solid transparent;\n"
                                                                    "    background-color: transparent;\n"
                                                                    "    width: 27px;\n"
                                                                    "    height: 27px;\n"
                                                                    "}\n"
                                                                    "\n"
                                                                    "QToolButton:flat {\n"
                                                                    "    border: none;\n"
                                                                    "}")
            self.gridLayout_3.addWidget(self.add_list_del[self.add_attribute_num], self.add_attribute_num, 2, 1, 1)
            self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
            self.add_attribute_num += 1
    
    def populate_attribute_netcdf(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf')
        try:
            self.gw_conventions_ln.setText(self.global_attributes["Conventions"])
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'Conventions key')
            pass
        try:
            self.gw_title_ln.setText(self.global_attributes["title"])
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'title key')
            pass
        try:
            self.gw_institution_ln.setText(self.global_attributes["institution"])
            self.gw_institution_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'institution key')
            pass
        try:
            self.gw_source_ln.setText(self.global_attributes["source"])
            self.gw_source_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'source key')
            pass

    def populate_attribute_nasaames(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_nasaames')
        try:
            self.gw_conventions_ln.setText('NASA Ames')
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_nasaames : '
                          'no Conventions key')
            pass
        try:
            self.gw_title_lb.setText('title - MNAME:')
            self.gw_title_ln.setText(self.global_attributes["MNAME"])
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_nasaames : '
                          'no title key')
            pass
        try:
            self.gw_institution_lb.setText('institution - ORG:')
            self.gw_institution_ln.setText(self.global_attributes["ORG"])
            self.gw_institution_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_nasaames : '
                          'no institution key')
            pass
        try:
            self.gw_source_lb.setText('source - SNAME:')
            self.gw_source_ln.setText(self.global_attributes["SNAME"])
            self.gw_source_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_nasaames : '
                          'no source key')
            pass

    def other_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - other_attribute : '
                      'gw_showButton.text() ' + str(self.gw_showButton.text()))
        if self.gw_showButton.text() == "Show other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            for key, value in sorted(self.global_attributes.items()):
                if (key != "Conventions" and key != "title" and key != "institution" and key != "source" and key not
                        in self.na_metadata_not_for_user):
                    font = QtGui.QFont()
                    font.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font.setPointSize(10)
                    font.setKerning(True)
                    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    font2 = QtGui.QFont()
                    font2.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font2.setPointSize(9)
                    font2.setKerning(True)
                    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.list_label.append(QtWidgets.QLabel()) 
                    self.list_label[self.attribute_num].setFont(font)
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
                    self.list_label[self.attribute_num].setText(key + ':')
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_label[self.attribute_num].setStyleSheet("QLabel {\n"
                                                                      "   color: rgb(45,45,45);\n"
                                                                      "}")
                    self.list_label[self.attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                     QtCore.Qt.AlignVCenter)
                    self.other_attributes_layout.addWidget(self.list_label[self.attribute_num], self.attribute_num,
                                                           0, 1, 1)
                    if key == "SCOM" or key == "NCOM":
                        self.list_line.append(QtWidgets.QPlainTextEdit())
                        self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 100))
                        self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 100))
                        self.list_line[self.attribute_num].setFrameShape(QtWidgets.QFrame.NoFrame)
                        self.list_line[self.attribute_num].setPlainText(str(value))
                        self.list_line[self.attribute_num].setStyleSheet("QPlainTextEdit {\n"
                                                                         "    border-radius: 3px;\n"
                                                                         "    padding: 1px 0px 1px 4px;\n"
                                                                         "    background-color:  rgb(240, 240, 240);\n"
                                                                         "    color: rgb(45,45,45);\n"
                                                                         "}\n"
                                                                         "    \n"
                                                                         "QPlainTextEdit:disabled {\n"
                                                                         "    background-color:  rgb(240, 240, 240);\n"
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
                                                                         "  border-bottom: 1px solid rgb(240,240,"
                                                                         "240);\n"
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
                                                                         "QScrollBar::right-arrow:horizontal:pressed "
                                                                         "{\n"
                                                                         "  right: -1px;\n"
                                                                         "  bottom: -1px;\n"
                                                                         "}")
                    else:
                        self.list_line.append(QtWidgets.QLineEdit())
                        self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                        self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                        self.list_line[self.attribute_num].setFrame(False)
                        self.list_line[self.attribute_num].setText(str(value))
                        self.list_line[self.attribute_num].setCursorPosition(0)
                        self.list_line[self.attribute_num].setStyleSheet("QLineEdit {\n"
                                                                         "  border-radius: 3px;\n"
                                                                         "  padding: 1px 4px 1px 4px;\n"
                                                                         "  background-color: rgb(240, 240, 240);\n"
                                                                         "  color: rgb(45,45,45);\n"
                                                                         "}\n"
                                                                         "\n"
                                                                         "QLineEdit:disabled {\n"
                                                                         "  background-color: rgb(240, 240, 240);\n"
                                                                         "}")
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setPalette(palette)
                    self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setFont(font2)
                    self.other_attributes_layout.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1,
                                                           1, 1)
                    if self.open_file_ext == 'NetCDF Files (*.nc)':
                        self.list_del.append(QtWidgets.QToolButton())
                        self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                        self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                        self.list_del[self.attribute_num].setText("")
                        self.list_del[self.attribute_num].setIcon(icon)
                        self.list_del[self.attribute_num].setIconSize(QtCore.QSize(23, 23))
                        self.list_del[self.attribute_num].setAutoRaise(True)
                        self.list_del[self.attribute_num].setObjectName("list_del_" + str(self.attribute_num))
                        self.list_del[self.attribute_num].setStyleSheet("QToolButton {\n"
                                                                        "    border: 1px solid transparent;\n"
                                                                        "    background-color: transparent;\n"
                                                                        "    width: 27px;\n"
                                                                        "    height: 27px;\n"
                                                                        "}\n"
                                                                        "\n"
                                                                        "QToolButton:flat {\n"
                                                                        "    border: none;\n"
                                                                        "}")
                        self.other_attributes_layout.addWidget(self.list_del[self.attribute_num], self.attribute_num, 2,
                                                               1, 1)
                        self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setEnabled(False)
                    if self.attribute_num > 0:
                        self.setTabOrder(self.list_line[self.attribute_num - 1], self.list_line[self.attribute_num])
                    self.attribute_num += 1   
            if self.attribute_num != 0:
                self.gw_showButton.setText("Hide other attributes")
            else:
                self.gw_showButton.setText("Hide other attributes")
                label = QtWidgets.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName("label")
                label.setText("No more attribute")
                self.other_attributes_layout.addWidget(label, 0, 0, 1, 1)
        elif self.gw_showButton.text() == "Hide other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            clear_layout(self.other_attributes_layout)
            self.gw_showButton.setText("Show other attributes")

    def delete_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - delete_attribute : sender('
                      ').objectName() ' + str(self.sender().objectName()))
        if "add" in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            self.add_list_label[index].deleteLater()
            self.add_list_label.pop(index)
            self.add_list_line[index].deleteLater()
            self.add_list_line.pop(index)
            self.add_list_del[index].deleteLater()
            self.add_list_del.pop(index)
            self.add_attribute_num -= 1
            if len(self.add_list_del) > 0:
                for i in range(0, len(self.add_list_del)):
                    self.add_list_line[i].setObjectName("add_line_" + str(i))
                    self.add_list_label[i].setObjectName("add_label_" + str(i))
                    self.add_list_del[i].setObjectName("add_list_del_" + str(i))
        else:
            index = int(self.sender().objectName()[9:])
            del self.global_attributes[str(self.list_label[index].text()[:-1])]
            self.list_label[index].deleteLater()
            self.list_label.pop(index)
            self.list_line[index].deleteLater()
            self.list_line.pop(index)
            self.list_del[index].deleteLater()
            self.list_del.pop(index)
            self.attribute_num -= 1
            if len(self.list_del) > 0:
                for i in range(0, len(self.list_del)):
                    self.list_line[i].setObjectName("line_" + str(i))
                    self.list_label[i].setObjectName("label_" + str(i))
                    self.list_del[i].setObjectName("list_del_" + str(i))

    def populate_combobox(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_combobox')
        self.gw_addAttribute_rl.addItem("Make a choice...")
        self.gw_addAttribute_rl.addItem("Other...")
        for item in self.combobox_items:
            try:
                if self.global_attributes[item] == "deleted":
                    self.gw_addAttribute_rl.addItem(item)
            except KeyError:
                self.gw_addAttribute_rl.addItem(item)


class MyVariableAttributes(QtWidgets.QDialog, Ui_variableAttributeWindow):
    def __init__(self, var, variable_attributes, open_file_ext):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - __init__ : var ' + str(var))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.vw_addAttribute_rl.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.variable = var
        self.open_file_ext = open_file_ext
        self.setWindowTitle('Variable attributes - ' + self.variable)
        self.attributes = variable_attributes
        self.vw_showButton.clicked.connect(self.other_attribute)
        self.vw_okButton.clicked.connect(self.close_window_save)
        self.vw_cancelButton.clicked.connect(self.close_window)
        self.vw_button_1.clicked.connect(self.add_attribute)
        self.combobox_items = ["ancillary_variables",
                               "CalibrationCoefficients",
                               "Category",
                               "Comments",
                               "Dependencies",
                               "flag_masks",
                               "flag_meaning",
                               "flag_values",
                               "InstrumentCoordinates",
                               "InstrumentLocation",
                               "long_name",
                               "long_name_<xx>",
                               "Processor",
                               "SampledRate",
                               "standard_name",
                               "valid_max",
                               "valid_min",
                               "valid_range"]
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_del = []
        self.add_attribute_num = 0
        self.populate_attribute()
        self.populate_combobox()
        if self.open_file_ext == 'NASA Ames Files (*.na)':
            clear_layout(self.verticalLayout_3)
            self.vw_addAttribute_lb.setVisible(False)
            self.vw_addAttribute_rl.setVisible(False)
            self.vw_button_1.setVisible(False)
            self.splitter.setSizes([177, 400, 0])
            self.populate_attribute_nasaames()
        logging.info('gui - metadata_windows_functions.py - MyVariableAttributes - ready')

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - close_window')
        self.attributes = None
        self.close()

    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - close_window_save')
        try:
            for index, widget in enumerate(self.list_label):
                try:
                    self.attributes[str(widget.text()[:-1])] = float(self.list_line[index].text())
                except ValueError:
                    self.attributes[str(widget.text()[:-1])] = str(self.list_line[index].text())
        except AttributeError:
            pass
        for index, widget in enumerate(self.add_list_label):
            try:
                self.attributes[str(widget.text())]
            except KeyError:
                try:
                    self.attributes[str(widget.text()[:-1])] = float(self.add_list_line[index].text())
                except ValueError:
                    self.attributes[str(widget.text()[:-1])] = str(self.add_list_line[index].text())
        self.close()

    def populate_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - populate_attribute')
        try:
            self.vw_units_ln.setText(str(self.attributes["units"]))
            self.vw_units_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyVariableAttributes - populate_attribute :no Units '
                          'attribute')
            pass
        try:
            self.vw_fillValue_ln.setText(str(self.attributes["_FillValue"]))
            self.vw_fillValue_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyVariableAttributes - populate_attribute : no '
                          'FillValue attribute')
            pass

    def other_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - other_attribute : '
                      'vw_showButton.text() ' + str(self.vw_showButton.text()))
        if self.vw_showButton.text() == "Show other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            for key, value in sorted(self.attributes.items()):
                if key != "units" and key != "_FillValue":
                    if isinstance(value, list):
                        value_string = ""
                        for string in value:
                            value_string += string + ", "
                        value = value_string[:-2]
                    font = QtGui.QFont()
                    font.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font.setPointSize(10)
                    font.setKerning(True)
                    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    font2 = QtGui.QFont()
                    font2.setFamily("fonts/SourceSansPro-Regular.ttf")
                    font2.setPointSize(9)
                    font2.setKerning(True)
                    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.list_label.append(QtWidgets.QLabel()) 
                    self.list_label[self.attribute_num].setFont(font)
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
                    self.list_label[self.attribute_num].setText(key + ':')
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_label[self.attribute_num].setStyleSheet("QLabel {\n"
                                                                      "   color: rgb(45,45,45);\n"
                                                                      "}")
                    self.list_label[self.attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                     QtCore.Qt.AlignVCenter)
                    self.other_attributes_layout.addWidget(self.list_label[self.attribute_num], self.attribute_num,
                                                           0, 1, 1)
                    self.list_line.append(QtWidgets.QLineEdit())
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_line[self.attribute_num].setPalette(palette)
                    self.list_line[self.attribute_num].setFrame(False)
                    self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
                    self.list_line[self.attribute_num].setText(str(value))
                    self.list_line[self.attribute_num].setCursorPosition(0)
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setStyleSheet("QLineEdit {\n"
                                                                     "  border-radius: 3px;\n"
                                                                     "  padding: 1px 4px 1px 4px;\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "  color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QLineEdit:disabled {\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "}")
                    self.list_line[self.attribute_num].setFont(font2)
                    self.other_attributes_layout.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1,
                                                           1, 1)
                    self.list_del.append(QtWidgets.QToolButton())
                    self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setText("")
                    self.list_del[self.attribute_num].setIcon(icon)
                    self.list_del[self.attribute_num].setIconSize(QtCore.QSize(23, 23))
                    self.list_del[self.attribute_num].setAutoRaise(True)
                    self.list_del[self.attribute_num].setObjectName("list_del_" + str(self.attribute_num))
                    self.list_del[self.attribute_num].setStyleSheet("QToolButton {\n"
                                                                    "    border: 1px solid transparent;\n"
                                                                    "    background-color: transparent;\n"
                                                                    "    width: 27px;\n"
                                                                    "    height: 27px;\n"
                                                                    "}\n"
                                                                    "\n"
                                                                    "QToolButton:flat {\n"
                                                                    "    border: none;\n"
                                                                    "}")
                    self.other_attributes_layout.addWidget(self.list_del[self.attribute_num], self.attribute_num, 2,
                                                           1, 1)
                    self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setEnabled(False)
                    if self.attribute_num > 0:
                        self.setTabOrder(self.list_line[self.attribute_num - 1], self.list_line[self.attribute_num])
                    self.attribute_num += 1     
            if self.attribute_num != 0:
                self.vw_showButton.setText("Hide other attributes")
            else:
                self.vw_showButton.setText("Hide other attributes")
                label = QtGui.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName("label")
                label.setText("No more attribute")
                label.setStyleSheet("QLabel {\n"
                                    "   color: rgb(45,45,45);\n"
                                    "}")
                self.other_attributes_layout.addWidget(label, 0, 0, 1, 1)
        elif self.vw_showButton.text() == "Hide other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            clear_layout(self.other_attributes_layout)
            self.vw_showButton.setText("Show other attributes")

    def add_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - add_attribute : vw_addAttribu'
                      + 'te_rl.currentText() ' + str(self.vw_addAttribute_rl.currentText()))
        selected_attribute = self.vw_addAttribute_rl.currentText()
        if selected_attribute == "Make a choice...":
            return
        else:
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font2 = QtGui.QFont()
            font2.setFamily("fonts/SourceSansPro-Regular.ttf")
            font2.setPointSize(9)
            font2.setKerning(True)
            font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if selected_attribute == "Other..." or selected_attribute == "long_name_<xx>":
                self.add_list_label.append(QtWidgets.QLineEdit())
                self.add_list_label[self.add_attribute_num].setFrame(False)
                self.add_list_label[self.add_attribute_num].setStyleSheet("QLineEdit {\n"
                                                                          "  border-radius: 3px;\n"
                                                                          "  padding: 1px 4px 1px 4px;\n"
                                                                          "  background-color: rgb(240, 240, 240);\n"
                                                                          "  color: rgb(45,45,45);\n"
                                                                          "}\n"
                                                                          "\n"
                                                                          "QLineEdit:disabled {\n"
                                                                          "  background-color: rgb(240, 240, 240);\n"
                                                                          "}")
                self.add_list_label[self.add_attribute_num].setFont(font2)
                if selected_attribute == "long_name_<xx>":
                    self.add_list_label[self.add_attribute_num].setText("long_name_")
            else:
                self.add_list_label.append(QtWidgets.QLabel())
                self.add_list_label[self.add_attribute_num].setFont(font)
                self.add_list_label[self.add_attribute_num].setToolTip(selected_attribute)
                self.add_list_label[self.add_attribute_num].setText(selected_attribute + ':')
                self.add_list_label[self.add_attribute_num].setStyleSheet("QLabel {\n"
                                                                          "   color: rgb(45,45,45);\n"
                                                                          "}")
                self.add_list_label[self.add_attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing
                                                                         | QtCore.Qt.AlignVCenter)
            self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
            self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.add_list_label[self.add_attribute_num].setObjectName("add_label_" + str(self.add_attribute_num))
            self.add_attribute_layout.addWidget(self.add_list_label[self.add_attribute_num], self.add_attribute_num,
                                                0, 1, 1)
            self.add_list_line.append(QtWidgets.QLineEdit())
            self.add_list_line[self.add_attribute_num].setEnabled(True)
            self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(400, 27))
            self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.add_list_line[self.add_attribute_num].setPalette(palette)
            self.add_list_line[self.add_attribute_num].setFrame(False)
            self.add_list_line[self.add_attribute_num].setObjectName("add_line_" + str(self.add_attribute_num))
            self.add_list_line[self.add_attribute_num].setFocus(True)
            self.add_list_line[self.add_attribute_num].setStyleSheet("QLineEdit {\n"
                                                                     "  border-radius: 3px;\n"
                                                                     "  padding: 1px 4px 1px 4px;\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "  color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QLineEdit:disabled {\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "}")
            self.add_list_line[self.add_attribute_num].setFont(font2)
            self.add_attribute_layout.addWidget(self.add_list_line[self.add_attribute_num], self.add_attribute_num,
                                                1, 1, 1)
            self.add_list_del.append(QtWidgets.QToolButton())
            self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
            self.add_list_del[self.add_attribute_num].setText("")
            self.add_list_del[self.add_attribute_num].setIcon(icon)
            self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(23, 23))
            self.add_list_del[self.add_attribute_num].setAutoRaise(True)
            self.add_list_del[self.add_attribute_num].setObjectName("add_list_del_" + str(self.add_attribute_num))
            self.add_list_del[self.add_attribute_num].setStyleSheet("QToolButton {\n"
                                                                    "    border: 1px solid transparent;\n"
                                                                    "    background-color: transparent;\n"
                                                                    "    width: 27px;\n"
                                                                    "    height: 27px;\n"
                                                                    "}\n"
                                                                    "\n"
                                                                    "QToolButton:flat {\n"
                                                                    "    border: none;\n"
                                                                    "}")
            self.add_attribute_layout.addWidget(self.add_list_del[self.add_attribute_num], self.add_attribute_num, 2,
                                                1, 1)
            self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
            self.add_attribute_num += 1

    def delete_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - delete_attribute : sender('
                      ').objectName() ' + str(self.sender().objectName()))
        if "add" in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            self.add_attribute_layout.removeWidget(self.add_list_label[index])
            self.add_attribute_layout.removeWidget(self.add_list_line[index])
            self.add_attribute_layout.removeWidget(self.add_list_del[index])
            self.add_list_label[index].deleteLater()
            self.add_list_label.pop(index)
            self.add_list_line[index].deleteLater()
            self.add_list_line.pop(index)
            self.add_list_del[index].deleteLater()
            self.add_list_del.pop(index)
            self.add_attribute_num -= 1
            row_number = self.add_attribute_layout.count() / 3
            if row_number > 0:
                for i in range(0, row_number):
                    self.add_list_line[i].setObjectName("add_line_" + str(i))
                    self.add_list_label[i].setObjectName("add_label_" + str(i))
                    self.add_list_del[i].setObjectName("add_list_del_" + str(i))
        else:
            index = int(self.sender().objectName()[9:])
            del self.attributes[str(self.list_label[index].text()[:-1])]
            self.other_attributes_layout.removeWidget(self.list_label[index])
            self.other_attributes_layout.removeWidget(self.list_line[index])
            self.other_attributes_layout.removeWidget(self.list_del[index])
            self.list_label[index].deleteLater()
            self.list_label.pop(index)
            self.list_line[index].deleteLater()
            self.list_line.pop(index)
            self.list_del[index].deleteLater()
            self.list_del.pop(index)
            self.attribute_num -= 1
            if len(self.list_del) > 0:
                for i in range(0, len(self.list_del)):
                    self.list_line[i].setObjectName("line_" + str(i))
                    self.list_label[i].setObjectName("label_" + str(i))
                    self.list_del[i].setObjectName("list_del_" + str(i))

    def populate_combobox(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - populate_combobox')
        self.vw_addAttribute_rl.addItem("Make a choice...")
        self.vw_addAttribute_rl.addItem("Other...")
        for item in self.combobox_items:
            try:
                if self.attributes[item] == "deleted":
                    self.vw_addAttribute_rl.addItem(item)
            except KeyError:
                self.vw_addAttribute_rl.addItem(item)


class MyNAVariableAttributes(QtWidgets.QDialog, Ui_naVariableAttributeWindow):
    def __init__(self, var, variable_attributes):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - __init__ : var ' + str(var))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.variable = var
        self.setWindowTitle('Variable attributes - ' + self.variable)
        self.attributes = variable_attributes
        self.vw_okButton.clicked.connect(self.close_window_save)
        self.vw_cancelButton.clicked.connect(self.close_window)
        self.populate_attribute()
        logging.info('gui - metadata_windows_functions.py - MyNAVariableAttributes - ready')

    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - close_window_save')
        self.attributes['units'] = str(self.vw_units_ln.text())
        self.attributes['_FillValue'] = str(self.vw_fillValue_ln.text())
        self.attributes['scale_factor'] = str(self.vw_scalefactor_ln.text())
        self.close()

    def populate_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute')
        try:
            self.vw_units_ln.setText(str(self.attributes["units"]))
            self.vw_units_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute :no Units '
                          'attribute')
            pass
        try:
            self.vw_fillValue_ln.setText(str(self.attributes["_FillValue"]))
            self.vw_fillValue_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute : no '
                          'FillValue attribute')
            pass
        try:
            self.vw_scalefactor_ln.setText(str(self.attributes["scale_factor"]))
            self.vw_scalefactor_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute : no '
                          'scale_factor attribute')
            pass

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - close_window')
        del self.attributes
        self.close()
