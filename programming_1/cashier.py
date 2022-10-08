price_child = float(input("What is the price of a child's meal?:"))
price_adult = float(input("What is the price of an adult's meal? "))
number_adults = int(input("How many adults do you have?"))
number_children = int(input("How many children are in your party?"))
sales_tax_rate = float(input("What is the sales tax rate?"))


subtutal_children = price_child*number_children
subtotal_adults = price_adult*number_adults
subtotal_total= subtotal_adults + subtutal_children + sales_tax_rate

print(subtotal_total)