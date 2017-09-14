===========
jx_argparse
===========
The jx_argparse is a decorator based framework to interface JSON/XML defined command line arguments 
for python scripts.

Usage
-----
To apply command line arguments defined in a JSON file to a function ::
	
	import jx_argparse as jx

	@jx.jarg(argset_definitions.json, 'argset_name')
	def new_function(*args, **kargs):
		'''
		This is my function, there are many like it but this one is mine.
		'''
		... Something Wonderful ...

The corresponding JSON file contains definitions for `ArgumentParser
<https://docs.python.org/3/library/argparse.html>`_  argument definitions, cf. ::

	{
		"argset_name":{
			"input":[
				{
					"args":["arg0"],
					"help":"Positional Argument"
				},
				{
					"args":["-i","--input"],
					"help":"Keyword Argument",
					"type":"str"
				}
			}
		]
	}

These may be used in conjunction with standalone scripts or as entry points resulting in a tool that
may be called from the command line, cf.::
	
	./console_script ARG0 --input ARG1

A working example may be found in ``jx_argparse/command_line.py`` with corresponding JSON argument
definitions given in ``jx_argparse/argdef_example.json``.  After installation of this package the
console script ``jx_print_args``, which executes the ``print_args`` function, is made available to
the user.

License
-------
jx_argparse is licensed under a 3-clause BSD style license (see the ``LICENSE.rst`` file).
