#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from time import sleep

try:
    print('Aguarde 5 segundos para a exceção...')
    sleep(5)
    raise ValueError
except:
    print('Ocorreu uma exceção:')
    raise
    print('Esta mensagem não será impressa.')
