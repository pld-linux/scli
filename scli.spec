Summary:	A collection of SNMP command line management tools
Summary(pl):	Zestaw narz�dzi SNMP do monitorowania i zarz�dzania
Name:		scli
Version:	0.2.12
Release:	4
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://ftp.ibr.cs.tu-bs.de/local/scli/%{name}-%{version}.tar.gz
# Source0-md5:	5e2e783d7e5f734f8588f23f215b3ff0
Patch0:		%{name}.patch
URL:		http://www.ibr.cs.tu-bs.de/projects/scli/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The scli package contains small and efficient command line utilities
to monitor and configure network devices and host systems. It is based
on the Simple Network Management Protocol (SNMP).

%description -l pl
scli jest narz�dziem s�u��cym do do monitorowania i konfiguracji
urz�dze� sieciowych i system�w operacyjnych przy pomocy protoko�u
SNMP.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I%{_includedir}/ncurses `xml2-config --cflags`"
export CPPFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/scli.info*
%{_mandir}/man1/*
