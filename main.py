import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
from time import sleep
import threading


builder = Gtk.Builder()

builder.add_from_file("interface.glade")

class Handler(object):

    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)

        self.button_a_start = builder.get_object('button_a_start')
        self.button_a_stop = builder.get_object('button_a_stop')
        self.button_m_start = builder.get_object('button_m_start')
        self.button_m_stop = builder.get_object('button_m_stop')
        self.apache_status = builder.get_object('apache_status')
        self.mysql_status = builder.get_object('mysql_status')
        self.open_directory = builder.get_object('open_directory')
        self.log_mysql = builder.get_object('log_mysql')
        self.install_lampp = builder.get_object('install_lampp')
        self.button_a_restart = builder.get_object('button_a_restart')
        self.button_m_restart = builder.get_object('button_m_restart')
        self.button_start_all = builder.get_object('button_start_all')
        self.button_stop_all = builder.get_object('button_stop_all')
        self.button_restart_all = builder.get_object('button_restart_all')
        self.button_p_start = builder.get_object('button_p_start')
        self.button_p_stop = builder.get_object('button_p_stop')
        self.ftpd_status = builder.get_object('ftpd_status')
        self.button_p_stop = builder.get_object('button_p_stop')
        self.button_p_restart = builder.get_object('button_p_restart')
        self.about = builder.get_object('about')
        self.apache_port = builder.get_object('apache_port')
        self.mysql_port = builder.get_object('mysql_port')
        self.ftp_port = builder.get_object('ftp_port')
        self.apache_img_status = builder.get_object('apache_img_status')
        self.mysql_img_status = builder.get_object('mysql_img_status')
        self.ftpd_img_status = builder.get_object('ftpd_img_status')
        self.localhost = builder.get_object('localhost')
        self.phpmyadmin = builder.get_object('phpmyadmin')
        self.php_info = builder.get_object('php_info')
        self.entry_apache_port = builder.get_object('entry_apache_port')
        self.send_apache_port = builder.get_object('send_apache_port')
        self.send_mysql_port = builder.get_object('send_mysql_port')
        self.entry_mysql_port = builder.get_object('entry_mysql_port')

        self.instalation_time = 0
# Quit button #
    def on_main_window_destroy(self, *args):
            Gtk.main_quit()

# Getting services port #
    def get_apache_port(self, *args):
        try:
            with open('/etc/apache2/ports.conf', 'r') as apache_port_file: 
                text_file = apache_port_file.readlines()
            self.current_apache_port = str(text_file[4].replace('Listen', '').strip())
            return self.current_apache_port
        except:
            return ''

    def get_mysql_port(self, *args):
        with open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'r') as mysql_port_file:
            text_file = mysql_port_file.readlines()
        self.current_mysql_port = str(text_file[18].replace('#port', '').strip().replace('= ', ''))
        return self.current_mysql_port


# Validating services #
    def validate_apache(self, *args):
        self.status_command_a  = os.popen('service apache2 status').readlines()
        return self.status_command_a

    def validate_mysql(self, *args):
        self.status_command_m  = os.popen('service mysql status').readlines()
        return self.status_command_m
    
    def validate_ftp(self, *args):
        self.status_command_f  = os.popen('service vsftpd status').readlines()
        return self.status_command_f

################################################################################

# Apache service control #

    def on_button_a_start_clicked(self, *args):
        # Start apache service
        if str(self.validate_apache())[0][0] == '●':
            try:
                os.system('service apache2 stop')
            except:
                os.popen('sudo /opt/lampp/lampp stopapache')
        else:
            pass

    def on_button_a_stop_clicked(self, *args):
        # Stop apache service
        if str(self.validate_apache())[0][0] == '●':
            try:
                os.system('service apache2 stop')
            except:
                os.popen('sudo /opt/lampp/lampp stopapache')
        else:
            pass

    def on_button_a_restart_clicked(self, *args):
        # Restart apache service
        if str(self.validate_apache())[0][0] == '●':
            try:
                os.system('service apache2 restart')
            except:
                os.popen('sudo /opt/lampp/lampp reloadapache')
        else:
            pass

