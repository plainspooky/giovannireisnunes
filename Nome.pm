#
#  Nome.pm
#
#  Copyright 2015, Giovanni Nunes <giovanni.nunes@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
package Nome;
use strict;

sub new
{
	my ( $class ) = shift;
	my $self = { _nome => shift, _sobrenome => shift };
	bless $self, $class;
	return $self;
}

sub alteraNome
{
	my ( $self, $nome ) = @_;
	$self->{ _nome }=$nome;
	return $self;
}

sub escreveNomeCompleto
{
	my ( $self ) = @_;
	return ( uc $self->{_sobrenome} ).", ".$self->{_nome};
}

sub escreveNome
{
	my ( $self ) = @_;
	return $self->{ _nome }
}

sub DESTROY
{
	
}

our $AUTOLOAD;
sub AUTOLOAD
{
    die "Ei, o método $AUTOLOAD não existe!\n";
}
1;
