import os
import subprocess

from NLGlite.stochastics.stochastics import select_word_with_bias
from NLGlite.constants.constants import *
from NLGlite.trainer import reader, trainingStructure
from NLGlite.grammar.grammar import grammar as g


class _NLGlite_:
    """
    NLGlite is a class that wraps the functions in the trainer and provides an easy interface to train and use the
    NLGlite system.
    """
    token_queue = []
    text = ""
    config_file_path = ""
    number_of_sentences = 1

    def __init__(self):
        self.token_queue = []
        self.text = ""
        self.config_file_path = ""
        self.number_of_sentences = 1

    def make_new_config_file(self, config_file_path):
        """
        Creates a new NLGlite configuration file at the path provided. It then sets
        :param config_file_path:
        :return:
        """
        try:
            f = open(config_file_path, "w", encoding="utf8")
            f.close()
            self.config_file_path = config_file_path
            return GOOD
        except:
            return NO_FILE

    def capitalise(self, s: str):
        """
        wrapper for the .capitalize() function because it doesn't work on array elements
        :param s: The word to capitalize
        :return: The capitalized word
        """
        return s.capitalize()

    def get_config_file_path(self) -> str:
        """
        Returns the path to the config file that is being used
        :return: the file path of the c.lcfg file
        """
        return self.config_file_path

    def set_config_file_path(self, new_path: str):
        """
        Updates the config file path
        :param new_path: the new file path
        """
        self.config_file_path = new_path

    def get_number_of_sentences(self) -> int:
        """
        Returns the number of sentences to generate.
        :return: The number of sentences
        """
        return self.number_of_sentences

    def set_number_of_sentences(self, new_num: int):
        """
        Updates the number of sentences. Will only accept natural numbers.
        :param new_num: the new number to update
        """
        if new_num < 0:
            raise ValueError("Number of sentences must be greater than or equal to 1")
        self.number_of_sentences = new_num

    def train(self, file_path: str, method: str) -> int:
        data = reader.read_file(file_path)

        # If there is no input or output files then we throw NO_FILE
        if not os.path.exists(file_path):
            return NO_FILE

        if self.config_file_path == "":
            return NO_FILE

        # Otherwise, lets scrape file and return GOOD. If the file is bad, the scraper will tell us.
        if method == "BLOB":
            reader.tag_process_dump(data, self.config_file_path, TAG_BLOB)
            return GOOD
        elif method == "CORE":
            reader.tag_process_dump(data, self.config_file_path, TAG_CORE)
            return GOOD
        else:
            reader.tag_process_dump(data, self.config_file_path, 1)
            return GOOD

    def generate_sentences(self, number_of_sentences: int):
        """
            Generates a set number of sentences using a populated .lcfg file.
            you are generating from.
            :param number_of_sentences: number of sentences to generate
            :return: Success: the generated sentence
                     Failure: Code constant depending on success. This can be used to throw errors.
                     Either NO_FILE or NOT_ENOUGH_DATA
            """
        # the paragraph is the list of words which we write to after processing
        paragraph = []

        grammar = g()

        # create a training structure from the file provided
        ts = trainingStructure()
        if os.path.exists(self.config_file_path):
            ts.parse_from(self.config_file_path)
        else:
            return NO_FILE

        # for as many sentences as requested, generate a pattern for that sentence "randomly"
        for i in range(number_of_sentences):
            grammar.generate()
        self.token_queue = grammar.get_token_queue()

        print(self.token_queue)  # these are the tokens that we will be matching

        # generate the words for the paragraph
        last_word = ""  # set the last word to be nothing
        i = 0  # we haven't processed any words yet
        while i < len(self.token_queue):  # whilst we aren't at the end of the queue
            # take item "i" from the token queue
            token = self.token_queue[i]
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
                            lookup_vector.append(
                                item[0])  # this is added to the list of possible items we are moving to

                            transition_vector.append(1)
                            # because it doesn't come after anything, we just add 1 and let the probabilities work out.
                            # I.e. if there are multiple "The"s then they just get shoved into the list next to each
                            # other.
                    else:
                        if token == item[3] and last_word == item[0]:  # otherwise if the last word is item 0
                            lookup_vector.append(
                                item[2])  # this is added to the list of possible items we could move to
                            transition_vector.append(item[4])  # and this is the probability we are choosing it

                print("Token: ", token, "| Lookup Vector: ", lookup_vector, "\nToken: ", token, "| Transition vector: ",
                      transition_vector, " | SizeOf: ", len(transition_vector), "\n")

                if len(transition_vector) != 0:  # if there are words to choose from...
                    # select a word and append it to the paragraph, then increment i to move to the next word
                    last_word = select_word_with_bias(transition_vector, lookup_vector)
                    paragraph.append(last_word)
                    i += 1
                    print("last_word =" + last_word)
                elif last_word != "":  # otherwise, the vector has no words, and so we just pick a random one of type
                    last_word = ""
                    print("last_word =" + last_word)
                else:
                    return NOT_ENOUGH_DATA

                # stops the memory monster growing
                del transition_vector
                del lookup_vector

        # postprocessing

        # process the items in paragraph linearly.
        i = 1
        stop_chars = [".", "?", "!", "..."]
        space_chars = stop_chars + [",", ":", ";", "-"]
        output = self.capitalise(paragraph[0]) + " "

        while i < len(paragraph):
            # if the previous token was a sentence end then we start the new sentence by capitalising it
            if paragraph[i - 1] in stop_chars:
                paragraph[i] = self.capitalise(paragraph[i])
            else:
                paragraph[i] = paragraph[i].lower()

                if paragraph[i] == "i":
                    paragraph[i] = "I"

            # if the next token is a space character then we don't write a space
            if i + 1 < len(paragraph) and paragraph[i + 1] in space_chars:
                # python uses lazy evaluation, so we can avoid the "out of range error by evaluating the length check
                # first
                output = output + paragraph[i]
            else:
                output = output + paragraph[i] + " "
            i += 1

        # print the paragraph
        return output

    def clear(self):
        # if the file doesn't exist, return NO_FILE
        if not os.path.exists(self.config_file_path):
            return NO_FILE

        # if reading the right type of file, open it and return GOOD
        if self.config_file_path.endswith(".lcfg"):
            f = open(self.config_file_path, "w", encoding="utf8")
            f.close()
            return GOOD

        # otherwise, the file exists but is BAD. Return BAD_FILE.
        return BAD_FILE

    def edit(self):
        """
        Opens the file in the user's default text editor
        :return: Code constant depending on success. This can be used to throw errors. Either GOOD, NO_FILE or BAD_FILE
        """
        if os.path.exists(self.config_file_path):
            if os.name == "nt":  # For Windows
                subprocess.Popen(["notepad.exe", self.config_file_path])
                return GOOD
            elif os.name == "posix":  # For Linux and Mac
                subprocess.Popen(["vim", self.config_file_path])
                return GOOD
            else:
                # OS not accepted
                return BAD_OS
        else:
            # File doesn't exist
            return NO_FILE
