import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

with open(PROJECT_ROOT/'tenscalc/data/unit_weights.json', 'r') as f:
    data = json.load(f)

with open(PROJECT_ROOT/'tenscalc/data/frequency_chart.json', 'r') as f:
    freq = json.load(f)

with open(PROJECT_ROOT/'tenscalc/data/tension_coefs.json', 'r') as f:
    coefs = json.load(f)


def get_uw(gauge, material):
    if str(gauge) not in data[material]['data']:
        if material == 'nps' and gauge > 0.054:
            unit_weight = coefs['nps_large'] * (gauge ** 2)
        else:
            unit_weight = coefs[material] * (gauge ** 2)
    else:
        unit_weight = data[material]['data'][str(gauge)]

    return unit_weight


def tension(gauge: float, material: str, pitch: str, scale_length: float):
    if gauge >= 1.0:
        gauge = gauge / 1000

    unit_weight = get_uw(gauge, material)
    hz = freq[pitch]

    lbs = (unit_weight * (2 * hz * scale_length) ** 2) / 386.4
    return lbs
