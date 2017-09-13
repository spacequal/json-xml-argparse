#-*-encoding=utf-8-*-
'''
Argument Parsing Framework for JSON-XML
'''
from __future__ import absolute_import, division, print_function, unicode_literals
import json, argparse, inspect, sys
import pkg_resources as rsc

#####################################################################
eval_list= [
	'type',
	'required'
	]

def jargs(argdef, argset_name):
	'''
	Decorator for the application of JSON defined arguments to a
	function for packaging as a console script.
	'''

	def jargs_dec(func):
		with open(argdef) as f: jarg= json.load(f)
		argset= jarg[argset_name]

		if 'isfile' not in argset or 'resource_name' not in argset:
			descr= func.__doc__.strip()
		elif argset['isfile']== "True":
			with open(argset['description']) as dfile: descr= dfile.read().strip()
		elif argset['resource_name']!= "None": 
			descr= rsc.resource_string(argset['resource_name'], argset['description'])
		else:
			descr= argset['description']

		parser= argparse.ArgumentParser('\n'+descr+'\n\n')

		#Keyword Arguments
		for ii in argset['input']:
			#Enforce literally interpreted inputs
			for key in ii:
				if key in eval_list: ii[key]= eval(ii[key])
			args= ii.pop('args')
			kargs= ii

			#Add arguments
			parser.add_argument(*args, **kargs)

		#Redefine function as a console script
		def f_main():
			pargs= vars(parser.parse_args())		

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

