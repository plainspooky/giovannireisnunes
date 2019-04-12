#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Exemplo de função sendo passada como argumento.
"""
from __future__ import print_function


def minha_funcao(i, j):
    """ Recebe dois valores em `i` e `j` e retorna a soma entre eles. """
    return i + j


def outra_funcao(func, *args, **kwargs):
    """ Executa uma função `func` e duplica o valor. """
    return func(*args, **kwargs) * 2


def main():
    """ Função principal """
    print("*** minha_funcao() ***")
    print(minha_funcao(2, 3))

    print("*** outra_funcao() ***")
    print(outra_funcao(minha_funcao, 2, 3))


if __name__ == "__main__":
    main()
