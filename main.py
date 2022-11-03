from sys import argv
# KUMAR SHIVAM
# ATRIA INSTITUTE OF TECHNOLOGY
# 1AT19CS059
# Path: main.py
# Product	Category	Original price in Rupees	Discount for the sale
# TSHIRT	Clothing	1000	10%
# JACKET	Clothing	2000	5%
# CAP	Clothing	500	20%
# NOTEBOOK	Stationery	200	20%
# PENS	Stationery	300	10%
# MARKERS	Stationery	500	5%

# For each clothing item, the maximum quantity that can be purchased is 2.
# For each stationery item, the maximum quantity that can be purchased is 3.
# Discounts can be applied only if the total purchase amount is 1000 rupees or more.
# An additional discount of 5% can be applied if the total amount to pay is 3000 rupees or more.
# There is a 10% sales tax on total bill. The tax is calculated after all the discounts are applied.

# Write a program to calculate the total amount to be paid by the customer.
products = {"TSHIRT": {"category": "Clothing", "price": 1000, "discount": 10, "max_quantity": 2},
            "JACKET": {"category": "Clothing", "price": 2000, "discount": 5, "max_quantity": 2},
            "CAP": {"category": "Clothing", "price": 500, "discount": 20, "max_quantity": 2},
            "NOTEBOOK": {"category": "Stationery", "price": 200, "discount": 20, "max_quantity": 3},
            "PENS": {"category": "Stationery", "price": 300, "discount": 10, "max_quantity": 3},
            "MARKERS": {"category": "Stationery", "price": 500, "discount": 5, "max_quantity": 3}}
total = 0
discount = 0


def add(item, quantity):
    global total
    global discount
    if quantity > products[item]["max_quantity"]:
        return "ERROR_QUANTITY_EXCEEDED"
    total += products[item]["price"] * quantity
    discount += products[item]["price"] * \
        quantity * products[item]["discount"] / 100
    return "ITEM_ADDED"


def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        output = ""  # process the input command and get the output
        # Add your code here to process input commands.
        x = line.split()
        if x[0] == "ADD_ITEM":
            output += (add(x[1], int(x[2])))

        if x[0] == "PRINT_BILL":
            global total
            global discount
            # discount applied for purchase of 1000 or more
            if total >= 1000:
                total -= discount
            # additional discount of 5% if total is 3000 or more
            if total >= 3000:
                total -= total * 5 / 100
            # reset discount if total is less than 1000
            if total < 1000:
                discount = 0
            # tax on the total bill
            total += total * 10 / 100

            output += "TOTAL_DISCOUNT " + str('%.2f' % discount) + '\n'
            output += "TOTAL_AMOUNT_TO_PAY " + str('%.2f' % total) + '\n'
        # Once it is processed print the output using the command System.out.println()
        print(output)


if __name__ == "__main__":
    main()
