import json
import sys

sys.path.append("./grammar")
sys.path.append("./postprocessing")
sys.path.append("./stochastics")
# local packages
from grammar import grammar
from postprocessing import *
from stochastics import *

token_queue = []        #create the initial queue for the tokens
paragraph = []          #create the initial queue for the paragraph

def __main__():
    #generate the structure of the paragraph
    token_queue = []
    while(generateNumber(1,5) < 5):
            grammar.matchCompoundComplex(generateNumber(1,3), token_queue)
            token_queue.append(".") #add a period to the end of the sentence

    #generate the words for the paragraph

    f = open("words_dictionary.json","r")
    data = json.load(f)
    for token in token_queue:
            if token in data:
                    token_list = data[token]
                    paragraph.append(token_list[generateNumber(0,len(token_list)-1)])
                    
    # print the paragraph

    output = ""
    for word in paragraph:
        output = output + word + " "

    #remove spaces before punctuation
    output = output.replace(" .", ".") 
    output = output.replace(" ,", ",") 
    output = output.replace(" ;", ";") 

    output = capitalise_after_char(output, ".")
    output = capitalise_after_char(output, "!")
    output = capitalise_after_char(output, "?")
    
    if(output != ""):
        output = output[0].upper() + output[1:]
    print(output)

__main__()