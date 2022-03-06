"""Command line interface for tenscalc.

Code in this module is run when tenscalc is tun from the command line.
    This package contains no public objects. Documentation for the CLI
    is contained externally in tenscalc.manual, which is accessible
    via the command line with ``tenscalc help``.
"""

import argparse

from tenscalc import StringTension, StringSet, SetFileParser, manual

msg = {
    'string': 'calculate tension for a single string',
    'set': 'calculate tensions for a set of strings',
    'gauge': 'inches, 1/1000 of an inch, or mm with --si flag',
    'mat': 'options: ps, nps, pb, 8020, 8515, ss, fw, pn',
    'pitch': 'e.g. A1, Bb2, C#3. C4 is middle C',
    'length': 'scale length in inches, or mm with --si flag',
    'si': 'supply gauge and length units in mm; get tension in kg',
    'title': 'optional title for output chart',
    'double': 'double each string spec (for instruments like mandolin)',
    'file': 'see tenscalc -h for format'
}

set_usage = """tenscalc set [-h] [--file FILE] [--title TITLE]
       tenscalc set [-h] [--length LENGTH] [--gauges [G ...]]
                         [--materials [M ...]] [--pitches [P ...]]
                         [--double] [--si] [--title TITLE]"""

parser = argparse.ArgumentParser(prog='tenscalc')
subparsers = parser.add_subparsers(dest='command')

help_parser = subparsers.add_parser('help', help='print manual',
                                    add_help=False)

string_parser = subparsers.add_parser('string', help=msg['string'])
string_parser.add_argument('gauge', type=float, help=msg['gauge'])
string_parser.add_argument('material', metavar='material', help=msg['mat'],
                           choices=['ps', 'nps', 'pb', '8020',
                                    '8515', 'ss', 'fw', 'pn'])
string_parser.add_argument('pitch', help=msg['pitch'])
string_parser.add_argument('length', type=float, help=msg['length'])
string_parser.add_argument('--si', action='store_true', help=msg['si'])

set_parser = subparsers.add_parser('set', help=msg['set'], usage=set_usage)
set_parser.add_argument('--file', help=msg['file'])
set_parser.add_argument('--length', type=float, help=msg['length'])
set_parser.add_argument('--gauges', nargs='*', metavar='G', help=msg['gauge'])
set_parser.add_argument('--materials', nargs='*', metavar='M', help=msg['mat'])
set_parser.add_argument('--pitches', nargs='*', metavar='P', help=msg['pitch'])
set_parser.add_argument('--double', help=msg['double'], action='store_true')
set_parser.add_argument('--si', help=msg['si'], action='store_true')
set_parser.add_argument('--title', help=msg['title'])

args = parser.parse_args()

if args.command == 'help':
    print(manual)

elif args.command == 'string':
    tension = StringTension(args.gauge, args.material, args.pitch,
                            args.length, args.si)
    if args.si:
        print('{:.1f} kg'.format(tension.kg))
    else:
        print('{:.1f} lb'.format(tension.lb))


elif args.command == 'set':
    if args.file is None:
        tension = StringSet(args.length, args.gauges, args.materials,
                            args.pitches, args.double, args.si)
    else:
        sf = SetFileParser(args.file)
        tension = StringSet(sf.length, sf.gauges, sf.materials, sf.pitches,
                            sf.double, sf.si)

    if args.si:
        tension.print(args.title, print_si=True)
    else:
        tension.print(args.title)

else:
    parser.print_help()
