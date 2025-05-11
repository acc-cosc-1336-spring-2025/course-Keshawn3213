 #def main():
    while True:
        print("\nHomework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            num = int(input("Enter a number between 1 and 9: "))
            while num <= 0 or num >= 10:
                num = int(input("Invalid. Enter a number between 1 and 9: "))
            print(f"Factorial of {num} is {repetition.get_factorial(num)}")

        elif choice == '2':
            num = int(input("Enter a number between 1 and 99: "))
            while num <= 0 or num >= 100:
                num = int(input("Invalid. Enter a number between 1 and 99: "))
            print(f"Sum of odd numbers up to {num} is {repetition.sum_odd_numbers(num)}")

        elif choice == '3':
            break

        else:
            print("Invalid selection.")

        cont = input("Do you want to exit? (y/n): ").lower()
        if cont == 'y':
            break

if __name__ == "__main__":
    main()
