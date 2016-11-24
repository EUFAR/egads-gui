# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QLineEdit, QPlainTextEdit, QToolButton
from PyQt4.QtCore import QObject, SIGNAL
#


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def modify_attribute_gui(self):
    
    ###########
    ###
    ### prévoir une couleur différente une fois la metadata sauvegardée afin de montrer que cette ligne a été modifée
    ### pour les variables, prévoir la lecture de la liste afin de vérifier si une metadata liée a été modifiée afin
    ### de colorer automatiquement la ligne
    ###
    ###########

    if self.sender().objectName() != "":
        for key, value in self.buttons_lines_dict.iteritems():
            if key == self.sender().objectName():
                widget = self.findChildren(QLineEdit, value)
                if not widget:
                    widget = self.findChildren(QPlainTextEdit, value)
                break
        if "va_button" in self.sender().objectName() and self.listWidget.currentItem():
            if widget[0].isEnabled() == False:
                widget[0].setEnabled(True)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save_as_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.sender().setIcon(icon)
            else:
                self.modified = True
                self.make_window_title()
                widget[0].setEnabled(False)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.sender().setIcon(icon)
                for key, value, in self.objects_metadata_dict.iteritems():
                    if key == widget[0].objectName():
                        var = self.listWidget.currentItem().text()
                        
                        for index, sublist in enumerate(self.list_of_variables_and_attributes):
                            if sublist[0] == var:
                                try:
                                    self.list_of_variables_and_attributes[index][1][value] = str(widget[0].text())
                                except AttributeError:
                                    self.list_of_variables_and_attributes[index][1][value] = str(widget[0].toPlainText())
                                break
                            
                        if value == "var_name":
                            self.listWidget.currentItem().setText(str(widget[0].text()))
                        break
        
        elif "new_button" in self.sender().objectName() and self.new_listwidget.currentItem():
            if widget[0].isEnabled() == False:
                widget[0].setEnabled(True)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save_as_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.sender().setIcon(icon)
            else:
                self.modified = True
                self.make_window_title()
                widget[0].setEnabled(False)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.sender().setIcon(icon)
                
                for key, value, in self.objects_metadata_dict.iteritems():
                    if key == widget[0].objectName():
                        var = self.new_listwidget.currentItem().text()
                        
                        for index, sublist in enumerate(self.list_of_new_variables_and_attributes):
                            if sublist[0] == var:
                                try:
                                    self.list_of_new_variables_and_attributes[index][1][value] = str(widget[0].text())
                                except AttributeError:
                                    self.list_of_new_variables_and_attributes[index][1][value] = str(widget[0].toPlainText())
                                break
                            
                        if value == "var_name":
                            self.new_listwidget.currentItem().setText(str(widget[0].text()))
                        break
                
        
        elif "gm_button" in self.sender().objectName():
            if widget[0].isEnabled() == False:
                widget[0].setEnabled(True)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save_as_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.sender().setIcon(icon)
            else:
                self.modified = True
                self.make_window_title()
                widget[0].setEnabled(False)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.sender().setIcon(icon)
                for key, value, in self.objects_metadata_dict.iteritems():
                    if key == widget[0].objectName():
                        for key2, value2 in self.list_of_global_attributes.iteritems():  # @UnusedVariable
                            if key2 == value:
                                self.list_of_global_attributes[key2] = str(widget[0].toPlainText())
                                break
                        break


def update_global_attribute_gui(self):
    try:
        self.gm_title_ln.setText(self.list_of_global_attributes["title"])
        self.gm_title_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("title")
    try:
        self.gm_institution_ln.setText(self.list_of_global_attributes["institution"])
        self.gm_institution_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("institution")
    try:
        self.gm_source_ln.setText(self.list_of_global_attributes["source"])
        self.gm_source_ln.setCursorPosition(0)
    except KeyError:
        self.missing_global_attributes.append("source")
    try:
        self.gm_project_ln.setText(self.list_of_global_attributes["project"])
        self.gm_project_ln.setCursorPosition(0)
    except KeyError:
        pass
    try:
        self.gm_dateCreation_ln.setText(self.list_of_global_attributes["date_created"])
    except KeyError:
        pass
    try:    
        self.gm_history_ln.setPlainText(self.list_of_global_attributes["history"])
    except KeyError:
        pass


def update_variable_attribute_gui(self):
    if self.tabWidget.currentIndex() == 1:
        list_object = self.listWidget
        variables_and_attributes = self.list_of_variables_and_attributes 
        varName_ln = self.va_varName_ln
        longName_ln = self.va_longName_ln
        category_ln = self.va_category_ln
        processor_ln = self.va_egadsProcessor_ln
        units_ln = self.va_units_ln
    elif self.tabWidget.currentIndex() == 2:
        list_object = self.new_listwidget
        variables_and_attributes = self.list_of_new_variables_and_attributes
        varName_ln = self.new_varName_ln
        longName_ln = self.new_longName_ln
        category_ln = self.new_category_ln
        processor_ln = self.new_egadsProcessor_ln
        units_ln = self.new_units_ln
    for sublist in variables_and_attributes:
        if sublist[1]["var_name"] == list_object.currentItem().text():
            break
    varName_ln.setText(sublist[1]["var_name"])
    varName_ln.setCursorPosition(0)
    try:
        if sublist[1]["long_name"] != "deleted":
            longName_ln.setText(' '.join(str(sublist[1]["long_name"]).split()))
            longName_ln.setCursorPosition(0)
        else:
            longName_ln.setText("")
    except KeyError:
        longName_ln.setText("")
    try:
        if sublist[1]["units"] != "deleted":
            units_ln.setText(str(sublist[1]["units"]))
            units_ln.setCursorPosition(0)
        else:
            units_ln.setText("")
    except KeyError:
            units_ln.setText("")
    try:
        if sublist[1]["Category"] != "deleted":
            if isinstance(sublist[1]["Category"], list):
                category_string = ""
                for string in sublist[1]["Category"]:
                    category_string += string + ", "
                category_ln.setText(category_string[:-2])
            else:
                category_ln.setText(str(sublist[1]["Category"]))
            category_ln.setCursorPosition(0)
        else:
            category_ln.setText("")
    except KeyError:
        category_ln.setText("")
        
    try:
        if sublist[1]["Processor"] != "deleted":
            processor_ln.setPlainText(str(sublist[1]["Processor"]))
            processor_ln.setCursorPosition(0)
        else:
            processor_ln.setPlainText("")
    except KeyError:
        processor_ln.setPlainText("")
    
    
def update_new_variable_list_gui(self):
    self.new_listwidget.clear()
    for sublist in self.list_of_new_variables_and_attributes:
        self.new_listwidget.addItem(sublist[0])


def statusBar_loading(self):
    self.sb_filename_lb = QtGui.QLabel()
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.sb_filename_lb.sizePolicy().hasHeightForWidth())
    self.sb_filename_lb.setSizePolicy(sizePolicy)
    self.sb_filename_lb.setMinimumSize(QtCore.QSize(0, 20))
    self.sb_filename_lb.setMaximumSize(QtCore.QSize(16777215, 20))
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("font/SourceSansPro-Regular.ttf"))
    font.setPointSize(10)
    font.setItalic(True)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.sb_filename_lb.setFont(font)
    self.sb_filename_lb.setObjectName(_fromUtf8("sb_filename_lb"))
    self.sb_filename_lb.setText("")
    self.statusBar.addWidget(self.sb_filename_lb)


def statusBar_updating(self, string):
    self.sb_filename_lb.setText(string)


