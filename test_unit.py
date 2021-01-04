import pytest
from exceptions_raise import *

### TABLE ###

from table import Table

class test_Table:

    def test_tableCreate(self):
        db = Table("table1")
        db.add_varcharField("varChar1", 300)
        db.add_varcharField("varChar2", 50)
        db.add_booleanField("bool1")
        db.add_intField("int1")
        db.add_floatField("float1")
        output = db.create_TABLE()

        answer = 'CREATE TABLE table1 (varChar1 varchar(255),varChar2 varchar(50),bool1 boolean,int1 int,float1 float)'
        assert output == answer
    
### INSERT ###

from insert import Insert

class test_Insertt:

    def test_Insert(self):
        db = Table("table1")
        db.add_varcharField("varChar1", 300)
        db.add_varcharField("varChar2", 50)
        db.add_booleanField("bool1")
        db.add_intField("int1")
        db.add_floatField("float1")
        table = db.create_TABLE()

        insert = Insert(db)
        entry = {
            'varChar1': 'hello1',
            'varChar2': 'hello2',
            'bool1': True,
            'int1': 35,
            'float1': 40.14,
        }
        output = insert.write_ENTRY(entry)

        answer = 'INSERT INTO table1 (varChar1,varChar2,bool1,int1,float1) VALUES (hello1,hello2,True,35,40.14)'
        assert output == answer
