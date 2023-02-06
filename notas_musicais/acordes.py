"""
Módulo de acordes.

O módulo de acordes conta com funções e ferramentas necessárias para a geração de acordes.
"""
from notas_musicais.escalas import NOTAS, escala


def _menor(cifra):
    nota, _ = cifra.split('m')

    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=1)]
        graus = ['I', 'III-', 'V+']

    else:
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']

    return notas, graus


def semitom(nota: str, *, intervalo: int) -> str:
    """
    Calcula a distância em semitons para uma outra nota usando intervalos.

    Parameters:
        nota: Uma nota qualquer
        intervalo: um intervalo em semitons

    Returns:
        Uma nota correspondente ao intervalo

    Examples:
        >>> semitom('C', intervalo=+1)
        'C#'

        >>> semitom('c', intervalo=-1)
        'B'
    """
    pos = NOTAS.index(nota.upper()) + intervalo

    return NOTAS[pos % 12]


def triade(nota, tonalidade) -> list[str]:
    """
    Gera triades a partir de uma tônica e uma tonalidade.

    Parameters:
        nota: Uma nota da qual se deseja obter um acorde
        tonalidade: Tonalidade na qual será formado o acorde

    Returns:
        A tríade do acorde referente a nota e a tonalidade

    Examples:
        >>> triade('C', 'maior')
        ['C', 'E', 'G']

        >>> triade('C', 'menor')
        ['C', 'D#', 'G']
    """
    graus = (0, 2, 4)
    notas_da_escala, _ = escala(nota, tonalidade).values()

    return [notas_da_escala[grau] for grau in graus]


def acorde(cifra: str) -> dict[str, list[str]]:
    """
    Gera as notas de um acorde partindo de uma cifra.

    Parameters:
        cifra: Um acorde em forma de cifra.

    Returns:
        Um dicionário com as notas e os graus correpondes a escala maior.

    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

        >>> acorde('Cm')
        {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}

        >>> acorde('C°')
        {'notas': ['C', 'D#', 'F#'], 'graus': ['I', 'III-', 'V-']}

        >>> acorde('C+')
        {'notas': ['C', 'E', 'G#'], 'graus': ['I', 'III', 'V+']}

        >>> acorde('Cm+')
        {'notas': ['C', 'D#', 'G#'], 'graus': ['I', 'III-', 'V+']}
    """
    if 'm' in cifra:
        notas, graus = _menor(cifra)

    elif '°' in cifra:
        nota, _ = cifra.split('°')
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=-1)]
        graus = ['I', 'III-', 'V-']

    elif '+' in cifra:
        nota, _ = cifra.split('+')
        tonica, terca, quinta = triade(nota, 'maior')
        notas = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus = ['I', 'III', 'V+']

    else:
        notas = triade(cifra, 'maior')
        graus = ['I', 'III', 'V']

    return {'notas': notas, 'graus': graus}
