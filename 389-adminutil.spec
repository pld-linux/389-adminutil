# TODO
# - merge with fedora-ds-admin.spec
Summary:	Utility library for 389 administration
Name:		389-adminutil
Version:	1.1.9
Release:	1
License:	LGPL v2
Group:		Development/Libraries
URL:		http://directory.fedoraproject.org/wiki/AdminUtil
Source0:	http://directory.fedoraproject.org/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	da96a9673ac983b79475fd9c51b663c3
BuildRequires:	icu
BuildRequires:	libicu-devel
BuildRequires:	mozldap-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	svrcore-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
389-adminutil is libraries of functions used to administer directory
servers, usually in conjunction with the admin server. 389-adminutil
is broken into two libraries - libadminutil contains the basic
functionality, and libadmsslutil contains SSL versions and wrappers
around the basic functions. The PSET functions allow applications to
store their preferences and configuration parameters in LDAP, without
having to know anything about LDAP. The configuration is cached in a
local file, allowing applications to function even if the LDAP server
is down. The other code is typically used by CGI programs used for
directory server management, containing GET/POST processing code as
well as resource handling (ICU ures API).

%package devel
Summary:	Development and header files for 389-adminutil
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libicu-devel
Requires:	mozldap-devel
Requires:	nspr-devel
Requires:	nss-devel
Requires:	pkgconfig
Requires:	svrcore-devel
Provides:	adminutil-devel = %{version}-%{release}
Obsoletes:	adminutil-devel < 1.1.8-2

%description devel
Development files and header files necessary to build applications
that use 389-adminutil.

%prep
%setup -q

%build
%configure \
	--disable-tests \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.a
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/%{name}.pc
%{_libdir}/*.so
%{_includedir}/libadminutil
%{_includedir}/libadmsslutil
