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

import pytest
import tomli

from tenscalc import StringTension

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
test_data = list(zip(gauge, material, pitch, tension))


@pytest.mark.parametrize('test_g,test_m,test_p,expected', test_data)
def test_accuracy(test_g, test_m, test_p, expected):
    """Test calculations against mfr. charts."""
    calc = StringTension(test_g, test_m, test_p, length=25.5)
    assert math.isclose(calc.lb, expected, rel_tol=0.01)