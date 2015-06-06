#!/usr/bin/perl -CS
#
#  IPSmaker v0.1
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
use warnings;
use IPSmaker;

unless ( scalar @ARGV==0 )
{
	if ( -f $ARGV[0] )
	{
		my $Original = IPSmaker->new( $ARGV[0] );
		
		if ( -f $ARGV[1] )
		{
			my $Modified = IPSmaker->new( $ARGV[1] );
			
			if ( $Original->{FileSize} == $Modified->{FileSize} )
			{
				my $Position=0;
				my $Mode=0;
				my $Start=0;
				my $Stop=0;
				
				my $IPSpatch = $ARGV[2];
				
				open(my $FH, '>', $IPSpatch) or
				die "*** Could not create file '$IPSpatch' $!";
				
				binmode $FH,":raw";
				
				print $FH IPSmaker->Header();
				
				do
				{
					if ( $Original->Byte($Position) != $Modified->Byte($Position) )
					{
						if ( $Mode==0 )
						{
							$Start=$Position;
						}
						$Mode=1;
					}
					else
					{
						if ( $Mode==1 )
						{
							$Stop=$Position;
							print $FH $Modified->Record( $Start,($Stop-$Start) );
							print sprintf('%06x',$Start)."\t".($Stop-$Start)."\t".$Modified->HexDump( $Start, $Stop )."\n";
						}
						$Mode=0;
					}
					$Position++;
				}
				while( $Position<$Original->{FileSize} );
				
				print $FH IPSmaker->Footer();
				
				close($FH);
			}
			else
			{
				print "*** Files don't have the same size! Can't continue!\n";
				exit 1
			}
		}
		else
		{
			print "*** $ARGV[1] not found!\n";
			exit 1
		}
	}
	else
	{
		print "*** $ARGV[0] not found!\n";
		exit 1
	}
}
else
{
	print "IPSmaker (a simple IPS generator) v1.0\nCopyright (C) 2015 Giovanni Nunes\n\n".
	"This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions.\n\n".
	"Use: ipsmaker <original file> <modified file> <patch file>.ips\n";
}

exit 0;

# MSX Rulez
