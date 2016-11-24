#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Nome(object):

    def __init__(self,nome,sobrenome):
        ''' método construtor da classe '''
        self.nome = nome
        self.sobrenome = sobrenome
    def __str__(self):
        ''' método para 'escrever' o conteúdo '''
        return self.nome

    def escreve_nome_completo(self):
        ''' método que escreve o nome completo '''
        return self.nome+" "+self.sobrenome
   
class Supernome(Nome):

    def escreve_nome_completo(self):
        ''' método que escreve o nome completo de outra forma '''
        return self.sobrenome.upper()+", "+self.nome

