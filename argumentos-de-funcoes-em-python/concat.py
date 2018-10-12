#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

def concat(*args):
    """ Concatena todas as strings passadas para a função """
    return ''.join([i for i in args])


if __name__ == '__main__':
    print(concat('a', 'b', 'c'))
    print(concat('caixa', ' ', 'de', ' ', 'madeira'))
