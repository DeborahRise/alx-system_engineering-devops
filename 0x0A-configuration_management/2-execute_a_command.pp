# kills a process named killmenow
exec { 'kill_killmenow_process':
  command  => '/usr/bin/pkill -9 -f killmenow',
}
