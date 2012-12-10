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



%changelog
* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 0.20031214-6mdv2011.0
+ Revision: 632028
- fix build
- bunzip2 the patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.20031214-3mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - import clara


* Fri Jun 02 2006 Stew Benedict <sbenedict@mandriva.com> 0.20031214-3mdv2007.0
- rebuild, new url

* Mon May  9 2005 Stew Benedict <sbenedict@mandriva.com> 0.20031214-2mdk
- fix x86_64 build

* Fri Apr  2 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.20031214-1mdk
- new snapshot, rework patch0

* Mon Mar 10 2003 Marcel Pol <mpol@gmx.net> 0.9.9-3mdk
- buildreq: XFree86-devel

* Mon Dec 30 2002 Stew Benedict <sbenedict@mandrakesoft.com> 0.9.9-2mdk
- rebuild for new glibc/rpm, add %%clean section for rpmlint

* Tue May 07 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9.9-1mdk
- 0.9.9
- refresh patch0

* Thu Nov 29 2001 Yves Duret <yduret@mandrakesoft.com> 0.9.8-1mdk
- version 0.9.8
- fix typo in url

* Mon Jul 23 2001 Yves Duret <yduret@mandrakesoft.com> 0.9.7-1mdk
- first MandrakeSoft package
