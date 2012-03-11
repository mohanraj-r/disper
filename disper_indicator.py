"""
GUI wrapper (Gnome panel indicator) around disper, a utility to switch between multiple monitor configurations.

TODO:
    . combine extend_left and extend_right by passing a 'direction' param. Have to find out how to pass the extra param in add_menu_item
"""


import gobject
import gtk
import appindicator
import commands

def single_primary(w):
    commands.getstatusoutput('disper -s')

def single_secondary(w):
    commands.getstatusoutput('disper -S')

def extend_left(w):
    commands.getstatusoutput('disper -e -t left')

def extend_right(w):
    commands.getstatusoutput('disper -e -t right')

def clone(w):
    commands.getstatusoutput('disper -c')

def extend(w, direction="left"):
    commands.getstatusoutput('disper -e -t %s' % direction)

def quit(w):
    gtk.main_quit()

def add_menu_item(name, action):
    menu_item = gtk.MenuItem(name)
    menu.append(menu_item)
    menu_item.connect("activate", action)
    menu_item.show()

if __name__ == "__main__":
    ind = appindicator.Indicator ("disper-indicator",
                        	      "gsd-xrandr",
	                              appindicator.CATEGORY_HARDWARE)
    ind.set_status (appindicator.STATUS_ACTIVE)

    menu = gtk.Menu()

    add_menu_item('Primary display only', single_primary)
    add_menu_item('Secondary display only', single_secondary)
    add_menu_item('Secondary <- Primary', extend_left)
    add_menu_item('Primary -> Secondary', extend_right)
    add_menu_item('Clone', clone)
    add_menu_item('Quit', quit)

    ind.set_menu(menu)

    gtk.main()

