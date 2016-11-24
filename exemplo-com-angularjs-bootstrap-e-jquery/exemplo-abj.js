(function(){
/*	
 *	Exemplo ABj 1.0
 * 	
 *	Exemplo de página web com AngularJS, Bootstrap e jQuery
 * 	
 *	Copyright 2015, Giovanni Nunes <giovanni.nunes--you know--gmail.com>
 * 	
 *	This program is free software; you can redistribute it and/or modify
 *	it under the terms of the GNU General Public License as published by
 *	the Free Software Foundation; either version 2 of the License, or
 *	(at your option) any later version.
 * 	
 *	This program is distributed in the hope that it will be useful,
 *	but WITHOUT ANY WARRANTY; without even the implied warranty of
 *	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *	GNU General Public License for more details.
 *	
 *	You should have received a copy of the GNU General Public License
 *	along with this program; if not, write to the Free Software
 *	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 *	MA 02110-1301, USA.
 * 	
 */
 
	/*
	 *	minha aplicação (portifolio) é definida aqui e os demais controles vão
	 *	concatenados na variável 'app'.
	 */
	var app=angular.module('exemplo',[])
	.controller("TituloController",function() {		
		this.texto=titulo;
	})
	/*
	 *	cuida de preencher o título em <title>...</title>
	 */
	.controller('MenuController',function() {
		this.pagina=0;
		this.texto=titulo;
		/*
		 *	altera o valor da variável 'pagina' (a aba ativa).
		 */
		this.escolhePagina = function(pag) {
			this.pagina=pag;
		};
		/*
		 *	retorna 'true' ou 'false' se o valor informado é o da aba ativa.
		 */
		this.verificaPagina = function(pag) {
			return this.pagina === pag;
		};
	})
	/*
	 *	preenche do conteúdo dentro do jumbotron da página	 
	 */
	.controller('JumboController',function() {
		this.conteudo=website["jumbo"];
	})
	/*
	 *	 responsável pelos três botões explicativos
	 */	
	.controller('ResumoController',function() {
		this.conteudos=website["conteudo"];
	})
	/*
	 *	preeenche o conteúdo do sobre 
	 */
	.controller('SobreController',function() {
		this.conteudo=website["sobre"];
		this.license=gpl;
	});

	/*
	 *	esta variável guarda o título to projeto
	 */
	var titulo="Um exemplo bem simples com AngularJS, Bootstrap e jQuery";
	
	/*
	 *	no mundo real este conteúdo poderia ser carregado diretamente de
	 *	um arquivo 'json' via http -- via Service -- mas aqui vai como um
	 *	hash em JavaScript mesmo.
	 */
	var website={
		'jumbo':{
			'texto':'Funciona!',
			'descr':'Veja o código fonte e compare com o que está na tela',
			'botao':'Baixe os arquivos aqui!',
			'link':'https://github.com/plainspooky/giovannireisnunes/blob/master/README.md'
			},
		'conteudo': [ {
			'titulo':'AngularJS',
			'texto': 'AngularJS é um framework open-source para a desenvolvimento de aplicações web.'+
					' Foi criado pelo Google e hoje é mantido por este e uma comunidade de desenvolvedores independentes.',
			'tela': 'https://giovannireisnunes.files.wordpress.com/2015/07/angular.jpeg',
			'link': 'http://www.angularjs.org'
			}, {
			'titulo':'Bootstrap',
			'texto': 'Bootstrap é um framework open-source para HTML, CSS e JavaScript desenvolvido'+
					' pelo Twitter para a criação rápida e do zero de sítios web responsivos ou móveis.',
			'tela': 'https://giovannireisnunes.files.wordpress.com/2015/07/bootstrap.jpeg',
			'link': 'http://getbootstrap.com/'
			}, {
			'titulo':'jQuery',
			'texto': 'jQuery é uma biblioteca em JavaScript para a manipulação dos elementos HTML.'+
					' Acrescenta recursos como animação, tratamento de eventos e AJAX em uma API simplificada.',
			'tela': 'https://giovannireisnunes.files.wordpress.com/2015/07/jquery.jpeg',
			'link': 'http://jquery.com/'
			}
		],
		'sobre': {
			'titulo':'Sobre',
			'texto':'Este é um pequeno exemplo do que se pode fazer juntando estas três ferramentas'+
					' (Angular.JS, Bootstrap e jQuery) na forma de um exercício de programação para'+
					' praticar o que aprendi nos cursos de AngularJS do Codecademy e do Codeschool'+
					' (sim eu fiz ambos).'
			}
		};
		/*
		 *	As cadeias de caracteres estão concatenadas e não apenas unidas com "\" para não
		 *	colocar conteúdo extra no texto (e obviamente deixá-las um pouco mais legíveis), justamente
		 *	o inverso do que fiz na variável abaixo:
		 */		 
	var gpl="Exemplo-ABj 1.0\n\
\n\
Exemplo de página web com AngularJS, Bootstrap e jQueryz\n\
\n\
This program is free software; you can redistribute it and/or modify\n\
it under the terms of the GNU General Public License as published by\n\
the Free Software Foundation; either version 2 of the License, or\n\
(at your option) any later version.\n\
\n\
This program is distributed in the hope that it will be useful,\n\
but WITHOUT ANY WARRANTY; without even the implied warranty of\n\
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n\
GNU General Public License for more details.\n\
\n\
You should have received a copy of the GNU General Public License\n\
along with this program; if not, write to the Free Software\n\
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,\n\
MA 02110-1301, USA."

})();
