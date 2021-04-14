"""Funções de uso geral."""
from math import sqrt

BPP_MASK = 0xE0

FLOYD_STEINBERG_NEIGHBORS = (
    (+1, 0, 7),
    (-1, +1, 3),
    (-1, +1, 5),
    (+1, +1, 1),
)

# estes lambdas estão aqui não precisar replicá-los no código
color_key = lambda color: color[0]
color_value = lambda color: color[1]


def add_noise(bitmap, x, y, error):
    """
    Adiciona ruído nos pixeis vizinhos aplicando a diferença nos
    valores RGB da cor original e seu valor após a redução.
    """
    for offset_x, offset_y, debt in FLOYD_STEINBERG_NEIGHBORS:
        try:
            # calcula o endereço do pixel a ser alterado
            off_x, off_y = x + offset_x, y + offset_y
            # adiciona o ruído definido pelo Floyd-Steinberg ao pixel
            bitmap[off_x, off_y] = tuple(
                (
                    color + error * debt // 16
                    for color, error in zip(bitmap[off_x, off_y], error)
                )
            )
        except IndexError:
            # trata o caso de um vizinho fora da área da imagem
            ...


def count_colors(image):
    """Calcula a frequência de cada pixel da imagem em uma paleta RGG de
    9-bit."""

    bitmap = image.load()
    colors = {}

    for y in range(image.height):
        for x in range(image.width):
            # extrai os componentes RGB e reduz os elementos de cor
            # (ignora o canal alfa caso ele exista)
            r, g, b, *__ = bitmap[x, y]

            # corta a parte não necessária (mais prático que ÷ e depois ×)
            r &= BPP_MASK
            g &= BPP_MASK
            b &= BPP_MASK

            # monta a frequência de cores da imagem
            colors[(r, g, b)] = colors.get((r, g, b), 1) + 1

    # organiza o dicionário para uma lista de tuplas
    return [(k, v) for k, v in colors.items()]


def distance(origin, destination):
    """Calcula a distância entre dois pontos num espaço euclidiano de três
    dimensões."""

    # ignora os canais alfa caso existam
    r1, g1, b1, *__ = origin
    r2, g2, b2, *__ = destination

    return sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)


def quantize_colors(palette, length):
    """Reduz o número de cores de uma imagem até o valor desejado."""

    # enquanto a paleta for maior que o valor desejado, faça...
    while len(palette) > length:
        # ordena a paleta em ordem crescente de frequência
        palette.sort(key=color_value)

        # recupera a 1ª cor e calcula a distância delas para as demais
        color, freq = palette.pop(0)

        # monta a lista de distância da cor lida para com as demais
        distances = [
            (idx, distance(color, clr[0]))
            for idx, clr in enumerate(palette[1:], start=1)
        ]

        # a nova cor é a de menor ocorrência, recupera seu índice
        index, __ = min(distances, key=color_value)

        # adiciona as ocorrências da cor antiga à nova e a remove da lista
        palette[index] = (
            palette[index][0],
            palette[index][1] + freq,
        )

    # retorna apenas as cores da paleta
    return [i[0] for i in sorted(palette, key=color_key)]


def reduce_colors(image, palette, dither=True):

    bitmap = image.load()
    # cache para as cores já calculadas
    colors = {}

    for y in range(image.height):
        for x in range(image.width):
            # recupera o valor do pixel
            pixel = bitmap[x, y]
            # verifica se a cor existe no cache
            index = colors.get(pixel)

            if index is None:
                # a cor não está no cache...
                index = min(
                    [
                        (idx, distance(pixel, clr))
                        for idx, clr in enumerate(palette)
                    ],
                    key=color_value,
                )[0]
                # salva a cor no cache
                colors[pixel] = index

            # atualiza o pixel com a nova cor
            bitmap[x, y] = palette[index]

            if dither:
                # adiciona ruído nos pixeis vizinhos
                error = [old - new for old, new in zip(pixel, palette[index])]
                add_noise(bitmap, x, y, error)
