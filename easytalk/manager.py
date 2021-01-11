import psycopg2
import json

#from local_settings_user import *
from .exceptions_raise import UnabletoConnect

# *******************************************************************

def jsonDown():
    with open('easytalk/credentials.json', 'r') as f:
        dataJson = f.read()
        data = json.loads(dataJson)
    return data


class Manager:
    def __init__(self, db):
        self.db = db

        credentials = jsonDown()
        try:
            self.connect = psycopg2.connect(host = credentials['host'],
                database = self.db,
                user = credentials['user'],
                password = credentials['password'])
        except:
            raise UnabletoConnect(self.db)
        
        self.cursor = self.connect.cursor()

    def scan_database(self):
        self.cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND  schemaname != 'information_schema';")
        answer = self.cursor.fetchall()
        return answer

    def scan_table(self, table):
        self.cursor.execute("SELECT column_name, is_nullable, data_type FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{}';".format(table))
        answer = self.cursor.fetchall()
        return answer

    def interact_up(self, phrase):
        # write something in DB
        self.cursor.execute(phrase)
        self.connect.commit()

    def interact_down(self, phrase):
        # read something in DB
        self.cursor.execute(phrase)
        answer = self.cursor.fetchall()
        return answer
    
    def shutdown_manager(self):
        self.cursor.close()
        self.connect.close()
