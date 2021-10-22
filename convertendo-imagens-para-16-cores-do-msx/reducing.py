#!/usr/bin/env python3
from PIL import Image

from functions import count_colors, quantize_colors, reduce_colors

image = Image.open("sample_256x192.png")

# recupera a lista de cores
colors = count_colors(image)

# cria a tabela de frequência de cores
palette = quantize_colors(colors, 16)

# converte uma dada imagem para 16 cores sem alicar dithering
__ = reduce_colors(image, palette, dither=False)

# exibe a imagem convertida, use ".save()" para salvá-la em arquivo...
image.show()
