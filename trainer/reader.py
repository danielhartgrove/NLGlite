from trainer.trainingStructure import TrainingStructure
from trainer.wordPair import wordPair
from trainer.tagger import *
from dh_popup import dh_popup as dh


# read a file and return the contents
def read_file(filepath: str):
    data = ""
    # if reading the right type of file
    if filepath.endswith(".txt"):
        f = open(filepath, "r", encoding="utf8")
        # add each line to the data string
        for line in f:
            data += line + " "
        f.close()
        return data
    else:
        # Otherwise we throw an error
        print("Invalid file path.")
        exit(1)  # exit with error code 1


def process_wordlist(wordlist: [(str, str)]):
    x = len(wordlist)
    commonly_mistagged_words_override = [("the", "DT")]
    y = len(commonly_mistagged_words_override)
    for i in range(0, x):
        for j in range(0, y):
            if wordlist[i][0].lower() == commonly_mistagged_words_override[j][0]:
                wordlist[i][1] = commonly_mistagged_words_override[j][1]


# scrape a file and write the contents to a specified file
def scrape(text: str, output_file_path: str, method: int):
    # get the text from the file
    banned_chars = [".", ",", "£", "!", "?", "£", "$", "%", "^", "&", "*", "(", ")", "@", "~", "#", "{", "}", "[", "]",
                    "+", "_", "-", "=", "|", "\"", ":", ";", "/", "|", "\\", "'"]

    for char in banned_chars:
        text = text.replace(char, "")

    wordlist = []
    if method == 1:
        wordlist += tag_nltk(text)
    elif method == 2:
        wordlist += tag_blob(text)
    else:
        wordlist += tag_core(text)

    process_wordlist(wordlist)  # word list is a list of tuples

    dh.popup("Training Complete", "Training Complete")
    # if the file exists create the trainingStructure from it
    ts = TrainingStructure()
    ts.parse_from(output_file_path)
    # write all word pairs to a file
    x = len(wordlist)
    for i in range(1, x):
        wp1 = wordPair(wordlist[i - 1][0], wordlist[i - 1][1])
        wp2 = wordPair(wordlist[i][0], wordlist[i][1])
        # this will update the word pair's frequency if it already exists in the data structure else set it to 1
        ts.insert(wp1, wp2)
        # dump the data structure to a file
    ts.dump_to_file(output_file_path)
