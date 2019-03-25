Name:           lounge-gtk-theme-xfce-sway
Version:        1.16.92
Release:        1%{?dist}
Epoch:          1
Summary:        Simple and clean gtk theme, version for xfce and sway

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
Conflicts:      lounge-gtk-theme

%global debug_package %{nil}

%description
%{summary}

%prep
%autosetup -p1 -n lounge-gtk-theme-%{version}

%build
%meson -Dicons=false
%meson_build

%install
%meson_install

%files
%license LICENSE COPYRIGHT
%doc README.md
%{_datadir}/themes/Lounge/*
%{_datadir}/themes/Lounge-night/*


%changelog
* Mon Mar 25 2019 Alex Monday <monday15@gmx.com>
- Initial commit

