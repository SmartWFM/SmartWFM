.PHONY: backend-php clean config-dev config-local create-directories frontend-dev upload-uni

BUILD_VERSION=dev

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