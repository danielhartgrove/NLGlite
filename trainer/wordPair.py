class wordPair:
    word = ""
    w_type = ""

    def __init__(self, word: str, w_type: str):
        self.word = word
        self.type = w_type
    
    def get_word(self):
        return self.word
    
    def get_type(self):
        return self.type
