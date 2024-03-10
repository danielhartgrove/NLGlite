import os
import platform
import subprocess

from src.NLGlite.trainer import reader as reader

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
    # opens the file in the user's default text editor

    if os.path.exists(filepath):
        if os.name == "nt":  # For Windows
            subprocess.Popen(["notepad.exe", filepath])
        elif os.name == "posix":  # For Linux and Mac
            subprocess.Popen(["vim", filepath])
        else:
            messagebox.showerror("Error", "Unsupported OS")
    else:
        messagebox.showerror("Error", f'File not found: {filepath}')
    return False


def train_data(filepath: str, output_path: str, genre: str):
    print("Tagging...")
    data = reader.read_file(filepath)

    if not os.path.exists(filepath):
        messagebox.showerror("Error", f'File not found: {filepath}')
        return False

    if output_path == "":
        messagebox.showerror("Error", f'File not found: {output_path}')
        return False

    if genre == "BLOB":
        reader.scrape(data, output_path, 2)
        return True
    elif genre == "CORE":
        reader.scrape(data, output_path, 3)
        return True
    else:
        reader.scrape(data, output_path, 1)
        return True


def create_lcfg(filepath: str):
    f = open(filepath, "w", encoding="utf8")
    f.close()
    return True


def get_os():
    return platform.system()
