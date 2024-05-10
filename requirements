#!/bin/bash
printf "\033[?47h"
printf "\033["$(tput lines)"A"
if [ -f /usr/bin/python3 ]
then
	echo "Python3 was installed"
else
	sudo apt install python3
fi
if [ -d /usr/lib/python3/dist-packages/pygame ]
then
	echo "Pygame was installed"
else
	sudo apt install python3-pygame
fi
if [ -d /usr/lib/python3/dist-packages/mutagen ]
then
        echo "Mutagen was installed"
else
        pip3 install mutagen
fi	
if [ -f /usr/bin/jp2a ]
then
	echo "jp2a was installed"
else
	sudo apt install jp2a
fi
sleep 2
printf "\033[?47l"
