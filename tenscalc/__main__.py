import argparse
from . import common

parser = argparse.ArgumentParser(prog='tenscalc')

parser.add_argument('gauge', type=float)
parser.add_argument('material')
parser.add_argument('pitch')
parser.add_argument('length', nargs='?', type=float, default=25.5)

args = parser.parse_args()

uw = common.get_uw(args.gauge, args.material)
lbs = common.tension(uw, args.pitch, args.length)
print('{:.2f} lbs'.format(lbs))
