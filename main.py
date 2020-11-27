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
        self.apache_port = builder.get_object('apache_port')
        self.mysql_port = builder.get_object('mysql_port')
        self.apache_img_status = builder.get_object('apache_img_status')
        self.mysql_img_status = builder.get_object('mysql_img_status')
        self.ftp_img_status = builder.get_object('ftp_img_status')



###########################################################################

#putting current apache's port
        try:
            status_command_a  = os.popen('service apache2 status').readlines()
            if status_command_a[0][0] == '●':
                apache_port_file = open('/etc/apache2/ports.conf', 'r')
                text_file = apache_port_file.readlines()
                #b_port_status = self.apache_port.get_label()
                self.apache_port.set_text(str(text_file[4].replace('Listen', '').strip()))
                print('gostosinha')
        except:
            pass
            

#putting current mysqls port
        try:
            status_command_m  = os.popen('service mysql status').readlines()
            if status_command_a[0][0] == '●':
                mysql_port_file = open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'r')
                text_file = mysql_port_file.readlines()
                self.mysql_port.set_text(text_file[18].replace('#port', '').strip().replace('= ', ''))
        except:
            pass




#putting current status of apacher service WORKING
        status_command_a  = os.popen('service apache2 status').readlines()
        a_first_status = self.apache_status.get_label()
        if str(a_first_status) != 'Active' or str(a_first_status) != 'Inactive':
            try:
                try:
                    if status_command_a[0][0] == '●':
                        if 'dead' in str(status_command_a[2]):
                            self.apache_status.set_text('Inactive')
                            self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                        elif 'running' in str(status_command_a[2]):
                            self.apache_status.set_text('Active')
                            self.apache_img_status.set_from_icon_name('emblem-default', 1)
                        else:
                            self.apache_status.set_text('Cannot connect')
                            self.apache_img_status.set_from_icon_name('emblem-important', 1)
                            
                    
                except:
                    if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                        status_command = os.popen('sudo /opt/lampp/lampp status').readlines()
                        if 'Apache is not running' in str(status_command[1]):
                            self.apache_status.set_text('Inactive')
                            self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                        elif 'Apache is running' in str(status_command[1]):
                            self.apache_status.set_text('Active')
                            self.apache_img_status.set_from_icon_name('emblem-default', 1)                            
                        else:
                            self.apache_status.set_text('Cannot connect')
                            self.apache_img_status.set_from_icon_name('emblem-important', 1)                    
                                
            except IndexError:
                self.apache_status.set_text('Not found')
                self.apache_img_status.set_from_icon_name('emblem-important', 1)



#putting current status of mysql service
        


        status_command_m  = os.popen('service mysql status').readlines()
        m_first_status = self.mysql_status.get_label()
        if str(m_first_status) != 'Active' or str(m_first_status) != 'Inactive': 
            try:  
                try:               
                    if status_command_m[0][0] == '●':
                        if 'dead' in str(status_command_m[2]):
                            self.mysql_status.set_text('Inactive')
                            self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)

                        elif 'running' in str(status_command_m[2]):
                            self.mysql_status.set_text('Active')
                            self.mysql_img_status.set_from_icon_name('emblem-default', 1)

                        
                except:
                    if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                        status_command_m1 = os.popen('sudo /opt/lampp/lampp status').readlines()
                        if 'MySQL is not running' in str(status_command_m1[2]):
                            self.mysql_status.set_text('Inactive')
                            self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                        elif 'Apache is running' in str(status_command_m1[2]):
                            self.mysql_status.set_text('Active')
                            self.mysql_img_status.set_from_icon_name('emblem-default', 1)
                                
            except IndexError:
                self.mysql_status.set_text('Not found')
                self.mysql_img_status.set_from_icon_name('emblem-important', 1)


#putting current status of proftp service
        p_first_status = self.proftp_status.get_label()
        if str(p_first_status) != 'Active' or str(p_first_status) != 'Inactive':
            try:

                status_command = os.popen('pkexec /opt/lampp/lampp status').readlines()
                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                    self.ftp_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
                    self.ftp_img_status.set_from_icon_name('emblem-default', 1)
            except:
                self.proftp_status.set_text('Not found')
                self.ftp_img_status.set_from_icon_name('emblem-important', 1)

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
                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                    elif 'running' in str(status_command[2]):
                        self.apache_status.set_text('Active')
                        self.apache_img_status.set_from_icon_name('emblem-default', 1)
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp startapache')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'Apache is not running' in str(status_command[1]):
                        self.apache_status.set_text('Inactive')
                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                    elif 'Apache is running' in str(status_command[1]):
                        self.apache_status.set_text('Active')
                        self.apache_img_status.set_from_icon_name('emblem-default', 1)
                        
        except:
            self.apache_status.set_text('Cannot connect')
            self.apache_img_status.set_from_icon_name('emblem-important', 1)


