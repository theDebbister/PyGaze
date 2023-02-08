#!/usr/bin/env python

"""
This file is part of PyGaze.

PyGaze is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyGaze is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with qnotero.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import glob
import pygaze
from setuptools import setup

print("Running setup for PyGaze version {}".format(pygaze.__version__))


def files(path):

	return [
		fname
		for fname in glob.glob(path) if os.path.isfile(fname)
		and not fname.endswith('.pyc')
	]


def data_files():

	"""
	desc:
		The OpenSesame plug-ins are installed as additional data. Under Windows,
		there is no special folder to put these plug-ins in, so we skip this
		step.

	returns:
		desc:	A list of data files to include.
		type:	list
	"""

	return [
		("share/opensesame_plugins/pygaze_init/resources/locale",
			files("opensesame_plugins/pygaze_init/resources/locale/*")),
		("share/opensesame_plugins/pygaze_init",
			files("opensesame_plugins/pygaze_init/*")),
		("share/opensesame_plugins/pygaze_drift_correct",
			files("opensesame_plugins/pygaze_drift_correct/*")),
		("share/opensesame_plugins/pygaze_log",
			files("opensesame_plugins/pygaze_log/*")),
		("share/opensesame_plugins/pygaze_start_recording",
			files("opensesame_plugins/pygaze_start_recording/*")),
		("share/opensesame_plugins/pygaze_stop_recording",
			files("opensesame_plugins/pygaze_stop_recording/*")),
		("share/opensesame_plugins/pygaze_wait",
			files("opensesame_plugins/pygaze_wait/*"))
	]


def get_readme():

	if os.path.exists('README.md'):
		with open('README.md') as fd:
			return fd.read()
	return 'No readme information'


setup(
	name='pygaze' if 'bdist_deb' in sys.argv else u'pygaze',
	python_requires=">=3",
	version=pygaze.__version__,
	description="A Python library for eye tracking",
	long_description=get_readme(),
	long_description_content_type='text/markdown',
	author="Edwin Dalmaijer",
	author_email="edwin.dalmaijer@gmail.com",
	url="http://www.pygaze.org/",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Environment :: X11 Applications',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Programming Language :: Python :: 3',
	],
	include_package_data=True,
	package_data={
		"pygaze._eyetracker.alea": ["*.dll"],
		"pygaze._eyetracker.eyelogic": ["*.dll"]
	},
	packages=[
		"pygaze",
		"pygaze._display",
		"pygaze._eyetracker",
		"pygaze._eyetracker.alea",
		"pygaze._eyetracker.eyelogic",
		"pygaze._eyetracker.tobiiglasses",
		"pygaze._joystick",
		"pygaze._keyboard",
		"pygaze._logfile",
		"pygaze._misc",
		"pygaze._mouse",
		"pygaze._screen",
		"pygaze._sound",
		"pygaze._time",
		"pygaze.plugins",
	],
	data_files=data_files()
)
