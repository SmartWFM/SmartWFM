<?php
	$user = $_SERVER['REMOTE_USER'];
	$path = '/afs/tu-chemnitz.de/home/urz/';
	$path .= substr($user,0,1) . '/'. $user;

	/* Set basepath of the file manager

	   USED BY: core, afs_special_actions, archive_actions, base_actions,
	   base_direct_actions, file_info_actions, new_file, search_actions
	*/
	SmartWFM_Registry::set('basepath', '/afs/tu-chemnitz.de');

	/* Specify the commands to be loaded
	   (possible values are all filenames in the commands directory without
	   their extension)

	   USED BY: core
	*/
	SmartWFM_Registry::set('commands', array(
		'base_actions', 'base_direct_commands', 'archive_actions', 
		'afs_special_actions', 'setting_actions', 'search_actions', 
		'feedback_actions', 'file_info_actions', 'bookmarks_actions'
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
	SmartWFM_Registry::set('filesystem_type', 'afs');

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

	/* Use this file to store the settings.
	   For multiuser support you have to modify the filename dynamically.
	   E.g.: SmartWFM_Registry::set('setting_filename',
			'/home/'.$_SERVER['PHP_AUTH_USER'].'/.smartwfm.ini');

	   USED BY: setting_actions
	*/
	SmartWFM_Registry::set('setting_filename', $path . '/.smartwfm.ini');

	/* Use this file to store the bookmarks.
	   For multiuser support you have to modify the filename dynamically.
	   E.g.: SmartWFM_Registry::set('bookmarks_filename',
			'/home/'.$_SERVER['PHP_AUTH_USER'].'/.smartwfm_bookmarks.ini');

	   USED BY: bookmarks_actions
	*/
	SmartWFM_Registry::set('bookmarks_filename', $path . '/.smartwfm_bookmarks.ini');

	/* Specify e-mail address(es) which should receive feedback messages

	   USED BY: feedback_actions
	*/
	SmartWFM_Registry::set('feedback_receiver', 'mjob@hrz.tu-chemnitz.de, webmaster@tu-chemnitz.de');

	/* Specify e-mail address which is the sender of the feedback messages

	   USED BY: feedback_actions
	*/
	SmartWFM_Registry::set('feedback_sender', $user.'@hrz.tu-chemnitz.de');
?>

