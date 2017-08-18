#!/usr/bin/env python3
# exemplo 7
import sys
sys.path.append('/tmp')

import meus_modulos

calculos = meus_modulos.Calculos(3, 2)
print(calculos.media())
