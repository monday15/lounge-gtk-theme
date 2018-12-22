## Info
Lounge is a simple and clean theme, based on original gtk theme Adwaita, made for gnome 3.28+ (gtk3 3.22+).  
Lounge theme also provides Lounge-aux icon theme - auxiliary set of symbolic icons for better user experience.  
 
## Installation
Requirements:  
`meson` (0.40+)  
`sassc`  
`gtk-murrine-engine` (`gtk2-engines-murrine` for debian/ubuntu).
> `gtk-murrine-engine` only needed for Lounge-night gtk2 theme.

- Download and decompress source tarball (or clone repository);
- Build theme:  
`meson build` 
 
  Additional options are availiable, to use them add `-D` before option name and set value after `-Doption='value'`, quotes needed only if value has multiple words separated by space. For example,  
`meson build -Dshell-font='Liberation Sans' -Dicon-theme=Suru`  
builds gnome-shell theme with Liberation Sans font and Lounge-aux icon theme that will inherit icons from Suru icon theme.

  Option | Description
  --- | ---
  icon-theme | Specify main icon theme for Lounge-aux (default: Adwaita)
  icons |Enable/disable Lounge-aux, can be true or false (default: true)
  shell-font | Specify font for gnome-shell theme (default: Roboto)

- Install theme:  
`sudo ninja -C build install`


Fedora users can install theme via copr:  
`sudo dnf copr enable monday15/lounge`  
`sudo dnf install lounge-gtk-theme`

> Fedora users will get Lounge-aux as a weak dependency with Adwaita as a main icon theme, for other icon themes - build theme with custom icon-theme option.

## Updating
Use regular installation instructions, old files will be overwritten with a new ones.

## Extra
Firefox looks decent with Lounge theme, but there are some tweaks, you can find them in `firefox-tweak` folder (or `firefox-tweak-dark` for dark theme). Copy `userChrome.css` to your profile's `chrome` dir - the path looks like this `~/.mozilla/firefox/randomletters.default/chrome/userChrome.css`.


## Removing
Remove installation folders:  
`/usr/share/themes/Lounge`  
`/usr/share/themes/Lounge-night`  
`/usr/share/icons/Lounge-aux`


## Licence
GPLv3+, see LICENSE file.    
Original themes/styles copyrights are in COPYRIGHT file.

## Bugs
Report bugs to [issues page](https://github.com/monday15/lounge-gtk-theme/issues).

## Thanks
Allan Day, Emmanuele Bassi, horst3180, nana-4, Sam Hewitt, Thibault Saunier, tista500, vinceliuice, ZMA, all people in copyright file, Meson developers, Yaru theme developers, Gnome developers and maintainers, Fedora developers and maintainers.

## Links
[Absolute gtk2 theme](https://www.gnome-look.org/p/1080258/), [Adapta theme](https://github.com/adapta-project/adapta-gtk-theme), [Adwaita gtk2 theme](https://gitlab.gnome.org/GNOME/gnome-themes-extra), [Adwaita gtk3 theme](https://gitlab.gnome.org/GNOME/gtk), [gnome-shell theme](https://gitlab.gnome.org/GNOME/gnome-shell), [Materia theme](https://github.com/nana-4/materia-theme), [Yaru theme](https://github.com/ubuntu/yaru).  
List of applications (their original css styles used in the theme): [Gedit](https://gitlab.gnome.org/GNOME/gedit), [Nautilus](https://gitlab.gnome.org/GNOME/nautilus).

## Screenshots
![auxdiff](https://user-images.githubusercontent.com/42862490/50310672-82702700-04c4-11e9-9e3c-e806dcc942eb.png)  

![firefoxdiff](https://user-images.githubusercontent.com/42862490/50310681-88660800-04c4-11e9-8244-189c4020319f.png)

![sh1](https://user-images.githubusercontent.com/42862490/50310682-8a2fcb80-04c4-11e9-863e-331b666ba68c.png)
