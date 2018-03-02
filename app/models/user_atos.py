class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email
    def user_data(self):
        return 'nome '+self.name+' email '+self.email