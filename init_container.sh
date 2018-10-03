#!/bin/sh

echo "Starting SSH ..."
rc-service sshd start

cp /opt/resolv.conf /etc/resolv.conf
python /opt/app/main.py
