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
