## This is the import manager ##

from easytalk.table import Table
from easytalk.insert import Insert
from easytalk.read import Read
from easytalk.delete import Delete
from easytalk.manager import Manager
from easytalk.exceptions_raise import *

import datetime
import psycopg2 # psycopg2-binary is used. TODO change in psycopg2

__version__ = "0.1.0"