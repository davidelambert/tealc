from pathlib import Path
import csv
import json

PROJECT_ROOT = Path(__file__).parent.parent.parent
charts = PROJECT_ROOT/'tenscalc/data/charts'

with open(PROJECT_ROOT/'tenscalc/data/material_codes.json') as f:
    fullname = json.load(f)

output = {}
for k, v in fullname.items():
    output[k] = {
        'full_name': v,
        'data': dict()
    }

for chart in charts.iterdir():
    with open(chart) as f:
        reader = csv.DictReader(f)
        for r in reader:
            output[chart.stem]['data'][r['gauge']] = float(r['unit_weight'])

with open(PROJECT_ROOT/'tenscalc/data/unit_weights.json', 'w') as f:
    json.dump(output, f, indent=2)
