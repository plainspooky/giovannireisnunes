#!/usr/bin/perl
use strict;
use Nome;

print "Digite seu primeiro nome : ";
my $n = <STDIN>;
chomp $n;

print "Digite agora seu sobrenome : ";
my $s = <STDIN>;
chomp $s;

my $a=Nome->new($n,$s);

print "\nOlá ".$a->escreveNomeCompleto()."!\n";

print "Ou devo usar apenas de ".$a->escreveNome()."?\n\n";

$a=Nome->DESTROY;

exit 0;
