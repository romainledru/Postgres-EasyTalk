import pytest
from easytalk import *

### TABLE ###

class Test_Table:
    
    def test_create(self):

        table = Table('easyTalk-db','tableTest')
        table.write_TABLE()
        tables = []
        man = Manager('easyTalk-db')
        answer = man.scan_database()
        man.shutdown_manager()
        if table in answer:
            assert True
        table.drop_TABLE() # delete table at the end of the test



"""
### TABLE ###

from easytalk.table import Table

class test_Table:

    def test_tableCreate(self):
        pattern1 = {
            'length': 300,
        }
        pattern2 = {
            'compulsory': False,
            'length': 50,
        }
        db = Table("table1")
        db.add_varcharField("varChar1", pattern1)
        db.add_varcharField("varChar2", pattern2)
        db.add_booleanField("bool1")
        db.add_intField("int1")
        db.add_floatField("float1")
        output = db.write_TABLE()

        answer = 'CREATE TABLE table1 (varChar1 VARCHAR(255), varChar2 VARCHAR(50), bool1 BOOLEAN, int1 INT, float1 REAL, id INT);'
        assert output == answer
    
### INSERT ###

from easytalk.insert import Insert

class test_Insert:

    def test_Insert(self):
        db = Table("table1")
        db.add_varcharField("varChar1")
        db.add_varcharField("varChar2")
        db.add_booleanField("bool1")
        db.add_intField("int1")
        db.add_floatField("float1")
        output = db.write_TABLE()

        insert = Insert(db)
        entry = {
            'varChar1': 'hello1',
            'varChar2': 'hello2',
            'bool1': True,
            'int1': 35,
            'float1': 40.14,
        }
        output = insert.write_ENTRY(entry)

        answer = 'INSERT INTO table1 (varChar1, varChar2, bool1, int1, float1, id) VALUES (hello1, hello2, True, 35, 40.14, None);'
        assert output == answer

### SELECT ###

from easytalk.select import Read

class test_Select:

    def test_Select(self):
        t = Table('tableTest')
        t.add_varcharField('name')
        t.add_intField('price')
        t.add_booleanField('buyORnot')

        s = Read(t)
        p = {
            'name': 'jouet',
            'price': 35,
        }
        l = ['name', 'buyORnot']
        output = s.find_filter(p, l)

        answer = "SELECT name, buyORnot FROM tableTest WHERE (name='jouet') AND (price=35);"
        assert output == answer
"""