#apache stop button WORKING
    def on_button_a_stop_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:
                    os.system('service apache2 stop')
                    status_command  = os.popen('service apache2 status').readlines()
                    if 'running' in str(status_command[2]):
                        self.apache_status.set_text('Active')
                        self.apache_img_status.set_from_icon_name('emblem-default', 1)
                    elif 'dead' in str(status_command[2]):
                        self.apache_status.set_text('Inactive')
                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                    else:
                        self.apache_status.set_text('Cannot connect')
                        self.apache_img_status.set_from_icon_name('emblem-important', 1)
                        
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp stopapache')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'Apache is not running' in str(status_command[1]):
                        self.mysql_status.set_text('Inactive')
                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                    elif 'Apache is running' in str(status_command[1]):
                        self.apache_status.set_text('Active')
                        self.apache_img_status.set_from_icon_name('emblem-default', 1)
        except:
            self.apache_status.set_text('Cannot connect')
            self.apache_img_status.set_from_icon_name('emblem-important', 1)


#restart apache button WORKING
    def on_button_a_restart_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service apache2 status').readlines()[0]:

                    os.system('service apache2 restart')
                    status_command = os.popen('service apache2 status').readlines()
                    if 'running' in str(status_command[2]):
                        self.apache_status.set_text('Active')
                        self.apache_img_status.set_from_icon_name('emblem-default', 1)
                    elif 'dead' in str(status_command[2]):
                        self.apache_status.set_text('Inactive')
                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp reloadapache')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'Apache is not running' in str(status_command[1]):
                        self.apache_status.set_text('Inactive')
                        self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                    elif 'Apache is running' in str(status_command[1]):
                        self.apache_status.set_text('Active')
                        self.apache_img_status.set_from_icon_name('emblem-default', 1)
        except:
            self.apache_status.set_text('Cannot connect')
            self.apache_img_status.set_from_icon_name('emblem-important', 1)


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
                        self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                    elif 'running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
                        self.mysql_img_status.set_from_icon_name('emblem-default', 1)
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp startmysql')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'MySQL is not running' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                        self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                    elif 'MySQL is running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
                        self.mysql_img_status.set_from_icon_name('emblem-default', 1)
        except:
            self.mysql_status.set_text('Cannot connect')
            self.mysql_img_status.set_from_icon_name('emblem-important', 1)


#mysql stop button WORKING
    def on_button_m_stop_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                    os.system('service mysql stop')
                    status_command  = os.popen('service mysql status').readlines()

                    if 'running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
                        self.mysql_img_status.set_from_icon_name('emblem-default', 1)
                    elif 'dead' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                        self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                    else:
                        self.mysql_status.set_text('Cannot connect')
            except:
                if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                    os.popen('sudo /opt/lampp/lampp stopmysql')
                    status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                    if 'MySQL is not running' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                        self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                    elif 'MySQL is running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
                        self.mysql_img_status.set_from_icon_name('emblem-default', 1)
        except:
            self.mysql_status.set_text('Cannot connect')
            self.mysql_img_status.set_from_icon_name('emblem-important', 1)

            
#restart mysql button
    def on_button_m_restart_clicked(self, *args):
        try:
            try:
                if 'Cannot run program' not in os.popen('service mysql status').readlines()[0]:
                    os.system('service mysql restart')
                    status_command = os.popen('service mysql status').readlines()
                    if 'running' in str(status_command[2]):
                        self.mysql_status.set_text('Active')
                        self.mysql_img_status.set_from_icon_name('emblem-default', 1)
                    elif 'dead' in str(status_command[2]):
                        self.mysql_status.set_text('Inactive')
                        self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)

            except:
                os.popen('sudo /opt/lampp/lampp reloadmysql')
                status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'MySQL is not running' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
                    self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'MySQL is running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
                    self.mysql_img_status.set_from_icon_name('emblem-default', 1)
        except:
            self.mysql_status.set_text('Cannot connect')
            self.mysql_img_status.set_from_icon_name('emblem-important', 1)


########################################## ProFTPD BUTTON ################################################    

#start ProFTPD button
    def on_button_p_start_clicked(self, *args):
        try:
            try:
                if 'sudo' not in os.popen('sudo systemctl status proftpd').readlines()[0]:
                    os.system('')
                

            except:
                    if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                        os.popen('sudo /opt/lampp/lampp startftp')
                        status_command = os.popen('sudo /opt/lampp/lampp status').readlines()
                        if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                            self.proftp_status.set_text('Inactive')
                            self.ftp_img_status.set_from_icon_name('emblem-unreadable', 1)
                        elif 'ProFTPD is running' in str(status_command[3]):
                            self.proftp_status.set_text('Active')
                            self.ftp_img_status.set_from_icon_name('emblem-default', 1)

        except:
            self.proftp_status.set_text('Cannot connect')
            self.ftp_img_status.set_from_icon_name('emblem-important', 1)
    
