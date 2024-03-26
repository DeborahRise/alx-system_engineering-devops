#  set up your client SSH configuration file

file { ~/.ssh/school:
ensure => 'present',
enable => True,
content => '~/.ssh/school'
}


file { ~/.ssh/config:
ensure => 'present',
Host => Alx,
HostName => 54.82.172.244,
User => 'ubuntu',
PasswordAuthentication enable => False,
require => File[~/.ssh/school]
}
