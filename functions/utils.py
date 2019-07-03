import os
import configparser
import logging
import egads
import datetime
import inspect
import pathlib
from PyQt5 import QtCore, QtGui, QtWidgets


def clear_layout(layout):
    logging.debug('gui - utils.py - clear_layout')
    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)


def create_option_file(main_path):
    ini_file = open(os.path.join(main_path, 'egads_gui.ini'), 'w')
    config_dict = configparser.ConfigParser()
    config_dict.add_section('LOG')
    config_dict.add_section('SYSTEM')
    config_dict.add_section('PLOTS')
    config_dict.add_section('OPTIONS')
    config_dict.set('LOG', 'level', 'INFO')
    config_dict.set('LOG', 'path', str(main_path))
    config_dict.set('SYSTEM', 'read_as_float', 'False')
    config_dict.set('SYSTEM', 'replace_fill_value', 'False')
    config_dict.set('SYSTEM', 'switch_fill_value', 'False')
    config_dict.set('PLOTS', 'same_unit_plot', '2')
    config_dict.set('PLOTS', 'subplot_disposition', '0')
    config_dict.set('OPTIONS', 'check_update', 'False')
    config_dict.write(ini_file)
    ini_file.close()


def create_logging_handlers(config_dict, filename):
    log_filename = os.path.join(config_dict.get('LOG', 'path'), filename)
    logging.getLogger('').handlers = []
    logging.basicConfig(filename=log_filename,
                        level=getattr(logging, config_dict.get('LOG', 'level')),
                        filemode='w',
                        format='%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def str_format(color, style=''):
    logging.debug('gui - utils.py - str_format')
    _color = QtGui.QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)
    _format = QtGui.QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QtGui.QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    return _format


STYLES = {
        'keyword': str_format('blue'),
        'operator': str_format('red'),
        'brace': str_format('darkGray'),
        'defclass': str_format('black', 'bold'),
        'string': str_format('magenta'),
        'string2': str_format('darkMagenta'),
        'comment': str_format('darkGreen', 'italic'),
        'self': str_format('black', 'italic'),
        'numbers': str_format('brown')}


class Highlighter(QtGui.QSyntaxHighlighter):
    """ the following code is based on the work of David Boddie
        https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
    """

    keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'print',
        'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False']

    operators = [
        '=', '==', '!=', '<', '<=', '>', '>=',
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        '\+=', '-=', '\*=', '/=', '\%=',
        '\^', '\|', '\&', '\~', '>>', '<<']

    braces = ['\{', '\}', '\(', '\)', '\[', '\]']

    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        self.tri_single = (QtCore.QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QtCore.QRegExp('"""'), 2, STYLES['string2'])

        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                  for w in Highlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator'])
                  for o in Highlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
                  for b in Highlighter.braces]

        rules += [
            (r'\bself\b', 0, STYLES['self']),
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),
            (r'#[^\n]*', 0, STYLES['comment']),
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers'])]

        self.rules = [(QtCore.QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, string_format in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, string_format)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)

    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)

        if self.currentBlockState() == in_state:
            return True
        else:
            return False


def create_algorithm_dict():
    logging.debug('gui - utils.py - create_algorithm_dict')
    algorithm_list = {}
    rep_list = [item for item in dir(egads.algorithms) if '__' not in item]
    rep_list.remove('egads')
    rep_list.remove('user')
    for rep in rep_list:
        tmp = [item for item in dir(getattr(egads.algorithms, rep)) if '__' not in item]
        for algo in tmp:
            try:
                _ = getattr(getattr(egads.algorithms, rep), algo)().run
                item = str(inspect.getmodule(getattr(getattr(egads.algorithms, rep), algo)))
                algorithm_list[rep + ' - ' + algo] = {'name': algo, 'folder': rep, 'user': False,
                                                      'path': str(pathlib.Path(item[item.find(' from ') + 7: -2])),
                                                      'method': getattr(getattr(egads.algorithms, rep), algo)}
            except (TypeError, AttributeError):
                pass
    rep_list = [item for item in dir(egads.algorithms.user) if '__' not in item]
    rep_list.remove('egads')
    for rep in rep_list:
        tmp = [item for item in dir(getattr(egads.algorithms.user, rep)) if '__' not in item]
        for algo in tmp:
            try:
                _ = getattr(getattr(egads.algorithms.user, rep), algo)().run
                item = str(inspect.getmodule(getattr(getattr(egads.algorithms.user, rep), algo)))
                algorithm_list[rep + ' - ' + algo] = {'name': algo, 'folder': rep, 'user': True,
                                                      'path': str(pathlib.Path(item[item.find(' from ') + 7: -2])),
                                                      'method': getattr(getattr(egads.algorithms.user, rep), algo)}
            except (TypeError, AttributeError):
                pass
    return algorithm_list


