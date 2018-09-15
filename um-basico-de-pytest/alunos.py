#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from json import loads
from medias import media_aritmetica

alunos = loads(open('alunos.json', 'r').read())

for aluno in alunos:
    nome, notas = aluno.items()
    print('{}\t'.format(aluno.get('nome')), end='')
    media = media_aritmetica(aluno.get('notas'))
    if media is not None:
        print('{:.3f}'.format(media))
    else:
        print('sem notas')
