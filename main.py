import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import webbrowser

builder = Gtk.Builder()

builder.add_from_file("interface.glade")

class Handler(object):
    def __init__(self, *args, **kwargs):
        super(Handler, self). __init__(*args, **kwargs)

        self.button_a_start = builder.get_object('button_a_start')
        self.button_a_stop = builder.get_object('button_a_stop')
        self.button_m_start = builder.get_object('button_m_start')
        self.button_m_stop = builder.get_object('button_m_stop')
        self.apache_status = builder.get_object('apache_status')
        self.mysql_status = builder.get_object('mysql_status')
        self.open_directory = builder.get_object('open_directory')
        self.install_lampp = builder.get_object('install_lampp')
        self.button_a_restart = builder.get_object('button_a_restart')
        self.button_m_restart = builder.get_object('button_m_restart')
        self.button_start_all = builder.get_object('button_start_all')
        self.button_stop_all = builder.get_object('button_stop_all')
        self.button_restart_all = builder.get_object('button_restart_all')
        self.button_p_start = builder.get_object('button_p_start')
        self.button_p_stop = builder.get_object('button_p_stop')
        self.proftp_status = builder.get_object('proftp_status')
        self.button_p_stop = builder.get_object('button_p_stop')
        self.button_p_restart = builder.get_object('button_p_restart')
        self.about = builder.get_object('about')



###########################################################################

#putting current status of apacher service WORKING
        status_command_a  = os.popen('service apache2 status').readlines()
        a_first_status = self.apache_status.get_label()
        try:
            if str(a_first_status) != 'Active' or str(a_first_status) != 'Inactive':
                if 'dead' in str(status_command_a[2]):
                    self.apache_status.set_text('Inactive')
                elif 'running' in str(status_command_a[2]):
                    self.apache_status.set_text('Active')
                else:
                    self.apache_status.set_text('Not Installed')
                    
        except:
            if str(a_first_status) != 'Active' or str(a_first_status) != 'Inactive':
                status_command  = os.popen('pkexec /opt/lampp/lampp status').readlines()
                if 'Apache is not running' in str(status_command[1]):
                    self.apache_status.set_text('Inactive')
                elif 'Apache is running' in str(status_command[1]):
                    self.apache_status.set_text('Active')
                else:
                    self.apache_status.set_text('Not Installed')



#putting current status of mysql service
        
        status_command_m  = os.popen('service mysql status').readlines()
        m_first_status = self.mysql_status.get_label()
        try:
            if str(m_first_status) != 'Active' or str(m_first_status) != 'Inactive':
                if 'dead' in str(status_command_m[2]):
                    self.mysql_status.set_text('Inactive')
                elif 'running' in str(status_command_m[2]):
                    self.mysql_status.set_text('Active')
                else:
                    self.mysql_status.set_text('Not Installed')

        except:
            if str(a_first_status) != 'Active' or str(a_first_status) != 'Inactive':
                status_command  = os.popen('pkexec /opt/lampp/lampp status').readlines()
                if 'MySQL is not running' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
                elif 'MySQL is running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
                else:
                    self.mysql_status.set_text('Not Installed')


#putting current status of proftp service

        p_first_status = self.proftp_status.get_label()
        if str(p_first_status) != 'Active' or str(p_first_status) != 'Inactive':
            status_command  = os.popen('pkexec /opt/lampp/lampp status').readlines()
            if 'ProFTPD is deactivated' in str(status_command[3]):
                self.proftp_status.set_text('Inactive')
            elif 'ProFTPD is running' in str(status_command[3]):
                self.proftp_status.set_text('Active')
            else:
                self.proftp_status.set_text('Not Installed')

################################################################################

        

#quit button
    def on_main_window_destroy(self, *args):
        Gtk.main_quit()


################################### APACHE BUTTONS ##############################################

#apache start button WORKING
    def on_button_a_start_clicked(self, *args):
        
        try:
            if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:            
                os.system('service apache2 start')
                status_command = os.popen('service apache2 status').readlines()  
                if 'dead' in str(status_command[2]):
                    self.apache_status.set_text('Inactive')
                elif 'running' in str(status_command[2]):
                    self.apache_status.set_text('Active')
        except:
            os.popen('pkexec /opt/lampp/lampp startapache')
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'Apache is not running' in str(status_command[1]):
                self.apache_status.set_text('Inactive')
            elif 'Apache is running' in str(status_command[1]):
                self.apache_status.set_text('Active')


