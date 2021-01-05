import pytest
from exceptions_raise import *

### TABLE ###

from table import Table

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

        answer = 'CREATE TABLE table1 (varChar1 varChar(255), varChar2 varChar(50), bool1 bool, int1 int, float1 float, id int)'
        assert output == answer
    
### INSERT ###

from insert import Insert

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

        answer = 'INSERT INTO table1 (varChar1, varChar2, bool1, int1, float1, id) VALUES (hello1, hello2, True, 35, 40.14, None)'
        assert output == answer

### SELECT ###

from select import Select

class test_Select:

    def test_Select(self):
        t = Table('tableTest')
        t.add_varcharField('name')
        t.add_intField('price')
        t.add_booleanField('buyORnot')

        s = Select(t)
        p = {
            'name': 'jouet',
            'price': 35,
        }
        l = ['name', 'buyORnot']
        output = s.find_filter(p, l)

        answer = "SELECT name, buyORnot FROM tableTest WHERE (name='jouet') AND (price=35)"
        assert output == answer