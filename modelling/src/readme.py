from pathlib import Path
from collections import namedtuple

import pandas as pd
from numpy import power
from statsmodels.api import OLS
from plotnine import *

PROJECT_ROOT = Path(__file__).parent.parent.parent
charts = PROJECT_ROOT/'modelling/charts'
images = PROJECT_ROOT/'modelling/images'


def scatterfit(data, x, y, plot_title,
               point_color='black', line_color='black'):
    """Quick scatterplot with OLS fit line using plotnine.ggplot

    data -- a Pandas dataframe
    x, y -- [string] column names from df
    plot_title -- [string]
    point_color, line_color -- [string]
    Returns: plotnine.ggplot object
    """

    p = ggplot(data, aes(x, y)) +\
        stat_smooth(method='ols', color=line_color,
                    fill=line_color, alpha=0.3) +\
        geom_point(color=point_color, size=2) +\
        labs(title=plot_title)

    return p


def short_table(fitted_model):
    """Abbreviated single-variable OLS results table"""

    coef = round(fitted_model.params['gauge_sq'], ndigits=4)
    se = round(fitted_model.bse['gauge_sq'], ndigits=4)
    t = round(fitted_model.tvalues['gauge_sq'], ndigits=2)
    p = round(fitted_model.pvalues['gauge_sq'], ndigits=4)
    r2 = round(fitted_model.rsquared, ndigits=4)

    table = str('Coef'.rjust(10) + 'SE'.rjust(10) + 't'.rjust(10) +
                'Pr>|t|'.rjust(10) + 'R^2'.rjust(10) + '\n' +
                str(coef).rjust(10) + str(se).rjust(10) + str(t).rjust(10) +
                str(p).rjust(10) + str(r2).rjust(10))

    return table


Material = namedtuple('Material', ['name', 'shortname', 'pcol', 'lcol'])
materials = [
    Material('plain steel', 'ps', 'dimgrey', 'grey'),
    Material('nickel-plated steel', 'nps', 'steelblue', 'cornflowerblue'),
    Material('phosphor bronze', 'pb', 'saddlebrown', 'sienna'),
    Material('80/20 bronze', '8020', 'peru', 'goldenrod'),
    Material('85/15 bronze', '8515', 'darkorange', 'orange'),
    Material('stainless steel roundwound', 'ss', 'royalblue', 'dodgerblue'),
    Material('pure nickel', 'pn', 'slategrey', 'lightslategray'),
    Material('stainless steel flatwound', 'fw', 'darkcyan', 'lightseagreen')
]

readme_top = open(str(PROJECT_ROOT/'modelling/src/readme_top.md'), 'r')
readme = open(str(PROJECT_ROOT/'modelling/README.md'), 'w')
readme.writelines(readme_top.readlines())
readme_top.close()

for mat in materials:
    readme.write(f'\n\n###{mat.name.title()}\n')

    data = pd.read_csv(str(charts/f'{mat.shortname}.csv'))
    data['gauge_sq'] = power(data['gauge'], 2)
    plot = scatterfit(data, x='gauge_sq', y='unit_weight',
                      plot_title=mat.name,
                      point_color=mat.pcol,
                      line_color=mat.lcol)
    plot.save(str(images/f'{mat.shortname}.svg'))
    fit = OLS(data['unit_weight'], data['gauge_sq']).fit()

    readme.write(
        f'![{mat.name} model plot](images/{mat.shortname}.svg)\n\n')
    readme.write(f'```\n{short_table(fit)}\n```\n\n')

readme.close()
