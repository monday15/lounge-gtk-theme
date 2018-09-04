## Info
---
Lounge gtk theme is a fork of Adwaita theme, inspired by Absolute gtk2 theme.  
Meson build system files based on Yaru's ones. All links to related projects can be found below.

## IMPORTANT NOTE
---
This theme is meant to be used with Lounge-aux-icons. It is not a "complete" icon theme - it has 10 icons (only symbolic), but they are VITAL for providing correct user expirience. Installation is simple and easy, check out https://github.com/monday15/lounge-aux-icons before procceding with installation.
> Fedora users will get Lounge-aux-icons as a weak dependency with Adwaita as a main icon theme, for other icon themes, they should also check the link. 

## Installation
---
Clone repository (or download release), run following commands from project directory:  
`meson build`  
`ninja -C build install`
> "build" is a name of build folder, you can change it if you need.  

Fedora users can install theme via copr:  
`sudo dnf copr enable monday15/lounge`  
`sudo dnf install lounge-gtk-theme`

## Extra
---
Firefox is look decent with the theme, I use only two tweaks, you can find it in firefox-tweak folder. Just copy userChrome.css to your profile - the path is `~/.mozilla/firefox/randomletters.default/chrome/userChrome.css`.

## Removing
---
Run from project folder:  
```
ninja -C build uninstall
```  
or simply remove installation folder  
```
rm /usr/share/themes/Lounge
```  

## Bugs
---
Report issues here, on github. Please check TODO list below, and existing issues, maybe your issue is already there.

## Licence
---
GPLv3+, see LICENSE file.  
Original themes copyrights are in COPYRIGHT file.

## Thanks
All the guys in #gnome-hackers chanell on gnome irc,  
horst3180,  
Emanuelle Bassi,  
Sam Hewitt,  
All the guys in a copyright file,  
Meson developers,
Yaru gtk theme developers,  
Gnome developers and maintainers,  
Fedora developers and maintainers.

## Links
+ Absolute gtk2 theme  
https://www.gnome-look.org/p/1080258/

+ Adwaita gtk2 theme  
https://gitlab.gnome.org/GNOME/gnome-themes-extra

+ Adwaita gtk3 theme (part of gtk+ project)  
https://gitlab.gnome.org/GNOME/gtk

+ Gedit  
https://gitlab.gnome.org/GNOME/gedit

+ Gnome-shell theme (part of gnome-shell project)  
https://gitlab.gnome.org/GNOME/gnome-shell

+ Meson build system
https://mesonbuild.com/

+ Nautilus  
https://gitlab.gnome.org/GNOME/nautilus

+ Yaru (gtk theme)  
https://github.com/ubuntu/yaru

## TODO

v. 3.28.1 (estimated date 17.09.18)

- [ ] gtk3: Make scss file for applications insted of apps.css
- [ ] gtk3: Better-looking expander buttons
- [ ] gtk3: Fix scrollbar animation (transition from regular scrollbar to small indicator and vice versa)
- [ ] gtk3: Reimplement simplified overshoots/undershoots (effect at the end of a scrolling)
- [ ] gtk2: Tooltips should have border
- [ ] shell: Tweak popup-notification button
- [ ] Nautilus: change status bar color for dark theme
- [ ] Nautilus: Fix animation when extacting archieve in nautilus
- [ ] general: Cleanup unused commented lines


v. 3.30.1 (parallel with 3.28.1)

- [ ] Add support for new style of Nautilus 3.30 

v. 3.28.2 & 3.30.2

- [ ] Evolution: find a workaround to change selected message background color for light theme


## Screenshots
![sh1](/screenshot/sh1.png?raw=true)
![sh2](/screenshot/sh2.png?raw=true)
![sh2](/screenshot/sh3.png?raw=true)
![sh3](/screenshot/sh4.png?raw=true)
![sh4](/screenshot/sh5.png?raw=true)

