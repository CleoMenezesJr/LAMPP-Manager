#!/bin/bash

sudo apt update & sudo apt upgrade -y
sudo apt purge --remove apache* php* mariadb* -y
sudo apt autoremove -y
sudo apt install mariadb-server -y
sudo apt install mariadb-client -y
sudo apt install php -y
cd  /opt/LAMPP-Manager/configuration\ files
sudo mv -f /opt/LAMPP-Manager/configuration\ files/ info.php /var/www/html/
sudo a2enmod rewrite
sudo service apache2 restartx
cd  /opt/LAMPP-Manager/configuration\ files
sudo mv -f 000-default.conf /etc/apache2/sites-available/
sudo apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
cd  /opt/LAMPP-Manager/configuration\ files
sudo mv apache2.conf /etc/apache2/
sudo ln -s /usr/share/phpmyadmin /var/www/
sudo chown -R www-data:www-data /usr/share/phpmyadmin
sudo a2enconf phpmyadmin.conf
sudo mkdir -p /var/lib/phpmyadmin/tmp
sudo chown www-data:www-data /var/lib/phpmyadmin/tmp
sudo a2enmod proxy_fcgi setenvif
sudo chmod 777 -R /var/www/html
sudo apt-get install vsftpd
sudo apt install libnotify-bin
sudo apt install apache2-bin  -y
sudo a2enconf php*.*-fpm
sudo apt install apache2

echo
echo 'Restart LAMPP Manager and Enjoy!'
exit