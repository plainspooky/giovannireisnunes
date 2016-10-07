# -*- mode: ruby -*-
# vi: set ft=ruby :

require './Nome.rb'

class Supernome < Nome

    # método que escreve o nome completo de outra forma
    def escreve_nome_completo
        @sobrenome.upcase+", "+@nome
    end

end
