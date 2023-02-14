<img src="https://notas-musicais.readthedocs.io/en/latest/assets/logo.png" width="200">

# Notas musicais
[![Documentation Status](https://readthedocs.org/projects/notas-musicais/badge/?version=latest)](https://notas-musicais.readthedocs.io/en/latest/?badge=latest)
![CI](https://github.com/dunossauro/notas-musicais/actions/workflows/pipeline.yaml/badge.svg)
[![codecov](https://codecov.io/gh/dunossauro/notas-musicais/branch/main/graph/badge.svg?token=OVQQF4IQY2)](https://codecov.io/gh/dunossauro/notas-musicais)

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.

Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um subcomando relacionado a cada ação que a aplicação pode realizar. Como `escalas`, `acordes` e `campo-harmonico`

## Instalação

Para instalação do cli do projeto recomendamos que use o `pipx` para fazer essa instalação:

```bash
pipx install notas-musicais
```

Embora isso seja somente uma recomendação! Você também pode instalar o projeto com o gerenciador de sua preferência. Como o pip:

```bash
pip install notas-musicais
```

## como usar?

### Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:


```bash
notas-musicais escala
```

Retornando os graus e as notas correspondentes a essa escala:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de `F#`:

```bash
notas-musicais escala F#
```

Resultado em:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Alteração na tonalidade da escala

Você pode alterar a tonalidade da escala também! Esse é o segundo parâmetro da linha de comando. Por exemplo, a escala de `D#` maior:

```
notas-musicais escala D# menor

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘

```


## Acordes

Uso básico

```bash
notas-musicais acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variações na cifra

```bash
notas-musicais acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento você usar acordes maiores, menores, dimunito e aumentados


## Campo harmônico

Você pode chamar os campos harmônicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
notas-musicais campo-harmonico

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmetros utilizados são a tônica de `C` e o campo harmônico `maior`.

### Alterações nos campos harmônicos

Você pode alterar os parâmetros da tônica e da tonalidade.

```bash
notas-musicais campo-harmonico [TONICA] [TONALIDADE]
```

#### Alteração na tônica do campo

Um exemplo com o campo harmônico de `E`:

```bash
notas-musicais campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteração da tonalidade do campo

Um exemplo utilizando o campo harmônico de `E` na tonalidade `menor`:

```bash
notas-musicais campo-harmonico E menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag `--help`:

```bash
notas-musicais --help
                                                                       
 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Commands ──────────────────────────────────────────────────────────╮
│ acorde                                                              │
│ campo-harmonico                                                     │
│ escala                                                              │
╰─────────────────────────────────────────────────────────────────────╯
```

### Mais informações sobre os subcomandos

As informações sobre os subcomandos podem ser acessadas usando a flag `--help` após o nome do parâmetro. Um exemplo do uso do `help` nos campos harmônicos:

```bash
notas-musicais campo-harmonico --help
                                                                       
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE] 
                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica do campo harmônico           │
│                                 [default: c]                        │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico       │
│                                 [default: maior]                    │
╰─────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────────────╯
```
