#!/usr/bin/env python3
"""
Converte uma imagem PNG de 256x192 aplicando dithering.
"""
from PIL import Image

from functions import add_noise, bsave, reduce_color, to_msx2_rgb

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

            # calcula a quantificação e apĺica nos vizinhos.
            error = [old - new for old, new in zip(old_pixel, new_pixel)]
            add_noise(bitmap, x, y, error)

    # salva a imagem
    image.save("dithered.png")
    bsave("dithered.sc8", vram)
