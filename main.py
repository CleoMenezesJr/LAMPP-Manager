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
        self.log_mysql = builder.get_object('log_mysql')
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
        if str(a_first_status) != 'Active' or str(a_first_status) != 'Inactive':
            try:
                try:
                    if status_command_a[0][0] == '●':
                        if 'dead' in str(status_command_a[2]):
                            self.apache_status.set_text('Inactive')
                        elif 'running' in str(status_command_a[2]):
                            self.apache_status.set_text('Active')
                        else:
                            self.apache_status.set_text('Cannot connect')
                    
                except:
                    if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                        status_command = os.popen('sudo /opt/lampp/lampp status').readlines()
                        if 'Apache is not running' in str(status_command[1]):
                            self.apache_status.set_text('Inactive')
                        elif 'Apache is running' in str(status_command[1]):
                            self.apache_status.set_text('Active')
                        else:
                            self.apache_status.set_text('Cannot connect')                    
                                
            except IndexError:
                self.apache_status.set_text('Not found')



#putting current status of mysql service
        


        status_command_m  = os.popen('service mysql status').readlines()
        m_first_status = self.mysql_status.get_label()
        if str(m_first_status) != 'Active' or str(m_first_status) != 'Inactive': 
            try:  
                try:               
                    if status_command_m[0][0] == '●':
                        if 'dead' in str(status_command_m[2]):
                            self.mysql_status.set_text('Inactive')
                        elif 'running' in str(status_command_m[2]):
                            self.mysql_status.set_text('Active')

                        
                except:
                    if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                        status_command_m1 = os.popen('sudo /opt/lampp/lampp status').readlines()
                        if 'MySQL is not running' in str(status_command_m1[2]):
                            self.mysql_status.set_text('Inactive')
                        elif 'Apache is running' in str(status_command_m1[2]):
                            self.mysql_status.set_text('Active')
                                
            except IndexError:
                self.mysql_status.set_text('Not found')


#putting current status of proftp service
        p_first_status = self.proftp_status.get_label()
        if str(p_first_status) != 'Active' or str(p_first_status) != 'Inactive':
            try:

                status_command = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
            except:
                self.proftp_status.set_text('Not found')

################################################################################

        

#quit button
    def on_main_window_destroy(self, *args):
        Gtk.main_quit()


################################### APACHE BUTTONS ##############################################

#apache start button WORKING
    def on_button_a_start_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:            
                    os.system('service apache2 start')
                    status_command = os.popen('service apache2 status').readlines()  
                    if 'dead' in str(status_command[2]):
                        self.apache_status.set_text('Inactive')
                    elif 'running' in str(status_command[2]):
                        self.apache_status.set_text('Active')
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp startapache')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'Apache is not running' in str(status_command[1]):
                        self.apache_status.set_text('Inactive')
                    elif 'Apache is running' in str(status_command[1]):
                        self.apache_status.set_text('Active')
        except:
            self.apache_status.set_text('Cannot connect')


#apache stop button WORKING
    def on_button_a_stop_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:
                    os.system('service apache2 stop')
                    status_command  = os.popen('service apache2 status').readlines()
                    if 'running' in str(status_command[2]):
                        self.apache_status.set_text('Active')
                    elif 'dead' in str(status_command[2]):
                        self.apache_status.set_text('Inactive')
                    else:
                        self.apache_status.set_text('Cannot connect')
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp stopapache')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'Apache is not running' in str(status_command[1]):
                        self.mysql_status.set_text('Inactive')
                    elif 'Apache is running' in str(status_command[1]):
                        self.apache_status.set_text('Active')
        except:
            self.apache_status.set_text('Cannot connect')


#restart apache button WORKING
    def on_button_a_restart_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:

                    os.system('service apache2 restart')
                    status_command = os.popen('service apache2 status').readlines()
                    if 'running' in str(status_command[2]):
                        self.apache_status.set_text('Active')
                    elif 'dead' in str(status_command[2]):
                        self.apache_status.set_text('Inactive')
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp reloadapache')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'Apache is not running' in str(status_command[1]):
                        self.apache_status.set_text('Inactive')
                    elif 'Apache is running' in str(status_command[1]):
                        self.apache_status.set_text('Active')
        except:
            self.apache_status.set_text('Cannot connect')


########################################### MYSQSL BUTTONS ##################################################

#mysql start button WORKING
    def on_button_m_start_clicked(self, *args):
        try:

            try:
                if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                    os.system('service mysql start')
                    status_command  = os.popen('service mysql status').readlines()
                    if 'dead' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                    elif 'running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp startmysql')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'MySQL is not running' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                    elif 'MySQL is running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
        except:
            self.mysql_status.set_text('Cannot connect')


#mysql stop button WORKING
    def on_button_m_stop_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                    os.system('service mysql stop')
                    status_command  = os.popen('service mysql status').readlines()

                    if 'running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
                    elif 'dead' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                    else:
                        self.mysql_status.set_text('Cannot connect')
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp stopmysql')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'MySQL is not running' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                    elif 'MySQL is running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
        except:
            self.mysql_status.set_text('Cannot connect')

            
#restart mysql button
    def on_button_m_restart_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                    os.system('service mysql restart')
                    status_command = os.popen('service mysql status').readlines()
                    if 'running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
                    elif 'dead' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')

            except:
                os.popen('sudo /opt/lampp/lampp reloadmysql')
                status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'MySQL is not running' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
                elif 'MySQL is running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
        except:
            self.mysql_status.set_text('Cannot connect')

########################################## ProFTPD BUTTON ################################################    

#start ProFTPD button
    def on_button_p_start_clicked(self, *args):
        try:
            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                os.popen('sudo /opt/lampp/lampp startftp')
                status_command = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
        except:
            self.proftp_status.set_text('Cannot connect')
    
#stop ProFTPD button    
    def on_button_p_stop_clicked(self, *args):
        try:
            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                os.popen('sudo /opt/lampp/lampp stopftp')
                status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
        except:
            self.proftp_status.set_text('Cannot connect')

#restart ProFTPD button    
    def on_button_p_restart_clicked(self, *args):
        try:
            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                os.popen('sudo /opt/lampp/lampp reloadftp')
                os.popen('sudo /opt/lampp/lampp startftp')
                status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
        except:
            self.proftp_status.set_text('Cannot connect')

##########################################################################################################

#open directory button
    def on_open_directory_clicked(self, *args):
        try:
            os.popen('nautilus /var/www/html')
        except:
            os.popen('nemo /var/www/html')
        else:
            os.popen('dolphin /var/www/html')

#Open directory logs apache 
    def on_log_mysql_clicked(self,*args):
        try:
            os.popen('nautilus /var/log/mysql')
        except:
            os.popen('nemo /var/log/mysql')
        else:
            os.popen('dolphin /var/log/mysql')

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
            os.system('sudo /opt/lampp/lampp start')


#stop all button
    def on_button_stop_all_clicked(self, *args):
        try:
            self.on_button_a_stop_clicked()
            self.on_button_m_stop_clicked()
            self.on_button_p_stop_clicked()
        except IndexError:
            os.system('sudo /opt/lampp/lampp stop')


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
            status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
            if 'ProFTPD is deactivated' in str(status_command[3]):
                self.proftp_status.set_text('Inactive')
            elif 'ProFTPD is running' in str(status_command[3]):
                self.proftp_status.set_text('Active')
        

###########################################################

# install lampp button
    def on_install_lampp_clicked(self, *args):
        os.system('sudo ./install.sh')
#########################################################

builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()

if __name__ == '__main__':
    Gtk.main()
