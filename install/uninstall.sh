#!/bin/bash

sudo apt purge --remove mariadb-server -y
sudo apt purge --remove mariadb-client -y
sudo apt purge --remove php* -y
sudo apt purge --remove phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
sudo apt purge --remove vsftpd -y
sudo apt purge --remove apache2 apache2-bin -y
sudo apt autoremove -y
echo
echo 'Restart LAMPP Manager and see you son!'
exit