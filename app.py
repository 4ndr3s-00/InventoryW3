
from servicios import *
from archivos import *

# Main function to run the application
def main():
    inventory = []
    running = True

    # Main loop
    while running:
        print("\n1. Add")
        print("2. Show")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        option = input("Select option: ")

        # Add product
        if option == "1":
            try:
                name = input("Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))

                if price < 0 or quantity < 0:
                    print("Values must be non negative.")
                else:
                    add_product(inventory, name, price, quantity)
            except:
                print("Invalid input.")

        # Show inventory
        elif option == "2":
            show_inventory(inventory)

        # Search product
        elif option == "3":
            name = input("Name: ")
            product = find_product(inventory, name)
            print(product if product else "Not found")

        # Update product
        elif option == "4":
            try:
                name = input("Name: ")
                price = float(input("New price: "))
                quantity = int(input("New quantity: "))

                if price < 0 or quantity < 0:
                    print("Values must be non negative.")
                else:
                    updated = update_product(inventory, name, price, quantity)
                    print("Updated" if updated else "Not found")
            except:
                print("Invalid input.")

        # Delete product
        elif option == "5":
            name = input("Name: ")
            deleted = delete_product(inventory, name)
            print("Deleted" if deleted else "Not found")

        # Show statistics
        elif option == "6":
            stats = calculate_statistics(inventory)

            if stats:
                print("\n--- Statistics ---")
                print(f"Total units: {stats['total_units']}")
                print(f"Total value: {stats['total_value']}")
                print(f"Most expensive: {stats['most_expensive']['name']} - {stats['most_expensive']['price']}")
                print(f"Highest stock: {stats['highest_stock']['name']} - {stats['highest_stock']['quantity']}")
            else:
                print("No data")

        # Save CSV
        elif option == "7":
            path = input("File path: ")
            save_csv(inventory, path)

        # Load CSV
        elif option == "8":
            path = input("File path: ")
            new_data, errors = load_csv(path)

            if len(new_data) > 0:
                choice = input("Overwrite inventory? (S/N): ")

                if choice.upper() == "S":
                    inventory = new_data
                    action = "replaced"
                else:
                    # Merge inventories
                    for new_p in new_data:
                        existing = find_product(inventory, new_p["name"])

                        if existing:
                            existing["quantity"] += new_p["quantity"]
                            if existing["price"] != new_p["price"]:
                                existing["price"] = new_p["price"]
                        else:
                            inventory.append(new_p)

                    action = "merged"

                print(f"Loaded: {len(new_data)} products")
                print(f"Invalid rows: {errors}")
                print(f"Inventory {action}")
            else:
                print("No valid data loaded.")

        # Exit
        elif option == "9":
            running = False

        # Invalid option
        else:
            print("Invalid option")


main()