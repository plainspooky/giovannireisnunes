#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MinhaExcecaoError(Exception):
    pass


try:
    erro = False

    # lista de comandos que mudarão o estado de 'erro' -->
    erro = True
    # <-- lista de comandos que mudarão o estado de 'erro'

    if erro:
        raise MinhaExcecaoError("Ocorreu um erro!")

except MinhaExcecaoError as mensagem:
    print(mensagem)
    exit(1)
