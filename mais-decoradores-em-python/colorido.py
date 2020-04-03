#!/usr/bin/env python3
from module.colors import TangoColors
from module.decorators import marker2

tango = TangoColors()


@marker2(tango.sky[2], tango.orange[1])
def greetings() -> str:
    """
    Retorna um "Olá mundo!"
    """
    return " Olá mundo! "


print(greetings())
