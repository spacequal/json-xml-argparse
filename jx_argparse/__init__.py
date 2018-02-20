#-*-encoding=utf-8-*-
'''
Argument Parsing Framework for JSON-XML
'''
from __future__ import absolute_import, division, print_function, unicode_literals

#XML/JSON Parsers
import json, argparse
import xml.etree.ElementTree as et

#Resources
import pkg_resources as rsc

#Standard Packages
import re, types
import inspect, sys

#Unit testing
import unittest as ut

#####################################################################
eval_list= [
	'type',
	'required'
	]

def jargs(parser_list, parser):
	'''
	Decorator for the addtion of command line input for a function defined in JSON files.

	Parameters
	----------
	parser_list: str or list
		Path to a JSON file containing parser definitions.  If input as a list
		it must match the shape of the input parser list.
	parser: str or list
		Name of the parser definition contained within the input file
	'''
	if not isinstance(parser     , types.ListType): parser= [parser,]
	if not isinstance(parser_list, types.ListType): parser_list= [parser_list,]

	def jargs_dec(func):
		#JSON readout of command line definition blocks
		descr= func.__doc__.strip()
		aparse= argparse.ArgumentParser('\n'+descr+'\n\n')

		for ii,jj in zip(parser_list, parser):
			with open(ii) as f: jarg= json.load(f)
			argset= jarg[jj]

			#Keyword Arguments
			for kk in argset['args']:
				#Enforce literally interpreted inputs
				for key in kk:
					if key in eval_list: kk[key]= eval(kk[key])
				args= kk.pop('args')
				kargs= kk

				#Add arguments
				aparse.add_argument(*args, **kargs)

		#Redefine function as a console script
		def f_main():
			pargs= vars(aparse.parse_args())		

			#Check for input arguments which are not contained in the function (TBD check option)
#			aspec= inspect.getargspec(func)
#			keys= pargs.keys()
#			for ii in keys:
#				if ii not in aspec.args: 
#					pargs.pop(ii)
#					print('Warning: Argument %s not accepted and ignored by the function'%ii, file= sys.stderr)

			#Return the function
			return func(**pargs)

		#Return the new console script function
		return f_main

	#Retrun the decorator
	return jargs_dec

def xargs(parser_list, parser):
	'''
	Decorator for the addtion of command line input for a function defined in XML files.

	Parameters
	----------
	parser_list: str or list
		Path to a XML file containing parser definitions
	parser: str or list
		Name of the parser definition contained within the input file
	'''
	if not isinstance(parser     , types.ListType): parser= [parser,]
	if not isinstance(parser_list, types.ListType): parser_list= [parser_list,]

	def xargs_dec(func):
		#XML Tree of command line definition blocks
		descr= func.__doc__.strip()
		aparse= argparse.ArgumentParser('\n'+descr+'\n\n')

		#Append all parser arguments from all input command line argument blocks
		for ii,jj in zip(parser_list, parser):
			t= et.parse(ii)
			matching_parser_list= t.findall(".//parser[@name='%s']"%jj)

			#Append parser arguments
			for arg in matching_parser_list[0]:
				kargs= arg.attrib
				args= re.split('\s*?,\s*', kargs.pop('args'))
				for kk in arg: kargs[kk.tag]= kk.text.strip()
				for kk in kargs:
					if kk in eval_list: kargs[kk]= eval(kargs[kk])
				aparse.add_argument(*args, **kargs)

		#Form the console script function
		def fout():
			pargs= vars(aparse.parse_args())

			#Function Return
			return func(**pargs)

		#Console script function
		return fout

	#Return decorator
	return xargs_dec
