#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Admin-Config
Summary:	Apache::Admin::Config - Manipulate Apache configuration files
Summary(pl):	Apache::Admin::Config - Manipuluj plikami konfiguracyjnymi Apache
Name:		perl-Apache-Admin-Config
Version:	0.55
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::Admin::Config provides an object interface to handling Apache
like configuration files without modifying comments, identation, or
truncated lines.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# I don't get why it's needed... -- radek
install -d $RPM_BUILD_ROOT%{_mandir}/man3
/usr/bin/pod2man lib/Apache/Admin/Config.pm > $RPM_BUILD_ROOT%{_mandir}/man3/Apache::Admin::Config.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Apache/Admin/*.pm
%{_mandir}/man3/*
