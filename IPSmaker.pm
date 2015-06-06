#
#  IPSmaker v0.1 (Perl Module)
#
#  This file contais the class used in IPSmaker
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
package IPSmaker;
use strict;
use warnings;

sub new
{
	my ( $class ) = shift;
	my $self={ FileName =>shift, FileSize=>0, FileData=>'' };
	my ( $filesize, $filedata, $filename, $fh );
	
	$filename = $self->{FileName};
	
	open($fh, '<', $filename) or die "*** Could not open file '".$filename."'!";
	
	binmode $fh,":raw";
	$filesize=-s $filename;
	read $fh,$filedata,$filesize;
	
	close($fh);
	
	$self->{FileSize}=$filesize;
	$self->{FileData}=$filedata;
	
	bless $self, $class;
	return $self;
}

sub Byte()
{
	my ( $self, $Pos ) = @_;
	
	if ( $Pos < $self->{FileSize} )
	{
		return vec($self->{FileData}, $Pos, 8);
	}
	else
	{
		return -1;
	}
}

sub Record()
{
	my ( $self, $Address, $Size ) = @_;
	return Spliter(sprintf('%06x',$Address)).Spliter(sprintf('%04x',$Size)).substr($self->{FileData}, $Address, $Size);
}

sub HexDump()
{
	my ( $self, $IniPos, $EndPos ) = @_;
	
	my ( $Data, $Hex, $Ascii );
	
	for ( my $Count=$IniPos; $Count<$EndPos; $Count++ )
	{
		$Data=vec($self->{FileData}, $Count, 8);
		
		$Hex.=sprintf('%02x',$Data  )." ";
		
		if ( $Data>=33 and $Data<=127 )
		{
			$Ascii.=chr($Data);
		}
		else
		{
			$Ascii.='.';
		}
	}
	
	return $Hex."\t".$Ascii;
}

sub Spliter()
{
	my ( $i, $j, $Data, $Value );
	
	$Value=$_[0];
	
	for ( $i=0; $i<length($Value); $i=$i+2 )
	{
		$Data.=chr( hex substr($Value,$i,2) );
	}
	
	return $Data;
}

sub Header()
{
	return	"PATCH";
}

sub Footer()
{
	return "EOF";
}

1;
