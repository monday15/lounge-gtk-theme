## Info
Lounge gtk theme is a fork of Adwaita theme, inspired by Absolute gtk2 theme.  
All links to related projects can be found below.

## IMPORTANT NOTE
This theme is meant to be used with Lounge-aux icons. It is not a "complete" icon theme - it has 10 icons (only symbolic), but they are VITAL for providing correct user expirience. Installation is simple and easy, check out https://github.com/monday15/lounge-aux before procceding with installation.
> Fedora users will get Lounge-aux as a weak dependency with Adwaita as a main icon theme, for other icon themes, they should also check the link. 

## Installation
Clone repository (or download release), run following commands from project directory:  
`meson build`  
`sudo ninja -C build install`

> You can also download last release and simply copy Lounge directory from archieve to your themes folder.

Fedora users can install theme via copr:  
`sudo dnf copr enable monday15/lounge`  
`sudo dnf install lounge-gtk-theme`

## Extra
Firefox is look decent with the theme, I use only two tweaks, you can find it in `firefox-tweak` folder (works only with light theme). Just copy `userChrome.css` to your profile - the path looks like this `~/.mozilla/firefox/randomletters.default/chrome/userChrome.css`.

## Removing
Run from project directory:  
`sudo ninja -C build uninstall`  
or simply remove installation folder `/usr/share/themes/Lounge`.

## Licence
GPLv3+, see LICENSE file.  
Original themes/styles copyrights are in COPYRIGHT file.

## Thanks
All the guys in #gnome-hackers chanell on gnome irc,  
horst3180,  
Emmanuele Bassi,  
Sam Hewitt,  
ZMA from gnome-look.org,  
All the guys in a copyright file,  
Meson developers,
Yaru gtk theme developers,  
Gnome developers and maintainers,  
Fedora developers and maintainers.

## Links
+ [Absolute gtk2 theme](https://www.gnome-look.org/p/1080258/)
+ [Adwaita gtk2 theme](https://gitlab.gnome.org/GNOME/gnome-themes-extra)
+ [Adwaita gtk3 theme](https://gitlab.gnome.org/GNOME/gtk)
+ [Gnome-shell theme](https://gitlab.gnome.org/GNOME/gnome-shell)
+ List of applications (their original css styles used in the theme)  
[Gedit](https://gitlab.gnome.org/GNOME/gedit), [Nautilus](https://gitlab.gnome.org/GNOME/nautilus).

## Screenshots
![sh1](/screenshots/sh1.png?raw=true)
![sh2](/screenshots/sh2.png?raw=true)
![sh2](/screenshots/sh3.png?raw=true)
![sh3](/screenshots/sh4.png?raw=true)
![sh4](/screenshots/sh5.png?raw=true)

