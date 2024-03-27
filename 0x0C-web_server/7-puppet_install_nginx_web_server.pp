# my automated tool for managing configuration

exec{'sudo apt-get update':
	sudo apt-get update
	}

package{'nginx':
	ensure => installed,
	require => Exec['sudo apt-get update']


