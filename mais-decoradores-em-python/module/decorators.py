"""
Decoradores usados como exemplo.
"""
from typing import Callable


def marker(func_obj) -> Callable:
    """
    (decorador) Realça uma _string_ usando outras cores.
    """

    def decorator(*args: str, **kvargs: int) -> str:
        """
        Adiciona os códigos VT-100 necessários para mudar a cor de uma
        string na tela.
        """
        fore, back = (0, 15, 0,), (0, 255, 63,)

        return (
            "\x1b[38;2;{};{};{}m".format(*fore)
            + "\x1b[48;2;{};{};{}m".format(*back)
            + func_obj(*args, **kvargs)
            + "\x1b[0m"
        )

    return decorator


def marker2(fore: tuple, back: tuple) -> Callable:
    """
    (decorador) Realça uma _string_ usando cores de frente como `fore`
    e de fundo como `back`.
    """

    def wrapper(func_obj) -> Callable:
        """
        Envelopa a função a ser chamada.
        """

        def decorator(*args: str, **kvargs: int) -> str:
            """
            Adiciona os códigos VT-100 necessários para mudar a cor de uma
            string na tela.            
            """
            return (
                "\x1b[38;2;{};{};{}m".format(*fore)
                + "\x1b[48;2;{};{};{}m".format(*back)
                + func_obj(*args, **kvargs)
                + "\x1b[0m"
            )

        return decorator

    if len(fore) != 3 or len(back) != 3:
        raise ValueError("Cores precisam ser tuplas com valores de (R, G, B)!")

    return wrapper


def multiply(factor: float) -> Callable:
    """
    Multiplica qualquer valor recebido pelo valor de `factor`.
    """

    def wrapper(func_obj) -> Callable:
        """
        Envelopa o decorador...
        """

        def decorator(*args: str, **kvargs: int) -> float:
            """
            Executa a função decorada pelo valor informado.
            """
            return func_obj(*args, **kvargs) * factor

        return decorator

    return wrapper
