"""
Mandelbrot
---
Este código foi convertido diretamente do MSX-BASIC (e esta de uma versão
em Applesoft BASIC), logo o nome das variáveis e até um pouco da lógica
estão um tanto quanto diferentes.
 
O programa original pode ser encontrado em:
https://www.retrocomputaria.com.br/2015/03/30/fractal-para-quem-precisa-de-fractal/
"""
from PIL import Image
from typing import Generator

WIDTH = 768
HEIGHT = 512

# paleta original do exemplo em MSX2
PALETTE = (
    (0, 0, 0,),
    (1, 0, 1,),
    (2, 0, 2,),
    (4, 0, 4,),
    (5, 0, 5,),
    (7, 0, 7,),
    (7, 0, 6,),
    (7, 0, 5,),
    (7, 0, 3,),
    (7, 0, 2,),
    (7, 0, 0,),
    (7, 1, 0,),
    (7, 2, 0,),
    (7, 4, 0,),
    (7, 5, 0,),
    (7, 7, 0,),
)


def convert_msx2_palette(palette) -> list:
    """
    Converte as cores da paleta de 9-bit do MSX2 em 24-bit.
    """
    new_palette = []
    for color in palette:
        new_palette.append(tuple(map(lambda i: (i + 1) * 32 - 1, color)))

    return new_palette


class Mandelbrot:
    """
    Calcula um conjunto de Mandelbrot
    """

    COLOR = 0xF  # 16 cores
    ASCII = 0x1F  # 32 caracteres

    # armazena a paleta de cores
    fake_palette = convert_msx2_palette(PALETTE)

    def __init__(self, iteractions: int, **kwargs) -> None:
        """
        Inicializa a classe
        """
        xc = kwargs.get("xc", -0.5)
        yc = kwargs.get("yc", 0.0)
        s = kwargs.get("s", 3.0)

        xr = s * 4 / 3
        yr = s

        self.x0 = xc - (xr / 2)
        self.x1 = xc + (xr / 2)
        self.y0 = yc - (yr / 2)
        self.y1 = yc - (yr / 2)

        self.xm = xr / WIDTH
        self.ym = yr / HEIGHT
        self.it = iteractions

    def __plot(self, x: int, y: int) -> int:
        """
        Método que efetivamente desenha o fractal
        """
        xx = x * self.xm + self.x0
        yy = y * self.ym + self.y0

        self.zx = self.zy = self.xx = self.yy = 0.0

        return self.__iteraction(xx, yy)

    def __iteraction(self, x: float, y: float) -> int:
        """
        Faz as iterações do Mandelbrot, recebe as coordenadas (x,y)
        do pixel como `x` e `y` e retorna a "cor" dele.
        """
        for i in range(self.it):
            self.zy = 2 * self.zx * self.zy + y
            self.zx = self.xx - self.yy + x
            self.xx = self.zx ** 2
            self.yy = self.zy ** 2

            color = self.it - i

            if self.xx + self.yy >= 4:
                break

        return color

    def to_png(self, width: int, height: int, filename: str) -> None:
        """
        Gera um fractal de Mandelbrot como uma imagem.
        """
        pillow_obj = Image.new("RGB", (width, height))
        pixel_set = pillow_obj.load()

        for y in range(height):
            for x in range(width):

                color = self.__plot(x, y) & self.COLOR
                pixel_set[x, y] = self.fake_palette[color]

        pillow_obj.save(filename, "PNG")

    def to_ascii(self, width: int, height: int) -> str:
        """
        Gera um fractal de Mandelbrot utilziando caracteres ASCII.
        """
        output = ""

        for y in range(height):
            for x in range(width):
                # Usa somente os primeiros 32 primeiros caracteres
                color = self.__plot(x, y) & self.ASCII
                output += chr(31 + color)

            output += "\n"

        return output


if __name__ == "__main__":
    # não faz muita coisa, instancia a classe e gera o arquivo
    mandel = Mandelbrot(50)
    mandel.to_png(WIDTH, HEIGHT, "pillow_fractal.png")
