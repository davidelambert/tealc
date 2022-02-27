import argparse
from tenscalc import tension

with open('./tenscalc/data/manual.txt', 'r') as f:
    manual = f.read()

parser = argparse.ArgumentParser(prog='tenscalc')
subparsers = parser.add_subparsers(dest='command')

string_parser = subparsers.add_parser('string',
                                      help='calculate tension for a single string',
                                      usage='tenscalc string [-h] [--si] <gauge> <material> <pitch> <length>')
string_parser.add_argument('gauge', type=float,
                           help='inches, 1/1000 of an inch, or mm with --si flag')
string_parser.add_argument('material', metavar='material',
                           choices=['ps', 'nps', 'pb', '8020', '8515', 'ss', 'fw', 'pn'],
                           help='options: ps, nps, pb, 8020, 8515, ss, fw, pn')
string_parser.add_argument('pitch',
                           help='e.g. A1, Bb2, C#3. C4 is middle C')
string_parser.add_argument('length', type=float,
                           help='scale length in inches, or mm with --si flag')
string_parser.add_argument('--si', action='store_true',
                           help='<gauge> and <length> in mm; return tension in kg')

# TODO: set syntax
# set_parser = subparsers.add_parser('set', help='calculate tension for a set of strings')
# set_parser.add_argument('file', help='see `tenscalc help` for formatting')

help_parser = subparsers.add_parser('help', help='print long help', add_help=False)

args = parser.parse_args()


if args.command == 'string':
    value = tension(args.gauge, args.material, args.pitch,
                    args.length, args.si)
    if args.si:
        units = 'kg'
    else:
        units = 'lbs'
    print('{:.2f} {}'.format(value, units))

# TODO: set logic
# elif args.command == 'set':
#     pass

elif args.command == 'help':
    print(manual)

else:
    parser.print_help()