#apache stop button WORKING
    def on_button_a_stop_clicked(self, *args):
        
        try:
            if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:
                os.system('service apache2 stop')
                status_command  = os.popen('service apache2 status').readlines()
                if 'running' in str(status_command[2]):
                    self.apache_status.set_text('Active')
                elif 'dead' in str(status_command[2]):
                    self.apache_status.set_text('Inactive')
        except:
            os.popen('pkexec /opt/lampp/lampp stopapache')
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'Apache is not running' in str(status_command[1]):
                self.mysql_status.set_text('Inactive')
            elif 'Apache is running' in str(status_command[1]):
                self.apache_status.set_text('Active')


#restart apache button WORKING
    def on_button_a_restart_clicked(self, *args):
        try:
            if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:

                os.system('service apache2 restart')
                status_command = os.popen('service apache2 status').readlines()
                if 'running' in str(status_command[2]):
                    self.apache_status.set_text('Active')
                elif 'dead' in str(status_command[2]):
                    self.apache_status.set_text('Inactive')
        except:
            os.popen('pkexec /opt/lampp/lampp reloadapache')
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'Apache is not running' in str(status_command[1]):
                self.apache_status.set_text('Inactive')
            elif 'Apache is running' in str(status_command[1]):
                self.apache_status.set_text('Active')


########################################### MYSQSL BUTTONS ##################################################

#mysql start button WORKING
    def on_button_m_start_clicked(self, *args):

        try:
            if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                os.system('service mysql start')
                status_command  = os.popen('service mysql status').readlines()
                if 'dead' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
                elif 'running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
        except:
            os.popen('pkexec /opt/lampp/lampp startmysql')
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'MySQL is not running' in str(status_command[2]):
                self.mysql_status.set_text('Inactive')
            elif 'MySQL is running' in str(status_command[2]):
                self.mysql_status.set_text('Active')




#mysql stop button WORKING
    def on_button_m_stop_clicked(self, *args):
        try:
            if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                os.system('service mysql stop')
                status_command  = os.popen('service mysql status').readlines()

                if 'running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
                elif 'dead' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
        except:
            os.popen('pkexec /opt/lampp/lampp stopmysql')
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'MySQL is not running' in str(status_command[2]):
                self.mysql_status.set_text('Inactive')
            elif 'MySQL is running' in str(status_command[2]):
                self.mysql_status.set_text('Active')

            
#restart mysql button
    def on_button_m_restart_clicked(self, *args):
        try:
            if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                os.system('service mysql restart')
                status_command = os.popen('service mysql status').readlines()
                if 'running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
                elif 'dead' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
        except:
            os.popen('pkexec /opt/lampp/lampp reloadmysql')
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'MySQL is not running' in str(status_command[2]):
                self.mysql_status.set_text('Inactive')
            elif 'MySQL is running' in str(status_command[2]):
                self.mysql_status.set_text('Active')

########################################## ProFTPD BUTTON ################################################    

#start ProFTPD button
    def on_button_p_start_clicked(self, *args):

        os.popen('pkexec /opt/lampp/lampp startftp')
        status_command  = os.popen('pkexec /opt/lampp/lampp status').readlines()
        if 'ProFTPD is deactivated' in str(status_command[3]):
            self.proftp_status.set_text('Inactive')
        elif 'ProFTPD is running' in str(status_command[3]):
            self.proftp_status.set_text('Active')
    
#stop ProFTPD button    
    def on_button_p_stop_clicked(self, *args):

        os.popen('pkexec /opt/lampp/lampp stopftp')
        status_command  = os.popen('pkexec /opt/lampp/lampp status').readlines()
        if 'ProFTPD is deactivated' in str(status_command[3]):
            self.proftp_status.set_text('Inactive')
        elif 'ProFTPD is running' in str(status_command[3]):
            self.proftp_status.set_text('Active')

