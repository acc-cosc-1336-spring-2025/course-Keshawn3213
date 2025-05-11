def main():
    options = int(input("Enter the number of options: "))
    total = int(input("Enter the total number of responses: "))
    ratio = decisions.get_options_ratio(options, total)
    rating = decisions.get_faculty_rating(ratio)
    print(f"Faculty rating is: {rating}")

if __name__ == "__main__":
    main()
