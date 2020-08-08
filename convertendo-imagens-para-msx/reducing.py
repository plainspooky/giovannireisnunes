#!/usr/bin/env python3
"""
Converte uma imagem PNG de 256x192 reduzindo as cores.
"""
from PIL import Image

from functions import bsave, reduce_color, to_msx2_rgb

HEIGHT = 192
WIDTH = 256

if __name__ == "__main__":

    # carrega a image em PNG
    image = Image.open("sample_256x192.png")
    bitmap = image.load()

    # inicializa a "VRAM"
    vram = bytearray()

    for y in range(HEIGHT):
        for x in range(WIDTH):

            # extrai os componentes RGB e reduz os elementos de cpr
            old_pixel = bitmap[x, y]
            new_pixel = reduce_color(*old_pixel)

            # reflete a reduçãao de cores na imagem original
            bitmap[x, y] = new_pixel

            # adiciona o pixel ao 'array'
            vram.append(to_msx2_rgb(*new_pixel))

    # salva a imagem
    image.save("reduced.png")
    bsave("reduced.sc8", vram)
