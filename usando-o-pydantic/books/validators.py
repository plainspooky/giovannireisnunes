"""Rotinas para validação do ISBN."""


def __calculate_isbn10_digit(isbn10: str) -> str:
    """Calcula o dígito de verificação para ISBN-10."""

    # a variável com o dígito de verificação
    digit = 0

    for i, j in zip((int(i) for i in isbn10), range(10, 1, -1)):
        # faz o primeiro dígito do ISBN×10, o segundo×9 etc
        digit += i * j

    # usa apenas o módulo 11 da soma
    digit %= 11

    # subtrai por 11, faz o módulo 11 e retorna o dígito como string...
    return str((11 - digit) % 11)


def __calculate_isbn13_digit(isbn13: str) -> str:
    """Calcula o dígito de verificação para ISBN-13."""

    # dígito de verificação a ser calculado
    digit = 0

    for i, j in enumerate((int(i) for i in isbn13), start=1):
        # se a posição do dígito é par, soma dígito×3 senão apenas dígito
        digit += j if i % 2 else j * 3

    # módulo 10 subtraído por 10
    digit = 10 - (digit % 10)

    # converte o dígito para string (quando for 10 retornará '0')
    return str(digit)[-1]


def __calculate_isbn_digit(isbn: str) -> str:
    """Calcula o dígito de verificação para o ISBN."""
    # se o ISBN informado não contiver números nem perco meu tempo

    if isbn.isdigit():
        if len(isbn) == 9:
            # é ISBN-10
            return __calculate_isbn10_digit(isbn)
        elif len(isbn) == 12:
            # é ISBN-13
            return __calculate_isbn13_digit(isbn)

    raise ValueError("ISBN doesn't match as ISBN-10 or ISBN-13.")


def validate_isbn_digit(isbn: str) -> bool:
    """Valida o dígito de verificação de um dado ISBN."""

    digit = __calculate_isbn_digit(isbn[:-1])

    return True if digit == isbn[-1] else False
