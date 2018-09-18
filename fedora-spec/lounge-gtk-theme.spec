Name:           lounge-gtk-theme
Version:        3.28.3
Release:        1%{?dist}
Summary:        Simple and clean gtk theme

License:        GPLv3+
URL:            https://github.com/monday15/lounge
Source0:        https://github.com/monday15/lounge/archive/v%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  sassc
BuildRequires:  meson >= 0.42.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

Requires:	gdk-pixbuf2
Recommends:	lounge-aux-icon-theme

%global debug_package %{nil}

%description
%{summary}

%prep
%autosetup -p1 -n lounge-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE COPYRIGHT
%doc README.md
%{_datadir}/themes/Lounge/*


%changelog
* Mon Sep 10 2018 Alex Monday <monday15@gmx.com>
- Update to 3.28.3

* Mon Sep 10 2018 Alex Monday <monday15@gmx.com>
- Prepare to 3.28.2
- Add sassc dependency

* Sat Sep 08 2018 Alex Monday <monday15@gmx.com>
- Update to 3.28.1
- Drop sassc dependency

* Tue Sep 04 2018 Alex Monday <monday15@gmx.com>
- Initial package

