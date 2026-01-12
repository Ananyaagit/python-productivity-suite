def unit_converter():
    print("1. KM to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose: ")

    if choice == "1":
        km = float(input("Enter KM: "))
        print("Miles:", km * 0.621371)

    elif choice == "2":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)
