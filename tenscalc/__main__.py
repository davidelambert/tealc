import argparse
import sys
import json
from .common import tension

parser = argparse.ArgumentParser(prog='tenscalc')

parser.add_argument('gauge', type=float)
parser.add_argument('material')
parser.add_argument('pitch')
parser.add_argument('length', nargs='?', type=float, default=25.5)
parser.add_argument('--si', action='store_true')

args = parser.parse_args()

# MATERIAL CODE VALIDATION ================================
with open('./tenscalc/data/material_codes.json', 'r') as f:
    material_codes = json.load(f)

if args.material not in list(material_codes):
    print('\nERROR: material must be one of the following codes')
    print('Code'.rjust(6), 'String material', sep='  ')
    print('----'.rjust(6), '---------------', sep='  ')
    for k, v in material_codes.items():
        print(k.rjust(6), v, sep='  ')
    sys.exit()

# PITCH VALIDATION =======================================
with open('./tenscalc/data/frequency_chart.json', 'r') as f:
    frequency_chart = json.load(f)

if args.pitch not in list(frequency_chart):
    print('\n ERROR: pitch must be in scientific pitch notation, from A0-E5,')
    print('  with uppercase note letter.')
    print('See help [-h, --help] for examples and common open string pitches')
    sys.exit()

# SI CONVERSION ==========================================
if args.si:
    args.gauge = round(args.gauge / 25.4, 3)
    args.length = args.length / 25.4

# CALCULATE & PRINT RESULTS ==============================
lbs = tension(args.gauge, args.material, args.pitch, args.length)

if args.si:
    print('{:.2f} kg'.format(lbs / 2.205))
else:
    print('{:.2f} lbs'.format(lbs))