################################################################################

# MySQL service control #

    def on_button_m_start_clicked(self, *args):
        # Start apache service
        if str(self.validate_mysql())[0][0] == '●':
            try:
                os.system('service mysql start')
            except:
                os.popen('sudo /opt/lampp/lampp startmysql')
        else:
            pass

    def on_button_m_stop_clicked(self, *args):
        # Stop apache service
        if str(self.validate_mysql())[0][0] == '●':
            try:
                os.system('service mysql stop')
            except:
                os.popen('sudo /opt/lampp/lampp stopmysql')
        else:
            pass

    def on_button_m_restart_clicked(self, *args):
        # Restart apache service
        if str(self.validate_mysql())[0][0] == '●':
            try:
                os.system('service mysql restart')
            except:
                os.popen('sudo /opt/lampp/lampp reloadmysql')
        else:
            pass

################################################################################    

# FTP service control #

    def on_button_p_start_clicked(self, *args):
        # Start FTP service
        if str(self.validate_ftp())[0][0] == '●':
            try:
                os.system('service vsftpd start')
            except:
                os.popen('sudo /opt/lampp/lampp startftp')
        else:
            pass
   
    def on_button_p_stop_clicked(self, *args):
        # Stop FTP service
        if str(self.validate_ftp())[0][0] == '●':
            try:
                os.system('service vsftpd stop')
            except:
                os.popen('sudo /opt/lampp/lampp stopftp')
        else:
            pass
 
    def on_button_p_restart_clicked(self, *args):
        # Restart FTP service
        if str(self.validate_ftp())[0][0] == '●':
            try:
                os.system('service vsftpd restart')
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp reloadftp')
                    os.popen('sudo /opt/lampp/lampp startftp')
            pass

################################################################################    

# Open directory button #

    def on_open_directory_clicked(self, *args):
        try:
            os.popen('cd  /var/www/html; current_user=`logname`; sudo -u ${current_user} nautilus .')
        except:
            os.popen('cd  /var/www/html; current_user=`logname`; sudo -u ${current_user} nemo .')
        else:
            os.popen('cd  /var/www/html; current_user=`logname`; sudo -u ${current_user} dolphin .')

# Open directory logs apache #

    def on_log_mysql_clicked(self,*args):
        try:
            os.popen('cd /var/log/mysql; current_user=`logname`; sudo -u ${current_user} nautilus .')
        except:
            os.popen('cd /var/log/mysql; current_user=`logname`; sudo -u ${current_user} nemo .')
        else:
            os.popen('cd /var/log/mysql; current_user=`logname`; sudo -u ${current_user} dolphin .')

# Open about #

    def on_about_clicked(self, *args):
        os.popen('sudo -u `logname` sensible-browser  https://github.com/CleoMenezes/LAMPP-Manager/ ; exit')

# Open localhost #

    def on_localhost_clicked(self, *args):
        os.popen(f'sudo -u `logname` sensible-browser http://localhost:{str(self.get_apache_port())}/ ; exit')

# Open phpmyadmin

    def on_phpmyadmin_clicked(self, *args):
        os.popen(f'sudo -u `logname` sensible-browser http://localhost:{str(self.get_apache_port())}/phpmyadmin/ ; exit')

# Open info.php

    def on_php_info_clicked(self, *args):
        os.popen(f'sudo -u `logname` sensible-browser http://localhost:{str(self.get_apache_port())}/info.php ; exit')


# Start all services #
    def on_button_start_all_clicked(self, *args):

        self.on_button_a_start_clicked()
        self.on_button_m_start_clicked()
        self.on_button_p_start_clicked()

