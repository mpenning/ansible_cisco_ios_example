# Example Ansible settings for Cisco IOS devices

- Edit inventory.ini with your own devices
- This ansible script requires Username / Password auth
  - username and password are captured in `./run_ansible.sh`
  - No ssh public-key authentication is configured in this example
- Look at `./filter_plugins` for custom filter examples
- Look at `./library` for a custom ansible module
