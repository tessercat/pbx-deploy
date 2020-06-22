""" Ansible module to find IPv4 and IPv6 addresses for a hostname. """
import socket
from ansible.module_utils.basic import AnsibleModule


def _get_addr(hostname, family):
    """ Return a single address based on family. """
    try:
        addrs = socket.getaddrinfo(
            hostname, None,
            type=socket.IPPROTO_IP,
            family=family
        )
    except socket.gaierror as err:
        raise AssertionError(err)
    try:
        return addrs[0][4][0]
    except IndexError:
        raise AssertionError('No address found for family %d' % family)


def main():
    """ Init and run module. """
    module = AnsibleModule(argument_spec={
        'hostname': {'required': True},
    })
    exit_json = {
        'changed': False,
        'failed': False,
        'failure': None
    }
    try:
        exit_json['ipv4_addr'] = _get_addr(
            module.params['hostname'],
            socket.AddressFamily.AF_INET,
        )
        exit_json['ipv6_addr'] = _get_addr(
            module.params['hostname'],
            socket.AddressFamily.AF_INET6,
        )
    except (AssertionError) as err:
        exit_json['failed'] = True
        exit_json['failure'] = repr(err)
    module.exit_json(**exit_json)


if __name__ == '__main__':
    main()
