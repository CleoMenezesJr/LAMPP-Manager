#!/usr/bin/python
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("customtray", "/home/cleomenezesjr/CODE/LAMPP Manager/Media/bitmap.png", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  command_one = gtk.MenuItem('Open Lampp Manager')
  command_one.connect('activate', note)
  menu.append(command_one)

  exittray = gtk.MenuItem('Exit')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def note(_):
  os.system("python3 main.py")

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()