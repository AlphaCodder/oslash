from sys import argv
from additionals import vendor, inventory, system



def parseArgs():
    # check if the input file is provided
    if len(argv) != system.maxArgs:
        raise Exception(system.filePathError)
    
    # open the input file and processing the lines
    file_path = argv[system.filePath]
    lines = open(file_path, system.readOnly).readlines()

    return lines



def main():
    # parse the input file(s)
    lines = parseArgs()

    # initialize the inventory
    localInventory = inventory.inventory(vendor.InventoryList)


    # printing the final bill
    print(localInventory.getBill(lines))  

if __name__ == system.main:
    main()