def netcdf_gui(self):
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
    font.setPointSize(12)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font2 = QtGui.QFont()
    font2.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
    font2.setPointSize(10)
    font2.setKerning(True)
    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.actionSaveAsBar.setEnabled(True)
    self.actionCloseBar.setEnabled(True)
    self.actionCreateVariableBar.setEnabled(True)
    self.actionGlobalAttributesBar.setEnabled(True)
    self.tabWidget = QtGui.QTabWidget(self.centralwidget)
    self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
    
    self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
    self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
    
    
    self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane { \n"
    "    border: 1px solid rgb(180,180,180);\n"
    "    border-bottom-left-radius: 5px;\n"
    "    border-bottom-right-radius: 5px;\n"
    "    border-top-right-radius: 5px;\n"
    "   top: -1px;\n"
    "   background-color: rgb(230,230,230);\n"
    "}\n"
    "\n"
    "QTabWidget::tab-bar {\n"
    "    left: 0px; \n"
    "}\n"
    "\n"
    "QTabBar::tab {\n"
    "    background: transparent;\n"
    "    border-top: 1px solid rgb(180,180,180);\n"
    "    border-left: 1px solid rgb(180,180,180);\n"
    "    border-right: 1px solid rgb(180,180,180);\n"
    "    border-top-right-radius: 5px;\n"
    "     border-top-left-radius: 5px;\n"
    "    padding: 2px 10px 2px 10px;\n"
    "    margin-right: 2px;\n"
    "}\n"
    "\n"
    "QTabBar::tab:hover {\n"
    "    background-color: rgb(210,210,210);\n"
    "}\n"
    "\n"
    "QTabBar::tab:selected {\n"
    "    background-color: rgb(230,230,230);\n"
    "}\n"
    "\n"
    "QTabBar::tab:!selected {\n"
    "    margin-top: 4px; \n"
    "}"))
    self.tab = QtGui.QWidget()
    self.tab.setObjectName(_fromUtf8("tab"))
    self.gridLayout_2 = QtGui.QGridLayout(self.tab)
    self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
    spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
    self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
    self.verticalLayout_7 = QtGui.QVBoxLayout()
    self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.gm_filename_lb = QtGui.QLabel(self.tab)
    self.gm_filename_lb.setMinimumSize(QtCore.QSize(90, 27))
    self.gm_filename_lb.setMaximumSize(QtCore.QSize(90, 27))
    self.gm_filename_lb.setObjectName(_fromUtf8("gm_filename_lb"))
    self.gm_filename_lb.setFont(font)
    self.horizontalLayout.addWidget(self.gm_filename_lb)
    self.gm_filename_ln = QtGui.QLabel(self.tab)
    self.gm_filename_ln.setMinimumSize(QtCore.QSize(500, 27))
    self.gm_filename_ln.setMaximumSize(QtCore.QSize(500, 27))
    self.gm_filename_ln.setObjectName(_fromUtf8("gm_filename_ln"))
    self.gm_filename_ln.setFont(font)
    self.horizontalLayout.addWidget(self.gm_filename_ln)
    spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem1)
    self.gm_dateCreation_lb = QtGui.QLabel(self.tab)
    self.gm_dateCreation_lb.setMinimumSize(QtCore.QSize(130, 27))
    self.gm_dateCreation_lb.setMaximumSize(QtCore.QSize(130, 27))
    self.gm_dateCreation_lb.setObjectName(_fromUtf8("gm_dateCreation_lb"))
    self.gm_dateCreation_lb.setFont(font)
    self.horizontalLayout.addWidget(self.gm_dateCreation_lb)
    self.gm_dateCreation_ln = QtGui.QLabel(self.tab)
    self.gm_dateCreation_ln.setMinimumSize(QtCore.QSize(150, 27))
    self.gm_dateCreation_ln.setMaximumSize(QtCore.QSize(150, 27))
    self.gm_dateCreation_ln.setObjectName(_fromUtf8("gm_dateCreation_ln"))
    self.gm_dateCreation_ln.setFont(font)
    self.horizontalLayout.addWidget(self.gm_dateCreation_ln)
    spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem2)
    self.verticalLayout_7.addLayout(self.horizontalLayout)
    spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    self.verticalLayout_7.addItem(spacerItem3)
    self.horizontalLayout_6 = QtGui.QHBoxLayout()
    self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
    self.verticalLayout_2 = QtGui.QVBoxLayout()
    self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
    self.horizontalLayout_2 = QtGui.QHBoxLayout()
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    self.gm_title_lb = QtGui.QLabel(self.tab)
    self.gm_title_lb.setMinimumSize(QtCore.QSize(90, 27))
    self.gm_title_lb.setMaximumSize(QtCore.QSize(90, 27))
    self.gm_title_lb.setObjectName(_fromUtf8("gm_title_lb"))
    self.gm_title_lb.setFont(font)
    self.horizontalLayout_2.addWidget(self.gm_title_lb)
    self.gm_title_ln = QtGui.QLineEdit(self.tab)
    self.gm_title_ln.setEnabled(False)
    self.gm_title_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.gm_title_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.gm_title_ln.setPalette(palette)
    self.gm_title_ln.setFrame(False)
    self.gm_title_ln.setObjectName(_fromUtf8("gm_title_ln"))
    self.gm_title_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.gm_title_ln.setFont(font)
    self.horizontalLayout_2.addWidget(self.gm_title_ln)
    self.gm_button_1 = QtGui.QToolButton(self.tab)
    self.gm_button_1.setMinimumSize(QtCore.QSize(27, 27))
    self.gm_button_1.setMaximumSize(QtCore.QSize(27, 27))
    self.gm_button_1.setText(_fromUtf8(""))
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.gm_button_1.setIcon(icon1)
    self.gm_button_1.setIconSize(QtCore.QSize(27, 27))
    self.gm_button_1.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.gm_button_1.setAutoRaise(True)
    self.gm_button_1.setObjectName(_fromUtf8("gm_button_1"))
    self.gm_button_1.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_2.addWidget(self.gm_button_1)
    spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem4)
    self.verticalLayout_2.addLayout(self.horizontalLayout_2)
    spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    self.verticalLayout_2.addItem(spacerItem5)
    self.horizontalLayout_3 = QtGui.QHBoxLayout()
    self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
    self.gm_institution_lb = QtGui.QLabel(self.tab)
    self.gm_institution_lb.setMinimumSize(QtCore.QSize(90, 27))
    self.gm_institution_lb.setMaximumSize(QtCore.QSize(90, 27))
    self.gm_institution_lb.setObjectName(_fromUtf8("gm_institution_lb"))
    self.gm_institution_lb.setFont(font)
    self.horizontalLayout_3.addWidget(self.gm_institution_lb)
    self.gm_institution_ln = QtGui.QLineEdit(self.tab)
    self.gm_institution_ln.setEnabled(False)
    self.gm_institution_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.gm_institution_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.gm_institution_ln.setPalette(palette)
    self.gm_institution_ln.setFrame(False)
    self.gm_institution_ln.setObjectName(_fromUtf8("gm_institution_ln"))
    self.gm_institution_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.gm_institution_ln.setFont(font)
    self.horizontalLayout_3.addWidget(self.gm_institution_ln)
    self.gm_button_2 = QtGui.QToolButton(self.tab)
    self.gm_button_2.setMinimumSize(QtCore.QSize(27, 27))
    self.gm_button_2.setMaximumSize(QtCore.QSize(27, 27))
    self.gm_button_2.setText(_fromUtf8(""))
    self.gm_button_2.setIcon(icon1)
    self.gm_button_2.setIconSize(QtCore.QSize(27, 27))
    self.gm_button_2.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.gm_button_2.setAutoRaise(True)
    self.gm_button_2.setObjectName(_fromUtf8("gm_button_2"))
    self.gm_button_2.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_3.addWidget(self.gm_button_2)
    spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_3.addItem(spacerItem6)
    self.verticalLayout_2.addLayout(self.horizontalLayout_3)
    spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    self.verticalLayout_2.addItem(spacerItem7)
    self.horizontalLayout_4 = QtGui.QHBoxLayout()
    self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
    self.gm_source_lb = QtGui.QLabel(self.tab)
    self.gm_source_lb.setMinimumSize(QtCore.QSize(90, 27))
    self.gm_source_lb.setMaximumSize(QtCore.QSize(90, 27))
    self.gm_source_lb.setObjectName(_fromUtf8("gm_source_lb"))
    self.gm_source_lb.setFont(font)
    self.horizontalLayout_4.addWidget(self.gm_source_lb)
    self.gm_source_ln = QtGui.QLineEdit(self.tab)
    self.gm_source_ln.setEnabled(False)
    self.gm_source_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.gm_source_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.gm_source_ln.setPalette(palette)
    self.gm_source_ln.setFrame(False)
    self.gm_source_ln.setObjectName(_fromUtf8("gm_source_ln"))
    self.gm_source_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.gm_source_ln.setFont(font)
    self.horizontalLayout_4.addWidget(self.gm_source_ln)
    self.gm_button_3 = QtGui.QToolButton(self.tab)
    self.gm_button_3.setMinimumSize(QtCore.QSize(27, 27))
    self.gm_button_3.setMaximumSize(QtCore.QSize(27, 27))
    self.gm_button_3.setText(_fromUtf8(""))
    self.gm_button_3.setIcon(icon1)
    self.gm_button_3.setIconSize(QtCore.QSize(27, 27))
    self.gm_button_3.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.gm_button_3.setAutoRaise(True)
    self.gm_button_3.setObjectName(_fromUtf8("gm_button_3"))
    self.gm_button_3.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_4.addWidget(self.gm_button_3)
    spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_4.addItem(spacerItem8)
    self.verticalLayout_2.addLayout(self.horizontalLayout_4)
    spacerItem9 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    self.verticalLayout_2.addItem(spacerItem9)
    self.horizontalLayout_5 = QtGui.QHBoxLayout()
    self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
    self.gm_project_lb = QtGui.QLabel(self.tab)
    self.gm_project_lb.setMinimumSize(QtCore.QSize(90, 27))
    self.gm_project_lb.setMaximumSize(QtCore.QSize(90, 27))
    self.gm_project_lb.setObjectName(_fromUtf8("gm_project_lb"))
    self.gm_project_lb.setFont(font)
    self.horizontalLayout_5.addWidget(self.gm_project_lb)
    self.gm_project_ln = QtGui.QLineEdit(self.tab)
    self.gm_project_ln.setEnabled(False)
    self.gm_project_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.gm_project_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.gm_project_ln.setPalette(palette)
    self.gm_project_ln.setFrame(False)
    self.gm_project_ln.setObjectName(_fromUtf8("gm_project_ln"))
    self.gm_project_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.gm_project_ln.setFont(font)
    self.horizontalLayout_5.addWidget(self.gm_project_ln)
    self.gm_button_4 = QtGui.QToolButton(self.tab)
    self.gm_button_4.setMinimumSize(QtCore.QSize(27, 27))
    self.gm_button_4.setMaximumSize(QtCore.QSize(27, 27))
    self.gm_button_4.setText(_fromUtf8(""))
    self.gm_button_4.setIcon(icon1)
    self.gm_button_4.setIconSize(QtCore.QSize(27, 27))
    self.gm_button_4.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.gm_button_4.setAutoRaise(True)
    self.gm_button_4.setObjectName(_fromUtf8("gm_button_4"))
    self.gm_button_4.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_5.addWidget(self.gm_button_4)
    spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_5.addItem(spacerItem10)
    self.verticalLayout_2.addLayout(self.horizontalLayout_5)
    self.horizontalLayout_6.addLayout(self.verticalLayout_2)
    spacerItem11 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_6.addItem(spacerItem11)
    self.verticalLayout_3 = QtGui.QVBoxLayout()
    self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
    self.horizontalLayout_8 = QtGui.QHBoxLayout()
    self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
    self.verticalLayout = QtGui.QVBoxLayout()
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.gm_history_lb = QtGui.QLabel(self.tab)
    self.gm_history_lb.setMinimumSize(QtCore.QSize(90, 27))
    self.gm_history_lb.setMaximumSize(QtCore.QSize(90, 27))
    self.gm_history_lb.setObjectName(_fromUtf8("gm_history_lb"))
    self.gm_history_lb.setFont(font)
    self.verticalLayout.addWidget(self.gm_history_lb)
    self.horizontalLayout_7 = QtGui.QHBoxLayout()
    self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
    spacerItem12 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_7.addItem(spacerItem12)
    self.gm_button_5 = QtGui.QToolButton(self.tab)
    self.gm_button_5.setMinimumSize(QtCore.QSize(27, 27))
    self.gm_button_5.setMaximumSize(QtCore.QSize(27, 27))
    self.gm_button_5.setText(_fromUtf8(""))
    self.gm_button_5.setIcon(icon1)
    self.gm_button_5.setIconSize(QtCore.QSize(27, 27))
    self.gm_button_5.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.gm_button_5.setAutoRaise(True)
    self.gm_button_5.setObjectName(_fromUtf8("gm_button_5"))
    self.gm_button_5.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_7.addWidget(self.gm_button_5)
    spacerItem13 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_7.addItem(spacerItem13)
    self.verticalLayout.addLayout(self.horizontalLayout_7)
    spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.verticalLayout.addItem(spacerItem14)
    self.horizontalLayout_8.addLayout(self.verticalLayout)
    self.gm_history_ln = QtGui.QPlainTextEdit(self.tab)
    self.gm_history_ln.setEnabled(False)
    self.gm_history_ln.setMinimumSize(QtCore.QSize(400, 150))
    self.gm_history_ln.setMaximumSize(QtCore.QSize(400, 150))
    palette = QtGui.QPalette()
    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    self.gm_history_ln.setPalette(palette)
    self.gm_history_ln.setFrameShape(QtGui.QFrame.NoFrame)
    self.gm_history_ln.setObjectName(_fromUtf8("gm_history_ln"))
    self.gm_history_ln.setStyleSheet(_fromUtf8("QPlainTextEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QPlainTextEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.gm_history_ln.setFont(font)
    self.horizontalLayout_8.addWidget(self.gm_history_ln)
    self.verticalLayout_3.addLayout(self.horizontalLayout_8)
    spacerItem15 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.verticalLayout_3.addItem(spacerItem15)
    self.horizontalLayout_6.addLayout(self.verticalLayout_3)
    
    self.verticalLayout_7.addLayout(self.horizontalLayout_6)
    spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    self.verticalLayout_7.addItem(spacerItem16)
    self.horizontalLayout_9 = QtGui.QHBoxLayout()
    self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
    self.gm_compatibility_lb = QtGui.QLabel(self.tab)
    self.gm_compatibility_lb.setMinimumSize(QtCore.QSize(30, 30))
    self.gm_compatibility_lb.setMaximumSize(QtCore.QSize(30, 30))
    self.gm_compatibility_lb.setScaledContents(True)
    self.gm_compatibility_lb.setObjectName(_fromUtf8("gm_compatibility_lb"))
    self.horizontalLayout_9.addWidget(self.gm_compatibility_lb)
    self.gm_details_lb = QtGui.QLabel(self.tab)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.gm_details_lb.sizePolicy().hasHeightForWidth())
    self.gm_details_lb.setSizePolicy(sizePolicy)
    self.gm_details_lb.setMinimumSize(QtCore.QSize(700, 27))
    self.gm_details_lb.setMaximumSize(QtCore.QSize(700, 54))
    self.gm_details_lb.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
    self.gm_details_lb.setWordWrap(True)
    self.gm_details_lb.setObjectName(_fromUtf8("gm_details_lb"))
    self.gm_details_lb.setFont(font2)
    self.horizontalLayout_9.addWidget(self.gm_details_lb)
    spacerItem17 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_9.addItem(spacerItem17)
    self.gm_button_6 = QtGui.QToolButton(self.tab)
    self.gm_button_6.setEnabled(False)
    self.gm_button_6.setMinimumSize(QtCore.QSize(27, 27))
    self.gm_button_6.setMaximumSize(QtCore.QSize(27, 27))
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/none_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.gm_button_6.setIcon(icon2)
    self.gm_button_6.setIconSize(QtCore.QSize(27, 27))
    self.gm_button_6.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.gm_button_6.setAutoRaise(True)
    self.gm_button_6.setArrowType(QtCore.Qt.NoArrow)
    self.gm_button_6.setObjectName(_fromUtf8("gm_button_6"))
    self.gm_button_6.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_9.addWidget(self.gm_button_6)
    spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_9.addItem(spacerItem18)
    self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        
    self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
    spacerItem16 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.gridLayout_2.addItem(spacerItem16, 0, 2, 1, 1)
    spacerItem17 = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout_2.addItem(spacerItem17, 1, 1, 1, 1)
    self.tabWidget.addTab(self.tab, _fromUtf8(""))
    self.tab_2 = QtGui.QWidget()
    self.tab_2.setObjectName(_fromUtf8("tab_2"))
    self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
    self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
    spacerItem18 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
    self.gridLayout_3.addItem(spacerItem18, 0, 0, 1, 1)
    self.horizontalLayout_17 = QtGui.QHBoxLayout()
    self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
    self.listWidget = QtGui.QListWidget(self.tab_2)
    self.listWidget.setMinimumSize(QtCore.QSize(400, 0))
    self.listWidget.setMaximumSize(QtCore.QSize(400, 16777215))
    self.listWidget.setFrameShape(QtGui.QFrame.NoFrame)
    self.listWidget.setObjectName(_fromUtf8("listWidget"))
    self.listWidget.setFont(font)
    self.listWidget.setStyleSheet(_fromUtf8("QListWidget {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QListView::item:selected {\n"
    "    border: 1px solid rgb(240,240,240);\n"
    "    border-radius: 3px;\n"
    "}\n"
    "\n"
    "QListView::item:selected:!active {\n"
    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "                            stop: 0 #e5e5e5, stop: 1 #b2b2b2);\n"
    "}\n"
    "\n"
    "QListView::item:selected:active {\n"
    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "                            stop: 0 #e5e5e5, stop: 1 #b2b2b2);\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QListView::item:hover {\n"
    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "                            stop: 0 #F0F0F0, stop: 1 #dddddd);\n"
    "    border: 1px solid rgb(240,240,240);\n"
    "    border-radius: 3px;\n"
    "}\n"
    ""))
    self.horizontalLayout_17.addWidget(self.listWidget)
    self.line = QtGui.QFrame(self.tab_2)
    self.line.setFrameShape(QtGui.QFrame.VLine)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setObjectName(_fromUtf8("line"))
    self.horizontalLayout_17.addWidget(self.line)
    self.verticalLayout_6 = QtGui.QVBoxLayout()
    self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
    self.verticalLayout_5 = QtGui.QVBoxLayout()
    self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
    self.horizontalLayout_16 = QtGui.QHBoxLayout()
    self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
    self.va_varName_lb = QtGui.QLabel(self.tab_2)
    self.va_varName_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.va_varName_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.va_varName_lb.setObjectName(_fromUtf8("va_varName_lb"))
    self.va_varName_lb.setFont(font)
    self.horizontalLayout_16.addWidget(self.va_varName_lb)
    self.va_varName_ln = QtGui.QLineEdit(self.tab_2)
    self.va_varName_ln.setEnabled(False)
    self.va_varName_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.va_varName_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.va_varName_ln.setPalette(palette)
    self.va_varName_ln.setFrame(False)
    self.va_varName_ln.setObjectName(_fromUtf8("va_varName_ln"))
    self.va_varName_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.va_varName_ln.setFont(font)
    self.horizontalLayout_16.addWidget(self.va_varName_ln)
    self.va_button_1 = QtGui.QToolButton(self.tab_2)
    self.va_button_1.setEnabled(False)
    self.va_button_1.setMinimumSize(QtCore.QSize(27, 27))
    self.va_button_1.setMaximumSize(QtCore.QSize(27, 27))
    self.va_button_1.setText(_fromUtf8(""))
    self.va_button_1.setIcon(icon1)
    self.va_button_1.setIconSize(QtCore.QSize(27, 27))
    self.va_button_1.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.va_button_1.setAutoRaise(True)
    self.va_button_1.setObjectName(_fromUtf8("va_button_1"))
    self.va_button_1.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_16.addWidget(self.va_button_1)
    spacerItem19 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_16.addItem(spacerItem19)
    self.verticalLayout_5.addLayout(self.horizontalLayout_16)
    self.horizontalLayout_10 = QtGui.QHBoxLayout()
    self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
    self.va_longName_lb = QtGui.QLabel(self.tab_2)
    self.va_longName_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.va_longName_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.va_longName_lb.setObjectName(_fromUtf8("va_longName_lb"))
    self.va_longName_lb.setFont(font)
    self.horizontalLayout_10.addWidget(self.va_longName_lb)
    self.va_longName_ln = QtGui.QLineEdit(self.tab_2)
    self.va_longName_ln.setEnabled(False)
    self.va_longName_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.va_longName_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.va_longName_ln.setPalette(palette)
    self.va_longName_ln.setFrame(False)
    self.va_longName_ln.setObjectName(_fromUtf8("va_longName_ln"))
    self.va_longName_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.va_longName_ln.setFont(font)
    self.horizontalLayout_10.addWidget(self.va_longName_ln)
    self.va_button_2 = QtGui.QToolButton(self.tab_2)
    self.va_button_2.setEnabled(False)
    self.va_button_2.setMinimumSize(QtCore.QSize(27, 27))
    self.va_button_2.setMaximumSize(QtCore.QSize(27, 27))
    self.va_button_2.setText(_fromUtf8(""))
    self.va_button_2.setIcon(icon1)
    self.va_button_2.setIconSize(QtCore.QSize(27, 27))
    self.va_button_2.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.va_button_2.setAutoRaise(True)
    self.va_button_2.setObjectName(_fromUtf8("va_button_2"))
    self.va_button_2.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_10.addWidget(self.va_button_2)
    spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_10.addItem(spacerItem20)
    self.verticalLayout_5.addLayout(self.horizontalLayout_10)
    self.horizontalLayout_11 = QtGui.QHBoxLayout()
    self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
    self.va_category_lb = QtGui.QLabel(self.tab_2)
    self.va_category_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.va_category_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.va_category_lb.setObjectName(_fromUtf8("va_category_lb"))
    self.va_category_lb.setFont(font)
    self.horizontalLayout_11.addWidget(self.va_category_lb)
    self.va_category_ln = QtGui.QLineEdit(self.tab_2)
    self.va_category_ln.setEnabled(False)
    self.va_category_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.va_category_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.va_category_ln.setPalette(palette)
    self.va_category_ln.setFrame(False)
    self.va_category_ln.setObjectName(_fromUtf8("va_category_ln"))
    self.va_category_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.va_category_ln.setFont(font)
    self.horizontalLayout_11.addWidget(self.va_category_ln)
    self.va_button_3 = QtGui.QToolButton(self.tab_2)
    self.va_button_3.setEnabled(False)
    self.va_button_3.setMinimumSize(QtCore.QSize(27, 27))
    self.va_button_3.setMaximumSize(QtCore.QSize(27, 27))
    self.va_button_3.setText(_fromUtf8(""))
    self.va_button_3.setIcon(icon1)
    self.va_button_3.setIconSize(QtCore.QSize(27, 27))
    self.va_button_3.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.va_button_3.setAutoRaise(True)
    self.va_button_3.setObjectName(_fromUtf8("va_button_3"))
    self.va_button_3.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_11.addWidget(self.va_button_3)
    spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_11.addItem(spacerItem21)
    self.verticalLayout_5.addLayout(self.horizontalLayout_11)
    self.horizontalLayout_12 = QtGui.QHBoxLayout()
    self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
    self.va_units_lb = QtGui.QLabel(self.tab_2)
    self.va_units_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.va_units_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.va_units_lb.setObjectName(_fromUtf8("va_units_lb"))
    self.va_units_lb.setFont(font)
    self.horizontalLayout_12.addWidget(self.va_units_lb)
    self.va_units_ln = QtGui.QLineEdit(self.tab_2)
    self.va_units_ln.setEnabled(False)
    self.va_units_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.va_units_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.va_units_ln.setPalette(palette)
    self.va_units_ln.setFrame(False)
    self.va_units_ln.setObjectName(_fromUtf8("va_units_ln"))
    self.va_units_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.va_units_ln.setFont(font)
    self.horizontalLayout_12.addWidget(self.va_units_ln)
    self.va_button_4 = QtGui.QToolButton(self.tab_2)
    self.va_button_4.setEnabled(False)
    self.va_button_4.setMinimumSize(QtCore.QSize(27, 27))
    self.va_button_4.setMaximumSize(QtCore.QSize(27, 27))
    self.va_button_4.setText(_fromUtf8(""))
    self.va_button_4.setIcon(icon1)
    self.va_button_4.setIconSize(QtCore.QSize(27, 27))
    self.va_button_4.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.va_button_4.setAutoRaise(True)
    self.va_button_4.setObjectName(_fromUtf8("va_button_4"))
    self.va_button_4.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.horizontalLayout_12.addWidget(self.va_button_4)
    spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_12.addItem(spacerItem22)
    self.verticalLayout_5.addLayout(self.horizontalLayout_12)
    self.horizontalLayout_13 = QtGui.QHBoxLayout()
    self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
    self.va_fillValue_lb = QtGui.QLabel(self.tab_2)
    self.va_fillValue_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.va_fillValue_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.va_fillValue_lb.setObjectName(_fromUtf8("va_fillValue_lb"))
    self.va_fillValue_lb.setFont(font)
    self.horizontalLayout_13.addWidget(self.va_fillValue_lb)
    self.va_fillValue_ln = QtGui.QLabel(self.tab_2)
    self.va_fillValue_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.va_fillValue_ln.setMaximumSize(QtCore.QSize(300, 27))
    self.va_fillValue_ln.setObjectName(_fromUtf8("va_fillValue_ln"))
    self.va_fillValue_ln.setFont(font)
    self.horizontalLayout_13.addWidget(self.va_fillValue_ln)
    spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_13.addItem(spacerItem23)
    self.verticalLayout_5.addLayout(self.horizontalLayout_13)
    self.horizontalLayout_14 = QtGui.QHBoxLayout()
    self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
    self.va_dimensions_lb = QtGui.QLabel(self.tab_2)
    self.va_dimensions_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.va_dimensions_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.va_dimensions_lb.setObjectName(_fromUtf8("va_dimensions_lb"))
    self.va_dimensions_lb.setFont(font)
    self.horizontalLayout_14.addWidget(self.va_dimensions_lb)
    self.va_dimensions_ln = QtGui.QLabel(self.tab_2)
    self.va_dimensions_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.va_dimensions_ln.setMaximumSize(QtCore.QSize(300, 27))
    self.va_dimensions_ln.setObjectName(_fromUtf8("va_dimensions_ln"))
    self.va_dimensions_ln.setFont(font)
    self.horizontalLayout_14.addWidget(self.va_dimensions_ln)
    spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_14.addItem(spacerItem24)
    self.verticalLayout_5.addLayout(self.horizontalLayout_14)
    self.horizontalLayout_15 = QtGui.QHBoxLayout()
    self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
    self.verticalLayout_4 = QtGui.QVBoxLayout()
    self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
    self.va_egadsProcessor_lb = QtGui.QLabel(self.tab_2)
    self.va_egadsProcessor_lb.setMinimumSize(QtCore.QSize(150, 27))
    self.va_egadsProcessor_lb.setMaximumSize(QtCore.QSize(150, 27))
    self.va_egadsProcessor_lb.setObjectName(_fromUtf8("va_egadsProcessor_lb"))
    self.va_egadsProcessor_lb.setFont(font)
    self.verticalLayout_4.addWidget(self.va_egadsProcessor_lb)
    spacerItem25 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.verticalLayout_4.addItem(spacerItem25)
    self.horizontalLayout_15.addLayout(self.verticalLayout_4)
    self.va_egadsProcessor_ln = QtGui.QPlainTextEdit(self.tab_2)
    self.va_egadsProcessor_ln.setEnabled(False)
    self.va_egadsProcessor_ln.setMinimumSize(QtCore.QSize(350, 100))
    self.va_egadsProcessor_ln.setMaximumSize(QtCore.QSize(350, 100))
    palette = QtGui.QPalette()
    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    self.va_egadsProcessor_ln.setPalette(palette)
    self.va_egadsProcessor_ln.setFrameShape(QtGui.QFrame.NoFrame)
    self.va_egadsProcessor_ln.setObjectName(_fromUtf8("va_egadsProcessor_ln"))
    self.va_egadsProcessor_ln.setStyleSheet(_fromUtf8("QPlainTextEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QPlainTextEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.va_egadsProcessor_ln.setFont(font)
    self.horizontalLayout_15.addWidget(self.va_egadsProcessor_ln)
    self.verticalLayout_5.addLayout(self.horizontalLayout_15)
    self.verticalLayout_6.addLayout(self.verticalLayout_5)
    spacerItem26 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.verticalLayout_6.addItem(spacerItem26)
    self.horizontalLayout_17.addLayout(self.verticalLayout_6)
    self.gridLayout_3.addLayout(self.horizontalLayout_17, 0, 1, 2, 1)
    spacerItem27 = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.gridLayout_3.addItem(spacerItem27, 1, 2, 1, 1)
    spacerItem28 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout_3.addItem(spacerItem28, 2, 1, 1, 1)
    self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
    self.verticalLayout3.addWidget(self.tabWidget)
    
    
    self.gm_filename_lb.setText(_translate("MainWindow", "Filename:", None))
    self.gm_filename_ln.setText(_translate("MainWindow", "TEMP", None))
    self.gm_dateCreation_lb.setText(_translate("MainWindow", "Date of creation:", None))
    self.gm_dateCreation_ln.setText(_translate("MainWindow", "TEMP", None))
    self.gm_title_lb.setText(_translate("MainWindow", "Title:", None))
    self.gm_title_ln.setText(_translate("MainWindow", "TEMP", None))
    self.gm_institution_lb.setText(_translate("MainWindow", "Institution:", None))
    self.gm_institution_ln.setText(_translate("MainWindow", "TEMP", None))
    self.gm_source_lb.setText(_translate("MainWindow", "Source:", None))
    self.gm_source_ln.setText(_translate("MainWindow", "TEMP", None))
    self.gm_project_lb.setText(_translate("MainWindow", "Project:", None))
    self.gm_project_ln.setText(_translate("MainWindow", "TEMP", None))
    self.gm_history_lb.setText(_translate("MainWindow", "History:", None))
    self.gm_history_ln.setPlainText(_translate("MainWindow", "TEMP", None))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Global Metadata", None))
    self.va_varName_lb.setText(_translate("MainWindow", "Variable name:", None))
    self.va_varName_ln.setText(_translate("MainWindow", "TEMP", None))
    self.va_longName_lb.setText(_translate("MainWindow", "Long name:", None))
    self.va_longName_ln.setText(_translate("MainWindow", "TEMP", None))
    self.va_category_lb.setText(_translate("MainWindow", "Category:", None))
    self.va_category_ln.setText(_translate("MainWindow", "TEMP", None))
    self.va_units_lb.setText(_translate("MainWindow", "Units:", None))
    self.va_units_ln.setText(_translate("MainWindow", "TEMP", None))
    self.va_fillValue_lb.setText(_translate("MainWindow", "Fill value:", None))
    self.va_fillValue_ln.setText(_translate("MainWindow", "TEMP", None))
    self.va_dimensions_lb.setText(_translate("MainWindow", "Dimensions:", None))
    self.va_dimensions_ln.setText(_translate("MainWindow", "TEMP", None))
    self.va_egadsProcessor_lb.setText(_translate("MainWindow", "EGADS processor:", None))
    self.va_egadsProcessor_ln.setPlainText(_translate("MainWindow", "TEMP", None))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Variables", None))


def add_new_variable_gui(self):
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("fonts/SourceSansPro-Regular.ttf"))
    font.setPointSize(12)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.new_tab = QtGui.QWidget()
    self.new_tab.setObjectName(_fromUtf8("new_tab"))
    self.new_grid = QtGui.QGridLayout(self.new_tab)
    self.new_grid.setObjectName(_fromUtf8("new_grid"))
    spacerItem18 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
    self.new_grid.addItem(spacerItem18, 0, 0, 1, 1)
    self.new_horlay_1 = QtGui.QHBoxLayout()
    self.new_horlay_1.setObjectName(_fromUtf8("new_horlay_1"))
    self.new_listwidget = QtGui.QListWidget(self.new_tab)
    self.new_listwidget.setMinimumSize(QtCore.QSize(400, 0))
    self.new_listwidget.setMaximumSize(QtCore.QSize(400, 16777215))
    self.new_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
    self.new_listwidget.setObjectName(_fromUtf8("new_listwidget"))
    self.new_listwidget.setStyleSheet(_fromUtf8("QListWidget {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QListView::item:selected {\n"
    "    border: 1px solid rgb(240,240,240);\n"
    "    border-radius: 3px;\n"
    "}\n"
    "\n"
    "QListView::item:selected:!active {\n"
    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "                            stop: 0 #e5e5e5, stop: 1 #b2b2b2);\n"
    "}\n"
    "\n"
    "QListView::item:selected:active {\n"
    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "                            stop: 0 #e5e5e5, stop: 1 #b2b2b2);\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QListView::item:hover {\n"
    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "                            stop: 0 #F0F0F0, stop: 1 #dddddd);\n"
    "    border: 1px solid rgb(240,240,240);\n"
    "    border-radius: 3px;\n"
    "}\n"
    ""))
    self.new_listwidget.setFont(font)
    self.new_horlay_1.addWidget(self.new_listwidget)
    self.new_line = QtGui.QFrame(self.new_tab)
    self.new_line.setFrameShape(QtGui.QFrame.VLine)
    self.new_line.setFrameShadow(QtGui.QFrame.Sunken)
    self.new_line.setObjectName(_fromUtf8("new_line"))
    self.new_horlay_1.addWidget(self.new_line)
    self.new_verlay_1 = QtGui.QVBoxLayout()
    self.new_verlay_1.setObjectName(_fromUtf8("new_verlay_1"))
    self.new_verlay_2 = QtGui.QVBoxLayout()
    self.new_verlay_2.setObjectName(_fromUtf8("new_verlay_2"))
    self.new_horlay_2 = QtGui.QHBoxLayout()
    self.new_horlay_2.setObjectName(_fromUtf8("new_horlay_2"))
    self.new_varName_lb = QtGui.QLabel(self.new_tab)
    self.new_varName_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.new_varName_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.new_varName_lb.setObjectName(_fromUtf8("new_varName_lb"))
    
    self.new_varName_lb.setFont(font)
    
    self.new_horlay_2.addWidget(self.new_varName_lb)
    self.new_varName_ln = QtGui.QLineEdit(self.new_tab)
    self.new_varName_ln.setEnabled(False)
    self.new_varName_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.new_varName_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.new_varName_ln.setPalette(palette)
    self.new_varName_ln.setFrame(False)
    self.new_varName_ln.setObjectName(_fromUtf8("new_varName_ln"))
    self.new_varName_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.new_varName_ln.setFont(font)
    self.new_horlay_2.addWidget(self.new_varName_ln)
    self.new_button_1 = QtGui.QToolButton(self.new_tab)
    self.new_button_1.setEnabled(False)
    self.new_button_1.setMinimumSize(QtCore.QSize(27, 27))
    self.new_button_1.setMaximumSize(QtCore.QSize(27, 27))
    self.new_button_1.setText(_fromUtf8(""))
    self.new_button_1.setIcon(icon1)
    self.new_button_1.setIconSize(QtCore.QSize(27, 27))
    self.new_button_1.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.new_button_1.setAutoRaise(True)
    self.new_button_1.setObjectName(_fromUtf8("new_button_1"))
    self.new_button_1.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.new_horlay_2.addWidget(self.new_button_1)
    spacerItem19 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.new_horlay_2.addItem(spacerItem19)
    self.new_verlay_2.addLayout(self.new_horlay_2)
    self.new_horlay_3 = QtGui.QHBoxLayout()
    self.new_horlay_3.setObjectName(_fromUtf8("new_horlay_3"))
    self.new_longName_lb = QtGui.QLabel(self.new_tab)
    self.new_longName_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.new_longName_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.new_longName_lb.setObjectName(_fromUtf8("new_longName_lb"))
    
    self.new_longName_lb.setFont(font)
    
    self.new_horlay_3.addWidget(self.new_longName_lb)
    self.new_longName_ln = QtGui.QLineEdit(self.new_tab)
    self.new_longName_ln.setEnabled(False)
    self.new_longName_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.new_longName_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.new_longName_ln.setPalette(palette)
    self.new_longName_ln.setFrame(False)
    self.new_longName_ln.setObjectName(_fromUtf8("new_longName_ln"))
    self.new_longName_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.new_longName_ln.setFont(font)
    self.new_horlay_3.addWidget(self.new_longName_ln)
    self.new_button_2 = QtGui.QToolButton(self.new_tab)
    self.new_button_2.setEnabled(False)
    self.new_button_2.setMinimumSize(QtCore.QSize(27, 27))
    self.new_button_2.setMaximumSize(QtCore.QSize(27, 27))
    self.new_button_2.setText(_fromUtf8(""))
    self.new_button_2.setIcon(icon1)
    self.new_button_2.setIconSize(QtCore.QSize(27, 27))
    self.new_button_2.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.new_button_2.setAutoRaise(True)
    self.new_button_2.setObjectName(_fromUtf8("new_button_2"))
    self.new_button_2.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.new_horlay_3.addWidget(self.new_button_2)
    spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.new_horlay_3.addItem(spacerItem20)
    self.new_verlay_2.addLayout(self.new_horlay_3)
    self.new_horlay_4 = QtGui.QHBoxLayout()
    self.new_horlay_4.setObjectName(_fromUtf8("new_horlay_4"))
    self.new_category_lb = QtGui.QLabel(self.new_tab)
    self.new_category_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.new_category_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.new_category_lb.setObjectName(_fromUtf8("new_category_lb"))
    
    self.new_category_lb.setFont(font)
    
    self.new_horlay_4.addWidget(self.new_category_lb)
    self.new_category_ln = QtGui.QLineEdit(self.new_tab)
    self.new_category_ln.setEnabled(False)
    self.new_category_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.new_category_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.new_category_ln.setPalette(palette)
    self.new_category_ln.setFrame(False)
    self.new_category_ln.setObjectName(_fromUtf8("new_category_ln"))
    self.new_category_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.new_category_ln.setFont(font)
    self.new_horlay_4.addWidget(self.new_category_ln)
    self.new_button_3 = QtGui.QToolButton(self.new_tab)
    self.new_button_3.setEnabled(False)
    self.new_button_3.setMinimumSize(QtCore.QSize(27, 27))
    self.new_button_3.setMaximumSize(QtCore.QSize(27, 27))
    self.new_button_3.setText(_fromUtf8(""))
    self.new_button_3.setIcon(icon1)
    self.new_button_3.setIconSize(QtCore.QSize(27, 27))
    self.new_button_3.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.new_button_3.setAutoRaise(True)
    self.new_button_3.setObjectName(_fromUtf8("new_button_3"))
    self.new_button_3.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.new_horlay_4.addWidget(self.new_button_3)
    spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.new_horlay_4.addItem(spacerItem21)
    self.new_verlay_2.addLayout(self.new_horlay_4)
    self.new_horlay_5 = QtGui.QHBoxLayout()
    self.new_horlay_5.setObjectName(_fromUtf8("new_horlay_5"))
    self.new_units_lb = QtGui.QLabel(self.new_tab)
    self.new_units_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.new_units_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.new_units_lb.setObjectName(_fromUtf8("new_units_lb"))
    
    self.new_units_lb.setFont(font)
    
    self.new_horlay_5.addWidget(self.new_units_lb)
    self.new_units_ln = QtGui.QLineEdit(self.new_tab)
    self.new_units_ln.setEnabled(False)
    self.new_units_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.new_units_ln.setMaximumSize(QtCore.QSize(300, 27))
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
    self.new_units_ln.setPalette(palette)
    self.new_units_ln.setFrame(False)
    self.new_units_ln.setObjectName(_fromUtf8("new_units_ln"))
    self.new_units_ln.setStyleSheet(_fromUtf8("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QLineEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.new_units_ln.setFont(font)
    self.new_horlay_5.addWidget(self.new_units_ln)
    self.new_button_4 = QtGui.QToolButton(self.new_tab)
    self.new_button_4.setEnabled(False)
    self.new_button_4.setMinimumSize(QtCore.QSize(27, 27))
    self.new_button_4.setMaximumSize(QtCore.QSize(27, 27))
    self.new_button_4.setText(_fromUtf8(""))
    self.new_button_4.setIcon(icon1)
    self.new_button_4.setIconSize(QtCore.QSize(27, 27))
    self.new_button_4.setPopupMode(QtGui.QToolButton.InstantPopup)
    self.new_button_4.setAutoRaise(True)
    self.new_button_4.setObjectName(_fromUtf8("new_button_4"))
    self.new_button_4.setStyleSheet(_fromUtf8("QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
    "         stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none; /* no border for a flat push button */\n"
    "}"))
    self.new_horlay_5.addWidget(self.new_button_4)
    spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.new_horlay_5.addItem(spacerItem22)
    self.new_verlay_2.addLayout(self.new_horlay_5)
    self.new_horlay_6 = QtGui.QHBoxLayout()
    self.new_horlay_6.setObjectName(_fromUtf8("new_horlay_6"))
    self.new_fillValue_lb = QtGui.QLabel(self.new_tab)
    self.new_fillValue_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.new_fillValue_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.new_fillValue_lb.setObjectName(_fromUtf8("new_fillValue_lb"))
    
    self.new_fillValue_lb.setFont(font)
    
    self.new_horlay_6.addWidget(self.new_fillValue_lb)
    self.new_fillValue_ln = QtGui.QLabel(self.new_tab)
    self.new_fillValue_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.new_fillValue_ln.setMaximumSize(QtCore.QSize(300, 27))
    self.new_fillValue_ln.setObjectName(_fromUtf8("new_fillValue_ln"))
    
    self.new_fillValue_ln.setFont(font)
    
    self.new_horlay_6.addWidget(self.new_fillValue_ln)
    spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.new_horlay_6.addItem(spacerItem23)
    self.new_verlay_2.addLayout(self.new_horlay_6)
    self.new_horlay_7 = QtGui.QHBoxLayout()
    self.new_horlay_7.setObjectName(_fromUtf8("new_horlay_7"))
    self.new_dimensions_lb = QtGui.QLabel(self.new_tab)
    self.new_dimensions_lb.setMinimumSize(QtCore.QSize(120, 27))
    self.new_dimensions_lb.setMaximumSize(QtCore.QSize(120, 27))
    self.new_dimensions_lb.setObjectName(_fromUtf8("new_dimensions_lb"))
    
    self.new_dimensions_lb.setFont(font)
    
    self.new_horlay_7.addWidget(self.new_dimensions_lb)
    self.new_dimensions_ln = QtGui.QLabel(self.new_tab)
    self.new_dimensions_ln.setMinimumSize(QtCore.QSize(300, 27))
    self.new_dimensions_ln.setMaximumSize(QtCore.QSize(300, 27))
    self.new_dimensions_ln.setObjectName(_fromUtf8("new_dimensions_ln"))
    
    self.new_dimensions_ln.setFont(font)
    
    self.new_horlay_7.addWidget(self.new_dimensions_ln)
    spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.new_horlay_7.addItem(spacerItem24)
    self.new_verlay_2.addLayout(self.new_horlay_7)
    self.new_horlay_8 = QtGui.QHBoxLayout()
    self.new_horlay_8.setObjectName(_fromUtf8("new_horlay_8"))
    self.new_verlay_3 = QtGui.QVBoxLayout()
    self.new_verlay_3.setObjectName(_fromUtf8("new_verlay_3"))
    self.new_egadsProcessor_lb = QtGui.QLabel(self.new_tab)
    self.new_egadsProcessor_lb.setMinimumSize(QtCore.QSize(150, 27))
    self.new_egadsProcessor_lb.setMaximumSize(QtCore.QSize(150, 27))
    self.new_egadsProcessor_lb.setObjectName(_fromUtf8("new_egadsProcessor_lb"))
    
    self.new_egadsProcessor_lb.setFont(font)
    
    self.new_verlay_3.addWidget(self.new_egadsProcessor_lb)
    spacerItem25 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.new_verlay_3.addItem(spacerItem25)
    self.new_horlay_8.addLayout(self.new_verlay_3)
    self.new_egadsProcessor_ln = QtGui.QPlainTextEdit(self.new_tab)
    self.new_egadsProcessor_ln.setEnabled(False)
    self.new_egadsProcessor_ln.setMinimumSize(QtCore.QSize(350, 100))
    self.new_egadsProcessor_ln.setMaximumSize(QtCore.QSize(350, 100))
    palette = QtGui.QPalette()
    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    self.new_egadsProcessor_ln.setPalette(palette)
    self.new_egadsProcessor_ln.setFrameShape(QtGui.QFrame.NoFrame)
    self.new_egadsProcessor_ln.setObjectName(_fromUtf8("new_egadsProcessor_ln"))
    self.new_egadsProcessor_ln.setStyleSheet(_fromUtf8("QPlainTextEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}\n"
    "\n"
    "QPlainTextEdit:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    ""))
    self.new_egadsProcessor_ln.setFont(font)
    self.new_horlay_8.addWidget(self.new_egadsProcessor_ln)
    self.new_verlay_2.addLayout(self.new_horlay_8)
    self.new_verlay_1.addLayout(self.new_verlay_2)
    spacerItem26 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.new_verlay_1.addItem(spacerItem26)
    self.new_horlay_1.addLayout(self.new_verlay_1)
    self.new_grid.addLayout(self.new_horlay_1, 0, 1, 2, 1)
    spacerItem27 = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.new_grid.addItem(spacerItem27, 1, 2, 1, 1)
    spacerItem28 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.new_grid.addItem(spacerItem28, 2, 1, 1, 1)
    self.tabWidget.addTab(self.new_tab, "New variables")
    
    self.new_varName_lb.setText(_translate("MainWindow", "Variable name:", None))
    self.new_longName_lb.setText(_translate("MainWindow", "Long name:", None))
    self.new_category_lb.setText(_translate("MainWindow", "Category:", None))
    self.new_units_lb.setText(_translate("MainWindow", "Units:", None))
    self.new_fillValue_lb.setText(_translate("MainWindow", "Fill value:", None))
    self.new_dimensions_lb.setText(_translate("MainWindow", "Dimensions:", None))
    self.new_egadsProcessor_lb.setText(_translate("MainWindow", "EGADS processor:", None))
    
    QtCore.QObject.connect(self.new_listwidget, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), lambda: netcdf_new_var_reading(self))
    all_buttons = self.findChildren(QToolButton)
    for widget in all_buttons:
        if "new_" in widget.objectName():
            QObject.connect(widget, SIGNAL("clicked()"), lambda: modify_attribute_gui(self))


def clear_layout(self, layout):
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtGui.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtGui.QLayout):
            clear_layout(self, item.layout())
        layout.removeItem(item)    


def tab_change(self):
    self.actionAlgorithmsBar.setEnabled(False)
    self.actionDeleteVariableBar.setEnabled(False)
    self.actionVariableAttributesBar.setEnabled(False)
    self.actionPlotBar.setEnabled(False)
    self.actionDisplayBar.setEnabled(False)
    self.actionMigrateVariableBar.setEnabled(False)
    if self.tabWidget.currentIndex() == 1:
        self.actionAlgorithmsBar.setEnabled(True)
        self.actionPlotBar.setEnabled(True)
        try:
            if self.listWidget.currentItem().text() == "":
                self.actionDisplayBar.setEnabled(False)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDeleteVariableBar.setEnabled(False)
            else:
                self.actionDisplayBar.setEnabled(True)
                self.actionVariableAttributesBar.setEnabled(True)
                self.actionDeleteVariableBar.setEnabled(True)
        except AttributeError:
            self.actionDisplayBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionDeleteVariableBar.setEnabled(False)
    elif self.tabWidget.currentIndex() == 2:
        self.actionAlgorithmsBar.setEnabled(True)
        self.actionPlotBar.setEnabled(True)
        try:
            if self.new_listwidget.currentItem().text() == "":
                self.actionDisplayBar.setEnabled(False)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDeleteVariableBar.setEnabled(False)
                self.actionMigrateVariableBar.setEnabled(False)
            else:
                self.actionDisplayBar.setEnabled(True)
                self.actionVariableAttributesBar.setEnabled(True)
                self.actionDeleteVariableBar.setEnabled(True)
                self.actionMigrateVariableBar.setEnabled(True)
        except AttributeError:
            self.actionDisplayBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionDeleteVariableBar.setEnabled(False)
            self.actionMigrateVariableBar.setEnabled(False)
            
            
def netcdf_new_var_reading(self):
    self.new_button_1.setEnabled(True)
    self.new_button_2.setEnabled(True)
    self.new_button_3.setEnabled(True)
    self.new_button_4.setEnabled(True)
    self.actionAlgorithmsBar.setEnabled(True)
    self.actionDeleteVariableBar.setEnabled(True)
    self.actionVariableAttributesBar.setEnabled(True)
    self.actionPlotBar.setEnabled(True)
    self.actionDisplayBar.setEnabled(True)
    self.actionMigrateVariableBar.setEnabled(True)
    self.new_varName_ln.setText("")
    self.new_longName_ln.setText("")
    self.new_category_ln.setText("")
    self.new_units_ln.setText("")
    self.new_fillValue_ln.setText("")
    self.new_dimensions_ln.setText("")
    self.new_egadsProcessor_ln.setPlainText("")
    
    all_lines_edit = self.findChildren(QLineEdit)
    for widget in all_lines_edit:
        if "new_" in widget.objectName():
            widget.setEnabled(False)
    all_text_edit = self.findChildren(QPlainTextEdit)
    for widget in all_text_edit:
        if "new_" in widget.objectName():
            widget.setEnabled(False)
    all_buttons = self.findChildren(QToolButton)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    for widget in all_buttons:
        if "new_" in widget.objectName():
            widget.setIcon(icon)
    for sublist in self.list_of_new_variables_and_attributes:
        try:
            if sublist[1]["var_name"] == self.new_listwidget.currentItem().text():
                break
        except TypeError:
            pass
    self.new_varName_ln.setText(sublist[1]["var_name"])
    self.new_varName_ln.setCursorPosition(0)
    try:
        if sublist[1]["long_name"] != "deleted":
            self.new_longName_ln.setText(' '.join(str(sublist[1]["long_name"]).split()))
            self.new_longName_ln.setCursorPosition(0)
        else:
            self.new_longName_ln.setText("")
    except KeyError:
        self.new_longName_ln.setText("")
    try:
        if sublist[1]["units"] != "deleted":
            self.new_units_ln.setText(str(sublist[1]["units"]))
            self.new_units_ln.setCursorPosition(0)
        else:
            self.new_units_ln.setText("")
    except KeyError:
        self.new_units_ln.setText("")
    try:
        if sublist[1]["Category"] != "deleted":
            if isinstance(sublist[1]["Category"], list):
                category_string = ""
                for string in sublist[1]["Category"]:
                    category_string += string + ", "
                    self.new_category_ln.setText(category_string[:-2])
                else:
                    self.new_category_ln.setText(str(sublist[1]["Category"]))
                self.new_category_ln.setCursorPosition(0)
            else:
                self.new_category_ln.setText("")
    except KeyError:
        self.new_category_ln.setText("")
    try:
        self.new_fillValue_ln.setText(str(sublist[1]["_FillValue"]))
    except KeyError:
        try:
            self.new_fillValue_ln.setText(str(sublist[1]["missing_value"]))
        except KeyError:
            self.new_fillValue_ln.setText("")
    dimensions_str = ""
    i = 0
    try: 
        for key, value in sublist[2].iteritems():
            if i == 0:
                dimensions_str = str(value) + " (" + key + ")"
            else: 
                dimensions_str = dimensions_str + " x " + str(value) + " (" + key + ")"
            i += 1
        self.new_dimensions_ln.setText(dimensions_str)
    except AttributeError:
        self.new_dimensions_ln.setText("")
    try:
        self.new_egadsProcessor_ln.setPlainText(str(sublist[1]["Processor"]))
    except KeyError:
        self.new_egadsProcessor_ln.setPlainText("")
       
       
       
       
