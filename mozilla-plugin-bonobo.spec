%define		_origname mozilla-bonobo

Summary:	Browser Bonobo plugin
Summary(pl.UTF-8):	Wtyczka Bonobo dla przeglądarek
Name:		mozilla-plugin-bonobo
Version:	0.4.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://savannah.nongnu.org/download/moz-bonobo/%{_origname}-%{version}.tar.gz
# Source0-md5:	101ad2c3f8bb25d0ce89e2a7820143b7
URL:		http://www.nongnu.org/moz-bonobo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	mozilla-devel
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mozilla-bonobo is a browser plugin. It "bridges" the browser to
Bonobo, the GNOME component technology. It tries to support the
Netscape 4 plugin API, and it should work on many different browsers.

In short: this plugin makes your browser use Bonobo controls to
display supported file types inside the browser window or frame.

%description -l pl.UTF-8
Mozilla-bonobo jest wtyczką dla przeglądarek. Łączy ona przeglądarkę z
Bonobo, technologią komponentów GNOME. Wtyczka próbuje wspierać API
wtyczek Netscape 4 ale powinna działać też z wieloma innymi
przeglądarkami.

W skrócie: wtyczka ta sprawia, że przeglądarka używa kontrolek Bonobo
do wyświetlania wspieranych typów plików w oknie przeglądarki.

%prep
%setup -q -n %{_origname}-%{version}

%build
%configure \
	--with-plugin-install-dir=%{_libdir}/mozilla/plugins \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_sysconfdir}/gconf/schemas/*
