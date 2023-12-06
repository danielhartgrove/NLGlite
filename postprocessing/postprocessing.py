def capitalise_after_char(input_string, char):
    output_string = ""
    for i in range(0, len(input_string)):
            output_string += input_string[i]
            if input_string[i] == char:
                    output_string += (input_string[i+1].upper())
                    i += 1
    return output_string