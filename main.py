import sys
from tkinter import *
import pyperclip
# public packages

from postprocessing.postprocessing import process_sentence_end
from stochastics.stochastics import generate_number, select_word_with_bias
from trainer.trainingStructure import TrainingStructure
from trainer.functions import *
from grammar import grammar

# local packages

sys.path.append("./grammar")
sys.path.append("./postprocessing")
sys.path.append("./stochastics")

method = "POS"
token_queue = []  # create the initial queue for the tokens
paragraph = []  # create the initial queue for the paragraph
num_of_sentences = 0


def generate(f, n):
    global token_queue, paragraph
    token_queue = []
    paragraph = []

    ts = TrainingStructure()
    ts.parse_from(f)

    for i in range(int(n)):
        grammar.match_sentence(generate_number(1, 4), token_queue)
    print(token_queue)

    # generate the words for the paragraph
    last_word = ""
    for i in range(len(token_queue)):
        token = token_queue[i]
        transition_vector = []
        lookup_vector = []
        # each token will correspond 1 : 1 to some part of the paragraph.
        # therefore, we want to do a direct swap
        for item in ts.data:
            if token == "." or token == "," or token == ";" or token == "?" or token == ":":
                paragraph.append(token)
                break
            # check that items are not punctuation
            if last_word == "":
                if token == item[1]:  # Corrected comparison here
                    lookup_vector.append(item[2])  # the item we are moving to
                    transition_vector.append(item[4])  # the probability we are choosing it
            else:
                if token == item[1] and last_word == item[0]:
                    lookup_vector.append(item[2])  # the item we are moving to
                    transition_vector.append(item[4])  # the probability we are choosing it

        total = 0
        for _ in transition_vector:
            total = total + 1

        print("Token: ", token, "| Lookup Vector: ", lookup_vector, "\nToken: ", token, "| Transition vector: ",
              transition_vector, " | SizeOf: ", total, "\n")

        if transition_vector:
            last_word = select_word_with_bias(transition_vector, lookup_vector)
            paragraph.append(last_word)
        else:
            last_word = ""
            i -= 1

    # postprocessing
    output = ""
    for word in paragraph:
        output = output + word + " "

    if output != "":
        output = output[0].upper() + output[1:]

    output = process_sentence_end(output)
    # print the paragraph
    return output


def update_sentence_number(n):
    global num_of_sentences
    num_of_sentences = n


def toggle(method_label):
    global method
    if method == "POS":
        method = "BLOB"
    elif method == "BLOB":
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
    confirm = Button(button_panel, text="Train", command=lambda: train_data(txt_box.get(), lcfg_box.get(), method))
    confirm.pack(side=LEFT, padx=10)
    deny = Button(button_panel, text="No", command=lambda: sub.destroy())
    deny.pack(side=RIGHT, padx=10)
    button_panel.pack(side=TOP, pady=10)


def clear(filepath, sub):
    clear_data(filepath)
    sub.destroy()


def open_clear_popup(filepath):
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


def update_output_box(output_box, text):
    output_box.config(state=NORMAL)
    output_box.delete("1.0", END)
    output_box.insert("1.0", text)
    output_box.config(state=DISABLED)


def __main__():
    global num_of_sentences

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
                         command=lambda: edit_data(lcfg_box.get()))  # Opens the file into a text editor
    edit_button.pack(side=LEFT, ipadx=10, padx=10)
    button_frame.pack(side=TOP, pady=5)

    # Run Setup
    run_frame = Frame(root)
    sentences_label = Label(run_frame, text="How many sentences?")
    sentences_label.pack(side=LEFT, pady=5)
    sentences_entry = Scale(run_frame, from_=0, to=200, orient=HORIZONTAL, command=update_sentence_number)
    sentences_entry.pack(side=RIGHT)
    run_frame.pack(side=TOP, pady=3)

    go_button = Button(root, text="Generate",
                       command=lambda: update_output_box(output_box, generate(lcfg_box.get(),
                                                                              num_of_sentences)))
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
