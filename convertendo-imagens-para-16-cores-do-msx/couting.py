#!/usr/bin/env python3
from PIL import Image

from functions import count_colors

image = Image.open("sample_256x192.png")

# cria a tabela de frequência de cores
counter = count_colors(image)

# cria uma lista contendo cor e sua frequência
colors = sorted(
    [("#{:02x}{:02x}{:02x}".format(*c), q) for c, q in counter],
    key=lambda i: i[1],
    reverse=True,
)

# imprime o resultado na tela...
print("\n".join("{} {:5d}".format(*c) for c in colors))
print("total de cores = {}".format(len(colors)))
