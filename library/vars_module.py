# -*- coding: utf-8 -*-

"""Example ansible module which accepts two parameters: backup_dir and path"""

##############################################################################
# -> http://ndemengel.github.io/2015/01/20/ansible-modules-and-action-plugins/
##############################################################################

# this line must be written exactly that way,
# as Ansible will replace it with the "imported" code
from ansible.module_utils.basic import AnsibleModule


# Ansible module documentation:
#    https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html#developing-modules-general
#

def run_module():
    global module
    module = AnsibleModule(
        argument_spec={
            'backup_dir': { 'required': True, 'type': 'str' },
            'path': { 'required': True, 'type': 'str' }
        },
        supports_check_mode=False
    )

    args = module.params
    # [..] check for early return reasons

    result = {"foo": "bar", "apple": "banana",}
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
