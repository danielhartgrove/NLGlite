import os

import nltk
from nltk.tag import StanfordPOSTagger
from nltk.tag import StanfordNERTagger
from textblob import TextBlob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# utilises nltk to tokenize the sentence
def tag_nltk(sentence: str):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    pos_tags_list = []
    for pair in pos_tags:
        pos_tags_list.append(list(pair))
    return pos_tags_list


# utilises blob to tokenize the sentence
def tag_blob(sentence: str):
    text_blob = TextBlob(sentence)
    pos_tags_list = [text_blob]
    return pos_tags_list


def tag_core(sentence: str):
    # remove the name things and add a new tag for it
    java_path = "C:/Program Files (x86)/Java/jre-1.8/bin/java.exe"
    os.environ["JAVAHOME"] = java_path

    jar = "src/trainer/stanford-postagger-full-2020-11-17/stanford-postagger.jar"
    model = "src/trainer/stanford-postagger-full-2020-11-17/models/english-bidirectional-distsim.tagger"

    st = StanfordPOSTagger(model, jar, encoding="utf-8")

    words = nltk.word_tokenize(sentence)
    pos_tags = st.tag(words)
    pos_tags_list = []
    for pair in pos_tags:
        pos_tags_list.append(list(pair))
    return pos_tags_list

