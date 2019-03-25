Name:           lounge-gtk-theme
Version:        1.17
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

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE COPYRIGHT
%doc README.md
%{_datadir}/themes/Lounge/*
%{_datadir}/themes/Lounge-night/*

%files -n lounge-aux-icon-theme
%license LICENSE COPYRIGHT
%doc README.md
%{_datadir}/icons/Lounge-aux/*
%ghost %{_datadir}/icons/Lounge-aux/icon-theme.cache


%changelog
* Fri Mar 08 2019 Alex Monday <monday15@gmx.com>
- Update to 1.15
- Add Roboto font to recommends
- Clean spec

