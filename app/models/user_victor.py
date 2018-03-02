import json

class UserVictor:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
