<?php
	/* Set basepath of the file manager

	   USED BY: core, afs_special_actions, archive_actions, base_actions,
	   base_direct_actions, file_info_actions, new_file, search_actions
	*/
	SmartWFM_Registry::set('basepath', '/home/mjob/Projekte/www/test');

	/* Specify the commands to be loaded
	   (possible values are all filenames in the commands directory without
	   their extension)

	   USED BY: core
	*/
	SmartWFM_Registry::set('commands', array(
		'base_actions', 'base_direct_commands', 'archive_actions',
		'setting_actions', 'search_actions', 'feedback_actions',
		'file_info_actions', 'bookmarks_actions', 'new_file'
	));

	/* Specify in which subdirectory the commands are located
			(standard value should be correct)

	   USED BY: core
	*/
	SmartWFM_Registry::set('commands_path', 'commands');

	/* Set filesystem type
	   - use one of the following options:
			* local - uses standard php filesystem functions
			* afs - like local just with additional support for afs-acl's

	   USED BY: archive_actions, base_actions, base_direct_actions,
	   file_info_actions, new_file, search_actions
	*/
	SmartWFM_Registry::set('filesystem_type', 'local');

	/* Set to True to use the X-Sendfile header
	   The Webserver must support X-Sendfile header!!!
	   Apache 2.x:
	   - install mod_xsendfile
	   - Set config options:
	     - XSendFile On
	     - XSendFileAllowAbove On

	   USED BY: base_direct_actions
	*/
	SmartWFM_Registry::set('use_x_sendfile', False);

	/* Specify temporary folder to create archives for folder download

	   USED BY: base_direct_actions
	*/
	SmartWFM_Registry::set('temp_folder', '/tmp');

	/* Use this file to store the settings.
	   For multiuser support you have to modify the filename dynamically.
	   E.g.: SmartWFM_Registry::set('setting_filename',
			'/home/'.$_SERVER['PHP_AUTH_USER'].'/.smartwfm.ini');

	   USED BY: setting_actions
	*/
	SmartWFM_Registry::set('setting_filename', '/home/mjob/Projekte/www/test/swfm.ini');

	/* Use this file to store the bookmarks.
	   For multiuser support you have to modify the filename dynamically.
	   E.g.: SmartWFM_Registry::set('bookmarks_filename',
			'/home/'.$_SERVER['PHP_AUTH_USER'].'/.smartwfm_bookmarks.ini');

	   USED BY: bookmarks_actions
	*/
	SmartWFM_Registry::set('bookmarks_filename', '/home/mjob/Projekte/www/test/swfm_bookmarks.ini');

	/* Specify e-mail address(es) which should receive feedback messages

	   USED BY: feedback_actions
	*/
	SmartWFM_Registry::set('feedback_receiver', 'webmaster@example.com, admin@example.com');

	/* Specify e-mail address which is the sender of the feedback messages

	   USED BY: feedback_actions
	*/
	SmartWFM_Registry::set('feedback_sender', 'user@example.com');

	/* Set regex to match folders, which shouldn't listed while do a "dir.list" request

	   USED BY: base_actions
	*/
	SmartWFM_Registry::set('folder_exclude_regex', '!^/home$!');

	/* Specify the initial default bookmarks
	   This is an array of a two value (name, location) array
	   E.g.: array(array('name1', '/path/to/name1'), array('name2', '/path/to/name2'))

	   USED BY: bookmarks_actions
	*/
	SmartWFM_Registry::set('default_bookmarks', array(array('/var/www', '/var/www')));
?>

