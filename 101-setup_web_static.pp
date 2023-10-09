# Setting up the Web servers using Puppet
exec {'check system update':
  command => "sudo /usr/bin/env apt update",
  notify => Exec['update system']
}

exec {'update systen':
  command => "sudo /usr/bin/env apt upgrade -y",
  require => Exec['check system update']
}

package {'nginx':
  ensure => 'installed',
  require => Exec['update system']
}

file {"/data":
  ensure => 'directory'
}

file {"/data/web_static":
  ensure => 'directory',
  require => File['/data'],
  owner => 'ubuntu',
  group => 'ubuntu',
  recurse => true
}

file {"/data/web_static/releases":
  ensure => 'directory',
  require => File['/data/web_static']
}

file {"/data/web_static/releases/test":
  ensure => 'directory',
  require => File['/data/web_static/releases']
}

file {"/data/web_static/releases/test/index.html":
  ensure => 'present',
  require => File['/data/web_static/releases/test'],
  content => "Hello, World!"
}

file {"/data/web_static/shared":
  ensure => 'directory',
  require => File['/data/web_static']
}

file {"/data/web_static/current":
  ensure => 'link',
  require => File['/data/web_static'],
  target => "/data/web_static/releases/test/",
  force => true
}

/* 
exec {"chown_data":
  command => "chown -R ubuntu:ubuntu /data/",
}
 */

exec {"hbnb_static":
  command => 'sudo sed -i "/listen 80 default_server;/a \\\tlocation \/hbnb_static \{\n\\t\\talias \/data\/web_static\/current\/;\n\\t\}\n" /etc/nginx/sites-enabled/default',
  require => Package['nginx'],
  notify => Exec['restart_nginx']
}

exec {"restart_nginx":
  command => "sudo service nginx restart",
  require => Exec["hbnb_static"]
}
