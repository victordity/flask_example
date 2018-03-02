class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "User name {}, User email {}".format(self.name, self.email)
