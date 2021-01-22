from User import User


if __name__ == '__main__':
    Users = User()

    Users.createUser("aditya", "peacebanti", "aditya@gmail.com")
    Users.getProfile("aditya")
    Users.updateProfile("aditya", "taylor", "aditya@gmail.com")
    Users.getProfile("aditya")
