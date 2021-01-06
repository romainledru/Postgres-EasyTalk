from exceptions_raise import *


class Table:

    def __init__(self,db_name):

        self.db_name = db_name

        self._tableCheck = self._tableCheck() # list of all tables already existing
        if self.db_name not in self._tableCheck:
            self.patron = {}
        else:
            pass # TODO define self.patron from existing table
        self.pattern = {
            'primary': None,
            'length': None,
            'compulsory': None,
            'type': None,
        }
    
    def __str__(self):
        return self.db_name
    
    def __transfert__(self): # Send DB-definition to an other class
        return self.patron

    #### INTERN METHODS ####

    ## CHECK PACKAGE ##

    def _tableCheck(self):
        # TODO Check for tables already existing
        return []

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
        self._setLength(pattern) # check and define length from given pattern
        self._setCompulsory(pattern)

    def _setLength(self, pattern):
        if pattern['type'] == str: # length is useful only for varChar entry
            if 'length' in pattern.keys():
                if type(pattern['length']) is not int:
                    raise TypeError 
                if pattern['length'] > 255:
                    pattern['length'] = 255
            else:
                pattern['length'] = 255
        else:
            pattern['length'] = None # for other entry types, length is kept as None
    
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
            self.add_intField('id', pattern)
            idCurrent = 'id'
        self._setIdPrimaryIfNoOtherPrimary(idCurrent, patron) # If no primary given, 'id' should be primary as default

    def _typeFormat(self, key):
        attr = ''
        attrs = ['bool', 'int', 'float']
        if self.patron[key]['type'].__name__ == 'str':
            attr = 'VARCHAR({})'.format(self.patron[key]['length'])
        elif self.patron[key]['type'].__name__ == 'bool':
            attr = 'BOOLEAN'
        elif self.patron[key]['type'].__name__ == 'int':
            attr = 'INT'
        elif self.patron[key]['type'].__name__ == 'float':
            attr = 'REAL'
            #attr = self.patron[key]['type'].__name__
        else:
            raise TypeError("\n\n***{}*** -> has a wrong Type !\n\n".format(key))
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
    

    def write_TABLE(self):
        self._checkIdKeyExist(self.patron)
        phrase = "CREATE TABLE {} (".format(self.db_name)
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
        return phrase
