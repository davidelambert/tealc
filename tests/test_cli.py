from pathlib import Path
import math

from click.testing import CliRunner

import tealc.cli as cli

TEST_DIR = Path(__file__).parent.resolve()


def test_cli_string():
    runner = CliRunner()
    result = runner.invoke(cli.string, '10 ps e4 25.5'.split())
    assert result.exit_code == 0
    assert result.output == '16.4 lb\n'


def test_cli_string_si():
    runner = CliRunner()
    result = runner.invoke(cli.string, '--si .25 ps e4 648'.split())
    assert result.exit_code == 0
    assert result.output == '7.4 kg\n'
    # TODO: math.isclose(), probably via regex


def test_cli_set():
    args = ('-l 25.5'.split()
            + '-s 10 ps e4'.split()
            + '-s 13 ps b3'.split()
            + '-s 17 ps g3'.split()
            + '-s 26 nps d3'.split()
            + '-s 36 nps a2'.split()
            + '-s 46 nps e2'.split())
    runner = CliRunner()
    result = runner.invoke(cli.set, args)
    assert result.exit_code == 0
    assert 'Total:  104.1 lb\n' in result.output

# TODO: debug this:
# ========================================
# Scale length: 25.5mm
# ----------------------------------------
#      Pitch     Gauge  Material   Tension
# ----------------------------------------
#         E4     0.250        ps    0.0 kg
#         B3     0.330        ps    0.0 kg
#         G3     0.430        ps    0.0 kg
#         D3     0.660       nps    0.0 kg
#         A2     0.910       nps    0.0 kg
#         E2     1.170       nps    0.0 kg
# ----------------------------------------
#                         Total:    0.1 kg
#                         ================


def test_cli_file():
    runner = CliRunner()
    result = runner.invoke(cli.file, str(TEST_DIR/'data/SetFiles/gbl'))
    assert result.exit_code == 0
    assert 'Total:  104.1 lb\n' in result.output


def test_cli_materials():
    runner = CliRunner()
    result = runner.invoke(cli.materials)
    assert result.exit_code == 0
    assert 'code  material' in result.output
