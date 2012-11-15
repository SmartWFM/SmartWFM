.PHONY: backend-php clean config-dev config-local create-directories frontend-dev upload-uni

clean:
	rm -rf build/

create-directories:
	mkdir -p build

backend-php: create-directories
	rsync -avP --delete backend-php/src/ build/backend-php

frontend: create-directories
	export ANT_ARGS='-logger org.apache.tools.ant.listener.AnsiColorLogger' && cd swfm && ant dev && cd ..
	rsync -avP --delete swfm/build/ build/swfm

config-local: backend-php frontend
	rsync -avP --delete config/local-$$USER-local.php build/backend-php/config/local.php
	rsync -avP --delete config/local-$$USER-Config.json.php build/swfm/app/config/Config.json.php
	sed -i 's/^.*\/\* AFS only \*\///' build/swfm/SmartWFM.dev.js

config: backend-php frontend
	rsync -avP --delete config/dev-local.php build/backend-php/config/local.php
	rsync -avP --delete config/dev-Config.json.php build/swfm/app/config/Config.json.php

upload-uni: config
	rsync -avP --delete index.html build/index.php
	rsync -avPe ssh --delete build/ uni:/var/www/html/swfm-test