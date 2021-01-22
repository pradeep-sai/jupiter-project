from User import User
from Restaurant import Restaurant, restaurants
from Orders import Orders, orders
from io import StringIO
import unittest
from unittest.mock import patch


class TestCase(unittest.TestCase):

    def test_user(self):
        # CREATE USER
        with patch('sys.stdout', new=StringIO()) as out:
            User.createUser(self, username="deepu", name="peacebeaker", email="bsai@gmail.com")
            self.assertEqual(out.getvalue(), "deepu created successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.createUser(self, username="pradeep", name="sai", email="saip@gmail.com")
            self.assertEqual(out.getvalue(), "pradeep created successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.createUser(self, username="deepu", name="sai", email="saip@gmail.com")
            self.assertEqual(out.getvalue(), "username taken\n")

        # DELETE USER
        with patch('sys.stdout', new=StringIO()) as out:
            User.deleteUser(self, username="deepu")
            self.assertEqual(out.getvalue(), "deepu deleted successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.deleteUser(self, username="deepu")
            self.assertEqual(out.getvalue(), "user does not exist\n")

        # GET PROFILE
        with patch('sys.stdout', new=StringIO()) as out:
            User.getProfile(self, username="deepu")
            self.assertEqual(out.getvalue(), "user does not exist\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.getProfile(self, username="pradeep")
            self.assertEqual(out.getvalue(), "sai saip@gmail.com\n")

        # UPDATE PROFILE
        with patch('sys.stdout', new=StringIO()) as out:
            User.updateProfile(self, username="pradeep", name="bokka", email="bsaipradee@gmail.com")
            self.assertEqual(out.getvalue(), "pradeep updated successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            User.getProfile(self, username="pradeep")
            self.assertEqual(out.getvalue(), "bokka bsaipradee@gmail.com\n")

    def test_restaurant(self):
        # Test for creating reaturants

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.createRestaurant(self, 100, "AB's", 10)
            self.assertEqual(out.getvalue(), "Restaurant created Succesfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.createRestaurant(self, 100, "AB's", 10)
            self.assertEqual(out.getvalue(), "Restaurant with the given Id already exists\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.createRestaurant(self, restId=101, name="Spicy Venue", maxOrders=10)
            self.assertEqual(out.getvalue(), "Restaurant created Succesfully\n")

        # Tests for adding and update menus

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].updateMenu(1, "Grilled Fish", 200, "Starter")
            self.assertEqual(out.getvalue(), "Item Id doesn't exist \n")

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].addMenu(1, "Grilled Fish", 200, "Starter")
            self.assertEqual(out.getvalue(), "Item Added Successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].addMenu(2, "Fish Biryani", 200, "Biryani")
            self.assertEqual(out.getvalue(), "Item Added Successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].addMenu(1, "Grilled Fish", 200, "Starter")
            self.assertEqual(out.getvalue(), "Item Id already exists with item name as Grilled Fish\n")
        # ...........

        # Tests for fetching food menu of a restaurant

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].getFullMenu()
            self.assertEqual(out.getvalue(), "1: Grilled Fish\n2: Fish Biryani\n")

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].getTypeSearch("Starter")
            self.assertEqual(out.getvalue(), "1: Grilled Fish\n")

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].getNameSearch("Fish")
            self.assertEqual(out.getvalue(), "1: Grilled Fish\n2: Fish Biryani\n")

        with patch('sys.stdout', new=StringIO()) as out:
            restaurants[100].getNameSearch("Grilled")
            self.assertEqual(out.getvalue(), "1: Grilled Fish\n")
        # ...........

        # Tests for updating restaurants
        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.updateRestaurant(self, restId=101, name="Spicy Venue", maxOrders=20)
            self.assertEqual(out.getvalue(), "Restaurent details updated successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.updateRestaurant(self, restId=103, name="Spicy Venue", maxOrders=20)
            self.assertEqual(out.getvalue(), "Restaurant doesn't exist\n")
        # ...........

        # Tests for deleting restaurants

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.deleteRestaurant(self, restId=102)
            self.assertEqual(out.getvalue(), "Restaurant with the given Id doesn't exist\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Restaurant.deleteRestaurant(self, restId=101)
            self.assertEqual(out.getvalue(), "Restaurant deleted successfully\n")

    # ..........

    def test_orders(self):
        User.createUser(self, username="abc", name="peacebeaker", email="bsai@gmail.com")
        Restaurant.createRestaurant(self, 99, "BBQ", 5)
        restaurants[99].addMenu(1, "Grilled Fish", 200, "Starter")
        restaurants[99].addMenu(2, "sachina Fish", 300, "Starter")

        with patch('sys.stdout', new=StringIO()) as out:
            Orders.placeOrder(self, 1, "abc", 99, 1)
            self.assertEqual(out.getvalue(), "order placed successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Orders.placeOrder(self, 2, "abc", 99, 2)
            self.assertEqual(out.getvalue(), "order placed successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Orders.placeOrder(self, 3, "abc", 99, 1)
            self.assertEqual(out.getvalue(), "order placed successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Orders.placeOrder(self, 4, "abc", 99, 2)
            self.assertEqual(out.getvalue(), "order placed successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Orders.placeOrder(self, 5, "abc", 99, 1)
            self.assertEqual(out.getvalue(), "order placed successfully\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Orders.placeOrder(self, 6, "abc", 99, 2)
            self.assertEqual(out.getvalue(), "max orders reached\n")

        with patch('sys.stdout', new=StringIO()) as out:
            Orders.retrieveOrder(self, "abc")
            self.assertEqual(out.getvalue(), "1 99 1\n2 99 2\n3 99 1\n4 99 2\n5 99 1\n")


if __name__ == '__main__':
    unittest.main()
