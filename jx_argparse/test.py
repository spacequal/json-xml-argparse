#-*-encoding=utf-8-*-
'''
JSON-XML Argument Parsing Framework Test Suite
'''
from __future__ import absolute_import, division, print_function, unicode_literals

#Resources
import pkg_resources as rsc

#Standard Packages
import re, types, sys

#Unit testing
import unittest as ut

#Test target package
import jx_argparse as jx

#####################################################################
eval_list= [
	'type',
	'required'
	]

class jx_argparse_test(ut.TestCase):

	def test_jargs(self):
		
		#Generate a function with an input argument parser
		@jx.jargs(rsc.resource_filename(__name__,'resources/examples/argdef.json'), 'tool_with_docstr_description')
		def jfunc(*args, **kargs):
			'''
			JARG Docstring
			'''
			return(args,kargs)

		#Override the input arguments
		oargv= sys.argv
		sys.argv= ['test', 'input_file', '-x', '1.0', '-z', '2.0']
		oargs, okargs= jfunc()

		#Restore original input argument list
		sys.argv= oargv

		#Check the input arguments
		self.assertTrue(okargs['xcoord']== 1.0            )
		self.assertTrue(okargs['zcoord']== 2.0            )
		self.assertTrue(okargs['ifile' ]== ['input_file'],)

	def test_stack_jargs(self):
		defs= [rsc.resource_filename(__name__,'resources/examples/%s'%i) for i in ['argdef.json','argdef.01.json']]
		@jx.jargs(defs, 2*['tool_with_docstr_description'])
		def jfunc(*args, **kargs):
			'''
			JARG Docstring
			'''
			return(args,kargs)

		#Override the input arguments
		oargv= sys.argv
		sys.argv= ['test', 'input_file', '-x', '1.0', '-z', '2.0']
		oargs, okargs= jfunc()

		#Restore original input argument list
		sys.argv= oargv

		#Check the input arguments
		self.assertTrue(okargs['xcoord']== 1.0            )
		self.assertTrue(okargs['ycoord']== 1.0            )
		self.assertTrue(okargs['zcoord']== 2.0            )
		self.assertTrue(okargs['ifile' ]== ['input_file'],)

	def test_xargs(self):
		@jx.xargs(rsc.resource_filename(__name__,'resources/examples/argdef.xml'), 'tool_with_docstr_description')
		def xfunc(*args, **kargs):
			'''
			JARG Docstring
			'''
			return(args,kargs)

		#Override the input arguments
		oargv= sys.argv
		sys.argv= ['test', 'input_file', '-x', '1.0', '-y', '2.0']
		oargs, okargs= xfunc()

		#Restore original input argument list
		sys.argv= oargv

		#Check the input arguments
		self.assertTrue(okargs['xcoord']== 1.0            )
		self.assertTrue(okargs['ycoord']== 2.0            )
		self.assertTrue(okargs['ifile' ]== ['input_file'],)

