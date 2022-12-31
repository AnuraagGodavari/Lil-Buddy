#!/bin/bash

# Update repos
sudo apt update

# Do full upgrade of system
sudo apt full-upgrade -y

# Remove leftover packages and purge configs
sudo apt autoremove
#sudo apt autoremove -y --purge

#Create .env file
env="
TOKEN=

DB_USER=
DB_PASS=
DB_HOST=
DB_DATABASE=
DB_PORT="

echo "$env" > .env

#Declare text which defines the lilbuddy service
pwd=`pwd`
lilbuddy="[Unit]
Description=Lil' Buddy Discord Bot
After=multi-user.target

[Service]
Type=simple
Restart=always

ExecStart=python3 $pwd

[Install]
WantedBy=multi-user.target"

echo "$lilbuddy" > lilbuddy.service

sudo cp lilbuddy.service /etc/systemd/system/
sudo systemctl start lilbuddy.service
sudo systemctl enable lilbuddy.service
sudo systemctl stop lilbuddy.service
rm lilbuddy.service

echo "Created service. Please fill information in the newly created .env file, then run the command \"sudo systemctl start lilbuddy.service\"."