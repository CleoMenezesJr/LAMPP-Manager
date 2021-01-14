#!/bin/bash

sudo apt purge --remove install mariadb-server -y
sudo apt purge --removemariadb-client -y
sudo apt purge --remove php*
sudo apt purge --remove phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
sudo apt purge --remove apache2 apache2-bin -y
sudo apt purge --remove vsftpd
sudo apt purge --remove libnotify-bin
sudo apt autoremove
exit