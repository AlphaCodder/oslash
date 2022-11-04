import item, messeges, vendor

# inventory class
class inventory:

    # inventory constructor
    def __init__(self):
        self.total = vendor.empty
        self.discount = vendor.empty
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
                    self.discount += product.price * quantity * product.discount / vendor.maxDiscount

                    # return the updated total and discount
                    return messeges.success

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
        return messeges.discount + str('%.2f' % self.discount) + messeges.newLine + messeges.finalAmount + str('%.2f' % self.total) + messeges.newLine