def prepare_algorithm_categories(algorithm_list):
    logging.debug('gui - utils.py - prepare_algorithm_categories')
    algorithm_categories = []
    for key in algorithm_list.keys():
        algorithm_categories.append(key[:key.find(' - ')].title())
    return sorted(list(dict.fromkeys(algorithm_categories)))


def prepare_output_categories(algorithm_list):
    logging.debug('gui - utils.py - prepare_output_categories')
    output_categories = []
    for key, algo_dict in algorithm_list.items():
        output_metadata = algo_dict['method']().output_metadata
        if isinstance(output_metadata, list):
            for metadata in output_metadata:
                if isinstance(metadata['Category'], list):
                    for category in metadata['Category']:
                        output_categories.append(category)
                else:
                    output_categories.append(metadata['Category'])
        else:
            if isinstance(output_metadata['Category'], list):
                for category in output_metadata['Category']:
                    output_categories.append(category)
            else:
                output_categories.append(output_metadata['Category'])
    output_categories = sorted(list(dict.fromkeys(output_categories)))
    try:
        output_categories.remove('')
    except ValueError:
        pass
    return output_categories


def create_datestring():
    logging.debug('gui - utils.py - create_datestring')
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    date_string = year + '-' + month + '-' + day + ' ' + hour + ':' + minute
    return date_string


def prepare_long_string(string, length, space_num):
    logging.debug('gui - utils.py - prepare_long_string')
    new_string = ''
    i = 0
    while len(string) > length:
        if i > 0:
            new_string += ' ' * space_num
        new_string += string[:length] + '\n'
        string = string[length:]
        i += 1
    else:
        if i > 0:
            new_string += ' ' * space_num + string
        else:
            new_string += string
    return new_string


def check_string_max_length(string_list):
    logging.debug('gui - utils.py - check_string_max_length')
    max_length = 0
    for string in string_list:
        if len(string) > max_length:
            max_length = len(string)
    return max_length


def write_algorithm(filename, string, category, author):
    logging.debug('gui - utils.py - write_algorithm : filename ' + str(filename) + ', category' + str(category)
                  + ', author ' + str(author) + ', string ' + str(string))
    category = category.lower()
    algorithm_path = egads.__path__[0] + '/algorithms/user/' + category
    addendum = '    from .' + filename + ' import *'
    if os.path.isdir(algorithm_path):
        with open(algorithm_path + '/__init__.py', 'r') as in_file:
            init_file = in_file.readlines()
        import_num, add_num, exist = 0, 0, False
        for line in init_file:
            if '    from ' in line:
                import_num += 1
            if addendum in line:
                exist = True

        if import_num == 0:
            with open(algorithm_path + '/__init__.py', 'w') as out_file:
                for line in init_file:
                    if 'try:' in line:
                        line = line + addendum + '\n'
                    out_file.write(line)
        else:
            if not exist:
                with open(algorithm_path + '/__init__.py', 'w') as out_file:
                    for line in init_file:
                        if '    from ' in line:
                            add_num += 1
                            if add_num == import_num:
                                line = line + addendum + '\n'
                        out_file.write(line)
        algorithm_file = open(algorithm_path + '/' + filename + '.py', 'w')
        algorithm_file.write(string)
        algorithm_file.close()
    else:
        os.makedirs(algorithm_path)
        init_string = ('__author__ = "' + author + '"\n'
                       + '__date__ = "' + create_datestring() + '"\n'
                       + '__version__ = "1.0"\n\n'
                       + 'import logging\n\n'
                       + 'try:\n'
                       + '    from .' + filename + ' import *\n'
                       + "    logging.info('egads [user/" + category + "] algorithms have been loaded')\n"
                       + 'except Exception:\n'
                       + "    logging.error('an error occured during the loading of a [user/" + category
                       + "] algorithm')\n")
        init_file = open(algorithm_path + '/__init__.py', 'w')
        init_file.write(init_string)
        init_file.close()

        init_addendum = 'import egads.algorithms.user.' + category
        with open(egads.__path__[0] + '/algorithms/user/__init__.py', 'r') as in_file:
            init_file = in_file.readlines()
        import_num, add_num = 0, 0
        for line in init_file:
            if 'import ' in line:
                import_num += 1
        with open(egads.__path__[0] + '/algorithms/user/__init__.py', 'w') as out_file:
            for line in init_file:
                if 'import ' in line:
                    add_num += 1
                    if add_num == import_num:
                        line = line + '\n' + init_addendum
                out_file.write(line)

        algorithm_file = open(algorithm_path + '/' + filename + '.py', 'w')
        algorithm_file.write(string)
        algorithm_file.close()


