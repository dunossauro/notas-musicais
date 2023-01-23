from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout():
    result = runner.invoke(app, ['escala'])
    assert result.exit_code == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_deve_conter_as_notas_na_resposta(nota):
    result = runner.invoke(app, ['escala'])
    assert nota in result.stdout


@mark.parametrize('nota', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_escala_cli_deve_conter_as_notas_na_resposta_de_fa(nota):
    result = runner.invoke(app, ['escala', 'F'])
    assert nota in result.stdout


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_deve_conter_todos_os_graus(grau):
    result = runner.invoke(app, ['escala', 'F'])
    assert grau in result.stdout


@mark.parametrize('nota', ['C', 'E', 'G'])
def test_acorde_cli_deve_conter_as_notas_na_resposta(nota):
    result = runner.invoke(app, ['acorde'])
    assert nota in result.stdout


@mark.parametrize('grau', ['I', 'III', 'V'])
def test_escala_cli_deve_conter_todos_os_graus(grau):
    result = runner.invoke(app, ['escala', 'F'])
    assert grau in result.stdout
