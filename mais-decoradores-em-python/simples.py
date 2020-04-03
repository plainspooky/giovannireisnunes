#!/usr/bin/env python3
from module.decorators import marker


@marker
def mesg(text: str) -> str:
    """
    Retorna uma 'string' em caixa alta.
    """
    return text.upper()


print(
    "Este texto é normal.",
    mesg("Mas este precisa ser marcado."),
    "E este aqui é normal também.",
    sep="\n",
)
