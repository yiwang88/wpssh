#!/usr/bin/env bash

echo "Setup openrc ..." && openrc && touch /run/openrc/softlevel
echo Starting ssh service...
rc-service sshd start

cp /opt/resolv.conf /etc/resolv.conf
python /opt/app/main.py
