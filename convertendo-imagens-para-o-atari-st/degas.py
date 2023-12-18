from divisiblelist import DivisibleList
from PIL import Image


def load_pic(filename):
    raw = open(filename, "rb").read()
    width, height, bpp = get_resolution(raw[0:2])
    palette = get_palette(raw[2:34])
    chunks = get_chunks(raw[34::])

    image = Image.new("RGB", (width, height))
    bitmap = image.load()

    words = DivisibleList(chunks) / {bpp}

    for y in range(height):
        for x in range(0, width, 16):
            pixels = dechunky(next(words))
            for index, pixel in enumerate(pixels):
                bitmap[x + index, y] = palette[pixel]

    return image


def get_resolution(res):
    return {
        0: (320, 200, 4),
        1: (640, 200, 2),
        2: (640, 400, 1),
    }[int.from_bytes(res, byteorder="big")]


def get_palette(pal):
    return [
        (
            (color[0] & 0x0F) << 5,
            (color[1] & 0xF0) << 1,
            (color[1] & 0x0F) << 5,
        )
        for color in DivisibleList(pal) / 16
    ]


def get_chunks(data):
    return [
        int.from_bytes(word, byteorder="big")
        for word in DivisibleList(data) / {2}
    ]


POWS_OF_TWO = (
    (0, 32768),
    (1, 16384),
    (2, 8192),
    (3, 4096),
    (4, 2048),
    (5, 1024),
    (6, 512),
    (7, 256),
    (8, 128),
    (9, 64),
    (10, 32),
    (11, 16),
    (12, 8),
    (13, 4),
    (14, 2),
    (15, 1),
)


def dechunky(words):
    pixels = [0 for __ in range(16)]
    for col, bit in POWS_OF_TWO:
        for word in words[::-1]:
            pixels[col] <<= 1
            pixels[col] |= 1 if word & bit else 0

    return pixels
