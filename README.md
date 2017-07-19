# pyawr - AWR Scripting in Python

**Python utilities for Microwave Office from AWR**

It is possible to write scripts for AWRDE in something other than Visual Basic such as Python, Perl, C#, etc.  This article describes the setup for Python
AWRDE is a COM automation server and any programming language that can perform as a COM client can be used. This includes most current programming languages such as Python. With Python you will need to install the win32com.client library.  The easiest way to do this is to use pip.

	pip install pypiwin32
	
While this is the minimum setup, if you plan to do significant work in python you want to create the entire type library you will need to run makepy.py. In a command prompt

	cd [python lib directory]/site-packages/win32com/client
	python makepy.py

If you run this with the -v option it will indicate the name of the generated python file in case you want to look at it.  These definitions will be loaded automatically when you connect to AWRDE.

### Testing your installation

Here is a very simple python program that connects to AWRDE and writes out all the models in the software:

	# This is a very simple python script that connects to AWRDE and
	# dumps out the complete list of models                
	#
	import win32com.client
	awrde=win32com.client.Dispatch("MWOApp.MWOffice")
	for model in awrde.Models:
		print model.Name
		
### Connecting to a Specific Instance of AWRDE

Calling Dispatch("MWOApp.MWOffice") will connect to the first instance of AWRDE that was started.  There are times when you want to connect to a specific instance of AWRDE which can be done by passing the class ID to Dispatch.  You can get the class ID of a specific instance of AWRDE from VB Scripting with

	Sub Main
		Debug.Print MWOffice.InstanceCLSID
	End Sub
	
The class ID will be in the form 

**62F49D56-070F-4E6C-8AB9-25845CB94B9A**

Then, from Python you will use

	obj = win32com.client.Dispatch("{CLSID}")
	
For example

	obj2 = win32com.client.Dispatch("{62F49D56-070F-4E6C-8AB9-25845CB94B9A}")
	
**Note:** the braces are required around the class ID
