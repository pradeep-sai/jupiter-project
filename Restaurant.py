from models.RestaurantObject import RestaurantObject

restaurants = dict()


class Restaurant:

    def deleteRestaurant(self, restId):
        if restId not in restaurants.keys():
            print("Restaurant with the given Id doesn't exist")
        else:
            del restaurants[restId]
            print("Restaurant deleted successfully")

    def createRestaurant(self, restId, name, maxOrders):
        if restId in restaurants.keys():
            print("Restaurant with the given Id already exists")
        else:
            restaurants[restId] = RestaurantObject(restId, name, maxOrders)
            print("Restaurant created Succesfully")

    def updateRestaurant(self, restId, name, maxOrders):
        if restId not in restaurants.keys():
            print("Restaurant doesn't exist")
        else:
            restaurants[restId].name = name
            restaurants[restId].maxOrders = maxOrders
            print("Restaurent details updated successfully")
