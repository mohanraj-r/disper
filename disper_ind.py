import gobject
import gtk
import appindicator
import commands

def single(w):
    commands.getstatusoutput('disper -s')

def extend(w):
    commands.getstatusoutput('disper -e')

def clone(w):
    commands.getstatusoutput('disper -c')

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

  add_menu_item('Single', single)
  add_menu_item('Extend', extend)
  add_menu_item('Clone', clone)

  ind.set_menu(menu)

  gtk.main()
