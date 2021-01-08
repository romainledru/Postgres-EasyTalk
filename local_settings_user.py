import datetime

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
        'database': 'CHANGEME'
    }


## LOCAL POSTGRESQL DEFINITION

pg_items = {
    'serial': 'serial',
    'text': str,
    'integer': int,
    'real': float,
    'boolean': bool,
    'timestamp with time zone': datetime.datetime,
}

pg_items_str = {
    'serial': 'serial',
    'text': 'str',
    'integer': 'int',
    'real': 'float',
    'boolean': 'bool',
    'timestamp with time zone': 'datetime',
}

## LOCAL MYSQL DEFINITION

## LOCAL SQLITE DEFINITION

## ...