#a puppet manuscript to replace a line in a file on a server. it fixes bad 'phpp' extensions to 'php' in the wordpress file

exec { 'fix-wordpress':
	command => "sed -i 's/phpp/php/g' ${file_to_edit}",
	path	=> ['/bin', '/usr/bin']
}
