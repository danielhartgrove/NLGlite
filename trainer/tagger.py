import nltk
from textblob import TextBlob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# utilises nltk to tokenize the sentence
def tag_nltk(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags


# utilises blob to tokenize the sentence
def tag_blob(sentence):
    text_blob = TextBlob(sentence)
    pos_tags = text_blob.tags
    return pos_tags
