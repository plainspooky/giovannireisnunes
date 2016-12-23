/*
    Versão não utilizando a especificação da ECMA-262
*/

// permite a execução do código em Node.js
"use strict";

// a classe 'Nome'
class Nome {
    // construtor da classe
    constructor(nome,sobrenome){
        this.nome = nome;
        this.sobrenome = sobrenome
    }
    // define o 'getter' que retorna apenas o nome
    escreveNome(){
        return this.nome;
    }
    // define o 'getter' que retorna o nome completo
    escreveNomeCompleto(){
        return this.nome + " " + this.sobrenome;
    }
    // define o 'setter' para armazenae o nome
    armazenaNome(nome){
        this.nome = nome;
    }
}

// a classe 'Supernome'
class Supernome extends Nome {
    escreveNomeCompleto(){
        return this.sobrenome.toUpperCase() + ", "+ this.nome;
    }
}

// cria uma instância de 'Nome'
var giovanni = new Nome("Giovanni","Nunes");
console.log("O primeiro nome é "+giovanni.escreveNome()+".");
console.log("E "+giovanni.escreveNomeCompleto()+" o nome completo.");

// cria uma instância de 'Supernome'
var giovanni2 = new Supernome("Giovanni","Nunes");
console.log("E "+giovanni2.escreveNomeCompleto()+" o nome completo.");

// e termina o programa
return true;
