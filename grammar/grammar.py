from stochastics.stochastics import generate_number


class grammar:
    """
    The grammar class is used to generate a token queue from a grammar. This is a class so that it would be overridable
    should a programmer want to do that.
    """
    token_queue = []

    def __init__(self):
        self.token_queue = []

    def generate(self):
        """
        Starts the generation process. It will generate a token queue for a single sentence.
        :return:
        """
        self.match_sentence(generate_number(1, 103))

    def get_token_queue(self):
        """
        Returns the token queue.
        :return:
        """
        return self.token_queue

    def clear_token_queue(self):
        self.token_queue = []

    def generate_adjectives(self):
        """
        Matches the possible number of adjectives under the rule of three. Will more likely add 0, 1 or 3 adjectives.
        Called before the nouns to describe the nouns.
        :return: None
        """
        x = generate_number(0, 18)
        if 5 <= x <= 10:
            self.token_queue.append("JJ")
        elif 11 <= x <= 13:
            self.token_queue.append("JJ")
            self.token_queue.append("JJ")
        elif 14 <= x <= 18:
            self.token_queue.append("JJ")
            self.token_queue.append("JJ")
            self.token_queue.append("JJ")

    def match_noun(self, pattern):
        """
        Matches the possible token patterns of a noun. Determines the context that the noun is used.
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if pattern == 1:
            y = generate_number(1, 2)
            if y == 1:
                self.token_queue.append("DT")
            self.generate_adjectives()
            self.token_queue.append("NN")
        elif pattern == 2:
            self.token_queue.append("NM")
        elif pattern == 3:
            self.token_queue.append("a")
            self.generate_adjectives()
            self.token_queue.append("NN")
        elif pattern == 4:
            self.token_queue.append("PRP")
            self.generate_adjectives()
            self.token_queue.append("NN")
        elif pattern == 5:
            self.token_queue.append("PRP$")
            self.generate_adjectives()
            self.token_queue.append("NN")

    def match_complement(self, pattern):
        """
        Matches the possible token patterns of an object/subject complement
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if pattern == 1:
            self.token_queue.append("IN")
            self.match_noun(generate_number(4, 5))
        if pattern == 2:
            self.token_queue.append("a")
            self.token_queue.append("NN")
        if pattern == 3:
            self.token_queue.append("JJ")

    def match_object(self):
        """
        Matches the possible token patterns of a sentence object, a wrapper for the match_noun function patterns 3-5
        :return: None
        """
        self.match_noun(generate_number(3, 5))

    def match_subject(self, pattern):
        """
        Matches the possible token patterns of a sentence subject
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if generate_number(1, 3) == 1:
            self.token_queue.append("PDT")
        if pattern == 1:
            self.match_noun(generate_number(1, 4))
        if pattern == 2:
            self.match_noun(generate_number(1, 4))
            self.token_queue.append("CC")
            self.match_noun(generate_number(1, 4))

    def match_verb_phrase(self, pattern):
        """
        Matches the possible token patterns of a verb phrase
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if pattern > 1:
            self.token_queue.append("MD")
        if pattern > 2:
            self.token_queue.append("VBP")
        if generate_number(1, 10) == 1:
            self.token_queue.append("RB")

        if generate_number(1, 2) == 1:
            self.token_queue.append("VB")
        else:
            self.token_queue.append("VBG")

    def match_independent_clause(self, pattern):
        """
        Matches the possible token patterns of an independent clause (simple sentence)
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        self.match_subject(0)
        self.token_queue.append("VB")
        if pattern == 1:
            self.match_object()
        elif pattern == 2:
            self.token_queue.append("JJ")
        elif pattern == 3:
            self.token_queue.append("RB")
        elif pattern == 4:
            self.match_verb_phrase(generate_number(1, 4))

    def match_question(self):
        """
        Matches the possible token patterns of a question
        :return: None
        """
        # Question word, Auxiliary verb, Subject, Main verb
        self.token_queue.append("WDT")
        self.token_queue.append("VB")
        self.match_subject(0)
        self.token_queue.append("VB")

    def match_exclamation(self, pattern):
        """
        Matches the possible token patterns of an exclamation
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if pattern == 1:
            self.token_queue.append("VB")
        elif pattern == 2:
            self.match_independent_clause(generate_number(1, 4))

    def match_dependent_clause(self):
        """
        Matches the dependent clause
        :return: None
        """
        self.match_subject(0)
        self.match_verb_phrase(generate_number(1, 3))

    def match_compound(self, pattern):
        """
        Matches the possible token patterns of a compound sentence
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if pattern == 1:
            self.match_independent_clause(generate_number(1, 5))
            self.token_queue.append(",")
            self.token_queue.append("CC")
            self.match_independent_clause(generate_number(1, 5))
        elif pattern == 2:
            self.match_independent_clause(generate_number(1, 5))
            self.token_queue.append(";")
            self.match_independent_clause(generate_number(1, 5))
        elif pattern == 3:
            self.match_independent_clause(generate_number(1, 5))
            self.token_queue.append(";")
            self.token_queue.append("CC")
            self.token_queue.append(",")
            self.match_independent_clause(generate_number(1, 5))

    def match_complex(self, pattern):
        """
        Matches the possible token patterns of a complex sentence
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if pattern == 1:
            self.token_queue.append("IN")
            self.match_dependent_clause()
            self.token_queue.append(",")
            self.match_independent_clause(generate_number(1, 2))
        elif pattern == 2:
            self.match_dependent_clause()
            self.token_queue.append(",")
            self.match_independent_clause(generate_number(1, 5))
            self.token_queue.append(",")
            self.match_dependent_clause()

    def match_compound_complex(self, pattern):
        """
        Matches the possible token patterns of a compound-complex sentence
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if pattern == 1:
            self.match_dependent_clause()
            self.token_queue.append(",")
            self.match_compound(generate_number(1, 3))
        elif pattern == 2:
            self.match_compound(generate_number(1, 3))
            self.token_queue.append(",")
            self.match_dependent_clause()

    def match_sentence(self, pattern):
        """
        Matches the possible token patterns of a complex sentence; data from sentence weighting taken from:
        # https://www.researchgate.net/figure/Grouped-Frequency-Distribution-of-Sentence-Combinations_tbl1_343795196
        :param pattern: The randomly chosen pattern that will be matched
        :return: None
        """
        if 1 <= pattern <= 21:
            self.match_complex(generate_number(1, 2))
            self.token_queue.append(".")
        elif 22 == pattern:
            self.match_compound_complex(generate_number(1, 2))
            self.token_queue.append(".")
        elif 23 <= pattern <= 33:
            self.match_compound(generate_number(1, 3))
            self.token_queue.append(".")
        elif 34 <= pattern <= 100:
            self.match_independent_clause(generate_number(1, 5))
            self.token_queue.append(".")
        # and the questions and exclamations were approximated.
        elif 101 <= pattern <= 103:
            self.match_question()
            self.token_queue.append("?")
        else:
            self.match_exclamation(generate_number(1, 2))
            self.token_queue.append("!")
