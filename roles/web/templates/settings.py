{
    'ADMINS': (
        ('PBX admin }}', '{{ admin_email }}'),
    ),
    'PBX_HOSTNAME': '{{ pbx_hostname }}',
    'SERVER_EMAIL': 'noreply@{{ pbx_hostname }}',
    'TIME_ZONE': '{{ timezone }}',
    'FIREWALL_PORT': {{ firewall_port }},
    'STUN_PORT': {{ stun_port }},
    'VERTO_PORT': {{ freeswitch_verto_port }},
}
