from additionals import vendor


# class for item
class item:

    def __init__(self, name, category, price, discount):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount
        self.max_quantity = vendor.ClothingMaxQuantity if category == vendor.Clothing else vendor.StationeryMaxQuantity
    
    @classmethod
    def fromString(cls, string):
        name, category, price, discount = string.split()
        return cls(name, category, int(price), int(discount))


# inventory class
class inventory():

    # inventory constructor
    def __init__(self, inventoryList):
        self.total = vendor.empty
        self.discount = vendor.empty
        self.bill = ""
        self.setProducts(inventoryList)
        
    # to add the products to the inventory
    def setProducts(self, inventoryList):
        self.products = []
        inventoryList = inventoryList.split(vendor.newLine)
        for object in inventoryList:
            self.products.append(item.fromString(object))

    # add products to the inventory
    def add(self, name, quantity):

        for product in self.products:
            if product.name == name:

                # if quantity is greater than maximum quantity
                if quantity > product.max_quantity:
                    return vendor.error

                # we can add the item to the bill and update the total and discount
                else:
                    self.total += product.price * quantity
                    self.discount += product.price * quantity * product.discount / vendor.maxDiscount

                    # return the updated total and discount
                    return vendor.success

    # calculate the bill to be paid
    def calculateBill(self):

        # remove discount if total is less than minDiscountThreshold
        if self.total >= vendor.minDiscountThreshold:
            self.total -= self.discount

        # discount applied for purchase of vendor.minDiscountThreshold or more
        else:
            self.discount = vendor.empty

        # if total is greater than vendor.extraDiscountThreshold, extra vendor.extraDiscount% discount is applied
        if self.total >= vendor.extraDiscountThreshold:
            self.discount += self.total * vendor.extraDiscount
            self.total -= self.total * vendor.extraDiscount

        # tax on the total bill
        self.total += self.total * vendor.taxPercentage

        # return the final amount
        bill = vendor.discount + str('%.2f' % self.discount) + vendor.newLine
        bill += vendor.finalAmount + str('%.2f' % self.total) + vendor.newLine
        return bill

    # to generate the bill
    def generateBill(self, orders):
            
            # process the orders
            for order in orders:
    
                if order.startswith(addItem):
                    action, item, quantity = order.split()
                    self.bill += self.add(item, int(quantity))
    
                else:
                    self.bill += self.calculateBill()
    
            # return the bill
            return self.bill


