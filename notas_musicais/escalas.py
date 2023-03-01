"""
Módulo das escalas musicais.

Attributes:
   ESCALAS: Escalas implementadas usando a notação de inteiros
   NOTAS: Notas musicais

# ESCALAS

A escalas estão implementadas em uma constande chamada `ESCALAS`. Que é um dicionário onde as chaves são as escalas. Se quiser ver todas as escalas implementadas pode usar:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import ESCALAS
>>> ESCALAS
{'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)...}

```

A notação inteira para as escalas foi retirada da página [List of musical scales and modes](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes) na wikipedia.

tip: Dica!
    Você pode contribuir com novas escalas usando a notação inteira:
    [Escalas wikipedia](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes).
    Todos os Pull Requests serão bem vindos! :heart:

# NOTAS

As notas estão sendo definidas em uma contasnte `NOTAS`. Para ver as 12 notas você pode:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import NOTAS
>>> NOTAS
['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']

```
"""
NOTAS = 'C C# Db D D# Eb E F F# Gb G G# Ab A A# Bb B'.split()
NOTAS_COM_SUSTENIDO = 'C C# D D# E F F# G G# A A# B'.split()
NOTAS_COM_BEMOL = 'C Db D Eb E F Gb G Ab A Bb B'.split()

ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala apartir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonialidade da escala

    Returns:
        Um dicionário com as notas da escala e os graus.

    Raises:
        ValueError: Caso a tônica não seja uma nota valida.
        KeyError: Caso a escala não exista ou não tenha sido implementada.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    tonica = tonica.upper()
    notas = NOTAS_COM_SUSTENIDO

    if len(tonica) > 1:
        tonica = tonica[0] + tonica[1].lower()
        if tonica[1] == 'b':
            notas = NOTAS_COM_BEMOL

    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = notas.index(tonica)
    except ValueError:
        raise ValueError(
            f'Essa nota não existe, tente uma dessas {NOTAS}'
        )
    except KeyError:
        raise KeyError(
            'Essa escala não existe ou não foi implementada. '
            f'Tente uma dessas {list(ESCALAS.keys())}'
        )

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(notas[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
