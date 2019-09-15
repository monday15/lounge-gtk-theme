Name:           lounge-gtk-theme
Version:        1.21
Release:        1%{?dist}
Epoch:          1
Summary:        Simple and clean gtk theme

License:        GPLv3+
URL:            https://github.com/monday15/lounge-gtk-theme
Source0:        https://github.com/monday15/lounge-gtk-theme/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  sassc
BuildRequires:  meson >= 0.45.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  gnome-shell
BuildRequires:  gtk3

BuildRequires:  intltool
BuildRequires:  librsvg2

Requires:       gdk-pixbuf2
Requires:       gtk-murrine-engine
Recommends:     lounge-aux-icon-theme
Recommends:     lounge-backgrounds
Recommends:     google-roboto-fonts
Conflicts:      lounge-gtk-theme-xfce-sway

%global debug_package %{nil}

%description
%{summary}


%package	-n lounge-aux-icon-theme

Summary:	Set of auxiliary symbolic icons for Lounge gtk theme

Requires:	adwaita-icon-theme

%description    -n lounge-aux-icon-theme

Set of auxiliary symbolic icons for Lounge gtk theme


%package	-n lounge-gtk-theme-xfce-sway

Summary:	Simple and clean gtk theme for xfce/sway users

Requires:       gdk-pixbuf2
Requires:       gtk-murrine-engine
Recommends:     lounge-aux-icon-theme
Conflicts:      lounge-gtk-theme

%description    -n lounge-gtk-theme-xfce-sway

Simple and clean gtk theme for xfce/sway users

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%post -n lounge-gtk-theme-xfce-sway
sed -i 's!GtkMenu::horizontal-padding  = 0!GtkMenu::horizontal-padding  = 1!g' %{_datadir}/themes/Lounge/gtk-2.0/main.rc
sed -i 's!#widget_class!widget_class!g' %{_datadir}/themes/Lounge/gtk-2.0/main.rc
sed -i 's!GtkMenu::horizontal-padding  = 0!GtkMenu::horizontal-padding  = 1!g' %{_datadir}/themes/Lounge-night/gtk-2.0/main.rc
sed -i 's!#widget_class!widget_class!g' %{_datadir}/themes/Lounge-night/gtk-2.0/main.rc
sed -i 's!GtkMenu::horizontal-padding  = 0!GtkMenu::horizontal-padding  = 1!g' %{_datadir}/themes/Lounge/gtk-2.0/main.rc
sed -i 's!#widget_class!widget_class!g' %{_datadir}/themes/Lounge-compact/gtk-2.0/main.rc
sed -i 's!GtkMenu::horizontal-padding  = 0!GtkMenu::horizontal-padding  = 1!g' %{_datadir}/themes/Lounge-night/gtk-2.0/main.rc
sed -i 's!#widget_class!widget_class!g' %{_datadir}/themes/Lounge-night-compact/gtk-2.0/main.rc

%files
%license LICENSE COPYRIGHT
%doc README.md
%{_datadir}/themes/Lounge/*
%{_datadir}/themes/Lounge-night/*
%{_datadir}/themes/Lounge-compact/*
%{_datadir}/themes/Lounge-night-compact/*

%files -n lounge-gtk-theme-xfce-sway
%license LICENSE COPYRIGHT
%doc README.md
%{_datadir}/themes/Lounge/*
%{_datadir}/themes/Lounge-night/*
%{_datadir}/themes/Lounge-compact/*
%{_datadir}/themes/Lounge-night-compact/*

%files -n lounge-aux-icon-theme
%license LICENSE COPYRIGHT
%doc README.md
%{_datadir}/icons/Lounge-aux/*
%ghost %{_datadir}/icons/Lounge-aux/icon-theme.cache


%changelog
* Sat Jul 13 2019 Alex Monday <monday15@gmx.com>
- Update to 1.20
- Merge xfce/sway variant into regular spec
- Add recommendation for lounge-backgrounds

* Fri Mar 08 2019 Alex Monday <monday15@gmx.com>
- Update to 1.15
- Add Roboto font to recommends
- Clean spec
