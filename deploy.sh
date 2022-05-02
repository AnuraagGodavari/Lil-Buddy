#!/bin/bash

# Update repos
sudo apt update

# Do full upgrade of system
sudo apt full-upgrade -y

# Remove leftover packages and purge configs
sudo apt autoremove -y --purge

#Declare text which defines the lilbuddy service
pwd=`pwd`
lilbuddy="[Unit]
Description=A discord bot built for fun!
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=sudo sh $pwd/lilbuddy.sh

[Install]
WantedBy=multi-user.target"

echo "$lilbuddy" > lilbuddy.service

sudo cp lilbuddy.service.service /etc/systemd/system/
sudo systemctl start lilbuddy.service
sudo systemctl enable lilbuddy.service