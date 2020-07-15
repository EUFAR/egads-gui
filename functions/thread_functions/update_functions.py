import logging
import time
from PyQt5 import QtCore
from distutils.version import LooseVersion
from functions.utils import set_size


class CheckEGADSGuiUpdateOnline(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal()

    def __init__(self, gui_version, frozen, system, installed):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - __init__')
        self.gui_version = gui_version
        self.frozen = frozen
        self.system = system
        self.installed = installed

    def run(self):
        logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run')
        url = 'https://api.github.com/repos/eufarn7sp/egads-gui/releases'
        try:
            import requests
            json_object = requests.get(url=url, timeout=5).json()
            lineage_list = []
            for egads_package in json_object:
                if egads_package['target_commitish'] == 'Lineage':
                    package_list = {'sources': None, 'windows_setup': None, 'windows_binaries': None,
                                    'linux_binaries': None}
                    for asset in egads_package['assets']:
                        if 'sources' in asset['name']:
                            package_list['sources'] = asset['browser_download_url']
                        elif 'windows_setup' in asset['name']:
                            package_list['windows_setup'] = asset['browser_download_url']
                        elif 'windows_binaries' in asset['name']:
                            package_list['windows_binaries'] = asset['browser_download_url']
                        elif 'linux_binaries' in asset['name']:
                            package_list['linux_binaries'] = asset['browser_download_url']
                    lineage_list.append([egads_package['tag_name'], package_list])
            lineage_list = sorted(lineage_list)
            if lineage_list:
                if LooseVersion(self.gui_version) < LooseVersion(lineage_list[-1][0]):
                    if self.frozen:
                        if self.system == 'Windows':
                            if self.installed:
                                if lineage_list[-1][1]['windows_setup'] is not None:
                                    self.finished.emit(lineage_list[-1][1]['windows_setup'])
                                else:
                                    logging.debug(
                                        'gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new '
                                        'version')
                                    self.finished.emit('no new version')
                            else:
                                if lineage_list[-1][1]['windows_binaries'] is not None:
                                    self.finished.emit(lineage_list[-1][1]['windows_binaries'])
                                else:
                                    logging.debug(
                                        'gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new '
                                        'version')
                                    self.finished.emit('no new version')
                        elif self.system == 'Linux':
                            if lineage_list[-1][1]['linux_binaries'] is not None:
                                self.finished.emit(lineage_list[-1][1]['linux_binaries'])
                            else:
                                logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new '
                                              'version')
                                self.finished.emit('no new version')
                        else:
                            logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new '
                                          'version, present system not a windows or linux system')
                            self.finished.emit('no new version')
                    else:
                        if lineage_list[-1][1]['sources'] is not None:
                            self.finished.emit(lineage_list[-1][1]['sources'])
                        else:
                            logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new '
                                          'version')
                            self.finished.emit('no new version')
                else:
                    logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                    self.finished.emit('no new version')
            else:
                logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                self.finished.emit('no new version')
        except ImportError:
            logging.exception('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - requests is not available')
        except Exception:
            logging.exception('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - internet connection '
                              'error - url ' + url)

    def stop(self):
        logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - stop')
        self.terminate()


class CheckEGADSUpdateOnline(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)

    def __init__(self, version):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - __init__')
        self.version = version

    def run(self):
        logging.debug('gui - file_functions.py - CheckEGADSUpdateOnline - run')
        url = 'https://api.github.com/repos/eufarn7sp/egads/releases'
        try:
            import requests
            json_object = requests.get(url=url, timeout=5).json()
            lineage_list = []
            for egads_package in json_object:
                if 'Lineage' in egads_package['name']:
                    lineage_list.append([egads_package['tag_name'], egads_package['assets'][0]['browser_download_url']])
            lineage_list = sorted(lineage_list)
            if lineage_list:
                if LooseVersion(self.version) < LooseVersion(lineage_list[-1][0]):
                    self.finished.emit(lineage_list[-1][1])
                else:
                    logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                    self.finished.emit('no new version')
            else:
                logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - no new version')
                self.finished.emit('no new version')
        except ImportError:
            logging.exception('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - requests is not available')
            self.error.emit('requests is not available')
        except Exception:
            logging.exception('gui - file_functions.py - CheckEGADSGuiUpdateOnline - run - internet connection '
                              'error - url ' + url)
            self.error.emit('internet connection error')

    def stop(self):
        logging.debug('gui - file_functions.py - CheckEGADSGuiUpdateOnline - stop')
        self.terminate()


