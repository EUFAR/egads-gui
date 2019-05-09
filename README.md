Version:
-------

EGADS Lineage GUI 0.11.0 (Python 3).


Developments:
-------------

As the EUFAR project ended the 31st of January 2018, developments involving EGADS GUI are now done in a new branch and the current version of EGADS GUI is called EGADS Lineage GUI. It is developed and maintained by Olivier Henry and is not developed under the scope of EUFAR. Merging of the Master and Lineage branch can happen in the next EUFAR project.


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

* read/write NetCDF files
* read/write NASA/Ames files (not yet)
* conversion between different file format (not yet)
* use of algorithms
* creation of new algorithms
* display/plot/print data
* batch processing (not yet)


Installation:
-------------

Actually, EGADS GUI is a simple python script. Just open a terminal in the EGADS GUI directory and launch the script as usual: python egads_gui.py.

Do not forget to install dependancies:
* Python (3.5.4 or newer)
* PyQt5 (5.11.3 or newer)
* EGADS Lineage (0.9.3 or newer)
* Matplotlib (2.2.2 or newer)
* Cartopy (0.17 or newer)
* Requests (2.18.4 or newer, optional, only to check updates if the user activates the option)


Documentation:
--------------

The documentation of EGADS Lineage GUI is available as a PDF in the Documentation folder or on Read The Docs (https://egads-gui.readthedocs.io/en/lineage/).
