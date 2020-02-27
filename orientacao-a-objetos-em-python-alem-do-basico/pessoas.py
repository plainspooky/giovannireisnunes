"""
Pessoas
"""
from dataclasses import dataclass


class Pessoa:
    """
    Classe que implementa `__repr__` e `__str__`.
    """

    ativo = False

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def __repr__(self) -> str:
        return f"nome={self.nome}, idade={self.idade}, ativo={self.ativo}"

    def __str__(self) -> str:
        idade = "anos" if self.idade > 1 else "ano"
        ativo = "ativo" if self.ativo else "inativo"
        return f"{self.nome}, {self.idade} {idade} ({ativo})"


class PessoaV2:
    """
    Classe que inicializa `ativo` no método `__init__` replicando código.
    """

    def __init__(self, nome: str, idade: int, ativo: bool = False) -> None:
        self.nome = nome
        self.idade = idade
        self.ativo = ativo


class PessoaV3(Pessoa):
    """
    Clase que inicializa `ativo` sen replicar código.
    """

    def __init__(self, nome: str, idade: int, ativo: bool = False) -> None:
        self.ativo = ativo
        Pessoa.__init__(self, nome, idade)


@dataclass
class PessoaDataClass:
    """
    Inicializa os atributos da classe de forma automática. 
    """

    pessoa: str
    idade: int
    ativo: bool = False
