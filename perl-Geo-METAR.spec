%define module  Geo-METAR
%define name    perl-%{module}
%define version 1.15
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Process aviation weather reports in the METAR format
License:        GPL
Group:          Development/Perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Geo/%{module}-%{version}.tar.gz
BuildRequires:  gmp-devel
BuildArch:      noarch

%description
METAR reports are available on-line, thanks to the National
Weather Service. Since reading the METAR format isn't easy
for non-pilots, these reports are relatively useles to the
common man who just wants a quick glace at the weather.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO README examples/*
%{perl_vendorlib}/Geo
%{_mandir}/*/*

