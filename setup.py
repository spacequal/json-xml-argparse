#!/usr/bin/env python
#-*-encoding=utf-8-*-
'Decorator based console script argument parsing framework for JSON/XML '\
'for increased standardization and reusability of command line argument '\
'definition blocks.'

#Distutils
from setuptools import setup, find_packages, Extension

#Unit Testing
import unittest

#####################################################################

VERSION= '0.0.2dev'
RELEASE= 'dev' not in VERSION

classifiers= [
	'Intended Audience :: Developers',
	'License :: OSI Approved :: BSD License',
	'Operating System :: OS Independent',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Topic :: Software Development :: Libraries :: Python Modules',
]

requirements = []

console_scripts= [
	'jx_print_args     = jx_argparse.command_line  :  print_args'  ,
	'jx_xml_print_args = jx_argparse.command_line  :  xprint_args' ,
]

entry_points= {
	'console_scripts':console_scripts,
}

#Github repository
url= 'https://github.com/spacequal/json-xml-argparse'

#Setup
setup(
	name                  = 'jx-argparse'             ,
	version               = VERSION                   ,
	description           = __doc__                   ,

	author                = 'Branden Allen'           ,
	author_email          = 'ballen@cfa.harvard.edu'  ,
	maintainer            = 'Branden Allen'           ,
	maintainer_email      = 'ballen@cfa.harvard.edu'  ,

	license               = 'BSD'                     ,
	package_dir           = {}                        ,
	packages              = find_packages()           ,
	include_package_data  = True                      ,
	url                   = url                       ,

	install_requires      = requirements              ,
	classifiers           = classifiers               ,

	python_requires       = '>=2.7'                   ,

	entry_points          = entry_points              ,

	test_suite            = 'jx_argparse.test'        ,
)

