import os
import shutil

def file_organizer():
    path = input("Enter folder path to organize: ")

    for file in os.listdir(path):
        if "." in file:
            ext = file.split(".")[-1]
            folder = os.path.join(path, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(path, file), os.path.join(folder, file))

    print("Files organized by type!")
