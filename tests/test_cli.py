from pathlib import Path

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


def test_cli_set_si():
    args = ('--si -l 648'.split()
            + '-s .25 ps e4'.split()
            + '-s .33 ps b3'.split()
            + '-s .43 ps g3'.split()
            + '-s .66 nps d3'.split()
            + '-s .91 nps a2'.split()
            + '-s 1.17 nps e2'.split())
    runner = CliRunner()
    result = runner.invoke(cli.set, args)
    assert result.exit_code == 0
    assert 'Total:   47.4 kg\n' in result.output


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
