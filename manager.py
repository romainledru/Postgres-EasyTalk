import psycopg2
from local_settings import *


class Manager:
    def __init__(self, db):
        self.db = db
        con = psycopg2.connect(host = 'localhost',
            database = self.db,
            user = 'postgres',
            password = "postgres")





### DRAFT / SANDBOX

con = psycopg2.connect(host = 'localhost',
    database = 'easyTalk-db',
    user = 'postgres',
    password = "postgres")

cur = con.cursor()

#cur.execute('CREATE TABLE test (id integer)')
#con.commit()


#****
#cur.execute('INSERT INTO public.test (id) VALUES (2)')
#con.commit()


#****
#cur.execute('SELECT * FROM public.test')
#rows = cur.fetchall()
#for row in rows:
#    print(row)

#****
# to find all existing (public) tables
cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND  schemaname != 'information_schema';")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
con.close()
