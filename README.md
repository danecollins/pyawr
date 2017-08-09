# pyawr - AWR Scripting in Python

**Python utilities for Microwave Office from AWR**

It is possible to write scripts for AWRDE in something other than Visual Basic such as Python, Perl, C#, etc.  This package create tools to make this easier and more pythonic.

For help getting your python environment setup for COM, see [AWR Scripting in Python](http://kb.awr.com/display/SCRIPTS/AWR+Scripting+in+Python)

Requirements for this package are defined in requirements.txt.

### Installation

To install this package use:

    > python setup.py install

### Testing your installation

Here is a very simple python program that connects to AWRDE and writes out all the models in the software:

	import pyawr
	awrde, awrc = pyawr.connect()
	for model in awrde.Models:
		print model.Name
		
### Connecting to a Specific Instance of AWRDE

Calling connect will connect to the first instance of AWRDE that was started.  There are times when you want to connect to a specific version, or instance of AWRDE which can be done by passing the version or class ID to connect as follows:

**To start a specific version**

   import pyawr
   awrde, awrc = pyawr.connect(version='13.0')  # version is a string
   
   
**To connect to a specific instance**

To connect to a specific instance you need to get the instance id from AWRDE.  The best way to get this is with a VB script of the following form:

	Sub Main
		Debug.Print MWOffice.InstanceCLSID
	End Sub
	
The class ID will be in the form 

**62F49D56-070F-4E6C-8AB9-25845CB94B9A**

Then, from Python you will use

	import pyawr
	awrde, awrc = pyawr.connect(clsid='{class id}')
	
For example

	awrde, awrc = pyawr.connect(clsid="{62F49D56-070F-4E6C-8AB9-25845CB94B9A}")
	
**Note:** the braces are required around the class ID

### Accessing AWRDE Enumerations

The [API Reference](https://awrcorp.com/download/faq/english/docs/ApiReference/api_reference.html) describes many [enumerations](https://awrcorp.com/download/faq/english/docs/ApiReference/ch02s03.html).  For example when looking at a measurement the data type could be mwMDT\_ReflectionData or mwMDT\_AdmittanceData. You can access these value from the object returned as the second argument of the tuple returned by  **connect()** as shown below.

	import pyawr
	awrde, awrc = pyawr.connect
	....
	if meas.DataType == awrc.mwMDT\_ReflectionData:
		....
		
If it often convenient to reverse map these values to strings for output.  To help in this, pyawr provides cmap which defines functions for each of the enumerations.  Using these we could convert the data type to a string.  From the example above (assuming the if test was true:

	from cmap import mwMeasDataType
	
	print(mwMeasDataType(meas.DataType))
	
	>> 'mwMDT_ReflectionData'
