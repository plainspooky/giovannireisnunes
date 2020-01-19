#!/usr/bin/env python3
"""
Teste do Pillow.
"""
from PIL import Image

# dimensões da iimagem e nome do arquivo
WIDTH, HEIGHT = 1024, 512
FILENAME = ("teste_pillow.png", "PNG")

# cria instância do Pillow
pillow_obj = Image.new("RGB", (WIDTH, HEIGHT))
pixel_set = pillow_obj.load()

# laço só executa em 1/4 da imagem
for row in range(HEIGHT // 2):
    for col in range(WIDTH // 2):
        # define a cor no padrão RGB
        color = (row, abs(col - row), col)

        # calcula os pontos opostos...
        rev_col, rev_row = WIDTH - col - 1, HEIGHT - row - 1

        # plota os pontos
        pixel_set[col, row] = color
        pixel_set[rev_col, row] = color
        pixel_set[col, rev_row] = color
        pixel_set[rev_col, rev_row] = color

# salva o objeto como um arquivo PNG
pillow_obj.save(*FILENAME)
