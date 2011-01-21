%define name	clara
%define version 0.20031214
%define tarver  20031214
%define release %mkrel 6
%define rc_name	%{name}-%{tarver}

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}

Summary: 	An OCR (Optical Character Recognition) program
URL: 		http://www.geocities.com/claraocr
Source: 	http://www.geocities.com/claraocr/%{rc_name}.tar.bz2
Patch0:		clara-optflags.patch
Patch1:		clara-fix-str-fmt.patch
Patch2:		clara-gcc44.patch
License: 	GPL
Group: 		Graphics
Buildroot: 	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	libx11-devel

%description
Clara OCR is intended for large scale digitalization projects. 
It features a powerful GUI and a web interface for cooperative 
digitalization of books. Clara OCR development started in 1999 
and we're approaching production level.

%prep
%setup -q -n %{rc_name}
%patch0 -p1 -b .makefile
%patch1 -p0 -b .str
%patch2 -p0 -b .gcc
%if %_lib == lib64
sed -i 's|LIBPATH = -L/usr/X11R6/lib|LIBPATH = |' Makefile
%endif

%build
%make LDFLAGS="%ldflags"
%make doc

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp clara $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/clara.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/clara-dev.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/clara-adv.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/*html doc/FAQ doc/README
%{_mandir}/man1/clara*
%{_bindir}/*

