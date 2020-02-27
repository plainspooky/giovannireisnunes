"""
Computadores
"""
# sistemas operacionais disponíveis
SISTEMAS = (
    "Linux",
    "macOS",
    "Windows",
    "outros",
)


class Computador:
    """
    Classe de testes implementando `__slots__`
    """

    __slots__ = (
        "hostname",
        "sistema",
        "endereco",
    )

    def __init__(self, hostname: str, so: int, ip: str) -> None:
        self.hostname = hostname
        self.sistema = SISTEMAS[so]
        self.endereco = ip or "127.0.0.1"

    def __str__(self) -> str:
        return "{host} ({os}) - {ip}".format(
            host=self.hostname, os=self.sistema, ip=self.endereco
        )


class Notebook(Computador):
    """
    Classe que herda os atributos de uma classe com `__slots__`.
    """

    __slots__ = "vpn"

    def __init__(self, hostname: str, so: int, ip: str, vpn: bool) -> None:
        self.vpn = vpn
        Computador.__init__(self, hostname, so, ip)
