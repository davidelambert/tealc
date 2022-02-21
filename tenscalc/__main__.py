import argparse
from . import common

parser = argparse.ArgumentParser(prog='tenscalc',
                                 usage="""tenscalc [-h] GAUGE MATERIAL PITCH [LENGTH]
   OR: tenscalc [-h] GAUGE -m MATERIAL -p PITCH [-l LENGTH]""")

parser.add_argument('gauge', type=float, metavar='GAUGE')
parser.add_argument('-m', '--material', metavar='MATERIAL',
                    choices=['ps', 'nps', 'pb', '8020', '8515', 'ss', 'pn', 'fw'])
parser.add_argument('material', nargs='?', metavar='MATERIAL',
                    choices=['ps', 'nps', 'pb', '8020', '8515', 'ss', 'pn', 'fw'])
parser.add_argument('-p', '--pitch', metavar='PITCH')
parser.add_argument('pitch', nargs='?', metavar='PITCH')
parser.add_argument('-l', '--length', metavar='LENGTH',
                    type=float, default=25.5)
parser.add_argument('length', nargs='?', metavar='LENGTH',
                    type=float, default=25.5)

args = parser.parse_args()

uw = common.get_uw(args.gauge, args.material)
lbs = common.tension(uw, args.pitch, args.length)
print('{:.2f} lbs'.format(lbs))
