#!/bin/bash

echo '#################### Welcome LAMPP Manager install ####################'
echo ; echo ; echo
echo '>> This script will install everything you need to have LAMPP on your computer.'
sudo apt install wget
echo ; echo ; echo
echo '#################### Now lets install Apache2 ####################'
echo ; echo ; echo
sudo apt install apache2 -y
echo ; echo ; echo
echo '>> Take a look if you installed correctly by accessing localhost.'
echo ; echo ; echo
sensible-browser localhost
echo ; echo ; echo
echo '>> If the browser does not open correctly, access localhost through it.'
echo ; echo ; echo
echo '#################### Now lets install MariaDB(MySQL) ####################'
echo ; echo ; echo
sudo apt install mariadb-server -y
echo ; echo ; echo
echo '>> We will also install your respective client'
echo ; echo ; echo
sudo apt install mariadb-client -y
echo ; echo ; echo
echo '>> Remember that after installation you will still need to configure MySQL.'
echo ; echo ; echo
echo '#################### Now lets install PHP. ####################'
echo ; echo ; echo
echo '>> We will also install php-fpm, php-gd, php-curl, php-mysql and libapache2-mod-php.'
echo ; echo ; echo
sudo apt install php php-fpm php-gd php-curl php-mysql libapache2-mod-php -y
echo 'Check if PHP has been installed correctly'
wget https://github.com/CleoMenezes/LAMPP-Manager/blob/master/configuration%20files/info.php
sudo mv info.php /var/www/html/
sensible-browser http://localhost/info.php
echo ; echo ; echo
echo '>> I suppose you will also need optimized settings for Wordpress.'
echo ; echo ; echo
echo '#################### Lets activate the REWRITE module. ####################'
echo ; echo ; echo
echo '>> Essential for WordPress permanent links (slugs) to work.'
echo ; echo ; echo
sudo a2enmod rewrite
echo ; echo ; echo

echo '#################### Optimal settings in the php.ini file. ####################'
echo ; echo ; echo
wget https://github.com/CleoMenezes/LAMPP-Manager/blob/master/configuration%20files/000-default.conf
sudo mv 000-default.conf /etc/apache2/sites-available/
echo ; echo ; echo
echo '#################### Lets install phpMyAdmin. ####################'
echo ; echo ; echo
echo '>> Before we are going to install the following PHP plugins.'
echo ; echo ; echo
sudo apt install php-imagick php-phpseclib php-common php-imap php-zip php-xml php-mbstring php-bz2 -y

echo ; echo ; echo
echo '>> Lets download the latest stable version of phpMyAdmin.'
echo ; echo ; echo
echo ; echo ; echo
sudo apt install unzip -y
echo ; echo ; echo
wget https://files.phpmyadmin.net/phpMyAdmin/4.9.7/phpMyAdmin-4.9.7-all-languages.zip
echo ; echo ; echo
unzip phpMyAdmin-4.9.7-all-languages.zip
echo ; echo ; echo
sudo mv phpMyAdmin-4.9.7-all-languages /usr/share/phpmyadmin
echo ; echo ; echo
sudo rm phpMyAdmin-4.9.7-all-languages.zip
echo ; echo ; echo
sudo chown -R www-data:www-data /usr/share/phpmyadmin
echo ; echo ; echo
echo -e '>> It is ideal that you create the phpMyAdmin database and assign it to our user as in the example below. You can do later:\n\nsudo mysql -u root -p\nCREATE DATABASE phpmyadmin;\nGRANT ALL PRIVILEGES ON phpmyadmin.* TO your_username;\n FLUSH PRIVILEGES;.'
echo ; echo ; echo
wget https://github.com/CleoMenezes/LAMPP-Manager/blob/master/configuration%20files/phpmyadmin.conf
sudo mv phpmyadmin.conf /etc/apache2/conf-available/
echo ; echo ; echo
echo '>> Lets enable the snippet for the configuration'
echo ; echo ; echo
sudo a2enconf phpmyadmin.conf
echo ; echo ; echo
echo '>> Lets create the temporary directory of phpMyAdmin'
echo ; echo ; echo
sudo mkdir -p /var/lib/phpmyadmin/tmp
echo ; echo ; echo
echo '>> Lets make the web server user (www-data) own the directory'
echo ; echo ; echo
sudo chown www-data:www-data /var/lib/phpmyadmin/tmp
echo ; echo ; echo
echo '>> Check that phpMyAdmin is installed correctly.'
echo ; echo ; echo
sensible-browser http://localhost/phpmyadmin
echo ; echo ; echo
echo '#################### Lets install VSFTP. ####################'
echo ; echo ; echo
sudo apt-get install vsftpd
echo ; echo ; echo
echo '#################### Lets set permission to html folder. ####################'
sudo chmod 777 -R /var/www/html
echo ; echo ; echo
sleep 3;
echo 'Enjoy!';

