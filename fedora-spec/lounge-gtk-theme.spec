# Set boostrap to 1 for initial bootstrapping when gtk3 is not yet built
# Taken from adwaita-icon-theme spec, dont know how it works
%global bootstrap 0

Name:           lounge-gtk-theme
Version:        1.14
Release:        1%{?dist}
Epoch:          1
Summary:        Simple and clean gtk theme

License:        GPLv3+
URL:            https://github.com/monday15/lounge-gtk-theme
Source0:        https://github.com/monday15/lounge-gtk-theme/archive/%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  sassc
BuildRequires:  meson >= 0.45.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  gnome-shell

BuildRequires:  intltool
BuildRequires:  librsvg2
%if ! 0%{bootstrap}
BuildRequires:  /usr/bin/gtk-encode-symbolic-svg
%endif

Requires:	gdk-pixbuf2
Requires:	gtk-murrine-engine
Recommends:	lounge-aux-icon-theme

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
* Tue Feb 26 2019 Alex Monday <monday15@gmx.com>
- Update to 1.14

* Sat Feb 09 2019 Alex Monday <monday15@gmx.com>
- Update to 1.13

* Sun Feb 03 2019 Alex Monday <monday15@gmx.com>
- Update to 1.12
- Update required version of meson

* Wed Jan 16 2019 Alex Monday <monday15@gmx.com>
- Update to 1.11
- Revert required version of meson

* Sun Dec 30 2018 Alex Monday <monday15@gmx.com>
- Update to 1.10
- Update required version of meson

* Sat Dec 23 2018 Alex Monday <monday15@gmx.com>
- Update to 1.9
- Merge Lounge-aux-icon-theme

* Sat Dec 01 2018 Alex Monday <monday15@gmx.com>
- Update to 1.8

* Tue Nov 27 2018 Alex Monday <monday15@gmx.com>
- Update to 1.7

* Tue Nov 13 2018 Alex Monday <monday15@gmx.com>
- Update to 1.6

* Sat Oct 20 2018 Alex Monday <monday15@gmx.com>
- Update to 1.5

* Sat Oct 13 2018 Alex Monday <monday15@gmx.com>
- Update to 1.4
- Drop gtk dependency
- Add gnome-shell dependency (required for build)

* Wed Sep 29 2018 Alex Monday <monday15@gmx.com>
- Update to 1.3

* Wed Sep 29 2018 Alex Monday <monday15@gmx.com>
- Update to 1.2

* Wed Sep 26 2018 Alex Monday <monday15@gmx.com>
- Update to 1.1

* Sun Sep 23 2018 Alex Monday <monday15@gmx.com>
- Update to 1.0

* Tue Sep 18 2018 Alex Monday <monday15@gmx.com>
- Update to 3.30.3

* Mon Sep 10 2018 Alex Monday <monday15@gmx.com>
- Prepare to 3.28.2
- Add sassc dependency

* Sat Sep 08 2018 Alex Monday <monday15@gmx.com>
- Update to 3.28.1
- Drop sassc dependency

* Tue Sep 04 2018 Alex Monday <monday15@gmx.com>
- Initial package

