%define version 0.2.3

Name:		scli
Version:	%{version}
Release:	1
Summary:	A collection of SNMP command line management tools
Summary(pl):	Zestaw narzedzi SNMP do monitorowania i zarzadzania 
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
URL:		http://www.ibr.cs.tu-bs.de/projects/scli/
Source0:	ftp://ftp.ibr.cs.tu-bs.de/local/scli/%{name}-%{version}.tar.gz
#Patch: scli-%{version}-missing.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The scli package contains small and efficient command line utilities
to monitor and configure network devices and host systems. It is based
on the Simple Network Management Protocol (SNMP).


%description -l pl
Pakiet scli zawiera poreczne narzedzia (dzialajace z linii polecen) sluzace 
do monitorowania i konfiguracji urzadzen sieciowych i systemów operacyjnych
przy pomocy protokolu SNMP. 

%prep
%setup -q 
#%patch -p1

%build
./configure --prefix=%{_prefix}
if [ -x %{_bindir}/getconf ] ; then
    NRPROC=$(%{_bindir}/getconf _NPROCESSORS_ONLN)
    if [ $NRPROC -eq 0 ] ; then
   NRPROC=1
    fi
else
    NRPROC=1
fi

%{__make} -j $NRPROC


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
# Adjust info,man paths to /usr/share as recommende by Linux FSSTD
install -d $RPM_BUILD_ROOT%{_datadir}/info
mv $RPM_BUILD_ROOT%{_infodir}/* $RPM_BUILD_ROOT%{_datadir}/info

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc %{_datadir}/info/*
%doc %{_mandir}/man1/*
%doc AUTHORS COPYING NEWS README TODO
