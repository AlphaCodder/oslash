# adding items to bill
def add(item, quantity, total, discount, products):

    # if quantity is greater than maximum quantity
    if quantity > products[item]["max_quantity"]:
        return "ERROR_QUANTITY_EXCEEDED", total, discount
    
    # we can add the item to the bill and update the total and discount
    total += products[item]["price"] * quantity
    discount += products[item]["price"] * quantity * products[item]["discount"] / 100
    
    # return the updated total and discount
    return "ITEM_ADDED", total, discount


# evaluating the final amount
def calculateBill(total, discount):

    # remove discount if total is less than 1000
    if total < 1000:
        discount = 0

    # discount applied for purchase of 1000 or more
    elif total >= 1000 and total < 3000:
        total -= discount

    # additional 5% discount if total is 3000 or more
    elif total >= 3000:
        total -= discount
        discount += total * 5 / 100
        total -= total * 5 / 100

    # tax on the total bill
    total += total * 10 / 100

    # return the final amount
    return "TOTAL_DISCOUNT " + str('%.2f' % discount) + '\n' + "TOTAL_AMOUNT_TO_PAY " + str('%.2f' % total) + '\n'