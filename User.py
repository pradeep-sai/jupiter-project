from models.UserObject import UserObject
class User:
    users = {}

    def createUser(self, username, name, email):
        if username in self.users.keys():
            print("username taken")
        else:
            self.users[username] = UserObject(username, name, email)
            print(username + "created successfully")

    def deleteUser(self, username):
        if username not in self.users.keys():
            print("user does not exist")
        else:
            self.users.pop(username)
            print(username + "deleted successfully")

    def getProfile(self, username):
        if username not in self.users.keys():
            print("user does not exist")
        else:
            print(self.users[username])

    def updateProfile(self, username, name, email):
        if username not in self.users.keys():
            print("user does not exist")
        else:
            self.users[username].name = name
            self.users[username].email = email
            print(username + "updated successfully")



