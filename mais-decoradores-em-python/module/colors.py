"""
Classe para gerenciar paletas de cores
"""
from typing import List, Tuple

ColorType = Tuple[int, ...]
ColorTupleType = Tuple[ColorType, ...]
PaletteType = List[str]


class BaseColors:
    """
    Classe base para criação de paletas de cores
    """

    def create_palette(self, name: str, values: PaletteType) -> None:
        """
        Define atributos na classe para a criação da paleta de cores.
        """

        def hex_to_tuple(hex_color: str) -> ColorType:
            """
            Converte um  número hexadecimal em _string_ (0xRRGGBB) em uma
            tupla com números inteiros (R, G, B).
            """
            color = hex_color.rjust(6, "0")

            return tuple(int(color[i : i + 2], 16) for i in range(0, 6, 2))

        color_tuple: ColorTupleType = tuple(
            [hex_to_tuple(color) for color in values]
        )

        setattr(self, name, color_tuple)


class TangoColors(BaseColors):
    """
    Define uma paleta de cores baseado nas cores do projeto Tango Desktop
    """

    PALETTE = {
        "butter": ["fce94f", "edd400", "c4a000",],
        "orange": ["fcaf3e", "f57900", "ce5c00",],
        "chocolate": ["e9b96e", "c17d11", "8f5902",],
        "chameleon": ["8ae234", "73d216", "4e9a06",],
        "sky": ["729fcf", "3465a4", "204a87",],
        "plum": ["ad7fa8", "75507b", "5c3566",],
        "scarlet": ["ef2929", "cc0000", "a40000"],
        "aluminium": [
            "ffffff",
            "eeeeec",
            "d3d7cf",
            "babdb6",
            "888a85",
            "555753",
            "2e3436",
            "000000",
        ],
    }

    def __init__(self) -> None:
        """
        Inicializa a classe carregando a paleta definida em PALETTE
        """
        for color, values in self.PALETTE.items():
            self.create_palette(color, values)
