class wordPair:
    word = ""
    w_type = ""

    def __init__(self, word: str, w_type: str):
        """
        Initialises a word pair, an auxiliary data structure that allows me for the manipulation of a pair of string
        variables in an easier context
        :param word: The word
        :param w_type: The type (NLTK token) of the word
        """
        self.word = word
        self.type = w_type
    
    def get_word(self):
        """
        Getter for the word of the word pair
        :return: the word of the word pair
        """
        return self.word
    
    def get_type(self):
        """
        Getter for the type of the word pair
        :return: the type of the word pair
        """
        return self.type
