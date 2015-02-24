Summary:	Xfontcache - X-TrueType font cache extension client library
Summary(pl.UTF-8):	Xfontcache - biblioteka kliencka rozszerzenia cache'u fontów X-TrueType
Name:		xorg-lib-libXfontcache
Version:	1.0.5
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfontcache-%{version}.tar.bz2
# Source0-md5:	bbd37768c87f63cf2eb845b2c0f56515
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfontcache is an X-TrueType font cache extension client library.

%description -l pl.UTF-8
Xfontcache to biblioteka kliencka rozszerzenia cache'u fontów
X-TrueType.

%package devel
Summary:	Header files for libXfontcache library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXfontcache
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-fontcacheproto-devel
Requires:	xorg-lib-libXext-devel

%description devel
Xfontcache is an X-TrueType font cache extension client library.

This package contains the header files needed to develop programs that
use libXfontcache.

%description devel -l pl.UTF-8
Xfontcache to biblioteka kliencka rozszerzenia cache'u fontów
X-TrueType.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXfontcache.

%package static
Summary:	Static libXfontcache library
Summary(pl.UTF-8):	Biblioteka statyczna libXfontcache
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xfontcache is an X-TrueType font cache extension client library.

This package contains the static libXfontcache library.

%description static -l pl.UTF-8
Xfontcache to biblioteka kliencka rozszerzenia cache'u fontów
X-TrueType.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXfontcache.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXfontcache.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfontcache.so
%{_libdir}/libXfontcache.la
%{_pkgconfigdir}/xfontcache.pc
%{_mandir}/man3/FontCache*.3*
%{_mandir}/man3/Xfontcache.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfontcache.a
