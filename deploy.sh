#!/bin/bash

# Update repos
sudo apt update

# Do full upgrade of system
sudo apt full-upgrade -y

# Remove leftover packages and purge configs
sudo apt autoremove
#sudo apt autoremove -y --purge

#Create .env file if not exists
if [ ! -f ".env" ] ; then
    env="
    TOKEN=

    DB_USER=
    DB_PASS=
    DB_HOST=
    DB_DATABASE=
    DB_PORT="

    echo "$env" > .env

    echo "Please fill out the information in the newly created .env file before proceeding."

    exit

#Build the docker image
sudo docker build -t lilbuddy .

#Declare text which defines the lilbuddy service
pwd=`pwd`
lilbuddy="[Unit]
Description=Lil' Buddy Discord Bot
After=multi-user.target

[Service]
Type=simple
Restart=always

ExecStart=/usr/bin/sudo docker run lilbuddy

[Install]
WantedBy=multi-user.target"

#Create the service
echo "$lilbuddy" > lilbuddy.service

sudo cp lilbuddy.service /etc/systemd/system/
sudo systemctl start lilbuddy.service
sudo systemctl enable lilbuddy.service

rm lilbuddy.service

echo "Successfully created lil-buddy service!"