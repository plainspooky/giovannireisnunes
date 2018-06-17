#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from time import sleep
from sys import stdout

print("Este programa contará até 100.")

contador = 0
while contador < 100:
    print (".", end="")
    stdout.flush() # força a atualização da tela.
    try:
        if contador == 25:
            comando_inexistente
        elif contador == 50:
            limite = int("abc")
    except NameError:
        print("<<\nexceção interceptada\n>>", end="")
    contador += 1
    sleep(.03125) # espera 1/32 segundos.

print (" FIM!")
    
