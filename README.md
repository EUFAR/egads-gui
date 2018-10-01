Version:
-------

EGADS GUI Lineage 0.10.0 (Python 3).


Developments:
-------------

As the EUFAR project ended the 31st of January 2018, developments involving EGADS GUI are now done in a new branch and the current version of EGADS GUI is called EGADS GUI Lineage. It is developed and maintained by Olivier Henry and is not developed under the scope of EUFAR. Merging of the Master and Lineage branch can happen in the next EUFAR project.


Project Overview:
-----------------

EGADS (EUFAR General Airborne Data-processing Software) is a Python-based toolbox for processing airborne atmospheric data. EGADS provides a framework for researchers to apply expert-contributed algorithms to data files, and acts as a platform for data intercomparison. Algorithms in EGADS will be contributed by members of the EUFAR Expert Working Group if they are found to be mature and well-established in the scientific community.

EGADS GUI is a Python-based graphical user interface dedicated to EGADS. The project is still in early development and is not intended to be used in a production environment. But it can be tested if a user wants to have an overview of the possibilities. 

EGADS and EGADS GUI are under development by EUFAR (European Facility for Airborne Research), an Integrating Activity funded by the European Commission. Specifically, the networking activity Standards & Protocols within EUFAR is responsible for development of toolbox, in addition to developing standards for use within the EUFAR community. A compilation of these standards and other Standards & Protocols products is available on the different Standards & Protocols webpages: 
* Standards & Protocols presentation: http://www.eufar.net/cms/standards-and-protocols/
* Standards & Protocols good practices: http://www.eufar.net/cms/good-practices/
* Standards & Protocols glossary: http://www.eufar.net/cms/glossary/
* Standards & Protocols tools: http://www.eufar.net/software-tools/list-matrix ; search for ASMM, EMC, EGADS-CORE and EGADS-GUI
  

More Information:
-----------------

Not yet.


Features:
---------

* read/write NetCDF files (not yet)
* read/write NASA/Ames files (not yet)
* conversion between different file format (not yet)
* use of algorithms (not yet)
* creation of new algorithms (not yet)
* display/plot/print data (not yet)


Installation:
-------------

Actually, EGADS GUI is a simple python script. Just open a terminal in the EGADS GUI directory and launch the script as usual: python egads_gui.py.

Do not forget to install dependancies:
* PyQt5 (5.10 or newer)
* EGADS Lineage (0.9.1 or newer)
* Numpy (1.14 or newer)
* Not necessary yet: Requests (2.18.4 or newer), optional, only for update checking)
* Matplotlib (2.0 or newer)
* Cartopy (0.16 or newer)
* Pillow (5.2 or newer, optional, only to save a figure in jpeg format)


Documentation:
--------------

Not yet.
