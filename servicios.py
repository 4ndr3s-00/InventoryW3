# servicios.py

# Add product to inventory
def add_product(inventory, name, price, quantity):
    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product)


# Show all products
def show_inventory(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.\n")
        return

    for p in inventory:
        print(f"{p['name']} | {p['price']} | {p['quantity']}")
    print()


# Find product by name
def find_product(inventory, name):
    for p in inventory:
        if p["name"] == name:
            return p
    return None


# Update product data
def update_product(inventory, name, new_price=None, new_quantity=None):
    product = find_product(inventory, name)

    if product:
        if new_price is not None:
            product["price"] = new_price
        if new_quantity is not None:
            product["quantity"] = new_quantity
        return True

    return False


# Delete product from inventory
def delete_product(inventory, name):
    product = find_product(inventory, name)

    if product:
        inventory.remove(product)
        return True

    return False


# Calculate inventory statistics
def calculate_statistics(inventory):
    if len(inventory) == 0:
        return None

    total_units = 0
    total_value = 0

    subtotal = lambda p: p["price"] * p["quantity"]

    most_expensive = inventory[0]
    highest_stock = inventory[0]

    for p in inventory:
        total_units += p["quantity"]
        total_value += subtotal(p)

        if p["price"] > most_expensive["price"]:
            most_expensive = p

        if p["quantity"] > highest_stock["quantity"]:
            highest_stock = p

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": {
            "name": most_expensive["name"],
            "price": most_expensive["price"]
        },
        "highest_stock": {
            "name": highest_stock["name"],
            "quantity": highest_stock["quantity"]
        }
    }