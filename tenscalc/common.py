import json
import sys

with open('./tenscalc/data/unit_weights.json', 'r') as f:
    data = json.load(f)

with open('./tenscalc/data/frequency_chart.json', 'r') as f:
    freq = json.load(f)

with open('./tenscalc/data/tension_coefs.json', 'r') as f:
    coefs = json.load(f)

with open('./tenscalc/data/material_codes.json', 'r') as f:
    mat_codes = json.load(f)


def validate_material(material):
    just_chars = 11
    if material not in list(mat_codes):
        print('\nERROR: material must be one of the following codes:')
        print('Code'.rjust(just_chars), 'String material', sep='  ')
        print('----'.rjust(just_chars), '---------------', sep='  ')
        for k, v in mat_codes.items():
            print(k.rjust(just_chars), v, sep='  ')
        sys.exit()
    else:
        pass


def validate_pitch(pitch):
    if pitch not in list(freq):
        print('\nERROR: pitch must be in scientific pitch notation,')
        print('       from A0-E5, with uppercase note letter.')
        sys.exit()
    else:
        pass


def get_uw(gauge, material):
    if str(gauge) not in data[material]['data']:
        if material == 'nps' and gauge > 0.054:
            unit_weight = coefs['nps_large'] * (gauge ** 2)
        else:
            unit_weight = coefs[material] * (gauge ** 2)
    else:
        unit_weight = data[material]['data'][str(gauge)]

    return unit_weight


def tension(gauge: float, material: str, pitch: str, scale_length: float, si=False):
    if si:
        gauge = round(gauge / 25.4, 3)
        scale_length = scale_length / 25.4

    if not si and gauge >= 1.0:
        gauge = gauge / 1000

    validate_material(material)
    validate_pitch(pitch)

    unit_weight = get_uw(gauge, material)
    hz = freq[pitch]

    lbs = (unit_weight * (2 * hz * scale_length) ** 2) / 386.4

    if si:
        value = lbs / 2.205
        unit = 'kg'
    else:
        value = lbs
        unit = 'lbs'

    return value, unit
