.PHONY: backend-php clean config-dev config-local create-directories frontend-dev upload-uni

backend-php: create-directories
	rsync -avP --delete backend-php/src/ build/backend-php

clean:
	rm -rf build/

config-dev: backend-php frontend-dev
	rsync -avP --delete config/dev-local.php build/backend-php/config/local.php
	rsync -avP --delete config/dev-Config.json.php build/swfm/app/config/Config.json.php

config-local: backend-php frontend-dev
	rsync -avP --delete config/local-local.php build/backend-php/config/local.php

create-directories:
	mkdir -p build

frontend-dev: create-directories
	rsync -avP --delete swfm/ build/swfm

upload-uni: config-dev
	rsync -avPe ssh --delete build/ uni:/var/www/html/swfm-test/v4