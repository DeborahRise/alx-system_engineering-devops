# set up your client SSH configuration file using puppet


exec {'/etc/ssh/ssh_config':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/school:wq" >> /etc/ssh/ssh_config',
}
