#!/usr/bin/perl
#
#  MyMAC.pl
#  My implementantion in PERL od Felix Angel's simple virtual
#  machine -- https://github.com/felixangell/mac
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
use strict;

use constant PSH => 0;
use constant ADD => 1;
use constant POP => 2;
use constant HLT => 3;

use constant True => 1;
use constant False => 0;

my $ip=0;
my $sp=-1;
my $running=True;

my @stack=(undef);

my @program=(	PSH, 5,
		PSH, 6,
		ADD,
		POP,
		HLT  );

sub fetch()
{
	return $program[$ip];
}

sub eval()
{
	my $instr=$_[0];
	
	if ( $instr == HLT )
	{
		$running=False;
		print "done\n";
	}
	elsif ( $instr == PSH )
	{
		$sp++;
		$stack[$sp]=$program[++$ip];
		print "push\n";
	}
	elsif ( $instr == POP )
	{
		my $val_popped = $stack[$sp--];
		print "popped $val_popped\n";
	}
	elsif ( $instr == ADD )
	{
		my $a = $stack[$sp--];
		my $b = $stack[$sp--];
		
		my $result=$b+$a;
		
		$sp++;
		$stack[$sp]=$result;
		print "add\n";
	}
}

while( $running == True)
{
	&eval( &fetch() );
	$ip++;
}

exit 0
