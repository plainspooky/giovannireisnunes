#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
from sys import argv

nome_do_arquivo = argv[1]

dados = "".join([chr(randint(32, 126)) for i in range(65536)])

try:
    status = 0
    with open(nome_do_arquivo, 'w') as f:
        f.write(dados)
except IOError as err:
    if 'Permission denied' in str(e):
        print('Você não pode criar arquivos aí!')
        status = 1
    else:
        print('Impossível escrever os dados em `{}`'
              .format(nome_do_arquivo))
        status = 2
else:
    print('Arquivo salvo com sucesso!')
finally:
    if status > 0:
        exit(status)

print("Faz outras coisas e depois termina.")
