import os

def notes_menu():
    data_folder = os.path.join(os.getcwd(), "data")
    os.makedirs(data_folder, exist_ok=True)
    notes_file = os.path.join(data_folder, "notes.txt")

    # Try creating file safely
    try:
        open(notes_file, "a").close()
    except PermissionError:
        print("Cannot write to data folder. Run VS Code as Administrator or move the project.")
        return

    while True:
        print("\n--- Notes Manager ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            note = input("Enter note: ")
            try:
                with open(notes_file, "a") as f:
                    f.write(note + "\n")
                print("Note saved!")
            except PermissionError:
                print("Cannot save note. Check folder permissions.")
        elif choice == "2":
            try:
                with open(notes_file, "r") as f:
                    content = f.read()
                    if content.strip() == "":
                        print("No notes found.")
                    else:
                        print("\nYour Notes:")
                        print(content)
            except:
                print("No notes found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
