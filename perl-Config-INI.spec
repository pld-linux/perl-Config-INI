#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Config
%define		pnam	INI
Summary:	Config::INI - simple .ini-file format
Summary(pl.UTF-8):	Config::INI - prosty format plików .ini
Name:		perl-Config-INI
Version:	0.027
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	61f6b3e890e1818545dd1112ba798273
URL:		https://metacpan.org/dist/Config-INI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Mixin-Linewise >= 0.105
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::INI - simple .ini-file format.

%description -l pl.UTF-8
Config::INI - prosty format plików .ini.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/INI.pm
%{perl_vendorlib}/Config/INI
%{_mandir}/man3/Config::INI*.3pm*
%{_examplesdir}/%{name}-%{version}
