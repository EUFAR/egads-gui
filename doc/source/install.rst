=============
Installation
=============

The latest version of the EGADS GUI can be obtained from https://github.com/EUFAR/egads-gui


*************
Prerequisites
*************

The use of the EGADS GUI requires the following packages:

* Python 2.7.10 or newer. Available at https://www.python.org/
* PyQt 5.8 or newer. Available at https://www.riverbankcomputing.com/software/pyqt/download5
* EGADS 0.8.8 or newer. Available at https://pypi.python.org/pypi/egads
* Matplotlib 2.0.0 or newer. Available at https://pypi.python.org/pypi/matplotlib
* Babel 2.3.4 or newer. Available at https://pypi.python.org/pypi/Babel

.. NOTE::
  It is recommended to use Anaconda (for Linux and Windows) - PyQt5 is included by default in the Anaconda distribution.
  Available at https://www.anaconda.com/download/#download



*************
Compatibility
*************

The EGADS GUI has been tested on Linux and Windows. Even if it has not been tested on MacOS, it should be compatible with the Apple system.


************
Installation
************

The EGADS GUI is actually available as a common Python script, thus it doesn't need any particular installation. To use it, the package must be downloaded and uncompressed somewhere on the hard drive, and the script executed with the usual command ``python egads_gui.py`` from a terminal launched in the EGADS GUI directory. This version can be executed on any version of Linux, Windows and MacOS as soon as prerequisites are installed and working.

In the future, a stand-alone version will be available, embedded or not the last version of EGADS core.

To learn how to install EGADS, please read the EGADS documentation available at the following places: https://github.com/EUFAR/egads/blob/master/Documentation/ & http://egads.readthedocs.io/


*******
Testing
*******

No test system has been introduced at this time.


***
Log
***

A logging system has been integrated in the EGADS GUI since the version 0.7.0. By default, the output file is available in the GUI directory and the logging level has been set to DEBUG. Options for logging level and location are set in a config_file ``egads_gui.ini`` and can be change directly through the Option window in the GUI.

Actual options to control the logging system are for now:

* ``level``: the logging level ( ``DEBUG``, ``INFO``, ``WARNING``, ``CRITICAL``, ``ERROR`` ).
* ``path``: the path of the file containing all logs.

Once the logging level has been changed in the Option window (saved and confirmed by clicking on Ok), the logging file will record new messages based on the logging level. On the contrary, if the path is modified, the GUI has to be restarted to take into account the new path.
