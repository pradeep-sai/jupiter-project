from models.OrdersObject import OrdersObject
from User import users, User
from Restaurant import restaurants, Restaurant

orders = {}


class Orders:
    def placeOrder(self, orderId, username, restaurantId, itemId):
        if orderId in orders.keys():
            print("orderId already exists")
        elif username not in users.keys():
            print("user does not exist")
        elif restaurantId not in restaurants.keys():
            print("restaurant does not exist")
        elif itemId not in restaurants[restaurantId].menu.keys():
            print("item does not exist")
        elif restaurants[restaurantId].totalOrders < restaurants[restaurantId].maxOrders:
            orders[orderId] = OrdersObject(orderId, username, restaurantId, itemId)
            restaurants[restaurantId].totalOrders = restaurants[restaurantId].totalOrders + 1
            print("order placed successfully")
        else:
            print("max orders reached")

    def retrieveOrder(self, username):
        if username not in users.keys():
            print("user does not exist")
        else:
            for order in orders.values():
                if order.username == username:
                    print(str(order.orderId) + " " + str(order.restaurantId) + " " + str(order.itemId))
