Summary:	Browser Bonobo plugin
Summary(pl):	Wtyczka Bonobo dla przegl±darek
Name:		mozilla-bonobo
Version:	0.3.0
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://savannah.nongnu.org/download/moz-bonobo/%{name}-%{version}.tar.gz
# Source0-md5:  cf607f4c20a26ef849dd54565de17532
Patch0:		%{name}-mozilla-config.patch
URL:		http://www.nongnu.org/moz-bonobo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
BuildRequires:	mozilla-embedded-devel
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mozilla-bonobo is a browser plugin. It "bridges" the browser to
Bonobo, the GNOME component technology. It tries to support the
Netscape 4 plugin API, and it should work on many different browsers.

In short: this plugin makes your browser use Bonobo controls to
display supported file types inside the browser window or frame.

%description -l pl
Mozilla-bonobo jest wtyczk± dla przegl±darek. £±czy ona przegl±darkê z
Bonobo, technologi± komponentów GNOME. Wtyczka próbuje wspieraæ API
wtyczek Netscape 4 ale powinna dzia³aæ te¿ z wieloma innymi
przegl±darkami.

W skrócie: wtyczka ta sprawia, ¿e przegl±darka u¿ywa kontrolek Bonobo
do wy¶wietlania wspieranych typów plików w oknie przegl±darki.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-plugin-install-dir=%{_libdir}/mozilla/plugins

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
