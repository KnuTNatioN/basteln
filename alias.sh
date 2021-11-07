#!/bin/bash

bashalias() {
# get bash aliases
echo -e "\e[101m...\e[0m \e[38;5;82m hole nun die aliases\e[0m"
wget https://gist.githubusercontent.com/KnuTNatioN/d52e83b281f049812d76ea925cbea5d3/raw/b221ec3ea456169e1cdb9d359ee8e676c25bc26b/myalias
cat myalias >> /home/pi/.bash_aliases
rm myalias
chown pi:pi .bash_aliases
echo -e "\e[101m...\e[0m \e[38;5;82m bash aliases eingefügt BRA.\e[0m"
}

bashalias   #aliases downloaden und hinzufuegen