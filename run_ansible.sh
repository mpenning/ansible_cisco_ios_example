#!/bin/bash

# Install juniper ansible infra
ansible-galaxy install juniper.junos
ansible-galaxy collection install ansible.netcommon

# read the username with default value...
# see -> https://stackoverflow.com/a/31938017/667301
DEFAULT=$USER
read -p "Ansible SSH username (default: $DEFAULT): " ansible_username
ansible_username="${ansible_username:-${DEFAULT}}"
rm ./ansible.log
ansible-playbook -u $ansible_username --ask-pass -T 5 -f 25 -i inventory.ini cisco_play.yml
