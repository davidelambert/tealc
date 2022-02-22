import argparse
from .common import tension

parser = argparse.ArgumentParser(prog='tenscalc')

parser.add_argument('gauge', type=float)
parser.add_argument('material')
parser.add_argument('pitch')
parser.add_argument('length', type=float)
parser.add_argument('--si', action='store_true')

args = parser.parse_args()


value = tension(args.gauge, args.material, args.pitch,
                args.length, args.si)
if args.si:
    units = 'kg'
else:
    units = 'lbs'

print('{:.2f} {}'.format(value, units))
