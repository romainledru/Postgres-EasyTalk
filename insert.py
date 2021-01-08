from exceptions_raise import *
from table import Table
from manager import Manager
from local_settings_user import local_set
import datetime

class Insert:

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
        man.interact_up(phrase)
        man.shutdown_manager()


    ## CHECK PACKAGE ##

    def _welcomeCheck(self, entry):
        if not isinstance(entry, dict):
            raise TypeError
        for key, value in entry.items():
            self._isUnknownEntry(key)
            self._isTypeValueCorrect(key, value)
        self._areAllCompulsoryEntryHere(entry)
    
    def _isUnknownEntry(self, key):
        if key not in self.patron.keys():
            raise WrongEntry(key)
    
    def _isTypeValueCorrect(self, key, value): # TODO with SERIAL: the type is no longer checked (str <-> str)
        if not isinstance(value, self.patron[key]['type']):
            raise TypeError("\n\n***{}: {}*** -> has a wrong Type !\n\n".format(key, value))

    def _areAllCompulsoryEntryHere(self, entry):
        for key, value in self.patron.items():
            if value['compulsory'] == True:
                if key not in entry.keys():
                    raise CompulsoryEntry(key)

    ## CONTAINER BUILD ##

    def _createBuild(self, entry):
        containerBuild = {}
        for key in self.patron.keys():
            if key in entry.keys(): # if user has given an entry for this key
                if isinstance(entry[key], str) or isinstance(entry[key], datetime.datetime):
                    containerBuild[key] = "'"+ str(entry[key]) +"'"
                else:
                    containerBuild[key] = entry[key]
        return containerBuild


    ### PUBLIC METHODS ###

    def write_ENTRY(self, entry):
        self._welcomeCheck(entry)
        containerBuild = self._createBuild(entry)

        phrase = "INSERT INTO {} (".format(self.table)

        for key in containerBuild.keys():
            phrase += key
            phrase += ', '
        phrase = phrase[:-2]
        phrase += ') VALUES ('

        for value in containerBuild.values():
            phrase += str(value)
            phrase += ', '
        phrase = phrase[:-2]
        phrase += ')'
        phrase += ';'

        self._activeManager(phrase)
        print("INSERT succesfull")
