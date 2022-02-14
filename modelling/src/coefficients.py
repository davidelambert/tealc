from pathlib import Path
import json
import pandas as pd
from numpy import power
from statsmodels.api import OLS

PROJECT_ROOT = Path(__file__).parent.parent.parent


def get_coef(csv):
    """Return b from the OLS model unit_weight = b * gauge^2 + e."""

    data = pd.read_csv(csv)
    data['gauge_sq'] = power(data.gauge, 2)
    coef = round(OLS(data.unit_weight, data.gauge_sq).fit().params[0], 4)

    return coef


charts = PROJECT_ROOT/'modelling/charts'
coefs = {}
for chart in charts.iterdir():
    string_type = chart.stem
    if not string_type.endswith('_D'):
        coef = get_coef(chart)
        coefs[string_type] = coef

with open(str(PROJECT_ROOT/'tenscalc/src/tension_coefs.json'), 'w') as f:
    json.dump(coefs, f, sort_keys=True, indent=2)
