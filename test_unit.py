import pytest
from easytalk import *
from easytalk.exceptions_raise import UnitError

### TABLE ###

class Test_Table:

    def test_create_phrase(self):

        p = {
            'compulsory': False,
        }
        table = Table('easyTalk-db','tabletest')
        table.add_serialField()
        table.add_datetimeField()
        table.add_varcharField('name')
        table.add_intField('price')
        table.add_booleanField('to_buy', p)
        table.write_TABLE()

        ist = table.phrase_test_unit
        soll = "CREATE TABLE tabletest (id SERIAL PRIMARY KEY, datetime timestamp with time zone DEFAULT NOW(), name text NOT NULL, price integer NOT NULL, to_buy boolean);"
        
        table.drop_TABLE()
        
        assert soll == ist

    def test_create(self):

        table = Table('easyTalk-db','tabletest')
        table.write_TABLE()
        tables = []
        man = Manager('easyTalk-db')
        answer = man.scan_database()
        man.shutdown_manager()
        table.drop_TABLE()

        if table in answer:
            assert True
        
    def test_create_containsId(self):

        table = Table('easyTalk-db','tabletest')
        table.write_TABLE()
        tablePick = Table('easyTalk-db','tabletest')

        try:
            if 'id' in tablePick.patron:
                assert True
        except:
            raise UnitError('id','not found in patron')
        finally:
            tablePick.drop_TABLE()

    ## TEST SERIAL ##
    def test_create_addSerialId(self):

        nameId = 'id'

        table = Table('easyTalk-db','tabletest')
        table.add_serialField(nameId)
        table.write_TABLE()
        tablePick = Table('easyTalk-db','tabletest')
        try:
            if nameId not in tablePick.patron:
                raise
        except:
            raise UnitError(nameId,'not found in patron')
        finally:
            tablePick.drop_TABLE()
        
        assert True # if no problems occurs until here

    def test_create_serial_pattern(self):

        nameId = 'id'
        table = Table('easyTalk-db','tabletest')
        table.add_serialField()
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': False,
            'primary': True,
            'type': int,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')

    ## TEST DATETIME ##
    def test_create_addDatetime(self):

        nameId = 'created_at'

        table = Table('easyTalk-db','tabletest')
        table.add_datetimeField(nameId)
        table.write_TABLE()
        tablePick = Table('easyTalk-db','tabletest')
        try:
            if nameId not in tablePick.patron:
                raise
        except:
            raise UnitError(nameId,'not found in patron')
        finally:
            tablePick.drop_TABLE()
        
        assert True # if no problems occurs until here

    def test_create_datetime_pattern(self):

        nameId = 'created_at'
        table = Table('easyTalk-db','tabletest')
        table.add_datetimeField(nameId)
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': False,
            'primary': False,
            'type': datetime.datetime,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')

    ## TEST VARCHAR ##
    def test_create_addVarchar(self):

        nameId = 'varchar1'

        table = Table('easyTalk-db','tabletest')
        table.add_varcharField(nameId)
        table.write_TABLE()
        tablePick = Table('easyTalk-db','tabletest')
        try:
            if nameId not in tablePick.patron:
                raise
        except:
            raise UnitError(nameId,'not found in patron')
        finally:
            tablePick.drop_TABLE()
        
        assert True # if no problems occurs until here

    def test_create_varchar_pattern(self):

        nameId = 'varchar1'
        table = Table('easyTalk-db','tabletest')
        table.add_varcharField(nameId)
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': True,
            'primary': False,
            'type': str,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')

    ## TEST INT ##
    def test_create_addInt(self):

        nameId = 'int1'

        table = Table('easyTalk-db','tabletest')
        table.add_intField(nameId)
        table.write_TABLE()
        tablePick = Table('easyTalk-db','tabletest')
        try:
            if nameId not in tablePick.patron:
                raise
        except:
            raise UnitError(nameId,'not found in patron')
        finally:
            tablePick.drop_TABLE()
        
        assert True # if no problems occurs until here

    def test_create_int_pattern(self):

        nameId = 'int1'
        table = Table('easyTalk-db','tabletest')
        table.add_intField(nameId)
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': True,
            'primary': False,
            'type': int,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')

    ## TEST FLOAT ##
    def test_create_addFloat(self):

        nameId = 'float1'

        table = Table('easyTalk-db','tabletest')
        table.add_floatField(nameId)
        table.write_TABLE()
        tablePick = Table('easyTalk-db','tabletest')
        try:
            if nameId not in tablePick.patron:
                raise
        except:
            raise UnitError(nameId,'not found in patron')
        finally:
            tablePick.drop_TABLE()
        
        assert True # if no problems occurs until here

    def test_create_float_pattern(self):

        nameId = 'float1'
        table = Table('easyTalk-db','tabletest')
        table.add_floatField(nameId)
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': True,
            'primary': False,
            'type': float,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')

    ## TEST BOOL ##
    def test_create_addBool(self):

        nameId = 'bool1'

        table = Table('easyTalk-db','tabletest')
        table.add_booleanField(nameId)
        table.write_TABLE()
        tablePick = Table('easyTalk-db','tabletest')
        try:
            if nameId not in tablePick.patron:
                raise
        except:
            raise UnitError(nameId,'not found in patron')
        finally:
            tablePick.drop_TABLE()
        
        assert True # if no problems occurs until here

    def test_create_boolean_pattern(self):

        nameId = 'bool1'
        table = Table('easyTalk-db','tabletest')
        table.add_booleanField(nameId)
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': True,
            'primary': False,
            'type': bool,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')

    ## ALTERED COMPULSORY ##
    def test_create_compulsory_altered_pattern(self):

        nameId = 'bool1'
        p = {
            'compulsory': False
        }
        table = Table('easyTalk-db','tabletest')
        table.add_booleanField(nameId, p)
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': False,
            'primary': False,
            'type': bool,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')

    ## ALTERED TYPE ##
    def test_create_type_altered_pattern(self):

        nameId = 'bool1'
        p = {
            'type': int
        }
        table = Table('easyTalk-db','tabletest')
        table.add_booleanField(nameId, p)
        table.write_TABLE()

        tablePick = Table('easyTalk-db','tabletest')

        pattern = {
            'compulsory': True,
            'primary': False,
            'type': bool,
        }
        problemTag = ''
        try:
            for key, value in tablePick.patron[nameId].items():
                if tablePick.patron[nameId][key] != pattern[key]:
                    problemTag = '{},{}'.format(key, value)
        except:
            raise UnitError(problemTag, 'error in try')
        finally:
            tablePick.drop_TABLE()
        
        if problemTag == '':
            assert True
        else:
            raise UnitError(problemTag, 'error in pattern')


