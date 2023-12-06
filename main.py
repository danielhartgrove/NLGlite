import random
import json
# local packages
import grammar
import postprocessing
import stochastics

token_queue = []        #create the initial queue for the tokens
paragraph = []          #create the initial queue for the paragraph

def main():
    #generate the structure of the paragraph
    while(generateNumber(1,5) < 5):
            matchCompoundComplex(generateNumber(1,3))
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
    output = output[0].upper() + output[1:]
    print(output)

main()