#!pyobjects
# -*- coding: utf-8 -*-
# vim: set syntax=python ts=4 sw=4 sts=4 et :

class ThemeMap(Map):
    class Debian:
        xdg_qubes_settings = '/etc/X11/Xsession.d/25xdg-qubes-settings'
        theme_dependencies = [ 'gnome-tweak-tool', 
                               'dconf-editor', 
                               'xdg-user-dirs', 
                               'gnome-themes-standard', 
                               'xsettingsd' ]
    class Ubuntu:
        __grain__ = 'os'
        xdg_qubes_settings = '/etc/X11/Xsession.d/25xdg-qubes-settings'
        theme_dependencies = [ 'gnome-tweak-tool ', 
                               'dconf-editor', 
                               'xdg-user-dirs', 
                               'gnome-themes-standard', 
                               'xsettingsd' ]

    class RedHat:
        xdg_qubes_settings = '/etc/X11/xinit/Xclients.d/25xdg-qubes-settings'
        theme_rpmfusion_dependencies = [ 'freetype-freeworld' ]
        theme_dependencies = [ 'ttmkfdir', 
                               'gnome-tweak-tool', 
                               'dconf-editor', 
                               'xdg-user-dirs', 
                               'gnome-themes-standard', 
                               'xsettingsd' ]
