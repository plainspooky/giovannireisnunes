<?php
/*
    SuperNome.php (classe)

    Copyright 2015, Giovanni Nunes <giovanni.nunes@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
   MA 02110-1301, USA.
*/

include('Nome.php');

class SuperNome extends Nome
{
    public $titulo;

    public function __construct($nome,$sobrenome,$titulo)
    {
      $this->nome = $nome;
      $this->sobrenome = $sobrenome;
      $this->titulo = $titulo;
    }

    public function escreveSuperNome()
    {
      return $this->titulo." ".$this->nome." ".$this->sobrenome;
    }
};
?>
