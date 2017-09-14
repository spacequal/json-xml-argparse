#-*-encoding=utf-8-*-
'''
Argument Parsing Framework for JSON-XML
'''
from __future__ import absolute_import, division, print_function, unicode_literals
import json, argparse, inspect, sys
import xml.etree.ElementTree as et
import pkg_resources as rsc
import re

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
	parser_list: str
		Path to a JSON file containing parser definitions
	parser: str
		Name of the parser definition contained within the input file
	'''
	with open(parser_list) as f: jarg= json.load(f)
	argset= jarg[parser]

	def jargs_dec(func):
		if 'isfile' not in argset or 'resource_name' not in argset:
			descr= func.__doc__.strip()
		elif argset['isfile']== "True":
			with open(argset['description']) as dfile: descr= dfile.read().strip()
		elif argset['resource_name']!= "None": 
			descr= rsc.resource_string(argset['resource_name'], argset['description'])
		else:
			descr= argset['description']

		aparse= argparse.ArgumentParser('\n'+descr+'\n\n')

		#Keyword Arguments
		for ii in argset['args']:
			#Enforce literally interpreted inputs
			for key in ii:
				if key in eval_list: ii[key]= eval(ii[key])
			args= ii.pop('args')
			kargs= ii

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
	parser_list: str
		Path to a XML file containing parser definitions
	parser: str
		Name of the parser definition contained within the input file
	'''
	def xargs_dec(func):
		#XML Tree readout and location of the desired elements
		descr= func.__doc__.strip()
		aparse= argparse.ArgumentParser('\n'+descr+'\n\n')
		t= et.parse(parser_list)
		matching_parser_list= t.findall(".//parser[@name='%s']"%parser)

		#Append parser arguments
		for ii in matching_parser_list[0]:
			kargs= ii.attrib
			args= re.split('\s*?,\s*', kargs.pop('args'))
			for jj in ii: kargs[jj.tag]= jj.text.strip()
			for jj in kargs:
				if jj in eval_list: kargs[jj]= eval(kargs[jj])
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

