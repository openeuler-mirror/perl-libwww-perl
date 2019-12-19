%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Authen::NTLM|Encode|File::Listing|HTTP::Date|HTTP::Negotiate|HTTP::Request|HTTP::Response|HTTP::Status|LWP::MediaTypes|MIME::Base64|Net::FTP|Net::HTTP|URI|WWW::RobotRules)\\)$

Name:           perl-libwww-perl
Version:        6.35
Release:        2
Summary:        The World-Wide Web library for Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/libwww-perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/libwww-perl-%{version}.tar.gz
Patch0000:      libwww-perl-6.19-Accept-proxy-URLs-with-IPv6-host-names.patch
BuildArch:      noarch

BuildRequires:  perl-generators perl-interpreter perl(:VERSION) >= 5.8.1
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620 perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy) perl(Getopt::Long) perl(Module::Metadata) perl(strict) perl(warnings)
BuildRequires:  perl(base) perl(Carp) perl(Digest::MD5) perl(Encode) >= 2.12 perl(Encode::Locale)
BuildRequires:  perl(Exporter) perl(HTML::Entities) perl(HTML::HeadParser) perl(HTTP::Config)
BuildRequires:  perl(HTTP::Date) >= 6 perl(HTTP::Headers::Util) perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Request::Common) >= 6 perl(HTTP::Response) >= 6 perl(HTTP::Status) >= 6
BuildRequires:  perl(IO::Select) perl(IO::Socket) perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(MIME::Base64) >= 2.1 perl(Net::HTTP) >= 6.07 perl(parent)
BuildRequires:  perl(Scalar::Util) perl(Try::Tiny) perl(URI) >= 1.10 perl(URI::Escape)
BuildRequires:  perl(WWW::RobotRules) >= 6 perl(Config) perl(File::Spec)
BuildRequires:  perl(File::Temp) perl(FindBin) perl(HTTP::Daemon) >= 6
BuildRequires:  perl(Test::Fatal) perl(Test::More) perl(Test::RequiresInternet)
BuildRequires:  perl(utf8) perl(Test::Needs)

BuildConflicts: perl(HTTP::Status) = 6.17

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Authen::NTLM) >= 1.02 perl(Encode) >= 2.12
Requires:       perl(HTML::HeadParser) perl(HTTP::Config) perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::Date) >= 6 perl(HTTP::Headers::Util) perl(HTTP::Negotiate) >= 6
Requires:       perl(HTTP::Request) >= 6 perl(HTTP::Request::Common) >= 6 perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6 perl(LWP::MediaTypes) >= 6 perl(MIME::Base64) >= 2.1
Requires:       perl(Net::FTP) >= 2.58 perl(Net::HTTP) >= 6.07 perl(URI) >= 1.10
Requires:       perl(URI::Escape) perl(WWW::RobotRules) >= 6

Suggests:       perl(CPAN::Config) perl(HTML::FormatPS) perl(HTML::FormatText)
Suggests:       perl(HTML::Parse) perl(LWP::Protocol::https) >= 6.02

Provides:       perl(LWP::Debug::TraceHTTP::Socket) = %{version}
Provides:       perl(LWP::Protocol::http::Socket) = %{version}
Provides:       perl(LWP::Protocol::http::SocketMethods) = %{version}

%description
The libwww-perl collection is a set of Perl modules which provides a simple
and consistent application programming interface (API) to the World-Wide Web.
The main focus of the library is to provide classes and functions that allow
you to write WWW clients. The library also contain modules that are of more general
use and even classes that help you implement simple HTTP servers.

%package help
Summary:        Documentation for perl-libwww-perl

%description help
Documentation for perl-libwww-perl.

%prep
%autosetup -n libwww-perl-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 --aliases < /dev/null
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{__chmod} -Rf a+rX,u+w,g-w,o-w $RPM_BUILD_ROOT/*

%check
unset PERL_LWP_ENV_HTTP_TEST_SERVER_TIMEOUT PERL_LWP_ENV_HTTP_TEST_URL
make test

%files
%license LICENSE
%{_bindir}/*
%{perl_vendorlib}/
%exclude %{_libdir}/perl5/perllocal.pod

%files help
%doc Changes README.SSL
%{_mandir}/man1/
%{_mandir}/man3/

%changelog
* Thu Oct 24 2019 Zaiwang Li <lizaiwang1@huawei.com> - 6.35-2
- Init package.
