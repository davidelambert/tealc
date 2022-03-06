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
