from .exceptions_raise import *
from .manager import Manager
from .nomenclatur import pg_items, pg_items_str
import datetime

# *******************************************************************

class Table:

    def __init__(self, db_name, tb_name):

        self.tb_name = tb_name
        self.db_name = db_name

        self._tableCheck = self._tableCheck() # list of all tables already existing in database
        self.patron = {}
        if self.tb_name in self._tableCheck:
            self._extractPatron(self.tb_name)
        self.pattern = {
            'primary': None,
            'compulsory': None,
            'type': None,
        }

    def __str__(self):
        # 'public.' added because of the PostgreSQL syntax
        # TODO pay attention for next SQL (MySQL,..) if there is also this 'publci
        return 'public.' + self.tb_name
    
    def __transfert__(self):
        # Send DB-definition to an other class
        return self.patron
    
    def get_db_name(self):
        return self.db_name
    
    def get_tb_name(self):
        return self.tb_name

# *******************************************************************

    #### INTERN METHODS ####

# *******************************************************************

    ## MANAGER DB ##

    def _tableCheck(self):
        # check for all tables in DB
        tables = []
        man = Manager(self.db_name)
        answer = man.scan_database()
        man.shutdown_manager()
        for row in answer:
            tables.append(row[0]) # row[0] is where table name is stored
        return tables
    
    def _extractPatron(self, table):
        # check for labels (columns names) in table
        man = Manager(self.db_name)
        answer = man.scan_table(table)
        for i in range(len(answer)):
            pattern = self._extractPattern(answer, i)
            self.patron[answer[i][0]] = pattern

    def _extractPattern(self, answer, row):
        # check for definition of a label (column name) in table
        pattern = {}
        if answer[row][0] == 'id':
            pattern['primary'] = True
            pattern['compulsory'] = False
        else:
            pattern['primary'] = False
            if answer[row][1] == 'NO':
                pattern['compulsory'] = True
            elif answer[row][1] == 'YES':
                pattern['compulsory'] = False
            else:
                raise NameError("\n\n***{}*** -> compulsory output from DB not interpreted succesfully\n\n".format(answer[row][1]))

        if answer[row][2] in pg_items.keys():
            for key, value in pg_items.items():
                if answer[row][2] == key:
                    pattern['type'] = value # transform <type> into accepted <type value> for a given sql language
        else:
            raise TypeError("\n\n***{}*** -> item type found which is not is not supported yet\n\n".format(answer[row][2]))

        return pattern

    def _activeManager(self, phrase):
        # send function (to DB)
        man = Manager(self.db_name)
        man.interact_up(phrase)
        man.shutdown_manager()

# *******************************************************************

    ## CHECK PACKAGE ##

    def _welcomeCheck(self, keyName, pattern):
        self._welcomeKeyCheck(keyName)
        self._welcomePatternCheck(pattern)


    # CHECK KEY #

    def _welcomeKeyCheck(self, keyName):
        self._alreadyExist(keyName)
        self._isNotStr(keyName)
    
    def _alreadyExist(self, keyName):
        if keyName in self.patron.keys():
            raise AlreadyExist(keyName)
    
    def _isNotStr(self, keyName):
        if type(keyName) is not str:
            raise TypeError("\n\n***{}*** -> must be a STRING\n\n".format(keyName))

    # CHECK PATTERN #

    def _welcomePatternCheck(self, pattern):
        self._patternFollowPattern(pattern)
        self._primaryShouldBeAlone(pattern)
    
    def _patternFollowPattern(self, pattern):
        # entry will be accepted only if it is in the accepted list
        accepted = ['primary', 'type', 'compulsory']
        for key in pattern.keys():
            if key not in accepted:
                raise KeyNotAccepted(key)
    
    def _primaryShouldBeAlone(self, pattern):
        if 'primary' in pattern.keys(): # if primary key is set from user entry -> checks has to be made
            if type(pattern['primary']) is not bool:
                raise TypeError
            if pattern['primary'] == True: # if primary key given is set to True
                for each in self.patron.keys(): # check in Table
                    if self.patron[each]['primary'] == True: # if there is already one primary key
                        raise PrimaryDouble(each) # raise error
        else:
            pattern['primary'] = False

# *******************************************************************

    ## SET PACKAGE ##

    def _setPattern(self, pattern, typeCurrent):
        # when pattern is not given (or partially), then we have to complete it
        self._setType(pattern, typeCurrent)
        self._setCompulsory(pattern)
    
    def _setType(self, pattern, typeCurrent):
        pattern['type'] = typeCurrent # force to give the right type
    
    def _setCompulsory(self, pattern):
        if 'compulsory' not in pattern.keys():
            pattern['compulsory'] = True
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

# *******************************************************************

    ## SET BUILD ##

    def _checkIdKeyExist(self, patron):
        # table should always have column 'id'
        # TODO if elif elif else could be improved with str.lower()
        if 'id' in patron:
            idCurrent = 'id'
        elif 'ID' in patron:
            idCurrent = 'ID'
        elif 'Id' in patron:
            idCurrent = 'Id'
        else:
            self.add_serialField('id') # if no id given from user, force to give one
            idCurrent = 'id'
        self._setIdPrimaryIfNoOtherPrimary(idCurrent, patron) # If no primary given, 'id' should be primary as default

    def _typeFormat(self, keyName):
        attr = ''

        if self.patron[keyName]['type'] == 'serial': # 'serial' is no type specific. This is why there is a single if
            attr = 'SERIAL'
        elif self.patron[keyName]['type'].__name__ in pg_items_str.values(): # the rest is type specific. We can check in loop
            for key, value in pg_items_str.items():
                if self.patron[keyName]['type'].__name__ == value:
                    attr = key # transform <type value> from sql into accepted <type> for python
        else:
            raise TypeError("\n\n***{}*** -> item type found which is not is not supported yet\n\n".format(keyName))

        return attr

# *******************************************************************

    #### PUBLIC METHODS ####

# *******************************************************************

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
    
    def add_datetimeField(self, keyName='datetime', pattern={'compulsory': False}):
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
                if self.patron[key]['type'] != 'serial':
                    phrase += ' NOT NULL'
            else:
                if self.patron[key]['type'] == datetime.datetime: # trigger the default not compulsory datetime
                    phrase += ' DEFAULT NOW()' # and allow default now() for 'automatic created_at'
            if self.patron[key]['primary']: # primary attrs
                phrase += ' PRIMARY KEY'
            phrase += ', '
        phrase = phrase [:-2]
        phrase += ')'
        phrase += ';'

        self._activeManager(phrase)
        print('CREATE succesfull')

    def drop_TABLE(self):
        man = Manager(self.db_name)
        man.drop_table(self.tb_name)
        man.shutdown_manager()