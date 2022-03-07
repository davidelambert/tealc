# -*- coding: utf-8 -*-
# Copyright (C) 2022 David E. Lambert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

"""Command line interface for tenscalc.

Code in this module is run when tenscalc is tun from the command line.
    This package contains no public objects. Documentation for the CLI
    is contained externally in tenscalc.manual, which is accessible
    via the command line with ``tenscalc help``.
"""

from pathlib import Path
import os
import subprocess
import argparse

from tenscalc import StringTension, StringSet, SetFileParser

PKG_DIR = Path(__file__).parent

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

help_parser = subparsers.add_parser('help', help='print manual',
                                    add_help=False)


def print_manual():
    """Print the manual with less (or more on Windows)."""
    if os.name == 'posix':
        prompt = '-Pstenscalc help line %lt/%L (press h for help or q to quit)'
        subprocess.run(['less', prompt, '--', PKG_DIR/'manual.txt'])
    elif os.name == 'nt':
        subprocess.run(['more', PKG_DIR/'manual.txt'])
    else:
        print(PKG_DIR/'manual.txt')


def main(args: list[str] = None):
    """Command line interface for tenscalc.

    Args:
        args (list[str], optional): Argument list. The default of ``None``
        will read sys.argv
    """
    parsed_args = parser.parse_args(args)

    if parsed_args.command == 'string':
        tension = StringTension(parsed_args.gauge, parsed_args.material,
                                parsed_args.pitch, parsed_args.length,
                                parsed_args.si)
        if parsed_args.si:
            print('{:.1f} kg'.format(tension.kg))
        else:
            print('{:.1f} lb'.format(tension.lb))

    elif parsed_args.command == 'set':
        if parsed_args.file is None:
            tension = StringSet(parsed_args.length, parsed_args.gauges,
                                parsed_args.materials, parsed_args.pitches,
                                parsed_args.double, parsed_args.si)
        else:
            sf = SetFileParser(parsed_args.file)
            tension = StringSet(sf.length, sf.gauges, sf.materials, sf.pitches,
                                sf.double, sf.si)

        if parsed_args.si:
            tension.print(parsed_args.title, print_si=True)
        else:
            tension.print(parsed_args.title)

    elif parsed_args.command == 'help':
        print_manual()

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
