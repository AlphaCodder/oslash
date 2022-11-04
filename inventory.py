import item, messeges, vendor

# inventory class
class inventory:

    # inventory constructor
    def __init__(self):
        self.total = 0
        self.discount = 0
        self.products = item.products

    # add products to the inventory
    def add(self, name, quantity):

        for product in self.products:
            if product.name == name:

                # if quantity is greater than maximum quantity
                if quantity > product.max_quantity:
                    return messeges.error

                # we can add the item to the bill and update the total and discount
                else:
                    self.total += product.price * quantity
                    self.discount += product.price * quantity * product.discount / 100

                    # return the updated total and discount
                    return messeges.success

    def calculateBill(self):

        # remove discount if total is less than 1000
        if self.total < 1000:
            self.discount = 0

        # discount applied for purchase of 1000 or more
        elif self.total >= 1000 and self.total < 3000:
            self.total -= self.discount

        # if total is greater than 3000, extra 5% discount is applied
        elif self.total >= 3000:
            self.total -= self.discount
            self.discount += self.total * 5 / 100
            self.total -= self.total * 5 / 100

        # tax on the total bill
        self.total += self.total * 10 / 100

        # return the final amount
        return messeges.discount + str('%.2f' % self.discount) + messeges.newLine + messeges.finalAmount + str('%.2f' % self.total) + messeges.newLine
