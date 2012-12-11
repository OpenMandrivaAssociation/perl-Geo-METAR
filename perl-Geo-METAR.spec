%define upstream_name    Geo-METAR
%define upstream_version 1.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Process aviation weather reports in the METAR format
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	gmp-devel
BuildArch:	noarch

%description
METAR reports are available on-line, thanks to the National
Weather Service. Since reading the METAR format isn't easy
for non-pilots, these reports are relatively useles to the
common man who just wants a quick glace at the weather.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc TODO README examples/*
%{perl_vendorlib}/Geo
%{_mandir}/*/*

%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.150.0-1mdv2010.0
+ Revision: 401658
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.15-3mdv2009.0
+ Revision: 257090
- rebuild
- fix no-buildroot-tag

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2008.1
+ Revision: 156695
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill (multiple!) definitions of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-5mdv2008.0
+ Revision: 86453
- rebuild


* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:36:46 (56134)
- test in %%check
- fix install section

* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:33:56 (56129)
Import perl-Geo-METAR

* Thu Dec 15 2005 Arnaud de Lorbeau <adelorbeau@mandriva.com> 1.14-3mdk
- rebuild
- mkrel

* Wed Feb 11 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.14-2mdk
- Own dir

* Fri Nov 21 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.14-1mdk
- New package for lcdproc

