import os

from NLGlite.trainer import wordPair
from NLGlite.constants.constants import *

class trainingStructure:
    """
    This class is responsible for storing the training structure of the NLGlite library.
    It is essentially a wrapper for a 2-D array and functions.

    Each element in the 2-D array contains entries for [WORD, TYPE, WORD, TYPE, FREQ];
    First Word, Token of First word, Second Word, Token of Second Word, Frequency of this Word Pair occurrence.

    [WORD, TYPE, WORD, TYPE, FREQ]
    [0   , 1   , 2   , 3   , 4   ]
    """
    data = []

    def __init__(self):
        """
        Initialise the data as a blank array
        """
        self.data = []

    def __str__(self):
        """
        Return a string representation of the training structure for each entry.
        """
        for x in self.data:
            print(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + x[4])

    def get_size(self):
        """
        Returns the number of entries in the training structure
        :return:
        """
        return len(self.data)

    def get_wordlist(self):
        """
        Returns a list containing every word in the training structure
        :return: The list of words.
        """
        a = []
        for x in self.data:
            a.append(x[0])
        return a

    def insert(self, word_pair: wordPair, word_pair2: wordPair):
        """
        Inserts a new word_pair into the training structure. Used in the training process.
        :param word_pair: The first word_pair object
        :param word_pair2: The second word_pair object
        :return: GOOD status.
        """
        # search the data structure for the word pair
        x = len(self.data)
        if x == 1:
            self.data.append([word_pair.get_word(), word_pair.get_type(), word_pair2.get_word(), word_pair2.get_type(),
                              1])
            return GOOD
        else:
            for i in range(x):
                if (self.data[i][0] == word_pair.get_word() and self.data[i][1] == word_pair.get_type() and
                        self.data[i][2] == word_pair2.get_word() and self.data[i][3] == word_pair2.get_type()):
                    # if it is here, increase the frequency
                    self.data[i][4] = str(int(self.data[i][4]) + 1)
                    return GOOD

            # if the word pair is not in the data structure, add it
            self.data.append([word_pair.get_word(), word_pair.get_type(), word_pair2.get_word(), word_pair2.get_type(),
                              1])
            return GOOD

    def dump_to_file(self, file_path: str):
        """
        Dumps the contents of the training data to a file specified.
        :param file_path: the path of the file to dump to.
        :return:
        """
        filepath = r"{}".format(file_path)
        if os.path.exists(filepath):
            f = open(filepath, "w")
            # for each item
            for i in range(len(self.data)):
                output_string = ""
                # write to a formatted string
                for j in range(5):
                    output_string += str(self.data[i][j]) + ","
                output_string += "\n"
                # write the formatted string to the file
                if ',,,,' not in output_string:
                    f.write(output_string)
            f.close()
            return GOOD
        return NO_FILE

    def parse_from(self, file_path: str):
        """
        Parses a .lcfg file and updates the training data.
        :param file_path: The file path of the .txt file to parse.
        :return: success: GOOD
                 failure: N0_FILE or BAD_FILE
        """
        filepath = r"{}".format(file_path)
        if filepath != "":
            if filepath.endswith(".lcfg"):
                f = open(filepath, "r")
                # for each line in the file
                for line in f:
                    # split the line into a list
                    line_list = line.split(",")
                    # remove the newline character from the last item
                    line_list[4] = line_list[4].rstrip("\n")
                    # add the list to the data structure
                    self.data.append(line_list)
                f.close()
                return GOOD
            else:
                return BAD_FILE
        else:
            return NO_FILE
