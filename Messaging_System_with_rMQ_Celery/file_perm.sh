#!/bin/bash

sudo touch /var/log/messaging_system.log
sudo chown $USER:$USER /var/log/messaging_system.log
sudo chmod 644 /var/log/messaging_system.log
