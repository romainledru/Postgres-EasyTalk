import psycopg2
from local_settings import *


class Manager:
    def __init__(self, db):
        self.db = db

        self.connect = psycopg2.connect(host = local_set['host'],
            database = self.db,
            user = local_set['user'],
            password = local_set['password'])
        
        self.cursor = self.connect.cursor()

    def scan_database(self):
        self.cursor.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND  schemaname != 'information_schema';")
        answer = self.cursor.fetchall()
        return answer

    def scan_table(self, table):
        self.cursor.execute("SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{}';".format(table))
        answer = self.cursor.fetchall()
        return answer

    def interact_up(self, phrase):
        self.cursor.execute(phrase)
        self.cursor.commit()

    def interact_down(self, phrase):
        self.cursor.execute(phrase)
        answer = self.cursor.fetchall()
        return answer
    
    def shutdown_manager(self):
        self.cursor.close()
        self.connect.close()
