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

import pytest
import tomli

from tealc import StringTension

with open('./tests/data/string_data.toml', 'rb') as f:
    string_data = tomli.load(f)

material = []
pitch = []
gauge = []
tension = []
for m in string_data.keys():
    for p in string_data[m].keys():
        n = len(string_data[m][p]['gauge'])
        material.extend([m] * n)
        pitch.extend([p] * n)
        gauge.extend(string_data[m][p]['gauge'])
        tension.extend(string_data[m][p]['tension'])
guitar_data = list(zip(gauge, material, pitch, tension))


@pytest.mark.parametrize('test_g, test_m, test_p, expected', guitar_data)
def test_accuracy(test_g, test_m, test_p, expected):
    """Test calculations against mfr. charts."""
    calc = StringTension(test_g, test_m, test_p, length=25.5)
    assert math.isclose(calc.lb, expected, rel_tol=0.1)


with open('./tests/data/bass_string_data.toml', 'rb') as f:
    bass_string_data = tomli.load(f)

b_material = []
b_pitch = []
b_gauge = []
b_tension = []
for m in bass_string_data.keys():
    for p in bass_string_data[m].keys():
        n = len(bass_string_data[m][p]['gauge'])
        b_material.extend([m] * n)
        b_pitch.extend([p] * n)
        b_gauge.extend(bass_string_data[m][p]['gauge'])
        b_tension.extend(bass_string_data[m][p]['tension'])
bass_data = list(zip(b_gauge, b_material, b_pitch, b_tension))
print(bass_data)


@pytest.mark.parametrize('test_g, test_m, test_p, expected', bass_data)
def test_bass_accuracy(test_g, test_m, test_p, expected):
    """Test bass string calculations against mfr. charts."""
    calc = StringTension(test_g, test_m, test_p, length=34)
    assert math.isclose(calc.lb, expected, rel_tol=0.1)
