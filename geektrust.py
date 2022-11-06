from sys import argv
from additionals import vendor, inventory



def parseArgs():
    # check if the input file is provided
    if len(argv) != 2:
        raise Exception(vendor.filePathError)
    
    # open the input file and processing the lines
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    return lines



def main():
    # parse the input file(s)
    lines = parseArgs()

    # initialize the inventory
    localInventory = inventory.inventory(vendor.InventoryList)


    # printing the final bill
    print(localInventory.generateBill(lines))  

if __name__ == "__main__":
    main()
