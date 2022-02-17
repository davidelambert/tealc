import argparse
from . import common

parser = argparse.ArgumentParser(prog='tenscalc',
                                 description='Stringed instrument tension calculator')
parser.add_argument('-g', '--gauge', type=float)
parser.add_argument('-m', '--material',
                    choices=['ps', 'nps', 'pb', '8020', '8515', 'ss', 'pn', 'fw'])
parser.add_argument('-p', '--pitch')
parser.add_argument('-s', '--scale_length', type=float, default=25.5)

args = parser.parse_args()

uw = common.get_uw(args.gauge, args.material)
lbs = common.tension(uw, args.pitch, args.scale_length)
print('{:.2f} lbs'.format(lbs))
