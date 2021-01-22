class UserObject:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __str__(self):
        return "username: %s \nname: %s \nemail: %s" % (self.username, self.name, self.email)