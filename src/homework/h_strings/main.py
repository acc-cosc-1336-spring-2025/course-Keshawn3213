def main():
    while True:
        print("\n1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dna1 = input("Enter DNA string 1: ").upper()
            dna2 = input("Enter DNA string 2: ").upper()
            if len(dna1) != len(dna2):
                print("Error: Strings must be of equal length.")
            else:
                distance = value_return.get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance: {distance}")

        elif choice == '2':
            dna = input("Enter DNA string: ").upper()
            complement = value_return.get_dna_complement(dna)
            print(f"DNA Reverse Complement: {complement}")

        elif choice == '3':
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
