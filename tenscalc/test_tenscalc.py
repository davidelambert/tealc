from math import log
import json
import tenscalc

with open('./testdata.json', 'r') as f:
    d = json.load(f)


def test_interval(material, pitch, gauge, target, alpha=0.1):
    uw = tenscalc.get_uw(gauge, material)
    tens = tenscalc.tension(uw, pitch)
    moe = (tens - alpha*tens, tens + alpha*tens)
    if moe[0] <= target <= moe[1]:
        passing = True
    else:
        passing = False
    result = passing, tens
    return result


def test_material(material, alpha=0.1):
    lst = []
    for pitch in list(d[material]['pitches']):
        for tup in d[material]['pitches'][pitch]:
            gauge = tup[0]
            target = tup[1]
            passing, actual = test_interval(material, pitch, gauge,
                                            target, alpha)
            if not passing:
                err = {'material': material,
                       'gauge': gauge/1000,
                       'pitch': pitch,
                       'target': target,
                       'actual': actual,
                       'diff': log(actual)-log(target)}
                lst.append(err)
    return(lst)


def print_failures(lst, title=''):
    cw = 8
    tw = 5 * cw
    print('')
    print('=' * tw)
    print(title.upper().center(tw))
    print('=' * tw)
    print('Gauge'.ljust(cw),
          'Pitch'.ljust(cw),
          'Target'.ljust(cw),
          'Actual'.ljust(cw),
          'Diff.'.ljust(cw),
          sep='')
    print('-' * tw)

    if len(lst) == 0:
        print('NO ERRORS!'.center(tw))
    else:
        for err in lst:
            print('{:6.4f}'.format(err['gauge']).ljust(cw),
                  '{}'.format(err['pitch'].upper()).ljust(cw),
                  '{}'.format(err['target']).ljust(cw),
                  '{:5.2f}'.format(err['actual']).ljust(cw),
                  '{:+.2%}'.format(err['diff']).ljust(cw),
                  sep='')

    print('-' * tw)


fail10 = test_material('ps', alpha=0.1)
try:
    assert len(fail10) == 0
except AssertionError:
    print_failures(fail10, 'failing 10% test')

fail05 = test_material('ps', alpha=0.05)
try:
    assert len(fail05) == 0
except AssertionError:
    print_failures(fail05, 'failing 5% test')
