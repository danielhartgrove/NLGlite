from stochastics.stochastics import generate_number


def match_complement(pattern, token_queue):
    print("matching complement pattern: ", pattern)
    if pattern == 1:
        token_queue.append("IN")
        token_queue.append("PRP$")
        token_queue.append("NN")
    if pattern == 2:
        token_queue.append("IN")
        token_queue.append("PRP")
        token_queue.append("NN")
    if pattern == 3:
        token_queue.append("a")
        token_queue.append("NN")
    if pattern == 4:
        token_queue.append("JJ")


def match_object(pattern, token_queue):
    print("matching object pattern ", pattern)
    if pattern == 1:
        token_queue.append("a")
        token_queue.append("NN")
    if pattern == 2:
        token_queue.append("PRP")
        token_queue.append("NN")
    if pattern == 3:
        token_queue.append("PRP$")
        token_queue.append("NN")
    if pattern == 4:
        token_queue.append("NNS")


def match_subject(pattern, token_queue):  # match subject patterns
    x = generate_number(1, 2)
    if x == 1:
        token_queue.append("DT")
        while pattern > 0:
            token_queue.append("JJ")
            pattern = pattern - 1
        token_queue.append("NN")
    else:
        match_object(generate_number(1, 4), token_queue)


def match_verb_phrase(pattern, token_queue):  # match verb phrase patterns
    print("matching vp pattern: ", pattern)
    token_queue.append("VB")
    while pattern > 0:
        token_queue.append("RB")
        if pattern > 1:
            token_queue.append("CC")
        pattern = pattern - 1


def match_tri_object(pattern, token_queue):  # match object patterns
    print("matching tri object pattern: ", pattern)
    token_queue.append("DT")
    while pattern > 0:
        token_queue.append("JJ")
        pattern = pattern - 1
    token_queue.append("NN")


def match_adjunct(pattern, token_queue):
    print("matching adjunct pattern: ", pattern)
    match_subject(0, token_queue)
    if pattern == 1:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_complement(generate_number(1, 4), token_queue)
    elif pattern == 2:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_object(generate_number(1, 4), token_queue)
    elif pattern == 3:
        match_object(generate_number(1, 4), token_queue)
        match_object(generate_number(1, 4), token_queue)
    elif pattern == 4:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_object(generate_number(1, 4), token_queue)
        match_complement(generate_number(1, 4), token_queue)


def match_independent_clause(pattern, token_queue):  # match independent clause patterns
    print("matching independent pattern: ", pattern)
    match_subject(0, token_queue)
    if pattern == 1:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_adjunct(generate_number(1, 2), token_queue)
    elif pattern == 2:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_complement(generate_number(1, 4), token_queue)
    elif pattern == 3:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_object(generate_number(1, 4), token_queue)
    elif pattern == 4:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_object(generate_number(1, 4), token_queue)
        match_object(generate_number(1, 4), token_queue)
    elif pattern == 5:
        match_verb_phrase(generate_number(1, 2), token_queue)
        match_object(generate_number(1, 4), token_queue)
        match_complement(generate_number(1, 4), token_queue)


def match_dependent_clause(pattern, token_queue):  # match dependent clause patterns
    print("matching dependent pattern: ", pattern)
    match_subject(0, token_queue)
    match_verb_phrase(generate_number(1, 2), token_queue)


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
        match_compound(generate_number(1, 4), token_queue)
    elif pattern == 2:
        match_compound(generate_number(1, 4), token_queue)
        token_queue.append(",")
        match_dependent_clause(generate_number(1, 5), token_queue)


def match_sentence(pattern, token_queue):
    print("\n\n\n")
    if pattern == 1:
        match_complex(generate_number(1, 2), token_queue)
    elif pattern == 2:
        match_compound_complex(generate_number(1, 2), token_queue)
    elif pattern == 3:
        match_compound(generate_number(1, 3), token_queue)
    elif pattern == 4:
        match_independent_clause(generate_number(1, 5), token_queue)
    token_queue.append(".")
