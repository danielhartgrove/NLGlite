import json
import sys

from postprocessing.postprocessing import capitalise_after_char
from stochastics.stochastics import generate_number
from grammar import grammar

sys.path.append("./grammar")
sys.path.append("./postprocessing")
sys.path.append("./stochastics")
# local packages


token_queue = []  # create the initial queue for the tokens
paragraph = []  # create the initial queue for the paragraph


def __main__():
    # generate the structure of the paragraph
    while generate_number(1, 5) < 5:
        grammar.match_compound_complex(generate_number(1, 3), token_queue)
        token_queue.append(".")  # add a period to the end of the sentence

    # generate the words for the paragraph

    f = open("words_dictionary.json", "r")
    data = json.load(f)
    for token in token_queue:
        if token in data:
            token_list = data[token]
            paragraph.append(token_list[generate_number(0, len(token_list) - 1)])

    # print the paragraph

    output = ""
    for word in paragraph:
        output = output + word + " "

    # remove spaces before punctuation
    output = output.replace(" .", ".")
    output = output.replace(" ,", ",")
    output = output.replace(" ;", ";")

    output = capitalise_after_char(output, ".")
    output = capitalise_after_char(output, "!")
    output = capitalise_after_char(output, "?")

    if output != "":
        output = output[0].upper() + output[1:]
    print(output)


__main__()
