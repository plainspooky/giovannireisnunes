#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Exemplo de função sendo decorada via passagem de argumento.
"""
from __future__ import print_function


def decora_funcao(func):
    """ Decora a função `func` escrevendo '%%% agora decorada %%%'. """

    def decoracao():
        """ Função aninhada para decorar a função. """
        print("%%% agora decorada %%%")
        func()

    return decoracao


def main():
    """ Função principal """

    def minha_funcao():
        """ Apenas escreve '### minha_funcao() ###'. """
        print("### minha_funcao() ###")

    minha_funcao = decora_funcao(minha_funcao)

    minha_funcao()


if __name__ == "__main__":
    main()
