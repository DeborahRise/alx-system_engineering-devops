#  set up your client SSH configuration file
file { '/etc/ssh/ssh_config':
ensure => 'present',
path => /etc/ssh/ssh_config,
content => "
Host Alx,
HostName 54.82.172.244,
User 'ubuntu'
",
line =>IdentityFile ~/.ssh/school,
line => PasswordAuthentication no,

}
