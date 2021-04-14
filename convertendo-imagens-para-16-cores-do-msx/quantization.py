#!/usr/bin/env python3
from PIL import Image

from functions import count_colors, quantize_colors

image = Image.open("sample_256x192.png")

# cria a tabela de frequência de cores
colors = count_colors(image)

# monta a paleta de 16 cores para a imagem
palette = quantize_colors(colors, 16)

# imprime relação das cores em hexadecimal...
print("\n".join((f"#{r:02x}{g:02x}{b:02x}" for r, g, b in palette)))
