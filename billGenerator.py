from inventory import *

def billGenerator(lines):
    for line in lines:   
        localInventory = inventory(0,0)
        bill = ""

        if line.startswith("ADD_ITEM"):
            action, item, quantity = line.split()
            bill += localInventory.add(item, int(quantity))

        else:
            bill += localInventory.calculateBill()
        
        # Once it is processed print the output using the command System.out.println()
    return (bill)