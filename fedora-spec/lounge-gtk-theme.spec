Name:           lounge-gtk-theme
Version:        1.4
Release:        1%{?dist}
Epoch:		1
Summary:        Simple and clean gtk theme

License:        GPLv3+
URL:            https://github.com/monday15/lounge-gtk-theme
Source0:        https://github.com/monday15/lounge-gtk-theme/archive/%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  sassc
BuildRequires:  meson >= 0.42.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  gnome-shell

Requires:	gdk-pixbuf2
Requires:	gtk-murrine-engine
Recommends:	lounge-aux-icon-theme

%global debug_package %{nil}

%description
%{summary}

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


%changelog
* Sat Oct 13 2018 Alex Monday <monday15@gmx.com>
- Update to 1.0
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

