#!/bin/bash

touch /var/log/messaging_system.log
chown $USER:$USER /var/log/messaging_system.log
chmod 644 /var/log/messaging_system.log
