Summary:	Xfontcache library
Summary(pl):	Bibliteka Xfontcache
Name:		xorg-lib-libXfontcache
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libXfontcache-%{version}.tar.bz2
# Source0-md5:	24c8d43dc2118fa214bf168748d68ec3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfontcache library.

%description -l pl
Biblioteka Xfontcache.

%package devel
Summary:	Header files libXfontcache development
Summary(pl):	Pliki nagłówkowe do biblioteki libXfontcache
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-fontcacheproto-devel
Requires:	xorg-lib-libXext-devel

%description devel
Xfontcache library.

This package contains the header files needed to develop programs that
use these libXfontcache.

%description devel -l pl
Biblioteka Xfontcache.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXfontcache.

%package static
Summary:	Static libXfontcache library
Summary(pl):	Biblioteka statyczna libXfontcache
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xfontcache library.

This package contains the static libXfontcache library.

%description static -l pl
Biblioteka Xfontcache.

Pakiet zawiera statyczną bibliotekę libXfontcache.

%prep
%setup -q -n libXfontcache-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXfontcache.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfontcache.so
%{_libdir}/libXfontcache.la
%{_pkgconfigdir}/xfontcache.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfontcache.a
