from src.NLGlite.stochastics.stochastics import generate_number


def generate_adjectives(token_queue):
    x = generate_number(0, 15)
    if 5 <= x <= 10:
        token_queue.append("DT")
    elif 11 <= x <= 13:
        token_queue.append("DT")
        token_queue.append("DT")
    elif 14 <= x <= 15:
        token_queue.append("DT")
        token_queue.append("DT")
        token_queue.append("DT")


def match_noun(pattern, token_queue):
    if pattern == 1:
        y = generate_number(1, 2)
        if y == 1:
            token_queue.append("DT")
        generate_adjectives(token_queue)
        token_queue.append("NN")
    elif pattern == 2:
        token_queue.append("NM")
    elif pattern == 3:
        token_queue.append("a")
        generate_adjectives(token_queue)
        token_queue.append("NN")
    elif pattern == 4:
        token_queue.append("PRP")
        generate_adjectives(token_queue)
        token_queue.append("NN")
    elif pattern == 5:
        token_queue.append("PRP$")
        generate_adjectives(token_queue)
        token_queue.append("NN")


def match_complement(pattern, token_queue):
    print("matching complement pattern: ", pattern)
    if pattern == 1:
        token_queue.append("IN")
        match_noun(generate_number(4, 5), token_queue)
    if pattern == 2:
        token_queue.append("a")
        token_queue.append("NN")
    if pattern == 3:
        token_queue.append("JJ")


def match_object(token_queue):
    match_noun(generate_number(3, 5), token_queue)


def match_subject(pattern, token_queue):  # match subject patterns
    if generate_number(1, 3) == 1:
        token_queue.append("PDT")
    if pattern == 1:
        match_noun(generate_number(1, 4), token_queue)
    if pattern == 2:
        match_noun(generate_number(1, 4), token_queue)
        token_queue.append("CC")
        match_noun(generate_number(1, 4), token_queue)


def match_verb_phrase(pattern, token_queue):  # match verb phrase patterns
    print("matching vp pattern: ", pattern)
    if pattern > 1:
        token_queue.append("MD")
    if pattern > 2:
        token_queue.append("VBP")
    if generate_number(1, 10) == 1:
        token_queue.append("RB")

    if generate_number(1, 2) == 1:
        token_queue.append("VB")
    else:
        token_queue.append("VBG")


def match_adjunct(pattern, token_queue):
    print("matching adjunct pattern: ", pattern)
    match_subject(0, token_queue)
    if pattern == 1:
        match_verb_phrase(generate_number(1, 3), token_queue)
        match_complement(generate_number(1, 3), token_queue)
    elif pattern == 2:
        match_verb_phrase(generate_number(1, 3), token_queue)
        match_object(token_queue)
    elif pattern == 3:
        match_object(token_queue)
        match_object(token_queue)
    elif pattern == 4:
        match_verb_phrase(generate_number(1, 3), token_queue)
        match_object(token_queue)
        match_complement(generate_number(1, 3), token_queue)


def match_independent_clause(pattern, token_queue):  # match independent clause patterns
    print("matching independent pattern: ", pattern)
    match_subject(0, token_queue)
    token_queue.append("VB")
    if pattern == 1:
        match_object(token_queue)
    elif pattern == 2:
        token_queue.append("JJ")
    elif pattern == 3:
        token_queue.append("RB")
    elif pattern == 4:
        match_verb_phrase(generate_number(1, 4), token_queue)


def match_question(pattern, token_queue):
    print("matching question: ", pattern)
    # Question word, Auxiliary verb, Subject, Main verb
    token_queue.append("WDT")
    token_queue.append("VB")
    match_subject(0, token_queue)
    token_queue.append("VB")


def match_exclamation(pattern, token_queue):
    print("matching exclamation: ", pattern)
    if pattern == 1:
        token_queue.append("VB")
    elif pattern == 2:
        match_independent_clause(generate_number(1, 4), token_queue)


def match_dependent_clause(pattern, token_queue):  # match dependent clause patterns
    print("matching dependent pattern: ", pattern)
    match_subject(0, token_queue)
    match_verb_phrase(generate_number(1, 3), token_queue)


def match_compound(pattern, token_queue):  # match compound sentence patterns
    print("matching compound pattern: ", pattern)
    if pattern == 1:
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(",")
        token_queue.append("CC")
        match_independent_clause(generate_number(1, 5), token_queue)
    elif pattern == 2:
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(";")
        match_independent_clause(generate_number(1, 5), token_queue)
    elif pattern == 3:
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(";")
        token_queue.append("CC")
        token_queue.append(",")
        match_independent_clause(generate_number(1, 5), token_queue)


def match_complex(pattern, token_queue):  # match complex sentence patterns
    print("matching complex pattern: ", pattern)
    if pattern == 1:
        token_queue.append("IN")
        match_dependent_clause(1, token_queue)
        token_queue.append(",")
        match_independent_clause(generate_number(1, 2), token_queue)
    elif pattern == 2:
        match_dependent_clause(generate_number(1, 2), token_queue)
        token_queue.append(",")
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(",")
        match_dependent_clause(generate_number(1, 2), token_queue)


def match_compound_complex(pattern, token_queue):  # match compound-complex sentence patterns
    print("matching compound complex pattern: ", pattern)
    if pattern == 1:
        match_dependent_clause(generate_number(1, 5), token_queue)
        token_queue.append(",")
        match_compound(generate_number(1, 3), token_queue)
    elif pattern == 2:
        match_compound(generate_number(1, 3), token_queue)
        token_queue.append(",")
        match_dependent_clause(generate_number(1, 5), token_queue)


def match_sentence(pattern, token_queue):
    # data from sentence weighting taken from:
    # https://www.researchgate.net/figure/Grouped-Frequency-Distribution-of-Sentence-Combinations_tbl1_343795196
    if 1 <= pattern <= 21:
        match_complex(generate_number(1, 2), token_queue)
        token_queue.append(".")
    elif 22 == pattern:
        match_compound_complex(generate_number(1, 2), token_queue)
        token_queue.append(".")
    elif 23 <= pattern <= 33:
        match_compound(generate_number(1, 3), token_queue)
        token_queue.append(".")
    elif 34 <= pattern <= 100:
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(".")
    # and the questions and exclamations were approximated.
    elif 101 <= pattern <= 103:
        match_question(generate_number(1, 2), token_queue)
        token_queue.append("?")
    else:
        match_exclamation(generate_number(1, 2), token_queue)
        token_queue.append("!")
