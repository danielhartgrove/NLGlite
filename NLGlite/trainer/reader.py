import os

from NLGlite.constants.constants import *
from NLGlite.trainer.tagger import tag_nltk, tag_blob, tag_core
from NLGlite.trainer.trainingStructure import trainingStructure
from NLGlite.trainer.wordPair import wordPair


# read a file and return the contents
def read_file(filepath: str):
    """
    Reads a text file and returns all the words in it.
    :param filepath: The path to the .txt file to read from.
    :return: Success: A string containing all words in the file
             Failure: code constant depending on success. This can be used to throw errors. Either GOOD, NO_FILE or
             BAD_FILE
    """
    data = ""
    # if reading the right type of file
    if os.path.exists(filepath):
        if filepath.endswith(".txt"):
            f = open(filepath, "r", encoding="utf-8", errors="ignore")
            # add each line to the data string
            for line in f:
                data += line + " "
            f.close()
            return data
        else:
            # Otherwise we throw an error
            return BAD_FILE
    return NO_FILE


def process_wordlist(wordlist: [(str, str)]):
    """
    Postprocessing on the list of words and corrects commonly mistagged words.
    :param wordlist: the list of words to process
    :return: the new wordlist
    """
    x = len(wordlist)
    commonly_mistagged_words_override = [("the", "DT")]  # manually add any commonly mistagged words here
    y = len(commonly_mistagged_words_override)
    for i in range(0, x):
        for j in range(0, y):
            if wordlist[i][0].lower() == commonly_mistagged_words_override[j][0]:
                wordlist[i][1] = commonly_mistagged_words_override[j][1]
    return wordlist


def tag_process_dump(text: str, output_file_path: str, method: int):
    """
    tags the text, processes it and dumps it to the output file using a specified method.
    :param text: The text to be manipulated.
    :param output_file_path: The output file to dump to.
    :param method: The method used to tag the code.
    :return: GOOD.
    """

    banned_chars = [".", ",", "£", "!", "?", "£", "$", "%", "^", "&", "*", "(", ")", "@", "~", "#", "{", "}", "[", "]",
                    "+", "_", "-", "=", "|", "\"", ":", ";", "/", "|", "\\", "'"]

    # Remove banned characters. These characters will mess up the process.
    for char in banned_chars:
        text = str(text).replace(char, "")

    # Tag the words and add them to the word list
    if method == TAG_NLTK:
        wordlist = tag_nltk(text)
    elif method == TAG_BLOB:
        wordlist = tag_blob(text)
    else:
        wordlist = tag_core(text)

    process_wordlist(wordlist)  # word list is a list of tuples. The tuples each contain a single word and its type.

    # if the file exists create the trainingStructure from it. We may need to update it. The if is handled by the ts.
    ts = trainingStructure()
    ts.parse_from(output_file_path)

    x = len(wordlist)
    for i in range(1, x):
        wp1 = wordPair(wordlist[i - 1][0], wordlist[i - 1][1])
        wp2 = wordPair(wordlist[i][0], wordlist[i][1])
        # this will update the word pair's frequency if it already exists in the data structure else set it to 1
        ts.insert(wp1, wp2)
        # this stops the rapid consumption of memory
        # dump the data structure to a file
    ts.dump_to_file(output_file_path)
    del ts
    return GOOD
