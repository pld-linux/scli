Summary:	A collection of SNMP command line management tools
Summary(pl):	Zestaw narzêdzi SNMP do monitorowania i zarz±dzania
Name:		scli
Version:	0.2.3
Release:	2
License:	BSD-like
Group:		Applications/System
Source0:	ftp://ftp.ibr.cs.tu-bs.de/local/scli/%{name}-%{version}.tar.gz
#Patch: scli-%{version}-missing.patch
URL:		http://www.ibr.cs.tu-bs.de/projects/scli/
BuildRequires:	glib-devel >= 1.2 
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The scli package contains small and efficient command line utilities
to monitor and configure network devices and host systems. It is based
on the Simple Network Management Protocol (SNMP).

%description -l pl
scli jest narzêdziem s³u¿±cym do do monitorowania i konfiguracji
urz±dzeñ sieciowych i systemów operacyjnych przy pomocy protokolu
SNMP.

%prep
%setup -q 
#%patch -p1

%build
CPPFLAGS="-I%{_includedir}/ncurses"
export CPPFLAGS

./configure --prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# Adjust info,man paths to /usr/share as recommende by FHS
install -d $RPM_BUILD_ROOT%{_infodir}
mv -f $RPM_BUILD_ROOT%{_prefix}/info/* $RPM_BUILD_ROOT%{_infodir}
mv -f $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_mandir}

gzip -9nf AUTHORS COPYING NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*
