{
    'ADMINS': (
        ('PBX admin }}', '{{ admin_email }}'),
    ),
    'COTURN_LISTENING_PORT': {{ coturn_listening_port }},
    'FIREWALL_API_PORT': {{ firewall_api_port }},
    'PBX_HOSTNAME': '{{ pbx_hostname }}',
    'SERVER_EMAIL': 'noreply@{{ pbx_hostname }}',
    'TIME_ZONE': '{{ timezone }}',
    'VERTO_PORT': {{ freeswitch_verto_port }},
}
