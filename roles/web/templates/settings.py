{
    'ADMINS': (
        ('PBX admin }}', '{{ admin_email }}'),
    ),
    'ALLOWED_HOSTS': (
        '{{ pbx_hostname }}',
        'localhost',
    ),
    'FIREWALL_API_PORT': {{ firewall_api_port }},
    'PUBLISH_ENDPOINT': 'http://127.0.0.1:{{ web_local_port }}/publish',
    'SERVER_EMAIL': 'noreply@{{ pbx_hostname }}',
    'TIME_ZONE': '{{ timezone }}',
}
