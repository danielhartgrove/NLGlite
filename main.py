import random
import sys
import numpy as np
# public packages

from postprocessing.postprocessing import process_sentence_end
from stochastics.stochastics import generate_number, select_word_with_bias
from trainer.trainingStructure import TrainingStructure
from grammar import grammar

sys.path.append("./grammar")
sys.path.append("./postprocessing")
sys.path.append("./stochastics")
# local packages


token_queue = []  # create the initial queue for the tokens
paragraph = []  # create the initial queue for the paragraph


def function():
    f = input("Which dataset (.lcfg) would you like to use? ")
    ts = TrainingStructure()
    ts.parse_from(f)

    n = input("How many sentences do you want to generate? ")
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
        for transition in transition_vector:
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
    print(output)


def __main__():
    function()


if __name__ == "__main__":
    __main__()
