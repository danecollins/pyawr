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

### Some Important Things to Note

##### Ranges

In many cases we have tried to be more pythonic in our interface so we have implemented capabilities such as ranges on collections with zero-based indeces which is standard in python rather than the one-based index in the COM API.  This means that both of these would get the same schematic:

		awrde.Project.Schematics.Item(1)
		awrde.Project.Schematics[0]

You can also get a list of objects using standard range syntax such as:

		awrde.Project.Schematics[1:-1]
		awrde.Project.Schematics[1:5:2]

Note that since the range operator can return an object or a list, it will often confuse Intellisense requiring you to add type information if you want to get proper Intellisense on the returned object.  For example this will not provide Intellisense on the schematic:

		schematic = awrde.Project.Schematic[0]

But both of these will:

		schematic = awrde.Project.Schematics[0]  # type: mwoffice.CSchematic
		schematic = awrde.Project.Schematics.Item(1)  # always returns a CSchematic

##### __str__

String representations of the objects will be of the form "<classname>(object name)" for objects or "<classname>(number of objects in collection)" for collections.

##### Enumerations

The AWR API uses a large number of enumerations.  Let's look at this example:
		
		>>> datafile = awrde.Project.DataFiles[0]  (1)
		>>> df_type = mwo.mwDataFileType(datafile.Type)  (2)
		>>> type(df_type)  (3)
		<enum 'mwDataFileType'>  (4)
		>>> df_type._name_  (5)
		'mwDFT_GMDIFD'  (6)

Here we get a datafile object and examine its type.  The type is numeric but we can use the corresponding function (mwo.mwDataFileType) to map that to the enumeration object (line 2).  Using that object we can get a string form of the name (line 5)

To set an attribute we would do the inverse

		>>> attrib = mwo.mwDataFileType.mwDFT_GMDIFD._value_

