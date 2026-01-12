from calculator import calculator_menu
from notes_manager import notes_menu
from timer import timer_menu
from file_organizer import file_organizer
from unit_converter import unit_converter

while True:
    print("\n=== PERSONAL PRODUCTIVITY SUITE ===")
    print("1. Calculator")
    print("2. Notes")
    print("3. Timer")
    print("4. File Organizer")
    print("5. Unit Converter")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        calculator_menu()
    elif choice == "2":
        notes_menu()
    elif choice == "3":
        timer_menu()
    elif choice == "4":
        file_organizer()
    elif choice == "5":
        unit_converter()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
