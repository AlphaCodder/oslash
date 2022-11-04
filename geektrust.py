from sys import argv
from inventory import *

# initialize the inventory
localInventory = inventory(0,0)

def main():

    # check if the input file is provided
    if len(argv) != 2:
        raise Exception("File path not entered")
    
    # open the input file and processing the lines
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        
        output = ""  # process the input command and get the output
        
        global localInventory


        if line.startswith("ADD_ITEM"):
            action, item, quantity = line.split()
            output = localInventory.add(item, int(quantity))

        if line.startswith("PRINT_BILL"):
            output = localInventory.calculateBill()
        

        # Once it is processed print the output using the command System.out.println()
        print(output)


if __name__ == "__main__":
    main()
