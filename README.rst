===========
jx_argparse
===========
The jx_argparse is a decorator based framework to interface JSON/XML defined command line arguments 
for python scripts.

-----
Usage
-----
Two command line argument definition filtypes are supported: XML and JSON.  The use of these is
described below briefly.

JSON
----
To apply command line arguments defined in a JSON file to a function ::
	
	import jx_argparse as jx

	@jx.jargs('parser_list.json', 'parser_name')
	def new_function(*args, **kargs):
		'''
		This is my function, there are many like it but this one is mine.
		'''
		... Something Wonderful ...

The corresponding JSON file contains definitions for `ArgumentParser
<https://docs.python.org/3/library/argparse.html>`_  argument definitions, cf. ::

	{
		"parser_name":{
			"args":[
				{
					"args":["arg0"],
					"help":"Positional Argument"
				},
				{
					"args":["-i","--input"],
					"help":"Keyword Argument",
					"type":"str"
				}
			]
		}
	}

These may be used in conjunction with standalone scripts or as entry points resulting in a tool that
may be called from the command line, cf.::
	
	./console_script ARG0 --input ARG1

A working example may be found in ``jx_argparse/command_line.py`` with corresponding JSON argument
definitions given in ``jx_argparse/examples/argdef.json``.  After installation of this package the
console script ``jx_print_args``, which executes the ``print_args`` function, is made available to
the user.

XML
---
To apply command line arguments defined in a XML file to a function ::
	
	import jx_argparse as jx

	@jx.xargs('parser_list.xml', 'parser_name')
	def new_function(*args, **kargs):
		'''
		This is my function, there are many like it but this one is mine.
		'''
		... Something Wonderful ...

The corresponding XML file contains definitions for `ArgumentParser
<https://docs.python.org/3/library/argparse.html>`_  argument definitions, cf. ::

	<?xml version="1.0" encoding="UTF-8"?>
	<parser_list>
		<parser name='parser_name'>
			<arg args='arg0' nargs='+'>
				<help>ARG0 HELP</help>
			</arg>
			<arg args='-i, --input' default='ARG1_DEFAULT' type='float'>
				<help>OPTIONAL ARG1 HELP</help>
			</arg>
		</parser>
	</parser_list>

The argument attributes may be input as either children to the ``<arg>`` elements or as attributes.

These may be used in conjunction with standalone scripts or as entry points resulting in a tool that
may be called from the command line, cf.::
	
	./console_script ARG0 --input ARG1

A working example may be found in ``jx_argparse/command_line.py`` with corresponding XML argument
definitions given in ``jx_argparse/examples/argdef.xml``.  After installation of this package the
console script ``jx_print_xml_args``, which executes the ``xprint_args`` function, is made available to
the user.

-------
License
-------
jx_argparse is licensed under a 3-clause BSD style license (see the ``LICENSE.rst`` file).
