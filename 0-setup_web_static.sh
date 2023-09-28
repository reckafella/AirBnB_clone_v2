#!/usr/bin/env bash
# A bash script that sets up the web servers for the deployment of "web_static"
# Install Nginx if it is not already installed
sudo apt update
sudo apt install nginx -y

# Create folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Add simple content to index.html
sudo echo -e "Hello, World!" > /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -s -f /data/web_static/releases/test /data/web_static/current

# Give ownership of "/data/" to user "ubuntu" and group "ubuntu"
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content of /data/web_static_current/ to
# hbnb_static
sudo sed -i "/listen 80 default_server;/a \\\tlocation \/hbnb_static \{\n\\t\\talias \/data\/web_static\/current\/;\n\\t\}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
