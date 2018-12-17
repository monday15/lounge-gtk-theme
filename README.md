## NEWS
Lounge-aux icons merged into this repo, read updated installation instructions.

## Installation
Lounge theme supports gnome 3.28+ (gtk3 3.22+).  
Requirements: `meson` (0.40+), `sassc` packages. Lounge-night theme also requires `gtk-murrine-engine` (`gtk2-engines-murrine` for debian/ubuntu).  

1. Download source tarball (or clone repository);
2. Build theme:  
`meson build -Dshell-font='Liberation Sans' -Dicon-theme='Suru'`  
   > Shell-font option sets a font that will be used by gnome-shell theme (default is Roboto, used if option is unset);  
Icon-theme option sets main icon theme for Lounge-aux icons - auxiliary set of symbolic icons, look at screenshots to see the difference (default is Adwaita, will be used if option is unset).

3. Install theme:  
`sudo ninja -C build install`

Fedora users can install theme via copr:  
`sudo dnf copr enable monday15/lounge`  
`sudo dnf install lounge-gtk-theme`

> Fedora users will get Lounge-aux as a weak dependency with Adwaita as a main icon theme, for other icon themes - build theme with custom icon-theme option.

## Updating
Use regular installation instructions, old files will be overwritten with a new ones.

## Extra
Firefox looks ok with the theme, but there are some tweaks, you can find them in `firefox-tweak` folder (or `firefox-tweak-dark` for dark theme). Copy `userChrome.css` to your profile's `chrome` dir - the path looks like this `~/.mozilla/firefox/randomletters.default/chrome/userChrome.css`.

![firefoxdiff](/screenshots/firefoxdiff.png?raw=true)

## Removing
Remove installation folders `/usr/share/themes/Lounge`, `/usr/share/themes/Lounge-night`, `/usr/share/icons/Lounge-aux`.


## Licence
GPLv3+, see LICENSE file.  
Lounge-gtk-theme based on original gtk theme Adwaita.  
Original themes/styles copyrights are in COPYRIGHT file.

## Bugs
Report bugs to [issues page](https://github.com/monday15/lounge-gtk-theme/issues).

## Thanks
Allan Day, Emmanuele Bassi, horst3180, nana-4, Sam Hewitt, Thibault Saunier, tista500, vinceliuice, ZMA, all people in copyright file, Meson developers, Yaru theme developers, Gnome developers and maintainers, Fedora developers and maintainers.

## Links
[Absolute gtk2 theme](https://www.gnome-look.org/p/1080258/), [Adapta theme](https://github.com/adapta-project/adapta-gtk-theme), [Adwaita gtk2 theme](https://gitlab.gnome.org/GNOME/gnome-themes-extra), [Adwaita gtk3 theme](https://gitlab.gnome.org/GNOME/gtk), [gnome-shell theme](https://gitlab.gnome.org/GNOME/gnome-shell), [Materia theme](https://github.com/nana-4/materia-theme), [Yaru theme](https://github.com/ubuntu/yaru).  
List of applications (their original css styles used in the theme): [Gedit](https://gitlab.gnome.org/GNOME/gedit), [Nautilus](https://gitlab.gnome.org/GNOME/nautilus).

## Screenshots
![auxdiff](/screenshots/auxdiff.png?raw=true)
---
![sh1](/screenshots/sh1.png?raw=true)