#stop ProFTPD button    
    def on_button_p_stop_clicked(self, *args):
        try:
            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                os.popen('sudo /opt/lampp/lampp stopftp')
                status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                    self.ftp_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
                    self.ftp_img_status.set_from_icon_name('emblem-default', 1)
        except:
            self.proftp_status.set_text('Cannot connect')
            self.ftp_img_status.set_from_icon_name('emblem-important', 1)

#restart ProFTPD button    
    def on_button_p_restart_clicked(self, *args):
        try:
            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                os.popen('sudo /opt/lampp/lampp reloadftp')
                os.popen('sudo /opt/lampp/lampp startftp')
                status_command  = os.popen('sudo /opt/lampp/lampp status').readlines()
                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                    self.ftp_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
                    self.ftp_img_status.set_from_icon_name('emblem-default', 1)
        except:
            self.proftp_status.set_text('Cannot connect')
            self.ftp_img_status.set_from_icon_name('emblem-important', 1)

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

            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                os.system('sudo /opt/lampp/lampp start')

                status_command = os.popen('sudo /opt/lampp/lampp status').readlines()

                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                    self.ftp_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
                    self.ftp_img_status.set_from_icon_name('emblem-default', 1)
                
                if 'Apache is not running' in str(status_command[1]):
                    self.apache_status.set_text('Inactive')
                    self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'Apache is running' in str(status_command[1]):
                    self.apache_status.set_text('Active')
                    self.apache_img_status.set_from_icon_name('emblem-default', 1)

                if 'MySQL is not running' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
                    self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'MySQL is running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
                    self.mysql_img_status.set_from_icon_name('emblem-default', 1)


#stop all button
    def on_button_stop_all_clicked(self, *args):
        try:
            self.on_button_a_stop_clicked()
            self.on_button_m_stop_clicked()
            self.on_button_p_stop_clicked()
        except IndexError:
            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                os.system('sudo /opt/lampp/lampp stop')
                status_command = os.popen('sudo /opt/lampp/lampp status').readlines()

                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                    self.ftp_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
                    self.ftp_img_status.set_from_icon_name('emblem-default', 1)
                
                if 'Apache is not running' in str(status_command[1]):
                    self.apache_status.set_text('Inactive')
                    self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'Apache is running' in str(status_command[1]):
                    self.apache_status.set_text('Active')
                    self.apache_img_status.set_from_icon_name('emblem-default', 1)

                if 'MySQL is not running' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
                    self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'MySQL is running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
                    self.mysql_img_status.set_from_icon_name('emblem-default', 1)


#restart all button
    def on_button_restart_all_clicked(self, *args):
        try:
            self.on_button_a_restart_clicked()
            self.on_button_m_restart_clicked()
            self.on_button_p_restart_clicked()
        except IndexError:
            os.system('sudo /opt/lampp/lampp reload; sudo /opt/lampp/lampp start')
            if 'sudo' not in os.popen('sudo /opt/lampp/lampp status').readlines()[0]:
                status_command = os.popen('sudo /opt/lampp/lampp status').readlines()

                if 'ProFTPD is deactivated' in str(status_command[3]) or 'ProFTPD is not running' in str(status_command[3]):
                    self.proftp_status.set_text('Inactive')
                    self.ftp_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'ProFTPD is running' in str(status_command[3]):
                    self.proftp_status.set_text('Active')
                    self.ftp_img_status.set_from_icon_name('emblem-default', 1)
                
                if 'Apache is not running' in str(status_command[1]):
                    self.apache_status.set_text('Inactive')
                    self.apache_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'Apache is running' in str(status_command[1]):
                    self.apache_status.set_text('Active')
                    self.apache_img_status.set_from_icon_name('emblem-default', 1)

                if 'MySQL is not running' in str(status_command[2]):
                    self.mysql_status.set_text('Inactive')
                    self.mysql_img_status.set_from_icon_name('emblem-unreadable', 1)
                elif 'MySQL is running' in str(status_command[2]):
                    self.mysql_status.set_text('Active')
                    self.mysql_img_status.set_from_icon_name('emblem-default', 1)
###########################################################

# install lampp button
    def on_install_lampp_clicked(self, *args):
        os.popen('cd install; ./Installer')
#########################################################

builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()

if __name__ == '__main__':
    Gtk.main()
