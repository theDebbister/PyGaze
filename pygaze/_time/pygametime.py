# -*- coding: utf-8 -*-
#
# This file is part of PyGaze - the open-source toolbox for eye tracking
#
#    PyGaze is a Python module for easily creating gaze contingent experiments
#    or other software (as well as non-gaze contingent experiments/software)
#    Copyright (C) 2012-2013  Edwin S. Dalmaijer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
import time

import pygame

from pygaze._time.basetime import BaseTime

# we try importing the copy_docstr function, but as we do not really need it
# for a proper functioning of the code, we simply ignore it when it fails to
# be imported correctly
try:
    from pygaze._misc.misc import copy_docstr
except:
    pass


class PyGameTime(BaseTime):

    # see pygaze._time.basetime.BaseTime

    def __init__(self):

        # see pygaze._time.basetime.BaseTime

        # try to copy docstring (but ignore it if it fails, as we do
        # not need it for actual functioning of the code)
        try:
            copy_docstr(BaseTime, PyGameTime)
        except:
            # we're not even going to show a warning, since the copied
            # docstring is useful for code editors; these load the docs
            # in a non-verbose manner, so warning messages would be lost
            pass

        # On Windows, time.clock() provides higher accuracy than time.time().
        if sys.platform == "win32":
            # DEPRECATED IN PYTHON 3
            if sys.version_info[0] <= 2:
                self._cpu_time = time.clock
            else:
                self._cpu_time = time.time
        else:
            self._cpu_time = time.time

        pygame.init()

    def expstart(self):

        # see pygaze._time.basetime.BaseTime

        self.expbegintime = self._cpu_time() * 1000

    def get_time(self):

        # see pygaze._time.basetime.BaseTime

        ctime = self._cpu_time() * 1000 - self.expbegintime

        return ctime

    def pause(self, pausetime):

        # see pygaze._time.basetime.BaseTime

        realpause = pygame.time.delay(int(pausetime))

        return realpause

    def expend(self):

        # see pygaze._time.basetime.BaseTime

        endtime = self.get_time()

        pygame.quit()

        return endtime
