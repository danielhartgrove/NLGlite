from trainer.trainingStructure import TrainingStructure
from trainer.wordPair import wordPair
from trainer.tagger import *
import timeit


# read a file and return the contents
def read_file(filepath):
    data = ""
    # if reading the right type of file
    if filepath.endswith(".txt"):
        f = open(filepath, "r", encoding="utf8")
        # add each line to the data string
        for line in f:
            data += line + " "
        f.close()
        return data
    else:
        # Otherwise we throw an error
        print("Invalid file path.")
        exit(1)  # exit with error code 1


# scrape a file and write the contents to a specified file
def scrape(text: str, output_file_path: str, method: int):
    start = timeit.timeit()
    # get the text from the file
    text = text.rstrip("\\\'\"/`,,:;#+$£^&*()!{}[]¬`\n\t")
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    sentences = text.split(".")
    wordlist = []
    if method == 1:
        for sentence in sentences:
            wordlist += tag_nltk(sentence)
    else:
        for sentence in sentences:
            wordlist += tag_blob(sentence)

    # if the file exists create the trainingStructure from it
    ts = TrainingStructure()
    ts.parse_from(output_file_path)
    # write all word pairs to a file
    x = len(wordlist)
    for i in range(1, x):
        wp1 = wordPair(wordlist[i - 1][0], wordlist[i - 1][1])
        wp2 = wordPair(wordlist[i][0], wordlist[i][1])
        # this will update the word pair's frequency if it already exists in the data structure else set it to 1
        ts.insert(wp1, wp2)
        # dump the data structure to a file
        ts.dump_to_file(output_file_path)
        print(f'{(i/x)*100}% complete', end='\r')
    end = timeit.timeit()
    print("Training Completed in: ", end - start)
