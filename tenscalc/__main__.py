import argparse
from .common import tension

parser = argparse.ArgumentParser(prog='tenscalc')

parser.add_argument('gauge', type=float)
parser.add_argument('material')
parser.add_argument('pitch')
parser.add_argument('length', type=float)
parser.add_argument('--si', action='store_true')

args = parser.parse_args()

# CALCULATE & PRINT RESULTS ==============================
value, unit = tension(args.gauge, args.material, args.pitch,
                      args.length, args.si)

print('{:.2f} {}'.format(value, unit))
