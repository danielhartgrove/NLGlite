import os

import nltk
from nltk.tag import StanfordPOSTagger
from textblob import TextBlob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def tag_nltk(sentence: str):
    """
    Tags a sentence using the NLTK base POS tagger.
    :param sentence: the sentence to be tagged
    :return: a list of tuples, the tuples each contain one word from the sentence and the corresponding tag
    """
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    pos_tags_list = []
    for pair in pos_tags:
        pos_tags_list.append(list(pair))
    return pos_tags_list


def tag_blob(sentence: str):
    """
    Tags a sentence using the TextBlob tagger.
    :param sentence: the sentence to be tagged
    :return: a list of tuples, the tuples each contain one word from the sentence and the corresponding tag
    """
    text_blob = TextBlob(sentence)
    pos_tags_list = [text_blob]
    return pos_tags_list


def tag_core(sentence: str):
    """
    Tags a sentence using the Stanford CoreNLP tagger. Takes longer but slightly more accurate.
    :param sentence: the sentence to be tagged
    :return: a list of tuples, the tuples each contain one word from the sentence and the corresponding tag
    """
    java_path = "C:/Program Files (x86)/Java/jre-1.8/bin/java.exe"
    os.environ["JAVAHOME"] = java_path

    jar = "NLGlite/trainer/stanford-postagger-full-2020-11-17/stanford-postagger.jar"
    model = "NLGlite/trainer/stanford-postagger-full-2020-11-17/models/english-bidirectional-distsim.tagger"

    st = StanfordPOSTagger(model, jar, encoding="utf-8")

    words = nltk.word_tokenize(sentence)
    pos_tags = st.tag(words)
    pos_tags_list = []
    for pair in pos_tags:
        pos_tags_list.append(list(pair))
    return pos_tags_list