#restart ProFTPD button    
    def on_button_p_restart_clicked(self, *args):

        os.popen('pkexec /opt/lampp/lampp reloadftp && sudo /opt/lampp/lampp startftp')
        status_command  = os.popen('pkexec /opt/lampp/lampp status').readlines()
        if 'ProFTPD is deactivated' in str(status_command[3]):
            self.proftp_status.set_text('Inactive')
        elif 'ProFTPD is running' in str(status_command[3]):
            self.proftp_status.set_text('Active')

##########################################################################################################

#open directory button
    def on_open_directory_clicked(self, *args):
        try:
            os.system('nautilus /var/www/html')
        except:
            os.system('nemo /var/www/html')
        else:
            os.system('dolphin /var/www/html')

# open about
    def on_about_clicked(self, *args):
        os.popen('sensible-browser https://github.com/CleoMenezes/LAMPP-Manager/')


#start all button
    def on_button_start_all_clicked(self, *args):

        try:
            self.on_button_a_start_clicked()
            self.on_button_m_start_clicked()
            self.on_button_p_start_clicked()
        except:
            os.system('pkexec /opt/lampp/lampp start')


#stop all button
    def on_button_stop_all_clicked(self, *args):
        try:
            self.on_button_a_stop_clicked()
            self.on_button_m_stop_clicked()
            self.on_button_p_stop_clicked()
        except IndexError:
            os.system('pkexec /opt/lampp/lampp stop')


#restart all button
    def on_button_restart_all_clicked(self, *args):
        try:
            self.on_button_a_restart_clicked()
            self.on_button_m_restart_clicked()
            self.on_button_p_restart_clicked()
        except IndexError:
            os.system('sudo /opt/lampp/lampp reload; sudo /opt/lampp/lampp start')
            #apache
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'Apache is not running' in str(status_command[1]):
                self.apache_status.set_text('Inactive')
            elif 'Apache is running' in str(status_command[1]):
                self.apache_status.set_text('Active')
            #mysql
            status_command  = os.popen('opt/lampp/lampp status').readlines()
            if 'MySQL is not running' in str(status_command[2]):
                self.mysql_status.set_text('Inactive')
            elif 'MySQL is running' in str(status_command[2]):
                self.mysql_status.set_text('Active')
            #ftp
            status_command  = os.popen('pkexec /opt/lampp/lampp status').readlines()
            if 'ProFTPD is deactivated' in str(status_command[3]):
                self.proftp_status.set_text('Inactive')
            elif 'ProFTPD is running' in str(status_command[3]):
                self.proftp_status.set_text('Active')
        




###########################################################

# install lampp button
#     def on_install_lampp_clicked(self, *args):
#         install_script = '''sudo apt install apache2 -y &&
#                         sensible-browser localhost &&
#                         sudo apt install mariadb-server -y &&
#                         sudo apt install mariadb-client -y &&
#                         sudo apt install php7 php7-fpm php7-gd php7-curl php7-mysql libapache2-mod-php7 - y &&
#                         sudo service apache2 restart &&
#                         sudo a2enmod rewrite -y &&
#                         sudo sudo service apache2 restart &&
#                         sudo apt install php-imagick php-phpseclib php-gettext php7.*-imap php7.*-zip php7.*-xml php7.*-mbstring php7.*-bz2 php7.*-intl -y &&
#                         sudo service apache2 restart &&
#                         wget https://files.phpmyadmin.net/phpMyAdmin/4.9.7/phpMyAdmin-4.9.7-all-languages.zip -y &&
#                         sudo apt install unzip -y &&
#                         unzip phpMyAdmin-4.9.7-all-languages.zip -y &&
#                         sudo mv phpMyAdmin-4.9.7-all-languages /usr/share/phpmyadmin -y &&
#                         sudo chown -R www-data:www-data /usr/share/phpmyadmin -y &&
#                         sudo mkdir -p /var/lib/phpmyadmin/tmp -y &&
#                         sudo chown www-data:www-data /var/lib/phpmyadmin/tmp -y &&
#                         sudo service apache2 reload &&
#                         sensible-browser http://localhost/phpmyadmin'''
#         os.system('./install.sh')

builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()

if __name__ == '__main__':
    Gtk.main()


