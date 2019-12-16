import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from functions.utils import populate_combobox, font_creation_function, icon_creation_function
from functions.plot_gd_option_secondary_functions import update_gd_slider_value, display_grid_projection_options
from functions.plot_gd_option_secondary_functions import set_projection_options, activate_boundaries_hex_rgb_color
from functions.plot_gd_option_secondary_functions import activate_coastlines_options, activate_lakes_options
from functions.plot_gd_option_secondary_functions import activate_grid_options, activate_colormap_dimensions
from functions.plot_gd_option_secondary_functions import activate_colormap_values, activate_colormap_options
from functions.plot_gd_option_secondary_functions import set_colormap_default_margins, projection_option_window
from functions.plot_gd_option_secondary_functions import tick_option_window, display_grid_ticks_options
from functions.plot_gd_option_secondary_functions import colorbar_tick_option_window, colorbar_tick_option_man_remove
from functions.material_functions import grid_projection_list
import matplotlib.pyplot as plt


def add_figure_options(self):
    logging.debug('gui - plot_gd_option_gui_functions.py - add_figure_options')
    font3 = font_creation_function('small')
    font2 = font_creation_function('big')
    font = font_creation_function('normal')
    icon = icon_creation_function('info_icon.svg')
    self.pw_figureOptions_hl_1 = QtWidgets.QHBoxLayout()
    self.pw_figureOptions_hl_1.setObjectName("pw_figureOptions_hl_1")
    self.pw_grid_label_46 = QtWidgets.QLabel()
    self.pw_grid_label_46.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_46.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_46.setFont(font2)
    self.pw_grid_label_46.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_46.setObjectName("pw_grid_label_46")
    self.pw_figureOptions_hl_1.addWidget(self.pw_grid_label_46)
    self.pw_figureOptions_hl_1.addItem(QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding,
                                                             QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_la.addLayout(self.pw_figureOptions_hl_1)
    self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_22.setObjectName("horizontalLayout_22")
    self.horizontalLayout_22.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_6 = QtWidgets.QGridLayout()
    self.gridLayout_6.setObjectName("gridLayout_6")
    self.pw_grid_label_2 = QtWidgets.QLabel()
    self.pw_grid_label_2.setMinimumSize(QtCore.QSize(100, 0))
    self.pw_grid_label_2.setMaximumSize(QtCore.QSize(100, 16777215))
    self.pw_grid_label_2.setFont(font)
    self.pw_grid_label_2.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_2.setWordWrap(True)
    self.pw_grid_label_2.setObjectName("pw_grid_label_2")
    self.gridLayout_6.addWidget(self.pw_grid_label_2, 0, 0, 1, 1)
    self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_23.setObjectName("horizontalLayout_23")
    self.gridLayout_7 = QtWidgets.QGridLayout()
    self.gridLayout_7.setObjectName("gridLayout_7")
    self.pw_grid_label_6 = QtWidgets.QLabel()
    self.pw_grid_label_6.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_6.setFont(font3)
    self.pw_grid_label_6.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_6.setObjectName("pw_grid_label_6")
    self.gridLayout_7.addWidget(self.pw_grid_label_6, 1, 2, 1, 1)
    self.pw_grid_label_3 = QtWidgets.QLabel()
    self.pw_grid_label_3.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_3.setFont(font)
    self.pw_grid_label_3.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_3.setObjectName("pw_grid_label_3")
    self.gridLayout_7.addWidget(self.pw_grid_label_3, 0, 0, 1, 1)
    self.pw_grid_slider_2 = QtWidgets.QSlider()
    self.pw_grid_slider_2.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_2.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_2.setStyleSheet("QSlider::groove:horizontal {\n"
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
                                        "}")
    self.pw_grid_slider_2.setMinimum(0)
    self.pw_grid_slider_2.setMaximum(40)
    self.pw_grid_slider_2.setSingleStep(1)
    self.pw_grid_slider_2.setPageStep(1)
    self.pw_grid_slider_2.setOrientation(QtCore.Qt.Horizontal)
    self.pw_grid_slider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_grid_slider_2.setTickInterval(4)
    self.pw_grid_slider_2.setObjectName("pw_grid_slider_2")
    self.gridLayout_7.addWidget(self.pw_grid_slider_2, 1, 1, 1, 1)
    self.pw_grid_slider_4 = QtWidgets.QSlider()
    self.pw_grid_slider_4.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_4.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_4.setStyleSheet("QSlider::groove:horizontal {\n"
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
                                        "QSlider::sub-page:horizontal {\n"
                                        "    background: rgb(200,200,200);\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::add-page:horizontal {\n"
                                        "    background: rgb(0,0,200);\n"
                                        "}")
    self.pw_grid_slider_4.setMinimum(0)
    self.pw_grid_slider_4.setMaximum(40)
    self.pw_grid_slider_4.setSingleStep(1)
    self.pw_grid_slider_4.setPageStep(1)
    self.pw_grid_slider_4.setProperty("value", 0)
    self.pw_grid_slider_4.setOrientation(QtCore.Qt.Horizontal)
    self.pw_grid_slider_4.setInvertedAppearance(True)
    self.pw_grid_slider_4.setInvertedControls(False)
    self.pw_grid_slider_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_grid_slider_4.setTickInterval(4)
    self.pw_grid_slider_4.setObjectName("pw_grid_slider_4")
    self.gridLayout_7.addWidget(self.pw_grid_slider_4, 1, 4, 1, 1)
    self.pw_grid_label_5 = QtWidgets.QLabel()
    self.pw_grid_label_5.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_5.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_5.setFont(font3)
    self.pw_grid_label_5.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_5.setObjectName("pw_grid_label_5")
    self.gridLayout_7.addWidget(self.pw_grid_label_5, 0, 2, 1, 1)
    self.pw_grid_label_9 = QtWidgets.QLabel()
    self.pw_grid_label_9.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_9.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_9.setFont(font3)
    self.pw_grid_label_9.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_9.setObjectName("pw_grid_label_9")
    self.gridLayout_7.addWidget(self.pw_grid_label_9, 0, 5, 1, 1)
    self.pw_grid_label_8 = QtWidgets.QLabel()
    self.pw_grid_label_8.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_8.setFont(font)
    self.pw_grid_label_8.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_8.setObjectName("pw_grid_label_8")
    self.gridLayout_7.addWidget(self.pw_grid_label_8, 1, 3, 1, 1)
    self.pw_grid_label_10 = QtWidgets.QLabel()
    self.pw_grid_label_10.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_10.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_10.setFont(font3)
    self.pw_grid_label_10.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_10.setObjectName("pw_grid_label_10")
    self.gridLayout_7.addWidget(self.pw_grid_label_10, 1, 5, 1, 1)
    self.pw_grid_slider_1 = QtWidgets.QSlider()
    self.pw_grid_slider_1.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_1.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_1.setStyleSheet("QSlider::groove:horizontal {\n"
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
                                        "}")
    self.pw_grid_slider_1.setMinimum(0)
    self.pw_grid_slider_1.setMaximum(40)
    self.pw_grid_slider_1.setSingleStep(1)
    self.pw_grid_slider_1.setPageStep(1)
    self.pw_grid_slider_1.setOrientation(QtCore.Qt.Horizontal)
    self.pw_grid_slider_1.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_grid_slider_1.setTickInterval(4)
    self.pw_grid_slider_1.setObjectName("pw_grid_slider_1")
    self.gridLayout_7.addWidget(self.pw_grid_slider_1, 0, 1, 1, 1)
    self.pw_grid_label_4 = QtWidgets.QLabel()
    self.pw_grid_label_4.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_4.setFont(font)
    self.pw_grid_label_4.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_4.setObjectName("pw_grid_label_4")
    self.gridLayout_7.addWidget(self.pw_grid_label_4, 1, 0, 1, 1)
    self.pw_grid_label_7 = QtWidgets.QLabel()
    self.pw_grid_label_7.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_7.setFont(font)
    self.pw_grid_label_7.setStyleSheet("QLabel {\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_label_7.setObjectName("pw_grid_label_7")
    self.gridLayout_7.addWidget(self.pw_grid_label_7, 0, 3, 1, 1)
    self.pw_grid_slider_3 = QtWidgets.QSlider()
    self.pw_grid_slider_3.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_3.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_grid_slider_3.setStyleSheet("QSlider::groove:horizontal {\n"
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
                                        "QSlider::sub-page:horizontal {\n"
                                        "    background: rgb(200,200,200);\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::add-page:horizontal {\n"
                                        "    background: rgb(0,0,200);\n"
                                        "}")
    self.pw_grid_slider_3.setMinimum(0)
    self.pw_grid_slider_3.setMaximum(40)
    self.pw_grid_slider_3.setSingleStep(1)
    self.pw_grid_slider_3.setPageStep(1)
    self.pw_grid_slider_3.setProperty("value", 0)
    self.pw_grid_slider_3.setOrientation(QtCore.Qt.Horizontal)
    self.pw_grid_slider_3.setInvertedAppearance(True)
    self.pw_grid_slider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_grid_slider_3.setTickInterval(4)
    self.pw_grid_slider_3.setObjectName("pw_grid_slider_3")
    self.gridLayout_7.addWidget(self.pw_grid_slider_3, 0, 4, 1, 1)
    self.horizontalLayout_23.addLayout(self.gridLayout_7)
    self.pw_grid_info_button_1 = QtWidgets.QToolButton()
    self.pw_grid_info_button_1.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_1.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_1.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_1.setIcon(icon)
    self.pw_grid_info_button_1.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_1.setObjectName("pw_grid_info_button_1")
    self.horizontalLayout_23.addWidget(self.pw_grid_info_button_1)
    self.horizontalLayout_23.addItem(QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_6.addLayout(self.horizontalLayout_23, 0, 1, 1, 1)
    self.gridLayout_6.addItem(QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum), 1, 0, 1, 1)
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
    self.gridLayout_6.addWidget(self.line, 1, 1, 1, 1)
    self.pw_grid_label_16 = QtWidgets.QLabel()
    self.pw_grid_label_16.setMinimumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_16.setMaximumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_16.setFont(font)
    self.pw_grid_label_16.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_16.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_16.setObjectName("pw_grid_label_16")
    self.gridLayout_6.addWidget(self.pw_grid_label_16, 2, 0, 1, 1)
    self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_24.setObjectName("horizontalLayout_24")
    self.pw_grid_line_1 = QtWidgets.QLineEdit()
    self.pw_grid_line_1.setMinimumSize(QtCore.QSize(240, 27))
    self.pw_grid_line_1.setMaximumSize(QtCore.QSize(240, 27))
    self.pw_grid_line_1.setFont(font3)
    self.pw_grid_line_1.setStyleSheet("QLineEdit {\n"
                                      "    border-radius: 3px;\n"
                                      "    padding: 1px 4px 1px 4px;\n"
                                      "    background-color:  rgb(240, 240, 240);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled {\n"
                                      "    background-color:  rgb(200,200,200);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
    self.pw_grid_line_1.setObjectName("pw_grid_line_1")
    self.horizontalLayout_24.addWidget(self.pw_grid_line_1)
    self.horizontalLayout_24.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_19 = QtWidgets.QLabel()
    self.pw_grid_label_19.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_19.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_19.setFont(font)
    self.pw_grid_label_19.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_19.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_19.setObjectName("pw_grid_label_19")
    self.horizontalLayout_24.addWidget(self.pw_grid_label_19)
    self.pw_grid_combobox_1 = QtWidgets.QComboBox()
    self.pw_grid_combobox_1.setMinimumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_1.setMaximumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_1.setFont(font3)
    self.pw_grid_combobox_1.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_1.setFrame(False)
    self.pw_grid_combobox_1.setObjectName("pw_grid_combobox_1")
    self.horizontalLayout_24.addWidget(self.pw_grid_combobox_1)
    self.horizontalLayout_24.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_47 = QtWidgets.QLabel()
    self.pw_grid_label_47.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_47.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_47.setFont(font)
    self.pw_grid_label_47.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_47.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_47.setObjectName("pw_grid_label_47")
    self.horizontalLayout_24.addWidget(self.pw_grid_label_47)
    self.pw_grid_combobox_4 = QtWidgets.QComboBox()
    self.pw_grid_combobox_4.setMinimumSize(QtCore.QSize(80, 27))
    self.pw_grid_combobox_4.setMaximumSize(QtCore.QSize(80, 27))
    self.pw_grid_combobox_4.setFont(font3)
    self.pw_grid_combobox_4.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_4.setFrame(False)
    self.pw_grid_combobox_4.setObjectName("pw_grid_combobox_4")
    self.horizontalLayout_24.addWidget(self.pw_grid_combobox_4)
    self.gridLayout_6.addLayout(self.horizontalLayout_24, 2, 1, 1, 1)
    self.gridLayout_6.addItem(QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum), 3, 0, 1, 1)
    self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_25.setObjectName("horizontalLayout_25")
    self.pw_grid_label_48 = QtWidgets.QLabel()
    self.pw_grid_label_48.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_48.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_48.setFont(font)
    self.pw_grid_label_48.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_48.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_48.setObjectName("pw_grid_label_48")
    self.horizontalLayout_25.addWidget(self.pw_grid_label_48)
    self.pw_grid_line_30 = QtWidgets.QLineEdit()
    self.pw_grid_line_30.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_30.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_30.setFont(font3)
    self.pw_grid_line_30.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_30.setObjectName("pw_grid_line_30")
    self.horizontalLayout_25.addWidget(self.pw_grid_line_30)
    self.horizontalLayout_25.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_49 = QtWidgets.QLabel()
    self.pw_grid_label_49.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_49.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_49.setFont(font)
    self.pw_grid_label_49.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_49.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_49.setObjectName("pw_grid_label_49")
    self.horizontalLayout_25.addWidget(self.pw_grid_label_49)
    self.pw_grid_line_31 = QtWidgets.QLineEdit()
    self.pw_grid_line_31.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_31.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_31.setFont(font3)
    self.pw_grid_line_31.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_31.setObjectName("pw_grid_line_31")
    self.horizontalLayout_25.addWidget(self.pw_grid_line_31)
    self.horizontalLayout_25.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_6.addLayout(self.horizontalLayout_25, 3, 1, 1, 1)
    self.gridLayout_6.addItem(QtWidgets.QSpacerItem(828, 10, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Fixed), 4, 0, 1, 2)
    self.pw_grid_label_17 = QtWidgets.QLabel()
    self.pw_grid_label_17.setMinimumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_17.setMaximumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_17.setFont(font)
    self.pw_grid_label_17.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_17.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_17.setObjectName("pw_grid_label_17")
    self.gridLayout_6.addWidget(self.pw_grid_label_17, 5, 0, 1, 1)
    self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_26.setObjectName("horizontalLayout_26")
    self.pw_grid_line_2 = QtWidgets.QLineEdit()
    self.pw_grid_line_2.setMinimumSize(QtCore.QSize(240, 27))
    self.pw_grid_line_2.setMaximumSize(QtCore.QSize(240, 27))
    self.pw_grid_line_2.setFont(font3)
    self.pw_grid_line_2.setStyleSheet("QLineEdit {\n"
                                      "    border-radius: 3px;\n"
                                      "    padding: 1px 4px 1px 4px;\n"
                                      "    background-color:  rgb(240, 240, 240);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled {\n"
                                      "    background-color:  rgb(200,200,200);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
    self.pw_grid_line_2.setObjectName("pw_grid_line_2")
    self.horizontalLayout_26.addWidget(self.pw_grid_line_2)
    self.horizontalLayout_26.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_20 = QtWidgets.QLabel()
    self.pw_grid_label_20.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_20.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_20.setFont(font)
    self.pw_grid_label_20.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_20.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_20.setObjectName("pw_grid_label_20")
    self.horizontalLayout_26.addWidget(self.pw_grid_label_20)
    self.pw_grid_combobox_2 = QtWidgets.QComboBox()
    self.pw_grid_combobox_2.setMinimumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_2.setMaximumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_2.setFont(font3)
    self.pw_grid_combobox_2.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_2.setFrame(False)
    self.pw_grid_combobox_2.setObjectName("pw_grid_combobox_2")
    self.horizontalLayout_26.addWidget(self.pw_grid_combobox_2)
    self.horizontalLayout_26.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_50 = QtWidgets.QLabel()
    self.pw_grid_label_50.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_50.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_50.setFont(font)
    self.pw_grid_label_50.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_50.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_50.setObjectName("pw_grid_label_50")
    self.horizontalLayout_26.addWidget(self.pw_grid_label_50)
    self.pw_grid_combobox_5 = QtWidgets.QComboBox()
    self.pw_grid_combobox_5.setMinimumSize(QtCore.QSize(80, 27))
    self.pw_grid_combobox_5.setMaximumSize(QtCore.QSize(80, 27))
    self.pw_grid_combobox_5.setFont(font3)
    self.pw_grid_combobox_5.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_5.setFrame(False)
    self.pw_grid_combobox_5.setObjectName("pw_grid_combobox_5")
    self.horizontalLayout_26.addWidget(self.pw_grid_combobox_5)
    self.gridLayout_6.addLayout(self.horizontalLayout_26, 5, 1, 1, 1)
    self.gridLayout_6.addItem(QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum), 6, 0, 1, 1)
    self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_27.setObjectName("horizontalLayout_27")
    self.pw_grid_label_51 = QtWidgets.QLabel()
    self.pw_grid_label_51.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_51.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_51.setFont(font)
    self.pw_grid_label_51.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_51.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_51.setObjectName("pw_grid_label_51")
    self.horizontalLayout_27.addWidget(self.pw_grid_label_51)
    self.pw_grid_line_32 = QtWidgets.QLineEdit()
    self.pw_grid_line_32.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_32.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_32.setFont(font3)
    self.pw_grid_line_32.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_32.setObjectName("pw_grid_line_32")
    self.horizontalLayout_27.addWidget(self.pw_grid_line_32)
    self.horizontalLayout_27.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_52 = QtWidgets.QLabel()
    self.pw_grid_label_52.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_52.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_52.setFont(font)
    self.pw_grid_label_52.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_52.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_52.setObjectName("pw_grid_label_52")
    self.horizontalLayout_27.addWidget(self.pw_grid_label_52)
    self.pw_grid_line_33 = QtWidgets.QLineEdit()
    self.pw_grid_line_33.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_33.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_33.setFont(font3)
    self.pw_grid_line_33.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_33.setObjectName("pw_grid_line_33")
    self.horizontalLayout_27.addWidget(self.pw_grid_line_33)
    self.horizontalLayout_27.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_6.addLayout(self.horizontalLayout_27, 6, 1, 1, 1)
    self.gridLayout_6.addItem(QtWidgets.QSpacerItem(828, 10, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Fixed), 7, 0, 1, 2)
    self.pw_grid_label_18 = QtWidgets.QLabel()
    self.pw_grid_label_18.setMinimumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_18.setMaximumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_18.setFont(font)
    self.pw_grid_label_18.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_18.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_18.setObjectName("pw_grid_label_18")
    self.gridLayout_6.addWidget(self.pw_grid_label_18, 8, 0, 1, 1)
    self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_28.setObjectName("horizontalLayout_28")
    self.pw_grid_line_3 = QtWidgets.QLineEdit()
    self.pw_grid_line_3.setMinimumSize(QtCore.QSize(240, 27))
    self.pw_grid_line_3.setMaximumSize(QtCore.QSize(240, 27))
    self.pw_grid_line_3.setFont(font3)
    self.pw_grid_line_3.setStyleSheet("QLineEdit {\n"
                                      "    border-radius: 3px;\n"
                                      "    padding: 1px 4px 1px 4px;\n"
                                      "    background-color:  rgb(240, 240, 240);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled {\n"
                                      "    background-color:  rgb(200,200,200);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}")
    self.pw_grid_line_3.setObjectName("pw_grid_line_3")
    self.horizontalLayout_28.addWidget(self.pw_grid_line_3)
    self.horizontalLayout_28.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_53 = QtWidgets.QLabel()
    self.pw_grid_label_53.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_53.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_53.setFont(font)
    self.pw_grid_label_53.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_53.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_53.setObjectName("pw_grid_label_53")
    self.horizontalLayout_28.addWidget(self.pw_grid_label_53)
    self.pw_grid_combobox_3 = QtWidgets.QComboBox()
    self.pw_grid_combobox_3.setMinimumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_3.setMaximumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_3.setFont(font3)
    self.pw_grid_combobox_3.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_3.setFrame(False)
    self.pw_grid_combobox_3.setObjectName("pw_grid_combobox_3")
    self.horizontalLayout_28.addWidget(self.pw_grid_combobox_3)
    self.horizontalLayout_28.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_54 = QtWidgets.QLabel()
    self.pw_grid_label_54.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_54.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_54.setFont(font)
    self.pw_grid_label_54.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_54.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_54.setObjectName("pw_grid_label_54")
    self.horizontalLayout_28.addWidget(self.pw_grid_label_54)
    self.pw_grid_combobox_6 = QtWidgets.QComboBox()
    self.pw_grid_combobox_6.setMinimumSize(QtCore.QSize(80, 27))
    self.pw_grid_combobox_6.setMaximumSize(QtCore.QSize(80, 27))
    self.pw_grid_combobox_6.setFont(font3)
    self.pw_grid_combobox_6.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_6.setFrame(False)
    self.pw_grid_combobox_6.setObjectName("pw_grid_combobox_6")
    self.horizontalLayout_28.addWidget(self.pw_grid_combobox_6)
    self.gridLayout_6.addLayout(self.horizontalLayout_28, 8, 1, 1, 1)
    self.gridLayout_6.addItem(QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum), 9, 0, 1, 1)
    self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_29.setObjectName("horizontalLayout_29")
    self.pw_grid_label_55 = QtWidgets.QLabel()
    self.pw_grid_label_55.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_55.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_55.setFont(font)
    self.pw_grid_label_55.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_55.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_55.setObjectName("pw_grid_label_55")
    self.horizontalLayout_29.addWidget(self.pw_grid_label_55)
    self.pw_grid_line_34 = QtWidgets.QLineEdit()
    self.pw_grid_line_34.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_34.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_34.setFont(font3)
    self.pw_grid_line_34.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_34.setObjectName("pw_grid_line_34")
    self.horizontalLayout_29.addWidget(self.pw_grid_line_34)
    self.horizontalLayout_29.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_56 = QtWidgets.QLabel()
    self.pw_grid_label_56.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_56.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_56.setFont(font)
    self.pw_grid_label_56.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_56.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_56.setObjectName("pw_grid_label_56")
    self.horizontalLayout_29.addWidget(self.pw_grid_label_56)
    self.pw_grid_line_35 = QtWidgets.QLineEdit()
    self.pw_grid_line_35.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_35.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_line_35.setFont(font3)
    self.pw_grid_line_35.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_35.setObjectName("pw_grid_line_35")
    self.horizontalLayout_29.addWidget(self.pw_grid_line_35)
    self.horizontalLayout_29.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_6.addLayout(self.horizontalLayout_29, 9, 1, 1, 1)
    self.horizontalLayout_22.addLayout(self.gridLayout_6)
    self.verticalLayout_7 = QtWidgets.QVBoxLayout()
    self.verticalLayout_7.setObjectName("verticalLayout_7")
    self.verticalLayout_7.addItem(QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum,
                                                        QtWidgets.QSizePolicy.Fixed))
    self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_30.setObjectName("horizontalLayout_30")
    self.horizontalLayout_30.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_info_button_2 = QtWidgets.QToolButton()
    self.pw_grid_info_button_2.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_2.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_2.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_2.setIcon(icon)
    self.pw_grid_info_button_2.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_2.setObjectName("pw_grid_info_button_2")
    self.horizontalLayout_30.addWidget(self.pw_grid_info_button_2)
    self.verticalLayout_7.addLayout(self.horizontalLayout_30)
    self.verticalLayout_7.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                        QtWidgets.QSizePolicy.Expanding))
    self.horizontalLayout_22.addLayout(self.verticalLayout_7)
    self.horizontalLayout_22.addItem(QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_la.addLayout(self.horizontalLayout_22)
    self.pw_figureOptions_la.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                           QtWidgets.QSizePolicy.Expanding))
    self.pw_figureOptions_la.setAlignment(QtCore.Qt.AlignTop)
    self.pw_grid_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_5.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_label_46.setText("Global options")
    self.pw_grid_label_2.setText("Set figure margins:")
    self.pw_grid_label_6.setText("TMP")
    self.pw_grid_label_3.setText("Left:")
    self.pw_grid_label_5.setText("TMP")
    self.pw_grid_label_9.setText("TMP")
    self.pw_grid_label_8.setText("Bottom:")
    self.pw_grid_label_10.setText("TMP")
    self.pw_grid_label_4.setText("Top:")
    self.pw_grid_label_7.setText("Right:")
    self.pw_grid_label_16.setText("Figure title:")
    self.pw_grid_label_19.setText("Font:")
    self.pw_grid_label_47.setText("Size:")
    self.pw_grid_label_48.setText("Horizontal distance from origin:")
    self.pw_grid_label_49.setText("Vertical distance from origin:")
    self.pw_grid_label_17.setText("X label:")
    self.pw_grid_label_20.setText("Font:")
    self.pw_grid_label_50.setText("Size:")
    self.pw_grid_label_51.setText("Horizontal distance from origin:")
    self.pw_grid_label_52.setText("Vertical distance from origin:")
    self.pw_grid_label_18.setText("Y label:")
    self.pw_grid_label_53.setText("Font:")
    self.pw_grid_label_54.setText("Size:")
    self.pw_grid_label_55.setText("Horizontal distance from origin:")
    self.pw_grid_label_56.setText("Vertical distance from origin:")
    populate_combobox(self.pw_grid_combobox_1, self.font_list, False, self.default_font)
    populate_combobox(self.pw_grid_combobox_2, self.font_list, False, self.default_font)
    populate_combobox(self.pw_grid_combobox_3, self.font_list, False, self.default_font)
    populate_combobox(self.pw_grid_combobox_4, [str(x) for x in range(1, 49, 1)], False, 9)
    populate_combobox(self.pw_grid_combobox_5, [str(x) for x in range(1, 49, 1)], False, 9)
    populate_combobox(self.pw_grid_combobox_6, [str(x) for x in range(1, 49, 1)], False, 9)
    self.pw_grid_slider_1.valueChanged.connect(lambda val: update_gd_slider_value(self, val))
    self.pw_grid_slider_2.valueChanged.connect(lambda val: update_gd_slider_value(self, val))
    self.pw_grid_slider_3.valueChanged.connect(lambda val: update_gd_slider_value(self, val))
    self.pw_grid_slider_4.valueChanged.connect(lambda val: update_gd_slider_value(self, val))
    self.pw_grid_info_button_1.clicked.connect(self.figure_button_information)
    self.pw_grid_info_button_2.clicked.connect(self.figure_button_information)
    self.pw_grid_slider_1.setSliderPosition(self.gd_figure_options['margin_left'] * 100)
    self.pw_grid_slider_2.setSliderPosition(100 - self.gd_figure_options['margin_top'] * 100)
    self.pw_grid_slider_3.setSliderPosition(100 - self.gd_figure_options['margin_right'] * 100)
    self.pw_grid_slider_4.setSliderPosition(self.gd_figure_options['margin_bottom'] * 100)
    self.pw_grid_line_30.setText(str(self.gd_figure_options['title_xpos']))
    self.pw_grid_line_31.setText(str(self.gd_figure_options['title_ypos']))
    if self.gd_plot_options['projection'] in ['PlateCarree', 'Mercator']:
        self.pw_grid_line_2.setText(self.gd_figure_options['title'])
        self.pw_grid_line_2.setText(self.gd_figure_options['xlabel'])
        self.pw_grid_line_3.setText(self.gd_figure_options['ylabel'])
        self.pw_grid_line_32.setText(str(self.gd_figure_options['xlabel_xpos']))
        self.pw_grid_line_33.setText(str(self.gd_figure_options['xlabel_ypos']))
        self.pw_grid_line_34.setText(str(self.gd_figure_options['ylabel_xpos']))
        self.pw_grid_line_35.setText(str(self.gd_figure_options['ylabel_ypos']))
    else:
        self.pw_grid_label_17.setEnabled(False)
        self.pw_grid_label_18.setEnabled(False)
        self.pw_grid_label_20.setEnabled(False)
        self.pw_grid_label_48.setEnabled(False)
        self.pw_grid_label_47.setEnabled(False)
        self.pw_grid_label_49.setEnabled(False)
        self.pw_grid_label_51.setEnabled(False)
        self.pw_grid_label_52.setEnabled(False)
        self.pw_grid_label_55.setEnabled(False)
        self.pw_grid_label_56.setEnabled(False)
        self.pw_grid_line_2.setEnabled(False)
        self.pw_grid_line_3.setEnabled(False)
        self.pw_grid_combobox_2.setEnabled(False)
        self.pw_grid_combobox_3.setEnabled(False)
        self.pw_grid_combobox_5.setEnabled(False)
        self.pw_grid_combobox_6.setEnabled(False)
        self.pw_grid_line_32.setEnabled(False)
        self.pw_grid_line_33.setEnabled(False)
        self.pw_grid_line_34.setEnabled(False)
        self.pw_grid_line_35.setEnabled(False)


