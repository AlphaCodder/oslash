# categories available in the inventory and max quantity of each category
Clothing = "Clothing"
Stationery = "Stationery"
ClothingMaxQuantity = 2
StationeryMaxQuantity = 3

# process the item list and add it to the products list
InventoryList = "TSHIRT Clothing 1000 10\nJACKET Clothing 2000 5\nCAP Clothing 50 20\nNOTEBOOK Stationery 200 20\nPENS Stationery 300 10\nMARKERS Stationery 500 5"

# absolute minimum value and maximum value of discount
empty = 0
maxDiscount = 100

# tax percentage
taxPercentage = 0.10

# discount percentages
minDiscountThreshold = 1000
extraDiscountThreshold = 3000
extraDiscount = 0.05

# inventory messeges
addItem = "ADD_ITEM"
error = "ERROR_QUANTITY_EXCEEDED\n"
success = "ITEM_ADDED\n"
discount = "TOTAL_DISCOUNT "
finalAmount = "TOTAL_AMOUNT_TO_PAY "
newLine = "\n"
formatSpecifier = '%.2f'
