from models.MenuObject import MenuObject


class RestaurantObject:
    def __init__(self, restId, name, maxOrders):
        self.restId = restId
        self.name = name
        self.menu = {}
        self.totalOrders = 0
        self.maxOrders = maxOrders
        self.totalOrders = 0

    def AddMenu(self, itemId, itemName, price, itemType):
        if itemId in self.menu.keys():
            print("Item Id already exists with item name as " + self.menu[itemId].name)
        else:
            self.menu[itemId] = MenuObject(itemId, itemName, price, itemType)
            print("Item Added Successfully")

    def updateMenu(self, itemId, itemName, itemPrice, itemType):
        if itemId not in self.menu.keys():
            print("Item Id doesn't exist ")
        else:
            self.menu[itemId].name = itemName
            self.menu[itemId].price = itemPrice
            self.menu[itemId].itemType = itemType
            print("Updated Successfully")

    def getFullMenu(self):
        for i in self.menu:
            print(i + ": " + self.menu[i].name)

    def getNameSearch(self, itemPhrase):
        for i in self.menu:
            temp = self.menu[i].name
            if temp.find(itemPhrase) != -1:
                print(i + ": " + temp)

    def getTypeSearch(self, itemType):
        for i in self.menu:
            temp = self.menu[i].itemType
            if itemType == temp:
                print(i + ": " + temp)


