"""
Veículos
"""


class Veiculo:
    """
    Classe de testes implementando accessors (getters e setters)
    """

    def __init__(self, modelo: str, cor: str) -> None:
        self.__modelo = modelo
        self.__cor = cor

    def __str__(self) -> str:
        return f"{self.modelo} {self.cor}"

    @property
    def modelo(self) -> str:
        return self.__modelo

    @property
    def cor(self) -> str:
        return self.__cor

    @cor.setter
    def cor(self, cor) -> None:
        self.__cor = cor
