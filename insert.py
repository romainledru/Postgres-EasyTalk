from exceptions_raise import *
from table import Table

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

    ## CHECK PACKAGE ##

    def _welcomeCheck(self, entry):
        if not isinstance(entry, dict):
            raise TypeError
        for key, value in entry.items():
            self._isUnknownEntry(key)
            #self._isEntryTwice(key) # no check anymore: restrict the entry possibilities
            self._isTypeValueCorrect(key, value)
            self._isLengthValueCorrect(key, value)
        self._areAllCompulsoryEntryHere(entry)
    
    def _isUnknownEntry(self, key):
        if key not in self.patron.keys():
            raise WrongEntry(key)
    
    def _isTypeValueCorrect(self, key, value):
        if not isinstance(value, self.patron[key]['type']):
            raise TypeError("\n\n***{}: {}*** -> has a wrong Type !\n\n".format(key, value))

    def _isLengthValueCorrect(self, key, value):
        if isinstance(value, str):
            if len(value) > self.patron[key]['length']:
                raise LengthError(key, self.patron[key]['length'])

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
                containerBuild[key] = entry[key]
            else: # if user has no entry given, and it was not compulsory, then None
                containerBuild[key] = None
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
        return phrase
