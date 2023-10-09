# Setting up the Web servers using Puppet
exec {'check system update':
  command => "sudo apt update",
}

package {'nginx':
  ensure => 'installed',
}

file {"/data":
  ensure => 'directory'
}

file {"/data/web_static":
  ensure => 'directory',
}

file {"/data/web_static/releases":
  ensure => 'directory',
}

file {"/data/web_static/releases/test":
  ensure => 'directory',
}

file {"/data/web_static/releases/test/index.html":
  ensure => 'present',
  content => "Hello, World!"
}

file {"/data/web_static/shared":
  ensure => 'directory',
}

file {"/data/web_static/current":
  ensure => 'link',
  target => "/data/web_static/releases/test/",
}

exec {"chown_data":
  command => "chown -R ubuntu:ubuntu /data/"
}

exec {"hbnb_static":
  command => 'sudo sed -i "/listen 80 default_server;/a \\\tlocation \/hbnb_static \{\n\\t\\talias \/data\/web_static\/current\/;\n\\t\}\n" /etc/nginx/sites-enabled/default',
  require => Package['nginx'],
  notify => Service['nginx service']
}

service {"nginx_service":
  ensure => 'running'
}
