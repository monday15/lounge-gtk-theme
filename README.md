## IMPORTANT NOTE
For best experience, use Lounge theme with [Lounge-aux](https://github.com/monday15/lounge-aux) icons - it is a set of symbolic icons (window controls and arrows), other icons will be taken from default icon theme or one that you are using. Installation is simple, proceed to [Lounge-aux repository](https://github.com/monday15/lounge-aux).

![auxdiff](/screenshots/auxdiff.png?raw=true)

> Fedora users will get Lounge-aux as a weak dependency with Adwaita as a main icon theme, for other icon themes, they should also check the link.

## Installation
Lounge theme supports gnome 3.28+ (gtk3 3.22+).  
Requirements: `meson`, `sassc` packages. Lounge-night theme also requires `gtk-murrine-engine` (`gtk2-engines-murrine` for debian/ubuntu).  

Download source tarball (or clone repository), run from source dir:  
`meson build`  
`sudo ninja -C build install`

Fedora users can install theme via copr:  
`sudo dnf copr enable monday15/lounge`  
`sudo dnf install lounge-gtk-theme`

## Updating
Use regular installation instructions, old files will be overwritten with a new ones.

## Extra
Firefox looks ok with the theme, but there are some tweaks, you can find them in `firefox-tweak` folder (or `firefox-tweak-dark` for dark theme). Copy `userChrome.css` to your profile's `chrome` dir - the path looks like this `~/.mozilla/firefox/randomletters.default/chrome/userChrome.css`.

![firefoxdiff](/screenshots/firefoxdiff.png?raw=true)

## Removing
Remove installation folders `/usr/share/themes/Lounge`, `/usr/share/themes/Lounge-night`.


## Licence
GPLv3+, see LICENSE file.  
Lounge-gtk-theme based on original gtk theme Adwaita.  
Original themes/styles copyrights are in COPYRIGHT file.

## Bugs
Report bugs to [issues page](https://github.com/monday15/lounge-gtk-theme/issues).

## Thanks
horst3180, Emmanuele Bassi, nana-4, Sam Hewitt, Thibault Saunier, ZMA, all people in copyright file, Meson developers, Yaru theme developers, Adapta theme developers, Gnome developers and maintainers, Fedora developers and maintainers.

## Links
[Absolute gtk2 theme](https://www.gnome-look.org/p/1080258/), [Adapta theme](https://github.com/adapta-project/adapta-gtk-theme), [Adwaita gtk2 theme](https://gitlab.gnome.org/GNOME/gnome-themes-extra), [Adwaita gtk3 theme](https://gitlab.gnome.org/GNOME/gtk), [gnome-shell theme](https://gitlab.gnome.org/GNOME/gnome-shell), [Materia theme](https://github.com/nana-4/materia-theme), [Yaru theme](https://github.com/ubuntu/yaru).  
List of applications (their original css styles used in the theme): [Gedit](https://gitlab.gnome.org/GNOME/gedit), [Nautilus](https://gitlab.gnome.org/GNOME/nautilus).

## Screenshot
![sh1](/screenshots/sh1.png?raw=true)
