#!/usr/bin/env python3
"""
Converte uma imagem PNG de 256x384 aplicando dithering e entrelaçando.
"""
from PIL import Image

from functions import add_noise, bsave, reduce_color, split_pages, to_msx2_rgb

HEIGHT = 384
WIDTH = 256

if __name__ == "__main__":

    # carrega a image em PNG
    image = Image.open("sample_256x384.png")
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
    image.save("interlaced.png")

    image_0, image_1 = split_pages(vram)

    bsave("interlac.s80", image_0)
    bsave("interlac.s81", image_1)
