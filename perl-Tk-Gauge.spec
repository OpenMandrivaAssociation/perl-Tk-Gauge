%define upstream_name    Tk-Gauge
%define upstream_version 0.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Create a multitude of analog gauge widgets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Tk)
BuildRequires:	perl-Tk-devel
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
This widget creates an analog gauge. A gauge has various components: a
radius highlighted by a circumference, one or more needles, a hub, three
granularities of tick marks, one of which has a value label, a caption,
title and specialized bands that visually compartmentalize the gauge.

A gauge's appearance is specified by manipulating a set of approximately 60
options, all described below. Given this flexibility one may create
instruments including, but not limited to, a 12 or 24 hour clock, CPU
meter, voltmeter, fuel and temperature gauge, speedometer and tachometer.

The following option/value pairs are supported (default value in
parentheses):

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run %make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 658453
- rebuild for updates rpm-setup

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 420260
- adding missing buildrequires
- adding missing buildrequires:
- import perl-Tk-Gauge


* Sun Aug 23 2009 cpan2dist 0.3-1mdv
- initial mdv release, generated with cpan2dist
