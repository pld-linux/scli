%define version 0.2.3

Name:		scli
Version:	%{version}
Release:	1
Summary:	A collection of SNMP command line management tools
Summary(pl):	Zestaw narzêdzi SNMP do monitorowania i zarz±dzania 
License:	BSD-like
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
URL:		http://www.ibr.cs.tu-bs.de/projects/scli/
Source0:	ftp://ftp.ibr.cs.tu-bs.de/local/scli/%{name}-%{version}.tar.gz
#Patch: scli-%{version}-missing.patch
BuildPrereq: 	glib >= 1.2 
BuildPrereq: 	libxml2 >= 2.0
BuildPrereq:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The scli package contains small and efficient command line utilities
to monitor and configure network devices and host systems. It is based
on the Simple Network Management Protocol (SNMP).


%description -l pl
scli jest narzêdziem s³u¿±cym do do monitorowania i konfiguracji urz±dzeñ
sieciowych i systemów operacyjnych przy pomocy protokolu SNMP.

%prep
%setup -q 
#%patch -p1

%build
CPPFLAGS="-I%{_includedir}/ncurses"
export CPPFLAGS

./configure --prefix=/usr 

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
mkdir -p $RPM_BUILD_ROOT/usr/share/info
if [ ! $RPM_BUILD_ROOT/usr/info = $RPM_BUILD_ROOT/%{_infodir} ] 
then mv $RPM_BUILD_ROOT/usr/info/* $RPM_BUILD_ROOT/%{_infodir}
fi 

if [ ! $RPM_BUILD_ROOT/usr/man = $RPM_BUILD_ROOT/%{_mandir} ] 
then mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/%{_mandir}
fi


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc %{_infodir}/*
%doc %{_mandir}/man1/*
%doc AUTHORS COPYING NEWS README TODO
