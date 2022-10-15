
#Meal Price Calculator



#What is the price of the child's meal?
price_child = float(input("What is the price of a child's meal?:"))

price_adult = float(input("What is the price of an adult's meal? "))
# Number of Adults
number_adults = int(input("How many adults do you have?"))
#Number of Children
number_children = int(input("How many children are in your party?"))
#Sales Tax Rate
sales_tax_rate = float(input("What is the sales tax rate?"))


subtutal_children = price_child*number_children
subtotal_adults = price_adult*number_adults
subtotal_total= subtotal_adults + subtutal_children + sales_tax_rate

print(subtotal_total)
print(f"Sales Tax: ${sales_tax_rate}")
print(f"Total for Children's Meals: ${subtutal_children}")
print(f"Total for Adult Meals: ${subtotal_adults}")
print(f"Total: ${subtotal_total}")
