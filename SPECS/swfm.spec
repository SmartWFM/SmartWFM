Summary:		Smart Web File Manager
Name:			swfm
Version:		1.0
Release:		1
License:		GPL
Group:			Applications/Internet
Source0:		%{name}-%{version}.tar.gz
#				https://github.com/SmartWFM/%{name}/archive/%{version}.tar.gz
Source1:		Config.json.php
URL:			https://github.com/SmartWFM/
Packager:		Morris Jobke <morris.jobke@gmail.com>
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
BuildArch:		noarch
BuildRequires:	ant
Requires:		httpd >= 2.0
Requires:		php >= 5.3
Requires:		swfm-backend-php >= 1.0

%description
Smart Web File Manager is a extensible web based file manager

%prep
%setup

%build
export ANT_ARGS='-logger org.apache.tools.ant.listener.AnsiColorLogger' && ant all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/www/html/swfm
cp -ar build/* $RPM_BUILD_ROOT/var/www/html/swfm
install -m 0644 %{_sourcedir}/Config.json.php $RPM_BUILD_ROOT/var/www/html/swfm/app/config/

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /var/www/html/swfm/app/config/Config.json.php
%config(noreplace) /var/www/html/swfm/app/config/Icons.js
/var/www/html/swfm/extjs
/var/www/html/swfm/i18n
/var/www/html/swfm/index.html
/var/www/html/swfm/index-dev.html
/var/www/html/swfm/resources
/var/www/html/swfm/SmartWFM.css
/var/www/html/swfm/SmartWFM.min.css
/var/www/html/swfm/SmartWFM.dev.js
/var/www/html/swfm/SmartWFM.min.js

%changelog
* Mon Feb 25 2013 Morris Jobke <morris.jobke@gmail.com>
- updated RPM SPEC file

* Mon Feb 11 2013 Morris Jobke <morris.jobke@gmail.com>
- initial RPM