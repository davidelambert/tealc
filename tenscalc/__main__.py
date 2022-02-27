import argparse
import sys
from .common import tension

helpstring = '''usage: tenscalc <gauge> <material> <pitch> <length> [--si]
       tenscalc --help

Required arguments:
  gauge     String gauge in inches, or in mm with the --si flag.
            Gauges in inches may be specified in thousandths of an inch:
            "11" or ".011" are both valid
  material  Code for string construction material. Current options are:
              Code  Material
              ----  --------
                ps  Plain Steel
               nps  Nickel-Plated Steel Wound
                pb  Phosphor Bronze Wound
              8020  80/20 Bronze Wound
              8515  85/15 Bronze Wound
                ss  Stainless Steel Roundwound
                fw  Stainless Steel Flatwound
                pn  Pure Nickel Wound
  pitch     Tuned pitch of string in scientific pitch notation, from A0-E5.
            Examples of open-string pitches in standard tunings:
                Guitar: E2, A2, D3, G3, B3, E4
                  Bass: (B0), E1, A1, D2, G2
              Mandolin: G3, D4, A4, E5
                 Banjo: G4, D3, G3, B3, D4
  length    Scale length of instrument in inches, or in mm with the --si flag.

Optional arguments:
  --si      <gauge> and <length> are interpreted as mm; tension is returned in kg.
  --help    Show this help message and exit

Examples:
  tenscalc .011 ps E4 25.5
  tenscalc --si 1.37 pb E2 632.5'''

parser = argparse.ArgumentParser(prog='tenscalc', add_help=False)
parser.add_argument('gauge', nargs='?', type=float)
parser.add_argument('material', nargs='?')
parser.add_argument('pitch', nargs='?')
parser.add_argument('length', nargs='?', type=float)
parser.add_argument('--si', action='store_true')
parser.add_argument('--help', action='store_true')
args = parser.parse_args()

if args.help:
    print(helpstring)
    sys.exit()
else:
    value = tension(args.gauge, args.material, args.pitch,
                    args.length, args.si)
    if args.si:
        units = 'kg'
    else:
        units = 'lbs'
    print('{:.2f} {}'.format(value, units))
