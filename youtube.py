def display_inventory(inventory):
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_inventory(inventory, item, new_quantity):
    if item in inventory:
        inventory[item] = new_quantity
        print(f"{item} updated. New quantity: {new_quantity}")
    else:
        print(f"{item} not found in inventory.")

def calculate_total_value(inventory, prices):
    total_value = 0
    for item, quantity in inventory.items():
        if item in prices:
            total_value += prices[item] * quantity
    return total_value

# Initialize inventory and item prices
inventory = {
    "apples": 10,
    "bananas": 15,
    "chocolates": 5,
    "milk": 7,
    "eggs": 30
}

prices = {
    "apples": 1.0,
    "bananas": 0.5,
    "chocolates": 2.0,
    "milk": 2.5,
    "eggs": 0.2
}

# Display the initial inventory
display_inventory(inventory)

# Update the inventory
item_to_update = input("Enter the item to update: ")
new_quantity = int(input("Enter the new quantity: "))
update_inventory(inventory, item_to_update, new_quantity)

# Calculate the total value of the inventory
total_value = calculate_total_value(inventory, prices)
print(f"Total inventory value: ${total_value:.2f}")
