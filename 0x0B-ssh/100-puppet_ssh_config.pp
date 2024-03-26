#  set up your client SSH configuration file

file { ~/.ssh/school:
ensure => 'present',
enable => True,
content => '~/.ssh/school'
}


file { ~/.ssh/config:
path => /etc/ssh/ssh_config,
ensure => 'present',
mode => '0744'
content => "
Host Alx,
HostName 54.82.172.244,
User 'ubuntu',
IdentityFile ~/.ssh/school
PasswordAuthentication no
",
}
