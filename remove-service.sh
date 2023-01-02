#!/bin/bash

#Disable the systemd service
sudo systemctl stop lilbuddy.service
sudo systemctl disable lilbuddy.service

#Remove the docker image
sudo docker system prune -a

#Remove the systemd service
sudo rm /etc/systemd/system/lilbuddy.service

sudo systemctl daemon-reload
sudo systemctl reset-failed

echo "Removed lilbuddy.service"

