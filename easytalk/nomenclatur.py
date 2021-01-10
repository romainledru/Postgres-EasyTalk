import datetime

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