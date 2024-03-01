import os
import platform

from trainer import reader as reader

from tkinter import messagebox


def clear_data(filepath: str):
    # if reading the right type of file
    if filepath.endswith(".lcfg"):
        f = open(filepath, "w", encoding="utf8")
        f.close()
        return True
    else:
        if not os.path.exists(filepath):
            messagebox.showerror("Error", f'File not found: {filepath}')

    return False


def edit_data(filepath: str):
    os_name = get_os()
    # opens the file in the user's default text editor
    if ' ' in filepath:
        filepath = '\"' + filepath + '\"'

    if os.path.exists(filepath):
        if os_name == "Windows":
            os.system(f"start {filepath}")
            return True
        elif os_name == "Linux":
            os.system(f"xdg-open {filepath}")
            return True
        elif os_name == "Darwin":
            os.system(f"open {filepath}")
            return True
    else:
        messagebox.showerror("Error", f'File not found: {filepath}')

    return False


def train_data(filepath: str, output_path: str, genre: str):
    print("Tagging...")
    data = reader.read_file(filepath)

    if output_path == "":
        output_path = "training_data.lcfg"  # training data liteconfig

    if genre == "BLOB":
        reader.scrape(data, output_path, 2)
        return True
    elif genre == "CORE":
        reader.scrape(data, output_path, 3)
        return True
    else:
        reader.scrape(data, output_path, 1)
        return True


def get_os():
    return platform.system()
