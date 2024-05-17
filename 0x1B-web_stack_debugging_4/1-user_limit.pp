# Task 1 to fix limit for user

exec { 'fix_limit_hbton_user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}


# always restart nginx
-> exec { 'nginx-restart':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
