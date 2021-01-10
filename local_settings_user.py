## SETTINGS TO BE CHANGED FOR USER

are_you_admin = True # CHANGEME

if are_you_admin:
    from local_settings_admin import local_set
else:
    local_set = {
        'host': 'CHANGEME',
        'port': 'CHANGEME',
        'user': 'CHANGEME',
        'password': 'CHANGEME',
    }