# Stop all services #
    def on_button_stop_all_clicked(self, *args):    

        self.on_button_a_stop_clicked()
        self.on_button_m_stop_clicked()
        self.on_button_p_stop_clicked()

# Restart all services #
    def on_button_restart_all_clicked(self, *args):

        self.on_button_a_restart_clicked()
        self.on_button_m_restart_clicked()
        self.on_button_p_restart_clicked()

# Install LAMPP #
        
    def on_install_lampp_clicked(self, *args):
        self.instalation_time += 1
        os.popen('cd install && for terminal in $TERMINAL x-terminal-emulator urxvt rxvt terminator Eterm aterm xterm gnome-terminal roxterm xfce4-terminal; do if which $terminal > /dev/null 2>&1; then exec $terminal --noclose -e sudo ./install.sh; fi; done')

################################################################################ 

# change ports #

    def on_send_apache_port_clicked(self, *args):
        # Change apache port
        current_port = self.current_apache_port 
        new_port = self.entry_apache_port.get_text()
        os.popen(f'sudo sed -i "5 s/{current_port}/{new_port}/" /etc/apache2/ports.conf')

    def on_send_mysql_port_clicked(self, *args):
        # Change apache port
        with open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'r') as mysql_port_file:
            text_file = mysql_port_file.readlines()
        current_port = str(text_file[18].replace('#port', '').strip().replace('= ', ''))
        new_port = self.entry_mysql_port.get_text()
        os.popen(f'sudo sed -i "5 s/{current_port}/{new_port}/" /etc/mysql/mariadb.conf.d/50-server.cnf')


################################################################################ 

class CurrentServiceStatus(Handler):
    def __init__(self, *args):
        super().__init__()

        while True:

# Putting current status of Apache #

            a_first_status = self.apache_status.get_label()
            if str(a_first_status) != 'Active' or str(a_first_status) != 'Inactive':       
                    try:
                        if self.validate_apache()[0][0] == '●':  
                            try:
                                if self.validate_apache()[0][0] == '●':
                                    if 'dead' in self.validate_apache()[2]:
                                        self.apache_status.set_text('Inactive')
                                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                                    elif 'running' in self.validate_apache()[2]:
                                        self.apache_status.set_text('Active')
                                        self.apache_img_status.set_from_icon_name('emblem-default', 1)
                                    else:
                                        self.apache_status.set_text('Cannot connect')
                                        self.apache_img_status.set_from_icon_name('emblem-important', 1)
                                        
                                
                            except:
                                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                                    status_command = os.popen('sudo /opt/lampp/lampp status').readlines()
                                    if 'Apache is not running' in self.validate_apache()[2]:
                                        self.apache_status.set_text('Inactive')
                                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                                    elif 'Apache is running' in self.validate_apache()[2]:
                                        self.apache_status.set_text('Active')
                                        self.apache_img_status.set_from_icon_name('emblem-default', 1)                            
                                    else:
                                        self.apache_status.set_text('Cannot connect')
                                        self.apache_img_status.set_from_icon_name('emblem-important', 1)                    
                                    
                    except IndexError:
                        self.apache_status.set_text('Not found')
                        self.apache_img_status.set_from_icon_name('emblem-important', 1)

# Putting current status of MySQL service #

            m_first_status = self.mysql_status.get_label()
            if str(m_first_status) != 'Active' or str(m_first_status) != 'Inactive':
                    try:
                        if self.validate_mysql()[0][0] == '●': 
                            try:               
                                if self.validate_mysql()[0][0] == '●':
                                    if 'dead' in self.validate_mysql()[2]:
                                        self.mysql_status.set_text('Inactive')
                                        self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)

                                    elif 'running' in self.validate_mysql()[2]:
                                        self.mysql_status.set_text('Active')
                                        self.mysql_img_status.set_from_icon_name('emblem-default', 1)

                                    
                            except:
                                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                                    status_command_m1 = os.popen('sudo /opt/lampp/lampp status').readlines()
                                    if 'MySQL is not running' in self.validate_mysql()[2]:
                                        self.mysql_status.set_text('Inactive')
                                        self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                                    elif 'Apache is running' in self.validate_mysql()[2]:
                                        self.mysql_status.set_text('Active')
                                        self.mysql_img_status.set_from_icon_name('emblem-default', 1)
                                        
                    except IndexError:
                        self.mysql_status.set_text('Not found')
                        self.mysql_img_status.set_from_icon_name('emblem-important', 1)

