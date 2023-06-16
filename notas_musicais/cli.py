from rich.console import Console
from rich.table import Table
from typer import Argument, Context, Exit, Option, Typer

from notas_musicais import __version__
from notas_musicais.acordes import acorde as _acorde
from notas_musicais.campo_harmonico import campo_harmonico as _campo_harmonico
from notas_musicais.escalas import escala as _escala

console = Console()
app = Typer()


def version_func(flag):
    if flag:
        print(__version__)
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def main(
    ctx: Context,
    version: bool = Option(False, callback=version_func, is_flag=True),
):
    message = """Forma de uso: [b]notas-musicais [SUBCOMANDO] [ARGUMENTOS][/]

 Existem 3 subcomandos disponíveis para essa aplicação

- [b]acorde[/]: Fornece um cliente para desvendar acordes
- [b]escala[/]: Fornece uma escala com base em uma tônica
- [b]campo-harmonico[/]: Fornece um campo harmonico com base em uma tônica

[b]Exemplos de uso:[/]
notas-musicais acorde cm+

notas-musicais acorde cm+

notas-musicais acorde cm+

[b]Para mais informações rápidas: [red]notas-musicais --help[/]

[b]Para informações detalhadas: [blue][link=http://notas-musicais.readthedocs.io]acesse a documentação![/]
"""
    if ctx.invoked_subcommand:
        return
    console.print(message)


@app.command()
def escala(
    tonica: str = Argument('c', help='Tônica da escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da escala'),
):
    table = Table()

    notas, graus = _escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)

    console.print(table)


@app.command()
def acorde(
    cifra: str = Argument('C', help='Cifra de um acorde'),
):
    table = Table()

    notas, graus = _acorde(cifra).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)

    console.print(table)


@app.command()
def campo_harmonico(
    tonica: str = Argument('c', help='Tônica do campo harmônico'),
    tonalidade: str = Argument('maior', help='Tonalidade do campo harmônico'),
):
    table = Table()

    acordes, graus = _campo_harmonico(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*acordes)

    console.print(table)
