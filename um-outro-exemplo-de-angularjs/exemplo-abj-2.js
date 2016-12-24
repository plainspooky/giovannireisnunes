  /*
 *	Exemplo AngularJS 2 1.0
 *
 *	Outro exemplo de página web só com AngularJS
 *
 *	Copyright 2015, Giovanni Nunes <giovanni.nunes-you.know-gmail.com>
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
(function(){

	var app=angular.module('exemplo2', [])
	.controller("BoletimCtrl", [ '$http',function($http) {

		this.bimestres=[1,2,3,4];
		this.agora=Date.now();

		var exemplo2=this;
		exemplo2.turma=[];

		/*
		 *	carrega a base de dados via HTTP
		 */
		this.file=$http.get('exemplo-abj-2.json').then(function(result) {
			exemplo2.turma=result.data;
		});

		 /*
		  *	calculo a média aritmética de um array de números
		  */
		this.mediaAritmetica=function(lista) {
			var itens=lista.length;
			var soma=0;
			for ( i=0; i<itens; i++ ){
				soma += lista[i];
			}
			return soma/itens;
		};
	}]);
})();