def add_plot_options(self):
    logging.debug('gui - plot_gd_option_gui_functions.py - add_plot_options')
    font4 = font_creation_function('small-italic')
    font3 = font_creation_function('small')
    font2 = font_creation_function('big')
    font = font_creation_function('normal')
    icon = icon_creation_function('info_icon.svg')
    self.pw_figureOptions_hl_3 = QtWidgets.QHBoxLayout()
    self.pw_figureOptions_hl_3.setObjectName("pw_figureOptions_hl_3")
    self.pw_grid_label_11 = QtWidgets.QLabel()
    self.pw_grid_label_11.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_11.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_11.setFont(font2)
    self.pw_grid_label_11.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_11.setObjectName("pw_grid_label_11")
    self.pw_figureOptions_hl_3.addWidget(self.pw_grid_label_11)
    self.pw_figureOptions_hl_3.addItem(QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding,
                                                             QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_la.addLayout(self.pw_figureOptions_hl_3)
    self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_20.setObjectName("horizontalLayout_20")
    self.horizontalLayout_20.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_3 = QtWidgets.QGridLayout()
    self.gridLayout_3.setObjectName("gridLayout_3")
    self.pw_grid_label_12 = QtWidgets.QLabel()
    self.pw_grid_label_12.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.pw_grid_label_12.setFont(font)
    self.pw_grid_label_12.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
    self.pw_grid_label_12.setObjectName("pw_grid_label_12")
    self.gridLayout_3.addWidget(self.pw_grid_label_12, 0, 0, 1, 1)
    self.verticalLayout = QtWidgets.QVBoxLayout()
    self.verticalLayout.setObjectName("verticalLayout")
    self.horizontalLayout = QtWidgets.QHBoxLayout()
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.pw_grid_combobox_7 = QtWidgets.QComboBox()
    self.pw_grid_combobox_7.setMinimumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_7.setMaximumSize(QtCore.QSize(240, 27))
    self.pw_grid_combobox_7.setFont(font3)
    self.pw_grid_combobox_7.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_7.setFrame(False)
    self.pw_grid_combobox_7.setObjectName("pw_grid_combobox_7")
    self.horizontalLayout.addWidget(self.pw_grid_combobox_7)
    self.horizontalLayout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_info_button_3 = QtWidgets.QToolButton()
    self.pw_grid_info_button_3.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_3.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_3.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_3.setIcon(icon)
    self.pw_grid_info_button_3.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_3.setObjectName("pw_grid_info_button_3")
    self.horizontalLayout.addWidget(self.pw_grid_info_button_3)
    self.horizontalLayout.addItem(QtWidgets.QSpacerItem(698, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
    self.verticalLayout.addLayout(self.horizontalLayout)
    self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_2.setObjectName("horizontalLayout_2")
    self.pw_grid_set_options = QtWidgets.QToolButton()
    self.pw_grid_set_options.setMinimumSize(QtCore.QSize(120, 27))
    self.pw_grid_set_options.setMaximumSize(QtCore.QSize(120, 27))
    self.pw_grid_set_options.setFont(font)
    self.pw_grid_set_options.setStyleSheet("QToolButton {\n"
                                           "    border: 1px solid #acacac;\n"
                                           "    border-radius: 1px;\n"
                                           "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                           "                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
                                           "    color: rgb(45,45,45);\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:disabled {\n"
                                           "    background-color:  rgb(200,200,200);\n"
                                           "    color: rgb(145,145,145);\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:hover {\n"
                                           "    border: 1px solid #7eb4ea;\n"
                                           "    border-radius: 1px;\n"
                                           "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                           "                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:pressed {\n"
                                           "    border: 1px solid #579de5;\n"
                                           "    border-radius: 1px;\n"
                                           "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                           "                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
                                           "}")
    self.pw_grid_set_options.setIconSize(QtCore.QSize(25, 25))
    self.pw_grid_set_options.setObjectName("pw_grid_set_options")
    self.horizontalLayout_2.addWidget(self.pw_grid_set_options)
    self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                          QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_13 = QtWidgets.QLabel()
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(self.pw_grid_label_13.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_13.setSizePolicy(size_policy)
    self.pw_grid_label_13.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.pw_grid_label_13.setWordWrap(True)
    self.pw_grid_label_13.setFont(font4)
    self.pw_grid_label_13.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_13.setObjectName("pw_grid_label_13")
    self.horizontalLayout_2.addWidget(self.pw_grid_label_13)
    self.verticalLayout.addLayout(self.horizontalLayout_2)
    self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
    self.gridLayout_3.addItem(QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum), 1, 0, 1, 1)
    self.line_4 = QtWidgets.QFrame()
    self.line_4.setStyleSheet("QFrame {\n"
                              "    background: rgb(190,190,190);\n"
                              "    height: 5px;\n"
                              "    border: 0px solid black;\n"
                              "}")
    self.line_4.setLineWidth(1)
    self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
    self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line_4.setObjectName("line_4")
    self.gridLayout_3.addWidget(self.line_4, 1, 1, 1, 1)
    self.pw_grid_label_22 = QtWidgets.QLabel()
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(self.pw_grid_label_22.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_22.setSizePolicy(size_policy)
    self.pw_grid_label_22.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.pw_grid_label_22.setFont(font)
    self.pw_grid_label_22.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_22.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
    self.pw_grid_label_22.setObjectName("pw_grid_label_22")
    self.gridLayout_3.addWidget(self.pw_grid_label_22, 2, 0, 1, 1)
    self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_8.setObjectName("horizontalLayout_8")
    self.verticalLayout_4 = QtWidgets.QVBoxLayout()
    self.verticalLayout_4.setObjectName("verticalLayout_4")
    self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_9.setObjectName("horizontalLayout_9")
    self.pw_grid_set_ticks = QtWidgets.QToolButton()
    self.pw_grid_set_ticks.setMinimumSize(QtCore.QSize(130, 27))
    self.pw_grid_set_ticks.setMaximumSize(QtCore.QSize(130, 27))
    self.pw_grid_set_ticks.setFont(font)
    self.pw_grid_set_ticks.setStyleSheet("QToolButton {\n"
                                         "    border: 1px solid #acacac;\n"
                                         "    border-radius: 1px;\n"
                                         "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                         "                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
                                         "    color: rgb(45,45,45);\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:disabled {\n"
                                         "    background-color:  rgb(200,200,200);\n"
                                         "    color: rgb(145,145,145);\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:hover {\n"
                                         "    border: 1px solid #7eb4ea;\n"
                                         "    border-radius: 1px;\n"
                                         "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                         "                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:pressed {\n"
                                         "    border: 1px solid #579de5;\n"
                                         "    border-radius: 1px;\n"
                                         "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                         "                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
                                         "}")
    self.pw_grid_set_ticks.setIconSize(QtCore.QSize(25, 25))
    self.pw_grid_set_ticks.setObjectName("pw_grid_set_ticks")
    self.horizontalLayout_9.addWidget(self.pw_grid_set_ticks)
    self.horizontalLayout_9.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                          QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_info_button_6 = QtWidgets.QToolButton()
    self.pw_grid_info_button_6.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_6.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_6.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_6.setIcon(icon)
    self.pw_grid_info_button_6.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_6.setObjectName("pw_grid_info_button_6")
    self.horizontalLayout_9.addWidget(self.pw_grid_info_button_6)
    self.horizontalLayout_9.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                          QtWidgets.QSizePolicy.Minimum))
    self.verticalLayout_4.addLayout(self.horizontalLayout_9)
    self.verticalLayout_4.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                        QtWidgets.QSizePolicy.Expanding))
    self.horizontalLayout_8.addLayout(self.verticalLayout_4)
    self.verticalLayout_3 = QtWidgets.QVBoxLayout()
    self.verticalLayout_3.setObjectName("verticalLayout_3")
    self.pw_grid_label_14 = QtWidgets.QLabel()
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(self.pw_grid_label_14.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_14.setSizePolicy(size_policy)
    self.pw_grid_label_14.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.pw_grid_label_14.setFont(font4)
    self.pw_grid_label_14.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
    self.pw_grid_label_14.setWordWrap(True)
    self.pw_grid_label_14.setObjectName("pw_grid_label_14")
    self.verticalLayout_3.addWidget(self.pw_grid_label_14)
    self.pw_grid_label_15 = QtWidgets.QLabel()
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(self.pw_grid_label_15.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_15.setSizePolicy(size_policy)
    self.pw_grid_label_15.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))

    self.pw_grid_label_15.setFont(font4)
    self.pw_grid_label_15.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
    self.pw_grid_label_15.setWordWrap(True)
    self.pw_grid_label_15.setObjectName("pw_grid_label_15")
    self.verticalLayout_3.addWidget(self.pw_grid_label_15)
    self.horizontalLayout_8.addLayout(self.verticalLayout_3)
    self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
    self.gridLayout_3.addItem(QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum), 3, 0, 1, 1)
    self.line_5 = QtWidgets.QFrame()
    self.line_5.setStyleSheet("QFrame {\n"
                              "    background: rgb(190,190,190);\n"
                              "    height: 5px;\n"
                              "    border: 0px solid black;\n"
                              "}")
    self.line_5.setLineWidth(1)
    self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
    self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line_5.setObjectName("line_5")
    self.gridLayout_3.addWidget(self.line_5, 3, 1, 1, 1)
    self.pw_grid_label_26 = QtWidgets.QLabel()
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(self.pw_grid_label_26.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_26.setSizePolicy(size_policy)
    self.pw_grid_label_26.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_26.setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.pw_grid_label_26.setFont(font)
    self.pw_grid_label_26.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_26.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
    self.pw_grid_label_26.setObjectName("pw_grid_label_26")
    self.gridLayout_3.addWidget(self.pw_grid_label_26, 4, 0, 1, 1)
    self.verticalLayout_5 = QtWidgets.QVBoxLayout()
    self.verticalLayout_5.setObjectName("verticalLayout_5")
    self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_17.setObjectName("horizontalLayout_17")
    self.pw_grid_checkbox_6 = QtWidgets.QCheckBox()
    self.pw_grid_checkbox_6.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_checkbox_6.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_checkbox_6.setFont(font)
    self.pw_grid_checkbox_6.setStyleSheet("QCheckBox {\n"
                                          "   color: rgb(45,45,45);\n"
                                          "}")
    self.pw_grid_checkbox_6.setChecked(True)
    self.pw_grid_checkbox_6.setObjectName("pw_grid_checkbox_6")
    self.horizontalLayout_17.addWidget(self.pw_grid_checkbox_6)
    self.horizontalLayout_17.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_info_button_7 = QtWidgets.QToolButton()
    self.pw_grid_info_button_7.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_7.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_7.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_7.setIcon(icon)
    self.pw_grid_info_button_7.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_7.setObjectName("pw_grid_info_button_7")
    self.horizontalLayout_17.addWidget(self.pw_grid_info_button_7)
    self.horizontalLayout_17.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.verticalLayout_5.addLayout(self.horizontalLayout_17)
    self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_15.setObjectName("horizontalLayout_15")
    self.horizontalLayout_15.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout = QtWidgets.QGridLayout()
    self.gridLayout.setObjectName("gridLayout")
    self.pw_grid_label_27 = QtWidgets.QLabel()
    self.pw_grid_label_27.setEnabled(True)
    self.pw_grid_label_27.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_27.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_27.setFont(font)
    self.pw_grid_label_27.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_27.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_27.setObjectName("pw_grid_label_27")
    self.gridLayout.addWidget(self.pw_grid_label_27, 0, 0, 1, 1)
    self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_12.setObjectName("horizontalLayout_12")
    self.pw_grid_combobox_12 = QtWidgets.QComboBox()
    self.pw_grid_combobox_12.setEnabled(True)
    self.pw_grid_combobox_12.setMinimumSize(QtCore.QSize(90, 27))
    self.pw_grid_combobox_12.setMaximumSize(QtCore.QSize(90, 27))
    self.pw_grid_combobox_12.setFont(font3)
    self.pw_grid_combobox_12.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_12.setFrame(False)
    self.pw_grid_combobox_12.setObjectName("pw_grid_combobox_12")
    self.pw_grid_combobox_12.addItem("")
    self.pw_grid_combobox_12.addItem("")
    self.pw_grid_combobox_12.addItem("")
    self.horizontalLayout_12.addWidget(self.pw_grid_combobox_12)
    self.horizontalLayout_12.addItem(QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_29 = QtWidgets.QLabel()
    self.pw_grid_label_29.setEnabled(True)
    self.pw_grid_label_29.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_29.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_29.setFont(font)
    self.pw_grid_label_29.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_29.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_29.setObjectName("pw_grid_label_29")
    self.horizontalLayout_12.addWidget(self.pw_grid_label_29)
    self.pw_grid_line_12 = QtWidgets.QLineEdit()
    self.pw_grid_line_12.setEnabled(True)
    self.pw_grid_line_12.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_12.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_12.setFont(font3)
    self.pw_grid_line_12.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(145,145,145);\n"
                                       "}")
    self.pw_grid_line_12.setObjectName("pw_grid_line_12")
    self.horizontalLayout_12.addWidget(self.pw_grid_line_12)
    self.horizontalLayout_12.addItem(QtWidgets.QSpacerItem(488, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)
    self.pw_grid_label_30 = QtWidgets.QLabel()
    self.pw_grid_label_30.setEnabled(True)
    self.pw_grid_label_30.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_30.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_30.setFont(font)
    self.pw_grid_label_30.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_30.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_30.setObjectName("pw_grid_label_30")
    self.gridLayout.addWidget(self.pw_grid_label_30, 1, 0, 1, 1)
    self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_10.setObjectName("horizontalLayout_10")
    self.pw_grid_combobox_13 = QtWidgets.QComboBox()
    self.pw_grid_combobox_13.setEnabled(True)
    self.pw_grid_combobox_13.setMinimumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_13.setMaximumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_13.setFont(font3)
    self.pw_grid_combobox_13.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_13.setFrame(False)
    self.pw_grid_combobox_13.setObjectName("pw_grid_combobox_13")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.pw_grid_combobox_13.addItem("")
    self.horizontalLayout_10.addWidget(self.pw_grid_combobox_13)
    self.pw_grid_line_13 = QtWidgets.QLineEdit()
    self.pw_grid_line_13.setEnabled(True)
    self.pw_grid_line_13.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_13.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_13.setFont(font3)
    self.pw_grid_line_13.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_13.setObjectName("pw_grid_line_13")
    self.horizontalLayout_10.addWidget(self.pw_grid_line_13)
    self.pw_grid_line_14 = QtWidgets.QLineEdit()
    self.pw_grid_line_14.setEnabled(True)
    self.pw_grid_line_14.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_14.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_14.setFont(font3)
    self.pw_grid_line_14.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_14.setObjectName("pw_grid_line_14")
    self.horizontalLayout_10.addWidget(self.pw_grid_line_14)
    self.pw_grid_line_15 = QtWidgets.QLineEdit()
    self.pw_grid_line_15.setEnabled(True)
    self.pw_grid_line_15.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_15.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_15.setFont(font3)
    self.pw_grid_line_15.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_15.setObjectName("pw_grid_line_15")
    self.horizontalLayout_10.addWidget(self.pw_grid_line_15)
    self.horizontalLayout_10.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_40 = QtWidgets.QLabel()
    self.pw_grid_label_40.setEnabled(True)
    self.pw_grid_label_40.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_40.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_40.setFont(font)
    self.pw_grid_label_40.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_40.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_40.setObjectName("pw_grid_label_40")
    self.horizontalLayout_10.addWidget(self.pw_grid_label_40)
    self.pw_grid_combobox_14 = QtWidgets.QComboBox()
    self.pw_grid_combobox_14.setEnabled(True)
    self.pw_grid_combobox_14.setMinimumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_14.setMaximumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_14.setFont(font3)
    self.pw_grid_combobox_14.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_14.setFrame(False)
    self.pw_grid_combobox_14.setObjectName("pw_grid_combobox_14")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.pw_grid_combobox_14.addItem("")
    self.horizontalLayout_10.addWidget(self.pw_grid_combobox_14)
    self.pw_grid_line_18 = QtWidgets.QLineEdit()
    self.pw_grid_line_18.setEnabled(True)
    self.pw_grid_line_18.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_18.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_18.setFont(font3)
    self.pw_grid_line_18.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_18.setObjectName("pw_grid_line_18")
    self.horizontalLayout_10.addWidget(self.pw_grid_line_18)
    self.pw_grid_line_16 = QtWidgets.QLineEdit()
    self.pw_grid_line_16.setEnabled(True)
    self.pw_grid_line_16.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_16.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_16.setFont(font3)
    self.pw_grid_line_16.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_16.setObjectName("pw_grid_line_16")
    self.horizontalLayout_10.addWidget(self.pw_grid_line_16)
    self.pw_grid_line_17 = QtWidgets.QLineEdit()
    self.pw_grid_line_17.setEnabled(True)
    self.pw_grid_line_17.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_17.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_17.setFont(font3)
    self.pw_grid_line_17.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_17.setObjectName("pw_grid_line_17")
    self.horizontalLayout_10.addWidget(self.pw_grid_line_17)
    self.horizontalLayout_10.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
    self.horizontalLayout_15.addLayout(self.gridLayout)
    self.verticalLayout_5.addLayout(self.horizontalLayout_15)
    self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_18.setObjectName("horizontalLayout_18")
    self.pw_grid_checkbox_7 = QtWidgets.QCheckBox()
    self.pw_grid_checkbox_7.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_checkbox_7.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_checkbox_7.setFont(font)
    self.pw_grid_checkbox_7.setStyleSheet("QCheckBox {\n"
                                          "   color: rgb(45,45,45);\n"
                                          "}")
    self.pw_grid_checkbox_7.setObjectName("pw_grid_checkbox_7")
    self.horizontalLayout_18.addWidget(self.pw_grid_checkbox_7)
    self.horizontalLayout_18.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_info_button_8 = QtWidgets.QToolButton()
    self.pw_grid_info_button_8.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_8.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_8.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_8.setIcon(icon)
    self.pw_grid_info_button_8.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_8.setObjectName("pw_grid_info_button_8")
    self.horizontalLayout_18.addWidget(self.pw_grid_info_button_8)
    self.horizontalLayout_18.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.verticalLayout_5.addLayout(self.horizontalLayout_18)
    self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_16.setObjectName("horizontalLayout_16")
    self.horizontalLayout_16.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_2 = QtWidgets.QGridLayout()
    self.gridLayout_2.setObjectName("gridLayout_2")
    self.pw_grid_label_28 = QtWidgets.QLabel()
    self.pw_grid_label_28.setEnabled(False)
    self.pw_grid_label_28.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_28.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_28.setFont(font)
    self.pw_grid_label_28.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_28.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_28.setObjectName("pw_grid_label_28")
    self.gridLayout_2.addWidget(self.pw_grid_label_28, 0, 0, 1, 1)
    self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_13.setObjectName("horizontalLayout_13")
    self.pw_grid_combobox_15 = QtWidgets.QComboBox()
    self.pw_grid_combobox_15.setEnabled(False)
    self.pw_grid_combobox_15.setMinimumSize(QtCore.QSize(90, 27))
    self.pw_grid_combobox_15.setMaximumSize(QtCore.QSize(90, 27))
    self.pw_grid_combobox_15.setFont(font3)
    self.pw_grid_combobox_15.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_15.setFrame(False)
    self.pw_grid_combobox_15.setObjectName("pw_grid_combobox_15")
    self.pw_grid_combobox_15.addItem("")
    self.pw_grid_combobox_15.addItem("")
    self.pw_grid_combobox_15.addItem("")
    self.horizontalLayout_13.addWidget(self.pw_grid_combobox_15)
    self.horizontalLayout_13.addItem(QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_41 = QtWidgets.QLabel()
    self.pw_grid_label_41.setEnabled(False)
    self.pw_grid_label_41.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_41.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_41.setFont(font)
    self.pw_grid_label_41.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_41.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_41.setObjectName("pw_grid_label_41")
    self.horizontalLayout_13.addWidget(self.pw_grid_label_41)
    self.pw_grid_line_19 = QtWidgets.QLineEdit()
    self.pw_grid_line_19.setEnabled(False)
    self.pw_grid_line_19.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_19.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_19.setFont(font3)
    self.pw_grid_line_19.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(145,145,145);\n"
                                       "}")
    self.pw_grid_line_19.setObjectName("pw_grid_line_19")
    self.horizontalLayout_13.addWidget(self.pw_grid_line_19)
    self.horizontalLayout_13.addItem(QtWidgets.QSpacerItem(488, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)
    self.pw_grid_label_42 = QtWidgets.QLabel()
    self.pw_grid_label_42.setEnabled(False)
    self.pw_grid_label_42.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_42.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_42.setFont(font)
    self.pw_grid_label_42.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_42.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_42.setObjectName("pw_grid_label_42")
    self.gridLayout_2.addWidget(self.pw_grid_label_42, 1, 0, 1, 1)
    self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_14.setObjectName("horizontalLayout_14")
    self.pw_grid_combobox_16 = QtWidgets.QComboBox()
    self.pw_grid_combobox_16.setEnabled(False)
    self.pw_grid_combobox_16.setMinimumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_16.setMaximumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_16.setFont(font3)
    self.pw_grid_combobox_16.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_16.setFrame(False)
    self.pw_grid_combobox_16.setObjectName("pw_grid_combobox_16")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.pw_grid_combobox_16.addItem("")
    self.horizontalLayout_14.addWidget(self.pw_grid_combobox_16)
    self.pw_grid_line_20 = QtWidgets.QLineEdit()
    self.pw_grid_line_20.setEnabled(False)
    self.pw_grid_line_20.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_20.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_20.setFont(font3)
    self.pw_grid_line_20.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_20.setObjectName("pw_grid_line_20")
    self.horizontalLayout_14.addWidget(self.pw_grid_line_20)
    self.pw_grid_line_21 = QtWidgets.QLineEdit()
    self.pw_grid_line_21.setEnabled(False)
    self.pw_grid_line_21.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_21.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_21.setFont(font3)
    self.pw_grid_line_21.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_21.setObjectName("pw_grid_line_21")
    self.horizontalLayout_14.addWidget(self.pw_grid_line_21)
    self.pw_grid_line_22 = QtWidgets.QLineEdit()
    self.pw_grid_line_22.setEnabled(False)
    self.pw_grid_line_22.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_22.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_22.setFont(font3)
    self.pw_grid_line_22.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_22.setObjectName("pw_grid_line_22")
    self.horizontalLayout_14.addWidget(self.pw_grid_line_22)
    self.horizontalLayout_14.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_43 = QtWidgets.QLabel()
    self.pw_grid_label_43.setEnabled(False)
    self.pw_grid_label_43.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_43.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_43.setFont(font)
    self.pw_grid_label_43.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_43.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_43.setObjectName("pw_grid_label_43")
    self.horizontalLayout_14.addWidget(self.pw_grid_label_43)
    self.pw_grid_combobox_17 = QtWidgets.QComboBox()
    self.pw_grid_combobox_17.setEnabled(False)
    self.pw_grid_combobox_17.setMinimumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_17.setMaximumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_17.setFont(font3)
    self.pw_grid_combobox_17.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_17.setFrame(False)
    self.pw_grid_combobox_17.setObjectName("pw_grid_combobox_17")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.pw_grid_combobox_17.addItem("")
    self.horizontalLayout_14.addWidget(self.pw_grid_combobox_17)
    self.pw_grid_line_23 = QtWidgets.QLineEdit()
    self.pw_grid_line_23.setEnabled(False)
    self.pw_grid_line_23.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_23.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_23.setFont(font3)
    self.pw_grid_line_23.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_23.setObjectName("pw_grid_line_23")
    self.horizontalLayout_14.addWidget(self.pw_grid_line_23)
    self.pw_grid_line_24 = QtWidgets.QLineEdit()
    self.pw_grid_line_24.setEnabled(False)
    self.pw_grid_line_24.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_24.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_24.setFont(font3)
    self.pw_grid_line_24.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_24.setObjectName("pw_grid_line_24")
    self.horizontalLayout_14.addWidget(self.pw_grid_line_24)
    self.pw_grid_line_25 = QtWidgets.QLineEdit()
    self.pw_grid_line_25.setEnabled(False)
    self.pw_grid_line_25.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_25.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_25.setFont(font3)
    self.pw_grid_line_25.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_25.setObjectName("pw_grid_line_25")
    self.horizontalLayout_14.addWidget(self.pw_grid_line_25)
    self.horizontalLayout_14.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_2.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)
    self.horizontalLayout_16.addLayout(self.gridLayout_2)
    self.verticalLayout_5.addLayout(self.horizontalLayout_16)
    self.gridLayout_3.addLayout(self.verticalLayout_5, 4, 1, 1, 1)
    self.gridLayout_3.addItem(QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum), 5, 0, 1, 1)
    self.line_6 = QtWidgets.QFrame()
    self.line_6.setStyleSheet("QFrame {\n"
                              "    background: rgb(190,190,190);\n"
                              "    height: 5px;\n"
                              "    border: 0px solid black;\n"
                              "}")
    self.line_6.setLineWidth(1)
    self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
    self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line_6.setObjectName("line_6")
    self.gridLayout_3.addWidget(self.line_6, 5, 1, 1, 1)
    self.pw_grid_label_44 = QtWidgets.QLabel()
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(self.pw_grid_label_44.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_44.setSizePolicy(size_policy)
    self.pw_grid_label_44.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_44.setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.pw_grid_label_44.setFont(font)
    self.pw_grid_label_44.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_44.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
    self.pw_grid_label_44.setObjectName("pw_grid_label_44")
    self.gridLayout_3.addWidget(self.pw_grid_label_44, 6, 0, 1, 1)
    self.verticalLayout_6 = QtWidgets.QVBoxLayout()
    self.verticalLayout_6.setObjectName("verticalLayout_6")
    self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_3.setObjectName("horizontalLayout_3")
    self.pw_grid_checkbox_1 = QtWidgets.QCheckBox()
    self.pw_grid_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_checkbox_1.setFont(font)
    self.pw_grid_checkbox_1.setStyleSheet("QCheckBox {\n"
                                          "   color: rgb(45,45,45);\n"
                                          "}")
    self.pw_grid_checkbox_1.setObjectName("pw_grid_checkbox_1")
    self.horizontalLayout_3.addWidget(self.pw_grid_checkbox_1)
    self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                          QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_info_button_4 = QtWidgets.QToolButton()
    self.pw_grid_info_button_4.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_4.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_4.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_4.setIcon(icon)
    self.pw_grid_info_button_4.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_4.setObjectName("pw_grid_info_button_4")
    self.horizontalLayout_3.addWidget(self.pw_grid_info_button_4)
    self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum))
    self.verticalLayout_6.addLayout(self.horizontalLayout_3)
    self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_19.setObjectName("horizontalLayout_19")
    self.horizontalLayout_19.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_23 = QtWidgets.QLabel()
    self.pw_grid_label_23.setEnabled(False)
    self.pw_grid_label_23.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_23.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_23.setFont(font)
    self.pw_grid_label_23.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_23.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_23.setObjectName("pw_grid_label_23")
    self.horizontalLayout_19.addWidget(self.pw_grid_label_23)
    self.pw_grid_combobox_8 = QtWidgets.QComboBox()
    self.pw_grid_combobox_8.setEnabled(False)
    self.pw_grid_combobox_8.setMinimumSize(QtCore.QSize(140, 27))
    self.pw_grid_combobox_8.setMaximumSize(QtCore.QSize(140, 27))
    self.pw_grid_combobox_8.setFont(font3)
    self.pw_grid_combobox_8.setStyleSheet("QComboBox {\n"
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
                                          "    color: rgb(145,145,145);\n"
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
                                          "QComboBox::down-arrow:disabled {\n"
                                          "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_8.setFrame(False)
    self.pw_grid_combobox_8.setObjectName("pw_grid_combobox_8")
    self.pw_grid_combobox_8.addItem("")
    self.pw_grid_combobox_8.addItem("")
    self.pw_grid_combobox_8.addItem("")
    self.pw_grid_combobox_8.addItem("")
    self.horizontalLayout_19.addWidget(self.pw_grid_combobox_8)
    self.horizontalLayout_19.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_24 = QtWidgets.QLabel()
    self.pw_grid_label_24.setEnabled(False)
    self.pw_grid_label_24.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_24.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_24.setFont(font)
    self.pw_grid_label_24.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_24.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_24.setObjectName("pw_grid_label_24")
    self.horizontalLayout_19.addWidget(self.pw_grid_label_24)
    self.pw_grid_line_4 = QtWidgets.QLineEdit()
    self.pw_grid_line_4.setEnabled(False)
    self.pw_grid_line_4.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_4.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_4.setFont(font3)
    self.pw_grid_line_4.setStyleSheet("QLineEdit {\n"
                                      "    border-radius: 3px;\n"
                                      "    padding: 1px 4px 1px 4px;\n"
                                      "    background-color:  rgb(240, 240, 240);\n"
                                      "    color: rgb(45,45,45);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled {\n"
                                      "    background-color:  rgb(200,200,200);\n"
                                      "    color: rgb(145,145,145);\n"
                                      "}")
    self.pw_grid_line_4.setObjectName("pw_grid_line_4")
    self.horizontalLayout_19.addWidget(self.pw_grid_line_4)
    self.horizontalLayout_19.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_grid_label_25 = QtWidgets.QLabel()
    self.pw_grid_label_25.setEnabled(False)
    self.pw_grid_label_25.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_25.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_25.setFont(font)
    self.pw_grid_label_25.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_25.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_25.setObjectName("pw_grid_label_25")
    self.horizontalLayout_19.addWidget(self.pw_grid_label_25)
    self.pw_grid_combobox_18 = QtWidgets.QComboBox()
    self.pw_grid_combobox_18.setEnabled(False)
    self.pw_grid_combobox_18.setMinimumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_18.setMaximumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_18.setFont(font3)
    self.pw_grid_combobox_18.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_18.setFrame(False)
    self.pw_grid_combobox_18.setObjectName("pw_grid_combobox_18")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.pw_grid_combobox_18.addItem("")
    self.horizontalLayout_19.addWidget(self.pw_grid_combobox_18)
    self.pw_grid_line_28 = QtWidgets.QLineEdit()
    self.pw_grid_line_28.setEnabled(False)
    self.pw_grid_line_28.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_28.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_28.setFont(font3)
    self.pw_grid_line_28.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_28.setObjectName("pw_grid_line_28")
    self.horizontalLayout_19.addWidget(self.pw_grid_line_28)
    self.pw_grid_line_27 = QtWidgets.QLineEdit()
    self.pw_grid_line_27.setEnabled(False)
    self.pw_grid_line_27.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_27.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_27.setFont(font3)
    self.pw_grid_line_27.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_27.setObjectName("pw_grid_line_27")
    self.horizontalLayout_19.addWidget(self.pw_grid_line_27)
    self.pw_grid_line_26 = QtWidgets.QLineEdit()
    self.pw_grid_line_26.setEnabled(False)
    self.pw_grid_line_26.setMinimumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_26.setMaximumSize(QtCore.QSize(60, 27))
    self.pw_grid_line_26.setFont(font3)
    self.pw_grid_line_26.setStyleSheet("QLineEdit {\n"
                                       "    border-radius: 3px;\n"
                                       "    padding: 1px 4px 1px 4px;\n"
                                       "    background-color:  rgb(240, 240, 240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:disabled {\n"
                                       "    background-color:  rgb(200,200,200);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}")
    self.pw_grid_line_26.setObjectName("pw_grid_line_26")
    self.horizontalLayout_19.addWidget(self.pw_grid_line_26)
    self.horizontalLayout_19.addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.verticalLayout_6.addLayout(self.horizontalLayout_19)
    self.gridLayout_3.addLayout(self.verticalLayout_6, 6, 1, 1, 1)
    self.horizontalLayout_20.addLayout(self.gridLayout_3)
    self.horizontalLayout_20.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_la.addLayout(self.horizontalLayout_20)
    self.pw_plotOptions_la.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                         QtWidgets.QSizePolicy.Fixed))
    self.line_3 = QtWidgets.QFrame()
    self.line_3.setStyleSheet("QFrame {\n"
                              "    background: rgb(190,190,190);\n"
                              "    height: 5px;\n"
                              "    border: 0px solid black;\n"
                              "}")
    self.line_3.setLineWidth(1)
    self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
    self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line_3.setObjectName("line_3")
    self.pw_plotOptions_la.addWidget(self.line_3)
    self.pw_plotOptions_la.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                         QtWidgets.QSizePolicy.Fixed))
    self.verticalLayout_7 = QtWidgets.QVBoxLayout()
    self.verticalLayout_7.setObjectName("verticalLayout_7")
    self.pw_figureOptions_hl_4 = QtWidgets.QHBoxLayout()
    self.pw_figureOptions_hl_4.setObjectName("pw_figureOptions_hl_4")
    self.pw_grid_label_21 = QtWidgets.QLabel()
    self.pw_grid_label_21.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_21.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_21.setFont(font2)
    self.pw_grid_label_21.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_21.setObjectName("pw_grid_label_21")
    self.pw_figureOptions_hl_4.addWidget(self.pw_grid_label_21)
    spacerItem34 = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.pw_figureOptions_hl_4.addItem(spacerItem34)
    self.verticalLayout_7.addLayout(self.pw_figureOptions_hl_4)
    self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_7.setObjectName("horizontalLayout_7")
    spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_7.addItem(spacerItem35)
    self.pw_grid_label_31 = QtWidgets.QLabel()
    self.pw_grid_label_31.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_31.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_31.setFont(font)
    self.pw_grid_label_31.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}")
    self.pw_grid_label_31.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_31.setObjectName("pw_grid_label_31")
    self.horizontalLayout_7.addWidget(self.pw_grid_label_31)
    self.pw_grid_combobox_10 = QtWidgets.QComboBox()
    self.pw_grid_combobox_10.setMinimumSize(QtCore.QSize(244, 30))
    self.pw_grid_combobox_10.setMaximumSize(QtCore.QSize(244, 30))
    self.pw_grid_combobox_10.setFont(font3)
    self.pw_grid_combobox_10.setStyleSheet("QComboBox {\n"
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
    self.pw_grid_combobox_10.setIconSize(QtCore.QSize(200, 22))
    self.pw_grid_combobox_10.setObjectName("pw_grid_combobox_10")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("images/colormap_coolwarm.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon1, "")
    self.pw_grid_combobox_10.setItemText(0, "")
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("images/colormap_jet.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon2, "")
    self.pw_grid_combobox_10.setItemText(1, "")
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap("images/colormap_ocean.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon3, "")
    self.pw_grid_combobox_10.setItemText(2, "")
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap("images/colormap_spectral.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon4, "")
    self.pw_grid_combobox_10.setItemText(3, "")
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap("images/hot.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon5, "")
    self.pw_grid_combobox_10.setItemText(4, "")
    icon6 = QtGui.QIcon()
    icon6.addPixmap(QtGui.QPixmap("images/hsv.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon6, "")
    self.pw_grid_combobox_10.setItemText(5, "")
    icon7 = QtGui.QIcon()
    icon7.addPixmap(QtGui.QPixmap("images/seismic.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon7, "")
    self.pw_grid_combobox_10.setItemText(6, "")
    icon8 = QtGui.QIcon()
    icon8.addPixmap(QtGui.QPixmap("images/terrain.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pw_grid_combobox_10.addItem(icon8, "")
    self.pw_grid_combobox_10.setItemText(7, "")
    self.horizontalLayout_7.addWidget(self.pw_grid_combobox_10)
    spacerItem36 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_7.addItem(spacerItem36)
    self.pw_grid_info_button_5 = QtWidgets.QToolButton()
    self.pw_grid_info_button_5.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_5.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_grid_info_button_5.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_grid_info_button_5.setIcon(icon)
    self.pw_grid_info_button_5.setIconSize(QtCore.QSize(23, 23))
    self.pw_grid_info_button_5.setObjectName("pw_grid_info_button_5")
    self.horizontalLayout_7.addWidget(self.pw_grid_info_button_5)
    spacerItem37 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_7.addItem(spacerItem37)
    self.pw_grid_checkbox_2 = QtWidgets.QCheckBox()
    self.pw_grid_checkbox_2.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_checkbox_2.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_checkbox_2.setFont(font)
    self.pw_grid_checkbox_2.setStyleSheet("QCheckBox {\n"
                                          "   color: rgb(45,45,45);\n"
                                          "}")
    self.pw_grid_checkbox_2.setChecked(True)
    self.pw_grid_checkbox_2.setObjectName("pw_grid_checkbox_2")
    self.horizontalLayout_7.addWidget(self.pw_grid_checkbox_2)
    self.verticalLayout_7.addLayout(self.horizontalLayout_7)
    self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_24.setObjectName("horizontalLayout_24")
    spacerItem38 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_24.addItem(spacerItem38)
    self.verticalLayout_2 = QtWidgets.QVBoxLayout()
    self.verticalLayout_2.setObjectName("verticalLayout_2")
    self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_4.setObjectName("horizontalLayout_4")
    self.pw_grid_label_45 = QtWidgets.QLabel()
    self.pw_grid_label_45.setEnabled(True)
    self.pw_grid_label_45.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_45.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_45.setFont(font)
    self.pw_grid_label_45.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_45.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_45.setObjectName("pw_grid_label_45")
    self.horizontalLayout_4.addWidget(self.pw_grid_label_45)
    self.pw_grid_line_29 = QtWidgets.QLineEdit()
    self.pw_grid_line_29.setEnabled(True)
    self.pw_grid_line_29.setMinimumSize(QtCore.QSize(300, 27))
    self.pw_grid_line_29.setMaximumSize(QtCore.QSize(300, 27))
    self.pw_grid_line_29.setFont(font3)
    self.pw_grid_line_29.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_29.setObjectName("pw_grid_line_29")
    self.horizontalLayout_4.addWidget(self.pw_grid_line_29)
    spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_4.addItem(spacerItem39)
    self.verticalLayout_2.addLayout(self.horizontalLayout_4)
    self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_5.setObjectName("horizontalLayout_5")
    self.pw_grid_label_32 = QtWidgets.QLabel()
    self.pw_grid_label_32.setEnabled(True)
    self.pw_grid_label_32.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_32.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_32.setFont(font)
    self.pw_grid_label_32.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_32.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_32.setObjectName("pw_grid_label_32")
    self.horizontalLayout_5.addWidget(self.pw_grid_label_32)
    self.pw_grid_combobox_11 = QtWidgets.QComboBox()
    self.pw_grid_combobox_11.setEnabled(True)
    self.pw_grid_combobox_11.setMinimumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_11.setMaximumSize(QtCore.QSize(170, 27))
    self.pw_grid_combobox_11.setFont(font3)
    self.pw_grid_combobox_11.setStyleSheet("QComboBox {\n"
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
                                           "    color: rgb(145,145,145);\n"
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
                                           "QComboBox::down-arrow:disabled {\n"
                                           "    image: url(icons/down_arrow_icon_deactivated.svg); \n"
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
    self.pw_grid_combobox_11.setObjectName("pw_grid_combobox_11")
    self.pw_grid_combobox_11.addItem("")
    self.pw_grid_combobox_11.addItem("")
    self.pw_grid_combobox_11.addItem("")
    self.pw_grid_combobox_11.addItem("")
    self.horizontalLayout_5.addWidget(self.pw_grid_combobox_11)
    spacerItem40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_5.addItem(spacerItem40)
    self.pw_grid_checkbox_3 = QtWidgets.QCheckBox()
    self.pw_grid_checkbox_3.setEnabled(True)
    self.pw_grid_checkbox_3.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_checkbox_3.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_checkbox_3.setFont(font)
    self.pw_grid_checkbox_3.setStyleSheet("QCheckBox {\n"
                                          "   color: rgb(45,45,45);\n"
                                          "}\n"
                                          "\n"
                                          "QCheckBox:disabled {\n"
                                          "    color: rgb(145,145,145);\n"
                                          "}")
    self.pw_grid_checkbox_3.setObjectName("pw_grid_checkbox_3")
    self.horizontalLayout_5.addWidget(self.pw_grid_checkbox_3)
    spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_5.addItem(spacerItem41)
    self.verticalLayout_2.addLayout(self.horizontalLayout_5)
    self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_6.setObjectName("horizontalLayout_6")
    self.pw_grid_checkbox_4 = QtWidgets.QCheckBox()
    self.pw_grid_checkbox_4.setEnabled(True)
    self.pw_grid_checkbox_4.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_checkbox_4.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_checkbox_4.setFont(font)
    self.pw_grid_checkbox_4.setStyleSheet("QCheckBox {\n"
                                          "   color: rgb(45,45,45);\n"
                                          "}\n"
                                          "\n"
                                          "QCheckBox:disabled {\n"
                                          "    color: rgb(145,145,145);\n"
                                          "}")
    self.pw_grid_checkbox_4.setChecked(True)
    self.pw_grid_checkbox_4.setObjectName("pw_grid_checkbox_4")
    self.horizontalLayout_6.addWidget(self.pw_grid_checkbox_4)
    spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_6.addItem(spacerItem42)
    self.verticalLayout_2.addLayout(self.horizontalLayout_6)
    self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_23.setObjectName("horizontalLayout_23")
    spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_23.addItem(spacerItem43)
    self.gridLayout_4 = QtWidgets.QGridLayout()
    self.gridLayout_4.setObjectName("gridLayout_4")
    self.pw_grid_label_33 = QtWidgets.QLabel()
    self.pw_grid_label_33.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_33.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_33.setSizePolicy(sizePolicy)
    self.pw_grid_label_33.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_33.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_33.setFont(font)
    self.pw_grid_label_33.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_33.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_33.setObjectName("pw_grid_label_33")
    self.gridLayout_4.addWidget(self.pw_grid_label_33, 0, 0, 1, 1)
    self.pw_grid_line_5 = QtWidgets.QLineEdit()
    self.pw_grid_line_5.setEnabled(False)
    self.pw_grid_line_5.setMinimumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_5.setMaximumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_5.setFont(font3)
    self.pw_grid_line_5.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_5.setObjectName("pw_grid_line_5")
    self.gridLayout_4.addWidget(self.pw_grid_line_5, 0, 1, 1, 1)
    spacerItem44 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout_4.addItem(spacerItem44, 0, 2, 1, 1)
    self.pw_grid_label_35 = QtWidgets.QLabel()
    self.pw_grid_label_35.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_35.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_35.setSizePolicy(sizePolicy)
    self.pw_grid_label_35.setMinimumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_35.setMaximumSize(QtCore.QSize(100, 27))
    self.pw_grid_label_35.setFont(font)
    self.pw_grid_label_35.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_35.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_35.setObjectName("pw_grid_label_35")
    self.gridLayout_4.addWidget(self.pw_grid_label_35, 0, 3, 1, 1)
    self.pw_grid_line_7 = QtWidgets.QLineEdit()
    self.pw_grid_line_7.setEnabled(False)
    self.pw_grid_line_7.setMinimumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_7.setMaximumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_7.setFont(font3)
    self.pw_grid_line_7.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_7.setObjectName("pw_grid_line_7")
    self.gridLayout_4.addWidget(self.pw_grid_line_7, 0, 4, 1, 1)
    spacerItem45 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout_4.addItem(spacerItem45, 0, 5, 1, 2)
    self.pw_grid_label_34 = QtWidgets.QLabel()
    self.pw_grid_label_34.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_34.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_34.setSizePolicy(sizePolicy)
    self.pw_grid_label_34.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_34.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_grid_label_34.setFont(font)
    self.pw_grid_label_34.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_34.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_34.setObjectName("pw_grid_label_34")
    self.gridLayout_4.addWidget(self.pw_grid_label_34, 1, 0, 1, 1)
    self.pw_grid_line_6 = QtWidgets.QLineEdit()
    self.pw_grid_line_6.setEnabled(False)
    self.pw_grid_line_6.setMinimumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_6.setMaximumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_6.setFont(font3)
    self.pw_grid_line_6.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_6.setObjectName("pw_grid_line_6")
    self.gridLayout_4.addWidget(self.pw_grid_line_6, 1, 1, 1, 1)
    spacerItem46 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout_4.addItem(spacerItem46, 1, 2, 1, 1)
    self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_11.setObjectName("horizontalLayout_11")
    spacerItem47 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_11.addItem(spacerItem47)
    self.pw_grid_set_cmap_ticks = QtWidgets.QToolButton()
    self.pw_grid_set_cmap_ticks.setEnabled(False)
    self.pw_grid_set_cmap_ticks.setMinimumSize(QtCore.QSize(160, 27))
    self.pw_grid_set_cmap_ticks.setMaximumSize(QtCore.QSize(160, 27))
    self.pw_grid_set_cmap_ticks.setFont(font)
    self.pw_grid_set_cmap_ticks.setStyleSheet("QToolButton {\n"
                                              "    border: 1px solid #acacac;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                              "                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton:disabled {\n"
                                              "    background-color:  rgb(200,200,200);\n"
                                              "    color: rgb(145,145,145);\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton:hover {\n"
                                              "    border: 1px solid #7eb4ea;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                              "                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton:pressed {\n"
                                              "    border: 1px solid #579de5;\n"
                                              "    border-radius: 1px;\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                              "                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
                                              "}")
    self.pw_grid_set_cmap_ticks.setIconSize(QtCore.QSize(25, 25))
    self.pw_grid_set_cmap_ticks.setObjectName("pw_grid_set_cmap_ticks")
    self.horizontalLayout_11.addWidget(self.pw_grid_set_cmap_ticks)
    spacerItem48 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_11.addItem(spacerItem48)
    self.gridLayout_4.addLayout(self.horizontalLayout_11, 1, 3, 1, 2)
    spacerItem49 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout_4.addItem(spacerItem49, 1, 5, 1, 1)
    self.pw_grid_label_57 = QtWidgets.QLabel()
    self.pw_grid_label_57.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_57.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_57.setSizePolicy(sizePolicy)
    self.pw_grid_label_57.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_57.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_57.setFont(font4)
    self.pw_grid_label_57.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_57.setText("")
    self.pw_grid_label_57.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_57.setObjectName("pw_grid_label_57")
    self.gridLayout_4.addWidget(self.pw_grid_label_57, 1, 6, 1, 1)
    self.horizontalLayout_23.addLayout(self.gridLayout_4)
    self.verticalLayout_2.addLayout(self.horizontalLayout_23)
    self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_21.setObjectName("horizontalLayout_21")
    self.pw_grid_checkbox_5 = QtWidgets.QCheckBox()
    self.pw_grid_checkbox_5.setEnabled(True)
    self.pw_grid_checkbox_5.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_checkbox_5.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_checkbox_5.setFont(font)
    self.pw_grid_checkbox_5.setStyleSheet("QCheckBox {\n"
                                          "   color: rgb(45,45,45);\n"
                                          "}\n"
                                          "\n"
                                          "QCheckBox:disabled {\n"
                                          "    color: rgb(145,145,145);\n"
                                          "}")
    self.pw_grid_checkbox_5.setChecked(True)
    self.pw_grid_checkbox_5.setObjectName("pw_grid_checkbox_5")
    self.horizontalLayout_21.addWidget(self.pw_grid_checkbox_5)
    spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_21.addItem(spacerItem50)
    self.verticalLayout_2.addLayout(self.horizontalLayout_21)
    self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_22.setObjectName("horizontalLayout_22")
    spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_22.addItem(spacerItem51)
    self.gridLayout_12 = QtWidgets.QGridLayout()
    self.gridLayout_12.setObjectName("gridLayout_12")
    self.pw_grid_label_38 = QtWidgets.QLabel()
    self.pw_grid_label_38.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_38.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_38.setSizePolicy(sizePolicy)
    self.pw_grid_label_38.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_38.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_38.setFont(font)
    self.pw_grid_label_38.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_38.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_38.setObjectName("pw_grid_label_38")
    self.gridLayout_12.addWidget(self.pw_grid_label_38, 0, 3, 1, 1)
    spacerItem52 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout_12.addItem(spacerItem52, 1, 2, 1, 1)
    self.pw_grid_label_39 = QtWidgets.QLabel()
    self.pw_grid_label_39.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_39.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_39.setSizePolicy(sizePolicy)
    self.pw_grid_label_39.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_39.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_39.setFont(font)
    self.pw_grid_label_39.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_39.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_39.setObjectName("pw_grid_label_39")
    self.gridLayout_12.addWidget(self.pw_grid_label_39, 1, 3, 1, 1)
    self.pw_grid_line_10 = QtWidgets.QLineEdit()
    self.pw_grid_line_10.setEnabled(False)
    self.pw_grid_line_10.setMinimumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_10.setMaximumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_10.setFont(font3)
    self.pw_grid_line_10.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_10.setObjectName("pw_grid_line_10")
    self.gridLayout_12.addWidget(self.pw_grid_line_10, 0, 4, 1, 1)
    self.pw_grid_line_8 = QtWidgets.QLineEdit()
    self.pw_grid_line_8.setEnabled(False)
    self.pw_grid_line_8.setMinimumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_8.setMaximumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_8.setFont(font3)
    self.pw_grid_line_8.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_8.setObjectName("pw_grid_line_8")
    self.gridLayout_12.addWidget(self.pw_grid_line_8, 0, 1, 1, 1)
    self.pw_grid_label_37 = QtWidgets.QLabel()
    self.pw_grid_label_37.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_37.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_37.setSizePolicy(sizePolicy)
    self.pw_grid_label_37.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_37.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_37.setFont(font)
    self.pw_grid_label_37.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_37.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_37.setObjectName("pw_grid_label_37")
    self.gridLayout_12.addWidget(self.pw_grid_label_37, 1, 0, 1, 1)
    spacerItem53 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout_12.addItem(spacerItem53, 0, 2, 1, 1)
    self.pw_grid_line_11 = QtWidgets.QLineEdit()
    self.pw_grid_line_11.setEnabled(False)
    self.pw_grid_line_11.setMinimumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_11.setMaximumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_11.setFont(font3)
    self.pw_grid_line_11.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_11.setObjectName("pw_grid_line_11")
    self.gridLayout_12.addWidget(self.pw_grid_line_11, 1, 4, 1, 1)
    self.pw_grid_label_36 = QtWidgets.QLabel()
    self.pw_grid_label_36.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pw_grid_label_36.sizePolicy().hasHeightForWidth())
    self.pw_grid_label_36.setSizePolicy(sizePolicy)
    self.pw_grid_label_36.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_grid_label_36.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_grid_label_36.setFont(font)
    self.pw_grid_label_36.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
    self.pw_grid_label_36.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    self.pw_grid_label_36.setObjectName("pw_grid_label_36")
    self.gridLayout_12.addWidget(self.pw_grid_label_36, 0, 0, 1, 1)
    self.pw_grid_line_9 = QtWidgets.QLineEdit()
    self.pw_grid_line_9.setEnabled(False)
    self.pw_grid_line_9.setMinimumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_9.setMaximumSize(QtCore.QSize(70, 27))
    self.pw_grid_line_9.setFont(font3)
    self.pw_grid_line_9.setStyleSheet("QLineEdit {\n"
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
    self.pw_grid_line_9.setObjectName("pw_grid_line_9")
    self.gridLayout_12.addWidget(self.pw_grid_line_9, 1, 1, 1, 1)
    self.horizontalLayout_22.addLayout(self.gridLayout_12)
    spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_22.addItem(spacerItem54)
    self.verticalLayout_2.addLayout(self.horizontalLayout_22)
    self.horizontalLayout_24.addLayout(self.verticalLayout_2)
    self.verticalLayout_7.addLayout(self.horizontalLayout_24)
    self.pw_plotOptions_la.addLayout(self.verticalLayout_7)
    self.pw_plotOptions_la.setAlignment(QtCore.Qt.AlignTop)
    self.pw_grid_label_11.setText("Plot options")
    self.pw_grid_label_12.setText("Projection:")
    self.pw_grid_set_options.setText("Set options")
    self.pw_grid_label_13.setText("Options:")
    self.pw_grid_label_22.setText("Ticks:")
    self.pw_grid_set_ticks.setText("Set X/Y ticks")
    self.pw_grid_label_14.setText("X:")
    self.pw_grid_label_15.setText("Y:")
    self.pw_grid_label_26.setText("Boundaries:")
    self.pw_grid_checkbox_6.setText("Display coastlines and lands ?")
    self.pw_grid_label_27.setText("Resolution:")
    self.pw_grid_combobox_12.setItemText(0, "10m")
    self.pw_grid_combobox_12.setItemText(1, "50m")
    self.pw_grid_combobox_12.setItemText(2, "110m")
    self.pw_grid_label_29.setText("Line width:")
    self.pw_grid_label_30.setText("Line color:")
    self.pw_grid_combobox_13.setItemText(0, "HEX Color")
    self.pw_grid_combobox_13.setItemText(1, "RGB Color")
    self.pw_grid_combobox_13.setItemText(2, "Black")
    self.pw_grid_combobox_13.setItemText(3, "Blue")
    self.pw_grid_combobox_13.setItemText(4, "Cyan")
    self.pw_grid_combobox_13.setItemText(5, "Green")
    self.pw_grid_combobox_13.setItemText(6, "Magenta")
    self.pw_grid_combobox_13.setItemText(7, "Red")
    self.pw_grid_combobox_13.setItemText(8, "Yellow")
    self.pw_grid_combobox_13.setItemText(9, "White")
    self.pw_grid_label_40.setText("Fill color:")
    self.pw_grid_combobox_14.setItemText(0, "No color")
    self.pw_grid_combobox_14.setItemText(1, "HEX Color")
    self.pw_grid_combobox_14.setItemText(2, "RGB Color")
    self.pw_grid_combobox_14.setItemText(3, "Black")
    self.pw_grid_combobox_14.setItemText(4, "Blue")
    self.pw_grid_combobox_14.setItemText(5, "Cyan")
    self.pw_grid_combobox_14.setItemText(6, "Green")
    self.pw_grid_combobox_14.setItemText(7, "Magenta")
    self.pw_grid_combobox_14.setItemText(8, "Red")
    self.pw_grid_combobox_14.setItemText(9, "Yellow")
    self.pw_grid_combobox_14.setItemText(10, "White")
    self.pw_grid_checkbox_7.setText("Display lake and rivers ?")
    self.pw_grid_label_28.setText("Resolution:")
    self.pw_grid_combobox_15.setItemText(0, "10m")
    self.pw_grid_combobox_15.setItemText(1, "50m")
    self.pw_grid_combobox_15.setItemText(2, "110m")
    self.pw_grid_label_41.setText("Line width:")
    self.pw_grid_label_42.setText("Line color:")
    self.pw_grid_combobox_16.setItemText(0, "HEX Color")
    self.pw_grid_combobox_16.setItemText(1, "RGB Color")
    self.pw_grid_combobox_16.setItemText(2, "Black")
    self.pw_grid_combobox_16.setItemText(3, "Blue")
    self.pw_grid_combobox_16.setItemText(4, "Cyan")
    self.pw_grid_combobox_16.setItemText(5, "Green")
    self.pw_grid_combobox_16.setItemText(6, "Magenta")
    self.pw_grid_combobox_16.setItemText(7, "Red")
    self.pw_grid_combobox_16.setItemText(8, "Yellow")
    self.pw_grid_combobox_16.setItemText(9, "White")
    self.pw_grid_label_43.setText("Fill color:")
    self.pw_grid_combobox_17.setItemText(0, "No color")
    self.pw_grid_combobox_17.setItemText(1, "HEX Color")
    self.pw_grid_combobox_17.setItemText(2, "RGB Color")
    self.pw_grid_combobox_17.setItemText(3, "Black")
    self.pw_grid_combobox_17.setItemText(4, "Blue")
    self.pw_grid_combobox_17.setItemText(5, "Cyan")
    self.pw_grid_combobox_17.setItemText(6, "Green")
    self.pw_grid_combobox_17.setItemText(7, "Magenta")
    self.pw_grid_combobox_17.setItemText(8, "Red")
    self.pw_grid_combobox_17.setItemText(9, "Yellow")
    self.pw_grid_combobox_17.setItemText(10, "White")
    self.pw_grid_label_44.setText("Grid:")
    self.pw_grid_checkbox_1.setText("Display grid ?")
    self.pw_grid_label_23.setText("Line style:")
    self.pw_grid_combobox_8.setItemText(0, "Dashed")
    self.pw_grid_combobox_8.setItemText(1, "Dash-dot")
    self.pw_grid_combobox_8.setItemText(2, "Dotted")
    self.pw_grid_combobox_8.setItemText(3, "Solid")
    self.pw_grid_label_24.setText("Line size:")
    self.pw_grid_label_25.setText("Line color:")
    self.pw_grid_combobox_18.setItemText(0, "HEX Color")
    self.pw_grid_combobox_18.setItemText(1, "RGB Color")
    self.pw_grid_combobox_18.setItemText(2, "Black")
    self.pw_grid_combobox_18.setItemText(3, "Blue")
    self.pw_grid_combobox_18.setItemText(4, "Cyan")
    self.pw_grid_combobox_18.setItemText(5, "Green")
    self.pw_grid_combobox_18.setItemText(6, "Magenta")
    self.pw_grid_combobox_18.setItemText(7, "Red")
    self.pw_grid_combobox_18.setItemText(8, "Yellow")
    self.pw_grid_combobox_18.setItemText(9, "White")
    self.pw_grid_label_21.setText("Colormap options")
    self.pw_grid_label_31.setText("Select a colormap:")
    self.pw_grid_checkbox_2.setText("Display colormap ?")
    self.pw_grid_label_45.setText("Colormap legend:")
    self.pw_grid_label_32.setText("Colormap position:")
    self.pw_grid_combobox_11.setItemText(0, "horizontal - bottom")
    self.pw_grid_combobox_11.setItemText(1, "horizontal - top")
    self.pw_grid_combobox_11.setItemText(2, "vertical - left")
    self.pw_grid_combobox_11.setItemText(3, "vertical - right")
    self.pw_grid_checkbox_3.setText("Reverse colormap ?")
    self.pw_grid_checkbox_4.setText("Handle colormap values automatically ?")
    self.pw_grid_checkbox_5.setText("Handle colormap dimensions automatically ?")
    self.pw_grid_label_33.setText("Min:")
    self.pw_grid_label_35.setText("Nbr of steps:")
    self.pw_grid_label_34.setText("Max:")
    self.pw_grid_set_cmap_ticks.setText("Set colorbar ticks")
    self.pw_grid_label_38.setText("Colormap width:")
    self.pw_grid_label_39.setText("Colormap height:")
    self.pw_grid_label_37.setText("Position from bottom:")
    self.pw_grid_label_36.setText("Position from left:")
    self.pw_grid_combobox_7.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_12.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_13.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_14.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_15.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_16.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_17.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_8.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_18.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_10.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_11.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_grid_combobox_12.setCurrentIndex(2)
    self.pw_grid_combobox_13.setCurrentIndex(2)
    self.pw_grid_combobox_15.setCurrentIndex(2)
    self.pw_grid_combobox_16.setCurrentIndex(2)
    self.pw_grid_combobox_18.setCurrentIndex(2)
    self.pw_grid_combobox_10.setCurrentIndex(1)
    self.pw_grid_combobox_11.setCurrentIndex(3)
    self.pw_grid_combobox_8.setCurrentIndex(3)
    self.pw_grid_line_13.setVisible(False)
    self.pw_grid_line_14.setVisible(False)
    self.pw_grid_line_15.setVisible(False)
    self.pw_grid_line_13.setEnabled(False)
    self.pw_grid_line_14.setEnabled(False)
    self.pw_grid_line_15.setEnabled(False)
    self.pw_grid_line_16.setVisible(False)
    self.pw_grid_line_17.setVisible(False)
    self.pw_grid_line_18.setVisible(False)
    self.pw_grid_line_20.setVisible(False)
    self.pw_grid_line_21.setVisible(False)
    self.pw_grid_line_22.setVisible(False)
    self.pw_grid_line_23.setVisible(False)
    self.pw_grid_line_24.setVisible(False)
    self.pw_grid_line_25.setVisible(False)
    self.pw_grid_line_26.setVisible(False)
    self.pw_grid_line_27.setVisible(False)
    self.pw_grid_line_28.setVisible(False)
    populate_combobox(self.pw_grid_combobox_7, grid_projection_list(), False, 13)
    self.pw_grid_combobox_7.currentIndexChanged.connect(lambda: set_projection_options(self))
    self.pw_grid_combobox_11.currentIndexChanged.connect(lambda: set_colormap_default_margins(self))
    self.pw_grid_combobox_13.currentIndexChanged.connect(lambda: activate_boundaries_hex_rgb_color(self))
    self.pw_grid_combobox_14.currentIndexChanged.connect(lambda: activate_boundaries_hex_rgb_color(self))
    self.pw_grid_combobox_16.currentIndexChanged.connect(lambda: activate_boundaries_hex_rgb_color(self))
    self.pw_grid_combobox_17.currentIndexChanged.connect(lambda: activate_boundaries_hex_rgb_color(self))
    self.pw_grid_combobox_18.currentIndexChanged.connect(lambda: activate_boundaries_hex_rgb_color(self))
    self.pw_grid_checkbox_6.stateChanged.connect(lambda: activate_coastlines_options(self))
    self.pw_grid_checkbox_7.stateChanged.connect(lambda: activate_lakes_options(self))
    self.pw_grid_checkbox_1.stateChanged.connect(lambda: activate_grid_options(self))
    self.pw_grid_checkbox_5.stateChanged.connect(lambda: activate_colormap_dimensions(self))
    self.pw_grid_checkbox_4.stateChanged.connect(lambda: activate_colormap_values(self))
    self.pw_grid_checkbox_2.stateChanged.connect(lambda: activate_colormap_options(self))
    self.pw_grid_set_options.clicked.connect(lambda: projection_option_window(self))
    self.pw_grid_set_ticks.clicked.connect(lambda: tick_option_window(self))
    self.pw_grid_set_cmap_ticks.clicked.connect(lambda: colorbar_tick_option_window(self))
    self.pw_grid_line_5.textEdited.connect(lambda: colorbar_tick_option_man_remove(self))
    self.pw_grid_line_6.textEdited.connect(lambda: colorbar_tick_option_man_remove(self))
    self.pw_grid_line_7.textEdited.connect(lambda: colorbar_tick_option_man_remove(self))
    self.pw_grid_info_button_3.clicked.connect(self.figure_button_information)
    self.pw_grid_info_button_4.clicked.connect(self.figure_button_information)
    self.pw_grid_info_button_5.clicked.connect(self.figure_button_information)
    self.pw_grid_info_button_6.clicked.connect(self.figure_button_information)
    self.pw_grid_info_button_7.clicked.connect(self.figure_button_information)
    self.pw_grid_info_button_8.clicked.connect(self.figure_button_information)
    display_grid_projection_options(self)
    display_grid_ticks_options(self)
    self.pw_grid_line_12.setText('1')
    self.pw_grid_combobox_14.setCurrentIndex(1)
    self.pw_grid_line_18.setText('#e6e6e6')
    self.pw_grid_line_19.setText('0.5')
    self.pw_grid_checkbox_1.setChecked(True)
    self.pw_grid_line_29.setText(self.gd_plot_options['colorbar_legend'])
    self.pw_grid_combobox_16.setCurrentIndex(3)
    self.pw_grid_combobox_17.setCurrentIndex(4)
