#!/bin/bash

echo '#################### Welcome LAMPP Manager install ####################';
sleep 4;
echo '';
echo '';
echo '### This script will install everything you need to have LAMPP on your computer. ###';
sleep 4;
echo '';
echo '';
echo '';
echo '';
echo '>>>>> Although much of the installation is automated, you need to pay attention as some parts will require you to do what is necessary.';
sleep 4;
echo '';
echo '';
echo '#################### Now lets install Apache2 ####################';
sleep 4;
echo '';
echo '';
sudo apt install apache2 -y;
echo '';
echo '';
echo '### Take a look if you installed correctly by accessing localhost. ###';
echo '';
echo '';
sleep 5;
sensible-browser localhost;
sleep 4;
echo '';
echo '';
echo '#################### Now lets install MariaDB(MySQL) ####################';
echo '';
echo '';
sleep 4;
sudo apt install mariadb-server -y;
echo '';
echo '';
echo '### We will also install your respective client ###';
echo '';
echo '';
sudo apt install mariadb-client -y;
echo '';
echo '';
echo '### Lets secure the MySQL installation ###'
echo '';
echo '';
sleep 4;
echo '### It will ask us if we want to change the root password, if so, enter it 2 times. ###'
echo '';
sleep 10;
echo '';
sudo mysql_secure_installation;
echo '';
echo ''
echo ' ### Remember that after installation you will still need to configure MySQL. ###'
sleep 4;
echo '';
echo '';
echo '#################### Now lets install PHP. ####################';
echo '';
echo '';
sleep 4;
echo '### We will also install php-fpm, php-gd, php-curl, php-mysql and libapache2-mod-php. ###';
echo '';
echo '';
sleep 4;
sudo apt install php php-fpm php-gd php-curl php-mysql libapache2-mod-php -y;
echo ''
echo '';
sleep 4;
echo '### I suppose you will also need optimized settings for Wordpress. ###';
sleep 4;
echo '';
echo '';
echo '#################### Lets activate the REWRITE module. ####################';
echo '';
echo '';
sleep 4;
echo '### Essential for WordPress permanent links (slugs) to work. ###';
echo '';
echo '';
sleep 4;
sudo a2enmod rewrite;
sleep 4;
echo '';
echo '';
echo '### Just a moment. Now it going to restart Apache. ###';
echo '';
echo '';
sleep 4;
sudo service apache2 restart;
echo '';
echo '';
echo '#################### Optimal settings in the php.ini file. ####################';
sleep 4;
echo '';
echo '';
echo '### Copy the following information, I will give you 20 seconds so you can do it smoothly. ###';
echo '';
echo '';
sleep 5;
echo -e '<Directory "/var/www/html">\n\tAllowOverride All\n</Directory>';
echo '';
sleep 20;
echo '';
echo -e '### Now paste in the last line and save in the nano file that will open in a few seconds.\nCtrl+S to save\nEnter to confirm\nCtrl+X to exit. ###';
sleep 6;
echo '';
echo '';
sudo nano /etc/apache2/sites-available/000-default.conf
echo '';
echo '';
echo '#################### Lets install phpMyAdmin. ####################';
sleep 4;
echo '';
echo '';
echo '### Before we are going to install the following PHP plugins. ###';
echo '';
echo '';
sleep 4;
sudo apt install php-imagick php-phpseclib php-common php-imap php-zip php-xml php-mbstring php-bz2 -y;
echo '';
echo '### Just a moment. Now it going to restart Apache. ###';
echo '';
echo '';
sleep 4;
sudo service apache2 restart -y;
echo '';
echo '';
echo '### Lets download the latest stable version of phpMyAdmin. ###';
echo '';
echo '';
sleep 4;
echo '';
echo '';
sudo apt install unzip -y;
echo '';
echo '';
wget https://files.phpmyadmin.net/phpMyAdmin/4.9.7/phpMyAdmin-4.9.7-all-languages.zip;
echo '';
echo '';
unzip phpMyAdmin-4.9.7-all-languages.zip;
echo '';
echo '';
sudo mv phpMyAdmin-4.9.7-all-languages /usr/share/phpmyadmin;
echo '';
echo '';
sudo chown -R www-data:www-data /usr/share/phpmyadmin;
echo '';
echo '';
echo '';
echo '';
echo '';
echo '';
echo '';
echo -e '### It is ideal that you create the phpMyAdmin database and assign it to our user as in the example below. You can do later:\n\nsudo mysql -u root -p\nCREATE DATABASE phpmyadmin;\nGRANT ALL PRIVILEGES ON phpmyadmin.* TO your_username;\n FLUSH PRIVILEGES;. ###';
echo '';
echo '';
echo '';
echo '';
echo '';
echo '';
echo '';
echo '';
sleep 15;
echo '';
echo '';
echo '### Save the file that will open next in the path /etc/apache2/conf-available/ ###';
echo '';
echo '';
sleep 15;
sudo nano phpmyadmin.conf
echo '';
echo '';
echo '### Lets enable the snippet for the configuration ###';
echo '';
echo '';
sudo a2enconf phpmyadmin.conf
echo '';
echo '';
sleep 4;
echo '### Lets create the temporary directory of phpMyAdmin ###';
echo '';
echo '';
sleep 4;
sudo mkdir -p /var/lib/phpmyadmin/tmp
echo '';
echo '';
sleep 4;
echo '### Lets make the web server user (www-data) own the directory ###';
echo '';
echo '';
sleep 4;
sudo chown www-data:www-data /var/lib/phpmyadmin/tmp;
echo '';
echo '';
echo '### Just a moment. Now it going to restart Apache. ###';
sleep 4;
sudo service apache2 reload;
echo '';
echo '';
echo '### Check that phpMyAdmin is installed correctly. ###';
echo '';
echo '';
sensible-browser http://localhost/phpmyadmin
echo '';
echo '';
sleep 4;
echo '#################### Lets set permission to html folder. ####################';
sudo chmod 777 -R /var/www/html;
echo '';
echo '';
sleep 3;
echo 'Enjoy!';
