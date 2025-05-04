from src.homework.j_classes.class_a import Die

def main():
    die = Die()
    while True:
        die.roll()
        print(die)
        choice = input("Roll again? (y/n): ").strip().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main() #
