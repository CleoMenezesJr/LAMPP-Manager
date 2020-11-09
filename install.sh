#!/bin/bash
sudo apt install apache2 -y &&
                        sensible-browser localhost &&
                        sudo apt install mariadb-server -y &&
                        sudo apt install mariadb-client -y &&
                        sudo apt install php7 php7-fpm php7-gd php7-curl php7-mysql libapache2-mod-php7 - y &&
                        sudo service apache2 restart &&
                        sudo a2enmod rewrite -y &&
                        sudo sudo service apache2 restart &&
                        sudo apt install php-imagick php-phpseclib php-gettext php7.*-imap php7.*-zip php7.*-xml php7.*-mbstring php7.*-bz2 php7.*-intl -y &&
                        sudo service apache2 restart &&
                        wget https://files.phpmyadmin.net/phpMyAdmin/4.9.7/phpMyAdmin-4.9.7-all-languages.zip -y &&
                        sudo apt install unzip -y &&
                        unzip phpMyAdmin-4.9.7-all-languages.zip -y &&
                        sudo mv phpMyAdmin-4.9.7-all-languages /usr/share/phpmyadmin -y &&
                        sudo chown -R www-data:www-data /usr/share/phpmyadmin -y &&
                        sudo mkdir -p /var/lib/phpmyadmin/tmp -y &&
                        sudo chown www-data:www-data /var/lib/phpmyadmin/tmp -y &&
                        sudo service apache2 reload &&
                        sensible-browser http://localhost/phpmyadmin