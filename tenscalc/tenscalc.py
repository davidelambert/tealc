import json
from pathlib import Path
import argparse

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


def tension(unit_weight, pitch, scale_length=25.5):
    hz = freq[pitch.upper()]
    lbs = (unit_weight * (2 * hz * scale_length) ** 2) / 386.4
    return lbs


parser = argparse.ArgumentParser(
    description='Stringed instrument tension calculator')
parser.add_argument('-g', '--gauge', type=int)
parser.add_argument('-m', '--material',
                    choices=['ps', 'nps', 'pb', '8020', '8515', 'ss', 'pn', 'fw'])
parser.add_argument('-p', '--pitch')
parser.add_argument('-s', '--scale_length', type=float, default=25.5)

args = parser.parse_args()

uw = get_uw(args.gauge, args.material)
lbs = tension(uw, args.pitch, args.scale_length)
print('{:.2f} lbs'.format(lbs))
