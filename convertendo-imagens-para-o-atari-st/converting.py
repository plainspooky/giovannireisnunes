#!/usr/bin/env python3
from PIL import Image

from functions import (
    bsave,
    convert_palette,
    convert_to_vram,
    count_colors,
    quantize_colors,
    reduce_colors,
    split_pages,
)

MAX_LINES = 256

VALID_SIZES = ((256, 192), (256, 384), (512, 192), (512, 384))

image = Image.open("sample_512x384.png")

try:
    # força o programa a aceitar imagens em 256×192 ou 512×384
    assert (image.width, image.height) in VALID_SIZES

    mode = "7" if image.width == 512 else "5"

    # recupera a lista de cores
    colors = count_colors(image)

    # converte a imagem para 16 cores sem aplicar dithering
    palette = quantize_colors(colors, 16)
    screen = reduce_colors(image, palette, dither=True)

    # divide a imagem em páginas de vídeo, caso necessário
    pages = (
        split_pages(screen)
        if image.height > MAX_LINES
        else (screen, None)
    )

    # converte para o leiaute da VRAM e salva a imagem
    for number, data in enumerate(pages):
        if data:
            bsave(f"SAMPLE.P{mode}{number}", convert_to_vram(data))

    # salva a paleta de cores
    bsave(f"SAMPLE.P{mode}L", convert_palette(palette))

    # exibe a imagem convertida, use ".save()" para salvar em arquivo...
    image.show()
    image.save("sample_512x424_default_palette.png")

except AssertionError:
    print(
        "Resolução inválida, use imagens com ",
        ", ".join([f"{w}×{h}" for w, h in VALID_SIZES]),
    )
