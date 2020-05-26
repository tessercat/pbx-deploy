{
    'ADMINS': (
        ('PBX admin }}', '{{ admin_email }}'),
    ),
    'ALLOWED_HOSTS': (
        '{{ pbx_hostname }}',
        'localhost',
    ),
    'FIREWALL_API_PORT': {{ firewall_api_port }},
    'SERVER_EMAIL': 'noreply@{{ pbx_hostname }}',
    'TIME_ZONE': '{{ timezone }}',
}
