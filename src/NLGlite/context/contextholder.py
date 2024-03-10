class contextHolder:
    noun = ""
    adjectives = []
    verbs = []
    adverbs = []

    def __init__(self, noun: str):
        self.noun = noun

    def get_noun(self):
        return self.noun

    def get_adjectives(self):
        return self.adjectives

    def get_verbs(self):
        return self.verbs

    def get_adverbs(self):
        return self.adverbs