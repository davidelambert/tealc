import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

with open(PROJECT_ROOT/'tenscalc/data/unit_weights.json', 'r') as f:
    data = json.load(f)

with open(PROJECT_ROOT/'tenscalc/data/frequency_chart.json', 'r') as f:
    freq = json.load(f)


def get_uw(gauge, material):
    if gauge >= 1.0:
        gauge = gauge / 1000
    # if str(gauge) not in list(data[material['data']]):
    #     do_something()
    uw = data[material]['data'][str(gauge)]
    return uw


def tension(unit_weight, pitch, scale_length):
    hz = freq[pitch.upper()]
    lbs = (unit_weight * (2 * hz * scale_length) ** 2) / 386.4
    return lbs
