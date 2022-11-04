from inventory import *
import messeges

def billGenerator(orders):
    # initialize the inventory
    bill = ""
    localInventory = inventory()

    # process the orders
    for order in orders:   
        

        if order.startswith(messeges.addItem):
            action, item, quantity = order.split()
            bill += localInventory.add(item, int(quantity))

        else:
            bill += localInventory.calculateBill()
        
        # Once it is processed print the output using the command System.out.println()
    return (bill)