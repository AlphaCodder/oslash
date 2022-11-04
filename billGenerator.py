from inventory import *

def billGenerator(orders):
    # initialize the inventory
    bill = ""
    localInventory = inventory(0,0)

    # process the orders
    for order in orders:   

        if order.startswith("ADD_ITEM"):
            action, item, quantity = order.split()
            bill += localInventory.add(item, int(quantity))
        
        else:
            bill += localInventory.calculateBill()
        
        # Once it is processed print the output using the command System.out.println()
    return (bill)