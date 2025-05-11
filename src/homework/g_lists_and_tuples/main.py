#from src.homework.g_lists_and_tuples import lists

def main():
    while True:
        print("\n1 - Show the list low/high values")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            values = []
            while True:
                num = int(input("Enter a list value: "))
                values.append(num)

                if len(values) >= 3:
                    cont = input("Do you want to enter another value? (y/n): ").lower()
                    if cont == 'n':
                        break

            low = lists.get_lowest_list_value(values)
            high = lists.get_highest_list_value(values)

            print(f"Lowest value: {low}")
            print(f"Highest value: {high}")

        elif choice == '2':
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
