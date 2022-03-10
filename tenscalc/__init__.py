# -*- coding: utf-8 -*-
# Copyright (C) 2022 David E. Lambert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

"""A stringed instrument tension calculator.

Modules:
    tenscalc.py: All primary package objects.
    __main__.py: Package CLI.
"""

from tenscalc.tenscalc import (StringTension,
                               StringSet,
                               SetFileParser,
                               print_material_codes)

__version__ = '0.1.1'
