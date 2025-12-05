# Define the menu
menu = {
    'Pasta': 170,
    'Pizza': 210,
    'Softdrink': 90,
    'Burger': 110,  # Fixed spelling from 'Buger'
    'Finger': 70,
    'Coffee': 190,
}

print("Welcome to our hotel")

print(" Pasta    : Rs-170\n Pizza    : Rs-210\n Softdrink: Rs-90\n Burger   : Rs-110\n Finger   : Rs-70\n Coffee   : Rs-190")

order_total = 0

# First order
item_1 = input("Enter the name of the item you want to order: ").strip().title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Here {item_1} is added to your order.")
else:
    print(f"Your ordered item {item_1} is not available yet.")

# Asking for another order
another_order = input("Do you want something else to order? (yes/no): ").strip().lower()

if another_order == "yes":  
    item_2 = input("Enter your second order: ").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available yet.")

# Ensure the total is always printed
print(f"\nThe total amount to pay for your order is Rs={order_total}.")
