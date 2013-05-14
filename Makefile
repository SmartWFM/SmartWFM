.PHONY: backend-php clean config-dev config-local create-directories frontend-dev upload-uni build

BUILD_VERSION=dev
VERSION=1.0

clean:
	rm -rf build/

create-directories:
	mkdir -p build

backend-php: create-directories
	rsync -avP --delete backend-php/src/ build/backend-php

frontend: create-directories
	export ANT_ARGS='-logger org.apache.tools.ant.listener.AnsiColorLogger' && cd swfm && ant ${BUILD_VERSION} && cd ..
	rsync -avP --delete swfm/build/ build/swfm

config-local: backend-php frontend
	rsync -avP --delete config/local-$$USER-local.php build/backend-php/config/local.php
	rsync -avP --delete config/local-$$USER-Config.json.php build/swfm/app/config/Config.json.php
	rsync -avP --delete config/local-$$USER-new_file.cfg build/backend-php/config/new_file.cfg
	#rsync -avP --delete config/dev-new_file/ build/backend-php/config/new_file
	sed -i 's/^.*\/\* AFS only \*\///' build/swfm/SmartWFM.dev.js

config: backend-php frontend
	rsync -avP --delete config/dev-local.php build/backend-php/config/local.php
	rsync -avP --delete config/dev-Config.json.php build/swfm/app/config/Config.json.php
	rsync -avP --delete config/dev-new_file.cfg build/backend-php/config/new_file.cfg
	#rsync -avP --delete config/dev-new_file/ build/backend-php/config/new_file

upload-uni: config
	rsync -avP --delete index.html build/index.php
	rsync -avPe ssh --delete build/ uni:/var/www/html/swfm-test

build:
	cd backend-php && make ARCHIVE_VERSION=${VERSION} archive && cd ..
	cd swfm && make ARCHIVE_VERSION=${VERSION} archive && cd ..
	mkdir -p ~/rpmbuild/SOURCES
	cp backend-php/dist/backend-php-${VERSION}.tar.gz ~/rpmbuild/SOURCES
	cp swfm/dist/swfm-${VERSION}.tar.gz ~/rpmbuild/SOURCES
	cp SOURCES/* ~/rpmbuild/SOURCES
	rpmbuild -ba SPECS/swfm.spec
	rpmbuild -ba SPECS/swfm-backend-php.spec