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
	def new_function(*args, **kargs) {
		'''
		This is my function, there are many like it but this one is mine.
		'''
		... Something Wonderful ...
	}

The corresponding JSON file contains definitions for ArgParse argument definitions, cf. ::
	
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

A working example can be found in ``jx_argparse/command.py`` with corresponding JSON argument
definitions given in ``jx_argparse/argdef_example.json``.

License
-------
jx_argparse is licensed under a 3-clause BSD style license (see the ``LICENSE.rst`` file).
