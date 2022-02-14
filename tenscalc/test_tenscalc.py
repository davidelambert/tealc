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
    cw = (4, 8, 6, 8, 8, 8)
    tw = sum(cw)
    print('')
    print('=' * tw)
    print(title.upper().center(tw))
    print('=' * tw)
    print('Mat.'.ljust(cw[0]),
          'Gauge'.rjust(cw[1]),
          'Pitch'.rjust(cw[2]),
          'Target'.rjust(cw[3]),
          'Actual'.rjust(cw[4]),
          'Diff.'.rjust(cw[5]),
          sep='')
    print('-' * tw)

    if len(lst) == 0:
        print('NO ERRORS!'.center(tw))
    else:
        for err in lst:
            print('{}'.format(err['material']).ljust(cw[0]),
                  '{:6.4f}'.format(err['gauge']).rjust(cw[1]),
                  '{}'.format(err['pitch'].upper()).rjust(cw[2]),
                  '{}'.format(err['target']).rjust(cw[3]),
                  '{:5.2f}'.format(err['actual']).rjust(cw[4]),
                  '{:+.2%}'.format(err['diff']).rjust(cw[5]),
                  sep='')

    print('-' * tw)


fail10 = test_material('ps', alpha=0.1)
assert len(fail10) == 0
# print_failures(fail10, 'failing 10% test')

fail05 = test_material('ps', alpha=0.05)
assert len(fail05) == 0
# print_failures(fail05, 'failing 5% test')
