#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Admin-Config
Summary:	Apache::Admin::Config - manipulate Apache configuration files
Summary(pl):	Apache::Admin::Config - manipulowanie plikami konfiguracyjnymi Apache'a
Name:		perl-Apache-Admin-Config
Version:	0.91
Release:	3
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eb3f330896a0a64137b2b5174649f40e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::Admin::Config provides an object interface to handling Apache
like configuration files without modifying comments, identation, or
truncated lines.

%description -l pl
Apache::Admin::Config udostêpnia obiektowy interfejs do obs³ugi plików
konfiguracyjnych w stylu Apache bez modyfikowania komentarzy, wciêæ
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
