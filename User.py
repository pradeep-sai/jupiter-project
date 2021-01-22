from models.UserObject import UserObject

users = {}


class User:

    def createUser(self, username, name, email):
        if username in users.keys():
            print("username taken")
        else:
            users[username] = UserObject(username, name, email)
            print(username + " created successfully")

    def deleteUser(self, username):
        if username not in users.keys():
            print("user does not exist")
        else:
            users.pop(username)
            print(username + " deleted successfully")

    def getProfile(self, username):
        if username not in users.keys():
            print("user does not exist")
        else:
            print(users[username].name+" "+users[username].email)

    def updateProfile(self, username, name, email):
        if username not in users.keys():
            print("user does not exist")
        else:
            users[username].name = name
            users[username].email = email
            print(username + " updated successfully")

