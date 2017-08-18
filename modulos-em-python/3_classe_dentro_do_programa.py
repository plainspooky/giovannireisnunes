#!/usr/bin/env python3
# exemplo 3
class Calculos(object):
    a=0
    b=0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def media(self):
        return (self.a + self.b)/2.0

calculos = Calculos(3, 2)
print(calculos.media())
