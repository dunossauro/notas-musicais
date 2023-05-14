from notas_musicais.constantes import ESCALAS, NOTAS


class EscalaError(Exception):
    def __init__(self) -> None:
        super().__init__(
            'Essa escala não existe ou não foi implementada. '
            f'Tente uma dessas {list(ESCALAS.keys())}'
        )


class NotaError(Exception):
    def __init__(self) -> None:
        super().__init__(f'Essa nota não existe, tente uma dessas {NOTAS}')
