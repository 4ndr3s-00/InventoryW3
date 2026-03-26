# archivos.py

# Save inventory to CSV file
def save_csv(inventory, path, include_header=True):
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    try:
        with open(path, "w") as file:
            if include_header:
                file.write("name,price,quantity\n")

            for p in inventory:
                file.write(f"{p['name']},{p['price']},{p['quantity']}\n")

        print(f"Inventory saved in: {path}")

    except Exception as e:
        print("Error saving file:", e)


# Load inventory from CSV file
def load_csv(path):
    inventory = []
    invalid_rows = 0

    try:
        with open(path, "r") as file:
            lines = file.readlines()

        # Validate header
        if lines[0].strip() != "name,price,quantity":
            print("Invalid file format.")
            return [], 0

        for line in lines[1:]:
            parts = line.strip().split(",")

            if len(parts) != 3:
                invalid_rows += 1
                continue

            name, price, quantity = parts

            try:
                price = float(price)
                quantity = int(quantity)

                if price < 0 or quantity < 0:
                    invalid_rows += 1
                    continue

                inventory.append({
                    "name": name,
                    "price": price,
                    "quantity": quantity
                })

            except ValueError:
                invalid_rows += 1

        return inventory, invalid_rows

    except FileNotFoundError:
        print("File not found.")
        return [], 0
    except UnicodeDecodeError:
        print("File encoding error.")
        return [], 0
    except Exception as e:
        print("Error loading file:", e)
        return [], 0