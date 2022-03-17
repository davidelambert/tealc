# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2022 David E. Lambert
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import math
from pathlib import Path

import pytest

from tenscalc import StringSet, SetFileParser

string_sets = {'gbul': 76.0, 'gb85': 79.0, 'gbxl': 85.1, 'gb95': 92.2,
               'gbcl': 95.3, 'gblxl': 91.7, 'gbl': 104.7, 'gb105': 109.9,
               'gbm': 120.8, 'gbtm': 123.8, 'gbtnt': 133.9, 'gbh': 131.2,
               'rrxl': 92.8, 'rrxll': 105.6, 'rrl': 115, 'rrm': 131.3,
               'rejl': 123.3, 'rejm': 137.8, 'stul': 81.3, 'stxl': 91.2,
               'stl': 108.6, 'fw750': 90.7, 'fw800': 128.5, 'fw900': 154.2,
               'fw1000': 180.6, 'bb10u': 116.2, 'bb20x': 138.2,
               'bb30l': 161.6, 'bb40m': 189.2, 'bb50h': 217.2, 's305': 116.2,
               's315': 142.5, 's325': 168.2, 'tm335': 176.0, 's335': 194.0,
               's340': 216.1, 'vnul': 114.8, 'vnxl': 140.0, 'vnl': 166.9,
               'vnb': 182.2, 'vnm': 189.2, 'l5000': 153.5, 'ml5000': 176.0,
               'm5000': 184.5, 'cm5000': 184.3, 'xl3045': 109.1,
               'l3045': 140.8, 'ml3045': 177.7, 'm3045': 186.5, 'h3045': 221.0,
               '5l': 172.1, '5ml': 210.9, '5m': 225.0, '6ml': 248.1,
               '3025': 163.2, 'cm3050': 174.1, 'm3050': 184.6, '3050': 229.1,
               'm3050x-5': 219.0}

set_paths = Path('./tests/data/SetFiles').iterdir()

test_data = [(str(sp), string_sets[sp.name]) for sp in set_paths]


@pytest.mark.parametrize('file, expected', test_data)
def test_set_accuracy(file, expected):
    """Test example sets against mfr. charts."""
    f = SetFileParser(file)
    calc = StringSet(f.length, f.gauges, f.materials, f.pitches)
    assert math.isclose(calc.set_lb, expected, rel_tol=0.05)
