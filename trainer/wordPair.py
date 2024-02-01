class wordPair:
    word = ""
    w_type = ""

    def __init__(self, word, w_type):
        self.word = word
        self.type = w_type
    
    def get_word(self):
        return self.word
    
    def get_type(self):
        return self.type
