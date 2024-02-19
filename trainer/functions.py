import os
import platform

from trainer import reader as reader


def clear_data(filepath):
    data = ""
    # if reading the right type of file
    if filepath.endswith(".lcfg"):
        f = open(filepath, "w", encoding="utf8")
        f.close()


def edit_data(filepath):
    os_name = get_os()
    # opens the file in the user's default text editor
    if os.path.exists(filepath):
        if os_name == "Windows":
            os.system(f"start {filepath}")
        elif os_name == "Linux":
            os.system(f"xdg-open {filepath}")
        elif os_name == "Darwin":
            os.system(f"open {filepath}")
    else:
        print("File not found.")


def train_data(filepath, output_path, genre):
    data = reader.read_file(filepath)

    if output_path == "":
        output_path = "training_data.lcfg"  # training data liteconfig

    if genre == "BLOB":
        reader.scrape(data, output_path, 2)
    else:
        reader.scrape(data, output_path, 1)


def get_os():
    return platform.system()
