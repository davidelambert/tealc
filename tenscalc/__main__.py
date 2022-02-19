import argparse
from . import common

parser = argparse.ArgumentParser(prog='tenscalc',
        description='Stringed instrument tension calculator',
        usage="""tenscalc [-h] GAUGE MATERIAL PITCH [length]
   OR: tenscalc [-h] GAUGE -m MATERIAL -p PITCH [-l LENGTH]""")

parser.add_argument('gauge', type=float)
parser.add_argument('-m', '--material', metavar='MATERIAL',
        choices=['ps', 'nps', 'pb', '8020', '8515', 'ss', 'pn', 'fw'])
parser.add_argument('material', nargs='?', metavar='material',
        choices=['ps', 'nps', 'pb', '8020', '8515', 'ss', 'pn', 'fw'])
parser.add_argument('-p', '--pitch')
parser.add_argument('pitch', nargs='?')
parser.add_argument('-l', '--length', type=float, default=25.5)
parser.add_argument('length', nargs='?', type=float, default=25.5)

args = parser.parse_args()

uw = common.get_uw(args.gauge, args.material)
lbs = common.tension(uw, args.pitch, args.length)
print('{:.2f} lbs'.format(lbs))

