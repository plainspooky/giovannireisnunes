# -*- mode: ruby -*-
# vi: set ft=ruby :

class Nome
    attr_accessor :nome, :sobrenome

    # construtor da classe
    def initialize(nome,sobrenome)
        @nome=nome
        @sobrenome=sobrenome
    end

    # método padrão para "escrever" o conteúdo
    def to_s
        @nome
    end

    # método que escreve o nome completo
    def escreve_nome_completo
        @nome+" "+@sobrenome
    end

end
