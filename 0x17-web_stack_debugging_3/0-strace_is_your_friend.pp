#a puppet manuscript to replace a line in a file on a server. it fixes bad 'phpp' extensions to 'php' in the wordpress file

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
