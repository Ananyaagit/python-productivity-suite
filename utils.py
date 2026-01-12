import os

def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def separator():
    """Prints a visual separator for menus"""
    print("\n" + "="*40 + "\n")
