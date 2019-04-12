#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Testa os decoradores
"""
from __future__ import print_function
from json import loads as json_loads

# from decoradores import html  # descomente para saída em HTML
# from decoradores import markdown  # descomente para saída em Markdown


DEFAULT_VALUE = ""
NOTAS_JSON = "notas.json"

# @markdown  # descomente para saída em Markdown
# @html  # descomente para saída em HTML
def tabulate_data(data_dict, sort_keys=True, sort_data=False):
    """ Converte um dicionário em uma lista em forma de tabela com as
    chaves do dicionário formando a primeira linha (cebeçalho) e os dados
    logo em sequência. Recebe o dicionárip em `data_dict` e opcionalmente
    os parâmetros `sort_keys` e `sort_data` como bolianos para respectivamente
    ordenar, ou não, as chaves do dicionário e seus dados. """

    # variáveis
    table_values = []
    temp_header_set = set()

    # itera em todas as chaves do dicionário e alimenta um 'set'.
    for i in data_dict:
        __ = [temp_header_set.add(j) for j in i.keys()]

    # converte o 'set' em uma lista, ordenando a ordem das chaves se o
    # conteúdo da variável `sort_keys` for `True`.
    table_header = list(sorted(temp_header_set) if sort_keys else temp_header_set)

    # para cada componente do cabeçalho, recupera seu valor, ou então
    # usa o valor padrão.
    for j in data_dict:
        table_values.append([j.get(keys, DEFAULT_VALUE) for keys in table_header])

    # ordena os dados se o valor da variável `sort_data` for `True`.
    if sort_data:
        table_values.sort()

    return [table_header] + table_values


def main():
    """ Função principal. """

    # lê o arquivo JSON com as notas (melhor que colocá-lo aqui no código)
    notas_json = json_loads(open(NOTAS_JSON, "r").read())

    # tabula os dados lidos do JSON...
    dados_alunos = tabulate_data(notas_json)

    # imprime na tela (ou salva em disco se for o caso)
    print(dados_alunos)


if __name__ == "__main__":
    main()
