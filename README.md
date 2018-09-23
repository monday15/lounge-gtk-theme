## Info
Lounge-gtk-theme based on original gtk theme Adwaita.

## IMPORTANT NOTE
This theme is meant to be used with Lounge-aux icons. It is not a "complete" icon theme - it has 10 icons (only symbolic), but they are VITAL for providing correct user expirience. Installation is simple and easy, check out https://github.com/monday15/lounge-aux before procceding with installation.
> Fedora users will get Lounge-aux as a weak dependency with Adwaita as a main icon theme, for other icon themes, they should also check the link. 

## Installation
From version 1.0 meson builds theme based on gtk3 version.  
You need 'meson' and 'sassc' packages to build and install the theme. For Lounge-night gtk2 theme (dark variant), you also need 'gtk-murrine-engine'. Download release, run following commands from project directory:  
`meson build`  
`sudo ninja -C build install`

You can also download already builded theme (download build-* from releases page, 3.28 tested on gnome 3.28, but should also work on any gnome 3.22+, 3.30 is for gtk3.24/gnome 3.30), and simply copy **Lounge** and **Lounge-night** folders from archive to **/usr/share/themes**.

Fedora users can install theme via copr:  
`sudo dnf copr enable monday15/lounge`  
`sudo dnf install lounge-gtk-theme`

## Extra
Firefox looks decent with the theme, but there are some tweaks, you can find them in `firefox-tweak` folder (or `firefox-tweak-dark` for dark theme). Just copy `userChrome.css` to your profile - the path looks like this `~/.mozilla/firefox/randomletters.default/chrome/userChrome.css`.

## Removing
Run from project directory:  
`sudo ninja -C build uninstall`  
or simply remove installation folders `/usr/share/themes/Lounge`, `/usr/share/themes/Lounge-night`.

## Licence
GPLv3+, see LICENSE file.  
Original themes/styles copyrights are in COPYRIGHT file.

## Bugs
Report bugs in issues tab.

## Thanks
All people in #gnome-hackers chanell on gnome irc,  
horst3180,  
Emmanuele Bassi,  
Sam Hewitt,  
ZMA from gnome-look.org,  
All people in a copyright file,  
Meson developers,  
Yaru gtk theme developers,  
Adapta theme developers,  
Gnome developers and maintainers,  
Fedora developers and maintainers.

## Links
+ [Absolute gtk2 theme](https://www.gnome-look.org/p/1080258/)
+ [Adapta theme](https://github.com/adapta-project/adapta-gtk-theme)
+ [Adwaita gtk2 theme](https://gitlab.gnome.org/GNOME/gnome-themes-extra)
+ [Adwaita gtk3 theme](https://gitlab.gnome.org/GNOME/gtk)
+ [Gnome-shell theme](https://gitlab.gnome.org/GNOME/gnome-shell)
+ List of applications (their original css styles used in the theme)  
[Gedit](https://gitlab.gnome.org/GNOME/gedit), [Nautilus](https://gitlab.gnome.org/GNOME/nautilus).

## Screenshots
![sh1](/screenshots/sh1.png?raw=true)
![sh2](/screenshots/sh2.png?raw=true)
![sh2](/screenshots/sh3.png?raw=true)
![sh4](/screenshots/sh3.png?raw=true)
![sh5](/screenshots/sh3.png?raw=true)

