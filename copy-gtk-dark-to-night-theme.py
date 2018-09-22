#!/usr/bin/env python3

from os import environ, path
from subprocess import call

if not environ.get('DESTDIR', ''):
    PREFIX = environ.get('MESON_INSTALL_PREFIX', '/usr')
    print('Copying gtk3 night theme...')
    call(['cp', path.join(PREFIX, 'share/themes/Lounge/gtk-3.0/gtk-dark.css'), path.join(PREFIX, 'share/themes/Lounge-night/gtk-3.0/gtk.css')])
