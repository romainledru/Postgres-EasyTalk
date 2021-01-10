class AlreadyExist(Exception):
    def __init__(self, name):
        self.name = name
        self.message = "The name can not be used twice in Table!"
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'

class WrongEntry(Exception):
    def __init__(self, name):
        self.name = name
        self.message = "This entry does not exist in Database!"
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'

class LengthError(Exception):
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.message = "The varChar has a length bigger than allowed! ({} is allowed)".format(self.length)
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'

class PrimaryDouble(Exception):
    def __init__(self, name):
        self.name = name
        self.message = "Is already Primary Key. There can not be two Primary Key"
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'
    
class KeyNotAccepted(Exception):
    def __init__(self, name):
        self.name = name
        self.message = "This key is not accepted"
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'

class TableLinkFailed(Exception):
    def __init__(self, name):
        self.name = name
        self.message = "Link with Table has failed"
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'

class CompulsoryEntry(Exception):
    def __init__(self, name):
        self.name = name
        self.message = "This entry should figure in your insert dict"
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'

class UnabletoConnect(Exception):
    def __init__(self, name):
        self.name = name
        self.message = "easytalk can't reach the database. Please check db-name, host, user, pswd, port."
        super().__init__(self.message)

    def __str__(self):
        return f' \n\n ***{self.name}*** -> {self.message}\n\n'