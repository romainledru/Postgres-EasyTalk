from .exceptions_raise import *
from .manager import Manager
from local_settings_user import local_set, pg_items, pg_items_str
import datetime

class Table:

    def __init__(self,tb_name):

        self.tb_name = tb_name # related to postgresql

        self._tableCheck = self._tableCheck() # list of all tables already existing
        self.patron = {}
        if self.tb_name in self._tableCheck:
            self._extractPatron(self.tb_name)
        self.pattern = {
            'primary': None,
            'compulsory': None,
            'type': None,
        }
    
    def __str__(self):
        return 'public.' + self.tb_name
    
    def __transfert__(self): # Send DB-definition to an other class
        return self.patron

    #### INTERN METHODS ####

    ## MANAGER DB ##

    def _tableCheck(self):
        tables = []
        man = Manager(local_set['database'])
        answer = man.scan_database()
        man.shutdown_manager()
        for row in answer:
            tables.append(row[0]) # row[0] is where table name is stored
        return tables
    
    def _extractPatron(self, table):
        man = Manager(local_set['database'])
        answer = man.scan_table(table)
        for i in range(len(answer)):
            pattern = self._extractPattern(answer, i)
            self.patron[answer[i][0]] = pattern

    def _extractPattern(self, answer, row):
        pattern = {}

        if answer[row][1] == 'NO':
            pattern['compulsory'] = False
            pattern['primary'] = True
        elif answer[row][1] == 'YES':
            pattern['compulsory'] = True
            pattern['primary'] = False
        else:
            raise NameError("\n\n***{}*** -> compulsory output from DB not interpreted succesfully\n\n".format(answer[row][1]))
        # TODO Add a raise

        if answer[row][2] in pg_items.keys():
            for key, value in pg_items.items():
                if answer[row][2] == key:
                    pattern['type'] = value # transform <type> into accepted <type value> for a given sql language
        else:
            raise TypeError("\n\n***{}*** -> item type found which is not is not supported yet\n\n".format(answer[row][2]))

        return pattern

    def _activeManager(self, phrase):
        man = Manager(local_set['database'])
        man.interact_up(phrase)
        man.shutdown_manager()


    ## CHECK PACKAGE ##

    def _welcomeCheck(self, keyName, pattern):
        self._welcomeKeyCheck(keyName)
        self._welcomePatternCheck(pattern)


    def _welcomeKeyCheck(self, keyName):
        self._alreadyExist(keyName)
        self._isNotStr(keyName)
    
    def _alreadyExist(self, keyName):
        if keyName in self.patron.keys():
            raise AlreadyExist(keyName)
    
    def _isNotStr(self, keyName):
        if type(keyName) is not str:
            raise TypeError("\n\n***{}*** -> must be a STRING\n\n".format(keyName))


    def _welcomePatternCheck(self, pattern):
        self._patternFollowPattern(pattern)
        self._primaryShouldBeAlone(pattern)
    
    def _patternFollowPattern(self, pattern): # entry will be accepted only if it is in the accepted list
        accepted = ['primary', 'type', 'length', 'compulsory']
        for key in pattern.keys():
            if key not in accepted:
                raise KeyNotAccepted(key)
    
    def _primaryShouldBeAlone(self, pattern):
        if 'primary' in pattern.keys(): # if primary key is given from add
            if type(pattern['primary']) is not bool:
                raise TypeError
            if pattern['primary'] == True: # if primary key given is set to True
                for each in self.patron.keys(): # check in Table
                    if self.patron[each]['primary'] == True: # if there is already one primary key
                        raise PrimaryDouble(each) # raise error
        else:
            pattern['primary'] = False

    ## SET PACKAGE ##

    def _setPattern(self, pattern, typeCurrent):
        self._setType(pattern, typeCurrent) # check and set type from given pattern
        self._setCompulsory(pattern)
    
    def _setType(self, pattern, typeCurrent):
        pattern['type'] = typeCurrent # force to give the right type
    
    def _setCompulsory(self, pattern):
        if 'compulsory' not in pattern.keys():
            pattern['compulsory'] = False
        else:
            accepted = [True, False]
            if type(pattern['compulsory']) is not bool:
                raise TypeError
    
    def _setIdPrimaryIfNoOtherPrimary(self, idCurrent, patron): # If no primary given, 'id' should be primary
        isPrimary = False
        for item in patron.keys():
            if patron[item]['primary'] == True:
                isPrimary = True
                break
        if not isPrimary:
            patron[idCurrent]['primary'] = True

    ## SET WRITE BUILD ##

    def _checkIdKeyExist(self, patron):
        if 'id' in patron: # table should always have column 'id'
            idCurrent = 'id'
        elif 'ID' in patron:
            idCurrent = 'ID'
        elif 'Id' in patron:
            idCurrent = 'Id'
        else:
            pattern = {
                'length': 10,
            }
            self.add_serialField('id') # if no id given from user, force to give one
            idCurrent = 'id'
        self._setIdPrimaryIfNoOtherPrimary(idCurrent, patron) # If no primary given, 'id' should be primary as default

    def _typeFormat(self, keyName):
        attr = ''

        if self.patron[keyName]['type'] == 'serial':
            attr = 'SERIAL'
        elif self.patron[keyName]['type'].__name__ in pg_items_str.values():
            for key, value in pg_items_str.items():
                if self.patron[keyName]['type'].__name__ == value:
                    attr = key # transform <type value> from sql into accepted <type> for python
        else:
            raise TypeError("\n\n***{}*** -> item type found which is not is not supported yet\n\n".format(keyName))

        return attr


    #### PUBLIC METHODS ####

    def add_varcharField(self, keyName, pattern={}):
        self._welcomeCheck(keyName, pattern)
        self._setPattern(pattern, str)

        self.patron[keyName] = pattern
    
    def add_booleanField(self, keyName, pattern={}):
        self._welcomeCheck(keyName, pattern)
        self._setPattern(pattern, bool)

        self.patron[keyName] = pattern
    
    def add_intField(self, keyName, pattern={}):
        self._welcomeCheck(keyName, pattern)
        self._setPattern(pattern, int)
        
        self.patron[keyName] = pattern
    
    def add_floatField(self, keyName, pattern={}):
        self._welcomeCheck(keyName, pattern)
        self._setPattern(pattern, float)
        
        self.patron[keyName] = pattern
    
    def add_serialField(self, keyName='id', pattern={'primary':True}):
        self._welcomeCheck(keyName, pattern)
        self._setPattern(pattern, 'serial')

        self.patron[keyName] = pattern
    
    def add_datetimeField(self, keyName='datetime', pattern={}):
        self._welcomeCheck(keyName, pattern)
        self._setPattern(pattern, datetime.datetime)

        self.patron[keyName] = pattern
    

    def write_TABLE(self):
        self._checkIdKeyExist(self.patron)
        phrase = "CREATE TABLE {} (".format(self.tb_name) # except 'public.'
        for key in self.patron:
            phrase += key
            phrase += ' '
            typeFormat = self._typeFormat(key)
            phrase += typeFormat
            if self.patron[key]['compulsory']: # compulsory attrs
                phrase += ' NOT NULL'
            if self.patron[key]['primary']: # primary attrs
                phrase += ' PRIMARY KEY'
            phrase += ', '
        phrase = phrase [:-2]
        phrase += ')'
        phrase += ';'

        self._activeManager(phrase)
        print('CREATE succesfull')