class CheckEGADSVersion(QtCore.QThread):
    version_issue = QtCore.pyqtSignal(dict)

    def __init__(self, egads_version, egads_branch, min_egads_version, gui_branch):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - CheckEGADSVersion - __init__')
        self.egads_version = egads_version
        self.min_egads_version = min_egads_version
        self.egads_branch = egads_branch
        self.gui_branch = gui_branch

    def run(self):
        logging.debug('gui - file_functions.py - CheckEGADSVersion - run')
        time.sleep(1)
        version_issue = {'version': True, 'branch': True}
        if LooseVersion(self.egads_version) < LooseVersion(self.min_egads_version):
            logging.info('gui - file_functions.py - CheckEGADSVersion - run - an old version of EGADS has been '
                         'found: ' + self.egads_version)
            version_issue['version'] = False
        if self.egads_branch != self.gui_branch:
            logging.info('gui - file_functions.py - CheckEGADSVersion - run - a different branch of EGADS has been '
                         'found: ' + self.egads_branch)
            version_issue['branch'] = False
        if version_issue:
            self.version_issue.emit(version_issue)

    def stop(self):
        logging.debug('gui - file_functions.py - CheckEGADSVersion - stop')
        self.terminate()


class DownloadFile(QtCore.QThread):
    download_update = QtCore.pyqtSignal(list)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal()

    def __init__(self, url_name, update_file):
        QtCore.QThread.__init__(self)
        logging.info('file_functions.py - DownloadFile - __init__ - url_name ' + str(url_name))
        self.url_name = url_name
        self.update_file = update_file
        self.filename = self.url_name[self.url_name.rfind("/") + 1:]
        self.cancel = False

    def run(self):
        logging.debug('file_functions.py - DownloadFile - run')
        download_text = 'Downloading %s at %s'
        pre_download_text = 'Downloading %s'
        self.download_update.emit([0, pre_download_text % self.filename])
        opened_file = open(self.update_file, 'wb')
        try:
            import requests
            opened_url = requests.get(self.url_name, stream=True)
            total_file_size = int(opened_url.headers['Content-length'])
            buffer_size = 8192
            file_size = 0
            start = time.time()
            for chunk in opened_url.iter_content(chunk_size=buffer_size):
                if self.cancel:
                    opened_file.close()
                    break
                opened_file.write(chunk)
                file_size += len(chunk)
                try:
                    download_speed = set_size(file_size / (time.time() - start)) + '/s'
                except ZeroDivisionError:
                    download_speed = '0b/s'
                self.download_update.emit([round(file_size * 100 / total_file_size),
                                           download_text % (self.filename, download_speed)])
            opened_file.close()
            if not self.cancel:
                logging.debug('file_functions.py - DownloadFile - run - download finished')
                self.download_done.emit()
            else:
                logging.debug('file_functions.py - DownloadFile - run - download canceled')
        except Exception:
            logging.exception('file_functions.py - DownloadFile - run - connexion issue ; self.url_name '
                              + self.url_name)
            opened_file.close()
            self.download_failed.emit()

    def cancel_download(self):
        logging.debug('file_functions.py - DownloadFile - cancel_download')
        self.cancel = True

    def stop(self):
        logging.debug('file_functions.py - DownloadFile - stop')
        self.terminate()