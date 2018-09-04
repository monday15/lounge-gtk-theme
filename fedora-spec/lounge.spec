Name:           lounge-gtk-theme
Version:        3.28.0
Release:        1%{?dist}
Summary:        Vintage looking gtk theme, inspired by gtk2 theme absolute

License:        GPLv3+
URL:            https://github.com/monday15/lounge
Source0:        https://github.com/monday15/lounge/archive/v%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  meson >= 0.42.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  sassc    >= 3.3

Requires:	gdk-pixbuf-2.0
Suggests:	lounge-aux-icon-theme

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
* Tue Sep 04 2018 Alex Monday <monday15@gmx.com>
- Initial package

