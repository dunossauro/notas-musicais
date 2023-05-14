"""
# CONSTANTES
As notas e escalas estão definidas nas respectivas constantes `NOTAS` e `ESCALAS`.
## NOTAS
As notas estão sendo definidas em uma constante `NOTAS`.
Foi optado por manter somente as notas no formato Natural e o Sustenido (#) para a simplificação do fluxo de trabalho.
Embora não esteja totalmente correto. Para ver as 12 notas você pode:

```py
>>> from teoria_musical.constantes import NOTAS
>>> NOTAS
['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

```

## ESCALAS
As escalas estão implementadas em uma constante chamada `ESCALAS`.
Que é um dicionário onde as chaves são os nomes das escalas.
Se quiser ver todas as escalas implementadas pode usar:

```py
>>> from teoria_musical.constantes import ESCALAS
>>> ESCALAS['maior']
(0, 2, 4, 5, 7, 9, 11)

```
## GPT

```GPT
Poderia formatar um texto para mim?

link: https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes
Gostaria que extraísse da tabela no link acima os "Integers notation"
 e formatasse como o exemplo a baixo:


ESCALAS = {'major': (0, 2, 4, 5, 7, 9, 11), 'minor': (0, 2, 3, 5, 7, 8, 10)}
```
"""


NOTAS = 'C C# D D# E F F# G G# A A# B'.split()


ESCALAS = {
    'maior': (0, 2, 4, 5, 7, 9, 11),
    'menor': (0, 2, 3, 5, 7, 8, 10),
    'Acoustic scale or Lydian dominant scale': (0, 2, 4, 6, 7, 9, 10),
    'Aeolian mode or natural minor scale': (0, 2, 3, 5, 7, 8, 10),
    'Algerian scale': (0, 2, 3, 6, 7, 9, 11, 12, 14, 15, 17),
    'Altered scale or Super Locrian scale': (0, 1, 3, 4, 6, 8, 10),
    'Augmented scale': (0, 3, 4, 7, 8, 11),
    'Bebop dominant scale': (0, 2, 4, 5, 7, 9, 10, 11),
    'Blues scale': (0, 3, 5, 6, 7, 10),
    'Chromatic scale': (
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ),
    'Dorian mode': (0, 2, 3, 5, 7, 9, 10),
    'Double harmonic scale': (0, 1, 4, 5, 7, 8, 11),
    'Enigmatic scale': (0, 1, 4, 6, 8, 10, 11),
    'Flamenco mode': (0, 1, 4, 5, 7, 8, 11),
    'Gypsy scale': (0, 2, 3, 6, 7, 8, 10),
    'Half diminished scale': (0, 2, 3, 5, 6, 8, 10),
    'major scale': (0, 2, 4, 5, 7, 8, 11),
    'minor scale': (0, 2, 3, 5, 7, 8, 11),
    'Yo scale': (0, 3, 5, 7, 10),
    'Harmonic Scale': (144,),
    'Ionian mode or major scale': (0, 2, 4, 5, 7, 9, 11),
    'Locrian mode': (0, 1, 3, 5, 6, 8, 10),
    'Lydian augmented scale': (0, 2, 4, 6, 8, 9, 11),
    'Lydian mode': (0, 2, 4, 6, 7, 9, 11),
    'Major Locrian scale': (0, 2, 4, 5, 6, 8, 10),
    'Major pentatonic scale': (0, 2, 4, 7, 9),
    'Melodic minor scale': (0, 2, 3, 5, 7, 9, 11),
    'Minor pentatonic scale': (0, 3, 5, 7, 10),
    'Mixolydian mode or Adonai malakh mode': (0, 2, 4, 5, 7, 9, 10),
    'Neapolitan major scale': (0, 1, 3, 5, 7, 9, 11),
    'Neapolitan minor scale': (0, 1, 3, 5, 7, 8, 11),
    'Octatonic scale': (0, 1, 3, 4, 6, 7, 9, 10),
    'Pentatonic scale': (0, 2, 4, 7, 9),
    'Persian scale': (0, 1, 4, 5, 6, 8, 11),
    'Phrygian dominant scale': (0, 1, 4, 5, 7, 8, 10),
    'Phrygian mode': (0, 1, 3, 5, 7, 8, 10),
    'Prometheus scale': (0, 2, 4, 6, 9, 10),
    'Tritone scale': (0, 1, 4, 6, 7, (10)),
    'Ukrainian Dorian scale': (0, 2, 3, 6, 7, 9, 10),
    'Whole tone scale': (0, 2, 4, 6, 8, 10),
}
