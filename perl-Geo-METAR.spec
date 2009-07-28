%define upstream_name    Geo-METAR
%define upstream_version 1.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Process aviation weather reports in the METAR format
License:    GPL
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  gmp-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
METAR reports are available on-line, thanks to the National
Weather Service. Since reading the METAR format isn't easy
for non-pilots, these reports are relatively useles to the
common man who just wants a quick glace at the weather.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

