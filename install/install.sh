#!/bin/bash

echo '#################### Welcome LAMPP Manager install ####################';
sleep 3;
echo ; echo ; echo
echo '>> This script will install everything you need to have LAMPP on your computer.';
sleep 3;
sudo apt install wget
echo ; echo ; echo
echo '#################### Now lets install Apache2 ####################';
sleep 3;
echo ; echo ; echo
sudo apt install apache2 -y;
echo ; echo ; echo
echo '>> Take a look if you installed correctly by accessing localhost.';
echo ; echo ; echo
sleep 3;
sensible-browser localhost;
sleep 3;
echo ; echo ; echo
echo '>> If the browser does not open correctly, access localhost through it.';
sleep 3
echo ; echo ; echo
echo '#################### Now lets install MariaDB(MySQL) ####################';
echo ; echo ; echo
sleep 3;
sudo apt install mariadb-server -y;
echo ; echo ; echo
echo '>> We will also install your respective client';
echo ; echo ; echo
sudo apt install mariadb-client -y;
echo ; echo ; echo
#echo '#################### Lets secure the MySQL installation ####################'
#echo ; echo ; echo
#sleep 4;
#echo '>> It will ask us if we want to change the root password, if so, enter it 2 times.'
#sleep 10;
#echo ; echo ; echo
#sudo mysql_secure_installation;

echo '>> Remember that after installation you will still need to configure MySQL.'
sleep 3;
echo ; echo ; echo
echo '#################### Now lets install PHP. ####################';
echo ; echo ; echo
sleep 3;
echo '>> We will also install php-fpm, php-gd, php-curl, php-mysql and libapache2-mod-php.';
echo ; echo ; echo
sleep 3;
sudo apt install php php-fpm php-gd php-curl php-mysql libapache2-mod-php -y;
sleep 3;
echo 'Check if PHP has been installed correctly';
sleep 2;
wget --------------------------------------------
sensible-browser http://localhost/info.php
echo ; echo ; echo
echo '>> I suppose you will also need optimized settings for Wordpress.';
sleep 3;
echo ; echo ; echo
echo '#################### Lets activate the REWRITE module. ####################';
echo ; echo ; echo
sleep 3;
echo '>> Essential for WordPress permanent links (slugs) to work.';
echo ; echo ; echo
sleep 3;
sudo a2enmod rewrite;
sleep 3;
echo ; echo ; echo
echo '>> Just a moment. Now it going to restart Apache.';
echo ; echo ; echo
sleep 3;
sudo service apache2 restart;
echo ; echo ; echo

echo '#################### Optimal settings in the php.ini file. ####################';
sleep 3;
echo ; echo ; echo
wget --------------------------------------
sudo mv 000-default.conf /etc/apache2/sites-available/
echo ; echo ; echo
echo '#################### Lets install phpMyAdmin. ####################';
sleep 3;
echo ; echo ; echo
echo '>> Before we are going to install the following PHP plugins.';
echo ; echo ; echo
sleep 3;
sudo apt install php-imagick php-phpseclib php-common php-imap php-zip php-xml php-mbstring php-bz2 -y;
echo ; echo ; echo
echo '>> Just a moment. Now it going to restart Apache.';
echo ; echo ; echo
sleep 3;
sudo service apache2 restart -y;
echo ; echo ; echo
echo '>> Lets download the latest stable version of phpMyAdmin.';
echo ; echo ; echo
sleep 3;
echo ; echo ; echo
sudo apt install unzip -y;
echo ; echo ; echo
wget https://files.phpmyadmin.net/phpMyAdmin/4.9.7/phpMyAdmin-4.9.7-all-languages.zip;
echo ; echo ; echo
unzip phpMyAdmin-4.9.7-all-languages.zip;
echo ; echo ; echo
sudo mv phpMyAdmin-4.9.7-all-languages /usr/share/phpmyadmin;
echo ; echo ; echo
sudo chown -R www-data:www-data /usr/share/phpmyadmin;
echo ; echo ; echo
echo -e '>> It is ideal that you create the phpMyAdmin database and assign it to our user as in the example below. You can do later:\n\nsudo mysql -u root -p\nCREATE DATABASE phpmyadmin;\nGRANT ALL PRIVILEGES ON phpmyadmin.* TO your_username;\n FLUSH PRIVILEGES;.';
sleep 7;
echo ; echo ; echo
wget ----------------------------------------------
sudo mv phpmyadmin.conf phpmyadmin.conf;
echo ; echo ; echo
sleep 3;
echo '>> Lets enable the snippet for the configuration';
echo ; echo ; echo
sleep 3;
sudo a2enconf phpmyadmin.conf
echo ; echo ; echo
sleep 3;
echo '>> Lets create the temporary directory of phpMyAdmin';
echo ; echo ; echo
sleep 3;
sudo mkdir -p /var/lib/phpmyadmin/tmp
echo ; echo ; echo
sleep 3;
echo '>> Lets make the web server user (www-data) own the directory';
echo ; echo ; echo
sleep 3;
sudo chown www-data:www-data /var/lib/phpmyadmin/tmp;
echo ; echo ; echo
sleep 3;
echo '>> Just a moment. Now it going to restart Apache.';
sleep 3;
sudo service apache2 reload;
echo ; echo ; echo
echo '>> Check that phpMyAdmin is installed correctly.';
echo ; echo ; echo
sleep 3;
sensible-browser http://localhost/phpmyadmin
echo ; echo ; echo
sleep 3;
echo ; echo ; echo
echo '#################### Lets install VSFTP. ####################';
echo ; echo ; echo
sleep 3;
sudo apt-get install vsftpd
echo ; echo ; echo
sleep 3;
echo '#################### Lets set permission to html folder. ####################';
sudo chmod 777 -R /var/www/html;
echo ; echo ; echo
sleep 3;
echo 'Enjoy!';

