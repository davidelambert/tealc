import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

with open('./tension_coefs.json', 'r') as f:
    coef = json.load(f)

with open('./frequency_chart.json', 'r') as f:
    freq = json.load(f)


def get_uw(gauge, material):
    if gauge >= 1.0:
        gauge = gauge / 1000
    uw = coef[material] * (gauge**2)
    return uw


def tension(unit_weight, pitch, scale_length=25.5):
    hz = freq[pitch.upper()]
    lbs = (unit_weight * (2 * hz * scale_length) ** 2) / 386.4
    return lbs
