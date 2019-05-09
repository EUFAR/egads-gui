import logging
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_displayalgorithmwindow import Ui_displayAlgorithmWindow
from ui.Ui_processingwindow import Ui_processingWindow
from ui.Ui_creationwindow import Ui_creationWindow
from functions.utils import Highlighter, create_datestring, prepare_long_string, check_string_max_length
from functions.utils import write_algorithm
from functions.other_windows_functions import MyInfo, MyFill, MyUnit, MyFilename, MyCategory, MyOverwriteFilename
from functions.other_windows_functions import MyWait
from functions.thread_functions import VariableProcessingThread
from functions.material_functions import algorithm_information_buttons_text
import egads


class MyAlgorithmDisplay(QtWidgets.QDialog, Ui_displayAlgorithmWindow):
    def __init__(self, algorithm_dict):
        logging.debug('gui - other_windows_functions.py - MyAlgorithmDisplay - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.algorithm_dict = algorithm_dict
        self.setWindowTitle('Algorithm - ' + self.algorithm_dict['File'])
        self.daw_okButton.clicked.connect(self.closeWindow)
        self.input_label_1 = []
        self.input_label_2 = []
        self.input_label_3 = []
        self.input_edit_1 = []
        self.input_edit_2 = []
        self.input_edit_3 = []
        self.input_line = []
        self.input_hor_lay_1 = []
        self.input_hor_lay_2 = []
        self.input_hor_lay_3 = []
        self.input_hor_lay_4 = []
        self.input_ver_lay_1 = []
        self.input_ver_lay_2 = []
        self.input_ver_lay_3 = []
        self.input_nbr = 0
        self.output_label_1 = []
        self.output_label_2 = []
        self.output_label_3 = []
        self.output_label_4 = []
        self.output_label_5 = []
        self.output_label_6 = []
        self.output_edit_1 = []
        self.output_edit_2 = []
        self.output_edit_3 = []
        self.output_edit_4 = []
        self.output_edit_5 = []
        self.output_edit_6 = []
        self.output_line = []
        self.output_hor_lay_1 = []
        self.output_hor_lay_2 = []
        self.output_hor_lay_3 = []
        self.output_hor_lay_4 = []
        self.output_nbr = 0
        self.highlighter = None
        self.populate_information()
        self.populate_algorithm()
        self.populate_inputs()
        self.populate_outputs()
        logging.info('gui - other_windows_functions.py - MyAlgorithmDisplay ready')

    def populate_information(self):
        self.daw_line_1.setText(self.algorithm_dict['Name'])
        self.daw_line_2.setText(self.algorithm_dict['Date'])
        self.daw_line_3.setText(self.algorithm_dict['Version'])
        self.daw_plain_1.setPlainText(self.algorithm_dict['Purpose'])
        self.daw_plain_2.setPlainText(self.algorithm_dict['Description'])
        self.daw_plain_3.setPlainText(self.algorithm_dict['Source'])
        self.daw_plain_4.setPlainText(self.algorithm_dict['References'])

    def populate_inputs(self):
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
        for input_dict in self.algorithm_dict['Input']:
            self.input_hor_lay_1.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_1[self.input_nbr].setObjectName('input_hor_lay_1_' + str(self.input_nbr))
            self.input_ver_lay_1.append(QtWidgets.QVBoxLayout())
            self.input_ver_lay_1[self.input_nbr].setObjectName('input_ver_lay_1_' + str(self.input_nbr))
            self.input_hor_lay_2.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_2[self.input_nbr].setObjectName('input_hor_lay_2_' + str(self.input_nbr))
            self.input_hor_lay_3.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_3[self.input_nbr].setObjectName('input_hor_lay_3_' + str(self.input_nbr))
            self.input_label_1.append(QtWidgets.QLabel())
            self.input_label_1[self.input_nbr].setMinimumSize(QtCore.QSize(80, 27))
            self.input_label_1[self.input_nbr].setMaximumSize(QtCore.QSize(80, 27))
            self.input_label_1[self.input_nbr].setFont(font)
            self.input_label_1[self.input_nbr].setStyleSheet("QLabel {\n"
                                                             "   color: rgb(45,45,45);\n"
                                                             "}")
            self.input_label_1[self.input_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                            QtCore.Qt.AlignTrailing |
                                                            QtCore.Qt.AlignVCenter)
            self.input_label_1[self.input_nbr].setObjectName('input_label_1_' + str(self.input_nbr))
            self.input_label_1[self.input_nbr].setText('Symbol:')
            self.input_hor_lay_2[self.input_nbr].addWidget(self.input_label_1[self.input_nbr])
            self.input_edit_1.append(QtWidgets.QLineEdit())
            self.input_edit_1[self.input_nbr].setEnabled(True)
            self.input_edit_1[self.input_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.input_edit_1[self.input_nbr].setMaximumSize(QtCore.QSize(150, 27))
            self.input_edit_1[self.input_nbr].setFont(font)
            self.input_edit_1[self.input_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.input_edit_1[self.input_nbr].setStyleSheet("QLineEdit {\n"
                                                            "  border-radius: 3px;\n"
                                                            "  padding: 1px 4px 1px 4px;\n"
                                                            "  background-color: rgb(240, 240, 240);\n"
                                                            "  color: rgb(45,45,45);\n"
                                                            "}\n"
                                                            "\n"
                                                            "QLineEdit:disabled {\n"
                                                            "  background-color: rgb(240, 240, 240);\n"
                                                            "}")
            self.input_edit_1[self.input_nbr].setText('')
            self.input_edit_1[self.input_nbr].setFrame(False)
            self.input_edit_1[self.input_nbr].setReadOnly(True)
            self.input_edit_1[self.input_nbr].setObjectName('input_edit_1_' + str(self.input_nbr))
            self.input_hor_lay_2[self.input_nbr].addWidget(self.input_edit_1[self.input_nbr])
            self.input_ver_lay_1[self.input_nbr].addLayout(self.input_hor_lay_2[self.input_nbr])
            self.input_label_2.append(QtWidgets.QLabel())
            self.input_label_2[self.input_nbr].setMinimumSize(QtCore.QSize(80, 27))
            self.input_label_2[self.input_nbr].setMaximumSize(QtCore.QSize(80, 27))
            self.input_label_2[self.input_nbr].setFont(font)
            self.input_label_2[self.input_nbr].setStyleSheet("QLabel {\n"
                                                             "   color: rgb(45,45,45);\n"
                                                             "}")
            self.input_label_2[self.input_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                            QtCore.Qt.AlignTrailing |
                                                            QtCore.Qt.AlignVCenter)
            self.input_label_2[self.input_nbr].setObjectName('input_label_2_' + str(self.input_nbr))
            self.input_label_2[self.input_nbr].setText('Units:')
            self.input_hor_lay_3[self.input_nbr].addWidget(self.input_label_2[self.input_nbr])
            self.input_edit_2.append(QtWidgets.QLineEdit())
            self.input_edit_2[self.input_nbr].setEnabled(True)
            self.input_edit_2[self.input_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.input_edit_2[self.input_nbr].setMaximumSize(QtCore.QSize(150, 27))
            self.input_edit_2[self.input_nbr].setFont(font)
            self.input_edit_2[self.input_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.input_edit_2[self.input_nbr].setStyleSheet("QLineEdit {\n"
                                                            "  border-radius: 3px;\n"
                                                            "  padding: 1px 4px 1px 4px;\n"
                                                            "  background-color: rgb(240, 240, 240);\n"
                                                            "  color: rgb(45,45,45);\n"
                                                            "}\n"
                                                            "\n"
                                                            "QLineEdit:disabled {\n"
                                                            "  background-color: rgb(240, 240, 240);\n"
                                                            "}")
            self.input_edit_2[self.input_nbr].setText('')
            self.input_edit_2[self.input_nbr].setFrame(False)
            self.input_edit_2[self.input_nbr].setReadOnly(True)
            self.input_edit_2[self.input_nbr].setObjectName('input_edit_2_' + str(self.input_nbr))
            self.input_hor_lay_3[self.input_nbr].addWidget(self.input_edit_2[self.input_nbr])
            self.input_ver_lay_1[self.input_nbr].addLayout(self.input_hor_lay_3[self.input_nbr])
            self.input_hor_lay_1[self.input_nbr].addLayout(self.input_ver_lay_1[self.input_nbr])
            self.input_hor_lay_4.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_4[self.input_nbr].setObjectName('input_hor_lay_4_' + str(self.input_nbr))
            self.input_ver_lay_2.append(QtWidgets.QHBoxLayout())
            self.input_ver_lay_2[self.input_nbr].setObjectName('input_ver_lay_2_' + str(self.input_nbr))
            self.input_label_3.append(QtWidgets.QLabel())
            self.input_label_3[self.input_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.input_label_3[self.input_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.input_label_3[self.input_nbr].setFont(font)
            self.input_label_3[self.input_nbr].setStyleSheet("QLabel {\n"
                                                             "   color: rgb(45,45,45);\n"
                                                             "}")
            self.input_label_3[self.input_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                            QtCore.Qt.AlignTrailing |
                                                            QtCore.Qt.AlignVCenter)
            self.input_label_3[self.input_nbr].setObjectName('input_label_3_' + str(self.input_nbr))
            self.input_label_3[self.input_nbr].setText('Description:')
            self.input_ver_lay_2[self.input_nbr].addWidget(self.input_label_3[self.input_nbr])
            self.input_hor_lay_4[self.input_nbr].addLayout(self.input_ver_lay_2[self.input_nbr])
            self.input_edit_3.append(QtWidgets.QPlainTextEdit())
            self.input_edit_3[self.input_nbr].setEnabled(True)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.input_edit_3[self.input_nbr].sizePolicy().hasHeightForWidth())
            self.input_edit_3[self.input_nbr].setSizePolicy(size_policy)
            self.input_edit_3[self.input_nbr].setMinimumSize(QtCore.QSize(200, 60))
            self.input_edit_3[self.input_nbr].setMaximumSize(QtCore.QSize(16777215, 60))
            self.input_edit_3[self.input_nbr].setFont(font2)
            self.input_edit_3[self.input_nbr].viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.input_edit_3[self.input_nbr].setStyleSheet("QPlainTextEdit {\n"
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
            self.input_edit_3[self.input_nbr].setFrameShape(QtWidgets.QFrame.NoFrame)
            self.input_edit_3[self.input_nbr].setReadOnly(True)
            self.input_edit_3[self.input_nbr].setPlainText("")
            self.input_edit_3[self.input_nbr].setObjectName('input_edit_3_' + str(self.input_nbr))
            self.input_hor_lay_4[self.input_nbr].addWidget(self.input_edit_3[self.input_nbr])
            self.input_hor_lay_1[self.input_nbr].addLayout(self.input_hor_lay_4[self.input_nbr])
            self.input_layout.addLayout(self.input_hor_lay_1[self.input_nbr])
            self.input_line.append(QtWidgets.QFrame())
            self.input_line[self.input_nbr].setFrameShape(QtWidgets.QFrame.HLine)
            self.input_line[self.input_nbr].setFrameShadow(QtWidgets.QFrame.Sunken)
            self.input_line[self.input_nbr].setObjectName('input_line_' + str(self.input_nbr))
            self.input_line[self.input_nbr].setStyleSheet("QFrame {\n"
                                                          "    background: rgb(190,190,190);\n"
                                                          "    height: 5px;\n"
                                                          "    border: 0px solid black;\n"
                                                          "}")
            self.input_layout.addWidget(self.input_line[self.input_nbr])
            self.input_edit_1[self.input_nbr].setText(input_dict['Symbol'])
            self.input_edit_2[self.input_nbr].setText(input_dict['Units'])
            self.input_edit_3[self.input_nbr].setPlainText(input_dict['Description'])
            self.input_nbr += 1

    def populate_outputs(self):
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
        for output_dict in self.algorithm_dict['Output']:
            self.output_hor_lay_1.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_1[self.output_nbr].setObjectName('output_hor_lay_1_' + str(self.output_nbr))
            self.output_hor_lay_2.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_2[self.output_nbr].setObjectName('output_hor_lay_2_' + str(self.output_nbr))
            self.output_hor_lay_3.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_3[self.output_nbr].setObjectName('output_hor_lay_3_' + str(self.output_nbr))
            self.output_hor_lay_4.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_4[self.output_nbr].setObjectName('output_hor_lay_4_' + str(self.output_nbr))
            self.output_label_1.append(QtWidgets.QLabel())
            self.output_label_1[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_1[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_label_1[self.output_nbr].setFont(font)
            self.output_label_1[self.output_nbr].setStyleSheet("QLabel {\n"
                                                               "   color: rgb(45,45,45);\n"
                                                               "}")
            self.output_label_1[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_1[self.output_nbr].setObjectName('output_label_1_' + str(self.output_nbr))
            self.output_label_1[self.output_nbr].setText('Symbol:')
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_label_1[self.output_nbr])
            self.output_edit_1.append(QtWidgets.QLineEdit())
            self.output_edit_1[self.output_nbr].setEnabled(True)
            self.output_edit_1[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_edit_1[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_edit_1[self.output_nbr].setFont(font)
            self.output_edit_1[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_1[self.output_nbr].setStyleSheet("QLineEdit {\n"
                                                              "  border-radius: 3px;\n"
                                                              "  padding: 1px 4px 1px 4px;\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "  color: rgb(45,45,45);\n"
                                                              "}\n"
                                                              "\n"
                                                              "QLineEdit:disabled {\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "}")
            self.output_edit_1[self.output_nbr].setText('')
            self.output_edit_1[self.output_nbr].setFrame(False)
            self.output_edit_1[self.output_nbr].setReadOnly(True)
            self.output_edit_1[self.output_nbr].setObjectName('output_edit_1_' + str(self.output_nbr))
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_edit_1[self.output_nbr])
            self.output_label_2.append(QtWidgets.QLabel())
            self.output_label_2[self.output_nbr].setMinimumSize(QtCore.QSize(130, 27))
            self.output_label_2[self.output_nbr].setMaximumSize(QtCore.QSize(130, 27))
            self.output_label_2[self.output_nbr].setFont(font)
            self.output_label_2[self.output_nbr].setStyleSheet("QLabel {\n"
                                                               "   color: rgb(45,45,45);\n"
                                                               "}")
            self.output_label_2[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_2[self.output_nbr].setObjectName('output_label_2_' + str(self.output_nbr))
            self.output_label_2[self.output_nbr].setText('Standard Name:')
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_label_2[self.output_nbr])
            self.output_edit_2.append(QtWidgets.QLineEdit())
            self.output_edit_2[self.output_nbr].setEnabled(True)
            self.output_edit_2[self.output_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.output_edit_2[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 27))
            self.output_edit_2[self.output_nbr].setFont(font)
            self.output_edit_2[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_2[self.output_nbr].setStyleSheet("QLineEdit {\n"
                                                              "  border-radius: 3px;\n"
                                                              "  padding: 1px 4px 1px 4px;\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "  color: rgb(45,45,45);\n"
                                                              "}\n"
                                                              "\n"
                                                              "QLineEdit:disabled {\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "}")
            self.output_edit_2[self.output_nbr].setText('')
            self.output_edit_2[self.output_nbr].setFrame(False)
            self.output_edit_2[self.output_nbr].setReadOnly(True)
            self.output_edit_2[self.output_nbr].setObjectName('output_edit_2_' + str(self.output_nbr))
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_edit_2[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_1[self.output_nbr])
            self.output_label_3.append(QtWidgets.QLabel())
            self.output_label_3[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_3[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_label_3[self.output_nbr].setFont(font)
            self.output_label_3[self.output_nbr].setStyleSheet("QLabel {\n"
                                                               "   color: rgb(45,45,45);\n"
                                                               "}")
            self.output_label_3[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_3[self.output_nbr].setObjectName('output_label_3_' + str(self.output_nbr))
            self.output_label_3[self.output_nbr].setText('Units:')
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_label_3[self.output_nbr])
            self.output_edit_3.append(QtWidgets.QLineEdit())
            self.output_edit_3[self.output_nbr].setEnabled(True)
            self.output_edit_3[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_edit_3[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_edit_3[self.output_nbr].setFont(font)
            self.output_edit_3[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_3[self.output_nbr].setStyleSheet("QLineEdit {\n"
                                                              "  border-radius: 3px;\n"
                                                              "  padding: 1px 4px 1px 4px;\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "  color: rgb(45,45,45);\n"
                                                              "}\n"
                                                              "\n"
                                                              "QLineEdit:disabled {\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "}")
            self.output_edit_3[self.output_nbr].setText('')
            self.output_edit_3[self.output_nbr].setFrame(False)
            self.output_edit_3[self.output_nbr].setReadOnly(True)
            self.output_edit_3[self.output_nbr].setObjectName('output_edit_3_' + str(self.output_nbr))
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_edit_3[self.output_nbr])
            self.output_label_4.append(QtWidgets.QLabel())
            self.output_label_4[self.output_nbr].setMinimumSize(QtCore.QSize(130, 27))
            self.output_label_4[self.output_nbr].setMaximumSize(QtCore.QSize(130, 27))
            self.output_label_4[self.output_nbr].setFont(font)
            self.output_label_4[self.output_nbr].setStyleSheet("QLabel {\n"
                                                               "   color: rgb(45,45,45);\n"
                                                               "}")
            self.output_label_4[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_4[self.output_nbr].setObjectName('output_label_4_' + str(self.output_nbr))
            self.output_label_4[self.output_nbr].setText('Long Name:')
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_label_4[self.output_nbr])
            self.output_edit_4.append(QtWidgets.QLineEdit())
            self.output_edit_4[self.output_nbr].setEnabled(True)
            self.output_edit_4[self.output_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.output_edit_4[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 27))
            self.output_edit_4[self.output_nbr].setFont(font)
            self.output_edit_4[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_4[self.output_nbr].setStyleSheet("QLineEdit {\n"
                                                              "  border-radius: 3px;\n"
                                                              "  padding: 1px 4px 1px 4px;\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "  color: rgb(45,45,45);\n"
                                                              "}\n"
                                                              "\n"
                                                              "QLineEdit:disabled {\n"
                                                              "  background-color: rgb(240, 240, 240);\n"
                                                              "}")
            self.output_edit_4[self.output_nbr].setText('')
            self.output_edit_4[self.output_nbr].setFrame(False)
            self.output_edit_4[self.output_nbr].setReadOnly(True)
            self.output_edit_4[self.output_nbr].setObjectName('output_edit_4_' + str(self.output_nbr))
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_edit_4[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_2[self.output_nbr])
            self.output_label_5.append(QtWidgets.QLabel())
            self.output_label_5[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_5[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_label_5[self.output_nbr].setFont(font)
            self.output_label_5[self.output_nbr].setStyleSheet("QLabel {\n"
                                                               "   color: rgb(45,45,45);\n"
                                                               "}")
            self.output_label_5[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_5[self.output_nbr].setObjectName('output_label_5_' + str(self.output_nbr))
            self.output_label_5[self.output_nbr].setText('Description:')
            self.output_hor_lay_3[self.output_nbr].addWidget(self.output_label_5[self.output_nbr])
            self.output_edit_5.append(QtWidgets.QPlainTextEdit())
            self.output_edit_5[self.output_nbr].setEnabled(True)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.output_edit_5[self.output_nbr].sizePolicy().hasHeightForWidth())
            self.output_edit_5[self.output_nbr].setSizePolicy(size_policy)
            self.output_edit_5[self.output_nbr].setMinimumSize(QtCore.QSize(200, 60))
            self.output_edit_5[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 60))
            self.output_edit_5[self.output_nbr].setFont(font2)
            self.output_edit_5[self.output_nbr].viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_5[self.output_nbr].setStyleSheet("QPlainTextEdit {\n"
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
            self.output_edit_5[self.output_nbr].setFrameShape(QtWidgets.QFrame.NoFrame)
            self.output_edit_5[self.output_nbr].setReadOnly(True)
            self.output_edit_5[self.output_nbr].setPlainText("")
            self.output_edit_5[self.output_nbr].setObjectName('output_edit_5_' + str(self.output_nbr))
            self.output_hor_lay_3[self.output_nbr].addWidget(self.output_edit_5[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_3[self.output_nbr])
            self.output_label_6.append(QtWidgets.QLabel())
            self.output_label_6[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_6[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_label_6[self.output_nbr].setFont(font)
            self.output_label_6[self.output_nbr].setStyleSheet("QLabel {\n"
                                                               "   color: rgb(45,45,45);\n"
                                                               "}")
            self.output_label_6[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_6[self.output_nbr].setObjectName('output_label_6_' + str(self.output_nbr))
            self.output_label_6[self.output_nbr].setText('Category:')
            self.output_hor_lay_4[self.output_nbr].addWidget(self.output_label_6[self.output_nbr])
            self.output_edit_6.append(QtWidgets.QPlainTextEdit())
            self.output_edit_6[self.output_nbr].setEnabled(True)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.output_edit_6[self.output_nbr].sizePolicy().hasHeightForWidth())
            self.output_edit_6[self.output_nbr].setSizePolicy(size_policy)
            self.output_edit_6[self.output_nbr].setMinimumSize(QtCore.QSize(200, 60))
            self.output_edit_6[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 60))
            self.output_edit_6[self.output_nbr].setFont(font2)
            self.output_edit_6[self.output_nbr].viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_6[self.output_nbr].setStyleSheet("QPlainTextEdit {\n"
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
            self.output_edit_6[self.output_nbr].setFrameShape(QtWidgets.QFrame.NoFrame)
            self.output_edit_6[self.output_nbr].setReadOnly(True)
            self.output_edit_6[self.output_nbr].setPlainText("")
            self.output_edit_6[self.output_nbr].setObjectName('output_edit_6_' + str(self.output_nbr))
            self.output_hor_lay_4[self.output_nbr].addWidget(self.output_edit_6[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_4[self.output_nbr])
            self.output_line.append(QtWidgets.QFrame())
            self.output_line[self.output_nbr].setFrameShape(QtWidgets.QFrame.HLine)
            self.output_line[self.output_nbr].setFrameShadow(QtWidgets.QFrame.Sunken)
            self.output_line[self.output_nbr].setObjectName('output_line_' + str(self.output_nbr))
            self.output_line[self.output_nbr].setStyleSheet("QFrame {\n"
                                                            "    background: rgb(190,190,190);\n"
                                                            "    height: 5px;\n"
                                                            "    border: 0px solid black;\n"
                                                            "}")
            self.output_layout.addWidget(self.output_line[self.output_nbr])
            self.output_edit_1[self.output_nbr].setText(output_dict['Symbol'])
            self.output_edit_2[self.output_nbr].setText(output_dict['StandardName'])
            self.output_edit_3[self.output_nbr].setText(output_dict['Units'])
            self.output_edit_4[self.output_nbr].setText(output_dict['LongName'])
            self.output_edit_5[self.output_nbr].setPlainText(output_dict['Description'])
            if isinstance(output_dict['Category'], list):
                category_str = ''
                for category in output_dict['Category']:
                    category_str += category + ', '
                category_str = category_str[0:-2]
                self.output_edit_6[self.output_nbr].setPlainText(category_str)
            else:
                self.output_edit_6[self.output_nbr].setPlainText(output_dict['Category'])
            self.output_nbr += 1

    def populate_algorithm(self):
        self.daw_plain_5.setPlainText(self.algorithm_dict['Algorithm'])
        self.highlighter = Highlighter(self.daw_plain_5.document())

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyAlgorithmDisplay - closeWindow')
        self.close()


class MyProcessing(QtWidgets.QDialog, Ui_processingWindow):
    def __init__(self, list_of_algorithms, list_of_variables_and_attributes, list_of_new_variables_and_attributes):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.aw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.aw_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.list_of_algorithms = list_of_algorithms
        self.list_of_new_variables_and_attributes = list_of_new_variables_and_attributes
        self.list_of_variables_and_attributes = dict(list_of_variables_and_attributes,
                                                     **list_of_new_variables_and_attributes)
        self.algorithm = None
        self.types_for_combobox = ["vector", "array", "vector_optional", "array_optional"]
        self.infoWindow = None
        self.thread = None
        self.aw_okButton.clicked.connect(self.execute_processing)
        self.aw_cancelButton.clicked.connect(self.close_window)
        self.aw_combobox_1.activated.connect(self.populate_combobox_algorithms)
        self.aw_combobox_2.activated.connect(self.load_algorithm_information)
        self.aw_combobox_2.activated.connect(self.populate_inputs)
        self.aw_combobox_2.activated.connect(self.populate_outputs)
        self.populate_combobox_category()
        logging.info('gui - algorithm_windows_functions.py - MyProcessing ready')

    def execute_processing(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - close_window_save : algorithm '
                      + self.algorithm().metadata["Processor"])
        self.thread = VariableProcessingThread(self.algorithm, self.list_combobox_input, self.list_edit_output,
                                               self.list_of_variables_and_attributes)
        self.thread.started.connect(self.wait_window)
        self.thread.finished.connect(self.close_wait_window)
        self.thread.error.connect(self.processing_error)
        self.thread.start()

    def wait_window(self):
        info_text = 'Processing data, please wait...'
        self.waitWindow = MyWait(info_text)
        self.waitWindow.exec_()

    def close_wait_window(self, val):
        self.list_of_new_variables_and_attributes = val
        self.waitWindow.close()
        self.close()

    def processing_error(self):
        self.waitWindow.close()
        info_text = ('Something went wrong during the processing. Please try to launch it again. If the process is'
                     + ' still not working, please check the algorithm and/or contact the developer.')
        self.infoWindow = MyInfo(info_text)
        self.infoWindow.exec_()
        del self.list_of_variables_and_attributes
        del self.list_of_new_variables_and_attributes
        self.close()

    def close_window(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - close_window')
        del self.list_of_variables_and_attributes
        del self.list_of_new_variables_and_attributes
        self.close()

    def populate_combobox_category(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - populate_combobox_1')
        self.aw_combobox_1.addItem("Make a choice...")
        folder_list = []
        for key, _ in self.list_of_algorithms.items():
            folder_list.append(key.title())
        folder_list = sorted(folder_list)
        self.aw_combobox_1.addItems(folder_list)

    def populate_combobox_algorithms(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - populate_combobox_2')
        self.setWindowTitle('Processing')
        self.aw_okButton.setEnabled(False)
        self.aw_combobox_2.clear()
        if self.aw_combobox_1.currentText() == "Make a choice...":
            self.aw_combobox_2.setEnabled(False)
        else:
            self.aw_combobox_2.setEnabled(True)
            self.aw_combobox_2.addItem("Make a choice...")
            algorithm_list = self.list_of_algorithms[str(self.aw_combobox_1.currentText()).lower()]
            self.aw_combobox_2.addItems(sorted(algorithm_list))

    def load_algorithm_information(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - load_algorithm_information : algorithm '
                      + str(self.aw_combobox_2.currentText()))
        self.setWindowTitle('Processing')
        self.aw_okButton.setEnabled(False)
        if self.aw_combobox_2.currentText() != "Make a choice...":
            self.setWindowTitle('Processing - ' + str(self.aw_combobox_2.currentText()))
            self.aw_edit_1.setPlainText("")
            self.aw_edit_2.setPlainText("")
            try:
                self.algorithm = getattr(getattr(egads.algorithms, str(self.aw_combobox_1.currentText()).lower()),
                                         str(self.aw_combobox_2.currentText()))
            except AttributeError:
                self.algorithm = getattr(getattr(egads.algorithms.user, str(self.aw_combobox_1.currentText()).lower()),
                                         str(self.aw_combobox_2.currentText()))
            try:
                self.aw_edit_2.setText('<p align="justify">' + str(self.algorithm().metadata["Description"]) + '</p>')
            except KeyError:
                logging.exception(
                    'gui - algorithm_window_functions.py - MyProcessing - load_algorithm_information : no description')
            try:
                self.aw_edit_1.setText('<p align="justify">' + str(self.algorithm().metadata["Purpose"]) + '</p>')
            except KeyError:
                logging.exception(
                    'gui - algorithm_window_functions.py - MyProcessing - load_algorithm_information : no purpose')

    def populate_inputs(self):
        self.clear_layout(self.input_layout)
        self.input_activate = 0
        self.list_of_inputs = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_button_input = []
        self.input_num = 0
        if self.aw_combobox_2.currentText() != "Make a choice...":
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
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            for index, item in enumerate(self.algorithm().metadata["Inputs"]):
                self.list_label_input.append(QtWidgets.QLabel())
                self.list_label_input[self.input_num].setFont(font)
                self.list_label_input[self.input_num].setText(item + ':')
                self.list_label_input[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
                self.list_label_input[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.list_label_input[self.input_num].setObjectName("list_label_input_" + str(self.input_num))
                self.list_label_input[self.input_num].setStyleSheet("QLabel {\n"
                                                                    "   color: rgb(45,45,45);\n"
                                                                    "}")
                self.list_label_input[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                   QtCore.Qt.AlignVCenter)
                self.input_layout.addWidget(self.list_label_input[self.input_num], self.input_num, 0, 1, 1)
                self.input_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                QtWidgets.QSizePolicy.Minimum), self.input_num, 1, 1, 1)
                if self.algorithm().metadata["InputTypes"][index] in self.types_for_combobox or \
                        self.algorithm().metadata["InputTypes"][index] == "time":
                    self.list_combobox_input.append(QtWidgets.QComboBox())
                    item_delegate = QtWidgets.QStyledItemDelegate()
                    self.list_combobox_input[self.input_num].setItemDelegate(item_delegate)
                    self.list_combobox_input[self.input_num].setEnabled(True)
                    self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                    self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                    self.list_combobox_input[self.input_num].setFrame(False)
                    self.list_combobox_input[self.input_num].setFont(font2)
                    self.list_combobox_input[self.input_num].setStyleSheet("QComboBox {\n"
                                                                           "    border: 1px solid #acacac;\n"
                                                                           "    border-radius: 1px;\n"
                                                                           "    padding-left: 5px;\n"
                                                                           "    background-color: qlineargradient(x1: "
                                                                           "0, y1: 0, x2: 0, y2: 1, \n"
                                                                           "                                "
                                                                           "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
                                                                           "    background-color: qlineargradient(x1: "
                                                                           "0, y1: 0, x2: 0, y2: 1, \n"
                                                                           "                                stop: 0 "
                                                                           "#ecf4fc, stop: 1 #dcecfc);\n"
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
                                                                           "    image: url(icons/down_arrow_icon.svg)"
                                                                           "; \n"
                                                                           "    width: 16px;\n"
                                                                           "    height: 16px\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox QAbstractItemView {\n"
                                                                           "    selection-background-color: rgb(200,200"
                                                                           ",200);\n"
                                                                           "    selection-color: black;\n"
                                                                           "    background: #f0f0f0;\n"
                                                                           "    border: 0px solid #f0f0f0;\n"
                                                                           "}\n"
                                                                           "\n"
                                                                           "QComboBox QAbstractItemView::item {\n"
                                                                           "    margin: 5px 5px 5px 5px;\n"
                                                                           "}")
                    self.list_combobox_input[self.input_num].setObjectName("list_combobox_input_" + str(self.input_num))
                    self.list_combobox_input[self.input_num].addItem("Make a choice...")
                    variable_list = []
                    for _, sublist in self.list_of_variables_and_attributes.items():
                        if self.algorithm().metadata["InputTypes"][index] in self.types_for_combobox:
                            if sublist[2] != 'deleted':
                                variable_list.append(sublist[1]["var_name"])
                        else:
                            if "time" in sublist[1]["var_name"]:
                                if sublist[2] != 'deleted':
                                    variable_list.append(sublist[1]["var_name"])
                    self.list_combobox_input[self.input_num].addItems(sorted(variable_list))
                    self.list_combobox_input[self.input_num].activated.connect(self.activate_save_button)
                    self.input_layout.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                else:
                    if "coeff.[" in self.algorithm().metadata["InputTypes"][index]:
                        line_edit_num = self.algorithm().metadata["InputTypes"][index][7:-1]
                        tmp = []
                        tmp_layout = QtWidgets.QHBoxLayout()
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            tmp_layout.setObjectName("optional_tmp_layout")
                        else:
                            tmp_layout.setObjectName("tmp_layout")
                        layout_factor = {2: 4, 3: 5, 4: 5, 5: 5}
                        try:
                            size = (300 / int(line_edit_num)) - layout_factor[int(line_edit_num)]
                        except KeyError:
                            size = (300 / int(line_edit_num))
                        for i in range(int(line_edit_num)):
                            tmp.append(QtWidgets.QLineEdit())
                            tmp[i].setEnabled(True)
                            tmp[i].setFrame(False)
                            tmp[i].setFont(font2)
                            tmp[i].setObjectName("multi_list_edit_input_" + str(i))
                            tmp[i].setMinimumSize(QtCore.QSize(size, 27))
                            tmp[i].setMaximumSize(QtCore.QSize(size, 27))
                            tmp[i].setStyleSheet("QLineEdit {\n"
                                                 "    border-radius: 3px;\n"
                                                 "    padding: 1px 4px 1px 4px;\n"
                                                 "    background-color:  rgb(240, 240, 240);\n"
                                                 "    color: rgb(45,45,45);\n"
                                                 "}\n")
                            tmp[i].textChanged.connect(self.activate_save_button)
                            tmp_layout.addWidget(tmp[i])
                        self.list_combobox_input.append(tmp_layout)
                        try:
                            self.input_layout.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2,
                                                        1, 1)
                        except TypeError:
                            self.input_layout.addLayout(self.list_combobox_input[self.input_num], self.input_num, 2,
                                                        1, 1)
                    else:
                        self.list_combobox_input.append(QtWidgets.QLineEdit())
                        self.list_combobox_input[self.input_num].setEnabled(True)
                        self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setFrame(False)
                        self.list_combobox_input[self.input_num].setFont(font2)
                        self.list_combobox_input[self.input_num].setStyleSheet("QLineEdit {\n"
                                                                               "    border-radius: 3px;\n"
                                                                               "    padding: 1px 4px 1px 4px;\n"
                                                                               "    background-color:  rgb(240,240,"
                                                                               "240);\n"
                                                                               "    color: rgb(45,45,45);\n"
                                                                               "}\n")
                        self.list_combobox_input[self.input_num].textChanged.connect(self.activate_save_button)
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_combobox_input[self.input_num].setObjectName("optional_list_lineedit_input_" +
                                                                                   str(self.input_num))
                        else:
                            self.list_combobox_input[self.input_num].setObjectName("list_edit_input_" +
                                                                                   str(self.input_num))
                        self.input_layout.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                self.list_button_input.append(QtWidgets.QToolButton())
                self.list_button_input[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setText("")
                self.list_button_input[self.input_num].setIcon(icon)
                self.list_button_input[self.input_num].setIconSize(QtCore.QSize(23, 23))
                self.list_button_input[self.input_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                if "optional" in self.algorithm().metadata["InputTypes"][index]:
                    self.list_button_input[self.input_num].setObjectName("optional_list_button_input_" + str(
                        self.input_num))
                else:
                    self.list_button_input[self.input_num].setObjectName("list_button_input_" + str(self.input_num))
                self.input_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                QtWidgets.QSizePolicy.Minimum), self.input_num, 3, 1, 1)
                self.list_button_input[self.input_num].setStyleSheet("QToolButton {\n"
                                                                     "    border: 1px solid transparent;\n"
                                                                     "    background-color: transparent;\n"
                                                                     "    width: 27px;\n"
                                                                     "    height: 27px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QToolButton:flat {\n"
                                                                     "    border: none;\n"
                                                                     "}")
                self.list_button_input[self.input_num].clicked.connect(self.information_button)
                self.input_layout.addWidget(self.list_button_input[self.input_num], self.input_num, 4, 1, 1)
                self.input_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum),
                    self.input_num, 5, 1, 1)
                self.input_num += 1

    def populate_outputs(self):
        self.clear_layout(self.output_layout)
        self.list_label_output = []
        self.list_edit_output = []
        self.list_button_output = []
        self.output_num = 0
        self.output_activate = 0
        self.list_of_outputs = []
        if self.aw_combobox_2.currentText() != "Make a choice...":
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
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            for item in self.algorithm().metadata["Outputs"]:
                self.list_label_output.append(QtWidgets.QLabel())
                self.list_label_output[self.output_num].setText(item + ':')
                self.list_label_output[self.output_num].setFont(font)
                self.list_label_output[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
                self.list_label_output[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.list_label_output[self.output_num].setObjectName("list_label_output_" + str(self.output_num))
                self.list_label_output[self.output_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
                self.list_label_output[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                     QtCore.Qt.AlignVCenter)
                self.output_layout.addWidget(self.list_label_output[self.output_num], self.output_num, 0, 1, 1)
                self.output_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum),
                    self.output_num, 1, 1, 1)
                self.list_edit_output.append(QtWidgets.QLineEdit())
                self.list_edit_output[self.output_num].setEnabled(True)
                self.list_edit_output[self.output_num].setFont(font2)
                self.list_edit_output[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
                self.list_edit_output[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
                self.list_edit_output[self.output_num].setFrame(False)
                self.list_edit_output[self.output_num].setStyleSheet("QLineEdit {\n"
                                                                     "  border-radius: 3px;\n"
                                                                     "  padding: 1px 4px 1px 4px;\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "  color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QLineEdit:disabled {\n"
                                                                     "  background-color: rgb(240, 240, 240);\n"
                                                                     "}")
                self.list_edit_output[self.output_num].setObjectName("list_edit_output_" + str(self.output_num))
                self.list_edit_output[self.output_num].textChanged.connect(self.activate_save_button)
                self.output_layout.addWidget(self.list_edit_output[self.output_num], self.output_num, 2, 1, 1)
                self.list_button_output.append(QtWidgets.QToolButton())
                self.list_button_output[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
                self.list_button_output[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
                self.list_button_output[self.output_num].setText("")
                self.list_button_output[self.output_num].setIcon(icon)
                self.list_button_output[self.output_num].setIconSize(QtCore.QSize(23, 23))
                self.list_button_output[self.output_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                self.list_button_output[self.output_num].setObjectName("list_button_output_" + str(self.output_num))
                self.output_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum),
                    self.output_num, 3, 1, 1)
                self.list_button_output[self.output_num].setStyleSheet("QToolButton {\n"
                                                                       "    border: 1px solid transparent;\n"
                                                                       "    background-color: transparent;\n"
                                                                       "    width: 27px;\n"
                                                                       "    height: 27px;\n"
                                                                       "}\n"
                                                                       "\n"
                                                                       "QToolButton:flat {\n"
                                                                       "    border: none;\n"
                                                                       "}")
                self.list_button_output[self.output_num].clicked.connect(self.information_button)
                self.output_layout.addWidget(self.list_button_output[self.output_num], self.output_num, 4, 1, 1)
                self.output_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum),
                    self.output_num, 5, 1, 1)
                self.output_num += 1

    def activate_save_button(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - activate_save_button')
        input_activate = 1
        for widget in self.list_combobox_input:
            try:
                if widget.currentText() == "Make a choice...":
                    input_activate = 0
            except AttributeError:
                if "optional" not in widget.objectName():
                    try:
                        if widget.text() == "":
                            input_activate = 0
                    except AttributeError:
                        subwidgets = (widget.itemAt(i) for i in range(widget.count()))
                        for subwidget in subwidgets:
                            if subwidget.widget().text() == "":
                                input_activate = 0
        output_activate = 1
        for widget in self.list_edit_output:
            if widget.text() == "":
                output_activate = 0
        if input_activate == 1 & output_activate == 1:
            self.aw_okButton.setEnabled(True)
        else:
            self.aw_okButton.setEnabled(False)
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - activate_save_button : '
                      'aw_okButton.isEnabled() ' + str(self.aw_okButton.isEnabled()))

    def information_button(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - information_button : sender().objectName() '
                      + str(self.sender().objectName()))
        if "optional" in self.sender().objectName():
            optional_str = '[Optional] '
            index = 27
        else:
            optional_str = ''
            index = 18
        if "input" in self.sender().objectName():
            description = self.algorithm().metadata["InputDescription"][int(self.sender().objectName()[index:])]
            units = self.algorithm().metadata["InputUnits"][int(self.sender().objectName()[index:])]
            if units is None:
                units = ''
            information_str = '<u>Description:</u> ' + optional_str + description + '<br><br><u>Units:</u> ' + units
        else:
            description = self.algorithm().metadata["OutputDescription"][int(self.sender().objectName()[index + 1:])]
            units = self.algorithm().metadata["OutputUnits"][int(self.sender().objectName()[index + 1:])]
            if units is None:
                units = ''
            if isinstance(self.algorithm().output_metadata, list):
                output_metadata = self.algorithm().output_metadata[int(self.sender().objectName()[index + 1:])]
            else:
                output_metadata = self.algorithm().output_metadata
            standard_name = output_metadata["standard_name"]
            long_name = output_metadata["long_name"]
            if isinstance(output_metadata["Category"], list):
                category_str = ''
                for category in output_metadata["Category"]:
                    category_str += category + ', '
                category_str = category_str[0:-2]
            else:
                category_str = output_metadata["Category"]
            information_str = '<u>Description:</u> ' + optional_str + description + '<br><br><u>Units:</u> ' + units \
                              + '<br><br><u>Standard name:</u> ' + standard_name + '<br><br><u>Long name:</u> ' + \
                              long_name + '<br><br><u>Category:</u> ' + category_str
        self.infoWindow = MyInfo(information_str)
        self.infoWindow.exec_()

    def clear_layout(self, layout):
        logging.debug('gui - gui_functions.py - clear_layout')
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QtWidgets.QLayout):
                self.clear_layout(item.layout())
            layout.removeItem(item)


class MyAlgorithm(QtWidgets.QDialog, Ui_creationWindow):
    def __init__(self, algorithm_categories, output_categories):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        algorithm_information_buttons_text(self)
        self.algorithm_categories = algorithm_categories
        self.output_categories = output_categories
        self.highlighter = Highlighter(self.cw_plain_4.document())
        self.cw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.reset_tab_title_color()
        self.cancel = True
        self.cw_okButton.clicked.connect(self.prepare_algorithm_creation)
        self.cw_cancelButton.clicked.connect(self.closeWindow)
        self.cw_add_1.clicked.connect(self.add_input)
        self.cw_add_2.clicked.connect(self.add_output)
        self.cw_combobox_1.currentIndexChanged.connect(self.add_algorithm_category)
        self.cw_info_3.clicked.connect(self.algorithm_button_info)
        self.cw_info_4.clicked.connect(self.algorithm_button_info)
        self.cw_info_5.clicked.connect(self.algorithm_button_info)
        self.cw_info_6.clicked.connect(self.algorithm_button_info)
        self.cw_info_7.clicked.connect(self.algorithm_button_info)
        self.cw_info_8.clicked.connect(self.algorithm_button_info)
        self.cw_info_9.clicked.connect(self.algorithm_button_info)
        self.cw_info_10.clicked.connect(self.algorithm_button_info)
        self.cw_label_11.setVisible(False)
        self.cw_line_5.setVisible(False)
        self.cw_info_1.setEnabled(False)
        self.cw_info_2.setEnabled(False)
        self.cw_info_1.setVisible(False)
        self.cw_info_2.setVisible(False)
        self.prepare_algorithm_categories()
        self.cw_input_vl_1 = []
        self.cw_input_hl_1 = []
        self.cw_input_gd_1 = []
        self.cw_input_lb_1 = []
        self.cw_input_lb_2 = []
        self.cw_input_lb_3 = []
        self.cw_input_lb_4 = []
        self.cw_input_lb_5 = []
        self.cw_input_ln_1 = []
        self.cw_input_ln_2 = []
        self.cw_input_ln_3 = []
        self.cw_input_ln_4 = []
        self.cw_input_bt_1 = []
        self.cw_info_bt_1 = []
        self.cw_info_bt_2 = []
        self.cw_info_bt_3 = []
        self.cw_info_bt_4 = []
        self.cw_input_del_1 = []
        self.cw_input_li_1 = []
        self.input_num = 0
        self.cw_output_vl_1 = []
        self.cw_output_vl_2 = []
        self.cw_output_vl_3 = []
        self.cw_output_hl_1 = []
        self.cw_output_hl_2 = []
        self.cw_output_hl_3 = []
        self.cw_output_hl_4 = []
        self.cw_output_hl_5 = []
        self.cw_output_hl_6 = []
        self.cw_output_hl_7 = []
        self.cw_output_hl_8 = []
        self.cw_output_hl_9 = []
        self.cw_output_gd_1 = []
        self.cw_output_lb_1 = []
        self.cw_output_lb_2 = []
        self.cw_output_lb_3 = []
        self.cw_output_lb_4 = []
        self.cw_output_lb_5 = []
        self.cw_output_lb_6 = []
        self.cw_output_lb_7 = []
        self.cw_output_ln_1 = []
        self.cw_output_ln_2 = []
        self.cw_output_ln_3 = []
        self.cw_output_ln_4 = []
        self.cw_output_ln_5 = []
        self.cw_output_ln_6 = []
        self.cw_output_cb_1 = []
        self.cw_output_lw_1 = []
        self.cw_info_bt_5 = []
        self.cw_info_bt_6 = []
        self.cw_info_bt_7 = []
        self.cw_info_bt_8 = []
        self.cw_info_bt_9 = []
        self.cw_info_bt_10 = []
        self.cw_info_bt_11 = []
        self.cw_output_del_1 = []
        self.cw_output_add_1 = []
        self.cw_output_li_1 = []
        self.output_num = 0
        self.algorithm_mandatory_fields = {self.cw_line_1: self.cw_label_3,
                                           self.cw_line_2: self.cw_label_4,
                                           self.cw_plain_1: self.cw_label_7,
                                           self.cw_plain_2: self.cw_label_8,
                                           self.cw_plain_4: self.cw_label_10}
        self.categoryWindow = None
        self.success = None
        self.algorithm_filename = None
        self.algorithm_category = None
        self.algorithm_name = None
        logging.info('gui - algorithm_windows_functions.py - MyAlgorithm -  ready')

    def add_input(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - add_input')
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/unit_validation_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_input_vl_1.append(QtWidgets.QVBoxLayout())
        self.cw_input_vl_1[self.input_num].setObjectName('cw_input_vl_1_' + str(self.input_num))
        self.cw_input_hl_1.append(QtWidgets.QHBoxLayout())
        self.cw_input_hl_1[self.input_num].setObjectName('cw_input_hl_1_' + str(self.input_num))
        self.cw_input_vl_1[self.input_num].addLayout(self.cw_input_hl_1[self.input_num])
        self.cw_input_del_1.append(QtWidgets.QToolButton())
        self.cw_input_del_1[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_input_del_1[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_input_del_1[self.input_num].setStyleSheet("QToolButton {\n"
                                                          "    border: 1px solid transparent;\n"
                                                          "    background-color: transparent;\n"
                                                          "    width: 27px;\n"
                                                          "    height: 27px;\n"
                                                          "}\n"
                                                          "\n"
                                                          "QToolButton:flat {\n"
                                                          "    border: none;\n"
                                                          "}")
        self.cw_input_del_1[self.input_num].setIcon(icon)
        self.cw_input_del_1[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_input_del_1[self.input_num].setObjectName('cw_input_del_1_' + str(self.input_num))
        self.cw_input_hl_1[self.input_num].addWidget(self.cw_input_del_1[self.input_num])
        self.cw_input_hl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.cw_input_gd_1.append(QtWidgets.QGridLayout())
        self.cw_input_gd_1[self.input_num].setObjectName('cw_input_gd_1_' + str(self.input_num))
        self.cw_input_hl_1[self.input_num].addLayout(self.cw_input_gd_1[self.input_num])
        self.cw_input_lb_1.append(QtWidgets.QLabel())
        self.cw_input_lb_1[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_1[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_1[self.input_num].setFont(font)
        self.cw_input_lb_1[self.input_num].setText('Input symbols:')
        self.cw_input_lb_1[self.input_num].setObjectName('cw_input_lb_1_' + str(self.input_num))
        self.cw_input_lb_1[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_1[self.input_num].setStyleSheet("QLabel {\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_1[self.input_num], 0, 0, 1, 1)
        self.cw_input_ln_1.append(QtWidgets.QLineEdit())
        self.cw_input_ln_1[self.input_num].setEnabled(True)
        self.cw_input_ln_1[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_1[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_1[self.input_num].setFont(font2)
        self.cw_input_ln_1[self.input_num].setStyleSheet("QLineEdit {\n"
                                                         "    border-radius: 3px;\n"
                                                         "    padding: 1px 4px 1px 4px;\n"
                                                         "    background-color: rgb(240, 240, 240);\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:disabled {\n"
                                                         "    background-color: rgb(200,200,200);\n"
                                                         "}")
        self.cw_input_ln_1[self.input_num].setText('')
        self.cw_input_ln_1[self.input_num].setFrame(False)
        self.cw_input_ln_1[self.input_num].setObjectName('cw_input_ln_1_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_1[self.input_num], 0, 1, 1, 1)
        self.cw_info_bt_1.append(QtWidgets.QToolButton())
        self.cw_info_bt_1[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_1[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_1[self.input_num].setStyleSheet("QToolButton {\n"
                                                        "    border: 1px solid transparent;\n"
                                                        "    background-color: transparent;\n"
                                                        "    width: 27px;\n"
                                                        "    height: 27px;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QToolButton:flat {\n"
                                                        "    border: none;\n"
                                                        "}")
        self.cw_info_bt_1[self.input_num].setIcon(icon2)
        self.cw_info_bt_1[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_1[self.input_num].setObjectName('cw_info_bt_1_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_1[self.input_num], 0, 2, 1, 1)
        self.cw_input_gd_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 0, 3, 1, 1)
        self.cw_input_lb_2.append(QtWidgets.QLabel())
        self.cw_input_lb_2[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_2[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_2[self.input_num].setFont(font)
        self.cw_input_lb_2[self.input_num].setText('Input units:')
        self.cw_input_lb_2[self.input_num].setObjectName('cw_input_lb_2_' + str(self.input_num))
        self.cw_input_lb_2[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_2[self.input_num].setStyleSheet("QLabel {\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_2[self.input_num], 1, 0, 1, 1)
        self.cw_input_ln_2.append(QtWidgets.QLineEdit())
        self.cw_input_ln_2[self.input_num].setEnabled(True)
        self.cw_input_ln_2[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_2[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_2[self.input_num].setFont(font2)
        self.cw_input_ln_2[self.input_num].setStyleSheet("QLineEdit {\n"
                                                         "    border-radius: 3px;\n"
                                                         "    padding: 1px 4px 1px 4px;\n"
                                                         "    background-color: rgb(240, 240, 240);\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:disabled {\n"
                                                         "    background-color: rgb(200,200,200);\n"
                                                         "}")
        self.cw_input_ln_2[self.input_num].setText('')
        self.cw_input_ln_2[self.input_num].setFrame(False)
        self.cw_input_ln_2[self.input_num].setObjectName('cw_input_ln_2_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_2[self.input_num], 1, 1, 1, 1)
        self.cw_info_bt_2.append(QtWidgets.QToolButton())
        self.cw_info_bt_2[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_2[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_2[self.input_num].setStyleSheet("QToolButton {\n"
                                                        "    border: 1px solid transparent;\n"
                                                        "    background-color: transparent;\n"
                                                        "    width: 27px;\n"
                                                        "    height: 27px;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QToolButton:flat {\n"
                                                        "    border: none;\n"
                                                        "}")
        self.cw_info_bt_2[self.input_num].setIcon(icon2)
        self.cw_info_bt_2[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_2[self.input_num].setObjectName('cw_info_bt_2_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_2[self.input_num], 1, 2, 1, 1)
        self.cw_input_gd_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 3, 1, 1)
        self.cw_input_lb_3.append(QtWidgets.QLabel())
        self.cw_input_lb_3[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_3[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_3[self.input_num].setFont(font)
        self.cw_input_lb_3[self.input_num].setText('Input type:')
        self.cw_input_lb_3[self.input_num].setObjectName('cw_input_lb_3_' + str(self.input_num))
        self.cw_input_lb_3[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_3[self.input_num].setStyleSheet("QLabel {\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_3[self.input_num], 2, 0, 1, 1)
        self.cw_input_ln_3.append(QtWidgets.QLineEdit())
        self.cw_input_ln_3[self.input_num].setEnabled(True)
        self.cw_input_ln_3[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_3[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_3[self.input_num].setFont(font2)
        self.cw_input_ln_3[self.input_num].setStyleSheet("QLineEdit {\n"
                                                         "    border-radius: 3px;\n"
                                                         "    padding: 1px 4px 1px 4px;\n"
                                                         "    background-color: rgb(240, 240, 240);\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:disabled {\n"
                                                         "    background-color: rgb(200,200,200);\n"
                                                         "}")
        self.cw_input_ln_3[self.input_num].setText('')
        self.cw_input_ln_3[self.input_num].setFrame(False)
        self.cw_input_ln_3[self.input_num].setObjectName('cw_input_ln_3_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_3[self.input_num], 2, 1, 1, 1)
        self.cw_info_bt_3.append(QtWidgets.QToolButton())
        self.cw_info_bt_3[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_3[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_3[self.input_num].setStyleSheet("QToolButton {\n"
                                                        "    border: 1px solid transparent;\n"
                                                        "    background-color: transparent;\n"
                                                        "    width: 27px;\n"
                                                        "    height: 27px;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QToolButton:flat {\n"
                                                        "    border: none;\n"
                                                        "}")
        self.cw_info_bt_3[self.input_num].setIcon(icon2)
        self.cw_info_bt_3[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_3[self.input_num].setObjectName('cw_info_bt_3_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_3[self.input_num], 2, 2, 1, 1)
        self.cw_input_gd_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 2, 3, 1, 1)
        self.cw_input_lb_4.append(QtWidgets.QLabel())
        self.cw_input_lb_4[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_4[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_4[self.input_num].setFont(font)
        self.cw_input_lb_4[self.input_num].setText('Input description:')
        self.cw_input_lb_4[self.input_num].setObjectName('cw_input_lb_4_' + str(self.input_num))
        self.cw_input_lb_4[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_4[self.input_num].setStyleSheet("QLabel {\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}")
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_4[self.input_num], 3, 0, 1, 1)
        self.cw_input_ln_4.append(QtWidgets.QLineEdit())
        self.cw_input_ln_4[self.input_num].setEnabled(True)
        self.cw_input_ln_4[self.input_num].setMinimumSize(QtCore.QSize(500, 27))
        self.cw_input_ln_4[self.input_num].setMaximumSize(QtCore.QSize(500, 27))
        self.cw_input_ln_4[self.input_num].setFont(font2)
        self.cw_input_ln_4[self.input_num].setStyleSheet("QLineEdit {\n"
                                                         "    border-radius: 3px;\n"
                                                         "    padding: 1px 4px 1px 4px;\n"
                                                         "    background-color: rgb(240, 240, 240);\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:disabled {\n"
                                                         "    background-color: rgb(200,200,200);\n"
                                                         "}")
        self.cw_input_ln_4[self.input_num].setText('')
        self.cw_input_ln_4[self.input_num].setFrame(False)
        self.cw_input_ln_4[self.input_num].setObjectName('cw_input_ln_4_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_4[self.input_num], 3, 1, 1, 3)
        self.cw_info_bt_4.append(QtWidgets.QToolButton())
        self.cw_info_bt_4[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_4[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_4[self.input_num].setStyleSheet("QToolButton {\n"
                                                        "    border: 1px solid transparent;\n"
                                                        "    background-color: transparent;\n"
                                                        "    width: 27px;\n"
                                                        "    height: 27px;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QToolButton:flat {\n"
                                                        "    border: none;\n"
                                                        "}")
        self.cw_info_bt_4[self.input_num].setIcon(icon2)
        self.cw_info_bt_4[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_4[self.input_num].setObjectName('cw_info_bt_4_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_info_bt_4[self.input_num], 3, 4, 1, 1)
        self.cw_input_hl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.cw_input_vl.addLayout(self.cw_input_vl_1[self.input_num])
        self.cw_input_vl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_input_li_1.append(QtWidgets.QFrame())
        self.cw_input_li_1[self.input_num].setFrameShape(QtWidgets.QFrame.HLine)
        self.cw_input_li_1[self.input_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cw_input_li_1[self.input_num].setObjectName("cw_input_li_1_" + str(self.input_num))
        self.cw_input_li_1[self.input_num].setStyleSheet("QFrame {\n"
                                                         "    background: rgb(190,190,190);\n"
                                                         "    height: 5px;\n"
                                                         "    border: 0px solid black;\n"
                                                         "}")
        self.cw_input_vl_1[self.input_num].addWidget(self.cw_input_li_1[self.input_num])
        self.cw_input_vl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_input_del_1[self.input_num].clicked.connect(self.del_input)
        self.cw_info_bt_1[self.input_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_2[self.input_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_3[self.input_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_4[self.input_num].clicked.connect(self.input_output_button_info)
        self.input_num += 1

    def del_input(self, index=None):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - del_input : index ' + str(index)
                      + ', sender().objectName() ' + str(self.sender().objectName()))
        if index is None:
            index = int(self.sender().objectName()[15:])
        self.cw_input_vl_1[index].deleteLater()
        self.cw_input_vl_1.pop(index)
        self.cw_input_li_1[index].deleteLater()
        self.cw_input_li_1.pop(index)
        self.cw_input_hl_1[index].deleteLater()
        self.cw_input_hl_1.pop(index)
        self.cw_input_del_1[index].deleteLater()
        self.cw_input_del_1.pop(index)
        self.cw_input_gd_1[index].deleteLater()
        self.cw_input_gd_1.pop(index)
        self.cw_input_lb_1[index].deleteLater()
        self.cw_input_lb_1.pop(index)
        self.cw_input_ln_1[index].deleteLater()
        self.cw_input_ln_1.pop(index)
        self.cw_info_bt_1[index].deleteLater()
        self.cw_info_bt_1.pop(index)
        self.cw_input_lb_2[index].deleteLater()
        self.cw_input_lb_2.pop(index)
        self.cw_input_ln_2[index].deleteLater()
        self.cw_input_ln_2.pop(index)
        self.cw_info_bt_2[index].deleteLater()
        self.cw_info_bt_2.pop(index)
        self.cw_input_lb_3[index].deleteLater()
        self.cw_input_lb_3.pop(index)
        self.cw_input_ln_3[index].deleteLater()
        self.cw_input_ln_3.pop(index)
        self.cw_info_bt_3[index].deleteLater()
        self.cw_info_bt_3.pop(index)
        self.cw_input_lb_4[index].deleteLater()
        self.cw_input_lb_4.pop(index)
        self.cw_input_ln_4[index].deleteLater()
        self.cw_input_ln_4.pop(index)
        self.cw_info_bt_4[index].deleteLater()
        self.cw_info_bt_4.pop(index)
        self.input_num -= 1
        if len(self.cw_input_vl_1) > 0:
            for i in range(0, len(self.cw_input_vl_1)):
                self.cw_input_vl_1[i].setObjectName('cw_input_vl_1_' + str(i))
                self.cw_input_li_1[i].setObjectName("cw_input_li_1_" + str(i))
                self.cw_input_hl_1[i].setObjectName('cw_input_hl_1_' + str(i))
                self.cw_input_del_1[i].setObjectName('cw_input_del_1_' + str(i))
                self.cw_input_gd_1[i].setObjectName('cw_input_gd_1_' + str(i))
                self.cw_input_lb_1[i].setObjectName('cw_input_lb_1_' + str(i))
                self.cw_input_ln_1[i].setObjectName('cw_input_ln_1_' + str(i))
                self.cw_info_bt_1[i].setObjectName('cw_info_bt_1_' + str(i))
                self.cw_input_lb_2[i].setObjectName('cw_input_lb_2_' + str(i))
                self.cw_input_ln_2[i].setObjectName('cw_input_ln_2_' + str(i))
                self.cw_info_bt_2[i].setObjectName('cw_info_bt_2_' + str(i))
                self.cw_input_lb_3[i].setObjectName('cw_input_lb_3_' + str(i))
                self.cw_input_ln_3[i].setObjectName('cw_input_ln_3_' + str(i))
                self.cw_info_bt_3[i].setObjectName('cw_info_bt_3_' + str(i))
                self.cw_input_lb_4[i].setObjectName('cw_input_lb_4_' + str(i))
                self.cw_input_ln_4[i].setObjectName('cw_input_ln_4_' + str(i))
                self.cw_info_bt_4[i].setObjectName('cw_info_bt_4_' + str(i))

    def add_output(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - add_output')
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_output_vl_3.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_3[self.output_num].setObjectName('cw_output_vl_3_' + str(self.output_num))
        self.cw_output_hl_9.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_9[self.output_num].setObjectName('cw_output_hl_9_' + str(self.output_num))
        self.cw_output_del_1.append(QtWidgets.QToolButton())
        self.cw_output_del_1[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_output_del_1[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_output_del_1[self.output_num].setStyleSheet("QToolButton {\n"
                                                            "    border: 1px solid transparent;\n"
                                                            "    background-color: transparent;\n"
                                                            "    width: 27px;\n"
                                                            "    height: 27px;\n"
                                                            "}\n"
                                                            "\n"
                                                            "QToolButton:flat {\n"
                                                            "    border: none;\n"
                                                            "}")
        self.cw_output_del_1[self.output_num].setIcon(icon)
        self.cw_output_del_1[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_output_del_1[self.output_num].setObjectName('cw_output_del_1_' + str(self.output_num))
        self.cw_output_hl_9[self.output_num].addWidget(self.cw_output_del_1[self.output_num])
        self.cw_output_hl_9[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1.append(QtWidgets.QGridLayout())
        self.cw_output_gd_1[self.output_num].setContentsMargins(0, 0, 0, 0)
        self.cw_output_gd_1[self.output_num].setObjectName("cw_output_gd_1_" + str(self.output_num))
        self.cw_output_lb_1.append(QtWidgets.QLabel())
        self.cw_output_lb_1[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_1[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_1[self.output_num].setFont(font)
        self.cw_output_lb_1[self.output_num].setStyleSheet("QLabel {\n"
                                                           "    color: rgb(45,45,45);\n"
                                                           "}")
        self.cw_output_lb_1[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_1[self.output_num].setObjectName("cw_output_lb_1_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_1[self.output_num], 0, 0, 1, 1)
        self.cw_output_hl_1.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_1[self.output_num].setObjectName("cw_output_hl_1_" + str(self.output_num))
        self.cw_output_ln_1.append(QtWidgets.QLineEdit())
        self.cw_output_ln_1[self.output_num].setEnabled(True)
        self.cw_output_ln_1[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_1[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_1[self.output_num].setFont(font2)
        self.cw_output_ln_1[self.output_num].setStyleSheet("QLineEdit {\n"
                                                           "   border-radius: 3px;\n"
                                                           "   padding: 1px 4px 1px 4px;\n"
                                                           "   background-color: rgb(240, 240, 240);\n"
                                                           "   color: rgb(45,45,45);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QLineEdit:disabled {\n"
                                                           "   background-color: rgb(200,200,200);\n"
                                                           "}")
        self.cw_output_ln_1[self.output_num].setText("")
        self.cw_output_ln_1[self.output_num].setFrame(False)
        self.cw_output_ln_1[self.output_num].setObjectName("cw_output_ln_1_" + str(self.output_num))
        self.cw_output_hl_1[self.output_num].addWidget(self.cw_output_ln_1[self.output_num])
        self.cw_info_bt_5.append(QtWidgets.QToolButton())
        self.cw_info_bt_5[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_5[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_5[self.output_num].setStyleSheet("QToolButton {\n"
                                                         "    border: 1px solid transparent;\n"
                                                         "    background-color: transparent;\n"
                                                         "    width: 27px;\n"
                                                         "    height: 27px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QToolButton:flat {\n"
                                                         "    border: none;\n"
                                                         "}")
        self.cw_info_bt_5[self.output_num].setIcon(icon2)
        self.cw_info_bt_5[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_5[self.output_num].setObjectName("cw_info_bt_5_" + str(self.output_num))
        self.cw_output_hl_1[self.output_num].addWidget(self.cw_info_bt_5[self.output_num])
        self.cw_output_hl_1[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_1[self.output_num], 0, 1, 1, 1)
        self.cw_output_lb_5.append(QtWidgets.QLabel())
        self.cw_output_lb_5[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_5[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_5[self.output_num].setFont(font)
        self.cw_output_lb_5[self.output_num].setStyleSheet("QLabel {\n"
                                                           "    color: rgb(45,45,45);\n"
                                                           "}")
        self.cw_output_lb_5[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                          QtCore.Qt.AlignVCenter)
        self.cw_output_lb_5[self.output_num].setObjectName("cw_output_lb_5_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_5[self.output_num], 0, 2, 1, 1)
        self.cw_output_hl_5.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_5[self.output_num].setObjectName("cw_output_hl_5_" + str(self.output_num))
        self.cw_output_ln_5.append(QtWidgets.QLineEdit())
        self.cw_output_ln_5[self.output_num].setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cw_output_ln_5[self.output_num].sizePolicy().hasHeightForWidth())
        self.cw_output_ln_5[self.output_num].setSizePolicy(sizePolicy)
        self.cw_output_ln_5[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_5[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_ln_5[self.output_num].setFont(font2)
        self.cw_output_ln_5[self.output_num].setStyleSheet("QLineEdit {\n"
                                                           "   border-radius: 3px;\n"
                                                           "   padding: 1px 4px 1px 4px;\n"
                                                           "   background-color: rgb(240, 240, 240);\n"
                                                           "   color: rgb(45,45,45);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QLineEdit:disabled {\n"
                                                           "   background-color: rgb(200,200,200);\n"
                                                           "}")
        self.cw_output_ln_5[self.output_num].setText("")
        self.cw_output_ln_5[self.output_num].setFrame(False)
        self.cw_output_ln_5[self.output_num].setObjectName("cw_output_ln_5_" + str(self.output_num))
        self.cw_output_hl_5[self.output_num].addWidget(self.cw_output_ln_5[self.output_num])
        self.cw_info_bt_9.append(QtWidgets.QToolButton())
        self.cw_info_bt_9[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_9[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_9[self.output_num].setStyleSheet("QToolButton {\n"
                                                         "    border: 1px solid transparent;\n"
                                                         "    background-color: transparent;\n"
                                                         "    width: 27px;\n"
                                                         "    height: 27px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QToolButton:flat {\n"
                                                         "    border: none;\n"
                                                         "}")
        self.cw_info_bt_9[self.output_num].setIcon(icon2)
        self.cw_info_bt_9[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_9[self.output_num].setObjectName("cw_info_bt_9_" + str(self.output_num))
        self.cw_output_hl_5[self.output_num].addWidget(self.cw_info_bt_9[self.output_num])
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_5[self.output_num], 0, 3, 1, 1)
        self.cw_output_lb_2.append(QtWidgets.QLabel())
        self.cw_output_lb_2[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_2[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_2[self.output_num].setFont(font)
        self.cw_output_lb_2[self.output_num].setStyleSheet("QLabel {\n"
                                                           "    color: rgb(45,45,45);\n"
                                                           "}")
        self.cw_output_lb_2[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_2[self.output_num].setObjectName("cw_output_lb_2_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_2[self.output_num], 1, 0, 1, 1)
        self.cw_output_hl_2.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_2[self.output_num].setObjectName("cw_output_hl_2_" + str(self.output_num))
        self.cw_output_ln_2.append(QtWidgets.QLineEdit())
        self.cw_output_ln_2[self.output_num].setEnabled(True)
        self.cw_output_ln_2[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_2[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_2[self.output_num].setFont(font2)
        self.cw_output_ln_2[self.output_num].setStyleSheet("QLineEdit {\n"
                                                           "   border-radius: 3px;\n"
                                                           "   padding: 1px 4px 1px 4px;\n"
                                                           "   background-color: rgb(240, 240, 240);\n"
                                                           "   color: rgb(45,45,45);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QLineEdit:disabled {\n"
                                                           "   background-color: rgb(200,200,200);\n"
                                                           "}")
        self.cw_output_ln_2[self.output_num].setText("")
        self.cw_output_ln_2[self.output_num].setFrame(False)
        self.cw_output_ln_2[self.output_num].setObjectName("cw_output_ln_2_" + str(self.output_num))
        self.cw_output_hl_2[self.output_num].addWidget(self.cw_output_ln_2[self.output_num])
        self.cw_info_bt_6.append(QtWidgets.QToolButton())
        self.cw_info_bt_6[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_6[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_6[self.output_num].setStyleSheet("QToolButton {\n"
                                                         "    border: 1px solid transparent;\n"
                                                         "    background-color: transparent;\n"
                                                         "    width: 27px;\n"
                                                         "    height: 27px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QToolButton:flat {\n"
                                                         "    border: none;\n"
                                                         "}")
        self.cw_info_bt_6[self.output_num].setIcon(icon2)
        self.cw_info_bt_6[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_6[self.output_num].setObjectName("cw_info_bt_6_" + str(self.output_num))
        self.cw_output_hl_2[self.output_num].addWidget(self.cw_info_bt_6[self.output_num])
        self.cw_output_hl_2[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_2[self.output_num], 1, 1, 1, 1)
        self.cw_output_lb_6.append(QtWidgets.QLabel())
        self.cw_output_lb_6[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_6[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_6[self.output_num].setFont(font)
        self.cw_output_lb_6[self.output_num].setStyleSheet("QLabel {\n"
                                                           "    color: rgb(45,45,45);\n"
                                                           "}")
        self.cw_output_lb_6[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_6[self.output_num].setObjectName("cw_output_lb_6_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_6[self.output_num], 1, 2, 1, 1)
        self.cw_output_hl_6.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_6[self.output_num].setObjectName("cw_output_hl_6_" + str(self.output_num))
        self.cw_output_ln_6.append(QtWidgets.QLineEdit())
        self.cw_output_ln_6[self.output_num].setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cw_output_ln_6[self.output_num].sizePolicy().hasHeightForWidth())
        self.cw_output_ln_6[self.output_num].setSizePolicy(sizePolicy)
        self.cw_output_ln_6[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_6[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_ln_6[self.output_num].setFont(font2)
        self.cw_output_ln_6[self.output_num].setStyleSheet("QLineEdit {\n"
                                                           "   border-radius: 3px;\n"
                                                           "   padding: 1px 4px 1px 4px;\n"
                                                           "   background-color: rgb(240, 240, 240);\n"
                                                           "   color: rgb(45,45,45);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QLineEdit:disabled {\n"
                                                           "   background-color: rgb(200,200,200);\n"
                                                           "}")
        self.cw_output_ln_6[self.output_num].setText("")
        self.cw_output_ln_6[self.output_num].setFrame(False)
        self.cw_output_ln_6[self.output_num].setObjectName("cw_output_ln_6_" + str(self.output_num))
        self.cw_output_hl_6[self.output_num].addWidget(self.cw_output_ln_6[self.output_num])
        self.cw_info_bt_10.append(QtWidgets.QToolButton())
        self.cw_info_bt_10[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_10[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_10[self.output_num].setStyleSheet("QToolButton {\n"
                                                          "    border: 1px solid transparent;\n"
                                                          "    background-color: transparent;\n"
                                                          "    width: 27px;\n"
                                                          "    height: 27px;\n"
                                                          "}\n"
                                                          "\n"
                                                          "QToolButton:flat {\n"
                                                          "    border: none;\n"
                                                          "}")
        self.cw_info_bt_10[self.output_num].setIcon(icon2)
        self.cw_info_bt_10[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_10[self.output_num].setObjectName("cw_info_bt_10_" + str(self.output_num))
        self.cw_output_hl_6[self.output_num].addWidget(self.cw_info_bt_10[self.output_num])
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_6[self.output_num], 1, 3, 1, 1)
        self.cw_output_lb_3.append(QtWidgets.QLabel())
        self.cw_output_lb_3[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_3[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_3[self.output_num].setFont(font)
        self.cw_output_lb_3[self.output_num].setStyleSheet("QLabel {\n"
                                                           "    color: rgb(45,45,45);\n"
                                                           "}")
        self.cw_output_lb_3[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_3[self.output_num].setObjectName("cw_output_lb_3_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_3[self.output_num], 2, 0, 1, 1)
        self.cw_output_hl_3.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_3[self.output_num].setObjectName("cw_output_hl_3_" + str(self.output_num))
        self.cw_output_ln_3.append(QtWidgets.QLineEdit())
        self.cw_output_ln_3[self.output_num].setEnabled(True)
        self.cw_output_ln_3[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_3[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_3[self.output_num].setFont(font2)
        self.cw_output_ln_3[self.output_num].setStyleSheet("QLineEdit {\n"
                                                           "   border-radius: 3px;\n"
                                                           "   padding: 1px 4px 1px 4px;\n"
                                                           "   background-color: rgb(240, 240, 240);\n"
                                                           "   color: rgb(45,45,45);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QLineEdit:disabled {\n"
                                                           "   background-color: rgb(200,200,200);\n"
                                                           "}")
        self.cw_output_ln_3[self.output_num].setText("")
        self.cw_output_ln_3[self.output_num].setFrame(False)
        self.cw_output_ln_3[self.output_num].setObjectName("cw_output_ln_3_" + str(self.output_num))
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_output_ln_3[self.output_num])
        self.cw_info_bt_7.append(QtWidgets.QToolButton())
        self.cw_info_bt_7[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_7[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_7[self.output_num].setStyleSheet("QToolButton {\n"
                                                         "    border: 1px solid transparent;\n"
                                                         "    background-color: transparent;\n"
                                                         "    width: 27px;\n"
                                                         "    height: 27px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QToolButton:flat {\n"
                                                         "    border: none;\n"
                                                         "}")
        self.cw_info_bt_7[self.output_num].setIcon(icon2)
        self.cw_info_bt_7[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_7[self.output_num].setObjectName("cw_info_bt_7_" + str(self.output_num))
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_info_bt_7[self.output_num])
        self.cw_output_hl_3[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_3[self.output_num], 2, 1, 1, 3)
        self.cw_output_lb_4.append(QtWidgets.QLabel())
        self.cw_output_lb_4[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_4[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_4[self.output_num].setFont(font)
        self.cw_output_lb_4[self.output_num].setStyleSheet("QLabel {\n"
                                                           "    color: rgb(45,45,45);\n"
                                                           "}")
        self.cw_output_lb_4[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_4[self.output_num].setObjectName("cw_output_lb_4_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_4[self.output_num], 3, 0, 1, 1)
        self.cw_output_hl_4.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_4[self.output_num].setObjectName("cw_output_hl_4_" + str(self.output_num))
        self.cw_output_ln_4.append(QtWidgets.QLineEdit())
        self.cw_output_ln_4[self.output_num].setEnabled(True)
        self.cw_output_ln_4[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_4[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_ln_4[self.output_num].setFont(font2)
        self.cw_output_ln_4[self.output_num].setStyleSheet("QLineEdit {\n"
                                                           "   border-radius: 3px;\n"
                                                           "   padding: 1px 4px 1px 4px;\n"
                                                           "   background-color: rgb(240, 240, 240);\n"
                                                           "   color: rgb(45,45,45);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QLineEdit:disabled {\n"
                                                           "   background-color: rgb(200,200,200);\n"
                                                           "}")
        self.cw_output_ln_4[self.output_num].setText("")
        self.cw_output_ln_4[self.output_num].setFrame(False)
        self.cw_output_ln_4[self.output_num].setObjectName("cw_output_ln_4_" + str(self.output_num))
        self.cw_output_hl_4[self.output_num].addWidget(self.cw_output_ln_4[self.output_num])
        self.cw_info_bt_8.append(QtWidgets.QToolButton())
        self.cw_info_bt_8[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_8[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_8[self.output_num].setStyleSheet("QToolButton {\n"
                                                         "    border: 1px solid transparent;\n"
                                                         "    background-color: transparent;\n"
                                                         "    width: 27px;\n"
                                                         "    height: 27px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QToolButton:flat {\n"
                                                         "    border: none;\n"
                                                         "}")
        self.cw_info_bt_8[self.output_num].setIcon(icon2)
        self.cw_info_bt_8[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_8[self.output_num].setObjectName("cw_info_bt_8_" + str(self.output_num))
        self.cw_output_hl_4[self.output_num].addWidget(self.cw_info_bt_8[self.output_num])
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_4[self.output_num], 3, 1, 1, 3)
        self.cw_output_lb_7.append(QtWidgets.QLabel())
        self.cw_output_lb_7[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_7[self.output_num].setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cw_output_lb_7[self.output_num].setFont(font)
        self.cw_output_lb_7[self.output_num].setStyleSheet("QLabel {\n"
                                                           "    color: rgb(45,45,45);\n"
                                                           "}")
        self.cw_output_lb_7[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_7[self.output_num].setObjectName("cw_output_lb_7_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_7[self.output_num], 4, 0, 1, 1)
        self.cw_output_hl_8.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_8[self.output_num].setObjectName("cw_output_hl_8_" + str(self.output_num))
        self.cw_output_vl_1.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_1[self.output_num].setObjectName("cw_output_vl_1_" + str(self.output_num))
        self.cw_output_hl_7.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_7[self.output_num].setObjectName("cw_output_hl_7_" + str(self.output_num))
        self.cw_output_cb_1.append(QtWidgets.QComboBox())
        self.cw_output_cb_1[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_cb_1[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_cb_1[self.output_num].setFont(font2)
        self.cw_output_cb_1[self.output_num].setStyleSheet("QComboBox {\n"
                                                           "    border: 1px solid #acacac;\n"
                                                           "    border-radius: 1px;\n"
                                                           "    padding-left: 5px;\n"
                                                           "    background-color: qlineargradient(x1: 0, y1: 0, "
                                                           "x2: 0, y2: 1, \n"
                                                           "                                stop: 0 #f0f0f0, "
                                                           "stop: 1 #e5e5e5);\n"
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
                                                           "    background-color: qlineargradient(x1: 0, y1: 0, "
                                                           "x2: 0, y2: 1, \n"
                                                           "                                stop: 0 #ecf4fc, "
                                                           "stop: 1 #dcecfc);\n"
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
        self.cw_output_cb_1[self.output_num].setFrame(False)
        self.cw_output_cb_1[self.output_num].setObjectName("cw_output_cb_1_" + str(self.output_num))
        self.cw_output_cb_1[self.output_num].addItems(['Make a choice...', 'Other...'] + self.output_categories)
        self.cw_output_cb_1[self.output_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.cw_output_hl_7[self.output_num].addWidget(self.cw_output_cb_1[self.output_num])
        self.cw_output_add_1.append(QtWidgets.QToolButton())
        self.cw_output_add_1[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_output_add_1[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_output_add_1[self.output_num].setStyleSheet("QToolButton {\n"
                                                            "    border: 1px solid transparent;\n"
                                                            "    background-color: transparent;\n"
                                                            "    width: 27px;\n"
                                                            "    height: 27px;\n"
                                                            "}\n"
                                                            "\n"
                                                            "QToolButton:flat {\n"
                                                            "    border: none;\n"
                                                            "}")
        self.cw_output_add_1[self.output_num].setIcon(icon3)
        self.cw_output_add_1[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_output_add_1[self.output_num].setObjectName("cw_output_add_1_" + str(self.output_num))
        self.cw_output_hl_7[self.output_num].addWidget(self.cw_output_add_1[self.output_num])
        self.cw_output_vl_1[self.output_num].addLayout(self.cw_output_hl_7[self.output_num])
        self.cw_output_vl_1[self.output_num].addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Expanding))
        self.cw_output_hl_8[self.output_num].addLayout(self.cw_output_vl_1[self.output_num])
        self.cw_output_lw_1.append(QtWidgets.QListWidget())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cw_output_lw_1[self.output_num].sizePolicy().hasHeightForWidth())
        self.cw_output_lw_1[self.output_num].setSizePolicy(sizePolicy)
        self.cw_output_lw_1[self.output_num].setMinimumSize(QtCore.QSize(250, 100))
        self.cw_output_lw_1[self.output_num].setMaximumSize(QtCore.QSize(250, 100))
        self.cw_output_lw_1[self.output_num].setFont(font2)
        self.cw_output_lw_1[self.output_num].setFocusPolicy(QtCore.Qt.NoFocus)
        self.cw_output_lw_1[self.output_num].setStyleSheet("QListWidget {\n"
                                                           "    border-radius: 3px;\n"
                                                           "    background-color:  rgb(240, 240, 240);\n"
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
        self.cw_output_lw_1[self.output_num].setObjectName("cw_output_lw_1_" + str(self.output_num))
        self.cw_output_hl_8[self.output_num].addWidget(self.cw_output_lw_1[self.output_num])
        self.cw_output_vl_2.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_2[self.output_num].setObjectName("cw_output_vl_2_" + str(self.output_num))
        self.cw_info_bt_11.append(QtWidgets.QToolButton())
        self.cw_info_bt_11[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_11[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_11[self.output_num].setStyleSheet("QToolButton {\n"
                                                          "    border: 1px solid transparent;\n"
                                                          "    background-color: transparent;\n"
                                                          "    width: 27px;\n"
                                                          "    height: 27px;\n"
                                                          "}\n"
                                                          "\n"
                                                          "QToolButton:flat {\n"
                                                          "    border: none;\n"
                                                          "}")
        self.cw_info_bt_11[self.output_num].setIcon(icon2)
        self.cw_info_bt_11[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_11[self.output_num].setObjectName("cw_info_bt_11_" + str(self.output_num))
        self.cw_output_vl_2[self.output_num].addWidget(self.cw_info_bt_11[self.output_num])
        self.cw_output_vl_2[self.output_num].addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Expanding))
        self.cw_output_hl_8[self.output_num].addLayout(self.cw_output_vl_2[self.output_num])
        self.cw_output_hl_8[self.output_num].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_8[self.output_num], 4, 1, 1, 3)
        self.cw_output_hl_9[self.output_num].addLayout(self.cw_output_gd_1[self.output_num])
        self.cw_output_vl_3[self.output_num].addLayout(self.cw_output_hl_9[self.output_num])
        self.cw_output_vl_3[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Fixed))
        self.cw_output_li_1.append(QtWidgets.QFrame())
        self.cw_output_li_1[self.output_num].setFrameShape(QtWidgets.QFrame.HLine)
        self.cw_output_li_1[self.output_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cw_output_li_1[self.output_num].setStyleSheet("QFrame {\n"
                                                           "    background: rgb(190,190,190);\n"
                                                           "    height: 5px;\n"
                                                           "    border: 0px solid black;\n"
                                                           "}")
        self.cw_output_li_1[self.output_num].setObjectName("cw_output_li_1_" + str(self.output_num))
        self.cw_output_vl_3[self.output_num].addWidget(self.cw_output_li_1[self.output_num])
        self.cw_output_vl_3[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Fixed))
        self.cw_output_vl.addLayout(self.cw_output_vl_3[self.output_num])
        self.cw_output_lb_1[self.output_num].setText("Output symbol:")
        self.cw_output_lb_5[self.output_num].setText("Output standard name:")
        self.cw_output_lb_2[self.output_num].setText("Output units:")
        self.cw_output_lb_6[self.output_num].setText("Output long name:")
        self.cw_output_lb_3[self.output_num].setText("Output type:")
        self.cw_output_lb_4[self.output_num].setText("Output description:")
        self.cw_output_lb_7[self.output_num].setText("Output category:")
        self.cw_output_del_1[self.output_num].clicked.connect(self.del_output)
        self.cw_output_add_1[self.output_num].clicked.connect(self.add_output_category)
        self.cw_output_lw_1[self.output_num].itemDoubleClicked.connect(self.remove_output_category)

        self.cw_info_bt_5[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_6[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_7[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_8[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_9[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_10[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_11[self.output_num].clicked.connect(self.input_output_button_info)

        self.output_num += 1

    def del_output(self, index=None):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - del_output : index ' + str(index)
                      + ', sender().objectName() ' + str(self.sender().objectName()))
        if index is None:
            index = int(self.sender().objectName()[16:])
        self.cw_output_vl_1[index].deleteLater()
        self.cw_output_vl_1.pop(index)
        self.cw_output_vl_2[index].deleteLater()
        self.cw_output_vl_2.pop(index)
        self.cw_output_vl_3[index].deleteLater()
        self.cw_output_vl_3.pop(index)
        self.cw_output_hl_1[index].deleteLater()
        self.cw_output_hl_1.pop(index)
        self.cw_output_hl_2[index].deleteLater()
        self.cw_output_hl_2.pop(index)
        self.cw_output_hl_3[index].deleteLater()
        self.cw_output_hl_3.pop(index)
        self.cw_output_hl_4[index].deleteLater()
        self.cw_output_hl_4.pop(index)
        self.cw_output_hl_5[index].deleteLater()
        self.cw_output_hl_5.pop(index)
        self.cw_output_hl_6[index].deleteLater()
        self.cw_output_hl_6.pop(index)
        self.cw_output_hl_7[index].deleteLater()
        self.cw_output_hl_7.pop(index)
        self.cw_output_hl_8[index].deleteLater()
        self.cw_output_hl_8.pop(index)
        self.cw_output_hl_9[index].deleteLater()
        self.cw_output_hl_9.pop(index)
        self.cw_output_gd_1[index].deleteLater()
        self.cw_output_gd_1.pop(index)
        self.cw_output_lb_1[index].deleteLater()
        self.cw_output_lb_1.pop(index)
        self.cw_output_lb_2[index].deleteLater()
        self.cw_output_lb_2.pop(index)
        self.cw_output_lb_3[index].deleteLater()
        self.cw_output_lb_3.pop(index)
        self.cw_output_lb_4[index].deleteLater()
        self.cw_output_lb_4.pop(index)
        self.cw_output_lb_5[index].deleteLater()
        self.cw_output_lb_5.pop(index)
        self.cw_output_lb_6[index].deleteLater()
        self.cw_output_lb_6.pop(index)
        self.cw_output_lb_7[index].deleteLater()
        self.cw_output_lb_7.pop(index)
        self.cw_output_ln_1[index].deleteLater()
        self.cw_output_ln_1.pop(index)
        self.cw_output_ln_2[index].deleteLater()
        self.cw_output_ln_2.pop(index)
        self.cw_output_ln_3[index].deleteLater()
        self.cw_output_ln_3.pop(index)
        self.cw_output_ln_4[index].deleteLater()
        self.cw_output_ln_4.pop(index)
        self.cw_output_ln_5[index].deleteLater()
        self.cw_output_ln_5.pop(index)
        self.cw_output_ln_6[index].deleteLater()
        self.cw_output_ln_6.pop(index)
        self.cw_output_cb_1[index].deleteLater()
        self.cw_output_cb_1.pop(index)
        self.cw_output_lw_1[index].deleteLater()
        self.cw_output_lw_1.pop(index)
        self.cw_info_bt_5[index].deleteLater()
        self.cw_info_bt_5.pop(index)
        self.cw_info_bt_6[index].deleteLater()
        self.cw_info_bt_6.pop(index)
        self.cw_info_bt_7[index].deleteLater()
        self.cw_info_bt_7.pop(index)
        self.cw_info_bt_8[index].deleteLater()
        self.cw_info_bt_8.pop(index)
        self.cw_info_bt_9[index].deleteLater()
        self.cw_info_bt_9.pop(index)
        self.cw_info_bt_10[index].deleteLater()
        self.cw_info_bt_10.pop(index)
        self.cw_info_bt_11[index].deleteLater()
        self.cw_info_bt_11.pop(index)
        self.cw_output_del_1[index].deleteLater()
        self.cw_output_del_1.pop(index)
        self.cw_output_add_1[index].deleteLater()
        self.cw_output_add_1.pop(index)
        self.cw_output_li_1[index].deleteLater()
        self.cw_output_li_1.pop(index)
        self.output_num -= 1
        if len(self.cw_output_vl_1) > 0:
            for i in range(0, len(self.cw_output_vl_1)):
                self.cw_output_hl_9[i].setObjectName('cw_output_hl_9_' + str(i))
                self.cw_output_vl_1[i].setObjectName('cw_output_vl_1_' + str(i))
                self.cw_output_hl_1[i].setObjectName('cw_output_hl_1_' + str(i))
                self.cw_output_del_1[i].setObjectName('cw_output_del_1_' + str(i))
                self.cw_output_vl_2[i].setObjectName('cw_output_vl_2_' + str(i))
                self.cw_output_vl_3[i].setObjectName('cw_output_vl_3_' + str(i))
                self.cw_output_gd_1[i].setObjectName('cw_output_gd_1_' + str(i))
                self.cw_output_lb_1[i].setObjectName('cw_output_lb_1_' + str(i))
                self.cw_output_ln_1[i].setObjectName('cw_output_ln_1_' + str(i))
                self.cw_info_bt_5[i].setObjectName('cw_info_bt_5_' + str(i))
                self.cw_output_lb_2[i].setObjectName('cw_output_lb_2_' + str(i))
                self.cw_output_ln_2[i].setObjectName('cw_output_ln_2_' + str(i))
                self.cw_info_bt_6[i].setObjectName('cw_info_bt_6_' + str(i))
                self.cw_output_lb_3[i].setObjectName('cw_output_lb_3_' + str(i))
                self.cw_output_ln_3[i].setObjectName('cw_output_ln_3_' + str(i))
                self.cw_info_bt_7[i].setObjectName('cw_info_bt_7_' + str(i))
                self.cw_output_lb_4[i].setObjectName('cw_output_lb_4_' + str(i))
                self.cw_output_ln_4[i].setObjectName('cw_output_ln_4_' + str(i))
                self.cw_info_bt_8[i].setObjectName('cw_info_bt_8_' + str(i))
                self.cw_output_hl_2[i].setObjectName('cw_output_hl_2_' + str(i))
                self.cw_output_lb_5[i].setObjectName('cw_output_lb_5_' + str(i))
                self.cw_output_ln_5[i].setObjectName('cw_output_ln_5_' + str(i))
                self.cw_output_ln_6[i].setObjectName('cw_output_ln_6_' + str(i))
                self.cw_info_bt_9[i].setObjectName('cw_info_bt_9_' + str(i))
                self.cw_info_bt_10[i].setObjectName('cw_info_bt_10_' + str(i))
                self.cw_info_bt_11[i].setObjectName('cw_info_bt_11_' + str(i))
                self.cw_output_hl_3[i].setObjectName('cw_output_hl_3_' + str(i))
                self.cw_output_lb_6[i].setObjectName('cw_output_lb_6_' + str(i))
                self.cw_output_lb_7[i].setObjectName('cw_output_lb_7_' + str(i))
                self.cw_output_add_1[i].setObjectName("cw_output_add_1_" + str(i))
                self.cw_output_lw_1[i].setObjectName("cw_output_lw_1_" + str(i))
                self.cw_output_li_1[i].setObjectName("cw_output_li_1_" + str(i))

    def prepare_algorithm_categories(self):
        self.cw_combobox_1.clear()
        self.cw_combobox_1.addItems(['Make a choice...', 'Other...'] + sorted(self.algorithm_categories))

    def add_output_category(self):
        index = int(self.sender().objectName()[16:])
        category = ''
        in_list = False
        if self.cw_output_cb_1[index].currentText() == 'Other...':
            self.categoryWindow = MyCategory()
            if self.categoryWindow.exec_():
                category = str(self.categoryWindow.ac_line.text())
        elif self.cw_output_cb_1[index].currentText() != 'Make a choice...':
            category = str(self.cw_output_cb_1[index].currentText())
        if category:
            for i in range(0, self.cw_output_lw_1[index].count()):
                if category == str(self.cw_output_lw_1[index].item(i).text()):
                    in_list = True
                    break
            if not in_list:
                self.cw_output_lw_1[index].addItem(category)

    def remove_output_category(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - remove_output_category')
        index = int(self.sender().objectName()[15:])
        self.cw_output_lw_1[index].takeItem(self.cw_output_lw_1[index].currentRow())

    def add_algorithm_category(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - add_algorithm_category')

        if self.cw_combobox_1.currentText() == 'Other...':
            self.cw_line_5.setText('')
            self.cw_label_11.setVisible(True)
            self.cw_line_5.setVisible(True)
        else:
            self.cw_line_5.setText('')
            self.cw_label_11.setVisible(False)
            self.cw_line_5.setVisible(False)

    def remove_algorithm_category(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - remove_algorithm_category')
        self.category_list.takeItem(self.category_list.currentRow())

    def prepare_algorithm_creation(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_creation')
        cancel = self.check_all_fields()
        if cancel:
            return
        category = ''
        if self.cw_combobox_1.currentText() == 'Other...':
            category = str(self.cw_line_5.text())
        elif self.cw_combobox_1.currentText() != 'Make a choice...':
            category = str(self.cw_combobox_1.currentText())
        try:
            getattr(getattr(egads.algorithms.user, category.lower()), str(self.cw_line_1.text()))
            info_text = ('An algorithm with the same name and in the same folder already exists in EGADS. Although it '
                         + 'is still possible to create it manually, they will be seen as one and only algorithm '
                         + 'once loaded into EGADS. Please change the name of the new algorithm before saving it.')
            self.infoWindow = MyInfo(info_text)
            self.infoWindow.exec_()
        except AttributeError:
            units_list = self.units_validation()
            if units_list:
                self.unitWindow = MyUnit(units_list)
                if self.unitWindow.exec_():
                    self.choose_filename()
            else:
                self.choose_filename()

    def choose_filename(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - choose_filename')
        category = ''
        if self.cw_combobox_1.currentText() == 'Other...':
            category = str(self.cw_line_5.text())
        elif self.cw_combobox_1.currentText() != 'Make a choice...':
            category = str(self.cw_combobox_1.currentText())
        self.filenameWindow = MyFilename()
        if self.filenameWindow.exec_():
            filename = str(self.filenameWindow.ac_line.text())
            if '.py' in filename:
                filename = filename[:-3]
            if filename:
                if os.path.isfile(egads.__path__[0] + '/algorithms/user/' + category + '/' + filename + '.py'):
                    self.overwriteWindow = MyOverwriteFilename(filename, category)
                    if self.overwriteWindow.exec_():
                        filename = str(self.overwriteWindow.ac_line.text())
                        if '.py' in filename:
                            filename = filename[:-3]
                        if filename:
                            self.create_algorithm(filename, category)
                else:
                    self.create_algorithm(filename, category)

    def create_algorithm(self, filename, category):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - create_algorithm - filename: '
                      + filename + ', category: ' + category)
        author = '__author__ = "' + str(self.cw_line_2.text()) + '"\n'
        date = '__date__ = "' + create_datestring() + '"\n'
        version = '__version__ = "1.0"\n'
        alg_all = '__all__ = ["' + str(self.cw_line_1.text()) + '"]\n\n\n'
        alg_imports = 'import egads.core.egads_core as egads_core\nimport egads.core.metadata as ' \
                      'egads_metadata\n\n'
        alg_class = 'class ' + str(self.cw_line_1.text()) + '(egads_core.EgadsAlgorithm):\n\n'
        purpose = prepare_long_string(str(self.cw_plain_2.toPlainText()), 75, 16)
        description = prepare_long_string(str(self.cw_plain_1.toPlainText()), 75, 16)
        source = prepare_long_string(str(self.cw_line_3.text()), 75, 16)
        reference = prepare_long_string(str(self.cw_line_4.text()), 75, 16)
        alg_input = self.prepare_inputs()
        alg_output = self.prepare_outputs()
        alg_help = ('    """\n'
                    + '    FILE        ' + filename + '.py\n'
                    + '\n'
                    + '    VERSION     1.0\n'
                    + '\n'
                    + '    CATEGORY    ' + category + '\n'
                    + '\n'
                    + '    PURPOSE     ' + purpose + '\n'
                    + '\n'
                    + '    DESCRIPTION ' + description + '\n'
                    + '\n'
                    + '    INPUT       ' + alg_input
                    + '\n'
                    + '    OUTPUT      ' + alg_output
                    + '\n'
                    + '    SOURCE      ' + source + '\n'
                    + '\n'
                    + '    REFERENCES  ' + reference + '\n'
                    + '    """\n\n')
        alg_init = ('    def __init__(self, return_Egads=True):\n        '
                    + 'egads_core.EgadsAlgorithm.__init__(self, return_Egads)\n\n')
        alg_out_metadata = self.prepare_output_metadata()
        alg_metadata = self.prepare_algorithm_metadata()
        alg_run = self.prepare_algorithm_run()
        algorithm = self.prepare_algorithm_text()
        complete_string = (author + date + version + alg_all + alg_imports + alg_class + alg_help
                           + alg_init + alg_out_metadata + alg_metadata + alg_run + algorithm)
        try:
            write_algorithm(filename, complete_string, category, str(self.cw_line_2.text()))
            self.success = True
        except Exception:
            logging.exception('gui - algorithm_window_functions.py - MyAlgorithm - prepare_algorithm : an '
                              'exception occurred when writing the algorithm file.')
            self.success = False
        self.algorithm_filename = filename
        self.algorithm_category = category
        self.algorithm_name = str(self.cw_line_1.text())
        self.cancel = False
        self.close()

    def prepare_inputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_inputs')
        input_string = ''
        input_symbols = []
        input_types = []
        input_units = []
        input_description = []
        for i in range(len(self.cw_input_vl_1)):
            input_symbols.append(str(self.cw_input_ln_1[i].text()))
            if str(self.cw_input_ln_2[i].text()):
                input_units.append(str(self.cw_input_ln_2[i].text()))
            else:
                input_units.append('_')
            input_types.append(str(self.cw_input_ln_3[i].text()))
            input_description.append(str(self.cw_input_ln_4[i].text()))
        max_symbols_length = check_string_max_length(input_symbols)
        max_units_length = check_string_max_length(input_units)
        max_types_length = check_string_max_length(input_types)
        for i in range(len(self.cw_input_vl_1)):
            tmp_string = ' ' * 16
            tmp_string += (input_symbols[i] + ' ' * (max_symbols_length - len(input_symbols[i]) + 4)
                           + input_types[i] + ' ' * (max_types_length - len(input_types[i]) + 4)
                           + input_units[i] + ' ' * (max_units_length - len(input_units[i]) + 4)
                           + input_description[i])
            carriage_length = max_symbols_length + max_types_length + max_units_length + 28
            tmp_string = prepare_long_string(tmp_string, 75, carriage_length)
            input_string += tmp_string + '\n'
        return input_string[16:]

    def prepare_outputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_outputs')
        output_string = ''
        output_symbols = []
        output_types = []
        output_units = []
        output_description = []
        for i in range(len(self.cw_output_vl_1)):
            output_symbols.append(str(self.cw_output_ln_1[i].text()))
            if str(self.cw_output_ln_3[i].text()):
                if 'input' in str(self.cw_output_ln_2[i].text()):
                    output_units.append('_')
                else:
                    output_units.append(str(self.cw_output_ln_2[i].text()))
            else:
                output_units.append('_')
            output_types.append(str(self.cw_output_ln_3[i].text()))
            output_description.append(str(self.cw_output_ln_4[i].text()))
        max_symbols_length = check_string_max_length(output_symbols)
        max_units_length = check_string_max_length(output_units)
        max_types_length = check_string_max_length(output_types)
        for i in range(len(self.cw_output_vl_1)):
            tmp_string = ' ' * 16
            tmp_string += (output_symbols[i] + ' ' * (max_symbols_length - len(output_symbols[i]) + 4)
                           + output_types[i] + ' ' * (max_types_length - len(output_types[i]) + 4)
                           + output_units[i] + ' ' * (max_units_length - len(output_units[i]) + 4)
                           + output_description[i])
            carriage_length = max_symbols_length + max_types_length + max_units_length + 28
            tmp_string = prepare_long_string(tmp_string, 75, carriage_length)
            output_string += tmp_string + '\n'
        return output_string[16:]

    def prepare_output_metadata(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_output_metadata')
        output_string = ''
        if len(self.cw_output_vl_1) > 1:
            output_string += '        self.output_metadata = []\n'
            for i in range(len(self.cw_output_vl_1)):
                units = str(self.cw_output_ln_2[i].text())
                long_name = str(self.cw_output_ln_6[i].text())
                standard_name = str(self.cw_output_ln_5[i].text())
                category = ''
                if self.cw_output_lw_1[i].count() > 0:
                    category += '['
                    for j in range(self.cw_output_lw_1[i].count()):
                        category += "'" + self.cw_output_lw_1[i].item(j).text() + "',"
                    category = category[:-1] + ']'

                ##########################
                #
                # temporaire
                #
                ##########################
                output_string += ("        self.output_metadata.append(egads_metadata.VariableMetadata({"
                                  + "'units':'" + units + "',\n"
                                  + ' ' * 64 + "'long_name':'" + long_name + "',\n"
                                  + ' ' * 64 + "'standard_name':'" + standard_name + "',\n"
                                  + ' ' * 64 + "'Category':" + category + "}))\n\n")

        elif len(self.cw_output_vl_1) == 1:
            units = str(self.cw_output_ln_2[0].text())
            long_name = str(self.cw_output_ln_6[0].text())
            standard_name = str(self.cw_output_ln_5[0].text())
            category = ''
            if self.cw_output_lw_1[0].count() > 0:
                category += '['
                for j in range(self.cw_output_lw_1[0].count()):
                    category += "'" + self.cw_output_lw_1[0].item(j).text() + "',"
                category = category[:-1] + ']'

            ##########################
            #
            # temporaire
            #
            #########################
            output_string += ("        self.output_metadata = egads_metadata.VariableMetadata({"
                              + "'units':'" + units + "',\n"
                              + ' ' * 63 + "'long_name':'" + long_name + "',\n"
                              + ' ' * 63 + "'standard_name':'" + standard_name + "',\n"
                              + ' ' * 63 + "'Category':" + category + "})\n\n")

        return output_string

    def prepare_algorithm_metadata(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_metadata')
        input_symbols = ''
        input_units = ''
        input_types = ''
        input_description = ''
        output_symbols = ''
        output_description = ''
        output_units = ''
        output_types = ''
        for i in range(len(self.cw_input_vl_1)):
            if i == 0:
                input_symbols = '['
                input_units = '['
                input_types = '['
                input_description = '['
            input_symbols += "'" + str(self.cw_input_ln_1[i].text()) + "',"
            if self.cw_input_ln_2[i].text():
                input_units += "'" + str(self.cw_input_ln_2[i].text()) + "',"
            else:
                input_units += "None,"
            input_types += "'" + str(self.cw_input_ln_3[i].text()) + "',"
            input_description += "'" + str(self.cw_input_ln_4[i].text()) + "',"
        input_symbols = input_symbols[:-1] + ']'
        input_units = input_units[:-1] + ']'
        input_types = input_types[:-1] + ']'
        input_description = input_description[:-1] + ']'
        for i in range(len(self.cw_output_vl_1)):
            if i == 0:
                output_symbols = '['
                output_description = '['
                output_units = '['
                output_types = '['
            output_symbols += "'" + str(self.cw_output_ln_1[i].text()) + "',"
            output_description += "'" + str(self.cw_output_ln_4[i].text()) + "',"
            output_units += "'" + str(self.cw_output_ln_2[i].text()) + "',"
            output_types += "'" + str(self.cw_output_ln_3[i].text()) + "',"
        output_symbols = output_symbols[:-1] + ']'
        output_description = output_description[:-1] + ']'
        output_units = output_units[:-1] + ']'
        output_types = output_types[:-1] + ']'
        category = ''
        if self.cw_combobox_1.currentText() == 'Other...':
            category = str(self.cw_line_5.text())
        elif self.cw_combobox_1.currentText() != 'Make a choice...':
            category = str(self.cw_combobox_1.currentText())
        space_string = "                                                          "
        metadata_string = ("        self.metadata = egads_metadata.AlgorithmMetadata({'Inputs':" + input_symbols + ",\n"
                           + space_string + "'InputUnits':" + input_units + ",\n"
                           + space_string + "'InputTypes':" + input_types + ",\n"
                           + space_string + "'InputDescription':" + input_description + ",\n"
                           + space_string + "'Outputs':" + output_symbols + ",\n"
                           + space_string + "'OutputUnits':" + output_units + ",\n"
                           + space_string + "'OutputTypes':" + output_types + ",\n"
                           + space_string + "'OutputDescription':" + output_description + ",\n"
                           + space_string + "'Purpose':'" + str(self.cw_plain_2.toPlainText()) + "',\n"
                           + space_string + "'Description':'" + str(self.cw_plain_1.toPlainText()) + "',\n"
                           + space_string + "'Category':'" + category + "',\n"
                           + space_string + "'Source':'" + str(self.cw_line_3.text()) + "',\n"
                           + space_string + "'References':'" + str(self.cw_line_4.text()) + "',\n"
                           + space_string + "'Processor':self.name,\n"
                           + space_string + "'ProcessorDate':__date__,\n"
                           + space_string + "'ProcessorVersion':__version__,\n"
                           + space_string + "'DateProcessed':self.now()},\n"
                           + space_string + "self.output_metadata)\n\n")
        return metadata_string

    def prepare_algorithm_run(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_run')
        run_string = ''
        input_symbols = ''
        for i in range(len(self.cw_input_vl_1)):
            input_symbols += str(self.cw_input_ln_1[i].text()) + ", "
        input_symbols = input_symbols[:-2]
        run_string += ("    def run(self, " + input_symbols + "):\n"
                       + "        return egads_core.EgadsAlgorithm.run(self, " + input_symbols + ")\n\n"
                       + "    def _algorithm(self, " + input_symbols + "):\n")
        return run_string

    def prepare_algorithm_text(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_text')
        algorithm_string = ''
        if self.cw_plain_4.toPlainText():
            algorithm = ' ' * 8 + str(self.cw_plain_4.toPlainText())
            algorithm_string = algorithm.replace('\n', '\n        ')
            algorithm_string += '\n'
        return algorithm_string

    def units_validation(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - validate_units')
        units_list = []
        for i in range(len(self.cw_input_vl_1)):
            if str(self.cw_input_ln_2[i].text()):
                unit_validation = egads.EgadsData(value=[0], units=str(self.cw_input_ln_2[i].text()))
                units_list.append([str(self.cw_input_ln_1[i].text()), str(self.cw_input_ln_2[i].text()),
                                  unit_validation.units, 'input'])
        for i in range(len(self.cw_output_vl_1)):
            if str(self.cw_output_ln_2[i].text()):
                if 'input' in str(self.cw_output_ln_2[i].text()):
                    pass
                else:
                    unit_validation = egads.EgadsData(value=[0], units=str(self.cw_output_ln_2[i].text()))
                    units_list.append([str(self.cw_output_ln_1[i].text()), str(self.cw_output_ln_2[i].text()),
                                      unit_validation.units, 'output'])
        return units_list

    def check_all_fields(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - check_all_fields')
        self.reset_tab_title_color()
        self.reset_labels_color()
        algorithm_section = True
        for widget, label in self.algorithm_mandatory_fields.items():
            if isinstance(widget, QtWidgets.QLineEdit):
                if not widget.text():
                    algorithm_section = False
                    label.setStyleSheet("QLabel {\n"
                                        "    color: rgb(200,0,0);\n"
                                        "}")
                    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            elif isinstance(widget, QtWidgets.QTextEdit):
                if not widget.toPlainText():
                    algorithm_section = False
                    label.setStyleSheet("QLabel {\n"
                                        "    color: rgb(200,0,0);\n"
                                        "}")
                    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            elif isinstance(widget, QtWidgets.QPlainTextEdit):
                if not widget.toPlainText():
                    algorithm_section = False
                    label.setStyleSheet("QLabel {\n"
                                        "    color: rgb(200,0,0);\n"
                                        "}")
                    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))

        if self.cw_combobox_1.currentText() == 'Make a choice...':
            algorithm_section = False
            self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            self.cw_label_9.setStyleSheet("QLabel {\n"
                                          "    color: rgb(200,0,0);\n"
                                          "}")
        elif self.cw_combobox_1.currentText() == 'Other...' and self.cw_line_5.text() == '':
            algorithm_section = False
            self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            self.cw_label_9.setStyleSheet("QLabel {\n"
                                          "    color: rgb(200,0,0);\n"
                                          "}")
        input_section = True
        if self.cw_input_vl_1:
            widget_list = self.tab_2.findChildren(QtWidgets.QLineEdit)
            for widget in widget_list:
                if 'cw_input_ln_2' not in widget.objectName():
                    if not widget.text():
                        input_section = False
                        label = self.tab_2.findChildren(QtWidgets.QLabel, widget.objectName()[:9] + 'lb' +
                                                        widget.objectName()[11:])[0]
                        label.setStyleSheet("QLabel {\n"
                                            "    color: rgb(200,0,0);\n"
                                            "}")
                        self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200, 0, 0))
        else:
            input_section = False
            self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200, 0, 0))
        output_section = True
        if self.cw_output_vl_1:
            widget_list = self.tab_3.findChildren(QtWidgets.QLineEdit)
            for widget in widget_list:
                if ('cw_output_ln_2' not in widget.objectName()) and ('cw_output_ln_6' not in widget.objectName()):
                    if not widget.text():
                        output_section = False
                        label = self.tab_3.findChildren(QtWidgets.QLabel, widget.objectName()[:10] + 'lb' +
                                                        widget.objectName()[12:])[0]
                        label.setStyleSheet("QLabel {\n"
                                            "    color: rgb(200,0,0);\n"
                                            "}")
                        self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200, 0, 0))
        else:
            output_section = False
            self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200, 0, 0))
        if not output_section or not input_section or not algorithm_section:
            self.fillWindow = MyFill()
            self.fillWindow.exec_()
            result = self.fillWindow.cancel
        else:
            result = False
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - check_all_fields : result ' + str(result))
        return result

    def reset_tab_title_color(self):
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(45, 45, 45))

    def reset_labels_color(self):
        for label in self.findChildren(QtWidgets.QLabel):
            label.setStyleSheet("QLabel {\n"
                                "    color: rgb(45,45,45);\n"
                                "}")

    def algorithm_button_info(self):
        self.infoWindow = MyInfo(self.information_buttons_text[self.sender().objectName()])
        self.infoWindow.exec_()

    def input_output_button_info(self):
        index = -1 * (int(''.join(reversed(self.sender().objectName())).find('_')) + 1)
        self.infoWindow = MyInfo(self.input_output_button_text[self.sender().objectName()[:index]])
        self.infoWindow.exec_()

    def closeWindow(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithmDisplay - closeWindow')
        self.close()
