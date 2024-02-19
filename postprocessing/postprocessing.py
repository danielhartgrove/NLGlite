def process_sentence_end(input_string):  # capitalise the first letter after a given character, used for ".", "?"
    input_string = input_string.replace(" .", ".")
    input_string = input_string.replace(" ,", ",")
    input_string = input_string.replace(" ?", "?")
    input_string = input_string.replace(" !", "?")
    input_string = input_string.replace(" :", ":")
    input_string = input_string.replace(" ;", ";")
    output_string = input_string
    return output_string
