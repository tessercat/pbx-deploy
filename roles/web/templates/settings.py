{
    'ADMINS': (
        ('Peers admin }}', '{{ admin_email }}'),
    ),
    'ALLOWED_HOSTS': (
        '{{ peers_hostname }}',
        'localhost',
    ),
    'FIREWALL_API_PORT': {{ firewall_api_port }},
    'SERVER_EMAIL': 'noreply@{{ peers_hostname }}',
    'TIME_ZONE': '{{ timezone }}',
}
