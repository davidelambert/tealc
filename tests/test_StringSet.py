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

import math
from pathlib import Path

import pytest

from tenscalc import StringSet, SetFileParser

set_tensions = {'gbul': 76.0, 'gb85': 79.0, 'gbxl': 85.1, 'gb95': 92.2,
                'gbcl': 95.3, 'gblxl': 91.7, 'gbl': 104.7, 'gb105': 109.9,
                'gbm': 120.8, 'gbtm': 123.8, 'gbtnt': 133.9, 'gbh': 131.2,
                'rrxl': 92.8, 'rrxll': 105.6, 'rrl': 115, 'rrm': 131.3,
                'rejl': 123.3, 'rejm': 137.8, 'stul': 81.3, 'stxl': 91.2,
                'stl': 108.6, 'fw750': 90.7, 'fw800': 128.5, 'fw900': 154.2,
                'fw1000': 180.6, 'bb10u': 116.2, 'bb20x': 138.2,
                'bb30l': 161.6, 'bb40m': 189.2, 'bb50h': 217.2, 's305': 116.2,
                's315': 142.5, 's325': 168.2, 'tm335': 176.0, 's335': 194.0,
                's340': 216.1, 'vnul': 114.8, 'vnxl': 140.0, 'vnl': 166.9,
                'vnb': 182.2, 'vnm': 189.2}

set_paths = Path('./tests/data/SetFiles').iterdir()

test_data = [(str(sp), set_tensions[sp.name]) for sp in set_paths]


@pytest.mark.parametrize('file,expected', test_data)
def test_set_accuracy(file, expected):
    """Test example sets against mfr. charts."""
    f = SetFileParser(file)
    calc = StringSet(f.length, f.gauges, f.materials, f.pitches)
    assert math.isclose(calc.set_lb, expected, rel_tol=0.01)
