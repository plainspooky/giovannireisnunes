#!/usr/bin/env python3
""" Gera listas com sequências de letras do alfabeto, contém uma função
convencional, `alfabeto_fn`, e um gerador, `alfabeto_gen`. """


PRIMEIRO, ULTIMO = "A", "Z"


def alfabeto_fn(primeiro=PRIMEIRO, ultimo=ULTIMO, passo=1):
    """ Recebe o primeiro caractere em `primeiro` (ou "A"), último caractere
    da sequência em `ultimo` (ou "Z") e icremento da sequência em `passo` (ou
    1). Retorna uma lista com a sequência de caracteres do primeiro ao último
    caractere aplicando o incremento definido. Invocará exceções de
    ValueError() nos casos do incremento ter valor 0 e os caracteres
    informados não estiverem em ordem crescente ou descrescente, de acordo com
    o incremento utilizado. """

    primeiro = primeiro.upper()
    ultimo = ultimo.upper()

    alfabeto_list = []

    caractere = ord(primeiro if primeiro > PRIMEIRO else PRIMEIRO)
    ultimo_caractere = ord(ultimo if ultimo < ULTIMO else ULTIMO)

    if passo == 0:
        raise ValueError("O valor de passo deve ser diferente de zero.")

    elif caractere > ultimo_caractere:
        if passo > 0:
            raise ValueError(
                "O último caractere deve ser maior que o primeiro quando o passo for positivo."
            )
        else:
            while caractere >= ultimo_caractere:
                alfabeto_list.append(chr(caractere))
                caractere += passo

    elif caractere < ultimo_caractere:
        if passo < 0:
            raise ValueError(
                "O último caractere deve ser menor que o primeiro quando o passo for negativo."
            )
        else:
            while caractere <= ultimo_caractere:
                alfabeto_list.append(chr(caractere))
                caractere += passo

    return alfabeto_list


def alfabeto_gen(primeiro=PRIMEIRO, ultimo=ULTIMO, passo=1):
    """ (Gerador) Recebe o primeiro caractere em `primeiro` (ou "A"), último
    caractere da sequência em `ultimo` (ou "Z") e icremento da sequência em
    `passo` (ou 1). Retorna uma lista com a sequência de caracteres do
    primeiro ao último caractere aplicando o incremento definido. Invocará
    exceções de ValueError() nos casos do incremento ter valor 0 e os
    caracteres informados não estiverem em ordem crescente ou descrescente,
    de acordo com o incremento utilizado. """

    primeiro = primeiro.upper()
    ultimo = ultimo.upper()

    caractere = ord(primeiro if primeiro > PRIMEIRO else PRIMEIRO)
    ultimo_caractere = ord(ultimo if ultimo < ULTIMO else ULTIMO)

    if passo == 0:
        raise ValueError("O valor de passo deve ser diferente de zero.")

    elif caractere > ultimo_caractere:
        if passo > 0:
            raise ValueError(
                "O último caractere deve ser maior que o primeiro quando o passo for positivo."
            )
        else:
            while caractere >= ultimo_caractere:
                yield chr(caractere)
                caractere += passo

    elif caractere < ultimo_caractere:
        if passo < 0:
            raise ValueError(
                "O último caractere deve ser menor que o primeiro quando o passo for negativo."
            )
        else:
            while caractere <= ultimo_caractere:
                yield chr(caractere)
                caractere += passo
