from .table import Table
from .manager import Manager
from .exceptions_raise import *
from local_settings_user import local_set

# Note:
# Be careful when deleting records in a table!
# Notice the WHERE clause in the DELETE statement.
# The WHERE clause specifies which record(s) should be deleted.
# If you omit the WHERE clause, all records in the table will be deleted!

class Delete:

    def __init__(self, table):
        self.table = table
        self.db_name = self.table.get_db_name()
        self.tb_name = self.table.get_tb_name()
        if isinstance(self.table, Table):
            self.patron = self.table.__transfert__() # Load DB-definition from Table-class
        else:
            raise TableLinkFailed(self.table)

    def __str__(self):
        return self.table

    
    ### INTERN METHODS ###

    ## MANAGER DB ##

    def _activeManager(self, phrase):
        man = Manager(self.db_name)
        man.interact_up(phrase)
        man.shutdown_manager()


    ## CHECK PACKAGE ##

    def _welcomeCheck(self, entry): # TODO _welcomeCheck is almost the same as in insert.py AND read.py. Maybe I can dedicate the checks in a special file
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
    
    ## CONTAINER BUILD ##

    def _alterEntry(self, entry):
        entryMod = {}
        for key, value in entry.items():
            if isinstance(value, str):
                entryMod[key] = "'"+value+"'"
            else:
                entryMod[key] = value
        return entryMod

    ### PUBLIC METHODS ###

    def remove_filter(self, entry={}):
        self._welcomeCheck(entry) # check if entry follows format
        entry = self._alterEntry(entry)
        phrase = "DELETE FROM {} WHERE ".format(self.tb_name)

        if entry != {}:
            for key, value in entry.items():
                phrase += "({}={})".format(key, value)
                phrase += ' AND '
            phrase = phrase[:-5] # Delete the 'END'
        else: # No for loop occurs -> delete the 'WHERE'
            phrase = phrase[:-7]
        phrase += ';'

        answer = self._activeManager(phrase)
        print('DELETE succesfull')
        return answer