class item:
    def __init__(self, name, category, price, discount, max_quantity):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount
        self.max_quantity = max_quantity


tshirt = item("TSHIRT", "Clothing", 1000, 10, 2)
jacket = item("JACKET", "Clothing", 2000, 5, 2)
cap = item("CAP", "Clothing", 500, 20, 2)
notebook = item("NOTEBOOK", "Stationery", 200, 20, 3)
pens = item("PENS", "Stationery", 300, 10, 3)
markers = item("MARKERS", "Stationery", 500, 5, 3)

products = [tshirt, jacket, cap, notebook, pens, markers]