from stochastics.stochastics import generate_number


def match_subject(pattern, token_queue):  # match subject patterns
    token_queue.append("DETERMINER")
    while pattern > 0:
        token_queue.append("ADJECTIVE")
        pattern = pattern - 1
    token_queue.append("NOUN")


def match_verb_phrase(pattern, token_queue):  # match verb phrase patterns
    token_queue.append("VERB")
    while pattern > 0:
        token_queue.append("ADVERB")
        if pattern > 1:
            token_queue.append("COORDINATING_CONJUNCTION")
        pattern = pattern - 1


def match_object(pattern, token_queue):  # match object patterns
    token_queue.append("DETERMINER")
    while pattern > 0:
        token_queue.append("ADJECTIVE")
        pattern = pattern - 1
    token_queue.append("NOUN")


def match_independent_clause(pattern, token_queue):  # match independent clause patterns
    match_subject(generate_number(0, 2), token_queue)
    if pattern == 1:
        match_verb_phrase(generate_number(0, 2), token_queue)
        token_queue.append("ADJUNCT")
    elif pattern == 2:
        match_verb_phrase(generate_number(0, 2), token_queue)
        token_queue.append("SUBJECT_COMPLIMENT")
    elif pattern == 3:
        match_verb_phrase(generate_number(0, 2), token_queue)
        token_queue.append("OBJECT")
    elif pattern == 4:
        token_queue.append("INDIRECT_OBJECT")
        token_queue.append("DIRECT_OBJECT")
    elif pattern == 5:
        match_verb_phrase(generate_number(0, 2), token_queue)
        token_queue.append("OBJECT")
        token_queue.append("OBJECT_COMPLIMENT")


def match_dependent_clause(pattern, token_queue):  # match dependent clause patterns
    match_subject(generate_number(0, 2), token_queue)
    match_verb_phrase(generate_number(0, 2), token_queue)


def match_compound(pattern, token_queue):  # match compound sentence patterns
    if pattern == 1:
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(",")
        token_queue.append("COORDINATING_CONJUNCTION")
        match_independent_clause(generate_number(1, 5), token_queue)
    elif pattern == 2:
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(";")
        match_independent_clause(generate_number(1, 5), token_queue)
    elif pattern == 3:
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(";")
        token_queue.append("COORDINATING_CONJUNCTION")
        token_queue.append(",")
        match_independent_clause(generate_number(1, 5), token_queue)
    elif pattern == 4:
        match_independent_clause(generate_number(1, 5), token_queue)


def match_complex(pattern, token_queue):  # match complex sentence patterns
    if pattern == 1:
        token_queue.append("SUBORDINATING_CONJUNCTION")
        match_dependent_clause(generate_number(1, 5), token_queue)
        token_queue.append(",")
        match_independent_clause(generate_number(1, 2), token_queue)
    elif pattern == 2:
        match_dependent_clause(generate_number(1, 2), token_queue)
        token_queue.append(",")
        match_independent_clause(generate_number(1, 5), token_queue)
        token_queue.append(",")
        match_dependent_clause(generate_number(1, 2), token_queue)
    elif pattern == 3:
        match_compound(generate_number(1, 4), token_queue)


def match_compound_complex(pattern, token_queue):  # match compound-complex sentence patterns
    if pattern == 1:
        match_dependent_clause(generate_number(1, 5), token_queue)
        token_queue.append(",")
        match_compound(generate_number(1, 4), token_queue)
    elif pattern == 2:
        match_compound(generate_number(1, 4), token_queue)
        token_queue.append(",")
        match_dependent_clause(generate_number(1, 5), token_queue)
    else:
        match_complex(generate_number(1, 3), token_queue)
