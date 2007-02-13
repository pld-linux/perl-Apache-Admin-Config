#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Admin-Config
Summary:	Apache::Admin::Config - manipulate Apache configuration files
Summary(pl.UTF-8):	Apache::Admin::Config - manipulowanie plikami konfiguracyjnymi Apache'a
Name:		perl-Apache-Admin-Config
Version:	0.94
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16c3f841580e0f58a98ce42704f5e84f
URL:		http://search.cpan.org/dist/Apache-Admin-Config/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::Admin::Config provides an object interface to handling Apache
like configuration files without modifying comments, identation, or
truncated lines.

%description -l pl.UTF-8
Apache::Admin::Config udostępnia obiektowy interfejs do obsługi plików
konfiguracyjnych w stylu Apache bez modyfikowania komentarzy, wcięć
ani skracania linii.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes UPGRADE-0.10
%dir %{perl_vendorlib}/Apache/Admin
%{perl_vendorlib}/Apache/Admin/*.pm
%{_mandir}/man3/*
