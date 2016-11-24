#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nomes import Nome, Supernome

''' define os novos objetos '''
giovanni=Supernome("Giovanni","Nunes")

''' usará automaticamente o __str__ '''
print("O primeiro nome é {}.".format(giovanni))

''' usará explicitamente um dos métodos '''
print("E {} e nome completo.".format(giovanni.escreve_nome_completo()))

''' o que tem dentro da classe? '''
print(giovanni)

exit
