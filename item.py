class item:
    def __init__(self, name, category, price, discount):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount
        if self.category is Clothing:
            self.max_quantity = 2
        elif self.category is Stationery:
            self.max_quantity = 3

Clothing = "Clothing"
Stationery = "Stationery"

tshirt = item("TSHIRT", Clothing, 1000, 10)
jacket = item("JACKET", Clothing, 2000, 5)
cap = item("CAP", Clothing, 500, 20)
notebook = item("NOTEBOOK", Stationery, 200, 20)
pens = item("PENS", Stationery, 300, 10)
markers = item("MARKERS", Stationery, 500, 5)

products = [tshirt, jacket, cap, notebook, pens, markers]