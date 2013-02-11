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
Requires:		backend-php >= 1.0

%description
Smart Web File Manager is a extensible web based file manager

%prep
%setup

%build
export ANT_ARGS='-logger org.apache.tools.ant.listener.AnsiColorLogger' && ant all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/www/swfm
cp -ar build/* $RPM_BUILD_ROOT/var/www/swfm
install -m 0644 %{_sourcedir}/Config.json.php $RPM_BUILD_ROOT/var/www/swfm/app/config/

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /var/www/swfm/app/config/Config.json.php
%config(noreplace) /var/www/swfm/app/config/Icons.js
/var/www/swfm/extjs
/var/www/swfm/i18n
/var/www/swfm/index.html
/var/www/swfm/index-dev.html
/var/www/swfm/resources
/var/www/swfm/SmartWFM.css
/var/www/swfm/SmartWFM.min.css
/var/www/swfm/SmartWFM.dev.js
/var/www/swfm/SmartWFM.min.js

%changelog
* Mon Feb 11 2013 Morris Jobke <morris.jobke@gmail.com>
- initial RPM