from sys import argv
import inventory
from inventoryFunctions import *

# initialize the inventory and bill
products = inventory.products
total = inventory.total
discount = inventory.discount

def main():


    if len(argv) != 2:
        raise Exception("File path not entered")
    
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        
        x = line.split()
        output = ""  # process the input command and get the output
        
        global total
        global discount


        if x[0] == "ADD_ITEM":
            output, total, discount = add(x[1], int(x[2]), total, discount, products)

        if x[0] == "PRINT_BILL":
            output += (calculateBill(total, discount))
        

        # Once it is processed print the output using the command System.out.println()
        print(output)


if __name__ == "__main__":
    main()