class Test_Insert:

    def test_insert_phrase(self):

        p = {
            'compulsory': False,
        }
        table = Table('easyTalk-db','tabletest')
        table.add_serialField()
        table.add_datetimeField()
        table.add_varcharField('name')
        table.add_intField('price')
        table.add_booleanField('to_buy')
        table.add_booleanField('to_buy_nc', p)
        table.write_TABLE()
        
        tablePick = Table('easyTalk-db','tabletest')
        insert = Insert(tablePick)
        entry = {
            'name': 'name1',
            'price': 30,
            'to_buy': True,
        }
        insert.write_ENTRY(entry)
        
        ist = insert.phrase_test_unit
        soll = "INSERT INTO tabletest (name, price, to_buy) VALUES ('name1', 30, True);"
        
        table.drop_TABLE()
        
        assert soll == ist

    def test_insert_compulsoryMissing(self):

        table = Table('easyTalk-db','tabletest')
        table.add_varcharField('name') # 'name' is set as compulsory=True
        table.add_intField('price')
        table.add_booleanField('to_buy')
        table.write_TABLE()
        
        tablePick = Table('easyTalk-db','tabletest')
        insert = Insert(tablePick)
        entry = { # 'name' is not given for the test
            'price': 30,
            'to_buy': True,
        }

        try:
            insert.write_ENTRY(entry)
            raise UnitError(entry, "should raise compulsory=True for 'name', but didn't")
        except CompulsoryEntry:
            assert True
        finally:
            table.drop_TABLE()