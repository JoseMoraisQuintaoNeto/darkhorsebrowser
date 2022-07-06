#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from gi.repository import Gtk, WebKit
 
 
class Browser(object):
    def __init__(self):
 
        builder = Gtk.Builder()
        builder.add_from_file("browser.glade")
        self.window = builder.get_object("window")
        self.window.show()
        self.go_back_button = builder.get_object("go_back")
        self.go_forward_button = builder.get_object("go_forward")
        self.refresh_button = builder.get_object("refresh")
        self.scrolledwindow = builder.get_object("scrolledwindow")
        self.url = builder.get_object("entry")
        self.search_entry = builder.get_object("search_entry")
 
        self.view = WebKit.WebView()
        self.scrolledwindow.add(self.view)
 
        self.view.open("https://duckduckgo.com/")
        self.view.show()
         
        self.view.connect("load-committed", self.check_buttons) 
        self.view.connect("title-changed", self.change_title)
         
        builder.connect_signals({
                                "gtk_main_quit": Gtk.main_quit,
                                "on_entry_activate": self.go_,
                                "on_search_activate": self.search,
                                "go_back_clicked": self.go_back,
                                "go_forward_clicked": self.go_forward,
                                "refresh_clicked": self.refresh,
                                })
                                 
    def go_(self, widget):
        """Load the page in address bar"""
        link = self.url.get_text()
        if link.startswith("https://"):
            self.view.open(link)
        else:
            self.view.open("https://" + link)
        self.view.show()
         
    def search(self, widget):
        """ Pesquisa no google o conteúdo contido
            na barra de pesquisa"""
        text = self.search_entry.get_text()
        text = text.replace(" ", "+")
        self.url.set_text("https://duckduckgo.com/?q=" + text)
        self.search_entry.set_text("")
        self.go_(self)
 
             
    def check_buttons(self, widget, data):
        """Checks if the back and forward buttons are available,
            if true, the buttons can be used if
            otherwise the buttons are disabled.
            Also updates the address bar with the page
            currently loaded."""
        uri = widget.get_main_frame().get_uri()
        self.url.set_text(uri)
        self.go_back_button.set_sensitive(self.view.can_go_back())
        self.go_forward_button.set_sensitive(self.view.can_go_forward())
         
         
    def change_title(self, widget, data, arg):
        """ Change browser title to search text """
        title = widget.get_main_frame().get_title()
        self.window.set_title("DarkHorse Browser - %s" % title)
         
         
    def go_back(self, widget):
        """Back"""
        self.view.go_back()
         
         
    def go_forward(self, widget):
        """Advance"""
        self.view.go_forward()
         
         
    def refresh(self, widget):
        """Reload"""
        self.view.reload()
         
if __name__ == "__main__":
    browser = Browser()
    Gtk.main()