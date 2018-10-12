#!/usr/bin/env python
from __future__ import print_function


def sem_argumentos():
    return 1


def um_argumento(i):
    return i + i


def dois_argumentos(i, j):
    return i + j


def argumentos_padrao(i, j=1):
    return i + j


def argumentos_padrao_2(i, j=0, k=0):
    return i + j + k


def todos_os_argumentos(*args):
    return sum(args)


def alguns_argumentos(i, *args):
    return [i * j for j in args]


def alguns_argumentos_com_padrao(i, *args, j=2):
    return [j + i * k for k in args]


def argumentos_em_dicionario(**kargs):
    for k, v in kargs.items():
        print('{} = {}'.format(k, v))


if __name__ == '__main__':
    print('Use \'from argumentos import *\' a partir do console do Python.')
