from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, mobile=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.email = email
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize