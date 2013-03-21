Summary:	Backend for Smart Web File Manager in PHP
Name:		swfm-backend-php
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Internet
Source0:	backend-php-%{version}.tar.gz
#			https://github.com/SmartWFM/%{name}/archive/%{version}.tar.gz
Source1:	local.php
Source2:	new_file.cfg
URL:		https://github.com/SmartWFM/
Packager:	Morris Jobke <morris.jobke@gmail.com>
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch
Requires:	httpd >= 2.0
Requires:	php >= 5.3

%description
This is the PHP backend for the Smart Web File Manager.

%prep
%setup -n backend-php-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/www/html/swfm-backend-php/config
cp -ar src/* $RPM_BUILD_ROOT/var/www/html/swfm-backend-php
rm $RPM_BUILD_ROOT/var/www/html/swfm-backend-php/config/*.dist
install -m 0644 %{_sourcedir}/local.php $RPM_BUILD_ROOT/var/www/html/swfm-backend-php/config/
install -m 0644 %{_sourcedir}/new_file.cfg $RPM_BUILD_ROOT/var/www/html/swfm-backend-php/config/

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /var/www/html/swfm-backend-php/config/local.php
%config /var/www/html/swfm-backend-php/config/new_file.cfg
/var/www/html/swfm-backend-php/commands
/var/www/html/swfm-backend-php/lib
/var/www/html/swfm-backend-php/config/new_file
/var/www/html/swfm-backend-php/index.php

%changelog
* Thu Mar 21 2013 Morris Jobke <morris.jobke@gmail.com>
- 1.1

* Mon Feb 25 2013 Morris Jobke <morris.jobke@gmail.com>
- updated RPM SPEC file

* Mon Feb 11 2013 Morris Jobke <morris.jobke@gmail.com>
- initial RPM