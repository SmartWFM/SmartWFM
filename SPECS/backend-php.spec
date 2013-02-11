Summary:	Backend for Smart Web File Manager in PHP
Name:		backend-php
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Internet
Source0:	backend-php-%{version}.tar.gz
#			https://github.com/SmartWFM/%{name}/archive/%{version}.tar.gz
Source1:	local.php
URL:		https://github.com/SmartWFM/
Packager:	Morris Jobke <morris.jobke@gmail.com>
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch
Requires:	httpd >= 2.0
Requires:	php >= 5.3

%description
This is the PHP backend for the Smart Web File Manager.

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/www/backend-php/config
cp -ar src/* $RPM_BUILD_ROOT/var/www/backend-php
rm $RPM_BUILD_ROOT/var/www/backend-php/config/*.dist
install -m 0644 %{_sourcedir}/local.php $RPM_BUILD_ROOT/var/www/backend-php/config/

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /var/www/backend-php/config/local.php
/var/www/backend-php/commands
/var/www/backend-php/lib
/var/www/backend-php/index.php

%changelog
* Mon Feb 11 2013 Morris Jobke <morris.jobke@gmail.com>
- initial RPM