#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import logging

logging.basicConfig(filename='registro_em_arquivo.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

logging.debug('Iniciando o programa.')

for i in range(1,9):
    print('+' * i, ' ', end='' if i < 8 else '\n')

logging.debug('Finalizando o programa.')

logging.shutdown()
