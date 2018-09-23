#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

logging.debug('Exibindo mensagem.')
logging.info('Exibindo mensagem')
logging.warning('Exibindo mensagem')
logging.error('Exibindo mensagem')
logging.critical('Exibindo mensagem')

# apenas as duas últimas linh
logging.disable(logging.WARNING)

logging.debug('Não exibindo mensagem.')
logging.info('Não exibindo mensagem')
logging.warning('Não exibindo mensagem')
logging.error('Não exibindo mensagem')
logging.critical('Não exibindo mensagem')
