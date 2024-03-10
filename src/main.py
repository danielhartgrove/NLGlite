from tkinter import *
from tkinter import filedialog

import pyperclip
# public packages

from NLGlite.stochastics.stochastics import generate_number, select_word_with_bias

from NLGlite.grammar import grammar
from dh_popup import dh_popup as dh
from NLGlite.trainer.functions import train_data, clear_data, edit_data
from NLGlite.trainer.trainingStructure import TrainingStructure

method = "CORE"
token_queue = []  # create the initial queue for the tokens
paragraph = []  # create the initial queue for the paragraph
num_of_sentences = 1


# TEXT FUNCTIONS #

# wrapper for the .capitalize() function because it doesn't work on array elements
def capitalise(s: str):
    return s.capitalize()


def generate(f: str, n: str):
    global token_queue, paragraph

    # we have an empty token queue which we are going to add to via the grammar.
    token_queue = []
    # the paragraph is the list of words which we write to after processing
    paragraph = []

    # create a training structure from the file provided
    ts = TrainingStructure()
    if f:
        ts.parse_from(f)
    else:
        dh.popup("Fatal Error", "No file provided", 100, 100)

    # for as many sentences as requested, generate a pattern for that sentence "randomly"
    for i in range(int(n)):
        grammar.match_sentence(generate_number(1, 103), token_queue)

    print(token_queue)  # these are the tokens that we will be matching

    # generate the words for the paragraph
    last_word = ""  # set the last word to be nothing
    i = 0  # we haven't processed any words yet
    while i < len(token_queue):  # whilst we aren't at the end of the queue
        # take item "i" from the token queue
        token = token_queue[i]
        # reset the vectors
        transition_vector = []
        lookup_vector = []
        # each token will correspond 1 : 1 to some part of the paragraph and therefore, we want to do a direct swap
        if (token == "." or token == "," or token == ";" or token == "?" or token == "!"
                or token == ":" or token == "a"):
            paragraph.append(token)
            i += 1
        else:
            for item in ts.data:
                # for each item in the data

                if last_word == "":  # if the last generated word is nothing then pick only the valid tokens
                    if token == item[1]:  # if the item type has an appropriate token
                        lookup_vector.append(item[0])  # this is added to the list of possible items we are moving to

                        transition_vector.append(1)
                        # because it doesn't come after anything, we just add 1 and let the probabilities work out.
                        # I.e. if there are multiple "The"s then they just get shoved into the list next to each other.
                else:
                    if token == item[3] and last_word == item[0]:  # otherwise if the last word is item 0
                        lookup_vector.append(item[2])  # this is added to the list of possible items we could move to
                        transition_vector.append(item[4])  # and this is the probability we are choosing it

            print("Token: ", token, "| Lookup Vector: ", lookup_vector, "\nToken: ", token, "| Transition vector: ",
                  transition_vector, " | SizeOf: ", len(transition_vector), "\n")

            if len(transition_vector) != 0:  # if there are words to choose from...
                # select a word and append it to the paragraph, then increment i to move to the next word
                last_word = select_word_with_bias(transition_vector, lookup_vector)
                paragraph.append(last_word)
                i += 1
            elif last_word != "":  # otherwise, the vector has no words, and so we just pick a random one of type
                last_word = ""
            else:
                # otherwise, there has been a big mistake.
                dh.popup("Fatal Error",
                         ("Config:\n \"" + f + "\" \ndoes not contain enough information to produce text." +
                          "\nPlease retrain the model."), 650, 150)
                break

    # postprocessing

    # process the items in paragraph linearly.
    i = 1
    stop_chars = [".", "?", "!", "..."]
    space_chars = stop_chars + [",", ":", ";", "-"]
    output = capitalise(paragraph[0]) + " "

    while i < len(paragraph):
        # if the previous token was a sentence end then we start the new sentence by capitalising it
        if paragraph[i - 1] in stop_chars:
            paragraph[i] = capitalise(paragraph[i])
        else:
            paragraph[i] = paragraph[i].lower()

            if paragraph[i] == "i":
                paragraph[i] = "I"

        # if the next token is a space character then we don't write a space
        if i + 1 < len(paragraph) and paragraph[i + 1] in space_chars:
            # python uses lazy evaluation, so we can avoid the "out of range error by evaluating the length check first
            output = output + paragraph[i]
        else:
            output = output + paragraph[i] + " "
        i += 1

    # print the paragraph
    return output


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
    confirm = Button(button_panel, text="Train", command=lambda: train_data(txt_box.get(), lcfg_box.get(), method))
    confirm.pack(side=LEFT, padx=10)
    deny = Button(button_panel, text="No", command=lambda: sub.destroy())
    deny.pack(side=RIGHT, padx=10)
    button_panel.pack(side=TOP, pady=10)


def clear(filepath: str, sub):
    clear_data(filepath)
    sub.destroy()


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
    sentences_entry = Scale(run_frame, from_=1, to=200, orient=HORIZONTAL, command=update_sentence_number)
    sentences_entry.pack(side=RIGHT)
    run_frame.pack(side=TOP, pady=3)

    go_button = Button(root, text="Generate",
                       command=lambda: update_output_box(output_box, generate(lcfg_box.get(),
                                                                              str(num_of_sentences))))
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
