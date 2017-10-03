#-*-encoding=utf-8-*-
'''
Sample Console Scripts for the JX-Argument Parsing Framework
'''

from __future__ import absolute_import, division, print_function, unicode_literals
import pkg_resources as rsc
import jx_argparse as jx

#####################################################################

@jx.jargs(rsc.resource_filename(__name__,'resources/examples/argdef.json'), 'tool_with_docstr_description')
def print_args(*argv, **kargs):
	'''
	This is my JSON DOCSTRING
	'''
	print(argv)
	print(kargs)
	
@jx.xargs(rsc.resource_filename(__name__,'resources/examples/argdef.xml'), 'tool_with_docstr_description')
def xprint_args(*argv, **kargs):
	'''
	This is my XML DOCSTRING
	'''
	print(argv)
	print(kargs)

