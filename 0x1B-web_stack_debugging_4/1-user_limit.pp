# Task 1 to fix limit for user

exec { 'fix_limit_hbton_user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# a cmd to increase the users file limit
exec { 'increase_soft_file':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}