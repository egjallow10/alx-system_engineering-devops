# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Start and enable the Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Ensure Nginx is listening on port 80
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80;
                location / {
                  return 200 'Hello World!';
                }
                location /redirect_me {
                  return 301 /;
                }
              }",
  notify  => Service['nginx'],
}
