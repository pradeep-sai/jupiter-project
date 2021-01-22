from User import User
from Restaurant import Restaurant
from io import StringIO
import unittest
from unittest.mock import patch


class TestCase(unittest.TestCase):

    def test_createuser(self):
        with patch('sys.stdout', new=StringIO()) as out:
            User.createUser(self, username="deepu", name="peacebeaker", email="bsai@gmail.com")
            self.assertEqual(out.getvalue(), "deepu created successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.createUser(self, username="pradeep", name="sai", email="saip@gmail.com")
            self.assertEqual(out.getvalue(), "pradeep created successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.createUser(self, username="deepu", name="sai", email="saip@gmail.com")
            self.assertEqual(out.getvalue(), "username taken\n")

    def test_deleteuser(self):
        User.createUser(self, username="deepu", name="peacebeaker", email="bsai@gmail.com")
        with patch('sys.stdout', new=StringIO()) as out:
            User.deleteUser(self, username="deepu")
            self.assertEqual(out.getvalue(), "deepu deleted successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.deleteUser(self, username="deepu")
            self.assertEqual(out.getvalue(), "user does not exist\n")

    def test_restaurant(self):
        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.createRestaurant(self, restId=100, name="Spicy Venue", maxOrders=10)
            self.assertEqual(out.getvalue(), "Restaurant created Succesfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.createRestaurant(self, 101, "AB's", 10)
            self.assertEqual(out.getvalue(), "Restaurant created Succesfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.createRestaurant(self, 101, "AB's", 10)
            self.assertEqual(out.getvalue(), "Restaurant with the given Id already exists\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.createRestaurant(self, 102, "BBQ", 10)
            self.assertEqual(out.getvalue(), "Restaurant created Succesfully\n")


if __name__ == '__main__':
    unittest.main()
