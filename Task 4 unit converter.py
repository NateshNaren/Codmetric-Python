#Task 4 Unit Converter
 
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def km_to_miles(km):
    return km * 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

conversions = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit),
    "2": ("Kilometers to Miles", km_to_miles),
    "3": ("Kilograms to Pounds", kg_to_pounds)
}

def main():
    while True:
        print("\nUnit Converter")
        for key, (name, _) in conversions.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("Select an option: ")
        if choice == "0":
            print("Exiting...")
            break

        if choice in conversions:
            try:
                value = float(input("Enter the value to convert: "))
                result = conversions[choice][1](value)
                print(f"Result: {result:.2f}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
