import vendor

products = []

class item:
    def __init__(self, name, category, price, discount):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount
        self.max_quantity = vendor.ClothingMaxQuantity if category == vendor.Clothing else vendor.StationeryMaxQuantity


InventoryItems = vendor.InventoryList.splitlines()
for InventoryItem in InventoryItems:
    InventoryItem = InventoryItem.split()
    itemToBeAdded = item(InventoryItem[0], InventoryItem[1], int(InventoryItem[2]), int(InventoryItem[3]))
    products.append(itemToBeAdded)

