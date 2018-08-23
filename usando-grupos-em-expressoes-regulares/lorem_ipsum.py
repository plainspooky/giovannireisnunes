#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':

    # lê o arquivo com a versão em HTML do _lorem ipsum_
    lorem_ipsum = open('lorem_ipsum.html').read()

    print('Texto emtre <strong>...</strong>:')

    # se for usado apenas uma vez, é possível fazer direto
    for i in re.findall('<strong>(.+)</strong>', lorem_ipsum):
        print('\t- ' + i )

    print('\nTexto entre <em>...</em>:')

    # mas se usar mais de uma vez, compensa criar uma variável.
    italizado = re.compile('<em>(.+)</em>')

    for i in italizado.findall(lorem_ipsum):
        print('\t- ' + i)

    print('')
