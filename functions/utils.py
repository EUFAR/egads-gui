import os
import configparser
import logging
import egads
import datetime
import importlib
from PyQt5 import QtCore, QtGui


def create_option_file(main_path):
    ini_file = open(os.path.join(main_path, 'egads_gui.ini'), 'w')
    config_dict = configparser.ConfigParser()
    config_dict.add_section('LOG')
    config_dict.add_section('OPTIONS')
    config_dict.set('LOG', 'level', 'DEBUG')
    config_dict.set('LOG', 'path', '')
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


def prepare_algorithm_categories(algorithm_list):
    algorithm_categories = []
    for key, _ in algorithm_list.items():
        algorithm_categories.append(str(key).title())
    return sorted(algorithm_categories)


def prepare_output_categories(algorithm_list):
    output_categories = []
    for key, value in algorithm_list.items():
        if isinstance(value, list):
            for item in value:
                try:
                    output_metadata = getattr(getattr(egads.algorithms, key), item)().output_metadata
                except AttributeError:
                    output_metadata = getattr(getattr(egads.algorithms.user, key), item)().output_metadata
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
        else:
            try:
                output_metadata = getattr(getattr(egads.algorithms, value), value)().output_metadata
            except AttributeError:
                output_metadata = getattr(getattr(egads.algorithms.user, value), value)().output_metadata
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
    output_categories.remove('')
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
    logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - check_string_max_length')
    max_length = 0
    for string in string_list:
        if len(string) > max_length:
            max_length = len(string)
    return max_length


def write_algorithm(filename, string, category, author):
    logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - write_algorithm : filename ' + str(filename)
                  + ', category' + str(category) + ', author ' + str(author) + ', string ' + str(string))
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


def reload_user_folders():
    logging.debug('gui - utils.py - reload_user_folders')
    importlib.reload(egads.algorithms.user)
    folder_list = []
    for item in os.walk(egads.__path__[0] + '/algorithms/user'):
        index = item[0].find('user')
        if item[0][index + 5:]:
            if 'file_templates' not in item[0][index + 5:]:
                folder_list.append(item[0][index + 5:])
    for folder in folder_list:
        if '__pycache__' not in folder:
            importlib.reload(getattr(egads.algorithms.user, folder))


def humansize(nbytes):
    logging.debug('gui - gui_functions.py - humansize : nbytes ' + str(nbytes))
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
