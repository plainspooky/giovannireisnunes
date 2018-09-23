#!/usr/bin/env python
""" hal_quotes.py : Exemplo de uso do módulo 'logging' dentro de uma função.
"""
# -*- coding: utf-8 -*-
from __future__ import print_function
from os import environ
import logging


# Use COLS para alterar a largura do terminal
COLUMNS = int(environ.get('COLS', 80)) - 1

# As citações do HAL9000, extraídas de:
# https://en.wikiquote.org/wiki/2001:_A_Space_Odyssey_(film)
QUOTES = {
    'DEBUG': 'Affirmative, Dave. I read you.',
    'INFO': 'This mission is too important for me to allow you to jeopardize it.',
    'WARNING': 'Without your space helmet, Dave, you\'re going to find that rather difficult.',
    'ERROR': 'I\'m sorry, Dave. I\'m afraid I can\'t do that.',
    'CRITICAL': 'Dave, this conversation can serve no purpose any more. Goodbye'
}

# Recupera as chaves de `QUOTES` (É preguiça que chama)
LEVELS = QUOTES.keys()

# As cores utilizadas
COLORS = {
    'NONE': (79, 79, 127),
    'DEBUG': (0, 191, 255),
    'INFO': (0, 192, 0),
    'WARNING': (255, 255, 0),
    'ERROR': (255, 127, 0),
    'CRITICAL': (255, 31, 0),
}


def colored(text, color='NONE'):
    """ Muda as cores do texto. Só funcionará em terminais com suporte
    a este recurso. """
    red, green, blue = COLORS.get(color)
    return "\x1b[38;2;{r};{g};{b}m{msg}\x1b[0m".format(
        r=red, g=green, b=blue, msg=text)


def hal9000_quotes(new_level):
    """ Escreve as citações do HAL na STDERR. """
    # recupera o logger do programa
    hal_log = logging.getLogger(__name__)

    # define o novo nível de log
    hal_log.setLevel(new_level)

    # exibe as mensagens
    hal_log.debug(colored(QUOTES['DEBUG'], 'DEBUG'))
    hal_log.info(colored(QUOTES['INFO'], 'INFO'))
    hal_log.warning(colored(QUOTES['WARNING'], 'WARNING'))

    # quando em 'DEBUG', repita a mensagem 4 vezes...
    times = 4 if new_level == 'DEBUG' else 1
    for __ in range(0, times):
        hal_log.error(colored(QUOTES['ERROR'], 'ERROR'))

    hal_log.critical(colored(QUOTES['CRITICAL'], 'CRITICAL'))


def main():
    """ Função principal. """

    # inicializa o módulo logging
    logging.basicConfig(level=logging.DEBUG,
                        format='2001-Sep-28 - %(levelname)s - %(message)s')

    # brinca de publicar mensagens
    for level in reversed(list(LEVELS)):
        hal9000_quotes(level)
        logging.shutdown()
        print(colored('-' * COLUMNS))


if __name__ == '__main__':
    main()
