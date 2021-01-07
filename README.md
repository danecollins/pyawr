# pyawr - AWR Scripting in Python

**Python utilities for Microwave Office from AWR**

It is possible to write scripts for AWRDE in languages other than Visual Basic such as Python.  This package implements tools to make working with Microwave Office more pythonic.  It is recommended that you use Python 3.7 or later with AWRDE but earlier Python 3 versions may work.

For help getting your python environment setup for COM, see [AWR Scripting in Python](http://kb.awr.com/display/SCRIPTS/AWR+Scripting+in+Python)

Requirements for this package are defined in requirements.txt.

### Installation

To install this package use:

    > python setup.py install

or,

    > pip install .

Next, we will install the packages required by pyawr which include Numpy and Pandas with:

	> pip install -r requirements.txt


### Testing your installation

Here is a very simple python program that connects to AWRDE and writes out all the models in the software:

	import pyawr.mwoffice as mwo
	awrde = mwo.CMWOffice()
	for model in awrde.Models:
		print(model.Name)
		
### Why pyawr?

The win32com package contains everything needed to connect to AWRDE from PYthon but since Python is not a strongly typed language, editors do not have sufficient information to provide advanced functionality such as IntelliSense.  Lack of IntelliSense makes it very difficult to work with the AWR COM interface.  To solve this problem, we have created an interface layer on top of win32com which adds type information for the AWR COM interface.  With this interface layer, editor, such as Visual Studio Code, can do a reasonable job of providing hints.

In addition to the layer over win32com, the pyawr package also provides a set of helper functions to simplify some of the common AWRDE interactions.

### Using pyawr

Usage information and examples are available on the AWR KnowledgeBase, see [AWR Scripting in Python](http://kb.awr.com/display/SCRIPTS/AWR+Scripting+in+Python)

