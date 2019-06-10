=============
Installation
=============

The latest version of the EGADS GUI can be obtained from https://github.com/EUFAR/egads-gui/tree/Lineage


*************
Prerequisites
*************

The use of the EGADS GUI requires the following packages:

* Python 3.5.4 or newer. Available at https://www.python.org/
* PyQt 5.11.3 or newer. Available at https://www.riverbankcomputing.com/software/pyqt/download5
* EGADS 0.9.3 or newer. Available at https://pypi.python.org/pypi/egads
* Matplotlib 2.2.2 or newer. Available at https://pypi.python.org/pypi/matplotlib
* Cartopy 0.17.0 or newer. Available at https://pypi.org/project/Cartopy/
* Requests 2.18.4 or newer. Optional, only for update checking. Available at https://pypi.org/project/requests/


*************
Compatibility
*************

The EGADS GUI has been tested on Linux and Windows. Even if it has not been tested on MacOS, it should be compatible with the Apple system.


************
Installation
************

The EGADS GUI is actually available as a common Python script, thus it doesn't need any particular installation. To use it, the package must be downloaded and uncompressed somewhere on the hard drive, and the script executed with the usual command ``python egads_gui.py`` from a terminal launched in the EGADS GUI directory. This version can be executed on any version of Linux, Windows and MacOS as soon as prerequisites are installed and working.

In the future, a stand-alone version will be available, embedding or not the last version of EGADS core.

To learn how to install EGADS, please read the EGADS documentation available at the following places: https://github.com/EUFAR/egads/tree/Lineage/Documentation & https://egads.readthedocs.io/en/lineage/


*******
Testing
*******

No test system has been introduced at this time.


*******
Options
*******

Since version 0.10.0, an .ini file has been added to EGADS GUI to welcome few options: log level and path, automatic check for a new EGADS GUI version on GitHub, and few other options. If the file is not present in EGADS GUI directory, when importing, EGADS GUI will create it automatically with default options. The modification of the file is made through the option window of the GUI.


***
Log
***

A logging system has been integrated in the EGADS GUI since the version 0.7.0. By default, the output file is available in the GUI directory and the logging level has been set to DEBUG. Options for logging level and location are set in a config_file ``egads_gui.ini`` and can be change directly through the Option window in the GUI.

Actual options to control the logging system are for now:

* ``level``: the logging level ( ``DEBUG``, ``INFO``, ``WARNING``, ``CRITICAL``, ``ERROR`` ).
* ``path``: the path of the file containing all logs.

Once the logging level has been changed in the Option window (saved and confirmed by clicking on Ok), the logging file will record new messages based on the logging level. On the contrary, if the path is modified, the GUI has to be restarted to take into account the new path.


Update
******
Since version 0.11.0, EGADS GUI can check for an update on GitHub. The check system is launched in a separate thread and can run automatically at each startup if the option to do so has been set accordingly. To install the update, the user has to follow the install instructions found in actual document. The module Requests is optional for EGADS GUI but is mandatory to check for an update.
