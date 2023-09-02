#!/bin/bash

bashalias() {
# get bash aliases
echo -e "\e[101m...\e[0m \e[38;5;82m hole nun die aliases\e[0m"
wget https://gist.githubusercontent.com/KnuTNatioN/854dbf07c6b21dcbde8be0a5f34e2c00/raw/e28f3703a79da4ca5490db77b9e878acb7f9c4f0/.bash_aliases
cat myalias >> /home/pi/.bash_aliases
rm myalias
chown pi:pi .bash_aliases
echo -e "\e[101m...\e[0m \e[38;5;82m bash aliases eingefügt BRA.\e[0m"
}

bashalias   #aliases downloaden und hinzufuegen
