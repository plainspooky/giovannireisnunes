#!/bin/bash
#
#  Old Kernel Cleaner (Ubuntu)
#  Just a way to remove older linux kernel images from a Ubuntu system
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

# keeping at least X newer linux images
TOKEEP=3

# get LSB release information
source /etc/lsb-release

# check where is running.
if [ ${DISTRIB_ID} = "Ubuntu" ]; then
    PACKAGE='linux-image'
    LINUX=$( dpkg -l ${PACKAGE}-[0-9]* | grep "ii " | awk '{ print $2 }' | tac )
    COUNT=0
    LIST=''
    # for each package found...
    for IMAGE in ${LINUX}; do
        if [ ${COUNT} -lt ${TOKEEP} ] ; then
            if [ ${COUNT} -eq 0 ]; then
                echo "Keeping:"
            fi
            echo "  ${IMAGE}"
        else
            LIST=${LIST}' '${IMAGE}
        fi
        COUNT=$((COUNT=COUNT+1))
    done
    # for safety I don't run 'apt-get', please copy & paste
    echo -e "\nTry this:\napt-get remove --purge${LIST}"
else
    echo "Ubuntu only!"
    exit 1
fi

exit 0
