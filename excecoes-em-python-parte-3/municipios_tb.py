#!/usr/bin/env python3
"""Exceções em Python - parte 3 (versão com traceback) """
# -*- coding: utf-8 -*-
from sys import argv, stderr
from traceback import print_exc

EXIBE_TRACEBACK = True


class ParseError(Exception):
    """A exceção customizada utilizada pelo 'parser'."""

    def __init__(self, mensagem, linha=0):
        """Construtor da classe, recebe o texto do erro (mensagem) e
        também o número da linha onde ocorreu (opcional)."""
        self.mensagem = mensagem
        self.linha = linha

    def __str__(self):
        """Imprime a mensagem de erro."""
        return "Erro: {}".format(self.mensagem) + \
            (" na linha {}!".format(self.linha) if self.linha > 0 else "!")


class Municipios(object):
    """Classe que armazena os municípios por região e estado."""
    # esta classe só aceita três níveis hierárquicos
    REGIAO = 1
    ESTADO = 2
    CIDADE = 3

    def __init__(self, municipios):
        """Construtor da classe, recebe o nome do arquivo a ser lido."""
        try:
            with open(municipios, "r") as arquivo:
                self.__municipios = self.__parser(arquivo)
        except FileNotFoundError:
            raise ParseError("Arquivo não encontrado") from FileNotFoundError

    @property
    def regioes(self):
        """Propriedade `regioes`, retorna as regiões existentes."""
        return [i for i in self.__municipios.keys()]

    def estados(self, regiao):
        """Retorna os estados de uma região específica."""
        return [i for i in self.__municipios[regiao].keys()]

    def municipios(self, regiao, estado):
        """Retorna os municípios de um determinado estado."""
        return self.__municipios[regiao][estado]

    def __parser(self, arquivo):
        """Interpreta o arquivo texto e retorna os dados em um dicionário
        ou chamará a exceção `ParseError` caso ocorra algo de errado."""
        corrente = linha = 0
        municipios = {}

        for itens in arquivo:
            linha += 1
            if itens is not "\n":
                nivel, valor = itens.strip().split(":")
                nivel = int(nivel)
                if nivel <= (corrente + 1):
                    if nivel == self.REGIAO:
                        regiao = valor
                        municipios[regiao] = {}
                    elif nivel == self.ESTADO:
                        estado = valor
                        municipios[regiao][estado] = []
                    elif nivel == self.CIDADE:
                        municipios[regiao][estado].append(valor)
                    else:
                        raise ParseError("Nível hierárquico inválido", linha)
                    corrente = nivel
                else:
                    raise ParseError("Hierarquia incorreta", linha)

        return municipios

    def __str__(self):
        """Retorna `lista de municípios` ao se imprimir o objeto."""
        return "lista de municípios"


def main():
    try:
        brasil = Municipios(argv[1])
    except ParseError as erro:
        # informa o erro e sai!
        if EXIBE_TRACEBACK:
            print_exc(file=stderr)
        print(erro)
        exit(1)
    else:
        # imprime os municípios do Rio de Janeiro.
        print(", ".join(brasil.municipios("Sudeste", "Rio de Janeiro")))


if __name__ == "__main__":
    main()
