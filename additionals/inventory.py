from additionals import vendor


# class for item
class item:

    def __init__(self, name, category, price, discount):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount = discount
        self.__max_quantity = vendor.ClothingMaxQuantity if category == vendor.Clothing else vendor.StationeryMaxQuantity
    
    @classmethod
    def fromString(cls, string):
        __name, __category, __price, __discount = string.split()
        return cls(__name, __category, int(__price), int(__discount))
    
    def getName(self):
        return self.__name
    
    def getCategory(self):
        return self.__category
    
    def getPrice(self):
        return self.__price
    
    def getDiscount(self):
        return self.__discount
    
    def getMaxQuantity(self):
        return self.__max_quantity


# inventory class
class inventory():
    
    # inventory constructor
    def __init__(self, inventoryList):
        self.__total = vendor.empty
        self.__discount = vendor.empty
        self.__bill = ""
        self.__products = []
        self.__setProducts(inventoryList)
        
    # to add the products to the inventory
    def __setProducts(self, inventoryList):
        inventoryList = inventoryList.split(vendor.newLine)
        for object in inventoryList:
            self.__products.append(item.fromString(object))

    # add products to the inventory
    def __addProducts(self, name, quantity):

        for product in self.__products:
            
            if product.getName() == name:

                # if quantity is greater than maximum quantity
                if quantity > product.getMaxQuantity():
                    return vendor.error

                # we can add the item to the bill and update the total and discount
                else:
                    self.__total += product.getPrice() * quantity
                    self.__discount += product.getPrice() * quantity * product.getDiscount() / vendor.maxDiscount

                    # return the updated total and discount
                    return vendor.success

    # calculate the bill to be paid
    def __setTotalAndDiscount(self):

        # remove discount if total is less than minDiscountThreshold
        if self.__total >= vendor.minDiscountThreshold:
            self.__total -= self.__discount

        # discount applied for purchase of vendor.minDiscountThreshold or more
        else:
            self.__discount = vendor.empty

        # if total is greater than vendor.extraDiscountThreshold, extra vendor.extraDiscount% discount is applied
        if self.__total >= vendor.extraDiscountThreshold:
            self.__discount += self.__total * vendor.extraDiscount
            self.__total -= self.__total * vendor.extraDiscount

        # tax on the total bill
        self.__total += self.__total * vendor.taxPercentage



    # to generate the bill
    def __generateBill(self, orders):
            
            # process the orders
            for order in orders:
    
                if order.startswith(vendor.addItem):
                    action, item, quantity = order.split()
                    self.__bill += self.__addProducts(item, int(quantity))
    
                else:
                    self.__setTotalAndDiscount()
                    self.__bill += vendor.billFormatter(self.__discount, self.__total)
                    
    
    # return the bill
    def getBill(self, orders):
        
        # generate the bill
        self.__generateBill(orders)
        
        return self.__bill



