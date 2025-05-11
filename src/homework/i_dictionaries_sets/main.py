from src.homework.i_dictionaries_and_sets import dictionary

def main():
    inventory = {}

    while True:
        print("\nInventory Menu")
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter widget name: ")
            quantity = int(input("Enter quantity to add or subtract: "))
            dictionary.add_inventory(inventory, name, quantity)
            print(f"Updated inventory: {inventory}")

        elif choice == '2':
            name = input("Enter widget name to delete: ")
            result = dictionary.remove_inventory_widget(inventory, name)
            print(result)

        elif choice == '3':
            break

        else:
            print("Invalid choice.")
