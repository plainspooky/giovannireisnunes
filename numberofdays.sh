#!/bin/bash
#
#  Number of Days
#  Print the number of days in a/this month
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

function numofdays()
{
	MONTH=$1
	
	case $MONTH in
	#
	# feb
	#
		2)
		cal -m 2 | grep 29 >/dev/null 2>&1
		if [ $? -eq 0 ]
		then
			DAYS=29 # leap year
		else
			DAYS=28 # ordinary year
		fi
		;;
		#
		# apr, jun, sep and nov
		#
		4|6|9|11)
		DAYS=30
		;;
		#
		# jan, mar, may, jul, aug, oct and dec
		#
		1|3|5|7|8|10|12)
		DAYS=31
		;;
		#
		# oh my god! they created a new month!
		#
		*)
		DAYS=0
		;;
	esac
	#
	# send the number of day
	#
	echo ${DAYS}
}

case $1 in
	1|2|3|4|5|6|7|8|9|10|11|12)
	numofdays $1
	;;
	'')
	numofdays $( date +%-m )
	;;
	*)
	echo "What?"
	exit 1
	;;
esac

exit 0
