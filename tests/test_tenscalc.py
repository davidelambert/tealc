from pathlib import Path
from math import log
import json
import common

PROJECT_ROOT = Path(__file__).parent.parent

magic_number = 40
with open(PROJECT_ROOT/'tenscalc/data/testdata.json', 'r') as f:
    d = json.load(f)


def test_interval(material, pitch, gauge, target, alpha=0.1):
    uw = common.get_uw(gauge, material)
    tens = common.tension(uw, pitch, length=25.5)
    moe = (tens - alpha*tens, tens + alpha*tens)
    if moe[0] <= target <= moe[1]:
        passing = True
    else:
        passing = False
    result = passing, tens
    return result


def test_material(material, alpha=0.1):
    lst = []
    for pitch in list(d[material]):
        for tup in d[material][pitch]:
            gauge = tup[0]
            target = tup[1]
            passing, actual = test_interval(material, pitch, gauge,
                                            target, alpha)
            if not passing:
                err = {'gauge': gauge/1000,
                       'pitch': pitch,
                       'target': target,
                       'actual': actual,
                       'diff': log(actual)-log(target)}
                lst.append(err)
    report = {'material': material, 'alpha': alpha, 'errors': lst}
    return(report)


def print_failures(report):
    errlist = report['errors']
    title = f"{int(report['alpha'] * 100)}% TEST FAILURES"
    tw = magic_number
    cw = magic_number // 5
    print('-' * tw)
    print(title.center(tw))
    print('-' * tw)
    print('Gauge'.ljust(cw),
          'Pitch'.ljust(cw),
          'Target'.ljust(cw),
          'Actual'.ljust(cw),
          'Diff.'.ljust(cw),
          sep='')
    print('-' * tw)

    for err in errlist:
        print('{:6.4f}'.format(err['gauge']).ljust(cw),
              '{}'.format(err['pitch'].upper()).ljust(cw),
              '{}'.format(err['target']).ljust(cw),
              '{:5.2f}'.format(err['actual']).ljust(cw),
              '{:+.2%}'.format(err['diff']).ljust(cw),
              sep='')


for mat in list(d):
    header = ' ' + mat.upper() + ' '
    print('\n\n', header.center(magic_number, '='), sep='')
    for a in [0.1, 0.05]:
        rpt = test_material(material=mat, alpha=a)
        try:
            assert len(rpt['errors']) == 0
        except AssertionError:
            print_failures(rpt)
