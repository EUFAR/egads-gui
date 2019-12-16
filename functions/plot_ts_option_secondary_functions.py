import logging
from functions.utils import populate_combobox
from functions.material_functions import line_style_list, marker_style_dict
from PyQt5 import QtCore, QtGui, QtWidgets


def update_ts_slider_value(self, val):
    logging.debug('gui - plot_ts_option_decondary_functions.py - update_ts_slider_value')
    object_name = self.sender().objectName()[-1:]
    self.findChild(QtWidgets.QLabel, 'slider_lb_' + str(object_name)).setText(str(float(val) / 100))


def activate_ts_grid_options(self):
    logging.debug('gui - plot_ts_option_decondary_functions.py - activate_ts_grid_options')
    self.pw_figureOptions_cb_9[int(self.sender().objectName()[22:])].setEnabled(self.sender().isChecked())
    self.pw_figureOptions_cb_10[int(self.sender().objectName()[22:])].setEnabled(self.sender().isChecked())
    self.pw_figureOptions_ln_10[int(self.sender().objectName()[22:])].setEnabled(self.sender().isChecked())
    self.pw_figureOptions_cb_9[int(self.sender().objectName()[22:])].setCurrentIndex(3)
    self.pw_figureOptions_cb_10[int(self.sender().objectName()[22:])].setCurrentIndex(0)
    self.pw_figureOptions_ln_10[int(self.sender().objectName()[22:])].setText('0.5')


def activate_ts_line_color(self):
    logging.debug('gui - plot_ts_option_decondary_functions.py - activate_ts_line_color')
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


def activate_ts_opacity_options(self):
    logging.debug('gui - plot_ts_option_decondary_functions.py - activate_ts_opacity_options')
    self.pw_plotOptions_ln_2[int(self.sender().objectName()[20:])].setEnabled(self.sender().isChecked())
    self.pw_plotOptions_lb_7[int(self.sender().objectName()[20:])].setEnabled(self.sender().isChecked())
    self.pw_plotOptions_ln_2[int(self.sender().objectName()[20:])].setText('100')


def activate_ts_line_style(self, val):
    logging.debug('gui - plot_ts_option_decondary_functions.py - activate_ts_line_style')
    self.pw_plotOptions_cb_1[int(val.objectName()[20:])].clear()
    if "pw_plotOptions_rb_1" in val.objectName():
        populate_combobox(self.pw_plotOptions_cb_1[int(val.objectName()[20:])], line_style_list(), False, 'Solid')
        self.pw_plotOptions_ln_1[int(val.objectName()[20:])].setText('1.25')
    else:
        populate_combobox(self.pw_plotOptions_cb_1[int(val.objectName()[20:])],
                          sorted(list(marker_style_dict().keys())),
                          False)
        self.pw_plotOptions_ln_1[int(val.objectName()[20:])].setText('10')