def humansize(nbytes):
    logging.debug('gui - utils.py - humansize : nbytes ' + str(nbytes))
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    if nbytes == 0:
        return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def populate_combobox(combobox, item_list, make_choice=True, set_index=None):
    logging.debug('gui - utils.py - populate_combobox')
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


def transparency_hexa_dict_function():
    logging.debug('gui - utils.py - transparency_hexa_dict_function')
    hexa_dict = {100: 'FF',
                 99: 'FC',
                 98: 'FA',
                 97: 'F7',
                 96: 'F5',
                 95: 'F2',
                 94: 'F0',
                 93: 'ED',
                 92: 'EB',
                 91: 'E8',
                 90: 'E6',
                 89: 'E3',
                 88: 'E0',
                 87: 'DE',
                 86: 'DB',
                 85: 'D9',
                 84: 'D6',
                 83: 'D4',
                 82: 'D1',
                 81: 'CF',
                 80: 'CC',
                 79: 'C9',
                 78: 'C7',
                 77: 'C4',
                 76: 'C2',
                 75: 'BF',
                 74: 'BD',
                 73: 'BA',
                 72: 'B8',
                 71: 'B5',
                 70: 'B3',
                 69: 'B0',
                 68: 'AD',
                 67: 'AB',
                 66: 'A8',
                 65: 'A6',
                 64: 'A3',
                 63: 'A1',
                 62: '9E',
                 61: '9C',
                 60: '99',
                 59: '96',
                 58: '94',
                 57: '91',
                 56: '8F',
                 55: '8C',
                 54: '8A',
                 53: '87',
                 52: '85',
                 51: '82',
                 50: '80',
                 49: '7D',
                 48: '7A',
                 47: '78',
                 46: '75',
                 45: '73',
                 44: '70',
                 43: '6E',
                 42: '6B',
                 41: '69',
                 40: '66',
                 39: '63',
                 38: '61',
                 37: '5E',
                 36: '5C',
                 35: '59',
                 34: '57',
                 33: '54',
                 32: '52',
                 31: '4F',
                 30: '4D',
                 29: '4A',
                 28: '47',
                 27: '45',
                 26: '42',
                 25: '40',
                 24: '3D',
                 23: '3B',
                 22: '38',
                 21: '36',
                 20: '33',
                 19: '30',
                 18: '2E',
                 17: '2B',
                 16: '29',
                 15: '26',
                 14: '24',
                 13: '21',
                 12: '1F',
                 11: '1C',
                 10: '1A',
                 9: '17',
                 8: '14',
                 7: '12',
                 6: '0F',
                 5: '0D',
                 4: '0A',
                 3: '08',
                 2: '05',
                 1: '03',
                 0: '00'}
    return hexa_dict
