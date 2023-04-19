"""
AAA - 3A - A3

Arange - Act - Assets!
Arrumar - Agir - Garantir!
"""
import re

from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Act - Chamo o que testar
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError, match=re.escape(mensagem_de_erro)):
        escala(tonica, tonalidade)


def test_deve_retornar_um_erro_dizendo_que_a_escala_não_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_de_erro = (
        'Essa escala não existe ou não foi implementada. '
        f'Tente uma dessas {list(ESCALAS.keys())}'
    )

    with raises(KeyError, match=re.escape(mensagem_de_erro)):
        escala(tonica, tonalidade)


@mark.parametrize(
    'tonica,tonalidade, esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D', 'maior', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('D#', 'maior', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('E', 'maior', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('F#', 'maior', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('G', 'maior', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('G#', 'maior', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('A', 'maior', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('A#', 'maior', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('B', 'maior', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    resultado = escala(tonica, tonalidade)
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
