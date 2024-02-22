from trainer import wordPair


class TrainingStructure:
    data = []

    # [WORD, TYPE, WORD, TYPE, FREQ]
    # [0   , 1   , 2   , 3   , 4   ]

    def __init__(self):
        self.data = []

    def __str__(self):
        for x in self.data:
            print(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + x[4])
        return ""

    def get_size(self):
        return len(self.data)

    def get_wordlist(self):
        a = []
        for x in self.data:
            a.append(x[0])

        return a

    def insert(self, word_pair: wordPair, word_pair2: wordPair):
        # search the data structure for the word pair
        x = len(self.data)
        if x == 1:
            self.data.append([word_pair.get_word(), word_pair.get_type(), word_pair2.get_word(), word_pair2.get_type(),
                              1])
            return
        else:
            for i in range(x):
                if (self.data[i][0] == word_pair.get_word() and self.data[i][1] == word_pair.get_type() and
                        self.data[i][2] == word_pair2.get_word() and self.data[i][3] == word_pair2.get_type()):
                    # if it is here, increase the frequency
                    self.data[i][4] = str(int(self.data[i][4]) + 1)
                    return

            # if the word pair is not in the data structure, add it
            self.data.append([word_pair.get_word(), word_pair.get_type(), word_pair2.get_word(), word_pair2.get_type(),
                              1])
            return

    def dump_to_file(self, file_path):
        filepath = r"{}".format(file_path)
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

    def parse_from(self, file_path):
        filepath = r"{}".format(file_path)
        if filepath != "":
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
