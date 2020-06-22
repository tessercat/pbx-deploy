{
    'ADMINS': (
        ('PBX admin }}', '{{ admin_email }}'),
    ),
    'ALLOWED_HOSTS': (
        '{{ pbx_hostname }}',
        'localhost',
    ),
    'ALLOWED_ORIGINS': (
        'https://{{ pbx_hostname }}:443',
    ),
    'COTURN_TLS_PORT': {{ coturn_listening_port }},
    'FIREWALL_API_PORT': {{ firewall_api_port }},
    'SERVER_EMAIL': 'noreply@{{ pbx_hostname }}',
    'TIME_ZONE': '{{ timezone }}',
}
