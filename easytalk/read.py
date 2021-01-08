from .exceptions_raise import *
from .table import Table
from .insert import Insert
from .manager import Manager
from local_settings_user import local_set

class Read:
    def __init__(self, table):
        self.table = table
        if isinstance(self.table, Table):
            self.patron = self.table.__transfert__() # Load DB-definition from Table-class
        else:
            raise TableLinkFailed(self.table)
    
    def __str__(self):
        return self.table


    ### INTERN METHODS ###

    ## MANAGER DB ##

    def _activeManager(self, phrase):
        man = Manager(local_set['database'])
        answer = man.interact_down(phrase)
        man.shutdown_manager()
        return answer


    ## CHECK PACKAGE ##

    def _welcomeCheck(self, entry): # TODO _welcomeCheck is almost the same as in insert.py AND delete.py. Maybe I can dedicate the checks in a special file
        if not isinstance(entry, dict):
            raise TypeError
        if entry != {}:
            for key, value in entry.items():
                self._isUnknownEntry(key)
                self._isTypeValueCorrect(key, value)

    def _isUnknownEntry(self, key):
        if key not in self.patron.keys() and key != '*':
            raise WrongEntry(key)
    
    def _isTypeValueCorrect(self, key, value):
        if not isinstance(value, self.patron[key]['type']):
            raise TypeError("\n\n***{}: {}*** -> has a wrong Type !\n\n".format(key, value))


    def _welcomeShowCheck(self, shows):
        for show in shows:
            self._isUnknownEntry(show)

    
    def _welcomeAttrsCheck(self, attrs): # TODO check the attrs (not definded yet but should be distinct, orderby, direction ...)
        pass

    ## CONTAINER BUILD ##

    def _createBuild(self, shows, entry, attrs):
        entryMod = self._alterEntry(entry)

        containerBuild = {
            'show': shows,
            'entry': entryMod,
            'attrs': attrs,
        }
        return containerBuild
    
    def _alterEntry(self, entry): # if entry is a str, it should appear on query (name='jouet') and not (name=jouet)
        entryMod = {}
        for key, value in entry.items():
            if isinstance(value, str):
                entryMod[key] = "'"+value+"'"
            else:
                entryMod[key] = value
        return entryMod

    ### PUBLIC METHODS ###

    def find_filter(self, entry={}, shows=['*'], attrs={}):
        self._welcomeShowCheck(shows) # check if all item in list correspond to an column in database
        self._welcomeCheck(entry) # check if entry follows format
        self._welcomeAttrsCheck(attrs) # check if attrs follows format
        containerBuild = self._createBuild(shows, entry, attrs)

        phrase = "SELECT "

        for item in containerBuild['show']:
            phrase += item
            phrase += ', '
        phrase = phrase[:-2]

        phrase += " FROM {} WHERE ".format(self.table)

        if entry != {}:
            for key, value in containerBuild['entry'].items():
                phrase += "({}={})".format(key, value)
                phrase += ' AND '
            phrase = phrase[:-5] # Delete the 'END'
        else: # No for loop occurs -> delete the 'WHERE'
            phrase = phrase[:-7]
        phrase += ';'

        answer = self._activeManager(phrase)
        print('READ succesfull')
        return answer
