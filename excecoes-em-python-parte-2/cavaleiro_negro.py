#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from time import sleep
import CavaleiroNegro

print("\x1b[3J{}\x1b[2;1H".format(CavaleiroNegro.imprime()))

for mensa in ["Ninguém passará! ", "Então você morrerá! ",
              "Não me afasto para ninguém. "]:
    sleep(.125)
    print(mensa)

fala = 0
while True:
    try:
        sleep(.25)
        if fala == 0:
            raise NameError
        elif fala == 1:
            raise TypeError
        elif fala == 2:
            raise ValueError
        elif fala == 3:
            raise ZeroDivisionError

    except NameError:
        print("Foi apenas um arranhão. ")
    except TypeError:
        print("Vamos, seu maricas! ")
    except ValueError:
        print("Oh, está amarelando, hem? ")
    except ZeroDivisionError:
        print("Covarde! Covarde! ")
    except KeyboardInterrupt:
        print("\nOk, considero um empate! ")
        break
    else:
        if fala < 12:
            print("Sou invencível! ")
    finally:
        fala += 1

print("\x1b[24;1H", end="")
exit(0)
