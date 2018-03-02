class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return """<User name {0.name} email {0.email} repr>""".format(self)

    def __str__(self):
        return """User name {0.name} email {0.email} str""".format(self)
