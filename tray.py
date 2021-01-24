#!/usr/bin/env python3
import signal
import gi
import os
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

class Indicator():
    def __init__(self):
        self.app = 'Lampp Manager'
        iconpath = "/home/cleomenezesjr/CODE/LAMPP Manager/Media/bitmap.png"
        self.indicator = AppIndicator3.Indicator.new(
            self.app, iconpath,
            AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)       
        self.indicator.set_menu(self.create_menu())

    def create_menu(self):
        menu = Gtk.Menu()
        # menu item 1
        openLM = Gtk.MenuItem('Open Lamp Manager')
        openLM.connect('activate', self.openLM)
        menu.append(openLM)
        # separator
        # menu_sep = Gtk.SeparatorMenuItem()
        # menu.append(menu_sep)
        # quit
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def openLM(self, source):
      os.popen('pkill -f main.py; exit')
      os.popen('python3 main.py; exit')

    def stop(self, source):
      os.popen('pkill -f main.py')
      Gtk.main_quit()

Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()