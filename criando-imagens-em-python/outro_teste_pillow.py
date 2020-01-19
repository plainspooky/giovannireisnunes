#!/usr/bin/env python3
"""
Teste do Pillow.
"""
from PIL import Image

FILENAME = ("outro_teste_pillow.png", "PNG")

# carrega o arquivo do primeiro exemplo
pillow_obj = Image.open("teste_pillow.png")
pixel_set = pillow_obj.load()

# recupera as dimensões da imagem
width = pillow_obj.width
height = pillow_obj.height

# laço só executa em 1/4 da imagem
for row in range(height // 2):
    for col in range(width // 2):

        # recupera as cores atuai
        r, g, b = pixel_set[col, row]

        r //= 2

        # plota os pontos
        pixel_set[col, row] = (b, g, r)
        pixel_set[width - col - 1, height - row - 1] = (b, g, r)

# salva o objeto como um arquivo PNG
pillow_obj.save(*FILENAME)
