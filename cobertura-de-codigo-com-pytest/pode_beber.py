#!/usr/bin/env python


IDADE_LEGAL = 18
SUGESTAO = 'copo d\'água'


def verifica_bebida(idade, bebida, alcool, sugestao=SUGESTAO):
    """ Verifica se a pessoa pode beber álcool de acordo com a idade. Recebe
    a idade em `idade` como inteiro, nome da bebibda em `bebida` como string,
    se esta possui álcool em `alcool` como booleano e sugestão em 'sugestao'
    como string (opcional). Retorna `True` e `bebida` se a idade for maior ou
    igual a permitida ou `False` e sugestão em caso contrário. """
    if idade < IDADE_LEGAL and alcool:
        return False, sugestao
    else:
        return True, bebida


class TestClass(object):
    """ Classe de testes para a função Verifica_bebida(). """

    def test_maior_pede_cerveja(self):
        """ Testa se um maior de idade pode pedir uma cerveja. """
        assert verifica_bebida(30, 'cerveja', True) == (True, 'cerveja')

    def test_menor_pede_cerveja(self):
        """ Testa se um menor de idade pode pedir uma cerveja. """
        assert verifica_bebida(15, 'cerveja', True) == (False, SUGESTAO)

    def test_maior_pede_suco(self):
        """ Testa se um maior de idade pode pedir um suco. """
        assert verifica_bebida(30, 'suco', False) == (True, 'suco')

    def test_menor_pede_suco(self):
        """ Testa se um menor de idade pode pedir um suco. """
        assert verifica_bebida(15, 'suco', False) == (True, 'suco')
