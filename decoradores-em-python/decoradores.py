#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Exemplo de decoradores
"""


def format_line(format_string, line_to_format, base_string=""):
    """ Formata uma linha da lista, recebe a _string_ a ser formatada em
    `format_string` e a lista contendo os dados em `line_to_format`.
    Retorna uma _string_ contendo os dados formatados. """

    return base_string.join([format_string.format(cell) for cell in line_to_format])


def get_column_width(table_data):
    """ Verifica na tabela em `table_data` a célula mais larga na estrutura e
    define como a largura padrão da coluna. Retorna uma lista com a largura
    para cada coluna. """

    width_temp = []

    # navega na tabela de coluna em coluna.
    for column in range(len(table_data[0])):
        width_temp.append(max([len(str(cell[column])) for cell in table_data]))

    return width_temp


def markdown(func_obj):
    """ (decorador) Formata uma lista em uma tabela em Markdown, recebe a
    função que produz a lista em `func_obj` e retorna a tabela formatada como
    uma _string_. """

    def markdown_format(*args, **kwargs):
        """ Recupera os dados da função `func_obj` e formata uma lista
        em uma tabela Markdown. """

        # recupera os valores gerados pela função.
        table_data = func_obj(*args, **kwargs)
        table_formated = ""
        table_width = get_column_width(table_data)

        # retira a primeira linha da lista para gerar a linha que separa
        # títulos e dados no cabeçalho das tabelas em markdown.
        temp_header = [
            [cell.ljust(table_width[col]) for col, cell in enumerate(table_data.pop(0))]
        ]

        temp_header += [["-" * column for column in table_width]]

        for line in temp_header + table_data:
            table_formated += (
                "|"
                + format_line(
                    " {} |",
                    [
                        str(cell).ljust(table_width[column])
                        for column, cell in enumerate(line)
                    ],
                )
                + "\n"
            )

        return table_formated

    return markdown_format


def html(func_obj):
    """ (decorador) Formata uma lista em uma tabela HTML, recebe a função
    que produz a lista em `func_obj` e retorna a tabela formatada como
    uma _string_. """

    def html_format(*args, **kwargs):
        """ Recupera os dados da função `func_obj` e formata uma lista
        em uma tabela HTML. """

        # recupera os valores gerados pela função.
        table_data = func_obj(*args, **kwargs)

        # converte a primeira linha da lista no cabeçalho, retirando-a
        # da lista.
        table_header = format_line("   <th>{}</th>", table_data.pop(0), "\n")

        # processa o corpo da tabela com o restante da lista.
        table_body = " <tbody>\n"

        for line in table_data:
            table_body += (
                "  <tr>\n" + format_line("   <td>{}</td>", line, "\n") + "\n  </tr>\n"
            )

        table_body += " </tbody>"

        # retorna os dados deviddamente formatados.
        return "<table>\n <thead>\n  <tr>\n{}\n  </tr>\n </thead>\n{}\n</table>".format(
            table_header, table_body
        )

    return html_format
