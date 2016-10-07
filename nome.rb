#!/usr/bin/env ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# as duas classes serão carregadas
require './Supernome.rb'

# define o novo objeto
giovanni=Nome.new('Giovanni','Nunes')
# giovanni=Supernome.new('Giovanni','Nunes')

# usará automaticamente o .to_s
puts "O primeiro nome é %s." % giovanni

# usará explicitamente um dos métodos
puts "E %s o nome completo do sujeito." % giovanni.escreve_nome_completo

# o que tem dentro da classe?
puts giovanni

exit
