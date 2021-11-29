#!/bin/bash

# read the username with default value...
# see -> https://stackoverflow.com/a/31938017/667301
DEFAULT=$USER
read -p "Ansible SSH username (default: $DEFAULT): " ansible_username
ansible_username="${ansible_username:-${DEFAULT}}"
rm ./ansible.log
ansible-playbook -u $ansible_username --ask-pass --flush-cache -i inventory.ini cisco_play.yml
