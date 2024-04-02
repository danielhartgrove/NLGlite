from tkinter import *
from tkinter import filedialog

import pyperclip
# public packages

from NLGlite.NLGlite import _NLGlite_ as nlg

method = "CORE"
num_of_sentences = 1
model = nlg()


# GUI FUNCTIONS #

def update_sentence_number(n: str):
    global num_of_sentences
    num_of_sentences = int(n)
    return str(num_of_sentences)


def toggle(method_label: Label):
    global method
    if method == "POS":
        method = "BLOB"
    elif method == "BLOB":
        method = "CORE"
    elif method == "CORE":
        method = "POS"

    method_label.config(text=("Method: " + method + " Tagging"))


def open_training_window(filepath: str):
    global method
    sub = Tk()
    sub.minsize(400, 200)
    sub.maxsize(400, 200)
    sub.title("Train Model")
    path = StringVar(value=filepath)
    # Configuration File Setup
    top_frame = Frame(sub)
    config_label = Label(top_frame, text="Select .lcfg file:")
    config_label.pack(side=LEFT, pady=5)
    lcfg_box = Entry(top_frame, textvariable=path)  # Entry box for the file path
    lcfg_box.pack(side=RIGHT)
    top_frame.pack(side=TOP, pady=10)

    # Training File Setup
    bottom_frame = Frame(sub)
    config_label = Label(bottom_frame, text="Select .txt file:")
    config_label.pack(side=LEFT, pady=5)
    txt_box = Entry(bottom_frame)  # Entry box for the file path
    txt_box.pack(side=RIGHT)
    bottom_frame.pack(side=TOP, pady=10)

    toggle_panel = Frame(sub)
    method_label = Label(toggle_panel, text=("Method: " + method + " Tagging"))
    method_label.pack(side=LEFT, pady=10, padx=10)
    toggle_button = Button(toggle_panel, text="Switch Method", command=lambda: toggle(method_label))
    toggle_button.pack(side=RIGHT, pady=10, padx=10)
    toggle_panel.pack()

    button_panel = Frame(sub)
    confirm = Button(button_panel, text="Train", command=lambda: train(txt_box.get(), lcfg_box.get(), method))
    confirm.pack(side=LEFT, padx=10)
    deny = Button(button_panel, text="No", command=lambda: sub.destroy())
    deny.pack(side=RIGHT, padx=10)
    button_panel.pack(side=TOP, pady=10)


def clear(filepath: str, sub):
    model.set_config_file_path(filepath)
    model.clear()
    sub.destroy()


def train(filepath: str, lcfg: str, method: str):
    model.set_config_file_path(lcfg)
    model.train(filepath, method)


def edit(filepath: str):
    model.set_config_file_path(filepath)
    model.edit()


def generate(filepath: str, number_of_sentences: str):
    model.set_config_file_path(filepath)
    return model.generate_sentences(int(number_of_sentences))


def open_clear_popup(filepath: str):
    sub = Tk()
    sub.minsize(400, 100)
    sub.maxsize(400, 100)
    sub.title("Clear Data?")
    heading = Label(sub, text="Do you really want to clear the data?")
    heading.pack(side=TOP, pady=10)

    button_panel = Frame(sub)
    confirm = Button(button_panel, text="Yes", command=lambda: clear(filepath, sub))
    confirm.pack(side=LEFT, padx=10)
    deny = Button(button_panel, text="No", command=lambda: sub.destroy())
    deny.pack(side=RIGHT, padx=10)
    button_panel.pack(side=TOP, pady=10)


def update_output_box(output_box, text: str):
    output_box.config(state=NORMAL)
    output_box.delete("1.0", END)
    output_box.insert("1.0", text)
    output_box.config(state=DISABLED)


def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    return filename


# MAIN #

def __main__():
    global num_of_sentences, model
    model = nlg()

    root = Tk()
    string_var = StringVar()
    string_var.set("")
    root.title("NLGLite Engine")
    root.minsize(400, 500)
    root.maxsize(400, 500)

    for i in range(0, 6):
        for j in range(0, 6):
            root.grid_columnconfigure(i, minsize=100)
            root.grid_rowconfigure(i, minsize=50)

    # Configuration File Setup
    top_frame = Frame(root)
    config_label = Label(top_frame, text="Select .lcfg file:")
    config_label.pack(side=LEFT, pady=5)
    lcfg_box = Entry(top_frame)  # Entry box for the file path
    lcfg_box.pack(side=RIGHT)

    top_frame.pack(side=TOP, pady=10)

    # Function Buttons
    button_frame = Frame(root)
    clear_button = Button(button_frame, text="Clear",
                          command=lambda: open_clear_popup(lcfg_box.get()))  # Removes all file
    # data
    clear_button.pack(side=LEFT, ipadx=10, padx=10)
    train_button = Button(button_frame, text="Train", command=lambda: open_training_window(lcfg_box.get()))  # Trains
    # the new model
    # on new training data, opens new window?
    train_button.pack(side=LEFT, ipadx=10, padx=10)
    edit_button = Button(button_frame, text="Edit",
                         command=lambda: edit(lcfg_box.get()))  # Opens the file into a text editor
    edit_button.pack(side=LEFT, ipadx=10, padx=10)
    button_frame.pack(side=TOP, pady=5)

    # Run Setup
    run_frame = Frame(root)
    sentences_label = Label(run_frame, text="How many sentences?")
    sentences_label.pack(side=LEFT, pady=5)
    sentences_entry = Scale(run_frame, from_=1, to=200, orient=HORIZONTAL, command=update_sentence_number)
    sentences_entry.pack(side=RIGHT)
    run_frame.pack(side=TOP, pady=3)

    go_button = Button(root, text="Generate",
                       command=lambda: update_output_box(output_box, generate(lcfg_box.get(), num_of_sentences)))
    go_button.pack(side=TOP, pady=7, padx=10)

    # Output Window
    output_frame = Frame(root)
    output_box = Text(output_frame, width=45, height=15, wrap=WORD)
    output_box.pack(side=TOP)
    output_frame.pack(side=TOP)

    text_control_frame = Frame(root)
    copy_button = Button(text_control_frame, text="Copy to Clipboard", command=lambda: pyperclip.copy(
        output_box.get("1.0", END)))
    copy_button.pack(side=LEFT, pady=5)
    clear_button = Button(text_control_frame, text="Clear Text", command=lambda: update_output_box(output_box, ""))
    clear_button.pack(side=RIGHT, pady=5, padx=10)
    text_control_frame.pack(side=TOP, pady=5)
    root.mainloop()


if __name__ == "__main__":
    __main__()