# Putting current status of FTP service #

            p_first_status = self.ftpd_status.get_label()
            if str(p_first_status) != 'Active' or str(p_first_status) != 'Inactive':
                    try:
                        if self.validate_ftp()[0][0] == '●':  
                            try:               
                                if self.validate_ftp()[0][0] == '●':
                                    if 'dead' in self.validate_ftp()[2]:
                                        self.ftpd_status.set_text('Inactive')
                                        self.ftpd_img_status.set_from_icon_name('emblem-unreadable', 1)

                                    elif 'running' in self.validate_ftp()[2]:
                                        self.ftpd_status.set_text('Active')
                                        self.ftpd_img_status.set_from_icon_name('emblem-default', 1)

                                    
                            except:
                                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                                    status_command = os.popen('pkexec /opt/lampp/lampp status').readlines()
                                    if 'ProFTPD is deactivated' in validate_ftp()[3] or 'ProFTPD is not running' in validate_ftp()[3]:
                                        self.ftpd_status.set_text('Inactive')
                                        self.ftpd_img_status.set_from_icon_name('emblem-unreadable', 1)
                                    elif 'ProFTPD is running' in validate_ftp()[3]:
                                        self.ftpd_status.set_text('Active')
                                        self.ftpd_img_status.set_from_icon_name('emblem-default', 1)
                                        
                    except IndexError:
                        self.ftpd_status.set_text('Not found')
                        self.ftpd_img_status.set_from_icon_name('emblem-important', 1)

# putting current apache's port #################################################################################

            try:
                if self.validate_apache()[0][0] == '●':
                    with open('/etc/apache2/ports.conf', 'r') as apache_port_file: 
                        text_file = apache_port_file.readlines()
                    self.apache_port.set_text(str(text_file[4].replace('Listen', '').strip()))

                    current_a = str(text_file[4].replace('Listen', '').strip())
                    current_b = str(self.entry_apache_port.get_text())
                    if current_b == str("."):
                        self.entry_apache_port.set_text(str(text_file[4].replace('Listen', '').strip()))
                    elif current_b == current_a:
                        pass

            except:        
                self.entry_apache_port.set_text('Not found')

# Putting current MySQL's port #
            
            try:
                if self.validate_mysql()[0][0] == '●':
                    status_command_m  = os.popen('service mysql status').readlines()
                    if status_command_m[0][0] == '●':
                        with open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'r') as mysql_port_file:
                            text_file = mysql_port_file.readlines()
                        self.mysql_port.set_text(text_file[18].replace('#port', '').strip().replace('= ', ''))

                        current_a = str(text_file[18].replace('#port', '').strip().replace('= ', ''))
                        current_b = str(self.entry_mysql_port.get_text())


                        if current_b == str("."):
                            self.entry_mysql_port.set_text(text_file[18].replace('#port', '').strip().replace('= ', ''))
                        elif current_b == current_a:
                            pass
            except:
                self.entry_mysql_port.set_text('Not found')
            
# Defalt FTP's port #
            if self.validate_ftp()[0][0] == '●':
                self.ftp_port.set_text('2121')

            sleep(5)
            
            if self.instalation_time == 1:
                sleep(20)
                self.instalation_time = 0


main_thread = CurrentServiceStatus
thread = threading.Thread(target=main_thread)
thread.daemon = True
thread.start()
    
builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()

if __name__ == '__main__':
    Gtk.main()
