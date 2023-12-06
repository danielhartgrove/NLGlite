def matchSubject(pattern):
    token_queue.append("DETERMINER")
    while pattern > 0:
        token_queue.append("ADJECTIVE")
        pattern = pattern - 1
    token_queue.append("NOUN")

def matchVerbPhrase(pattern):
    token_queue.append("VERB")
    while pattern > 0:
        token_queue.append("ADVERB")
        if(pattern > 1):
            token_queue.append("COORDINATING_CONJUNCTION")
        pattern = pattern - 1

def matchObject(pattern):
    token_queue.append("DETERMINER")
    while pattern > 0:
        token_queue.append("ADJECTIVE")
        pattern = pattern - 1
    token_queue.append("NOUN")

def matchIndependentClause(pattern):
    matchSubject(generateNumber(0,2))
    if(pattern == 1):
            matchVerbPhrase(generateNumber(0,2))
            token_queue.append("ADJUNCT")
    elif(pattern == 2):
            matchVerbPhrase(generateNumber(0,2))
            token_queue.append("SUBJECT_COMPLIMENT")
    elif(pattern == 3):
            matchVerbPhrase(generateNumber(0,2))
            token_queue.append("OBJECT")
    elif(pattern == 4):
            token_queue.append("INDIRECT_OBJECT")
            token_queue.append("DIRECT_OBJECT")
    elif(pattern == 5):
            matchVerbPhrase(generateNumber(0,2))
            token_queue.append("OBJECT")
            token_queue.append("OBJECT_COMPLIMENT")


def matchDependentClause(pattern):
    matchSubject(generateNumber(0,2))
    matchVerbPhrase(generateNumber(0,2))

def matchCompound(pattern):
    if(pattern == 1):
            matchIndependentClause(generateNumber(1,5))
            token_queue.append(",")
            token_queue.append("COORDINATING_CONJUNCTION")
            matchIndependentClause(generateNumber(1,5))
    elif(pattern == 2):
            matchIndependentClause(generateNumber(1,5))
            token_queue.append(";")
            matchIndependentClause(generateNumber(1,5))
    elif(pattern == 3):
            matchIndependentClause(generateNumber(1,5))
            token_queue.append(";")
            token_queue.append("COORDINATING_CONJUNCTION")
            token_queue.append(",")
            matchIndependentClause(generateNumber(1,5))
    elif(pattern == 4):
            matchIndependentClause(generateNumber(1,5))

def matchComplex(pattern):
    if(pattern == 1):
            token_queue.append("SUBORDINATING_CONJUNCTION")
            matchDependentClause(generateNumber(1,5))
            token_queue.append(",")
            matchIndependentClause(generateNumber(1,2))
    elif(pattern == 2):
            matchDependentClause(generateNumber(1,2))
            token_queue.append(",")
            matchIndependentClause(generateNumber(1,5))
            token_queue.append(",")
            matchDependentClause(generateNumber(1,2))
    elif(pattern == 3):
        matchCompound(generateNumber(1,4))

def matchCompoundComplex(pattern):
    if(pattern == 1):
            matchDependentClause(generateNumber(1,5))
            token_queue.append(",")
            matchCompound(generateNumber(1,4))
    elif(pattern == 2):
            matchCompound(generateNumber(1,4))
            token_queue.append(",")
            matchDependentClause(generateNumber(1,5))
    else:
            matchComplex(generateNumber(1,3))


    