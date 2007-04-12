Name:           perl-%realname
Version:        1.14
Release:        %mkrel 4
%define realname        Geo-METAR

License:        GPL
Group:          Development/Perl
Summary:        Geo::METAR - Process aviation weather reports in the METAR format.
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/%{realname}-%{version}.tar.bz2
Url:            http://www.cpan.org
Prefix:         %{_prefix}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  perl-devel gmp-devel
Requires:       perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:      noarch

%description
METAR reports are available on-line, thanks to the National
Weather Service. Since reading the METAR format isn't easy
for non-pilots, these reports are relatively useles to the
common man who just wants a quick glace at the weather.

%prep
%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc TODO README MANIFEST examples/*
%dir %{perl_vendorlib}/Geo
%{perl_vendorlib}/Geo/METAR.pm
%{_mandir}/*/*

