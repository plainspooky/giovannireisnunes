#!/usr/bin/env python3
from typing import Callable

from module.decorators import multiply

# o valor inicial de 
f = 2


@multiply(f)
def to_float(i) -> float:
    """
    Converte um nome em `i` para ponto flutuante.
    """
    return float(i)


if __name__ == "__main__":
    print(to_float(4))
    f += 1  # não vai funcionar
    print(to_float(4))
