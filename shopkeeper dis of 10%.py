def calculate_total_cost(quantity, price_per_item):
    total_cost = quantity * price_per_item

    if total_cost > 1000:
        total_cost -= total_cost * 0.1
    
    return total_cost

quantity = int(input("Enter the quantity of items purchased: "))
price_per_item = float(input("Enter the price per item: "))

total_cost = calculate_total_cost(quantity, price_per_item)

print("Total cost for the user:", total_cost, "rupees")

